---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Stratégies de Configuration Sécurisée des Bases de Données
translated: true
type: note
---

### Gestion des configurations de base de données sensibles dans les projets Python

La gestion des informations sensibles comme les mots de passe et les ports de base de données dans les fichiers de configuration est un défi courant dans les projets Python. L'objectif est d'éviter de commettre des secrets dans le contrôle de version (par exemple, Git) tout en gardant le déploiement simple. Ci-dessous, je vais comparer les deux approches que vous avez mentionnées : (1) utiliser un modèle `config_example.ini` avec `.gitignore` pour le vrai fichier, et une configuration manuelle sur des serveurs comme UAT ; et (2) utiliser le chiffrement GPG pour stocker des valeurs chiffrées dans `config.ini` et les déchiffrer au runtime. Les deux sont sécurisées si elles sont correctement mises en œuvre, mais elles échangent la simplicité contre l'automatisation.

#### Approche 1 : Modèle de configuration + `.gitignore` + Configuration manuelle sur le serveur
Il s'agit d'une méthode simple et peu technologique. Vous créez un exemple de fichier de configuration pour les développeurs et les pipelines CI/CD, ignorez le vrai dans Git, et gérez la configuration réelle manuellement sur des environnements de type production (par exemple, les serveurs UAT).

**Étapes de mise en œuvre :**
1. Créer `config_example.ini` avec des espaces réservés :
   ```
   [database]
   host = localhost
   port = 5432  # Exemple de port ; remplacez par le vrai
   user = dbuser
   password = example_password  # Remplacer par le vrai mot de passe
   database = mydb
   ```

2. Ajouter le vrai `config.ini` à `.gitignore` :
   ```
   config.ini
   ```

3. Dans votre code Python, charger depuis `config.ini` (revenir à l'exemple s'il est manquant pour le dev) :
   ```python
   import configparser
   import os

   config = configparser.ConfigParser()
   config_file = 'config.ini' if os.path.exists('config.ini') else 'config_example.ini'
   config.read(config_file)

   db_host = config['database']['host']
   db_port = config['database']['port']
   db_user = config['database']['user']
   db_password = config['database']['password']
   db_name = config['database']['database']
   ```

4. Pour les serveurs UAT : Copier manuellement `config.ini` avec les vraies valeurs (par exemple, via SCP ou Ansible) pendant le déploiement. Les développeurs peuvent copier `config_example.ini` en `config.ini` et le remplir localement.

**Avantages :**
- Simple — aucune bibliothèque ou clé supplémentaire à gérer.
- Aucune surcharge au runtime (déchiffrement).
- Facile pour les petites équipes ; fonctionne bien avec les déploiements manuels.

