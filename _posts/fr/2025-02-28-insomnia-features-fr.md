---
audio: false
generated: true
lang: fr
layout: post
title: Fonctionnalités de l'Interface Graphique Kong Insomnia
translated: true
type: note
---

Kong Insomnia fournit une interface utilisateur graphique (GUI) robuste pour simplifier le développement d'API. Voici un guide détaillé sur la façon d'utiliser **params**, **body**, **auth**, **cookies**, **certificates**, **settings** et **proxy** dans l'interface graphique d'Insomnia.

---

#### 1. **Params (Paramètres de Requête)**
Les paramètres de requête sont utilisés pour ajouter des données à l'URL, généralement pour les requêtes GET.

- **Comment utiliser** :
  - Ouvrez l'**onglet Debug** et sélectionnez ou créez une requête (par exemple, GET).
  - À côté du champ URL, cliquez sur l'onglet **Query**.
  - Ajoutez des paires clé-valeur pour vos paramètres de requête. Par exemple, saisir `key` comme "id" et `value` comme "123" ajoutera `?id=123` à votre URL.
  - Pour utiliser des variables d'environnement, tapez `{{nomDeLaVariable}}` dans le champ value (par exemple, `{{userId}}`).
  - Activez ou désactivez des paramètres spécifiques en basculant la case à cocher à côté de chaque paire.

- **Exemple** :
  Pour une URL comme `https://api.example.com/users?id=123`, ajoutez :
  - Clé : `id`
  - Valeur : `123`
  Insomnia formatera automatiquement l'URL avec la chaîne de requête.

---

#### 2. **Body (Corps)**
Le corps est utilisé pour envoyer des données avec des requêtes comme POST ou PUT.

- **Comment utiliser** :
  - Dans l'**onglet Debug**, sélectionnez une requête (par exemple, POST ou PUT).
  - Passez à l'onglet **Body** en dessous du champ URL.
  - Choisissez un type de corps dans le menu déroulant :
    - **JSON** : Saisissez des données JSON (par exemple, `{"name": "John", "age": 30}`).
    - **Form URL-Encoded** : Ajoutez des paires clé-valeur, similaires aux paramètres de requête.
    - **Multipart Form** : Ajoutez des champs ou téléchargez des fichiers pour les formulaires avec pièces jointes.
    - **Raw** : Saisissez du texte brut ou d'autres formats (par exemple, XML).
  - Utilisez des variables d'environnement en tapant `{{nomDeLaVariable}}` dans le contenu du corps.

- **Exemple** :
  Pour une requête POST envoyant du JSON :
  - Sélectionnez **JSON** dans le menu déroulant.
  - Saisissez : `{"name": "John", "age": "{{userAge}}"}`.
  Insomnia définira automatiquement l'en-tête `Content-Type` sur `application/json`.

---

#### 3. **Auth (Authentification)**
Les paramètres d'authentification vous permettent d'inclure des informations d'identification ou des jetons dans vos requêtes.

- **Comment utiliser** :
  - Dans l'**onglet Debug**, sélectionnez votre requête.
  - Allez dans l'onglet **Auth**.
  - Choisissez un type d'authentification dans le menu déroulant :
    - **Basic Auth** : Saisissez un nom d'utilisateur et un mot de passe.
    - **Bearer Token** : Collez votre jeton (par exemple, un JWT).
    - **OAuth 2.0** : Configurez l'ID client, le secret et autres détails pour les flux OAuth.
    - **API Key** : Ajoutez une paire clé-valeur (par exemple, Clé : `Authorization`, Valeur : `your-api-key`).
  - Insomnia ajoute automatiquement les détails d'authentification aux en-têtes de la requête.

- **Exemple** :
  Pour un Bearer Token :
  - Sélectionnez **Bearer Token**.
  - Collez votre jeton (par exemple, `abc123xyz`).
  L'en-tête de la requête inclura : `Authorization: Bearer abc123xyz`.

---

#### 4. **Cookies**
Les cookies sont gérés automatiquement mais peuvent être visualisés ou modifiés manuellement.

