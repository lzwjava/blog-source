---
audio: false
generated: true
lang: fr
layout: post
title: Test du registre NPM avec des requêtes HTTP brutes
translated: true
type: note
---

Pour tester votre registre NPM en utilisant des requêtes HTTP brutes avec des outils comme `curl` ou Insomnia, vous pouvez vérifier son fonctionnement en testant la connectivité, l'authentification et la capacité à servir les données des packages—le tout sans dépendre du client NPM. Étant donné que votre registre nécessite un nom d'utilisateur et un mot de passe, vous devrez gérer l'authentification manuellement dans vos requêtes. Voici un guide complet pour tester votre registre en utilisant des requêtes HTTP brutes, en supposant qu'il s'agit d'un registre compatible NPM (par exemple, Verdaccio, Nexus, ou une implémentation personnalisée) qui prend en charge l'authentification par token ou basique.

---

## Étapes pour tester le registre avec des requêtes HTTP brutes

### 1. S'authentifier et obtenir un token (si nécessaire)

La plupart des registres NPM utilisent une authentification par token, vous obligeant à vous connecter pour obtenir un token avant de faire d'autres requêtes. Certains registres peuvent également prendre en charge l'authentification basique directement. Voici comment s'authentifier avec `curl` :

#### Utilisation de `curl` pour se connecter
Envoyez une requête PUT vers le endpoint d'authentification du registre pour obtenir un token :

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "<username>", "password": "<password>"}' \
  <registry-url>/-/user/org.couchdb.user:<username>
```

- **Remplacez** :
  - `<username>` : Votre nom d'utilisateur du registre.
  - `<password>` : Votre mot de passe du registre.
  - `<registry-url>` : L'URL complète de votre registre (par exemple, `https://my-registry.example.com`).
- **Réponse attendue** : En cas de succès, vous obtiendrez une réponse JSON avec un token :
  ```json
  {
    "token": "your-auth-token"
  }
  ```
- **Sauvegardez le Token** : Copiez la valeur `your-auth-token` pour l'utiliser dans les requêtes suivantes.

**Note** : Si votre registre utilise un endpoint ou une méthode d'authentification différente (par exemple, l'authentification basique ou une API personnalisée), consultez sa documentation. S'il prend en charge l'authentification basique directement, vous pouvez ignorer cette étape et inclure `-u "<username>:<password>"` dans les requêtes suivantes à la place.

---

### 2. Tester la connectivité (Ping) du registre

Testez la connectivité de base au registre en envoyant une requête GET à son URL racine ou à un endpoint de ping.

#### Utilisation de `curl` pour le ping
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>
```

- **Remplacez** :
  - `your-auth-token` : Le token de l'Étape 1.
  - `<registry-url>` : L'URL de votre registre.
- **Réponse attendue** : Une réponse réussie (HTTP 200) peut renvoyer la page d'accueil du registre ou un simple message de statut (par exemple, `{"db_name":"registry"}` pour les registres basés sur CouchDB).
- **Alternative** : Certains registres proposent un endpoint `/-/ping` :
  ```bash
  curl -H "Authorization: Bearer your-auth-token" <registry-url>/-/ping
  ```

**Si vous utilisez l'authentification basique** : Si votre registre n'utilise pas de tokens et prend en charge l'authentification basique :
```bash
curl -u "<username>:<password>" <registry-url>
```

---

### 3. Récupérer les métadonnées d'un package

Vérifiez que le registre peut servir les métadonnées des packages en demandant les détails d'un package spécifique.

#### Utilisation de `curl` pour obtenir les métadonnées
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>/<package-name>
```

- **Remplacez** :
  - `<package-name>` : Un package dont vous savez qu'il existe sur votre registre (par exemple, `lodash` s'il proxy le registre public, ou un package privé comme `my-org-utils`).
- **Réponse attendue** : Un objet JSON avec les métadonnées du package, incluant les versions, les dépendances et les URLs des tarballs. Par exemple :
  ```json
  {
    "name": "lodash",
    "versions": {
      "4.17.21": {
        "dist": {
          "tarball": "<registry-url>/lodash/-/lodash-4.17.21.tgz"
        }
      }
    }
  }
  ```

