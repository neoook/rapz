#!/usr/bin/env python3

# =============================================================================
# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║              ███████╗██╗   ██╗██╗      █████╗ ██╗   ██╗                ║
# ║              ██╔════╝██║   ██║██║     ██╔══██╗██║   ██║                ║
# ║              ███████╗██║   ██║██║     ███████║██║   ██║                ║
# ║              ╚════██║██║   ██║██║     ██╔══██║╚██╗ ██╔╝                ║
# ║              ███████║╚██████╔╝███████╗██║  ██║ ╚████╔╝                 ║
# ║              ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═══╝                  ║
# ║                                                                          ║
# ║                    ╔════════════════════════════╗                       ║
# ║                    ║     X AJAY X SULAV         ║                       ║
# ║                    ║   ULTIMATE GENERATOR v12.0 ║                       ║
# ║                    ╚════════════════════════════╝                       ║
# ║                                                                          ║
# ║              ┌────────────────────────────────────────────┐             ║
# ║              │   THE MOST ADVANCED ACCOUNT GENERATOR      │             ║
# ║              │       WITH ULTIMATE ADMIN CONTROL         │             ║
# ║              └────────────────────────────────────────────┘             ║
# ║                                                                          ║
# ║              ╔════════════════════════════════════════════╗             ║
# ║              ║  CREDIT: SULAV AND AJAY                    ║             ║
# ║              ║  GITHUB: https://github.com/Sulav          ║             ║
# ║              ║  TELEGRAM: @sulav_don1 | @agajayofficial   ║             ║
# ║              ╚════════════════════════════════════════════╝             ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝
# =============================================================================

import hmac
import hashlib
import requests
import string
import random
import json
import codecs
import time
from datetime import datetime
import os
import sys
import base64
import signal
import threading
import psutil
import re
import subprocess
import importlib
import logging
import warnings
import urllib3
import shutil
import inspect
import platform
import getpass

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")

# =============================================================================
# 🛡️ ULTIMATE ANTI-CREDIT & FILENAME PROTECTION SYSTEM
# =============================================================================

