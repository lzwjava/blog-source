---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide du Portail WiFi des Hôtels Jinjiang
translated: true
type: note
---

Le portail WiFi des hôtels Jinjiang (https://portal.jinjianghotels.com.cn/) est un portail captif conçu pour un accès sur site uniquement—il n'est pas entièrement explorable publiquement en dehors du réseau de l'hôtel, ce qui explique pourquoi la navigation directe renvoie souvent des pages vides ou des erreurs. Sur la base de rapports d'utilisateurs et de guides, voici une analyse de sa structure typique de "routes" (c'est-à-dire les principaux chemins d'URL/points de terminaison) et comment y accéder. Ceci est courant pour les hôtels Vienna (une marque Jinjiang) et les chaînes similaires en Chine.

### Route principale et méthode d'accès
- **Route principale** : Le chemin racine `/` (c'est-à-dire https://portal.jinjianghotels.com.cn/ ou http://portal.jinjianghotels.com.cn/).
  - Il s'agit de la page d'accueil qui se charge automatiquement lorsque vous essayez d'accéder à un site web non-HTTPS tout en étant connecté au WiFi de l'hôtel.
  - **Comment y accéder** :
    1. Connectez votre appareil au SSID WiFi de l'hôtel (par exemple, "ViennaHotel", "Jinjiang_Free", ou "Vienna_Free_WiFi"—aucun mot de passe n'est requis initialement).
    2. Ouvrez un navigateur web et accédez à n'importe quel site HTTP (par exemple, http://neverssl.com ou http://172.16.16.1—l'adresse IP de la passerelle locale mentionnée dans votre première requête).
    3. Vous serez redirigé vers la page racine `/` du portail. Si la redirection automatique ne fonctionne pas, saisissez manuellement `http://172.16.16.1` ou l'URL du portail (utilisez HTTP, pas HTTPS, car les portails captifs bloquent ou ignorent souvent HTTPS).
  - La page est en chinois mais simple : Elle affiche la marque de l'hôtel, les conditions d'utilisation et des boutons de connexion. Utilisez la traduction du navigateur (par exemple, celle intégrée à Chrome) pour l'anglais.

### Sous-routes/chemins connus
Le portail utilise une structure minimale—principalement une application monopage avec des soumissions de formulaire plutôt que des sous-chemins profonds. Aucune documentation publique ne liste tous les points de terminaison, mais d'après des vidéos d'utilisateurs et des rapports de dépannage, les plus courants incluent :
- **Chemin de connexion par SMS** : Géré via un formulaire sur la racine `/` (pas de sous-route `/sms` distincte ; c'est une requête POST vers un point de terminaison interne comme `/auth/sms` ou similaire).
  - **Comment y accéder/l'utiliser** : Sur la page principale, cliquez sur le bouton SMS (短信验证). Saisissez votre numéro de téléphone (+86 pour la Chine, ou au format international). Un code arrive par SMS ; soumettez-le pour vous authentifier. L'accès expire après 24 heures.
- **Chemins de connexion sociale** : Liens ou iframes vers des points de terminaison tiers, par exemple :
  - Connexion Weibo/QQ : Redirige vers `/oauth/weibo` ou `/oauth/qq` (sous-routes temporaires pour le callback d'authentification).
  - **Comment y accéder** : Cliquez sur le bouton du réseau social respectif sur la page racine ; cela ouvre une popup ou redirige brièvement.
- **Autres sous-routes potentielles** (déduites de systèmes similaires ; non confirmées pour Jinjiang) :
  - `/terms` ou `/agreement` : Pour consulter les conditions complètes (liens dans le pied de page de la page principale).
  - `/logout` : Pour se déconnecter manuellement (rarement utilisé).
  - Chemins d'erreur comme `/error` ou 404 pour un accès invalide.

Si vous êtes sur site et avez besoin d'inspecter les sous-routes (par exemple, pour les outils de développement), ouvrez la console de développement du navigateur (F12) sur la page du portail—cela peut révéler des appels AJAX vers des points de terminaison comme `/api/verify` pour la soumission du SMS.

### Dépannage de l'accès
- **Pas de redirection ?** Effacez le cache du navigateur, oubliez/rejoignez le WiFi, ou désactivez brièvement les données mobiles.
- **Téléphone international ?** Fonctionne pour la plupart, mais les codes peuvent être retardés—demandez à la réception un code partagé.
- **Note de sécurité** : Tout le trafic passe par la passerelle de l'hôtel (plage 172.16.16.x), donc utilisez un VPN après la connexion.

Pour des visuels, consultez les courtes vidéos Douyin sur "维也纳酒店 WiFi 登录" qui montrent le flux exact de la page.

Références :  
[Reddit : Problèmes avec le WiFi dans les hôtels en Chine](https://www.reddit.com/r/travelchina/comments/1kjdngn/issues_with_wifi_connection/)  
[Douyin : Étapes pour le WiFi des hôtels Vienna](https://www.douyin.com/search/%E7%BB%B4%E4%B9%9F%E7%BA%B3%E9%85%92%E5%BA%97Wi-Fi%E8%BF%9E%E6%8E%A5%E6%AD%A5%E9%AA%A4)  
[Douyin : Guide de connexion au WiFi de l'hôtel](https://www.douyin.com/search/%E9%85%92%E5%BA%97%E6%97%A0%E7%BA%BF%E7%BD%91%E6%80%8E%E4%B9%88%E8%BF%9E%E6%8E%A5)