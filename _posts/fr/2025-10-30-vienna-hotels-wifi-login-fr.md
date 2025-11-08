---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Connexion au WiFi des Hôtels de Vienne
translated: true
type: note
---

Le WiFi des hôtels Vienna (appartenant au groupe Jinjiang International) utilise un système de portail captif standard pour l'authentification des clients, courant dans les hôtels chinois. L'adresse IP de la passerelle (172.16.16.1) est l'adresse interne du routeur, et y accéder (ou accéder à tout site non-HTTPS) vous redirige vers la page de connexion à l'adresse portal.jinjianghotels.com.cn. Voici comment fonctionne la connexion par SMS — c'est simple et sécurisé pour une navigation basique, bien que certains utilisateurs s'inquiètent de la confidentialité des données (c'est géré par l'hôtel, donc utilisez un VPN si vous êtes paranoïaque).

### Procédure étape par étape :
1.  **Connectez-vous au réseau WiFi** : Sur votre appareil (téléphone, ordinateur portable, etc.), recherchez et rejoignez le SSID WiFi de l'hôtel (souvent quelque chose comme "Vienna_Free_WiFi" ou "Jinjiang_WiFi"). Aucun mot de passe n'est généralement nécessaire pour se connecter.

2.  **Déclenchez le portail** : Ouvrez n'importe quel navigateur web et essayez de charger un site (par exemple, google.com ou baidu.com). Vous serez automatiquement redirigé vers la page du portail Jinjiang (cela peut prendre quelques secondes ; sinon, tapez manuellement `http://172.16.16.1` ou `http://portal.jinjianghotels.com.cn` dans la barre d'adresse). La page est en chinois, mais vous pouvez utiliser Google Traduction ou un outil similaire pour vous aider.

3.  **Choisissez la méthode d'authentification** : Le portail propose quelques options, telles que :
    *   Vérification par SMS (短信验证 — la plus simple pour la plupart des clients).
    *   Connexion via les réseaux sociaux (par exemple, Weibo, QQ).
    *   Parfois une option en un clic si vous êtes membre enregistré chez Jinjiang.

4.  **Détails de la connexion par SMS** :
    *   Sélectionnez l'option SMS.
    *   Entrez votre numéro de téléphone portable (les numéros chinois commencent par +86 ; les numéros internationaux comme +1 pour les États-Unis devraient fonctionner mais peuvent entraîner des frais d'itinérance pour la réception du SMS).
    *   Cliquez sur "Envoyer le code" (发送验证码). Vous recevrez un code à 4-6 chiffres par SMS du système de l'hôtel (généralement instantané, provenant d'un numéro court comme 106XXXX).
    *   Saisissez le code sur le portail.
    *   Cliquez sur "Confirmer" ou "Se connecter" (立即连接). S'il est valide, vous obtiendrez un accès complet à Internet pour 24 heures (ou jusqu'à votre départ).

### Conseils et Dépannage :
*   **Pas de redirection ?** Oubliez le réseau, reconnectez-vous et effacez le cache/les cookies de votre navigateur. Sur mobile, activez brièvement le mode avion.
*   **Le code n'arrive pas ?** Vérifiez le signal (le WiFi de l'hôtel est séparé des données mobiles), attendez 60 secondes pour réessayer, ou demandez de l'aide à la réception — ils ont souvent un code partagé.
*   **Problèmes avec un numéro étranger ?** Cela fonctionne pour la plupart des opérateurs internationaux, mais en cas de blocage, essayez la connexion via les réseaux sociaux ou demandez un bon d'accès à la chambre au personnel.
*   **Vitesse/Sécurité** : Attendez-vous à des vitesses correctes après la connexion, mais c'est un réseau public — évitez les connexions sensibles sans VPN. Aucun signalement majeur d'arnace concernant ce portail.

Si vous êtes bloqué sur place, le personnel de la réception peut vous faire une démonstration (apportez votre téléphone). Pour plus de visuels, recherchez "锦江酒店 WiFi 登录" sur Douyin (le TikTok chinois) pour des vidéos rapides.