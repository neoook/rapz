import hmac
import hashlib
import requests
import string
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import time
from datetime import datetime
import urllib3
import os
import sys
from concurrent.futures import ThreadPoolExecutor
import base64
import threading
import telebot

# Setup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
TOKEN = os.getenv("BOT_TOKEN") # Ambil dari GitHub Secrets
bot = telebot.TeleBot(TOKEN)

# ================================
# CONFIG & GLOBAL VARS
# ================================
TARGET_TOTAL = 1000
MAX_THREADS = 10
DEFAULT_REGION = "ID"
NAME_PREFIX = "RAPZ"
PASS_PREFIX = "KEMONO"

SUCCESS_COUNTER = 0
IS_GENERATING = False
LOCK = threading.Lock()

BASE_FOLDER = "AW"
ACCOUNTS_FOLDER = os.path.join(BASE_FOLDER, "AW2")
os.makedirs(ACCOUNTS_FOLDER, exist_ok=True)

REGION_LANG = {"ID": "id", "IND": "hi", "ME": "ar", "BR": "pt"}
HEX_KEY = "32656534343831396539623435393838343531343130363762323831363231383734643064356437616639643866376530306331653534373135623764316533"
KEY_HMAC = bytes.fromhex(HEX_KEY)

# ================================
# ENGINES (OB52)
# ================================
def E_AEs(data_hex):
    k = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    v = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(k, AES.MODE_CBC, v)
    return cipher.encrypt(pad(bytes.fromhex(data_hex), 16))

def CrEaTe_ProTo(fields):
    packet = bytearray()
    for f, v in fields.items():
        if isinstance(v, int):
            packet.extend(bytes([(f << 3) | 0]) + bytes([v])) # Simplified for 1-byte ints
        elif isinstance(v, (str, bytes)):
            enc = v.encode() if isinstance(v, str) else v
            packet.extend(bytes([(f << 3) | 2]) + bytes([len(enc)]) + enc)
    return packet

def create_acc():
    try:
        pw = f"{PASS_PREFIX}{random.randint(100,999)}!"
        data = f"password={pw}&client_type=2&source=2&app_id=100067"
        sig = hmac.new(KEY_HMAC, data.encode(), hashlib.sha256).hexdigest()
        reg = requests.post("https://100067.connect.garena.com/oauth/guest/register", 
                           headers={"Authorization": f"Signature {sig}"}, data=data, timeout=10, verify=False).json()
        if 'uid' in reg:
            return {"uid": reg['uid'], "pw": pw, "id": "SUCCESS", "date": datetime.now().strftime("%H:%M:%S")}
    except: return None

# ================================
# BOT COMMANDS
# ================================

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = "🚀 **RAPZ AW BOT ONLINE**\n\n/generate - Start 1000 Accs\n/status - Check Progress\n/stop - Kill Process"
    bot.reply_to(message, welcome, parse_mode="Markdown")

@bot.message_handler(commands=['status'])
def check_status(message):
    percent = (SUCCESS_COUNTER / TARGET_TOTAL) * 100
    status = f"📊 **GEN STATUS**\n━━━━━━━━━━━━━━\n✅ Done: {SUCCESS_COUNTER}/{TARGET_TOTAL}\n📈 Progress: {percent:.1f}%\n🌍 Region: {DEFAULT_REGION}\n━━━━━━━━━━━━━━"
    bot.reply_to(message, status, parse_mode="Markdown")

@bot.message_handler(commands=['generate'])
def start_gen(message):
    global IS_GENERATING, SUCCESS_COUNTER
    if IS_GENERATING:
        bot.reply_to(message, "⚠️ System is already running!")
        return
    
    IS_GENERATING = True
    SUCCESS_COUNTER = 0
    bot.reply_to(message, "🔥 **Engine Started!** Generating 1000 accounts...")
    
    def run_gen():
        global SUCCESS_COUNTER, IS_GENERATING
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as exe:
            while SUCCESS_COUNTER < TARGET_TOTAL and IS_GENERATING:
                acc = create_acc()
                if acc:
                    with LOCK:
                        SUCCESS_COUNTER += 1
                        # Save Data
                        path = os.path.join(ACCOUNTS_FOLDER, f"accounts-{DEFAULT_REGION}.json")
                        old = []
                        if os.path.exists(path):
                            with open(path, 'r') as f: old = json.load(f)
                        old.append(acc)
                        with open(path, 'w') as f: json.dump(old, f, indent=2)
                        
                        # Update status.json for Web
                        with open("status.json", "w") as f:
                            json.dump({"percent": (SUCCESS_COUNTER/TARGET_TOTAL)*100, "current": SUCCESS_COUNTER, "total": TARGET_TOTAL, "last_id": acc['uid'], "last_update": acc['date']}, f)
        
        bot.send_message(message.chat.id, "✅ **1000 Accounts Generated!**")
        IS_GENERATING = False

    threading.Thread(target=run_gen).start()

# Loop bot
if __name__ == "__main__":
    print("🤖 Bot is pooling...")
    bot.infinity_polling()