**Inconvénients :**
- La configuration manuelle sur chaque serveur augmente le risque d'erreur (par exemple, oublier de mettre à jour le mot de passe).
- Pas idéal pour CI/CD automatisé ; nécessite une injection sécurisée des secrets (par exemple, via des variables d'environnement dans les pipelines).
- Si quelqu'un commet `config.ini` par erreur, les secrets sont exposés.

Cette approche est excellente pour les projets en phase de démarrage ou lorsque le chiffrement semble excessif.

#### Approche 2 : Chiffrement GPG pour les valeurs de configuration
Ici, vous chiffrez les champs sensibles (par exemple, le mot de passe) en utilisant GPG, stockez le blob chiffré dans `config.ini`, et le déchiffrez dans votre code au runtime. Le fichier chiffré peut être validé en toute sécurité dans Git, tant que votre clé privée n'est jamais partagée.

**Étapes de mise en œuvre :**
1. Installer GPG sur votre système (c'est standard sur Linux/Mac ; utilisez Gpg4win sur Windows). Générez une paire de clés si nécessaire :
   ```
   gpg --gen-key  # Suivez les invites pour votre clé
   ```

2. Chiffrez la valeur sensible (par exemple, le mot de passe) dans un fichier :
   ```
   echo "real_password_here" | gpg --encrypt --recipient your-email@example.com -o encrypted_password.gpg
   ```
   - Cela crée `encrypted_password.gpg`. Vous pouvez l'encoder en base64 pour un stockage facile dans INI :
     ```bash
     base64 encrypted_password.gpg > encrypted_password.b64
     ```

3. Mettez à jour `config.ini` pour inclure la valeur chiffrée (et encodée en base64). Validez-le — c'est sûr :
   ```
   [database]
   host = localhost
   port = 5432
   user = dbuser
   password_encrypted = <base64-encoded-encrypted-blob-here>  # De encrypted_password.b64
   database = mydb
   ```

4. Dans votre code Python, déchiffrez en utilisant la bibliothèque `gnupg` (installez via `pip install python-gnupg` pour le dev, mais supposez qu'elle est disponible) :
   ```python
   import configparser
   import gnupg
   import base64
   import tempfile
   import os

   config = configparser.ConfigParser()
   config.read('config.ini')  # Peut valider ceci en toute sécurité

   # Déchiffrer le mot de passe
   gpg = gnupg.GPG()  # Suppose que GPG est installé et que la clé est disponible
   encrypted_b64 = config['database']['password_encrypted']
   encrypted_data = base64.b64decode(encrypted_b64)

   with tempfile.NamedTemporaryFile(delete=False) as tmp:
       tmp.write(encrypted_data)
       tmp.flush()
       decrypted = gpg.decrypt_file(None, passphrase=None, extra_args=['--batch', '--yes'], output=tmp.name)
       if decrypted.ok:
           db_password = decrypted.data.decode('utf-8').strip()
       else:
           raise ValueError("Échec du déchiffrement")

   os.unlink(tmp.name)  # Nettoyer

   db_host = config['database']['host']
   db_port = config['database']['port']
   db_user = config['database']['user']
   db_name = config['database']['database']

   # Maintenant utiliser db_password...
   ```

5. Pour les serveurs UAT : Déployez `config.ini` tel quel (via Git ou copie). Assurez-vous que la clé privée GPG est placée de manière sécurisée sur le serveur (par exemple, via Ansible vault ou copie sécurisée manuelle). Le code déchiffrera au démarrage.

**Avantages :**
- La configuration chiffrée peut être contrôlée en version — pas besoin de `.gitignore` pour les secrets.
- Automatise le déploiement ; fonctionne avec CI/CD (il suffit de synchroniser la clé de manière sécurisée).
- Auditable : Les modifications des valeurs chiffrées sont suivies.

**Inconvénients :**
- Nécessite la configuration de GPG et la gestion des clés (par exemple, rotation périodique des clés ; ne jamais valider les clés privées).
- Dépendance au runtime sur GPG et `python-gnupg` ; le déchiffrement échoue si la clé est manquante.
- Légèrement plus complexe pour les débutants ; impact potentiel sur les performances lors du déchiffrement (négligeable pour les mots de passe).

Utilisez cela pour les équipes avec des déploiements automatisés ou lors du partage de configurations entre environnements.

#### Tableau comparatif

| Aspect              | Modèle + .gitignore + Manuel | Chiffrement GPG + Déchiffrement Runtime |
|---------------------|--------------------------------|----------------------------------|
| **Sécurité**       | Élevée si les étapes manuelles sont prudentes ; risque d'erreur humaine. | Élevée ; les secrets jamais en texte clair. |
| **Facilité de configuration**  | Très facile (aucun outil nécessaire).  | Modérée (GPG + bibliothèque).       |
| **Contrôle de version**| Modèle validé ; vrai fichier ignoré. | Configuration complète validée (chiffrée). |
| **Déploiement**     | Manuel par serveur (par exemple, SCP).| Automatisé (synchronisation de clé nécessaire).    |
| **Surcharge**       | Aucune.                         | Mineure (déchiffrement au chargement).        |
| **Idéal pour**       | Petits projets/manuels.        | Pipelines automatisés/CI/CD.      |

#### Recommandations
- Commencez avec l'**Approche 1** si votre projet est simple ou si l'équipe est petite — elle est éprouvée.
- Passez à l'**Approche 2** (ou évoluez vers des variables d'environnement/des gestionnaires de secrets comme AWS SSM/HashiCorp Vault) pour la mise à l'échelle.
- Combinez toujours avec des variables d'environnement pour les remplacements (par exemple, `os.getenv('DB_PASSWORD', db_password)`).
- Testez le déchiffrement dans un environnement de staging avant UAT.

Si vous partagez plus de détails (par exemple, votre outil de déploiement ou la configuration complète), je peux affiner le code !