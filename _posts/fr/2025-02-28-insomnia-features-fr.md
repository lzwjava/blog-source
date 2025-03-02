---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser les fonctionnalités dans l'interface utilisateur de Kong Insomnia
translated: true
---

Kong Insomnia fournit une interface utilisateur graphique (GUI) robuste pour simplifier le développement d'API. Voici un guide détaillé sur l'utilisation des **params**, **body**, **auth**, **cookies**, **certificats**, **paramètres** et **proxy** dans l'interface GUI d'Insomnia.

---

#### 1. **Params (Paramètres de requête)**
Les paramètres de requête sont utilisés pour ajouter des données à l'URL, généralement pour les requêtes GET.

- **Comment utiliser** :
  - Ouvrez l'onglet **Debug** et sélectionnez ou créez une requête (par exemple, GET).
  - À côté du champ URL, cliquez sur l'onglet **Query**.
  - Ajoutez des paires clé-valeur pour vos paramètres de requête. Par exemple, en entrant `key` comme "id" et `value` comme "123", cela ajoutera `?id=123` à votre URL.
  - Pour utiliser des variables d'environnement, tapez `{{variableName}}` dans le champ de valeur (par exemple, `{{userId}}`).
  - Activez ou désactivez des paramètres spécifiques en basculant la case à cocher à côté de chaque paire.

- **Exemple** :
  Pour une URL comme `https://api.example.com/users?id=123`, ajoutez :
  - Clé : `id`
  - Valeur : `123`
  Insomnia formatera automatiquement l'URL avec la chaîne de requête.

---

#### 2. **Body**
Le corps est utilisé pour envoyer des données avec des requêtes comme POST ou PUT.

- **Comment utiliser** :
  - Dans l'onglet **Debug**, sélectionnez une requête (par exemple, POST ou PUT).
  - Passez à l'onglet **Body** en dessous du champ URL.
  - Choisissez un type de corps dans le menu déroulant :
    - **JSON** : Entrez des données JSON (par exemple, `{"name": "John", "age": 30}`).
    - **Form URL-Encoded** : Ajoutez des paires clé-valeur, similaires aux paramètres de requête.
    - **Multipart Form** : Ajoutez des champs ou téléchargez des fichiers pour les formulaires avec des pièces jointes.
    - **Raw** : Entrez du texte brut ou d'autres formats (par exemple, XML).
  - Utilisez des variables d'environnement en tapant `{{variableName}}` dans le contenu du corps.

- **Exemple** :
  Pour une requête POST envoyant JSON :
  - Sélectionnez **JSON** dans le menu déroulant.
  - Entrez : `{"name": "John", "age": "{{userAge}}"}`.
  Insomnia définira automatiquement l'en-tête `Content-Type` sur `application/json`.

---

#### 3. **Auth (Authentification)**
Les paramètres d'authentification permettent d'inclure des identifiants ou des jetons dans vos requêtes.

- **Comment utiliser** :
  - Dans l'onglet **Debug**, sélectionnez votre requête.
  - Allez à l'onglet **Auth**.
  - Choisissez un type d'authentification dans le menu déroulant :
    - **Basic Auth** : Entrez un nom d'utilisateur et un mot de passe.
    - **Bearer Token** : Collez votre jeton (par exemple, un JWT).
    - **OAuth 2.0** : Configurez l'ID client, le secret et d'autres détails pour les flux OAuth.
    - **API Key** : Ajoutez une paire clé-valeur (par exemple, Clé : `Authorization`, Valeur : `your-api-key`).
  - Insomnia ajoute automatiquement les détails d'authentification aux en-têtes de la requête.

- **Exemple** :
  Pour un Bearer Token :
  - Sélectionnez **Bearer Token**.
  - Collez votre jeton (par exemple, `abc123xyz`).
  L'en-tête de la requête inclura : `Authorization: Bearer abc123xyz`.

---

#### 4. **Cookies**
Les cookies sont gérés automatiquement mais peuvent être consultés ou modifiés manuellement.

