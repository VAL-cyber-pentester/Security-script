# 🛠️ Security Scripts

Collection de scripts d'automatisation pour la cybersécurité.

## 📊 Script de Veille Cybersécurité Automatisée

### Description

Script Python qui automatise la collecte quotidienne d'informations de sécurité depuis :
- **CERT-FR** : Alertes de sécurité officielles
- **CVE Database** : Vulnérabilités récentes
- **The Hacker News** : Actualités cybersécurité

Génère un rapport HTML professionnel avec les dernières menaces et actualités.

### Fonctionnalités

✅ Agrégation automatique de multiples sources  
✅ Génération de rapport HTML responsive  
✅ Design professionnel avec code couleur par sévérité  
✅ Ouverture automatique dans le navigateur  
✅ Horodatage et archivage des rapports  

### Installation
```bash
# Cloner le repo
git clone https://github.com/VAL-cyber-pentester/Security-Scripts.git

# Installer les dépendances
pip install feedparser requests beautifulsoup4
```

### Utilisation
```bash
python veille_cyber.py
```

Le script génère un fichier `veille_cyber_YYYYMMDD_HHMMSS.html` et l'ouvre automatiquement.

### Automatisation 

**Windows - Planificateur de tâches :**
```
Créer une tâche planifiée quotidienne à 9h
Action : python C:\Projets\Veille-Cyber\veille_cyber.py
```

**Linux - Cron :**
```bash
0 9 * * * python3 /path/to/veille_cyber.py
```



### Améliorations futures

- [ ] Intégration API NVD pour CVE réelles
- [ ] Envoi par email automatique
- [ ] Filtrage par mots-clés
- [ ] Export PDF
- [ ] Notifications push

---

## 🔐 Script de Hardening Linux Automatisé

### Description

Script Bash qui automatise le durcissement de la sécurité d'un système Linux avec :
- Mise à jour complète du système
- Configuration du pare-feu UFW
- Désactivation des services inutiles
- Sécurisation SSH (désactivation root login)
- Vérification et correction des permissions critiques
- Activation des mises à jour automatiques de sécurité
- Audit de sécurité basique
- Génération de rapport détaillé

### Fonctionnalités

✅ Automatisation complète du hardening  
✅ Messages colorés avec codes de statut  
✅ Logs détaillés de toutes les opérations  
✅ Rapport de conformité automatique  
✅ Vérification des fichiers sensibles (/etc/passwd, /etc/shadow)  
✅ Configuration pare-feu avec règles par défaut sécurisées  
✅ Backup automatique des configurations modifiées  

### Prérequis

- Système Linux (Debian/Ubuntu/Kali)
- Privilèges root (sudo)

### Installation
```bash
# Télécharger le script
wget https://raw.githubusercontent.com/VAL-cyber-pentester/Security-Scripts/main/hardening.sh

# Rendre exécutable
chmod +x hardening.sh
```

### Utilisation
```bash
# Exécuter le script
sudo ./hardening.sh
```

Le script génère :
- `/var/log/hardening_YYYYMMDD_HHMMSS.log` : Log détaillé
- `~/hardening_report_YYYYMMDD_HHMMSS.txt` : Rapport de conformité

### Actions Effectuées

**1. Mise à jour système**
- `apt update` et `apt upgrade`
- Suppression des paquets inutiles

**2. Pare-feu (UFW)**
- Politique par défaut : deny incoming, allow outgoing
- SSH autorisé (port 22)
- Pare-feu activé

**3. Services**
- Désactivation de Bluetooth, CUPS, Avahi-daemon

**4. SSH**
- Désactivation de la connexion root
- Backup de la configuration originale
- Redémarrage du service

**5. Permissions**
- Vérification et correction des permissions :
  - /etc/passwd (644)
  - /etc/shadow (640)
  - /etc/group (644)
  - /etc/gshadow (640)

**6. Mises à jour automatiques**
- Installation et configuration de unattended-upgrades

**7. Audit**
- Liste des utilisateurs avec shell
- Ports en écoute (ss -tlnp)
- Tentatives de connexion échouées

### Capture d'écran
![Hardening Script Execution](screenshot rapport final.png)

### Sécurité

⚠️ **Testez d'abord sur une VM ou un système de test !**

Ce script modifie la configuration système. Utilisez-le en connaissance de cause.

### Améliorations futures

- [ ] Support CentOS/RHEL (firewalld)
- [ ] Configuration SELinux/AppArmor
- [ ] Durcissement kernel (sysctl)
- [ ] Détection et suppression des rootkits
- [ ] Configuration fail2ban
- [ ] Scan de compliance ANSSI/CIS

---

**Auteur :** Valérie Ename  
**Formation :** Bachelor AIS - Cybersécurité  
**Portfolio :** [GitHub](https://github.com/VAL-cyber-pentester)




