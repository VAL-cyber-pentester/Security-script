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

**Auteur :** Valérie Ename  
**Formation :** Bachelor AIS - Cybersécurité  
**Portfolio :** [GitHub](https://github.com/VAL-cyber-pentester)
```



