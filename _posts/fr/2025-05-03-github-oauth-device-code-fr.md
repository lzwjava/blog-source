---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Flux de code d’appareil OAuth GitHub
translated: true
type: note
---

### Aperçu

Ce code JavaScript implémente le flux d'autorisation d'appareil OAuth 2.0 (également appelé Device Code grant) pour s'authentifier auprès de GitHub et obtenir un jeton d'accès. Ce flux est généralement utilisé pour les applications sans interface utilisateur directe (par exemple, les outils CLI ou les systèmes embarqués) où l'utilisateur ne peut pas interagir directement avec un navigateur web pour approuver l'authentification.

Dans ce cas précis, il semble imiter les requêtes du plugin GitHub Copilot (par exemple, pour Neovim ou Vim), en utilisant des en-têtes qui usurpent l'identité d'un client Copilot pour potentiellement s'intégrer ou accéder au système d'authentification de GitHub. L'objectif est de générer un jeton d'accès qui pourrait être utilisé pour des appels à l'API GitHub nécessitant une authentification utilisateur, comme la lecture des informations utilisateur (comme l'indique le `scope: "read:user"`).

Ce code s'exécute comme un script Node.js, utilisant `fetch` pour les requêtes HTTP et `process` pour les variables d'environnement. Il suppose que Node.js a `fetch` disponible (comme dans les versions plus récentes ou via un polyfill). En cas de succès, il interroge périodiquement les serveurs de GitHub jusqu'à ce que l'utilisateur autorise la demande ou que le délai d'attente soit dépassé.