class SecurityShield:
    """Ultimate protection system - Cannot be bypassed"""
    
    # REQUIRED FILENAME - MUST MATCH EXACTLY
    REQUIRED_FILENAME = "OB52-FAST-GENRATOR-AGXSULAV.py"
    
    # CREDIT SIGNATURES - MULTIPLE LAYERS
    CREDIT_SIGNATURES = [
        "SULAV", "AJAY", "@sulav_don1", "@agajayofficial",
        "GITHUB: https://github.com/Sulav", "SULAV X AJAY",
        "ULTIMATE ADMIN CONTROL", "OWNER MODE"
    ]
    
    # HIDDEN WATERMARKS
    WATERMARKS = [
        "ULTIMATE_PROTECTION_v12", "SA_GEN_2025", "PROTECTED_BY_SULAV",
        "ADMIN_CONTROL_SYSTEM", "OWNER_VERIFICATION"
    ]
    
    # DUAL PASSWORDS - ENCRYPTED IN ASCII
    # User password: hatbsdke
    _USER_PASSWORD = [83, 85, 76, 65, 86, 88, 65, 74, 65, 89]  # hatbsdke
    
    # Admin password: hatbsdke
    _ADMIN_PASSWORD = [65, 68, 77, 73, 78, 83, 85, 76, 65, 86, 65, 74, 65, 89]  # hatbsdke
    
    # Owner password: hatbsdke
    _OWNER_PASSWORD = [83, 85, 76, 65, 86, 65, 74, 65, 89]  # hatbsdke
    
    @classmethod
    def verify_filename(cls):
        """Verify filename - CANNOT BE CHANGED"""
        current = os.path.basename(__file__)
        return current == cls.REQUIRED_FILENAME
    
    @classmethod
    def verify_credits(cls):
        """Verify credits haven't been tampered with"""
        try:
            with open(__file__, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check all credit signatures
            for sig in cls.CREDIT_SIGNATURES:
                if sig not in content:
                    return False, f"MISSING: {sig}"
            
            # Check watermarks
            for mark in cls.WATERMARKS:
                if mark not in content:
                    return False, f"WATERMARK MISSING"
            
            return True, "✓ INTEGRITY VERIFIED"
        except:
            return False, "VERIFICATION FAILED"
    
    @classmethod
    def verify_password(cls, input_pass):
        """Verify password - returns user level"""
        input_clean = input_pass.strip()
        
        # Check owner password (highest level)
        owner_correct = ''.join(chr(x) for x in cls._OWNER_PASSWORD)
        if input_clean == owner_correct:
            return "OWNER"
        
        # Check admin password
        admin_correct = ''.join(chr(x) for x in cls._ADMIN_PASSWORD)
        if input_clean == admin_correct:
            return "ADMIN"
        
        # Check user password
        user_correct = ''.join(chr(x) for x in cls._USER_PASSWORD)
        if input_clean == user_correct:
            return "USER"
        
        return None
    
    @classmethod
    def show_breach(cls, reason):
        """Show security breach alert"""
        print(f"\n{VISUAL.COLORS['error']}{VISUAL.COLORS['bold']}")
        print(VISUAL.center_text("╔" + "═" * 60 + "╗"))
        print(VISUAL.center_text("║" + " " * 18 + "🚨 SECURITY BREACH 🚨" + " " * 18 + "║"))
        print(VISUAL.center_text("╠" + "═" * 60 + "╣"))
        print(VISUAL.center_text(f"║  {reason:<56} ║"))
        print(VISUAL.center_text("╠" + "═" * 60 + "╣"))
        print(VISUAL.center_text("║  THIS TOOL IS PROTECTED BY SULAV X AJAY     ║"))
        print(VISUAL.center_text("║  DO NOT ATTEMPT TO MODIFY CREDITS            ║"))
        print(VISUAL.center_text("║  OR CHANGE FILENAME!                        ║"))
        print(VISUAL.center_text("╚" + "═" * 60 + "╝"))
        print(f"{VISUAL.COLORS['reset']}")
        time.sleep(10)
        sys.exit(1)

# =============================================================================
# 🎨 ULTIMATE VISUAL MASTER - PROFESSIONAL GRADE
# =============================================================================

class VisualMaster:
    """Professional visual design system - Cinema quality UI"""
    
    # Premium color palette
    COLORS = {
        'primary': '\033[38;5;51m',        # Electric Cyan
        'secondary': '\033[38;5;201m',      # Hot Pink
        'success': '\033[38;5;46m',         # Lime Green
        'error': '\033[38;5;196m',          # Bright Red
        'warning': '\033[38;5;226m',        # Golden Yellow
        'rare': '\033[38;5;165m',            # Royal Purple
        'couple': '\033[38;5;208m',          # Deep Orange
        'info': '\033[38;5;45m',             # Sky Blue
        'highlight': '\033[38;5;226m',       # Bright Yellow
        'dim': '\033[38;5;240m',             # Gray
        'owner': '\033[38;5;196m',           # Bright Red for owner
        'admin': '\033[38;5;202m',            # Orange for admin
        'user': '\033[38;5;46m',              # Green for user
        'reset': '\033[0m',
        'bold': '\033[1m',
    }
    
    # Premium Icons
    ICONS = {
        'success': '✅', 'error': '❌', 'warning': '⚠️', 'info': 'ℹ️',
        'rare': '💎', 'couple': '💑', 'fire': '🔥', 'rocket': '🚀',
        'lock': '🔒', 'key': '🔑', 'shield': '🛡️', 'user': '👤',
        'id': '🆔', 'pass': '🔐', 'time': '⏱️', 'speed': '⚡',
        'target': '🎯', 'folder': '📁', 'stats': '📊', 'globe': '🌍',
        'thread': '🧵', 'crown': '👑', 'star': '⭐', 'heart': '❤️',
        'admin': '👑', 'owner': '💎', 'user_icon': '👤', 'edit': '✏️',
        'save': '💾', 'config': '⚙️', 'custom': '🎨', 'credit': '📝',
    }
    
    # Box drawing characters
    BOX = {
        'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝', 'h': '═', 'v': '║',
    }
    
    @classmethod
    def center_text(cls, text, width=None):
        if width is None:
            width = shutil.get_terminal_size().columns
        return text.center(width)
    
    @classmethod
    def create_box(cls, title=None, width=70, height=1):
        lines = []
        if title:
            top = f"{cls.COLORS['primary']}{cls.BOX['tl']}{cls.BOX['h'] * 2} {title} {cls.BOX['h'] * 2}{cls.BOX['tr']}{cls.COLORS['reset']}"
        else:
            top = f"{cls.COLORS['primary']}{cls.BOX['tl']}{cls.BOX['h'] * (width-2)}{cls.BOX['tr']}{cls.COLORS['reset']}"
        lines.append(top)
        
        for _ in range(height-1):
            lines.append(f"{cls.COLORS['primary']}{cls.BOX['v']}{' ' * (width-2)}{cls.BOX['v']}{cls.COLORS['reset']}")
        
        bottom = f"{cls.COLORS['primary']}{cls.BOX['bl']}{cls.BOX['h'] * (width-2)}{cls.BOX['br']}{cls.COLORS['reset']}"
        lines.append(bottom)
        
        return lines
    
    @classmethod
    def create_panel(cls, title, content, width=None, color='primary'):
        if width is None:
            width = shutil.get_terminal_size().columns - 4
        
        lines = cls.create_box(title, width, len(content.split('\n')) + 2)
        result = []
        
        for i, line in enumerate(lines):
            if i == 0 or i == len(lines) - 1:
                result.append(line)
            else:
                content_line = content.split('\n')[i-1] if i-1 < len(content.split('\n')) else ''
                padding = width - len(content_line) - 4
                result.append(f"{line[0]}{line[1]}{line[2]} {content_line}{' ' * padding} {line[-2]}{line[-1]}")
        
        return '\n'.join(result)
    
    @classmethod
    def create_progress_bar(cls, current, total, width=50):
        percent = current / total if total > 0 else 0
        filled = int(width * percent)
        bar = '█' * filled + '░' * (width - filled)
        return f"{bar} {percent*100:5.1f}%"
    
    @classmethod
    def clear(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @classmethod
    def show_header(cls, user_level="USER"):
        cls.clear()
        width = shutil.get_terminal_size().columns
        
        # Determine color based on user level
        if user_level == "OWNER":
            header_color = cls.COLORS['owner']
            level_text = f"{cls.ICONS['owner']} OWNER MODE {cls.ICONS['owner']}"
        elif user_level == "ADMIN":
            header_color = cls.COLORS['admin']
            level_text = f"{cls.ICONS['admin']} ADMIN MODE {cls.ICONS['admin']}"
        else:
            header_color = cls.COLORS['user']
            level_text = f"{cls.ICONS['user_icon']} USER MODE {cls.ICONS['user_icon']}"
        
        print(header_color + cls.BOX['tl'] + cls.BOX['h'] * (width-2) + cls.BOX['tr'] + cls.COLORS['reset'])
        print(header_color + cls.BOX['v'] + ' ' * (width-2) + cls.BOX['v'] + cls.COLORS['reset'])
        
        titles = [
            "███████╗██╗   ██╗██╗      █████╗ ██╗   ██╗",
            "██╔════╝██║   ██║██║     ██╔══██╗██║   ██║",
            "███████╗██║   ██║██║     ███████║██║   ██║",
            "╚════██║██║   ██║██║     ██╔══██║╚██╗ ██╔╝",
            "███████║╚██████╔╝███████╗██║  ██║ ╚████╔╝ ",
            "╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═══╝  "
        ]
        
        colors = [cls.COLORS['primary'], cls.COLORS['secondary'], cls.COLORS['highlight']]
        
        for i, title in enumerate(titles):
            print(header_color + cls.BOX['v'] + ' ' + colors[i % len(colors)] + cls.COLORS['bold'] + title.center(width-4) + cls.COLORS['reset'] + ' ' + header_color + cls.BOX['v'])
        
        print(header_color + cls.BOX['v'] + ' ' * (width-2) + header_color + cls.BOX['v'] + cls.COLORS['reset'])
        subtitle = f"⚡ X AJAY X SULAV ⚡  {level_text}"
        print(header_color + cls.BOX['v'] + ' ' + cls.COLORS['secondary'] + cls.COLORS['bold'] + subtitle.center(width-4) + cls.COLORS['reset'] + ' ' + header_color + cls.BOX['v'])
        print(header_color + cls.BOX['v'] + ' ' * (width-2) + header_color + cls.BOX['v'] + cls.COLORS['reset'])
        
        features = "  ".join([f"{cls.ICONS['rocket']} GENERATOR", f"{cls.ICONS['fire']} ACTIVATOR", f"{cls.ICONS['rare']} RARE", f"{cls.ICONS['couple']} COUPLES"])
        print(header_color + cls.BOX['v'] + ' ' + cls.COLORS['info'] + features.center(width-4) + cls.COLORS['reset'] + ' ' + header_color + cls.BOX['v'])
        print(header_color + cls.BOX['v'] + ' ' * (width-2) + header_color + cls.BOX['v'] + cls.COLORS['reset'])
        
        credit = "📱 @sulav_don1 | @agajayofficial | 🐙 github.com/Sulav"
        print(header_color + cls.BOX['v'] + ' ' + cls.COLORS['highlight'] + credit.center(width-4) + cls.COLORS['reset'] + ' ' + header_color + cls.BOX['v'])
        print(header_color + cls.BOX['v'] + ' ' * (width-2) + header_color + cls.BOX['v'] + cls.COLORS['reset'])
        print(header_color + cls.BOX['bl'] + cls.BOX['h'] * (width-2) + header_color + cls.BOX['br'] + cls.COLORS['reset'])
        print()

# Initialize Visual Master
VISUAL = VisualMaster()

# =============================================================================
# 🔑 DUAL PASSWORD LOGIN SYSTEM - VISIBLE PASSWORDS
# =============================================================================

def dual_login_system():
    """Dual password login system - returns user level"""
    VISUAL.clear()
    
    width = shutil.get_terminal_size().columns
    
    # Login header
    print(f"{VISUAL.COLORS['primary']}{VISUAL.COLORS['bold']}")
    print(VISUAL.center_text("╔" + "═" * 60 + "╗"))
    print(VISUAL.center_text("║" + " " * 18 + "🔐 ULTIMATE SECURITY SYSTEM 🔐" + " " * 18 + "║"))
    print(VISUAL.center_text("╠" + "═" * 60 + "╣"))
    print(f"{VISUAL.COLORS['reset']}")
    
    print(VISUAL.center_text(f"{VISUAL.COLORS['secondary']}╔{'═'*50}╗{VISUAL.COLORS['reset']}"))
    print(VISUAL.center_text(f"{VISUAL.COLORS['secondary']}║{' '*50}║{VISUAL.COLORS['reset']}"))
    print(VISUAL.center_text(f"{VISUAL.COLORS['secondary']}║{VISUAL.COLORS['warning']}{' '*12}CONTACT FOR PASSWORD{' '*11}{VISUAL.COLORS['secondary']}║{VISUAL.COLORS['reset']}"))
    print(VISUAL.center_text(f"{VISUAL.COLORS['secondary']}║{VISUAL.COLORS['highlight']}{' '*8}📱 @sulav_don1 | @agajayofficial{' '*7}{VISUAL.COLORS['secondary']}║{VISUAL.COLORS['reset']}"))
    print(VISUAL.center_text(f"{VISUAL.COLORS['secondary']}║{' '*50}║{VISUAL.COLORS['reset']}"))
    print(VISUAL.center_text(f"{VISUAL.COLORS['secondary']}╚{'═'*50}╝{VISUAL.COLORS['reset']}"))
    print()
    
    attempts = 3
    while attempts > 0:
        try:
            print(f"{VISUAL.COLORS['highlight']}{VISUAL.COLORS['bold']}➤ PASSWORD IS VISIBLE - YOU CAN SEE WHAT YOU TYPE{VISUAL.COLORS['reset']}")
            password = input(f"{VISUAL.COLORS['highlight']}🔑 Enter password: {VISUAL.COLORS['reset']}")
            
            user_level = SecurityShield.verify_password(password)
            
            if user_level:
                print(f"\n{VISUAL.COLORS['success']}{VISUAL.COLORS['bold']}")
                
                if user_level == "OWNER":
                    print(VISUAL.center_text("👑 OWNER ACCESS GRANTED! WELCOME, CREATOR! 👑"))
                elif user_level == "ADMIN":
                    print(VISUAL.center_text("⚡ ADMIN ACCESS GRANTED! WELCOME, ADMIN! ⚡"))
                else:
                    print(VISUAL.center_text("✅ USER ACCESS GRANTED! WELCOME! ✅"))
                
                print(f"{VISUAL.COLORS['reset']}")
                time.sleep(1)
                return user_level
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"{VISUAL.COLORS['error']}❌ INCORRECT! {attempts} ATTEMPTS REMAINING{VISUAL.COLORS['reset']}")
                else:
                    print(f"{VISUAL.COLORS['error']}{VISUAL.COLORS['bold']}")
                    print(VISUAL.center_text("╔" + "═" * 50 + "╗"))
                    print(VISUAL.center_text("║" + " " * 14 + "🚫 ACCESS DENIED 🚫" + " " * 14 + "║"))
                    print(VISUAL.center_text("╚" + "═" * 50 + "╝"))
                    print(f"{VISUAL.COLORS['reset']}")
                    time.sleep(3)
                    sys.exit(1)
        except KeyboardInterrupt:
            print(f"\n{VISUAL.COLORS['warning']}👋 GOODBYE!{VISUAL.COLORS['reset']}")
            sys.exit(0)

# Run filename and credit checks first
if not SecurityShield.verify_filename():
    SecurityShield.show_breach(f"INVALID FILENAME!\nREQUIRED: {SecurityShield.REQUIRED_FILENAME}")

credit_status, credit_msg = SecurityShield.verify_credits()
if not credit_status:
    SecurityShield.show_breach(credit_msg)

# Run dual login
USER_LEVEL = dual_login_system()

# =============================================================================
# ⚡ FAST REQUIREMENTS INSTALLER
# =============================================================================

def install_requirements():
    """Fast requirements installation"""
    required = ['requests', 'pycryptodome', 'colorama', 'psutil']
    
    print(f"{VISUAL.COLORS['info']}🔧 Checking requirements...{VISUAL.COLORS['reset']}")
    
    for pkg in required:
        try:
            if pkg == 'pycryptodome':
                import Crypto
            elif pkg == 'requests':
                import requests
            elif pkg == 'colorama':
                from colorama import Fore, Style, init
            elif pkg == 'psutil':
                import psutil
            print(f"{VISUAL.COLORS['success']}✅ {pkg} already installed{VISUAL.COLORS['reset']}")
        except ImportError:
            print(f"{VISUAL.COLORS['info']}📦 Installing {pkg}...{VISUAL.COLORS['reset']}")
            try:
                process = subprocess.Popen(
                    [sys.executable, '-m', 'pip', 'install', '--no-cache-dir', pkg, '-q'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                try:
                    stdout, stderr = process.communicate(timeout=30)
                    if process.returncode == 0:
                        print(f"{VISUAL.COLORS['success']}✅ {pkg} installed{VISUAL.COLORS['reset']}")
                except subprocess.TimeoutExpired:
                    process.kill()
                    print(f"{VISUAL.COLORS['warning']}⚠️ {pkg} timeout, continuing...{VISUAL.COLORS['reset']}")
            except:
                print(f"{VISUAL.COLORS['warning']}⚠️ {pkg} install failed, continuing...{VISUAL.COLORS['reset']}")
            time.sleep(1)
    
    try:
        from colorama import Fore, Style, init
        init(autoreset=True)
    except:
        pass
    
    time.sleep(1)

install_requirements()

# Import crypto
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    AES_AVAILABLE = True
except:
    AES_AVAILABLE = False
    def aes_encrypt(data): return data.encode() if isinstance(data, str) else data
    def encrypt_api(data): return data

# =============================================================================
# ⚙️ CONFIGURATION - WITH USER LEVEL CONTROLS
# =============================================================================

class Config:
    """Ultimate configuration with user level controls"""
    
    VERSION = "12.0 ULTIMATE ADMIN CONTROL"
    MAX_THREADS = min(psutil.cpu_count() * 2, 16)
    
    # User level
    USER_LEVEL = USER_LEVEL
    
    # Counters
    SUCCESS = 0
    RARE = 0
    COUPLES = 0
    ACTIVATED = 0
    FAILED = 0
    BIO = 0
    ATTEMPTS = 0
    
    # Locks
    LOCK = threading.Lock()
    FILE_LOCKS = {}
    
    # Flags - controlled by user level
    EXIT = False
    AUTO_ACT = True
    AUTO_BIO = True
    MAX_RETRIES = 5 if USER_LEVEL == "USER" else 10
    
    # Custom generation settings (for admin)
    CUSTOM_NAME_PREFIX = "AJAYXSULAV"
    CUSTOM_PASS_PREFIX = "AJJUBHAIXSULAV"
    CUSTOM_RARITY_THRESHOLD = 3
    CUSTOM_TARGET = 999999999
    
    # Advanced features - only for admin/owner
    if USER_LEVEL in ["ADMIN", "OWNER"]:
        DEBUG_MODE = True
        VERBOSE_LOGGING = True
        MAX_THREADS = min(psutil.cpu_count() * 4, 32)
        CAN_EDIT_CREDITS = True
    else:
        DEBUG_MODE = False
        VERBOSE_LOGGING = False
        CAN_EDIT_CREDITS = False
    
    # Owner only features
    if USER_LEVEL == "OWNER":
        BYPASS_RATE_LIMIT = True
        FORCE_GENERATION = True
        CUSTOM_API_PRIORITY = True
    else:
        BYPASS_RATE_LIMIT = False
        FORCE_GENERATION = False
        CUSTOM_API_PRIORITY = False
    
    # Thresholds
    RARITY_THRESHOLD = 3
    
    # Bio config
    BIO_API_URL = "https://sulav-long-bio-api.vercel.app/bio_upload"
    BIO_TEXT = "[c][B][FF0000]AJAY X SULAV [b][00FF00]IG : AGAJAYOFFICIAL TG - AGAJAYOFFICIAL"
    
    # Region languages
    REGION_LANG = {
        "ME": "ar", "IND": "hi", "ID": "id", "VN": "vi", "TH": "th",
        "BD": "bn", "PK": "ur", "TW": "zh", "CIS": "ru", "SAC": "es", "BR": "pt"
    }
    
    # Activation regions
    ACTIVATION_REGIONS = {
        'IND': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                'get_login_data_url': 'https://client.ind.freefiremobile.com/GetLoginData',
                'client_host': 'client.ind.freefiremobile.com'},
        'BD': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
               'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
               'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
               'client_host': 'clientbp.ggblueshark.com'},
        'PK': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
               'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
               'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
               'client_host': 'clientbp.ggblueshark.com'},
        'ID': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
               'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
               'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
               'client_host': 'clientbp.ggblueshark.com'},
        'TH': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
               'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
               'get_login_data_url': 'https://clientbp.common.ggbluefox.com/GetLoginData',
               'client_host': 'clientbp.common.ggbluefox.com'},
        'VN': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
               'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
               'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
               'client_host': 'clientbp.ggblueshark.com'},
        'ME': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
               'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
               'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
               'client_host': 'clientbp.ggblueshark.com'},
        'BR': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
               'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
               'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
               'client_host': 'clientbp.ggblueshark.com'}
    }
    
    # Main hex key
    MAIN_HEX_KEY = "32656534343831396539623435393838343531343130363762323831363231383734643064356437616639643866376530306331653534373135623764316533"
    
    # Folders
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_FOLDER = os.path.join(CURRENT_DIR, "Sulav")
    TOKENS_FOLDER = os.path.join(BASE_FOLDER, "TOKENS")
    ACCOUNTS_FOLDER = os.path.join(BASE_FOLDER, "ACCOUNTS")
    RARE_ACCOUNTS_FOLDER = os.path.join(BASE_FOLDER, "RARE_ACCOUNTS")
    COUPLES_ACCOUNTS_FOLDER = os.path.join(BASE_FOLDER, "COUPLES_ACCOUNTS")
    GHOST_FOLDER = os.path.join(BASE_FOLDER, "GHOST")
    GHOST_ACCOUNTS_FOLDER = os.path.join(GHOST_FOLDER, "ACCOUNTS")
    GHOST_RARE_FOLDER = os.path.join(GHOST_FOLDER, "RARE_ACCOUNTS")
    GHOST_COUPLES_FOLDER = os.path.join(GHOST_FOLDER, "COUPLES_ACCOUNTS")
    ACTIVATED_FOLDER = os.path.join(BASE_FOLDER, "ACTIVATED")
    FAILED_ACTIVATION_FOLDER = os.path.join(BASE_FOLDER, "FAILED_ACTIVATION")
    CONFIG_FOLDER = os.path.join(BASE_FOLDER, "CONFIG")
    BACKUP_FOLDER = os.path.join(BASE_FOLDER, "BACKUP")
    
    @classmethod
    def create_folders(cls):
        """Create all folders"""
        folders = [
            cls.BASE_FOLDER, cls.TOKENS_FOLDER, cls.ACCOUNTS_FOLDER, cls.RARE_ACCOUNTS_FOLDER,
            cls.COUPLES_ACCOUNTS_FOLDER, cls.GHOST_FOLDER, cls.GHOST_ACCOUNTS_FOLDER,
            cls.GHOST_RARE_FOLDER, cls.GHOST_COUPLES_FOLDER, cls.ACTIVATED_FOLDER,
            cls.FAILED_ACTIVATION_FOLDER, cls.CONFIG_FOLDER, cls.BACKUP_FOLDER
        ]
        
        print(f"{VISUAL.COLORS['info']}📁 Creating folders...{VISUAL.COLORS['reset']}")
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        print(f"{VISUAL.COLORS['success']}✅ Folders ready!{VISUAL.COLORS['reset']}")
        time.sleep(1)

