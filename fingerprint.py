"""
Détecteur d'Empreinte Digitale du Navigateur
Identifie les utilisateurs par les caractéristiques uniques de leur navigateur
"""

import subprocess
import platform
import hashlib
import json
import os
from datetime import datetime

def get_browser_info():
    """
    Récupère les informations uniques du navigateur et du système
    """
    infos = {}
    
    # 1. Informations sur le système d'exploitation
    infos["os"] = platform.system()
    infos["os_version"] = platform.version()
    infos["machine"] = platform.machine()
    infos["processor"] = platform.processor()
    
    # 2. Résolution d'écran (Windows uniquement via PowerShell)
    if platform.system() == "Windows":
        try:
            result = subprocess.run(
                ['powershell', '-command', 
                 'Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width + "x" + [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height'],
                capture_output=True, text=True
            )
            infos["screen_resolution"] = result.stdout.strip()
        except:
            infos["screen_resolution"] = "unknown"
    else:
        infos["screen_resolution"] = "unknown"
    
    # 3. Liste des polices installées (fingerprint unique)
    if platform.system() == "Windows":
        try:
            result = subprocess.run(
                ['powershell', '-command', 
                 "Get-ItemProperty 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts' | Select-Object -Property * | Out-String"],
                capture_output=True, text=True
            )
            # On prend juste les noms des polices principales
            fonts = [line for line in result.stdout.split('\n') if '.ttf' in line or '.otf' in line]
            infos["fonts_hash"] = hashlib.md5(str(fonts[:20]).encode()).hexdigest()[:8]
        except:
            infos["fonts_hash"] = "unknown"
    else:
        infos["fonts_hash"] = "unknown"
    
    # 4. Timezone
    try:
        result = subprocess.run(['powershell', '-command', 'Get-TimeZone | Select-Object -ExpandProperty Id'], 
                               capture_output=True, text=True)
        infos["timezone"] = result.stdout.strip()
    except:
        infos["timezone"] = "unknown"
    
    # 5. Langue du système
    if platform.system() == "Windows":
        try:
            result = subprocess.run(['powershell', '-command', 'Get-Culture | Select-Object -ExpandProperty Name'],
                                   capture_output=True, text=True)
            infos["language"] = result.stdout.strip()
        except:
            infos["language"] = "unknown"
    else:
        infos["language"] = "unknown"
    
    return infos

def generate_fingerprint(infos):
    """
    Génère une empreinte unique à partir des informations
    """
    fingerprint_string = json.dumps(infos, sort_keys=True)
    fingerprint = hashlib.sha256(fingerprint_string.encode()).hexdigest()
    return fingerprint

def save_fingerprint(fingerprint, username):
    """
    Sauvegarde l'empreinte dans un fichier
    """
    fingerprints = {}
    if os.path.exists("fingerprints.json"):
        with open("fingerprints.json", "r") as f:
            fingerprints = json.load(f)
    
    fingerprints[username] = {
        "fingerprint": fingerprint,
        "last_seen": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open("fingerprints.json", "w") as f:
        json.dump(fingerprints, f, indent=4)

def load_fingerprints():
    """
    Charge toutes les empreintes sauvegardées
    """
    if os.path.exists("fingerprints.json"):
        with open("fingerprints.json", "r") as f:
            return json.load(f)
    return {}

def check_identity(username, current_fingerprint):
    """
    Vérifie si l'utilisateur est bien celui qu'il prétend être
    """
    fingerprints = load_fingerprints()
    
    if username not in fingerprints:
        print(f"\n🆕 Premier connexion pour {username} !")
        print("   → Empreinte digitale enregistree")
        save_fingerprint(current_fingerprint, username)
        return True
    
    saved_fingerprint = fingerprints[username]["fingerprint"]
    
    if current_fingerprint == saved_fingerprint:
        print(f"\n✅ Identite confirmee pour {username}")
        print(f"   → Derniere connexion : {fingerprints[username]['last_seen']}")
        return True
    else:
        print(f"\n🚨 ALERTE DE SECURITE !")
        print(f"   → Quelqu'un essaie de se faire passer pour {username}")
        print(f"   → Empreinte differente detectee !")
        return False

# ============================================
# PROGRAMME PRINCIPAL
# ============================================

print("=" * 60)
print("🆔 Detecteur d'Empreinte Digitale du Navigateur")
print("   (Browser Fingerprinting)")
print("=" * 60)

# Recuperation des informations
print("\n📊 Analyse de ton navigateur et systeme...")
infos = get_browser_info()
fingerprint = generate_fingerprint(infos)

# Affichage des informations collectees
print("\n📋 Informations collectees :")
print(f"   • Systeme d'exploitation : {infos['os']}")
print(f"   • Version OS : {infos['os_version'][:40]}...")
print(f"   • Architecture : {infos['machine']}")
print(f"   • Processeur : {infos['processor'] or 'Non detecte'}")
print(f"   • Resolution d'ecran : {infos['screen_resolution']}")
print(f"   • Fuseau horaire : {infos['timezone']}")
print(f"   • Langue : {infos['language']}")
print(f"   • Hash des polices : {infos['fonts_hash']}")
print(f"\n🔑 Empreinte unique : {fingerprint[:30]}...")

# Simulation d'identification
print("\n" + "=" * 60)
print("🔐 SIMULATION D'AUTHENTIFICATION")
print("=" * 60)

username = input("\n👤 Entre ton nom d'utilisateur : ")

# Verification
if check_identity(username, fingerprint):
    print("\n🎉 Acces autorise !")
    print("   → Ton navigateur est reconnu")
else:
    print("\n⛔ Acces refuse !")
    print("   → Authentification supplementaire requise")

# Sauvegarde
save_fingerprint(fingerprint, username)
print(f"\n💾 Empreinte sauvegardee pour {username}")

# Conseils de securite
print("\n" + "=" * 60)
print("💡 ASTUCES DE SECURITE")
print("=" * 60)
print("• Cette technique est utilisee par les banques")
print("• Elle fonctionne meme sans cookies")
print("• Certains navigateurs bloquent ce fingerprinting")
print("=" * 60)