---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de Google Analytics
translated: true
---

Pour utiliser Google Analytics, intégrez-le dans votre projet frontend et vérifiez les données à la fois via l'application et le site web, suivez ces étapes. Ce guide suppose que votre projet frontend est soit un site web, soit une application mobile et utilise **Google Analytics 4 (GA4)**, la norme actuelle en 2023, car Universal Analytics n'est plus pris en charge pour la nouvelle collecte de données.

---

### 1. Configurer Google Analytics
Avant d'intégrer Google Analytics dans votre projet, vous devez créer un compte et le configurer :

- **Créer un Compte** : Allez sur [analytics.google.com](https://analytics.google.com) et inscrivez-vous avec votre compte Google si vous n'en avez pas déjà un.
- **Créer une Propriété GA4** :
  - Cliquez sur "Admin" dans le coin inférieur gauche.
  - Sous "Propriété", cliquez sur "Créer une propriété", remplissez les détails de votre projet et sélectionnez **Google Analytics 4**.
- **Ajouter un Flux de Données** : Selon le type de votre projet frontend :
  - **Pour un Site Web** : Choisissez "Web", entrez l'URL de votre site web et nommez le flux (par exemple, "Mon Site Web").
  - **Pour une Application Mobile** : Choisissez "App", sélectionnez iOS ou Android et fournissez les détails de votre application (par exemple, le nom du package).

Après avoir configuré le flux de données, vous obtiendrez un **ID de Mesure** (par exemple, `G-XXXXXXXXXX`), que vous utiliserez pour l'intégration.

---

### 2. Intégrer Google Analytics dans Votre Projet Frontend
Le processus d'intégration dépend de savoir si votre projet frontend est un site web ou une application mobile.

#### Pour un Site Web
- **Ajouter la Balise Google** :
  - Dans votre propriété GA4, allez dans "Flux de Données", sélectionnez votre flux web et trouvez les "Instructions de Balisage".
  - Copiez le script de **Balise Google** fourni, qui ressemble à ceci :
    ```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - Collez ce code dans la section `<head>` du HTML de votre site web, en remplaçant `YOUR_MEASUREMENT_ID` par votre ID de Mesure réel.
- **Pour les Applications à Page Unique (SPA)** (par exemple, React, Angular, Vue) :
  - Le script par défaut ne suit que le chargement initial de la page. Pour les SPA, où les pages ne se rechargent pas lors des changements de route, utilisez une bibliothèque pour suivre la navigation. Par exemple, dans **React** :
    1. Installez la bibliothèque `react-ga4` :
       ```bash
       npm install react-ga4
       ```
    2. Initialisez-la dans votre application (par exemple, dans `index.js` ou `App.js`) :
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. Suivez les vues de page lors des changements de route (par exemple, en utilisant React Router) :
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       Appelez ceci chaque fois que la route change, par exemple, dans un hook `useEffect` lié à l'emplacement du routeur.
  - Des bibliothèques similaires existent pour d'autres frameworks (par exemple, `ngx-analytics` pour Angular, `vue-ga` pour Vue — vérifiez la compatibilité avec GA4).
- **Optionnel** : Utilisez **Google Tag Manager** (GTM) au lieu de coder manuellement la balise pour une gestion plus facile des scripts de suivi.

#### Pour une Application Mobile
- **Utilisation de Firebase (Recommandé)** :
  - Si votre application utilise Firebase, activez **Google Analytics pour Firebase** :
    1. Créez un projet Firebase à [console.firebase.google.com](https://console.firebase.google.com).
    2. Ajoutez votre application au projet (iOS ou Android).
    3. Suivez les instructions pour télécharger le fichier de configuration (par exemple, `GoogleService-Info.plist` pour iOS, `google-services.json` pour Android) et ajoutez-le à votre application.
    4. Installez le SDK Firebase :
       - **iOS** : Utilisez CocoaPods (`pod 'Firebase/Analytics'`) et initialisez dans `AppDelegate`.
       - **Android** : Ajoutez les dépendances dans `build.gradle` et initialisez dans votre application.
    5. Firebase se lie automatiquement à votre propriété GA4 et commence à collecter des données.
- **Sans Firebase** :
  - Utilisez le **SDK Google Analytics autonome** pour iOS ou Android (moins courant maintenant avec l'intégration de GA4 à Firebase). Reportez-vous à la documentation officielle pour la configuration, car elle varie selon la plateforme.

---

### 3. Vérifier l'Intégration
- **Pour les Sites Web** : Après avoir ajouté le code de suivi :
  - Visitez votre site web et ouvrez le rapport **Temps Réel** dans Google Analytics (sous "Rapports" > "Temps Réel").
  - Si vous voyez votre visite enregistrée, l'intégration fonctionne.
  - Alternativement, utilisez un outil de navigateur comme **GA Checker** ou la console Chrome DevTools pour confirmer les appels `gtag`.
- **Pour les Applications** : Vérifiez la console Firebase ou le rapport Temps Réel GA4 après avoir lancé votre application avec le SDK installé. Il peut falloir quelques minutes pour que les données apparaissent.

---

### 4. Vérifier les Données via l'Application et le Site Web
Une fois que Google Analytics commence à collecter des données, vous pouvez les consulter de deux manières :
- **Interface Web de Google Analytics** :
  - Connectez-vous à [analytics.google.com](https://analytics.google.com).
  - Sélectionnez votre propriété GA4.
  - Explorez les rapports comme :
    - **Temps Réel** : Voir l'activité utilisateur en direct.
    - **Audience** : Comprendre la démographie des utilisateurs.
    - **Acquisition** : Suivre d'où viennent les utilisateurs.
    - **Comportement** : Analyser les interactions utilisateur (par exemple, vues de page, événements).
- **Application Mobile Google Analytics** :
  - Téléchargez l'application officielle **Google Analytics** depuis l'App Store (iOS) ou le Google Play Store (Android).
  - Connectez-vous avec votre compte Google et sélectionnez votre propriété.
  - Consultez un sous-ensemble de rapports (par exemple, Temps Réel, Audience) en déplacement.

---

### Notes Supplémentaires
- **Si Votre Projet Inclut à la fois un Site Web et une Application** : Vous pouvez ajouter plusieurs flux de données (par exemple, un pour le site web, un pour l'application) sous la même propriété GA4. Cela vous permet de voir des analyses combinées ou séparées dans la même interface.
- **Suivi des Événements** : Au-delà des vues de page, suivez des événements personnalisés (par exemple, clics de bouton) en utilisant `gtag('event', ...)` pour les sites web ou `logEvent` de Firebase pour les applications. Exemple pour un site web :
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 vs. Universal Analytics** : Utilisez GA4 pour les nouveaux projets, car Universal Analytics a cessé de traiter les données après le 1er juillet 2023.

En suivant ces étapes, vous intégrerez avec succès Google Analytics dans votre projet frontend et pourrez surveiller les données utilisateur à la fois via le site web et l'application Google Analytics. Si le type de votre projet (site web ou application) nécessite des clarifications spécifiques, ajustez les étapes d'intégration en conséquence !