# =============================================================================
# 🔌 API MASTER
# =============================================================================

class APIMaster:
    """Professional API management"""
    
    MAIN_HEX_KEY = Config.MAIN_HEX_KEY
    
    # Base APIs
    API_POOL = [{"id": "100067", "key": bytes.fromhex(Config.MAIN_HEX_KEY), "label": f"API {i:02d} ⚡"} for i in range(1, 8)]
    
    @classmethod
    def init(cls):
        """Initialize API pool"""
        more_ids = ["100068", "100069", "100070", "100071", "100072"]
        for i, api_id in enumerate(more_ids, start=len(cls.API_POOL)+1):
            cls.API_POOL.append({
                "id": api_id,
                "key": bytes.fromhex(cls.MAIN_HEX_KEY),
                "label": f"API {i:02d} ⚡"
            })
        
        variant_keys = [
            "33656534343831396539623435393838343531343130363762323831363231383734643064356437616639643866376530306331653534373135623764316544",
            "34656534343831396539623435393838343531343130363762323831363231383734643064356437616639643866376530306331653534373135623764316555",
        ]
        
        for key_idx, variant_key in enumerate(variant_keys, start=1):
            for i in range(3):
                cls.API_POOL.append({
                    "id": f"10007{key_idx}{i}",
                    "key": bytes.fromhex(variant_key),
                    "label": f"API-V{key_idx}-{i} ⚡"
                })
        
        return len(cls.API_POOL)

API_COUNT = APIMaster.init()

# =============================================================================
# 📝 CREDIT EDITOR SYSTEM (ADMIN ONLY)
# =============================================================================

class CreditEditor:
    """Admin-only credit editing system"""
    
    CREDIT_FILE = os.path.join(Config.CONFIG_FOLDER, "credit_config.json")
    
    @classmethod
    def load_credits(cls):
        """Load current credit configuration"""
        default_credits = {
            "primary_credit": "SULAV AND AJAY",
            "github": "https://github.com/Sulav",
            "telegram1": "@sulav_don1",
            "telegram2": "@agajayofficial",
            "display_name": "SULAV X AJAY",
            "banner_text": "⚡ POWERED BY AJAY X SULAV⚡",
            "footer_text": "👤 CREDIT: SULAV | TELEGRAM: @sulav_don1,@agajayofficial| GITHUB: Sulav",
            "bio_text": "[c][B][FF0000]AJAY X SULAV [b][00FF00]IG : AGAJAYOFFICIAL TG - AGAJAYOFFICIAL",
            "last_modified": datetime.now().isoformat(),
            "modified_by": Config.USER_LEVEL
        }
        
        try:
            if os.path.exists(cls.CREDIT_FILE):
                with open(cls.CREDIT_FILE, 'r') as f:
                    return json.load(f)
            else:
                cls.save_credits(default_credits)
                return default_credits
        except:
            return default_credits
    
    @classmethod
    def save_credits(cls, credits):
        """Save credit configuration"""
        try:
            credits["last_modified"] = datetime.now().isoformat()
            credits["modified_by"] = Config.USER_LEVEL
            with open(cls.CREDIT_FILE, 'w') as f:
                json.dump(credits, f, indent=4)
            return True
        except:
            return False
    
    @classmethod
    def update_banner_text(cls):
        """Update banner text with new credits"""
        credits = cls.load_credits()
        Config.BIO_TEXT = credits.get("bio_text", Config.BIO_TEXT)
        # Update any other global text variables here
        return True
    
    @classmethod
    def backup_current_file(cls):
        """Backup current file before making changes"""
        try:
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
            backup_path = os.path.join(Config.BACKUP_FOLDER, backup_name)
            shutil.copy2(__file__, backup_path)
            return backup_path
        except:
            return None

# =============================================================================
# 🔐 FILE LOCK MANAGEMENT
# =============================================================================

def get_file_lock(filename):
    if filename not in Config.FILE_LOCKS:
        Config.FILE_LOCKS[filename] = threading.Lock()
    return Config.FILE_LOCKS[filename]

# =============================================================================
# 💾 SAFE JSON OPERATIONS
# =============================================================================

def safe_json_save(filepath, data):
    try:
        parent = os.path.dirname(filepath)
        if parent and not os.path.isdir(parent):
            os.makedirs(parent, exist_ok=True)
        
        temp = filepath + '.tmp'
        with open(temp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        if os.path.exists(filepath):
            os.replace(temp, filepath)
        else:
            os.rename(temp, filepath)
        return True
    except:
        return False

def safe_json_load(filepath, default=None):
    try:
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return default if default is not None else []

# =============================================================================
# 🔄 COUPLES DETECTION
# =============================================================================

POTENTIAL_COUPLES = {}
COUPLES_LOCK = threading.Lock()

# =============================================================================
# 🚦 SIGNAL HANDLING
# =============================================================================

EXIT_FLAG = False

def safe_exit(signum=None, frame=None):
    global EXIT_FLAG
    EXIT_FLAG = True
    print(f"\n{VISUAL.COLORS['warning']}🚨 Shutting down...{VISUAL.COLORS['reset']}")
    sys.exit(0)

signal.signal(signal.SIGINT, safe_exit)
signal.signal(signal.SIGTERM, safe_exit)

# =============================================================================
# 🖨️ PRINT FUNCTIONS
# =============================================================================

def print_success(msg): print(f"{VISUAL.COLORS['success']}{VISUAL.COLORS['bold']}✅ {msg}{VISUAL.COLORS['reset']}")
def print_error(msg): print(f"{VISUAL.COLORS['error']}{VISUAL.COLORS['bold']}❌ {msg}{VISUAL.COLORS['reset']}")
def print_warning(msg): print(f"{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⚠️ {msg}{VISUAL.COLORS['reset']}")
def print_info(msg): print(f"{VISUAL.COLORS['info']}ℹ️ {msg}{VISUAL.COLORS['reset']}")
def print_rare(msg): print(f"{VISUAL.COLORS['rare']}{VISUAL.COLORS['bold']}💎 {msg}{VISUAL.COLORS['reset']}")
def print_couple(msg): print(f"{VISUAL.COLORS['couple']}{VISUAL.COLORS['bold']}💑 {msg}{VISUAL.COLORS['reset']}")
def print_activation(msg): print(f"{VISUAL.COLORS['primary']}{VISUAL.COLORS['bold']}🔥 {msg}{VISUAL.COLORS['reset']}")

# Admin/Owner only debug prints
def debug_print(msg):
    if Config.USER_LEVEL in ["ADMIN", "OWNER"] and Config.DEBUG_MODE:
        print(f"{VISUAL.COLORS['dim']}🔍 DEBUG: {msg}{VISUAL.COLORS['reset']}")

# =============================================================================
# 🔐 BIO FUNCTION
# =============================================================================

BIO_SET_COUNTER = 0

def set_account_bio(uid, password, bio_text):
    global BIO_SET_COUNTER
    
    if not Config.AUTO_BIO:
        return False
    
    try:
        # Use custom bio text if available
        credits = CreditEditor.load_credits()
        bio_to_use = credits.get("bio_text", bio_text)
        
        encoded_bio = requests.utils.quote(bio_to_use)
        url = f"{Config.BIO_API_URL}?uid={uid}&pass={password}&bio={encoded_bio}"
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            with Config.LOCK:
                BIO_SET_COUNTER += 1
            return True
    except:
        pass
    return False

# =============================================================================
# 🔐 CRYPTO FUNCTIONS
# =============================================================================

def EnC_Vr(N):
    if N < 0: return b''
    H = []
    while True:
        BesTo = N & 0x7F
        N >>= 7
        if N: BesTo |= 0x80
        H.append(BesTo)
        if not N: break
    return bytes(H)

def CrEaTe_VarianT(field_number, value):
    return EnC_Vr((field_number << 3) | 0) + EnC_Vr(value)

def CrEaTe_LenGTh(field_number, value):
    h = EnC_Vr((field_number << 3) | 2)
    e = value.encode() if isinstance(value, str) else value
    return h + EnC_Vr(len(e)) + e

def CrEaTe_ProTo(fields):
    p = bytearray()
    for f, v in fields.items():
        if isinstance(v, dict):
            p.extend(CrEaTe_LenGTh(f, CrEaTe_ProTo(v)))
        elif isinstance(v, int):
            p.extend(CrEaTe_VarianT(f, v))
        elif isinstance(v, (str, bytes)):
            p.extend(CrEaTe_LenGTh(f, v))
    return p

def E_AEs(Pc):
    if not AES_AVAILABLE:
        return bytes.fromhex(Pc)
    Z = bytes.fromhex(Pc)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    K = AES.new(key, AES.MODE_CBC, iv)
    return K.encrypt(pad(Z, AES.block_size))

def encrypt_api(plain_text):
    if not AES_AVAILABLE:
        return plain_text
    Z = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(Z, AES.block_size)).hex()

def decode_jwt_token(jwt_token):
    try:
        parts = jwt_token.split('.')
        if len(parts) >= 2:
            payload_part = parts[1]
            padding = 4 - len(payload_part) % 4
            if padding != 4:
                payload_part += '=' * padding
            decoded = base64.urlsafe_b64decode(payload_part)
            data = json.loads(decoded)
            account_id = data.get('account_id') or data.get('external_id')
            if account_id:
                return str(account_id)
    except:
        pass
    return "N/A"

# =============================================================================
# 💎 RARITY DETECTION
# =============================================================================

ACCOUNT_RARITY_PATTERNS = {
    "REPEATED_DIGITS_4": [r"(\d)\1{3,}", 3],
    "REPEATED_DIGITS_3": [r"(\d)\1\1(\d)\2\2", 2],
    "SEQUENTIAL_5": [r"(12345|23456|34567|45678|56789)", 4],
    "SEQUENTIAL_4": [r"(0123|1234|2345|3456|4567|45678|5678|6789|9876|8765|7654|6543|5432|4321|3210)", 3],
    "PALINDROME_6": [r"^(\d)(\d)(\d)\3\2\1$", 5],
    "PALINDROME_4": [r"^(\d)(\d)\2\1$", 3],
    "SPECIAL_COMBINATIONS_HIGH": [r"(69|420|1337|007)", 4],
    "SPECIAL_COMBINATIONS_MED": [r"(100|200|300|400|500|666|777|888|999)", 2],
    "QUADRUPLE_DIGITS": [r"(1111|2222|3333|4444|5555|6666|7777|8888|9999|0000)", 4],
    "MIRROR_PATTERN_HIGH": [r"^(\d{2,3})\1$", 3],
    "MIRROR_PATTERN_MED": [r"(\d{2})0\1", 2],
    "GOLDEN_RATIO": [r"1618|0618", 3]
}

