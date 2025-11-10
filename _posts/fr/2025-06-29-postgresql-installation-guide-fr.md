---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre psycopg2 en installant PostgreSQL
translated: true
type: note
---

L'erreur que vous rencontrez indique que le package `psycopg2` nécessite l'exécutable `pg_config` de PostgreSQL pour être compilé à partir des sources, mais qu'il n'est pas trouvé sur votre système. Cela signifie que vous devez installer PostgreSQL sur votre système macOS pour fournir les dépendances nécessaires. Voici les étapes pour installer PostgreSQL sur macOS et résoudre le problème.

### Étapes pour installer PostgreSQL sur macOS

#### 1. **Installer PostgreSQL en utilisant Homebrew (Recommandé)**
Homebrew est le moyen le plus simple d'installer et de gérer PostgreSQL sur macOS.

1. **Installer Homebrew (s'il n'est pas déjà installé)** :
   - Ouvrez le Terminal et exécutez :
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Suivez les instructions à l'écran pour terminer l'installation de Homebrew.

2. **Installer PostgreSQL** :
   - Dans le Terminal, exécutez :
     ```bash
     brew install postgresql
     ```
   - Cette commande installe PostgreSQL et ses dépendances, y compris l'exécutable `pg_config` nécessaire pour `psycopg2`.

3. **Démarrer PostgreSQL** :
   - Pour démarrer le service PostgreSQL, exécutez :
     ```bash
     brew services start postgresql
     ```
   - Alternativement, pour le démarrer manuellement pour une seule session :
     ```bash
     pg_ctl -D /opt/homebrew/var/postgres start
     ```

4. **Vérifier l'installation** :
   - Vérifiez si PostgreSQL est installé et en cours d'exécution :
     ```bash
     psql --version
     ```
   - Vous devriez voir la version de PostgreSQL (par exemple, `psql (PostgreSQL) 17.0`).
   - Vous pouvez également vous connecter à l'invite PostgreSQL pour confirmer :
     ```bash
     psql -U $(whoami)
     ```

#### 2. **Installer `psycopg2` après PostgreSQL**
Une fois PostgreSQL installé, réessayez d'installer `psycopg2`. L'exécutable `pg_config` devrait maintenant être disponible dans votre PATH.

1. **Installer `psycopg2`** :
   - Exécutez :
     ```bash
     pip install psycopg2
     ```
   - Si vous utilisez un fichier de requirements, exécutez :
     ```bash
     pip install -r scripts/requirements/requirements.local.txt
     ```

2. **Alternative : Installer `psycopg2-binary` (Option plus simple)** :
   - Si vous souhaitez éviter de compiler `psycopg2` à partir des sources (ce qui nécessite les dépendances PostgreSQL), vous pouvez installer le package précompilé `psycopg2-binary` :
     ```bash
     pip install psycopg2-binary
     ```
   - Remarque : `psycopg2-binary` n'est pas recommandé pour les environnements de production en raison de problèmes de compatibilité potentiels, mais il convient pour le développement ou les tests.

#### 3. **Optionnel : Ajouter `pg_config` au PATH (si nécessaire)**
Si l'exécutable `pg_config` n'est toujours pas trouvé après l'installation de PostgreSQL, vous devrez peut-être l'ajouter manuellement à votre PATH.

1. Localiser `pg_config` :
   - Homebrew installe généralement PostgreSQL dans `/opt/homebrew/bin` (pour Apple Silicon) ou `/usr/local/bin` (pour les Mac Intel).
   - Vérifiez l'emplacement :
     ```bash
     find /opt/homebrew -name pg_config
     ```
     ou
     ```bash
     find /usr/local -name pg_config
     ```

2. Ajouter au PATH :
   - Si `pg_config` est trouvé (par exemple, dans `/opt/homebrew/bin`), ajoutez-le à votre PATH en modifiant votre fichier de configuration de shell (par exemple, `~/.zshrc` ou `~/.bash_profile`) :
     ```bash
     echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
     ```
   - Appliquez les modifications :
     ```bash
     source ~/.zshrc
     ```

3. Vérifier `pg_config` :
   - Exécutez :
     ```bash
     pg_config --version
     ```
   - Si cela retourne une version, le PATH est correctement configuré.

#### 4. **Dépannage**
- **L'erreur persiste** : Si `pip install psycopg2` échoue toujours, assurez-vous d'avoir les outils de compilation nécessaires :
  - Installez Xcode Command Line Tools :
    ```bash
    xcode-select --install
    ```
  - Installez `libpq` (la bibliothèque cliente PostgreSQL) explicitement si nécessaire :
    ```bash
    brew install libpq
    ```

- **Compatibilité de la version Python** : Assurez-vous que votre version de Python (3.13 dans votre cas) est compatible avec `psycopg2`. Si les problèmes persistent, envisagez d'utiliser un environnement virtuel avec une version de Python légèrement antérieure (par exemple, 3.11 ou 3.12) :
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  pip install psycopg2
  ```

- **Vérifier Homebrew** : Assurez-vous que Homebrew est à jour :
  ```bash
  brew update
  brew upgrade
  ```

#### 5. **Méthodes d'installation alternatives (Optionnel)**
Si vous préférez ne pas utiliser Homebrew, vous pouvez installer PostgreSQL via :
- **Postgres.app** :
  - Téléchargez-le depuis [postgresapp.com](https://postgresapp.com/).
  - Suivez les instructions de configuration pour installer et démarrer PostgreSQL.
  - Ajoutez le répertoire `bin` (par exemple, `/Applications/Postgres.app/Contents/Versions/latest/bin`) à votre PATH comme décrit ci-dessus.
- **Installateur PostgreSQL officiel** :
  - Téléchargez l'installateur macOS depuis [postgresql.org](https://www.postgresql.org/download/macosx/).
  - Suivez l'assistant d'installation.

#### 6. **Réessayer votre projet**
Après avoir installé PostgreSQL et `psycopg2` (ou `psycopg2-binary`), réessayez d'exécuter votre projet ou de réinstaller les requirements :
```bash
pip install -r scripts/requirements/requirements.local.txt
```

### Notes supplémentaires
- **Pourquoi l'erreur s'est produite** : Le package `psycopg2` nécessite les bibliothèques de développement PostgreSQL (spécifiquement `libpq`) pour être compilé à partir des sources. L'installation de PostgreSQL via Homebrew fournit ces bibliothèques.
- **Considérations pour la production** : Pour la production, utilisez `psycopg2` (et non `psycopg2-binary`) et assurez-vous que votre version de PostgreSQL correspond à l'environnement cible.
- **Documentation** : Pour plus de détails, consultez le guide d'installation de `psycopg2` à l'adresse [psycopg.org/docs/install.html](https://www.psycopg.org/docs/install.html).

Si vous rencontrez d'autres problèmes, veuillez partager le message d'erreur spécifique, et je pourrai vous aider à les résoudre !