- **Comment utiliser** :
  - Insomnia stocke les cookies reçus des réponses du serveur par espace de travail.
  - Pour gérer les cookies :
    - Allez dans **Préférences** (Ctrl + , ou Cmd + , sur macOS).
    - Naviguez vers **Data** > **Cookie Jar**.
    - Visualisez, modifiez ou supprimez les cookies selon les besoins.
  - Les cookies persistent entre les requêtes dans le même espace de travail et sont envoyés automatiquement avec les requêtes suivantes.

- **Astuce** :
  Si vous avez besoin de tester avec des cookies spécifiques, ajoutez-les manuellement dans la **Cookie Jar** pour le domaine concerné.

---

#### 5. **Certificates (Certificats)**
Les certificats clients sont utilisés pour les requêtes HTTPS nécessitant une authentification TLS mutuelle.

- **Comment utiliser** :
  - Allez dans **Préférences** (Ctrl + , ou Cmd + ,).
  - Sélectionnez la section **Certificates**.
  - Cliquez sur **Add Certificate** :
    - Fournissez le fichier de certificat (par exemple, `.pem`, `.crt`).
    - Ajoutez le fichier de clé privée et une phrase secrète facultative si nécessaire.
    - Associez le certificat à des hôtes spécifiques (par exemple, `api.example.com`).
  - Insomnia utilisera le certificat pour les requêtes vers les hôtes spécifiés.

- **Exemple** :
  Pour `api.example.com` nécessitant un certificat :
  - Téléchargez `client.crt` et `client.key`.
  - Définissez Host sur `api.example.com`.
  Les requêtes vers ce domaine incluront le certificat.

---

#### 6. **Settings (Paramètres)**
Les paramètres vous permettent de personnaliser le comportement d'Insomnia.

- **Comment utiliser** :
  - Accédez-y via **Préférences** (Ctrl + , ou Cmd + ,).
  - Les options principales incluent :
    - **Theme** : Basculez entre clair, sombre ou celui par défaut du système.
    - **Proxy** : Configurez les paramètres de proxy (voir ci-dessous).
    - **Plugins** : Installez des fonctionnalités supplémentaires (par exemple, des formateurs de réponse personnalisés).
    - **Data** : Gérez le Local Vault pour le stockage sécurisé de données sensibles comme les clés API.

- **Astuce** :
  Utilisez le **Local Vault** pour stocker de manière sécurisée des valeurs sensibles (par exemple, des jetons) au lieu de les coder en dur.

---

#### 7. **Proxy**
Les proxies acheminent vos requêtes via un serveur spécifié, utile pour le débogage ou les réseaux d'entreprise.

- **Comment utiliser** :
  - Allez dans **Préférences** > **Proxy**.
  - Activez le proxy et saisissez les détails du serveur proxy (par exemple, `http://proxy.example.com:8080`).
  - Pour une utilisation globale, enregistrez-le ici.
  - Pour un proxy par requête :
    - Cliquez sur l'icône en forme de roue dentée à côté du nom de la requête dans l'**onglet Debug**.
    - Remplacez les paramètres du proxy dans la configuration spécifique à la requête.

- **Exemple** :
  Pour acheminer les requêtes via un proxy d'entreprise :
  - Activez le proxy dans **Préférences**.
  - Définissez Proxy URL sur `http://proxy.example.com:8080`.
  Toutes les requêtes utiliseront désormais ce proxy sauf indication contraire.

---

### Résumé
Voici un rapide récapitulatif de l'utilisation de ces fonctionnalités dans l'interface graphique d'Insomnia :
- **Params** : Ajoutez des paramètres de requête dans l'onglet **Query** pour les requêtes GET.
- **Body** : Envoyez des données avec les requêtes POST/PUT via l'onglet **Body**, en sélectionnant le format.
- **Auth** : Configurez l'authentification dans l'onglet **Auth** pour les requêtes sécurisées.
- **Cookies** : Gérez les cookies dans **Préférences** > **Cookie Jar**.
- **Certificates** : Ajoutez des certificats clients dans **Préférences** > **Certificates** pour HTTPS.
- **Settings** : Personnalisez Insomnia dans **Préférences** (thèmes, plugins, etc.).
- **Proxy** : Configurez les proxies dans **Préférences** ou par requête.

En tirant parti de ces fonctionnalités, vous pouvez tester et déboguer efficacement les API dans Kong Insomnia. Expérimentez avec chaque section pour adapter votre flux de travail !