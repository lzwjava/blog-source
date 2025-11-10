---
audio: false
generated: true
lang: fr
layout: post
title: Guide des analyses Web axées sur la confidentialité
translated: true
type: note
---

Cloudflare Web Analytics est un outil gratuit axé sur la confidentialité, conçu pour aider les propriétaires de sites web à suivre et à comprendre les performances du site et le comportement des visiteurs sans compromettre la vie privée des utilisateurs. Voici un guide complet pour configurer et utiliser Cloudflare Web Analytics, basé sur les dernières informations disponibles.

### Aperçu de Cloudflare Web Analytics
Cloudflare Web Analytics fournit des informations sur le trafic du site web, les pages vues et les métriques de performance tout en priorisant la vie privée des utilisateurs. Contrairement aux outils d'analyse traditionnels qui peuvent suivre les données personnelles ou utiliser des cookies, la solution de Cloudflare évite les méthodes de suivi invasives comme l'empreinte numérique, les cookies ou le stockage local à des fins d'analyse. Elle convient aux sites web de toutes tailles et peut être utilisée avec ou sans les services de proxy de Cloudflare.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)

### Fonctionnalités Clés
- **Priorité à la Confidentialité** : Ne collecte pas de données personnelles, n'utilise pas de cookies et ne suit pas les utilisateurs via les adresses IP ou les user agents, garantissant ainsi la conformité avec des réglementations comme le RGPD.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Deux Méthodes de Collecte de Données** :
  - **Balise JavaScript** : Un snippet JavaScript léger collecte les métriques côté client en utilisant l'API Performance du navigateur. Idéal pour des données détaillées de Real User Monitoring (RUM), telles que les temps de chargement des pages et les Core Web Vitals.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
  - **Analytics Edge** : Collecte les données côté serveur à partir des serveurs edge de Cloudflare pour les sites proxyés via Cloudflare. Aucune modification de code n'est nécessaire, et elle capture toutes les requêtes, y compris celles des bots ou des utilisateurs ayant désactivé JavaScript.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **Métriques Fournies** : Suit les pages vues, les visites, les pages les plus populaires, les référents, les pays, les types d'appareils, les codes d'état et les métriques de performance comme les temps de chargement des pages.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Adaptive Bit Rate (ABR)** : Ajuste automatiquement la résolution des données en fonction de la taille des données, de la plage de dates et des conditions du réseau pour des performances optimales.[](https://developers.cloudflare.com/web-analytics/about/)
- **Gratuit** : Disponible pour toute personne ayant un compte Cloudflare, même sans changer le DNS ou utiliser le proxy de Cloudflare.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Tableau de bord et Filtres** : Offre un tableau de bord intuitif pour visualiser et filtrer les données par hostname, URL, pays et plage horaire. Vous pouvez zoomer sur des périodes spécifiques ou regrouper les données pour une analyse plus approfondie.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)
- **Prise en charge des Applications Monopages (SPA)** : Suit automatiquement les changements de route dans les SPA en remplaçant la fonction `pushState` de l'History API (les routeurs basés sur le hachage ne sont pas pris en charge).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### Limitations
- **Rétention des Données** : Limitée à 30 jours de données historiques, ce qui peut ne pas convenir aux utilisateurs ayant besoin d'analyses à long terme.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Échantillonnage des Données** : Les métriques sont basées sur un échantillon de 10 % des événements de chargement de page, ce qui peut entraîner des inexactitudes par rapport à des outils comme Plausible ou Fathom Analytics.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Problèmes d'Exactitude** : L'analyse côté serveur (edge analytics) peut inclure le trafic des bots, gonflant les chiffres par rapport à l'analyse côté client comme Google Analytics. L'analyse côté client peut manquer des données des utilisateurs ayant désactivé JavaScript ou utilisant des bloqueurs de publicités.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
- **Absence de Prise en charge des Paramètres UTM** : Actuellement, les chaînes de requête comme les paramètres UTM ne sont pas enregistrées pour éviter de collecter des données sensibles.[](https://developers.cloudflare.com/web-analytics/faq/)
- **Limitations à l'Exportation** : Aucun moyen direct d'exporter les données (par exemple, vers CSV), contrairement à certains concurrents comme Fathom Analytics.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Analytique Basique** : Manque de fonctionnalités avancées comme le suivi des conversions ou l'analyse détaillée du parcours utilisateur par rapport à Google Analytics.[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)

### Configuration de Cloudflare Web Analytics
#### Prérequis
- Un compte Cloudflare (gratuit à créer sur cloudflare.com).
- L'accès au code de votre site web (pour la balise JavaScript) ou aux paramètres DNS (pour l'analyse edge si vous utilisez le proxy de Cloudflare).