**Si vous utilisez l'authentification basique** :
```bash
curl -u "<username>:<password>" <registry-url>/<package-name>
```

- **Succès** : Une réponse 200 OK avec les métadonnées confirme que le registre sert correctement les données du package.

---

### 4. Télécharger un Tarball de package (Optionnel)

Pour tester complètement le registre, téléchargez un tarball de package pour vous assurer qu'il peut délivrer les fichiers réels du package.

#### Utilisation de `curl` pour télécharger un Tarball
1. À partir des métadonnées de l'Étape 3, trouvez l'URL `tarball` pour une version spécifique (par exemple, `<registry-url>/lodash/-/lodash-4.17.21.tgz`).
2. Téléchargez-le :
```bash
curl -H "Authorization: Bearer your-auth-token" -O <tarball-url>
```

- **Remplacez** : `<tarball-url>` par l'URL issue des métadonnées.
- **Drapeau `-O`** : Sauvegarde le fichier avec son nom d'origine (par exemple, `lodash-4.17.21.tgz`).
- **Si vous utilisez l'authentification basique** :
  ```bash
  curl -u "<username>:<password>" -O <tarball-url>
  ```
- **Succès** : Le fichier est téléchargé avec succès, et vous pouvez l'extraire (par exemple, avec `tar -xzf <nom_du_fichier>`) pour vérifier son contenu.

---

## Test avec Insomnia

Si vous préférez un outil graphique comme Insomnia, suivez ces étapes :

### 1. Configurer l'authentification
- Créez une nouvelle requête dans Insomnia.
- Allez dans l'onglet **Auth** :
  - **Bearer Token** : Si vous avez obtenu un token à l'Étape 1, sélectionnez "Bearer Token" et collez `your-auth-token`.
  - **Basic Auth** : Si le registre utilise l'authentification basique, sélectionnez "Basic Auth" et entrez votre `<username>` et `<password>`.

### 2. Tester la connectivité (Ping) du registre
- **Méthode** : GET
- **URL** : `<registry-url>` ou `<registry-url>/-/ping`
- Cliquez sur **Send**.
- **Réponse attendue** : Un statut 200 OK avec un corps de réponse simple.

### 3. Récupérer les métadonnées d'un package
- **Méthode** : GET
- **URL** : `<registry-url>/<package-name>`
- Assurez-vous que l'authentification est configurée dans l'onglet Auth.
- Cliquez sur **Send**.
- **Réponse attendue** : Un statut 200 OK avec les métadonnées du package en JSON.

### 4. Télécharger un Tarball
- **Méthode** : GET
- **URL** : L'URL du tarball issue des métadonnées (par exemple, `<registry-url>/<package-name>/-/<package-name>-<version>.tgz`).
- Cliquez sur **Send and Download** pour sauvegarder le fichier localement.
- **Succès** : Le fichier est téléchargé, confirmant que le registre sert les packages.

---

## Dépannage

- **401 Non Autorisé** :
  - Vérifiez votre token ou vos identifiants.
  - Assurez-vous que l'en-tête `Authorization` ou l'authentification basique est correctement formaté.
- **404 Non Trouvé** :
  - Vérifiez que le package existe sur le registre.
  - Si vous testez des packages publics (par exemple, `lodash`), confirmez que le registre proxy le registre public NPM.
- **Erreurs de Connexion** :
  - Vérifiez à nouveau `<registry-url>` (par exemple, incluez `https://` si nécessaire).
  - Pour les registres HTTPS, si vous obtenez des erreurs SSL avec `curl`, ajoutez `-k` pour contourner les vérifications de certificat (pour les tests uniquement).
- **Comportement de Registre Personnalisé** :
  - Si ces étapes échouent, consultez la documentation de votre registre pour des endpoints ou méthodes d'authentification spécifiques.

---

## Conclusion

En suivant ces étapes avec `curl` ou Insomnia, vous pouvez tester la connectivité, l'authentification et les capacités de service des packages de votre registre NPM en utilisant des requêtes HTTP brutes. Commencez par vous authentifier (si nécessaire), puis testez la connectivité du registre, récupérez les métadonnées d'un package connu, et téléchargez optionnellement un tarball. Cette approche garantit que votre registre est pleinement opérationnel au niveau HTTP.