def check_account_rarity(account_data):
    account_id = account_data.get("account_id", "")
    if account_id == "N/A" or not account_id:
        return False, None, None, 0

    rarity_score = 0
    detected_patterns = []

    for rarity_type, pattern_data in ACCOUNT_RARITY_PATTERNS.items():
        pattern = pattern_data[0]
        score = pattern_data[1]
        if re.search(pattern, account_id):
            rarity_score += score
            detected_patterns.append(rarity_type)

    account_id_digits = [int(d) for d in account_id if d.isdigit()]

    if len(set(account_id_digits)) == 1 and len(account_id_digits) >= 4:
        rarity_score += 5
        detected_patterns.append("UNIFORM_DIGITS")

    if len(account_id_digits) >= 4:
        differences = [account_id_digits[i+1] - account_id_digits[i] for i in range(len(account_id_digits)-1)]
        if len(set(differences)) == 1:
            rarity_score += 4
            detected_patterns.append("ARITHMETIC_SEQUENCE")

    if len(account_id) <= 8 and account_id.isdigit() and int(account_id) < 1000000:
        rarity_score += 3
        detected_patterns.append("LOW_ACCOUNT_ID")

    # Use custom threshold if set
    threshold = Config.CUSTOM_RARITY_THRESHOLD if Config.USER_LEVEL in ["ADMIN", "OWNER"] else Config.RARITY_THRESHOLD
    
    if rarity_score >= threshold:
        reason = f"Account ID {account_id} - Score: {rarity_score} - Patterns: {', '.join(detected_patterns)}"
        return True, "RARE_ACCOUNT", reason, rarity_score

    return False, None, None, rarity_score

def check_account_couples(account_data, thread_id):
    account_id = account_data.get("account_id", "")
    if account_id == "N/A" or not account_id:
        return False, None, None

    with COUPLES_LOCK:
        for stored_id, stored_data in POTENTIAL_COUPLES.items():
            stored_account_id = stored_data.get('account_id', '')
            couple_found, reason = check_account_couple_patterns(account_id, stored_account_id)
            if couple_found:
                partner_data = stored_data
                del POTENTIAL_COUPLES[stored_id]
                return True, reason, partner_data

        POTENTIAL_COUPLES[account_id] = {
            'uid': account_data.get('uid', ''),
            'account_id': account_id,
            'name': account_data.get('name', ''),
            'password': account_data.get('password', ''),
            'region': account_data.get('region', ''),
            'thread_id': thread_id,
            'timestamp': datetime.now().isoformat()
        }

    return False, None, None

def check_account_couple_patterns(account_id1, account_id2):
    if account_id1 and account_id2 and abs(int(account_id1) - int(account_id2)) == 1:
        return True, f"Sequential Account IDs: {account_id1} & {account_id2}"

    if account_id1 == account_id2[::-1]:
        return True, f"Mirror Account IDs: {account_id1} & {account_id2}"

    if account_id1 and account_id2:
        sum_acc = int(account_id1) + int(account_id2)
        if sum_acc % 1000 == 0 or sum_acc % 10000 == 0:
            return True, f"Complementary sum: {account_id1} + {account_id2} = {sum_acc}"

    love_numbers = ['520', '521', '1314', '3344']
    for love_num in love_numbers:
        if love_num in account_id1 and love_num in account_id2:
            return True, f"Both contain love number: {love_num}"

    return False, None

def print_rarity_found(account_data, rarity_type, reason, rarity_score):
    print(f"\n{VISUAL.COLORS['rare']}{VISUAL.COLORS['bold']}╔══════════════════════════════════════════════╗{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}{VISUAL.COLORS['bold']}║  💎 RARE ACCOUNT FOUND!                      ║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}{VISUAL.COLORS['bold']}╠══════════════════════════════════════════════╣{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}║  🎯 Type: {rarity_type:<30}║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}║  ⭐ Score: {rarity_score:<29}║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}║  👤 Name: {account_data['name']:<30}║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}║  🆔 UID: {account_data['uid']:<30}║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}║  🎮 Account ID: {account_data.get('account_id', 'N/A'):<23}║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}║  📝 Reason: {reason:<28}║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['rare']}{VISUAL.COLORS['bold']}╚══════════════════════════════════════════════╝{VISUAL.COLORS['reset']}\n")

def print_couples_found(account1, account2, reason):
    print(f"\n{VISUAL.COLORS['couple']}{VISUAL.COLORS['bold']}╔══════════════════════════════════════════════╗{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['couple']}{VISUAL.COLORS['bold']}║  💑 COUPLES ACCOUNT FOUND!                   ║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['couple']}{VISUAL.COLORS['bold']}╠══════════════════════════════════════════════╣{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['couple']}║  📝 Reason: {reason:<36}║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['couple']}║  👤 Account 1: {account1['name']} (ID: {account1.get('account_id', 'N/A')})║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['couple']}║  👤 Account 2: {account2['name']} (ID: {account2.get('account_id', 'N/A')})║{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['couple']}{VISUAL.COLORS['bold']}╚══════════════════════════════════════════════╝{VISUAL.COLORS['reset']}\n")

# =============================================================================
# 🔑 ACCOUNT GENERATION HELPERS
# =============================================================================

def generate_exponent_number():
    exponent_digits = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
    number = random.randint(1, 99999)
    number_str = f"{number:05d}"
    return ''.join(exponent_digits[digit] for digit in number_str)

def generate_random_name():
    """Generate random name with custom prefix for admin"""
    if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
        base = Config.CUSTOM_NAME_PREFIX
    else:
        base = "AJAYXSULAV"
    return f"{base[:7]}{generate_exponent_number()}"

def generate_custom_password():
    """Generate random password with custom prefix for admin"""
    if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
        prefix = Config.CUSTOM_PASS_PREFIX
    else:
        prefix = "AJJUBHAIXSULAV"
    characters = string.ascii_uppercase + string.digits
    random_part = ''.join(random.choice(characters) for _ in range(5))
    return f"{prefix}{random_part}"

def encode_string(original):
    keystream = [0x30, 0x30, 0x30, 0x32, 0x30, 0x31, 0x37, 0x30, 0x30, 0x30, 0x30, 0x30, 0x32, 0x30, 0x31, 0x37,
                 0x30, 0x30, 0x30, 0x30, 0x30, 0x32, 0x30, 0x31, 0x37, 0x30, 0x30, 0x30, 0x30, 0x30, 0x32, 0x30]
    encoded = ""
    for i in range(len(original)):
        orig_byte = ord(original[i])
        key_byte = keystream[i % len(keystream)]
        result_byte = orig_byte ^ key_byte
        encoded += chr(result_byte)
    return {"open_id": original, "field_14": encoded}

def to_unicode_escaped(s):
    return ''.join(c if 32 <= ord(c) <= 126 else '\\u{:04x}'.format(ord(c)) for c in s)

def smart_delay():
    time.sleep(random.uniform(0.1, 0.3))

# =============================================================================
# ⚡ AUTO ACTIVATOR
# =============================================================================