#### Étapes de Configuration
1. **Se connecter au Tableau de bord Cloudflare** :
   - Allez sur [cloudflare.com](https://www.cloudflare.com) et connectez-vous ou créez un compte.
   - À partir de la page d'accueil du compte, naviguez vers **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/web-analytics/get-started/)

2. **Ajouter un Site** :
   - Cliquez sur **Add a site** dans la section Web Analytics.
   - Entrez le hostname de votre site web (par exemple, `example.com`) et sélectionnez **Done**.[](https://developers.cloudflare.com/web-analytics/get-started/)

3. **Choisir la Méthode de Collecte de Données** :
   - **Balise JavaScript (Recommandé pour les Sites Non Proxyés)** :
     - Copiez le snippet JavaScript fourni dans la section **Manage site**.
     - Collez-le dans le HTML de votre site web avant la balise fermante `</body>`. Assurez-vous que votre site a un HTML valide pour que le snippet fonctionne.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
     - Pour les Applications Monopages, assurez-vous que `spa: true` est présent dans la configuration pour le suivi automatique des routes (les routeurs basés sur le hachage ne sont pas pris en charge).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
     - Exemple pour les applications Nuxt : Utilisez le composable `useScriptCloudflareWebAnalytics` ou ajoutez le token à votre configuration Nuxt pour un chargement global.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
   - **Analytics Edge (Pour les Sites Proxyés)** :
     - Proxyez votre site web via Cloudflare en mettant à jour vos paramètres DNS pour qu'ils pointent vers les nameservers de Cloudflare. Cela peut être fait en quelques minutes et ne nécessite aucune modification de code.[](https://www.cloudflare.com/en-in/web-analytics/)
     - Les métriques apparaîtront dans le tableau de bord Cloudflare sous **Analytics & Logs**.[](https://developers.cloudflare.com/web-analytics/faq/)
   - **Cloudflare Pages** :
     - Pour les projets Pages, activez Web Analytics en un clic : Depuis **Workers & Pages**, sélectionnez votre projet, allez dans **Metrics**, et cliquez sur **Enable** sous Web Analytics.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/get-started/)

4. **Vérifier la Configuration** :
   - Les données peuvent prendre quelques minutes à apparaître dans le tableau de bord. Vérifiez la section **Web Analytics Sites** pour confirmer que le site est ajouté.[](https://developers.cloudflare.com/web-analytics/get-started/)
   - Si vous utilisez l'analyse edge, assurez-vous que la propagation DNS est terminée (cela peut prendre 24 à 72 heures).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)

5. **Configurer des Règles (Optionnel)** :
   - Configurez des règles pour suivre des sites web ou des chemins spécifiques. Utilisez les dimensions pour catégoriser les métriques (par exemple, par hostname ou URL).[](https://developers.cloudflare.com/web-analytics/)

#### Notes
- Si votre site a un en-tête `Cache-Control: public, no-transform`, la balise JavaScript ne sera pas injectée automatiquement et Web Analytics pourrait ne pas fonctionner. Ajustez vos paramètres de cache ou ajoutez le snippet manuellement.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
- Certains bloqueurs de publicités peuvent bloquer la balise JavaScript, mais l'analyse edge n'est pas affectée car elle repose sur les logs serveur.[](https://developers.cloudflare.com/web-analytics/faq/)
- Pour une configuration manuelle, la balise envoie des données à `cloudflareinsights.com/cdn-cgi/rum` ; pour les sites proxyés, elle utilise le endpoint `/cdn-cgi/rum` de votre domaine.[](https://developers.cloudflare.com/web-analytics/faq/)

### Utilisation de Cloudflare Web Analytics
1. **Accéder au Tableau de bord** :
   - Connectez-vous au tableau de bord Cloudflare, sélectionnez votre compte et domaine, et allez dans **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/analytics/types-of-analytics/)
   - Visualisez les métriques comme les pages vues, les visites, les pages les plus populaires, les référents, les pays, les types d'appareils et les données de performance (par exemple, les temps de chargement des pages, les Core Web Vitals).[](https://www.cloudflare.com/en-in/web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)

2. **Filtrer et Analyser les Données** :
   - Utilisez les filtres pour vous concentrer sur des métriques spécifiques (par exemple, par hostname, URL ou pays).
   - Zoomez sur des plages horaires pour enquêter sur des pics de trafic ou regroupez les données par des métriques comme les référents ou les pages.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - Pour les utilisateurs avancés, interrogez les données via l'**API GraphQL Analytics** pour créer des tableaux de bord personnalisés.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)

3. **Comprendre les Métriques Clés** :
   - **Pages Vues** : Nombre total de fois où une page est chargée (type de contenu HTML avec réponse HTTP réussie).[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)
   - **Visites** : Pages vues à partir d'un référent différent (ne correspondant pas au hostname) ou de liens directs.[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - **Visiteurs Uniques** : Basé sur les adresses IP, mais non stocké pour des raisons de confidentialité. Peut être plus élevé que dans d'autres outils en raison du trafic des bots ou de l'absence de déduplication basée sur JavaScript.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)
   - **Métriques de Performance** : Inclut les temps de chargement des pages, le first paint et les Core Web Vitals (côté client uniquement).[](https://usefathom.com/features/vs-cloudflare-web-analytics)

4. **Comparer avec d'Autres Outils** :
   - Contrairement à Google Analytics, Cloudflare ne suit pas les parcours utilisateur ou les conversions mais inclut le trafic des bots et des menaces, ce qui peut gonfler les chiffres (20 à 50 % du trafic pour la plupart des sites).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.cloudflare.com/insights/)
   - Comparé à Plausible ou Fathom Analytics, les données de Cloudflare sont moins granulaires en raison de l'échantillonnage et de la rétention limitée.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
   - L'analyse edge peut afficher des chiffres plus élevés que les outils côté client comme Google Analytics, qui excluent les bots et les requêtes sans JavaScript.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/CloudFlare/comments/1alzkwm/why_are_my_cloudflare_traffic_stats_so_different/)

### Bonnes Pratiques
- **Choisir la Bonne Méthode** : Utilisez la balise JavaScript pour des métriques axées sur la confidentialité côté client ou l'analyse edge pour des données côté serveur complètes si votre site est proxyé.[](https://www.cloudflare.com/web-analytics/)
- **Combiner avec d'Autres Outils** : Associez avec Google Analytics ou des alternatives axées sur la confidentialité comme Plausible ou Fathom pour des insights plus profonds, car l'analyse de Cloudflare est basique.[](https://www.cloudflare.com/insights/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Surveiller les Performances** : Utilisez les métriques de performance pour identifier les pages à chargement lent et tirez parti des recommandations de Cloudflare (par exemple, les optimisations de cache).[](https://developers.cloudflare.com/web-analytics/)
- **Vérifier les Problèmes de Bloqueurs de Publicités** : Si vous utilisez la balise JavaScript, informez les utilisateurs d'autoriser `cloudflare.com` ou de désactiver les bloqueurs de publicités pour assurer la collecte de données.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
- **Examiner Régulièrement les Données** : Vérifiez fréquemment le tableau de bord pour repérer les tendances ou les anomalies, car les données ne sont conservées que 30 jours.[](https://plausible.io/vs-cloudflare-web-analytics)

### Dépannage
- **Aucune Donnée Affichée** :
  - Vérifiez que le snippet JavaScript est correctement placé et que le site a un HTML valide.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
  - Pour l'analyse edge, assurez-vous que le DNS pointe vers Cloudflare (la propagation peut prendre 24 à 72 heures).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
  - Vérifiez la présence d'en-têtes `Cache-Control: no-transform` bloquant l'injection automatique de la balise.[](https://developers.cloudflare.com/web-analytics/get-started/)
- **Statistiques Imprécises** :
  - L'analyse edge inclut le trafic des bots, gonflant les chiffres. Utilisez l'analyse côté client pour des décomptes de visiteurs plus précis.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
  - L'échantillonnage des données (10 %) peut causer des écarts. Prenez cela en compte lors de la comparaison avec d'autres outils.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Problèmes de Bloqueurs de Publicités** : Certaines extensions de navigateur bloquent la balise JavaScript. L'analyse edge n'est pas affectée par cela.[](https://developers.cloudflare.com/web-analytics/faq/)
- **Métriques SPA Manquantes** : Assurez-vous que la prise en charge SPA est activée (`spa: true`) et évitez les routeurs basés sur le hachage.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### Utilisation Avancée
- **API GraphQL Analytics** : Pour une analyse personnalisée, interrogez l'API de Cloudflare pour créer des tableaux de bord sur mesure ou intégrer avec d'autres systèmes. Nécessite une expertise technique.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)
- **Cloudflare Workers** : Envoyez les données d'analyse vers une base de données time-series pour un traitement personnalisé ou utilisez Workers pour une analyse serverless avancée.[](https://developers.cloudflare.com/analytics/)
- **Insights de Sécurité** : Combinez avec Security Analytics de Cloudflare pour surveiller les menaces et les bots parallèlement aux données des visiteurs.[](https://www.cloudflare.com/insights/)[](https://developers.cloudflare.com/waf/analytics/security-analytics/)

### Comparaison avec les Alternatives
- **Google Analytics** : Offre un suivi détaillé du parcours utilisateur et des conversions mais repose sur les cookies et JavaScript, qui peuvent être bloqués. Cloudflare est plus simple et axé sur la confidentialité mais moins riche en fonctionnalités.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Plausible Analytics** : Open-source, axé sur la confidentialité, avec une rétention de données illimitée et sans échantillonnage. Plus précis pour les visiteurs uniques mais nécessite un plan payant.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Fathom Analytics** : Similaire à Plausible, avec des données exportables et des fonctionnalités avancées comme le suivi des campagnes. L'offre gratuite de Cloudflare est moins robuste mais plus facile à configurer pour les besoins basiques.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Jetpack Stats** : Spécifique à WordPress, avec une rétention de données limitée (28 jours) et aucun suivi au niveau utilisateur. Même orientation vers la confidentialité mais moins flexible que Cloudflare.[](https://wordpress.com/support/stats/)

### Ressources Supplémentaires
- **Documentation Officielle** : [Cloudflare Web Analytics Docs](https://developers.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
- **Guide de Configuration** : [Activation de Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/get-started/)
- **FAQ** : [FAQ Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/faq/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **Article de Blog** : [Cloudflare’s Privacy-First Web Analytics](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Support Communautaire** : Consultez les forums de la communauté Cloudflare pour une aide supplémentaire.[](https://developers.cloudflare.com/web-analytics/faq/)

### Conclusion
Cloudflare Web Analytics est un excellent choix pour les propriétaires de sites web recherchant un outil d'analyse gratuit et axé sur la confidentialité avec une configuration minimale. Il est idéal pour la surveillance basique du trafic et des performances mais peut être limité pour les besoins avancés en raison de l'échantillonnage des données, de la rétention limitée et du manque de fonctionnalités comme le suivi des conversions. Pour des insights plus profonds, envisagez de le combiner avec des outils comme Plausible ou Fathom Analytics. Vérifiez toujours l'exactitude de la configuration et soyez conscient des limites lors de l'interprétation des données.

Si vous avez besoin d'une aide spécifique pour la configuration ou si vous avez des questions sur l'intégration de Cloudflare Web Analytics à votre site, faites-le moi savoir !