- **Comment utiliser** :
  - Insomnia stocke les cookies reçus des réponses du serveur par espace de travail.
  - Pour gérer les cookies :
    - Allez dans **Preferences** (Ctrl + , ou Cmd + , sur macOS).
    - Naviguez vers **Data** > **Cookie Jar**.
    - Consultez, modifiez ou supprimez les cookies selon les besoins.
  - Les cookies persistent à travers les requêtes dans le même espace de travail et sont envoyés automatiquement avec les requêtes suivantes.

- **Astuce** :
  Si vous devez tester avec des cookies spécifiques, ajoutez-les manuellement dans le **Cookie Jar** pour le domaine pertinent.

---

#### 5. **Certificats**
Les certificats clients sont utilisés pour les requêtes HTTPS nécessitant une authentification TLS mutuelle.

- **Comment utiliser** :
  - Allez dans **Preferences** (Ctrl + , ou Cmd + ,).
  - Sélectionnez la section **Certificates**.
  - Cliquez sur **Add Certificate** :
    - Fournissez le fichier de certificat (par exemple, `.pem`, `.crt`).
    - Ajoutez le fichier de clé privée et un mot de passe facultatif si nécessaire.
    - Associez le certificat à des hôtes spécifiques (par exemple, `api.example.com`).
  - Insomnia utilisera le certificat pour les requêtes aux hôtes spécifiés.

- **Exemple** :
  Pour `api.example.com` nécessitant un certificat :
  - Téléchargez `client.crt` et `client.key`.
  - Définissez l'hôte sur `api.example.com`.
  Les requêtes à ce domaine incluront le certificat.

---

#### 6. **Paramètres**
Les paramètres permettent de personnaliser le comportement d'Insomnia.

- **Comment utiliser** :
  - Accédez via **Preferences** (Ctrl + , ou Cmd + ,).
  - Options clés :
    - **Theme** : Passez entre clair, sombre ou système par défaut.
    - **Proxy** : Configurez les paramètres proxy (voir ci-dessous).
    - **Plugins** : Installez des fonctionnalités supplémentaires (par exemple, des formatteurs de réponse personnalisés).
    - **Data** : Gérez le Local Vault pour le stockage sécurisé des données sensibles comme les clés API.

- **Astuce** :
  Utilisez le **Local Vault** pour stocker les valeurs sensibles (par exemple, les jetons) de manière sécurisée au lieu de les coder en dur.

---

#### 7. **Proxy**
Les proxys routent vos requêtes via un serveur spécifié, utile pour le débogage ou les réseaux d'entreprise.

- **Comment utiliser** :
  - Allez dans **Preferences** > **Proxy**.
  - Activez le proxy et entrez les détails du serveur proxy (par exemple, `http://proxy.example.com:8080`).
  - Pour une utilisation globale, enregistrez-le ici.
  - Pour un proxy par requête :
    - Cliquez sur l'icône d'engrenage à côté du nom de la requête dans l'onglet **Debug**.
    - Remplacez les paramètres proxy dans la configuration spécifique à la requête.

- **Exemple** :
  Pour router les requêtes via un proxy d'entreprise :
  - Activez le proxy dans **Preferences**.
  - Définissez l'URL du proxy sur `http://proxy.example.com:8080`.
  Toutes les requêtes utiliseront maintenant ce proxy sauf si elles sont remplacées.

---

### Résumé
Voici un rapide rappel de l'utilisation de ces fonctionnalités dans l'interface GUI d'Insomnia :
- **Params** : Ajoutez des paramètres de requête dans l'onglet **Query** pour les requêtes GET.
- **Body** : Envoyez des données avec les requêtes POST/PUT via l'onglet **Body**, en sélectionnant le format.
- **Auth** : Configurez l'authentification dans l'onglet **Auth** pour des requêtes sécurisées.
- **Cookies** : Gérez les cookies dans **Preferences** > **Cookie Jar**.
- **Certificats** : Ajoutez des certificats clients dans **Preferences** > **Certificates** pour HTTPS.
- **Paramètres** : Personnalisez Insomnia dans **Preferences** (thèmes, plugins, etc.).
- **Proxy** : Configurez les proxys dans **Preferences** ou par requête.

En utilisant ces fonctionnalités, vous pouvez tester et déboguer efficacement les API dans Kong Insomnia. Expérimentez chaque section pour adapter votre flux de travail !