class AutoActivator:
    def __init__(self, max_workers=5, turbo_mode=True):
        self.key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
        self.iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
        self.max_workers = max_workers
        self.turbo_mode = turbo_mode
        self.session = requests.Session()
        self.stop_execution = False

    def encrypt_api(self, plain_text):
        if not AES_AVAILABLE:
            return plain_text
        try:
            plain_text = bytes.fromhex(plain_text)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
            return cipher_text.hex()
        except:
            return None

    def parse_my_message(self, serialized_data):
        try:
            text = serialized_data.decode('utf-8', errors='ignore')
            jwt_start = text.find("eyJ")
            if jwt_start != -1:
                jwt_token = text[jwt_start:]
                second_dot = jwt_token.find(".", jwt_token.find(".") + 1)
                if second_dot != -1:
                    jwt_token = jwt_token[:second_dot + 44]
                    return jwt_token, None, None
            return None, None, None
        except:
            return None, None, None

    def guest_token(self, uid, password, region='IND'):
        if self.stop_execution:
            return None, None

        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['guest_url']
        data = {
            "uid": f"{uid}",
            "password": f"{password}",
            "response_type": "token",
            "client_type": "2",
            "client_secret": Config.MAIN_HEX_KEY,
            "client_id": "100067",
        }
        for attempt in range(3):
            try:
                timeout = 8 if self.turbo_mode else 15
                response = self.session.post(url, data=data, timeout=timeout, verify=False)
                if response.status_code == 200:
                    data_json = response.json()
                    return data_json.get('access_token'), data_json.get('open_id')
                elif response.status_code == 429:
                    time.sleep(2 ** attempt)
            except:
                pass
            if attempt < 2:
                time.sleep(1)
        return None, None

    def major_login(self, access_token, open_id, region='IND'):
        if self.stop_execution:
            return None

        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['major_login_url']
        headers = {
            'X-Unity-Version': '2018.4.11f1',
            'ReleaseVersion': 'OB52',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-GA': 'v1 1',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
            'Host': 'loginbp.ggblueshark.com',
            'Connection': 'Keep-Alive',
        }
        payload_template = bytes.fromhex(
            '1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e3132302e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e32473438482f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c203480019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a012b476f6f676c657c31663361643662372d636562342d343934622d383730622d623164616364373230393131a2010c3139372e312e31322e313335aa0102656eb201203939366136323964626364623339363462653662363937386635643831346462ba010134c2010848616e6468656c64ea014066663930633037656239383135616633306134336234613966363031393531366530653463373033623434303932353136643064656661346365663531663261f00101ca0207416e64726f6964d2020457494649ca03203734323862323533646566633136343031386336303461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e667265656669726574682d312f6c69622f61726de00401ea044832303837663631633139663537663261663465376665666630623234643964397c2f646174612f6170702f636f6d2e6474732e667265656669726574682d312f626173652e61706bf00403f804018a050233329a050a32303139313138363933b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b71734854394748625876574c6668437950416c52526873626d43676542557562555551317375746d525536634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830663935542b6456593d8806019006019a060134a2060134'
        )
        OLD_OPEN_ID = b"996a629dbcdb3964be6b6978f5d814db"
        OLD_ACCESS_TOKEN = b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a"
        payload = payload_template.replace(OLD_OPEN_ID, open_id.encode())
        payload = payload.replace(OLD_ACCESS_TOKEN, access_token.encode())
        encrypted_payload = self.encrypt_api(payload.hex())
        if not encrypted_payload:
            return None
        final_payload = bytes.fromhex(encrypted_payload)
        for attempt in range(3):
            try:
                timeout = 12 if self.turbo_mode else 18
                response = self.session.post(url, headers=headers, data=final_payload, verify=False, timeout=timeout)
                if response.status_code == 200 and len(response.content) > 0:
                    return response.content
            except:
                pass
            if attempt < 2:
                time.sleep(1)
        return None

    def GET_LOGIN_DATA(self, JWT_TOKEN, access_token, region='IND'):
        if self.stop_execution:
            return False

        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['get_login_data_url']
        client_host = region_config['client_host']

        try:
            token_payload_base64 = JWT_TOKEN.split('.')[1]
            token_payload_base64 += '=' * ((4 - len(token_payload_base64) % 4) % 4)
            decoded_payload = base64.urlsafe_b64decode(token_payload_base64).decode('utf-8')
            decoded_payload = json.loads(decoded_payload)
            NEW_EXTERNAL_ID = decoded_payload['external_id']
            SIGNATURE_MD5 = decoded_payload['signature_md5']
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            payload = bytes.fromhex("1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e3132302e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e32473438482f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c203480019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a012b476f6f676c657c31663361643662372d636562342d343934622d383730622d623164616364373230393131a2010c3139372e312e31322e313335aa0102656eb201203939366136323964626364623339363462653662363937386635643831346462ba010134c2010848616e6468656c64ea014066663930633037656239383135616633306134336234613966363031393531366530653463373033623434303932353136643064656661346365663531663261f00101ca0207416e64726f6964d2020457494649ca03203734323862323533646566633136343031386336303461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e667265656669726574682d312f6c69622f61726de00401ea044832303837663631633139663537663261663465376665666630623234643964397c2f646174612f6170702f636f6d2e6474732e667265656669726574682d312f626173652e61706bf00403f804018a050233329a050a32303139313138363933b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b71734854394748625876574c6668437950416c52526873626d43676542557562555551317375746d525536634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830663935542b6456593d8806019006019a060134a2060134")
            payload = payload.replace(b"2025-07-30 11:02:51", now.encode())
            payload = payload.replace(b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a", access_token.encode("UTF-8"))
            payload = payload.replace(b"996a629dbcdb3964be6b6978f5d814db", NEW_EXTERNAL_ID.encode("UTF-8"))
            payload = payload.replace(b"7428b253defc164018c604a1ebbfebdf", SIGNATURE_MD5.encode("UTF-8"))
            PAYLOAD = payload.hex()
            PAYLOAD = self.encrypt_api(PAYLOAD)
            if not PAYLOAD:
                return False
            final_payload = bytes.fromhex(PAYLOAD)
        except:
            return False

        headers = {
            'Expect': '100-continue',
            'Authorization': f'Bearer {JWT_TOKEN}',
            'X-Unity-Version': '2018.4.11f1',
            'X-GA': 'v1 1',
            'ReleaseVersion': 'OB52',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)',
            'Host': client_host,
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        for attempt in range(2):
            try:
                timeout = 8 if self.turbo_mode else 12
                response = self.session.post(url, headers=headers, data=final_payload, verify=False, timeout=timeout)
                if response.status_code == 200:
                    return True
            except:
                pass
            if attempt < 1:
                time.sleep(1)
        return False

    def activate_account(self, account_data):
        """Activate a single account"""
        uid = account_data['uid']
        password = account_data['password']
        region = account_data.get('region', 'IND')

        if region not in Config.ACTIVATION_REGIONS:
            region = 'IND'

        access_token, open_id = self.guest_token(uid, password, region)
        if not access_token or not open_id:
            return False

        major_login_response = self.major_login(access_token, open_id, region)
        if not major_login_response:
            return False

        jwt_token, key, iv = self.parse_my_message(major_login_response)
        if not jwt_token:
            return False

        activation_success = self.GET_LOGIN_DATA(jwt_token, access_token, region)
        return activation_success

# Global activator
auto_activator = AutoActivator(max_workers=5, turbo_mode=True)

# =============================================================================
# 👤 ACCOUNT CREATION FUNCTIONS
# =============================================================================

def create_acc(region, session, is_ghost=False):
    if EXIT_FLAG:
        return None
    
    # Admin/Owner get more retries
    max_attempts = Config.MAX_RETRIES
    
    for attempt in range(max_attempts):
        try:
            current_api = random.choice(APIMaster.API_POOL)
            app_id = current_api["id"]
            secret_key = current_api["key"]

            password = generate_custom_password()
            data = f"password={password}&client_type=2&source=2&app_id={app_id}"
            message = data.encode('utf-8')
            signature = hmac.new(secret_key, message, hashlib.sha256).hexdigest()

            url = f"https://{app_id}.connect.garena.com/oauth/guest/register"
            headers = {
                "User-Agent": "GarenaMSDK/4.0.19P8(ASUS_Z01QD ;Android 12;en;US;)",
                "Authorization": "Signature " + signature,
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip",
                "Connection": "Keep-Alive"
            }

            debug_print(f"API Attempt {attempt+1}: {current_api['label']}")
            
            response = session.post(url, headers=headers, data=data, timeout=15, verify=False)
            
            if response.status_code == 200:
                response_json = response.json()
                if 'uid' in response_json:
                    uid = response_json['uid']
                    print_success(f"Guest via {current_api['label']}: {uid}")
                    smart_delay()
                    with Config.LOCK:
                        Config.ATTEMPTS += 1
                    return token(uid, password, region, current_api, session, is_ghost)
            elif response.status_code == 429:
                wait_time = 2 ** attempt
                debug_print(f"Rate limited, waiting {wait_time}s")
                time.sleep(wait_time)
        except Exception as e:
            debug_print(f"API error: {str(e)[:30]}")
        
        smart_delay()
    
    return None

def token(uid, password, region, api_config, session, is_ghost=False):
    if EXIT_FLAG:
        return None
    
    try:
        app_id = api_config["id"]
        secret_key = api_config["key"]

        url = f"https://{app_id}.connect.garena.com/oauth/guest/token/grant"
        headers = {
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": f"{app_id}.connect.garena.com",
            "User-Agent": "GarenaMSDK/4.0.19P8(ASUS_Z01QD ;Android 12;en;US;)",
        }
        body = {
            "uid": uid,
            "password": password,
            "response_type": "token",
            "client_type": "2",
            "client_secret": secret_key,
            "client_id": app_id
        }

        debug_print(f"Getting token for {uid}")
        response = session.post(url, headers=headers, data=body, timeout=15, verify=False)
        
        if response.status_code == 200:
            response_json = response.json()
            if 'open_id' in response_json:
                open_id = response_json['open_id']
                access_token = response_json["access_token"]

                result = encode_string(open_id)
                field = to_unicode_escaped(result['field_14'])
                field = codecs.decode(field, 'unicode_escape').encode('latin1')
                print_success(f"Token granted for: {uid}")
                smart_delay()
                with Config.LOCK:
                    Config.ATTEMPTS += 1
                return Major_Regsiter(access_token, open_id, field, uid, password, region, api_config, session, is_ghost)
        return None
    except Exception as e:
        debug_print(f"Token error: {str(e)[:30]}")
        smart_delay()
        return None

def select_veteran(region, jwt_token, session):
    try:
        if region.upper() in ["ME", "TH"]:
            url = "https://clientbp.common.ggbluefox.com/ActiveBeginnerGuide"
        else:
            url = "https://clientbp.ggblueshark.com/ActiveBeginnerGuide"

        fields = {1: 3}
        proto_data = CrEaTe_ProTo(fields)
        encrypted_data = encrypt_api(proto_data.hex())
        payload = bytes.fromhex(encrypted_data)

        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; M2101K7AG Build/SKQ1.210908.001)",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded",
            'Expect': "100-continue",
            'Authorization': f"Bearer {jwt_token}",
            'X-Unity-Version': "2018.4.11f1",
            'X-GA': "v1 1",
            'ReleaseVersion': "OB52"
        }

        response = session.post(url, data=payload, headers=headers, verify=False, timeout=15)
        return response.status_code == 200
    except:
        return False

def Major_Regsiter(access_token, open_id, field, uid, password, region, api_config, session, is_ghost=False):
    if EXIT_FLAG:
        return None
    
    try:
        if is_ghost:
            url = "https://loginbp.ggblueshark.com/MajorRegister"
        else:
            if region.upper() in ["ME", "TH"]:
                url = "https://loginbp.common.ggbluefox.com/MajorRegister"
            else:
                url = "https://loginbp.ggblueshark.com/MajorRegister"

        name = generate_random_name()

        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": "Bearer",   
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Expect": "100-continue",
            "Host": "loginbp.ggblueshark.com" if is_ghost or region.upper() not in ["ME", "TH"] else "loginbp.common.ggbluefox.com",
            "ReleaseVersion": "OB52",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
            "X-GA": "v1 1",
            "X-Unity-Version": "2018.4."
        }

        lang_code = "pt" if is_ghost else Config.REGION_LANG.get(region.upper(), "en")
        payload = {
            1: name,
            2: access_token,
            3: open_id,
            5: 102000007,
            6: 4,
            7: 1,
            13: 1,
            14: field,
            15: lang_code,
            16: 1,
            17: 1
        }

        payload_bytes = CrEaTe_ProTo(payload)
        encrypted_payload = E_AEs(payload_bytes.hex())

        debug_print(f"Registering account: {name}")
        response = session.post(url, headers=headers, data=encrypted_payload, verify=False, timeout=15)

        if response.status_code == 200:
            print_success(f"MajorRegister successful: {name}")

            login_result = perform_major_login(uid, password, access_token, open_id, region, session, is_ghost)
            account_id = login_result.get("account_id", "N/A")
            jwt_token = login_result.get("jwt_token", "")

            if not is_ghost and jwt_token and account_id != "N/A" and region.upper() != "BR":
                region_bound = force_region_binding(region, jwt_token, session)
                if region_bound:
                    print_success(f"Region {region} bound successfully!")

                veteran_selected = select_veteran(region, jwt_token, session)
                if veteran_selected:
                    print_success(f"🔥 Veteran Mode Selected")

            return {
                "uid": uid, 
                "password": password, 
                "name": name, 
                "region": "GHOST" if is_ghost else region, 
                "status": "success",
                "account_id": account_id,
                "jwt_token": jwt_token,
                "api_label": api_config["label"]
            }
        return None
    except Exception as e:
        debug_print(f"Register error: {str(e)[:30]}")
        smart_delay()
        return None

def perform_major_login(uid, password, access_token, open_id, region, session, is_ghost=False):
    try:
        lang = "pt" if is_ghost else Config.REGION_LANG.get(region.upper(), "en")

        payload_parts = [
            b'\x1a\x132025-08-30 05:19:21"\tfree fire(\x01:\x081.114.13B2Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)J\x08HandheldR\nATM MobilsZ\x04WIFI`\xb6\nh\xee\x05r\x03300z\x1fARMv7 VFPv3 NEON VMH | 2400 | 2\x80\x01\xc9\x0f\x8a\x01\x0fAdreno (TM) 640\x92\x01\rOpenGL ES 3.2\x9a\x01+Google|dfa4ab4b-9dc4-454e-8065-e70c733fa53f\xa2\x01\x0e105.235.139.91\xaa\x01\x02',
            lang.encode("ascii"),
            b'\xb2\x01 1d8ec0240ede109973f3321b9354b44d\xba\x01\x014\xc2\x01\x08Handheld\xca\x01\x10Asus ASUS_I005DA\xea\x01@afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390\xf0\x01\x01\xca\x02\nATM Mobils\xd2\x02\x04WIFI\xca\x03 7428b253defc164018c604a1ebbfebdf\xe0\x03\xa8\x81\x02\xe8\x03\xf6\xe5\x01\xf0\x03\xaf\x13\xf8\x03\x84\x07\x80\x04\xe7\xf0\x01\x88\x04\xa8\x81\x02\x90\x04\xe7\xf0\x01\x98\x04\xa8\x81\x02\xc8\x04\x01\xd2\x04=/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/lib/arm\xe0\x04\x01\xea\x04_2087f61c19f57f2af4e7feff0b24d9d9|/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/base.apk\xf0\x04\x03\xf8\x04\x01\x8a\x05\x0232\x9a\x05\n2019118692\xb2\x05\tOpenGLES2\xb8\x05\xff\x7f\xc0\x05\x04\xe0\x05\xf3F\xea\x05\x07android\xf2\x05pKqsHT5ZLWrYljNb5Vqh//yFRlaPHSO9NWSQsVvOmdhEEn7W+VHNUK+Q+fduA3ptNrGB0Ll0LRz3WW0jOwesLj6aiU7sZ40p8BfUE/FI/jzSTwRe2\xf8\x05\xfb\xe4\x06\x88\x06\x01\x90\x06\x01\x9a\x06\x014\xa2\x06\x014\xb2\x06"GQ@O\x00\x0e^\x00D\x06UA\x0ePM\r\x13hZ\x07T\x06\x0cm\\V\x0ejYV;\x0bU5'
        ]

        payload = b''.join(payload_parts)

        if is_ghost:
            url = "https://loginbp.ggblueshark.com/MajorLogin"
        elif region.upper() in ["ME", "TH"]:
            url = "https://loginbp.common.ggbluefox.com/MajorLogin"
        else:
            url = "https://loginbp.ggblueshark.com/MajorLogin"

        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": "Bearer",
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Expect": "100-continue",
            "Host": "loginbp.ggblueshark.com" if is_ghost or region.upper() not in ["ME", "TH"] else "loginbp.common.ggbluefox.com",
            "ReleaseVersion": "OB52",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
            "X-GA": "v1 1",
            "X-Unity-Version": "2018.4.11f1"
        }

        data = payload
        data = data.replace(b'afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390', access_token.encode())
        data = data.replace(b'1d8ec0240ede109973f3321b9354b44d', open_id.encode())

        d = encrypt_api(data.hex())
        final_payload = bytes.fromhex(d)

        debug_print(f"Performing major login for {uid}")
        response = session.post(url, headers=headers, data=final_payload, verify=False, timeout=15)

        if response.status_code == 200 and len(response.text) > 10:
            jwt_start = response.text.find("eyJ")
            if jwt_start != -1:
                jwt_token = response.text[jwt_start:]
                second_dot = jwt_token.find(".", jwt_token.find(".") + 1)
                if second_dot != -1:
                    jwt_token = jwt_token[:second_dot + 44]
                    account_id = decode_jwt_token(jwt_token)
                    return {"account_id": account_id, "jwt_token": jwt_token}

        return {"account_id": "N/A", "jwt_token": ""}
    except:
        return {"account_id": "N/A", "jwt_token": ""}

def force_region_binding(region, jwt_token, session):
    try:
        if region.upper() in ["ME", "TH"]:
            url = "https://loginbp.common.ggbluefox.com/ChooseRegion"
        else:
            url = "https://loginbp.ggblueshark.com/ChooseRegion"

        region_code = "RU" if region.upper() == "CIS" else region.upper()

        fields = {1: region_code}
        proto_data = CrEaTe_ProTo(fields)
        encrypted_data = encrypt_api(proto_data.hex())
        payload = bytes.fromhex(encrypted_data)

        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; M2101K7AG Build/SKQ1.210908.001)",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded",
            'Expect': "100-continue",
            'Authorization': f"Bearer {jwt_token}",
            'X-Unity-Version': "2018.4.11f1",
            'X-GA': "v1 1",
            'ReleaseVersion': "OB52"
        }

        response = session.post(url, data=payload, headers=headers, verify=False, timeout=15)
        return response.status_code == 200
    except:
        return False

# =============================================================================
# 🔥 AUTO ACTIVATION INTEGRATION
# =============================================================================

ACTIVATED_COUNTER = 0
FAILED_ACTIVATION_COUNTER = 0

def auto_activate_account(account_data):
    """Automatically activate account after generation"""
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER

    if not Config.AUTO_ACT:
        return False

    try:
        print_activation(f"Auto-activating: {account_data['uid']}")

        activator = AutoActivator(max_workers=1, turbo_mode=True)
        success = activator.activate_account(account_data)

        with Config.LOCK:
            if success:
                ACTIVATED_COUNTER += 1
                print_activation(f"✅ Activated! Total: {ACTIVATED_COUNTER}")
                save_activated_account(account_data)
            else:
                FAILED_ACTIVATION_COUNTER += 1
                print_error(f"❌ Failed! Total failed: {FAILED_ACTIVATION_COUNTER}")
                save_failed_activation(account_data)

        return success
    except Exception as e:
        print_error(f"Activation error: {e}")
        with Config.LOCK:
            FAILED_ACTIVATION_COUNTER += 1
        return False

# =============================================================================
# 💾 SAVE FUNCTIONS
# =============================================================================

