---
audio: false
generated: true
image: true
lang: fr
layout: post
title: Comment Regarder YouTube à la Télévision
translated: true
type: post
---

Ce guide suppose que vous avez déjà un moyen de contourner les restrictions géographiques. Voici comment regarder YouTube sur votre TV sans flasher de firmware personnalisé sur votre routeur – il suffit d’utiliser une application.

---

## **SmartYouTubeTV**

![SmartYouTubeTV](assets/images/youtube-tv/smart.jpg)

1. **Télécharger et installer** :
   Téléchargez l’application et installez-la sur votre TV via une clé USB (sideload).

2. **Configurer le proxy** :
   - Sur votre client proxy (ex. : Clash), activez **« Autoriser les connexions depuis le LAN»** pour permettre aux appareils du réseau local de router le trafic via votre machine.
   - Dans **SmartYouTubeTV**, allez dans les paramètres et entrez les détails de votre proxy (ex. : `192.168.1.3:7890`).
     *Remarque* : Utilisez **SOCKS5** (les proxys HTTP ont échoué lors des tests). Remplacez `192.168.1.3` par l’IP locale de votre machine.

3. **Tester et confirmer** :
   Cliquez sur **« Test»** dans l’application pour vérifier la connectivité. Si le test réussit, enregistrez les paramètres et commencez le streaming.

![Configuration du proxy](assets/images/youtube-tv/proxy1.jpeg)
![Succès](assets/images/youtube-tv/tan.jpeg)

---

## **gfreezy/seeker (Proxy transparent)**
Un projet GitHub qui transforme votre ordinateur en une passerelle proxy utilisant **TUN** (similaire aux modes enhanced/gateway de Surge). Voici les points clés et une configuration fonctionnelle :

### **Configuration (`config.yml`)**
```yml
verbose: true
dns_start_ip: 10.0.0.10
dns_servers:
  - 223.5.5.5:53
  - 114.114.114.114:53
dns_timeout: 1s
tun_name: utun4
tun_ip: 10.0.0.1
tun_cidr: 10.0.0.0/16
dns_listen: 0.0.0.0:53
gateway_mode: true
ping_timeout: 2s
probe_timeout: 30ms
connect_timeout: 1s
read_timeout: 30s
write_timeout: 5s
max_connect_errors: 2

servers:
  - name: http proxy server
   addr: 0.0.0.0:7890
   protocol: Http
  - name: https proxy server
   addr: 0.0.0.0:7890
   protocol: Https

rules:
  - 'MATCH,PROXY'
```

### **Pourquoi pas SOCKS5 ?**
J’ai d’abord tenté SOCKS5 :
```yml
servers:
  - name: socks5 proxy server
   addr: 0.0.0.0:7891
   protocol: Socks5
```
Mais cela provoquait des **boucles de connexion** (selon la [documentation](https://github.com/gfreezy/seeker)), nécessitant des règles explicites pour les connexions directes vers certains domaines. Les proxys **HTTP/HTTPS** étaient plus stables.

### **Compromis**
- **Seeker** : Nécessite une machine dédiée agissant comme routeur.
- **Mode Proxy (SmartYouTubeTV)** : Plus flexible – fonctionne avec des téléphones/tablettes partageant un port proxy.

![Seeker](assets/images/youtube-tv/seeker.jpg)

---

## **Captures d’écran TV (Xiaomi TV)**
Pour capturer des captures d’écran :
1. **Appuyez deux fois sur le bouton `Home`** de la télécommande pour ouvrir le gestionnaire d’applications.
2. Sélectionnez le **bouton de capture d’écran** et partagez via WeChat (ou d’autres applications).
3. Utilisez ce menu pour **forcer la fermeture des applications bloquées**.

![Capture TV](assets/images/youtube-tv/tv_screen.jpeg)

---

Profitez de l’expérience grand écran !

---

## **Mise à jour (septembre 2025)**

Apple TV supporte désormais les logiciels VPN nativement. Vous pouvez installer **Shadowrocket** pour vous connecter à votre serveur proxy et diffuser YouTube TV directement.