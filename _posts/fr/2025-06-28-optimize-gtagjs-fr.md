---
audio: false
generated: true
lang: fr
layout: post
title: Optimisation des performances de gtag.js sur Jekyll GitHub Pages
translated: true
type: note
---

L'utilisation de `gtag.js` sur un site GitHub Pages construit avec Jekyll présente des contraintes particulières, car GitHub Pages offre un contrôle serveur limité et aucun accès direct aux en-têtes de cache ou au scripting côté serveur. Cependant, vous pouvez toujours optimiser la vitesse de récupération de `https://www.googletagmanager.com/gtag/js?id=UA-66656236-1` en utilisant des techniques côté client et des configurations spécifiques à Jekyll. Voici des stratégies ciblées pour améliorer ses performances dans ce contexte :

---

### 1. **Charger `gtag.js` de manière asynchrone**
Assurez-vous que le script `gtag.js` est chargé de manière asynchrone pour éviter de bloquer le rendu de la page. Dans votre site Jekyll :
- Ajoutez le script à votre mise en page Jekyll ou au fichier d'inclusion (par exemple, `_includes/analytics.html` ou directement dans votre mise en page `default.html`).
- Utilisez l'attribut `async` :
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
```
- Placez ceci dans le `<head>` ou juste avant `</body>` dans votre modèle Jekyll (par exemple, `_layouts/default.html`) :
```html
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  </script>
</head>
```
- **Pourquoi cela aide** : `async` garantit que le script ne bloque pas l'analyse HTML, réduisant le temps de chargement perçu.

---

### 2. **Ajouter Preconnect pour le domaine de Google**
Réduisez la recherche DNS et la latence de connexion en ajoutant un indice `preconnect` pour `googletagmanager.com`. Dans votre mise en page Jekyll (`_layouts/default.html` ou `_includes/head.html`) :
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
```
- Placez ceci dans le `<head>` avant le script `gtag.js`.
- **Pourquoi cela aide** : Initie la résolution DNS et la connexion TCP tôt, accélérant la récupération de `gtag.js`.

---

### 3. **Chargement différé de `gtag.js`**
Étant donné que GitHub Pages est statique, vous pouvez charger `gtag.js` de manière différée pour prioriser le contenu critique. Ajoutez le JavaScript suivant à votre modèle Jekyll ou à un fichier JS séparé (par exemple, `assets/js/analytics.js`) :
```javascript
window.addEventListener('load', () => {
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-66656236-1';
  script.async = true;
  document.head.appendChild(script);
  script.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  };
});
```
- Incluez ce script dans votre mise en page Jekyll :
```html
<script src="{{ '/assets/js/analytics.js' | relative_url }}"></script>
```
- **Pourquoi cela aide** : Retarde le chargement de `gtag.js` jusqu'à ce que les ressources critiques de la page (par exemple, HTML, CSS) soient chargées, améliorant la vitesse initiale de la page.

---

### 4. **Utiliser un proxy CDN via Cloudflare**
GitHub Pages ne permet pas d'en-têtes de cache personnalisés, mais vous pouvez proxifier `gtag.js` via un CDN comme Cloudflare pour le mettre en cache plus près de vos utilisateurs :
1. **Configurer Cloudflare** :
   - Ajoutez votre site GitHub Pages à Cloudflare (par exemple, `username.github.io`).
   - Activez le DNS et le proxying de Cloudflare pour votre domaine.
2. **Proxifier `gtag.js`** :
   - Créez une Règle de Page dans Cloudflare pour mettre en cache le script `gtag.js` ou hébergez une copie locale dans le dossier `_site` de votre site Jekyll (par exemple, `assets/js/gtag.js`).
   - Mettez à jour votre balise de script :
```html
<script async src="{{ '/assets/js/gtag.js' | relative_url }}"></script>
```
   - Synchronisez la copie locale avec le `gtag.js` de Google périodiquement pour garantir sa mise à jour (processus manuel ou via un script CI/CD).
3. **Paramètres de cache** :
   - Dans Cloudflare, définissez une règle de cache pour le script (par exemple, `Cache Everything` avec un TTL de 1 heure).
- **Pourquoi cela aide** : Les serveurs edge de Cloudflare réduisent la latence en servant le script depuis un emplacement plus proche de vos utilisateurs.
- **Note** : Soyez prudent avec le proxying des scripts Google, car ils peuvent être mis à jour fréquemment. Testez minutieusement pour garantir le fonctionnement du suivi.

---

### 5. **Optimiser la construction et la livraison Jekyll**
Assurez-vous que votre site Jekyll est optimisé pour minimiser le temps de chargement global de la page, ce qui aide indirectement les performances de `gtag.js` :
- **Minifier les assets** :
  - Utilisez un plugin Jekyll comme `jekyll-compress` ou `jekyll-minifier` pour minifier le HTML, CSS et JS.
  - Ajoutez à votre `_config.yml` :