def save_activated_account(account_data):
    try:
        region = account_data.get('region', 'UNKNOWN')
        filename = os.path.join(Config.ACTIVATED_FOLDER, f"activated-{region}.json")

        entry = {
            'uid': account_data['uid'],
            'password': account_data['password'],
            'account_id': account_data.get('account_id', 'N/A'),
            'name': account_data['name'],
            'region': region,
            'activated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        file_lock = get_file_lock(filename)
        with file_lock:
            accounts_list = safe_json_load(filename, [])
            accounts_list.append(entry)
            safe_json_save(filename, accounts_list)
    except:
        pass

def save_failed_activation(account_data):
    try:
        region = account_data.get('region', 'UNKNOWN')
        filename = os.path.join(Config.FAILED_ACTIVATION_FOLDER, f"failed-{region}.json")

        entry = {
            'uid': account_data['uid'],
            'password': account_data['password'],
            'account_id': account_data.get('account_id', 'N/A'),
            'name': account_data['name'],
            'region': region,
            'failed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        file_lock = get_file_lock(filename)
        with file_lock:
            accounts_list = safe_json_load(filename, [])
            accounts_list.append(entry)
            safe_json_save(filename, accounts_list)
    except:
        pass

def save_jwt_token(account_data, jwt_token, region, is_ghost=False):
    try:
        if is_ghost:
            token_filename = os.path.join(Config.GHOST_FOLDER, "tokens-ghost.json")
        else:
            token_filename = os.path.join(Config.TOKENS_FOLDER, f"tokens-{region}.json")

        token_entry = {
            'uid': account_data["uid"],
            'account_id': account_data.get("account_id", "N/A"),
            'jwt_token': jwt_token,
            'name': account_data["name"],
            'password': account_data["password"],
            'date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'region': "Sulav" if is_ghost else region,
            'thread_id': account_data.get('thread_id', 'N/A')
        }

        file_lock = get_file_lock(token_filename)
        with file_lock:
            tokens_list = safe_json_load(token_filename, [])
            existing_ids = [t.get('account_id') for t in tokens_list]
            if account_data.get("account_id", "N/A") not in existing_ids:
                tokens_list.append(token_entry)
                safe_json_save(token_filename, tokens_list)
                return True
        return False
    except:
        return False

def save_normal_account(account_data, region, is_ghost=False):
    try:
        if is_ghost:
            account_filename = os.path.join(Config.GHOST_ACCOUNTS_FOLDER, "ghost.json")
        else:
            account_filename = os.path.join(Config.ACCOUNTS_FOLDER, f"accounts-{region}.json")

        account_entry = {
            'uid': account_data["uid"],
            'password': account_data["password"],
            'account_id': account_data.get("account_id", "N/A"),
            'name': account_data["name"],
            'region': "Sulav" if is_ghost else region,
            'date_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'thread_id': account_data.get('thread_id', 'N/A')
        }

        file_lock = get_file_lock(account_filename)
        with file_lock:
            accounts_list = safe_json_load(account_filename, [])
            existing_ids = [acc.get('account_id') for acc in accounts_list]
            if account_data.get("account_id", "N/A") not in existing_ids:
                accounts_list.append(account_entry)
                safe_json_save(account_filename, accounts_list)
                return True
        return False
    except:
        return False

def save_rare_account(account_data, rarity_type, reason, rarity_score, is_ghost=False):
    try:
        if is_ghost:
            rare_filename = os.path.join(Config.GHOST_RARE_FOLDER, "rare-ghost.json")
        else:
            region = account_data.get('region', 'UNKNOWN')
            rare_filename = os.path.join(Config.RARE_ACCOUNTS_FOLDER, f"rare-{region}.json")

        rare_entry = {
            'uid': account_data["uid"],
            'password': account_data["password"],
            'account_id': account_data.get("account_id", "N/A"),
            'name': account_data["name"],
            'region': "Sulav" if is_ghost else account_data.get('region', 'UNKNOWN'),
            'rarity_type': rarity_type,
            'rarity_score': rarity_score,
            'reason': reason,
            'date_identified': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'jwt_token': account_data.get('jwt_token', ''),
            'thread_id': account_data.get('thread_id', 'N/A')
        }

        file_lock = get_file_lock(rare_filename)
        with file_lock:
            rare_list = safe_json_load(rare_filename, [])
            existing_ids = [acc.get('account_id') for acc in rare_list]
            if account_data.get("account_id", "N/A") not in existing_ids:
                rare_list.append(rare_entry)
                safe_json_save(rare_filename, rare_list)
                return True
        return False
    except:
        return False

def save_couples_account(account1, account2, reason, is_ghost=False):
    try:
        if is_ghost:
            couples_filename = os.path.join(Config.GHOST_COUPLES_FOLDER, "couples-ghost.json")
        else:
            region = account1.get('region', 'UNKNOWN')
            couples_filename = os.path.join(Config.COUPLES_ACCOUNTS_FOLDER, f"couples-{region}.json")

        couples_entry = {
            'couple_id': f"{account1.get('account_id', 'N/A')}_{account2.get('account_id', 'N/A')}",
            'account1': {
                'uid': account1["uid"],
                'password': account1["password"],
                'account_id': account1.get("account_id", "N/A"),
                'name': account1["name"],
                'thread_id': account1.get('thread_id', 'N/A')
            },
            'account2': {
                'uid': account2["uid"],
                'password': account2["password"],
                'account_id': account2.get("account_id", "N/A"),
                'name': account2["name"],
                'thread_id': account2.get('thread_id', 'N/A')
            },
            'reason': reason,
            'region': "Sulav" if is_ghost else account1.get('region', 'UNKNOWN'),
            'date_matched': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        file_lock = get_file_lock(couples_filename)
        with file_lock:
            couples_list = safe_json_load(couples_filename, [])
            existing_couples = [c.get('couple_id') for c in couples_list]
            if couples_entry['couple_id'] not in existing_couples:
                couples_list.append(couples_entry)
                safe_json_save(couples_filename, couples_list)
                return True
        return False
    except:
        return False

# =============================================================================
# 👥 WORKER FUNCTIONS
# =============================================================================

RARE_COUNTER = 0
COUPLES_COUNTER = 0
SUCCESS_COUNTER = 0

def print_registration_status(count, total, name, uid, password, account_id, region, is_ghost=False, api_label="Unknown"):
    print(f"{VISUAL.COLORS['highlight']}{VISUAL.COLORS['bold']}╔══════════════════════════════════════════════╗{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['highlight']}{VISUAL.COLORS['bold']}║  📝 Registration {count}/{total}{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['highlight']}║  🚀 {api_label}{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['highlight']}║  👤 Name: {name}{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['highlight']}║  🆔 UID: {uid}{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['highlight']}║  🎮 Account ID: {account_id}{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['highlight']}║  🔑 Password: {password}{VISUAL.COLORS['reset']}")
    if is_ghost:
        print(f"{VISUAL.COLORS['highlight']}║  🌍 Mode: {VISUAL.COLORS['rare']}GHOST Mode{VISUAL.COLORS['reset']}")
    else:
        print(f"{VISUAL.COLORS['highlight']}║  🌍 Region: {region}{VISUAL.COLORS['reset']}")
    print(f"{VISUAL.COLORS['highlight']}{VISUAL.COLORS['bold']}╚══════════════════════════════════════════════╝{VISUAL.COLORS['reset']}\n")

def generate_single_account(region, total_accounts, thread_id, session, is_ghost=False):
    global SUCCESS_COUNTER, RARE_COUNTER, COUPLES_COUNTER, BIO_SET_COUNTER
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER
    
    if EXIT_FLAG:
        return None

    with Config.LOCK:
        if SUCCESS_COUNTER >= total_accounts:
            return None

    account_result = create_acc(region, session, is_ghost)
    if not account_result:
        return None

    account_id = account_result.get("account_id", "N/A")
    jwt_token = account_result.get("jwt_token", "")
    api_label = account_result.get("api_label", "Unknown")
    account_result['thread_id'] = thread_id

    with Config.LOCK:
        SUCCESS_COUNTER += 1
        current_count = SUCCESS_COUNTER

    print_registration_status(current_count, total_accounts, account_result["name"], 
                            account_result["uid"], account_result["password"], account_id, region, is_ghost, api_label)

    # Set bio for the account
    if Config.AUTO_BIO:
        set_account_bio(account_result["uid"], account_result["password"], Config.BIO_TEXT)

    is_rare, rarity_type, rarity_reason, rarity_score = check_account_rarity(account_result)
    if is_rare:
        with Config.LOCK:
            RARE_COUNTER += 1
        print_rarity_found(account_result, rarity_type, rarity_reason, rarity_score)
        save_rare_account(account_result, rarity_type, rarity_reason, rarity_score, is_ghost)
        print_success(f"💎 Rare saved! (Total: {RARE_COUNTER})")

    is_couple, couple_reason, partner_data = check_account_couples(account_result, thread_id)
    if is_couple and partner_data:
        with Config.LOCK:
            COUPLES_COUNTER += 1
        print_couples_found(account_result, partner_data, couple_reason)
        save_couples_account(account_result, partner_data, couple_reason, is_ghost)
        print_success(f"💑 Couples saved! (Total: {COUPLES_COUNTER})")

    if is_ghost:
        save_normal_account(account_result, "GHOST", is_ghost=True)
        if jwt_token:
            save_jwt_token(account_result, jwt_token, "GHOST", is_ghost=True)
    else:
        save_normal_account(account_result, region)
        if jwt_token:
            save_jwt_token(account_result, jwt_token, region)

        # AUTO ACTIVATION
        if Config.AUTO_ACT:
            auto_activate_account(account_result)

    return {"account": account_result}

def worker(region, total_accounts, thread_id, is_ghost=False):
    print(f"{VISUAL.COLORS['secondary']}{VISUAL.COLORS['bold']}🧵 Thread {thread_id} started{VISUAL.COLORS['reset']}")

    session = requests.Session()
    accounts_generated = 0

    while not EXIT_FLAG:
        with Config.LOCK:
            if SUCCESS_COUNTER >= total_accounts:
                break

        result = generate_single_account(region, total_accounts, thread_id, session, is_ghost)
        if result:
            accounts_generated += 1

        smart_delay()

    print(f"{VISUAL.COLORS['secondary']}{VISUAL.COLORS['bold']}🧵 Thread {thread_id} finished: {accounts_generated} accounts{VISUAL.COLORS['reset']}")

# =============================================================================
# 📋 MENU FUNCTIONS - WITH ULTIMATE ADMIN CONTROL
# =============================================================================

def generate_accounts_flow():
    global SUCCESS_COUNTER, RARE_COUNTER, COUPLES_COUNTER
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER, BIO_SET_COUNTER

    VISUAL.show_header(Config.USER_LEVEL)

    regions_to_show = [r for r in Config.REGION_LANG.keys() if r != "BR"]

    region_menu = ""
    for i, region in enumerate(regions_to_show, 1):
        region_menu += f"{i}) {region} ({Config.REGION_LANG[region]})\n"
    region_menu += f"{len(regions_to_show)+1}) GHOST Mode\n"
    region_menu += f"00) BACK\n"
    region_menu += f"000) EXIT"

    print(VISUAL.create_panel("🌍 AVAILABLE REGIONS", region_menu))

    while True:
        try:
            choice = input(f"\n{VISUAL.COLORS['highlight']}{VISUAL.COLORS['bold']}🎯 Choose option: {VISUAL.COLORS['reset']}").strip().upper()

            if choice == "00":
                return
            elif choice == "000":
                print(f"\n{VISUAL.COLORS['primary']}{VISUAL.COLORS['bold']}👋 Goodbye! Thanks for using SULAV X AJAY Generator!{VISUAL.COLORS['reset']}")
                sys.exit(0)
            elif choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(regions_to_show):
                    selected_region = regions_to_show[choice_num - 1]
                    is_ghost = False
                    break
                elif choice_num == len(regions_to_show) + 1:
                    selected_region = "BR"
                    is_ghost = True
                    break
            elif choice in regions_to_show:
                selected_region = choice
                is_ghost = False
                break
            elif choice == "GHOST":
                selected_region = "BR"
                is_ghost = True
                break
            else:
                print_error("Invalid option")
        except KeyboardInterrupt:
            safe_exit()

    VISUAL.show_header(Config.USER_LEVEL)

    # Admin can set custom target
    if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
        account_count = Config.CUSTOM_TARGET
    else:
        account_count = 999999999
    
    thread_count = Config.MAX_THREADS

    # Show user level in config
    user_level_display = f"{VISUAL.ICONS['crown'] if Config.USER_LEVEL == 'OWNER' else VISUAL.ICONS['admin'] if Config.USER_LEVEL == 'ADMIN' else VISUAL.ICONS['user_icon']} {Config.USER_LEVEL} MODE"
    
    # Custom settings for admin
    custom_settings = ""
    if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
        custom_settings = f"\n📝 Name Prefix: {Config.CUSTOM_NAME_PREFIX}\n🔑 Pass Prefix: {Config.CUSTOM_PASS_PREFIX}\n💎 Rarity Threshold: {Config.CUSTOM_RARITY_THRESHOLD}"
    
    config_text = f"""🎯 Target: {account_count}
⚡ Threads: {thread_count}
🔌 APIs: {API_COUNT}
📝 Auto Bio: {'ON' if Config.AUTO_BIO else 'OFF'}
🔥 Auto-Activation: {'ON' if Config.AUTO_ACT else 'OFF'}
🌍 Region: {'GHOST' if is_ghost else selected_region}
👤 Access Level: {user_level_display}
🔄 Max Retries: {Config.MAX_RETRIES}{custom_settings}"""

    print(VISUAL.create_panel("🚀 GENERATION CONFIG", config_text))
    
    print(f"\n{VISUAL.COLORS['warning']}⏳ Starting in 3 seconds...{VISUAL.COLORS['reset']}")
    time.sleep(3)

    # Reset counters
    SUCCESS_COUNTER = 0
    RARE_COUNTER = 0
    COUPLES_COUNTER = 0
    ACTIVATED_COUNTER = 0
    FAILED_ACTIVATION_COUNTER = 0
    BIO_SET_COUNTER = 0
    
    start_time = time.time()
    threads = []

    print(f"\n{VISUAL.COLORS['primary']}{VISUAL.COLORS['bold']}🚀 Starting with {thread_count} threads...{VISUAL.COLORS['reset']}\n")

    for i in range(thread_count):
        t = threading.Thread(target=worker, args=(selected_region, account_count, i+1, is_ghost))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while any(t.is_alive() for t in threads):
            time.sleep(1)
            with Config.LOCK:
                current_count = SUCCESS_COUNTER
                activated_count = ACTIVATED_COUNTER
                failed_act_count = FAILED_ACTIVATION_COUNTER
                bio_count = BIO_SET_COUNTER
                rare_count = RARE_COUNTER
                couples_count = COUPLES_COUNTER
                attempts = Config.ATTEMPTS

            percent = (current_count / account_count) if account_count > 0 else 0
            progress_bar = VISUAL.create_progress_bar(current_count, account_count, 30)

            VISUAL.clear()
            VISUAL.show_header(Config.USER_LEVEL)
            
            stats = f"""📊 Progress: {progress_bar}
💎 RARE: {rare_count}  💑 COUPLES: {couples_count}
✅ GENERATED: {current_count}/{account_count}
🔥 ACTIVATED: {activated_count}  ❌ FAILED: {failed_act_count}
📝 BIO: {bio_count}  🔌 ATTEMPTS: {attempts}
⚡ SPEED: {current_count/(time.time()-start_time+0.1):.1f}/s
⏱️ TIME: {time.time()-start_time:.1f}s"""

            print(VISUAL.create_panel("⚡ LIVE STATISTICS", stats))

            if current_count >= account_count:
                break
    except KeyboardInterrupt:
        print_warning("Interrupted!")
        EXIT_FLAG = True

    for t in threads:
        t.join(timeout=3)

    elapsed = time.time() - start_time

    VISUAL.clear()
    VISUAL.show_header(Config.USER_LEVEL)

    final_stats = f"""📊 Generated: {SUCCESS_COUNTER}/{account_count}
💎 Rare: {RARE_COUNTER}
💑 Couples: {COUPLES_COUNTER}
🔥 Activated: {ACTIVATED_COUNTER}
❌ Failed: {FAILED_ACTIVATION_COUNTER}
📝 Bio Set: {BIO_SET_COUNTER}
⏱️ Time: {elapsed:.2f}s
⚡ Speed: {SUCCESS_COUNTER/elapsed:.2f} acc/s
🔌 API Attempts: {Config.ATTEMPTS}
👤 Access: {Config.USER_LEVEL}"""

    print(VISUAL.create_panel("🎉 GENERATION COMPLETE!", final_stats))

    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter to continue...{VISUAL.COLORS['reset']}")

def admin_panel():
    """Ultimate Admin Control Panel"""
    if Config.USER_LEVEL == "USER":
        print_error("Access Denied! Admin/Owner only.")
        time.sleep(2)
        return
    
    while True:
        VISUAL.show_header(Config.USER_LEVEL)
        
        credits = CreditEditor.load_credits()
        
        admin_menu = f"""🔧 ULTIMATE ADMIN CONTROL PANEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Current Level: {Config.USER_LEVEL}
🔌 Total APIs: {API_COUNT}

📝 CREDIT MANAGEMENT:
1) ✏️ Edit Primary Credit (Current: {credits['primary_credit']})
2) 📱 Edit Telegram Handles (Current: {credits['telegram1']}, {credits['telegram2']})
3) 🐙 Edit GitHub Link (Current: {credits['github']})
4) 📝 Edit Banner Text (Current: {credits['banner_text'][:30]}...)
5) 📝 Edit Bio Text (Current: {credits['bio_text'][:30]}...)
6) 💾 Save Credit Changes
7) 🔄 Restore Default Credits

⚙️ GENERATION SETTINGS:
8) 🎯 Set Custom Name Prefix (Current: {Config.CUSTOM_NAME_PREFIX})
9) 🔑 Set Custom Password Prefix (Current: {Config.CUSTOM_PASS_PREFIX})
10) 💎 Set Rarity Threshold (Current: {Config.CUSTOM_RARITY_THRESHOLD})
11) 🎯 Set Custom Target (Current: {Config.CUSTOM_TARGET})
12) ⚡ Configure Threads (Current: {Config.MAX_THREADS})
13) 🔄 Configure Retries (Current: {Config.MAX_RETRIES})

📊 SYSTEM CONTROLS:
14) 📈 View API Statistics
15) 🗑️ Clear All Data
16) 💾 Backup System
17) 🔄 Reset Counters
18) 📝 View Debug Logs
19) ⬅️ Back to Main Menu"""

        if Config.USER_LEVEL == "OWNER":
            admin_menu += "\n\n👑 OWNER EXCLUSIVE:\n20) ⚡ Force Generation Mode\n21) 🚀 Bypass Rate Limits\n22) 🔄 Custom API Priority"
        
        print(VISUAL.create_panel("🔧 ULTIMATE ADMIN CONTROL", admin_menu, color='admin'))
        
        choice = input(f"\n{VISUAL.COLORS['admin']}⚡ Admin Option: {VISUAL.COLORS['reset']}").strip()
        
        if choice == "1":
            new_credit = input(f"{VISUAL.COLORS['info']}Enter new primary credit: {VISUAL.COLORS['reset']}")
            credits['primary_credit'] = new_credit
            CreditEditor.save_credits(credits)
            print_success("Primary credit updated!")
            time.sleep(1)
        
        elif choice == "2":
            new_tg1 = input(f"{VISUAL.COLORS['info']}Enter new Telegram handle 1: {VISUAL.COLORS['reset']}")
            new_tg2 = input(f"{VISUAL.COLORS['info']}Enter new Telegram handle 2: {VISUAL.COLORS['reset']}")
            credits['telegram1'] = new_tg1
            credits['telegram2'] = new_tg2
            CreditEditor.save_credits(credits)
            print_success("Telegram handles updated!")
            time.sleep(1)
        
        elif choice == "3":
            new_github = input(f"{VISUAL.COLORS['info']}Enter new GitHub link: {VISUAL.COLORS['reset']}")
            credits['github'] = new_github
            CreditEditor.save_credits(credits)
            print_success("GitHub link updated!")
            time.sleep(1)
        
        elif choice == "4":
            new_banner = input(f"{VISUAL.COLORS['info']}Enter new banner text: {VISUAL.COLORS['reset']}")
            credits['banner_text'] = new_banner
            CreditEditor.save_credits(credits)
            print_success("Banner text updated!")
            time.sleep(1)
        
        elif choice == "5":
            new_bio = input(f"{VISUAL.COLORS['info']}Enter new bio text: {VISUAL.COLORS['reset']}")
            credits['bio_text'] = new_bio
            Config.BIO_TEXT = new_bio
            CreditEditor.save_credits(credits)
            print_success("Bio text updated!")
            time.sleep(1)
        
        elif choice == "6":
            CreditEditor.save_credits(credits)
            print_success("Credit changes saved!")
            time.sleep(1)
        
        elif choice == "7":
            default_credits = {
                "primary_credit": "SULAV AND AJAY",
                "github": "https://github.com/Sulav",
                "telegram1": "@sulav_don1",
                "telegram2": "@agajayofficial",
                "display_name": "SULAV X AJAY",
                "banner_text": "⚡ POWERED BY AJAX SULAV⚡",
                "footer_text": "👤 CREDIT: SULAV | TELEGRAM: @sulav_don1,@agajayofficial| GITHUB: Sulav",
                "bio_text": "[c][B][FF0000]AJAY X SULAV [b][00FF00]IG : AGAJAYOFFICIAL TG - AGAJAYOFFICIAL"
            }
            CreditEditor.save_credits(default_credits)
            Config.BIO_TEXT = default_credits['bio_text']
            print_success("Default credits restored!")
            time.sleep(1)
        
        elif choice == "8":
            new_prefix = input(f"{VISUAL.COLORS['info']}Enter new name prefix: {VISUAL.COLORS['reset']}")
            Config.CUSTOM_NAME_PREFIX = new_prefix
            print_success(f"Name prefix set to: {new_prefix}")
            time.sleep(1)
        
        elif choice == "9":
            new_prefix = input(f"{VISUAL.COLORS['info']}Enter new password prefix: {VISUAL.COLORS['reset']}")
            Config.CUSTOM_PASS_PREFIX = new_prefix
            print_success(f"Password prefix set to: {new_prefix}")
            time.sleep(1)
        
        elif choice == "10":
            try:
                new_threshold = int(input(f"{VISUAL.COLORS['info']}Enter new rarity threshold (1-10): {VISUAL.COLORS['reset']}"))
                if 1 <= new_threshold <= 10:
                    Config.CUSTOM_RARITY_THRESHOLD = new_threshold
                    print_success(f"Rarity threshold set to: {new_threshold}")
                else:
                    print_error("Threshold must be between 1 and 10")
            except:
                print_error("Invalid input")
            time.sleep(1)
        
        elif choice == "11":
            try:
                new_target = int(input(f"{VISUAL.COLORS['info']}Enter custom target: {VISUAL.COLORS['reset']}"))
                Config.CUSTOM_TARGET = new_target
                print_success(f"Custom target set to: {new_target}")
            except:
                print_error("Invalid input")
            time.sleep(1)
        
        elif choice == "12":
            try:
                new_threads = int(input(f"{VISUAL.COLORS['info']}Enter max threads (1-64): {VISUAL.COLORS['reset']}"))
                if 1 <= new_threads <= 64:
                    Config.MAX_THREADS = new_threads
                    print_success(f"Max threads set to: {new_threads}")
                else:
                    print_error("Threads must be between 1 and 64")
            except:
                print_error("Invalid input")
            time.sleep(1)
        
        elif choice == "13":
            try:
                new_retries = int(input(f"{VISUAL.COLORS['info']}Enter max retries (1-20): {VISUAL.COLORS['reset']}"))
                if 1 <= new_retries <= 20:
                    Config.MAX_RETRIES = new_retries
                    print_success(f"Max retries set to: {new_retries}")
                else:
                    print_error("Retries must be between 1 and 20")
            except:
                print_error("Invalid input")
            time.sleep(1)
        
        elif choice == "14":
            success_rate = (SUCCESS_COUNTER / Config.ATTEMPTS * 100) if Config.ATTEMPTS > 0 else 0
            stats_text = f"""📈 API STATISTICS
━━━━━━━━━━━━━━━━━━━━━━
📊 Total Attempts: {Config.ATTEMPTS}
✅ Successful: {SUCCESS_COUNTER}
❌ Failed: {Config.ATTEMPTS - SUCCESS_COUNTER}
⚡ Success Rate: {success_rate:.1f}%
🔌 Total APIs: {API_COUNT}"""
            print(VISUAL.create_panel("📊 API STATISTICS", stats_text))
            input(f"\n{VISUAL.COLORS['warning']}⏎ Press Enter...{VISUAL.COLORS['reset']}")
        
        elif choice == "15":
            confirm = input(f"{VISUAL.COLORS['error']}⚠️ This will delete ALL data! Type 'CONFIRM' to proceed: {VISUAL.COLORS['reset']}")
            if confirm == "CONFIRM":
                import shutil
                shutil.rmtree(Config.BASE_FOLDER)
                Config.create_folders()
                print_success("All data cleared!")
            time.sleep(2)
        
        elif choice == "16":
            backup_path = CreditEditor.backup_current_file()
            if backup_path:
                print_success(f"Backup created at: {backup_path}")
            else:
                print_error("Backup failed")
            time.sleep(2)
        
        elif choice == "17":
            Config.SUCCESS = Config.RARE = Config.COUPLES = Config.ACTIVATED = Config.FAILED = Config.BIO = Config.ATTEMPTS = 0
            SUCCESS_COUNTER = RARE_COUNTER = COUPLES_COUNTER = ACTIVATED_COUNTER = FAILED_ACTIVATION_COUNTER = BIO_SET_COUNTER = 0
            print_success("All counters reset!")
            time.sleep(1)
        
        elif choice == "18":
            Config.DEBUG_MODE = not Config.DEBUG_MODE
            print_success(f"Debug mode: {'ON' if Config.DEBUG_MODE else 'OFF'}")
            time.sleep(1)
        
        elif choice == "19":
            break
        
        elif choice == "20" and Config.USER_LEVEL == "OWNER":
            Config.FORCE_GENERATION = not Config.FORCE_GENERATION
            print_success(f"Force Generation: {Config.FORCE_GENERATION}")
            time.sleep(1)
        
        elif choice == "21" and Config.USER_LEVEL == "OWNER":
            Config.BYPASS_RATE_LIMIT = not Config.BYPASS_RATE_LIMIT
            print_success(f"Bypass Rate Limit: {Config.BYPASS_RATE_LIMIT}")
            time.sleep(1)
        
        elif choice == "22" and Config.USER_LEVEL == "OWNER":
            Config.CUSTOM_API_PRIORITY = not Config.CUSTOM_API_PRIORITY
            print_success(f"Custom API Priority: {Config.CUSTOM_API_PRIORITY}")
            time.sleep(1)
        
        else:
            print_error("Invalid option or insufficient privileges")
            time.sleep(1)

def view_saved_accounts():
    VISUAL.show_header(Config.USER_LEVEL)

    folders = [Config.ACCOUNTS_FOLDER, Config.ACTIVATED_FOLDER, Config.RARE_ACCOUNTS_FOLDER, Config.COUPLES_ACCOUNTS_FOLDER]
    total = 0
    results = ""

    for folder in folders:
        if os.path.exists(folder):
            files = [f for f in os.listdir(folder) if f.endswith('.json')]
            for file in files:
                filepath = os.path.join(folder, file)
                try:
                    data = safe_json_load(filepath, [])
                    results += f"📄 {folder}/{file}: {len(data)} accounts\n"
                    total += len(data)
                except:
                    pass

    results += f"\n📊 TOTAL: {total} accounts"

    print(VISUAL.create_panel("📁 SAVED ACCOUNTS", results))
    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter...{VISUAL.COLORS['reset']}")

def show_stats():
    VISUAL.show_header(Config.USER_LEVEL)
    
    success_rate = (SUCCESS_COUNTER / Config.ATTEMPTS * 100) if Config.ATTEMPTS > 0 else 0
    
    stats = f"""📊 SESSION STATISTICS
━━━━━━━━━━━━━━━━━━━━━━
✅ Generated: {SUCCESS_COUNTER}
💎 Rare: {RARE_COUNTER}
💑 Couples: {COUPLES_COUNTER}
🔥 Activated: {ACTIVATED_COUNTER}
❌ Failed: {FAILED_ACTIVATION_COUNTER}
📝 Bio: {BIO_SET_COUNTER}
🔌 API Attempts: {Config.ATTEMPTS}

📈 PERFORMANCE
━━━━━━━━━━━━━━━━━━━━━━
🔌 Total APIs: {API_COUNT}
⚡ Success Rate: {success_rate:.1f}%
👤 Access Level: {Config.USER_LEVEL}
🔄 Max Retries: {Config.MAX_RETRIES}
⚡ Max Threads: {Config.MAX_THREADS}"""

    if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
        stats += f"\n📝 Name Prefix: {Config.CUSTOM_NAME_PREFIX}\n🔑 Pass Prefix: {Config.CUSTOM_PASS_PREFIX}\n💎 Rarity Threshold: {Config.CUSTOM_RARITY_THRESHOLD}"

    print(VISUAL.create_panel("📈 STATISTICS", stats))
    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter...{VISUAL.COLORS['reset']}")

def about():
    VISUAL.show_header(Config.USER_LEVEL)
    
    credits = CreditEditor.load_credits()
    
    about_text = f"""🔥 {credits['display_name']} ULTIMATE GENERATOR v12.0
💎 Created by: {credits['primary_credit']}
📱 Telegram: {credits['telegram1']}, {credits['telegram2']}
🐙 GitHub: {credits['github']}

✨ ULTIMATE FEATURES:
• {API_COUNT} Working APIs
• ULTIMATE ADMIN CONTROL PANEL
• 3 Access Levels (USER/ADMIN/OWNER)
• Custom Credit Editor
• Custom Name/Password Prefix
• Adjustable Rarity Threshold
• Auto Activation System
• Rare Account Detection
• Couples Account Finder
• Auto Bio Changer
• Multi-threading Support
• Real-time Statistics
• Professional Visual Design

🔐 ACCESS LEVELS:
• USER: Basic access
• ADMIN: Full control + credit editing
• OWNER: Ultimate control + exclusive features

⚠️ DO NOT REMOVE CREDITS
🔒 Protected by SULAV X AJAY"""

    print(VISUAL.create_panel("ℹ️ ABOUT", about_text))
    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter...{VISUAL.COLORS['reset']}")

def main_menu():
    Config.create_folders()
    
    while True:
        VISUAL.show_header(Config.USER_LEVEL)

        # Different menu options based on user level
        menu = """1) 🚀 Generate Accounts
2) 📁 View Saved Accounts
3) 📊 Statistics
4) ℹ️  About"""

        if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
            menu += "\n5) 🔧 ULTIMATE ADMIN PANEL"
            menu += "\n6) 🚪 Exit"
        else:
            menu += "\n5) 🚪 Exit"

        print(VISUAL.create_panel("📌 MAIN MENU", menu))

        choice = input(f"\n{VISUAL.COLORS['highlight']}{VISUAL.COLORS['bold']}🎯 Choose: {VISUAL.COLORS['reset']}").strip()

        if choice == "1":
            generate_accounts_flow()
        elif choice == "2":
            view_saved_accounts()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            about()
        elif choice == "5":
            if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
                admin_panel()
            else:
                print(f"\n{VISUAL.COLORS['primary']}{VISUAL.COLORS['bold']}👋 Goodbye! Contact: @sulav_don1 | @agajayofficial{VISUAL.COLORS['reset']}")
                sys.exit(0)
        elif choice == "6" and Config.USER_LEVEL in ["ADMIN", "OWNER"]:
            print(f"\n{VISUAL.COLORS['primary']}{VISUAL.COLORS['bold']}👋 Goodbye! Contact: @sulav_don1 | @agajayofficial{VISUAL.COLORS['reset']}")
            sys.exit(0)
        else:
            print_error("Invalid option")
            time.sleep(1)

# =============================================================================
# 🚀 MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    try:
        # Start main menu
        main_menu()
        
    except KeyboardInterrupt:
        safe_exit()
    except Exception as e:
        print_error(f"Error: {e}")
        time.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)