**Notes importantes :**
- Ce code nécessite de définir une variable d'environnement `MY_COPILOT_CLIENT_ID`, probablement un ID client d'application OAuth GitHub enregistré pour GitHub Copilot.
- Il gère les erreurs de manière minimale – par exemple, si la récupération échoue, il journalise l'erreur et continue ou quitte.
- D'un point de vue sécurité, stocker ou journaliser les jetons d'accès est risqué (ils accordent un accès à l'API). Ce code imprime directement l'objet complet du jeton dans la console, ce qui pourrait poser un problème de confidentialité/sécurité dans un usage réel. Les jetons d'accès doivent être gérés de manière sécurisée (par exemple, stockés chiffrés et renouvelés).
- Le flux implique une interaction utilisateur : L'utilisateur doit visiter une URL et saisir un code sur le site de GitHub pour autoriser l'accès.
- Ceci n'est pas un code de documentation "officiel" de GitHub ; il semble avoir été rétro-conçu à partir du comportement de GitHub Copilot. Utilisez les API de manière responsable et conformément aux conditions d'utilisation de GitHub.

### Détail étape par étape

#### 1. Vérification de l'environnement
```javascript
const clientId = process.env.MY_COPILOT_CLIENT_ID;

if (!clientId) {
  console.error("MY_COPILOT_CLIENT_ID is not set");
  process.exit(1);
}
```
- Récupère `MY_COPILOT_CLIENT_ID` à partir des variables d'environnement (par exemple, défini via `export MY_COPILOT_CLIENT_ID=your_client_id` dans votre shell).
- Si la variable n'est pas définie, il journalise une erreur et quitte le script (le code de sortie 1 indique un échec).
- Cet ID client provient d'une application OAuth GitHub enregistrée (nécessaire pour les flux OAuth).

#### 2. Configuration des en-têtes communs
```javascript
const commonHeaders = new Headers();
commonHeaders.append("accept", "application/json");
commonHeaders.append("editor-version", "Neovim/0.6.1");
commonHeaders.append("editor-plugin-version", "copilot.vim/1.16.0");
commonHeaders.append("content-type", "application/json");
commonHeaders.append("user-agent", "GithubCopilot/1.155.0");
commonHeaders.append("accept-encoding", "gzip,deflate,b");
```
- Crée un objet `Headers` avec des paires clé-valeur pour les requêtes HTTP.
- Ces en-têtes font paraître les requêtes comme provenant du plugin Vim GitHub Copilot (version 1.16.0 pour Neovim 0.6.1). Cela vise probablement à usurper l'user-agent et à imiter les appels API de Copilot, ce qui pourrait être nécessaire ou utile pour que GitHub accepte les requêtes.
- `"accept": "application/json"` : Attend des réponses au format JSON.
- `"content-type": "application/json"` : Envoie des données JSON dans le corps des requêtes.
- `"accept-encoding"` : Autorise la compression gzip/deflate pour économiser la bande passante.

#### 3. Fonction `getDeviceCode()`
```javascript
async function getDeviceCode() {
  const raw = JSON.stringify({
    "client_id": clientId,
    "scope": "read:user",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  const data = await fetch(
    "https://github.com/login/device/code",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
  return data;
}
```
- **Objectif** : Initie le flux Device Code en demandant un code d'appareil à GitHub.
- Construit une charge utile JSON avec :
  - `client_id` : L'ID client OAuth (pour l'authentification de votre application).
  - `scope` : `"read:user"` – limite le jeton à la lecture des informations de base du profil utilisateur (par exemple, le nom d'utilisateur, l'e-mail via l'API GitHub). Il s'agit d'une portée minimale.
- Effectue une requête POST vers `https://github.com/login/device/code` (le point de terminaison de code d'appareil OAuth de GitHub).
- Analyse la réponse JSON (champs attendus : `device_code`, `user_code`, `verification_uri`, `expires_in` – non affichés dans le code, mais standard pour ce flux).
- En cas d'erreur (par exemple, problèmes de réseau), la journalise mais continue (pourrait retourner `undefined`).
- Retourne l'objet de données JSON analysé provenant de GitHub.

#### 4. Fonction `getAccessToken(deviceCode: string)`
```javascript
async function getAccessToken(deviceCode: string) {
  const raw = JSON.stringify({
    "client_id": clientId,
    "device_code": deviceCode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  return await fetch(
    "https://github.com/login/oauth/access_token",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
}
```
- **Objectif** : Interroge périodiquement GitHub pour échanger le code d'appareil contre un jeton d'accès une fois que l'utilisateur l'a autorisé.
- Prend le `device_code` de l'étape précédente.
- Construit un JSON avec :
  - `client_id` : Identique à précédemment.
  - `device_code` : Le code unique identifiant cette tentative d'authentification/appareil.
  - `grant_type` : Spécifie qu'il s'agit d'un Device Code grant (URN OAuth2 standard).
- Effectue une requête POST vers `https://github.com/login/oauth/access_token`.
- Retourne la réponse JSON analysée, qui pourrait être :
  - En cas de succès : `{ access_token: "...", token_type: "bearer", scope: "read:user" }`.
  - En attente/erreur : `{ error: "...", error_description: "..." }` (par exemple, "authorization_pending" ou "slow_down").
- Les erreurs (par exemple, échecs de `fetch`) sont journalisées mais pas explicitement gérées, donc l'appelant doit vérifier la valeur de retour.

#### 5. Exécution principale (Fonction asynchrone immédiatement invoquée)
```javascript
(async function () {
  const { device_code, user_code, verification_uri, expires_in } =
    await getDeviceCode();
  console.info(`enter user code:\n${user_code}\n${verification_uri}`);
  console.info(`Expires in ${expires_in} seconds`);
  while (true) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const accessToken = await getAccessToken(device_code);
    if (accessToken.error) {
      console.info(`${accessToken.error}: ${accessToken.error_description}`);
    }
    if (accessToken.access_token) {
      console.info(`access token:\n${JSON.stringify(accessToken, null, 1)}`);
      break;
    }
  }
})();
```
- **Flux général** : Orchestre l'intégralité du flux Device Code grant OAuth 2.0.
- Appelle `getDeviceCode()` et déstructure la réponse en variables (suppose que cela réussit et possède ces propriétés).
- Journalise les instructions pour l'utilisateur :
  - `user_code` : Un code alphanumérique court (par exemple, "ABCD-EFGH").
  - `verification_uri` : Généralement `https://github.com/login/device`, où l'utilisateur s'authentifie.
  - `expires_in` : Temps en secondes jusqu'à l'expiration du code (par exemple, 900 pour 15 minutes).
- L'utilisateur doit visiter l'URL, se connecter à GitHub et saisir le code utilisateur pour autoriser l'application.
- Entre dans une boucle infinie pour interroger périodiquement le jeton :
  - Attend 5 secondes entre les tentatives (intervalle d'interrogation ; GitHub recommande de ralentir en cas de requêtes trop fréquentes).
  - Appelle `getAccessToken(device_code)`.
  - Si la réponse a une `error` : La journalise (par exemple, continue d'attendre si c'est "authorization_pending").
  - Si elle a `access_token` : Journalise l'objet complet du jeton (formaté avec indentation) et sort de la boucle.
- **Cas limites/Problèmes** :
  - Si `getDeviceCode()` échoue, la déstructuration pourrait provoquer une erreur (le code ne vérifie pas cela).
  - Aucun délai d'attente pour la boucle – continue d'interroger indéfiniment à moins que le jeton d'accès ne soit reçu ou que le script ne plante.
  - Journaliser le jeton d'accès dans la console l'expose ; en production, il faudrait le sauvegarder de manière sécurisée (par exemple, dans un fichier ou une base de données).

### Fonctionnement de bout en bout
1. **Étape 1 : Demander le code d'appareil** → Le script obtient un code temporaire auprès de GitHub.
2. **Étape 2 : Autorisation de l'utilisateur** → L'utilisateur visite GitHub et saisit le code pour accorder l'autorisation.
3. **Étape 3 : Interrogation pour le jeton** → Le script continue de demander à GitHub jusqu'à ce que le jeton soit délivré.
4. **Résultat** : Un jeton d'accès pour la portée spécifiée (par exemple, lire les données utilisateur via l'API GitHub).

Il s'agit d'une simulation du fonctionnement d'outils comme GitHub CLI, adaptée pour Copilot. Pour la documentation OAuth officielle de GitHub, reportez-vous à https://docs.github.com/fr/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow. Si vous construisez quelque chose de similaire, assurez-vous de la conformité avec les standards OAuth et les politiques de GitHub. Si vous avez des questions sur la modification ou l'exécution de ce code, n'hésitez pas à demander !