```yaml
plugins:
  - jekyll-compress
```
- **Activer la compression Gzip** :
  - GitHub Pages active automatiquement Gzip pour les fichiers pris en charge, mais vérifiez que vos fichiers CSS/JS sont compressés en vérifiant l'en-tête `Content-Encoding` dans les outils de développement du navigateur.
- **Réduire les ressources bloquantes** :
  - Minimisez le nombre de fichiers CSS/JS bloquant le rendu chargés avant `gtag.js`.
  - Utilisez `jekyll-assets` ou similaire pour optimiser la livraison des assets :
```yaml
plugins:
  - jekyll-assets
```
- **Inline Critical CSS** :
  - Intégrez le CSS critique dans le `<head>` et différez le CSS non critique pour réduire le temps de blocage du rendu, ce qui peut donner l'impression que `gtag.js` se charge plus vite.
- **Optimisation des images** :
  - Compressez les images en utilisant `jekyll-picture-tag` ou un plugin similaire pour réduire le poids total de la page, libérant de la bande passante pour `gtag.js`.

---

### 6. **Passer à une analytique minimale**
Si `gtag.js` reste lent ou si l'analytique n'est pas critique :
- Envisagez des alternatives légères comme Plausible ou Fathom, qui utilisent des scripts plus petits (~1 Ko contre ~50 Ko pour `gtag.js`).
- Exemple pour Plausible :
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```
- Ajoutez ceci à votre `_includes/analytics.html` Jekyll et incluez-le dans votre mise en page.
- **Pourquoi cela aide** : Les scripts plus petits se chargent plus rapidement, surtout sur l'infrastructure statique de GitHub Pages.

---

### 7. **Tester et surveiller les performances**
- **Mesurer le temps de récupération** :
  - Utilisez Chrome DevTools (onglet Network) pour vérifier le temps de chargement de `gtag.js`.
  - Testez avec des outils comme Lighthouse ou WebPageTest pour évaluer les performances globales de la page.
- **Simuler les emplacements des utilisateurs** :
  - Utilisez un outil comme Pingdom pour tester les temps de chargement depuis les régions où se trouve votre audience, car les performances du CDN de GitHub Pages et de Google varient géographiquement.
- **Surveiller les métriques des utilisateurs réels** :
  - Si vous utilisez Google Analytics, vérifiez le rapport Site Speed pour suivre l'impact de `gtag.js`.
- **Débogage spécifique à Jekyll** :
  - Exécutez `jekyll build --profile` pour identifier les composants à construction lente dans votre site qui pourraient indirectement affecter les performances.

---

### 8. **Limitations avec GitHub Pages**
- **Aucun contrôle côté serveur** : GitHub Pages est un hôte statique, vous ne pouvez donc pas implémenter le tagging côté serveur ou des en-têtes de cache personnalisés pour `gtag.js`.
- **Pas de HTTP/3** : GitHub Pages utilise HTTP/2, qui est rapide mais pas aussi optimisé que HTTP/3. Un CDN comme Cloudflare peut passer à HTTP/3.
- **Latence géographique** : Les serveurs GitHub Pages sont principalement basés aux États-Unis, donc les utilisateurs éloignés des États-Unis peuvent connaître des chargements plus lents. Un CDN atténue ce problème.

---

### Exemple de configuration Jekyll
Voici un exemple de `_includes/analytics.html` pour votre site Jekyll combinant `preconnect` et `async` :
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-66656236-1');
</script>
```
Incluez-le dans votre mise en page (`_layouts/default.html`) :
```html
<head>
</head>
```

---

### Prochaines étapes
- **Tester les performances actuelles** : Partagez le temps de récupération actuel pour `gtag.js` (depuis les outils de développement du navigateur) ou l'URL de votre site, et je pourrai l'analyser plus en détail.
- **Contexte géographique** : Indiquez-moi la localisation principale de votre audience (par exemple, États-Unis, Europe, Asie) pour adapter les recommandations de CDN ou de proxy.
- **Configuration Cloudflare** : Si vous êtes ouvert à utiliser Cloudflare, je peux fournir des étapes détaillées pour proxifier `gtag.js`.
- **Analytique alternative** : Si vous êtes ouvert à changer de Google Analytics, je peux recommander des outils légers spécifiques et leur intégration Jekyll.

Souhaitez-vous que je me concentre sur l'un de ces aspects ou que j'effectue une analyse spécifique (par exemple, tester les performances de votre site ou fournir un guide de configuration Cloudflare) ?