---
audio: false
generated: false
image: false
lang: fr
layout: post
title: GFW, API de proxy, détection de VPN
translated: true
---

### Table des matières

1. [Les API dans les serveurs proxy peuvent-elles éviter les blocages du GFW ?](#les-api-dans-les-serveurs-proxy-peuvent-elles-éviter-les-blocages-du-gfw)
   - Mélanger le trafic proxy et API évite les blocages du GFW
   - Le GFW distingue le trafic proxy du trafic HTTP/HTTPS normal
   - Le GFW bloque probablement en fonction du trafic proxy exclusif
   - Le GFW utilise une fenêtre temporelle pour l'analyse du trafic
   - Accéder régulièrement à l'API peut empêcher la détection

2. [Fonctionnement du Grand Pare-feu (GFW).](#fonctionnement-du-grand-pare-feu-gfw)
   - Le GFW enregistre les requêtes avec les données source et cible
   - Bloque les IP associées à des activités illégales
   - Utilise des règles pour détecter des protocoles spécifiques
   - Peut bloquer en fonction du pourcentage de requêtes illégales
   - Emploie l'IA pour une détection intelligente des motifs de trafic

3. [Analyse de la détection VPN de ChatGPT iOS](#analyse-de-la-détection-vpn-de-chatgpt-ios)
   - ChatGPT iOS fonctionne désormais avec certains VPN
   - L'accès dépend de l'emplacement du serveur VPN
   - La détection est basée sur des adresses IP spécifiques
   - Certaines IP de fournisseurs cloud sont bloquées

---

## Les API dans les serveurs proxy peuvent-elles éviter les blocages du GFW ?

Je fais tourner un serveur simple sur mon instance Shadowsocks avec le code suivant :

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # Exécuter la commande vnstat pour obtenir les statistiques de trafic par intervalles de 5 minutes pour eth0
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # Retourner les données capturées en tant que réponse JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Et j'utilise nginx pour servir le port 443 comme montré ci-dessous :

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # géré par
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

Ce programme serveur fournit des données réseau, et j'utilise le serveur comme mon serveur proxy, ce qui me permet d'afficher mon statut en ligne sur mon blog en utilisant les données réseau.

Ce qui est intéressant, c'est que le serveur n'a pas été bloqué par le Grand Pare-feu (GFW) ou tout autre système de contrôle réseau depuis plusieurs jours. Normalement, le serveur proxy que j'ai configuré serait bloqué en un ou deux jours. Le serveur exécute un programme Shadowsocks sur un port comme 51939, donc il fonctionne avec un trafic Shadowsocks mélangé à un trafic API normal. Ce mélange semble amener le GFW à croire que le serveur n'est pas un proxy dédié, mais plutôt un serveur normal, l'empêchant de bloquer l'IP.

Cette observation est intrigante. Il semble que le GFW utilise une logique spécifique pour différencier le trafic proxy du trafic normal. Bien que de nombreux sites comme Twitter et YouTube soient bloqués en Chine, de nombreux sites étrangers — comme ceux d'universités internationales et d'entreprises — restent accessibles.

Cela suggère que le GFW fonctionne probablement selon des règles qui distinguent le trafic HTTP/HTTPS normal du trafic lié aux proxy. Les serveurs qui gèrent les deux types de trafic semblent éviter les blocages, tandis que les serveurs ne gérant que le trafic proxy sont plus susceptibles d'être bloqués.

Une question est de savoir quelle plage de temps le GFW utilise pour accumuler les données de blocage — que ce soit une journée ou une heure. Pendant cette période, il détecte si le trafic provient exclusivement d'un proxy. Si c'est le cas, l'IP du serveur est bloquée.

Je visite souvent mon blog pour relire ce que j'ai écrit, mais dans les semaines à venir, mon attention se tournera vers d'autres tâches plutôt que vers la rédaction d'articles de blog. Cela réduira mes accès à l'API `bandwidth` via le port 443. Si je constate que je suis à nouveau bloqué, je devrais écrire un programme pour accéder régulièrement à cette API afin de tromper le GFW.

Voici une version améliorée de votre texte avec une structure et une clarté optimisées :

---

## Fonctionnement du Grand Pare-feu (GFW).

### Étape 1 : Journalisation des requêtes

```python
import time

# Base de données pour stocker les données des requêtes
request_log = []

# Fonction pour enregistrer les requêtes
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

La fonction `log_request` enregistre les requêtes entrantes avec des informations essentielles comme l'IP source, l'IP cible, le port cible, le corps de la requête et l'horodatage.

### Étape 2 : Vérification et blocage des IP

```python
# Fonction pour vérifier les requêtes et bloquer les IP
def check_and_ban_ips():
    banned_ips = set()

    # Parcourir toutes les requêtes enregistrées
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # Appliquer les blocages à toutes les IP identifiées
    ban_ips(banned_ips)
```

La fonction `check_and_ban_ips` parcourt toutes les requêtes enregistrées, identifie et bloque les IP associées à des activités illégales.

### Étape 3 : Définition de ce qui rend une requête illégale

```python
# Fonction pour simuler la vérification si une requête est illégale
def is_illegal(request):
    # Espace réservé pour la logique réelle de vérification des requêtes illégales
    # Par exemple, vérifier le corps de la requête ou la cible
    return "illegal" in request['body']
```

Ici, `is_illegal` vérifie si le corps de la requête contient le mot "illegal". Cela peut être étendu à une logique plus sophistiquée en fonction de ce qui constitue une activité illégale.

### Étape 4 : Blocage des IP identifiées

```python
# Fonction pour bloquer une liste d'IP
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"Blocage de l'IP : {ip}")
```

Une fois les IP illégales identifiées, la fonction `ban_ips` les bloque en affichant leurs adresses IP (ou, dans un système réel, pourrait les bloquer).

### Étape 5 : Méthode alternative pour vérifier et bloquer les IP en fonction de 80 % de requêtes illégales

```python
# Fonction pour vérifier les requêtes et bloquer les IP en fonction de 80 % de requêtes illégales
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # Parcourir toutes les requêtes enregistrées
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # Si 80 % ou plus des requêtes sont illégales, bloquer ces IP
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # Appliquer les blocages à toutes les IP identifiées
    ban_ips(banned_ips)
```

Cette méthode alternative évalue si une IP doit être bloquée en fonction du pourcentage de requêtes illégales. Si 80 % ou plus des requêtes d'une IP sont illégales, elle est bloquée.

### Étape 6 : Vérification améliorée des requêtes illégales (ex. : détection des protocoles Shadowsocks et Trojan)

```python
def is_illegal(request):
    # Vérifier si la requête utilise le protocole Shadowsocks (corps contenant des données binaires)
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

La fonction `is_illegal` vérifie maintenant également des protocoles spécifiques comme Shadowsocks et Trojan :
- **Shadowsocks** : On peut vérifier la présence de données chiffrées ou binaires dans le corps de la requête.
- **Trojan** : Si la requête passe par le port 443 (HTTPS) et correspond à des motifs spécifiques (ex. : caractéristiques du trafic Trojan), elle est marquée comme illégale.

### Étape 7 : Exemple de requêtes légales

Par exemple, des requêtes comme `GET https://some-domain.xyz/bandwidth` sont sûrement légales et ne déclencheront pas le mécanisme de blocage.

### Étape 8 : Caractéristiques du trafic des serveurs proxy

Les serveurs proxy ont des caractéristiques de trafic très différentes de celles des serveurs web ou API normaux. Le GFW doit distinguer le trafic normal des serveurs web de celui des serveurs proxy, qui peut être totalement différent.

### Étape 9 : Modèles d'IA et d'apprentissage automatique pour une détection intelligente

Étant donné la grande variété de requêtes et de réponses qui transitent par Internet, le GFW pourrait employer des modèles d'IA et d'apprentissage automatique pour analyser les motifs de trafic et détecter intelligemment les comportements illégaux. En formant le système sur divers types de trafic et en utilisant des techniques avancées, il pourrait bloquer ou filtrer le trafic plus efficacement en fonction des motifs observés.

---

## Mise à jour

Malgré mes efforts, mon serveur proxy continue d'être bloqué. Pour atténuer ce problème, j'ai mis en place une solution de contournement en utilisant la fonction d'IP inversée de Digital Ocean, qui me permet d'attribuer rapidement une nouvelle adresse IP chaque fois qu'un blocage se produit.

---

## Analyse de la détection VPN de ChatGPT iOS

*26.12.2024*

Aujourd'hui, j'ai découvert que l'application iOS de ChatGPT permet désormais de se connecter avec un VPN en Chine. Auparavant, elle affichait une invite de blocage, comme celle montrée ci-dessous.

Cependant, à partir d'aujourd'hui, elle fonctionne correctement avec un VPN.

Je me souviens qu'au lancement de l'application iOS de ChatGPT, son utilisation avec un VPN ne posait pas de problème. Plus tard, la détection des VPN est devenue plus stricte, rendant la connexion difficile. Heureusement, il semble que cette restriction ait été assouplie récemment.

Après des tests supplémentaires, j'ai constaté que lorsque j'utilisais un VPN de la région de Singapour de DigitalOcean, je ne pouvais pas accéder à l'application. Cependant, avec des VPN de Taïwan ou du Royaume-Uni (fournis par https://zhs.cloud), cela fonctionnait parfaitement.

Il semble que la détection VPN de ChatGPT iOS soit basée sur des adresses IP spécifiques. Certains fournisseurs cloud ou certaines adresses IP sont bloqués, ce qui peut expliquer le comportement incohérent en fonction de l'emplacement du serveur VPN.

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }