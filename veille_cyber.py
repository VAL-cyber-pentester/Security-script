#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script d'automatisation de veille cybersécurité
Auteur : Valérie Ename
Description : Agrège les infos de CERT-FR, CVE, et The Hacker News
"""

import feedparser
import requests
from datetime import datetime
import os

def banner():
    """Affiche le banner"""
    print("="*60)
    print("   VEILLE CYBERSÉCURITÉ AUTOMATISÉE")
    print("   Auteur : Valérie Ename")
    print("   Date : " + datetime.now().strftime("%d/%m/%Y %H:%M"))
    print("="*60)
    print()

def get_certfr_alerts():
    """Récupère les dernières alertes du CERT-FR"""
    print("[+] Récupération des alertes CERT-FR...")
    try:
        feed = feedparser.parse('https://www.cert.ssi.gouv.fr/feed/')
        alerts = []
        
        for entry in feed.entries[:5]:  # Les 5 dernières
            alerts.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published if 'published' in entry else 'N/A'
            })
        
        print(f"[✓] {len(alerts)} alertes récupérées\n")
        return alerts
    except Exception as e:
        print(f"[✗] Erreur CERT-FR : {e}\n")
        return []

def get_recent_cves():
    """Récupère les CVE récentes (simulation - API NVD nécessite une clé)"""
    print("[+] Récupération des CVE récentes...")
    # Note : Pour une vraie implémentation, utiliser l'API NVD avec une clé
    # https://nvd.nist.gov/developers/request-an-api-key
    
    # Simulation pour le projet
    cves = [
        {"id": "CVE-2024-XXXXX", "description": "Exemple de CVE récente", "severity": "HIGH"},
        {"id": "CVE-2024-XXXXY", "description": "Autre CVE d'exemple", "severity": "CRITICAL"}
    ]
    
    print(f"[✓] {len(cves)} CVE récupérées (données d'exemple)\n")
    print("[i] Pour des données réelles, configurer une clé API NVD\n")
    return cves

def get_hackernews():
    """Récupère les derniers articles de The Hacker News"""
    print("[+] Récupération des articles The Hacker News...")
    try:
        feed = feedparser.parse('https://feeds.feedburner.com/TheHackersNews')
        articles = []
        
        for entry in feed.entries[:5]:  # Les 5 derniers
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published if 'published' in entry else 'N/A'
            })
        
        print(f"[✓] {len(articles)} articles récupérés\n")
        return articles
    except Exception as e:
        print(f"[✗] Erreur The Hacker News : {e}\n")
        return []

def generate_html_report(certfr_alerts, cves, hackernews_articles):
    """Génère un rapport HTML"""
    print("[+] Génération du rapport HTML...")
    
    filename = f"veille_cyber_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Veille Cybersécurité - {datetime.now().strftime('%d/%m/%Y')}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }}
        .section {{
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .alert-item, .cve-item, .article-item {{
            margin: 15px 0;
            padding: 15px;
            border-left: 4px solid #3498db;
            background: #ecf0f1;
            border-radius: 4px;
        }}
        .alert-item h3, .cve-item h3, .article-item h3 {{
            margin: 0 0 10px 0;
            color: #2c3e50;
        }}
        .cve-critical {{
            border-left-color: #e74c3c;
        }}
        .cve-high {{
            border-left-color: #e67e22;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .date {{
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #bdc3c7;
            color: #7f8c8d;
        }}
        .severity {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.8em;
            font-weight: bold;
            color: white;
        }}
        .severity-critical {{
            background-color: #e74c3c;
        }}
        .severity-high {{
            background-color: #e67e22;
        }}
    </style>
</head>
<body>
    <h1>📊 Rapport de Veille Cybersécurité</h1>
    <p class="date">Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
    
    <div class="section">
        <h2>🔴 CERT-FR - Alertes de Sécurité</h2>
"""
    
    if certfr_alerts:
        for alert in certfr_alerts:
            html_content += f"""
        <div class="alert-item">
            <h3>{alert['title']}</h3>
            <p class="date">Publié le : {alert['published']}</p>
            <p><a href="{alert['link']}" target="_blank">Lire l'alerte complète →</a></p>
        </div>
"""
    else:
        html_content += "<p>Aucune alerte récupérée</p>"
    
    html_content += """
    </div>
    
    <div class="section">
        <h2>🛡️ CVE Récentes</h2>
"""
    
    if cves:
        for cve in cves:
            severity_class = f"severity-{cve['severity'].lower()}"
            html_content += f"""
        <div class="cve-item">
            <h3>{cve['id']} <span class="severity {severity_class}">{cve['severity']}</span></h3>
            <p>{cve['description']}</p>
        </div>
"""
    else:
        html_content += "<p>Aucune CVE récupérée</p>"
    
    html_content += """
    </div>
    
    <div class="section">
        <h2>📰 The Hacker News - Actualités</h2>
"""
    
    if hackernews_articles:
        for article in hackernews_articles:
            html_content += f"""
        <div class="article-item">
            <h3>{article['title']}</h3>
            <p class="date">Publié le : {article['published']}</p>
            <p><a href="{article['link']}" target="_blank">Lire l'article →</a></p>
        </div>
"""
    else:
        html_content += "<p>Aucun article récupéré</p>"
    
    html_content += f"""
    </div>
    
    <div class="footer">
        <p>Script d'automatisation de veille cybersécurité</p>
        <p>Développé par Valérie Ename | <a href="https://github.com/VAL-cyber-pentester">GitHub</a></p>
    </div>
</body>
</html>
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"[✓] Rapport généré : {filename}\n")
    return filename

def main():
    """Fonction principale"""
    banner()
    
    # Récupération des données
    certfr_alerts = get_certfr_alerts()
    cves = get_recent_cves()
    hackernews_articles = get_hackernews()
    
    # Génération du rapport
    report_file = generate_html_report(certfr_alerts, cves, hackernews_articles)
    
    print("="*60)
    print(f"[✓] Veille terminée ! Rapport disponible : {report_file}")
    print("="*60)
    
    # Ouvrir le rapport dans le navigateur
    import webbrowser
    webbrowser.open(report_file)

if __name__ == "__main__":
    main()