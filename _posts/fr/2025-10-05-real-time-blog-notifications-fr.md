---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Notifications Telegram en temps réel des visites de blog
translated: true
type: note
---

Oui, il est possible de configurer un système pour analyser les logs ou le trafic Cloudflare en quasi temps réel et envoyer des notifications Telegram pour chaque visite sur votre blog, mais ce n'est pas simple avec les logs d'analyse standard seuls. Les analyses de Cloudflare sont principalement agrégées (par exemple, des résumés quotidiens/hebdomadaires), et même leur fonctionnalité Logpush (qui exporte les logs) traite les données par lots toutes les 1 à 5 minutes, ce qui la rend inadaptée pour des alertes instantanées par visite. Instant Logs offre un streaming en temps réel mais nécessite un plan Business ou Enterprise et requerrait un traitement personnalisé (par exemple, via WebSocket et un script) pour déclencher les messages Telegram—c'est excessif pour la plupart des utilisateurs.

L'approche la plus pratique et en temps réel consiste à utiliser **Cloudflare Workers** pour intercepter chaque requête entrante vers votre blog. Cela exécute du code serverless à chaque visite, vous permettant de journaliser l'événement et d'envoyer immédiatement un message Telegram via leur API. C'est gratuit pour un trafic faible (jusqu'à 100k requêtes/jour), mais les blogs à fort trafic pourraient atteindre les limites ou engendrer des coûts—de plus, vous seriez spammé de notifications, donc envisagez un filtrage (par exemple, seulement pour les IP uniques ou des pages spécifiques).

### Étapes de configuration rapide
1. **Créer un Bot Telegram** :
   - Envoyez un message à @BotFather sur Telegram, utilisez `/newbot` pour en créer un, et notez le token du bot (par exemple, `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).
   - Démarrez une discussion avec votre bot, puis envoyez un message à @userinfobot pour obtenir votre ID de chat (par exemple, `123456789`).
   - Testez l'envoi d'un message via curl :  
     ```
     curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage" \
     -H "Content-Type: application/json" \
     -d '{"chat_id":"<YOUR_CHAT_ID>","text":"Test visit!"}'
     ```

2. **Créer un Cloudflare Worker** :
   - Connectez-vous à votre tableau de bord Cloudflare > Workers & Pages > Create application > Create Worker.
   - Nommez-le (par exemple, `blog-visit-notifier`) et déployez le modèle par défaut.

3. **Ajouter le Code de Notification** :
   - Modifiez le code du worker pour intercepter les requêtes et envoyer vers Telegram. Voici un exemple basique (remplacez les espaces réservés) :
     ```javascript
     export default {
       async fetch(request, env) {
         // Optionnel : Journaliser ou filtrer la visite (par ex., seulement pour la page d'accueil de votre blog)
         const url = new URL(request.url);
         if (url.pathname !== '/') {  // Ajustez le chemin si nécessaire
           return fetch(request);  // Ignorer les pages non concernées
         }

         // Envoyer le message Telegram (async pour ne pas bloquer)
         const message = `Nouvelle visite sur ${url.origin}! IP: ${request.headers.get('cf-connecting-ip')}, User-Agent: ${request.headers.get('user-agent')}`;
         await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({
             chat_id: env.TELEGRAM_CHAT_ID,
             text: message,
             parse_mode: 'HTML'  // Pour le formatage si nécessaire
           })
         }).catch(err => console.error('Échec envoi Telegram :', err));

         // Proxifier la requête originale vers votre blog
         return fetch(request);
       }
     };
     ```
     - Ceci s'exécute sur chaque requête correspondante, journalise les informations basiques du visiteur et les envoie via Telegram sans retarder le chargement de la page.

4. **Configurer les Variables d'Environnement** :
   - Dans les paramètres du worker > Variables > Ajouter :  
     - `TELEGRAM_BOT_TOKEN` : Votre token de bot.  
     - `TELEGRAM_CHAT_ID` : Votre ID de chat.  
   - Sauvegardez et redéployez.

5. **Router le Worker vers Votre Blog** :
   - Dans les paramètres Workers > Triggers > Add route.  
   - Définissez-la sur le domaine/chemin de votre blog (par exemple, `yourblog.com/*`).  
   - Cela garantit que le worker s'exécute à chaque visite avant d'atteindre votre serveur d'origine.

6. **Tester et Surveiller** :
   - Visitez votre blog— vous devriez recevoir un ping Telegram instantanément.  
   - Vérifiez les logs du worker dans le tableau de bord pour les erreurs. Si vous atteignez les limites de débit (par exemple, 30 msg/sec pour Telegram), ajoutez un anti-rebond avec le stockage KV.

### Alternatives si les Workers ne Conviennent Pas
- **Pour l'Analyse de Logs par Lots** : Utilisez Logpush pour exporter les logs de requêtes HTTP vers un service comme AWS S3 ou Google Pub/Sub, puis dirigez-les vers un outil comme Zapier ou n8n pour les alertes Telegram (par exemple, pour résumer les visites horaires). Pas en temps réel, cependant.
- **Intégrations** : Des outils comme Albato ou n8n peuvent connecter les webhooks Cloudflare à Telegram pour des événements plus larges, mais pas par visite.
- **Limitations** : Les Workers gratuits ont 10ms de temps CPU par requête—suffisant pour cela, mais augmentez la puissance si nécessaire. À éviter sur les sites à fort trafic sans limitation.

Cette configuration transforme votre trafic Cloudflare en alertes actionnables et instantanées. Si vous avez besoin de modifications de code ou d'aide pour les erreurs, partagez plus de détails !

[Documentation Cloudflare Workers](https://developers.cloudflare.com/workers/)  
[API Telegram Bot](https://core.telegram.org/bots/api)  
[Cloudflare Instant Logs](https://developers.cloudflare.com/logs/instant-logs/)