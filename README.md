# 🆔 Browser Fingerprinting - Détecteur d'Empreinte Digitale

Un projet de cybersécurité qui identifie les utilisateurs par les caractéristiques uniques de leur navigateur et de leur système d'exploitation.

---

## 🎯 QU'EST-CE QUE LE BROWSER FINGERPRINTING ?

Le fingerprinting (ou empreinte digitale) est une technique utilisée par les sites web et les banques pour identifier un utilisateur **sans utiliser de cookies**.

### Comment ça fonctionne ?
Le programme collecte plusieurs informations sur ton ordinateur et ton navigateur :
- Système d'exploitation et sa version
- Résolution de ton écran
- Polices installées
- Fuseau horaire
- Langue du système
- Architecture du processeur

**La combinaison unique de ces éléments crée une "empreinte" impossible à falsifier.**

---

## 🔐 POURQUOI C'EST UTILE EN CYBERSÉCURITÉ ?

| Application | Exemple |
|-------------|---------|
| **Anti-fraude bancaire** | Détecter si une connexion vient du même ordinateur |
| **Authentification renforcée** | Vérifier que c'est bien le même utilisateur |
| **Protection contre l'usurpation** | Alerter si quelqu'un essaie de se faire passer pour toi |
| **Sécurité sans cookie** | Fonctionne même si l'utilisateur efface ses cookies |

---

## 🚀 COMMENT UTILISER CE PROGRAMME ?

### Prérequis
- Avoir Python installé (version 3.6 ou plus)
- Windows (le programme utilise PowerShell pour certaines infos)

### Installation

1. **Télécharge le fichier** `fingerprint.py`

2. **Ouvre un terminal** dans le dossier du fichier

3. **Exécute la commande** :
   ```bash
   python fingerprint.py

### EXEMPLE D'EXÉCUTION 

### Première connexion (création de l'empreinte) 

🆔 Detecteur d'Empreinte Digitale du Navigateur

📊 Analyse de ton navigateur et systeme...

📋 Informations collectees :
   • Systeme d'exploitation : Windows
   • Version OS : 10.0.22631...
   • Architecture : AMD64
   • Resolution d'ecran : 1920x1080
   • Fuseau horaire : Romance Standard Time
   • Langue : fr-FR
   • Hash des polices : a3f5c2e1

🔑 Empreinte unique : 8f4e2a1c7b3d9e5f6a2c8b4d...

🔐 SIMULATION D'AUTHENTIFICATION

👤 Entre ton nom d'utilisateur : Test

🆕 Premier connexion pour Test !
   → Empreinte digitale enregistree

🎉 Acces autorise !
   → Ton navigateur est reconnu

💾 Empreinte sauvegardee pour Test 

### Deuxième connexion (vérification) 

👤 Entre ton nom d'utilisateur : Test 

✅ Identite confirmee pour Test 
   → Derniere connexion : 2026-05-16 14:30:00

🎉 Acces autorise ! 

### Tentative d'usurpation (alerte) 

👤 Entre ton nom d'utilisateur : Test 

🚨 ALERTE DE SECURITE !
   → Quelqu'un essaie de se faire passer pour Test 
   → Empreinte differente detectee !

⛔ Acces refuse ! 

