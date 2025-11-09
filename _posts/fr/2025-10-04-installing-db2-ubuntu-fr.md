---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation d'IBM Db2 sur Ubuntu
translated: true
type: note
---

### Installation d'IBM Db2 12.1.2 sur Ubuntu 22.04 ou 24.04 à partir de `ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz`

La version 12.1.2 d'IBM Db2 (Fix Pack 2) est prise en charge sur les versions récentes d'Ubuntu, y compris 22.04 (Jammy) et 24.04 (Noble), à condition que votre système réponde aux prérequis matériels et logiciels. Cette installation utilise le programme d'installation graphique ou silencieux à partir du fichier tar.gz. Je recommande de consulter la documentation officielle d'IBM pour Db2 12.1 (par exemple, sur l'IBM Knowledge Center ou la page de téléchargement de Db2) pour les derniers détails, car les exigences peuvent varier selon l'édition (Server Edition ici).

**Notes importantes avant de commencer :**
- **Exigences système** :
  - Architecture 64 bits x86_64 (Intel/AMD).
  - Au moins 4 Go de RAM (8 Go recommandés) et 2 Go d'espace swap.
  - 10 Go d'espace disque libre pour l'installation de base (plus pour les données).
  - Accès root ou sudo.
  - Version du noyau : Ubuntu 22.04/24.04 devrait fonctionner, mais assurez-vous que votre noyau est au moins en version 3.10 (vérifiez avec `uname -r`).
  - Pare-feu : Désactivez temporairement ou ouvrez les ports (port par défaut de Db2 : 50000 pour TCP/IP).
- **Problèmes potentiels sur Ubuntu** :
  - Db2 est principalement testé sur RHEL/SUSE, mais Ubuntu est pris en charge via des packages Debian. Vous devrez peut-être résoudre les dépendances de bibliothèques.
  - Si vous utilisez Ubuntu 24.04, c'est une version très récente — testez d'abord dans une VM, car la certification complète peut prendre du retard.
  - Ceci installe la Server Edition. Pour d'autres éditions (par exemple, Express-C), téléchargez le fichier tar.gz approprié.
- **Sauvegarde** : Sauvegardez votre système avant de continuer.
- Téléchargez le fichier depuis le site officiel IBM Passport Advantage ou Db2 Downloads (nécessite un IBM ID).

#### Étape 1 : Installer les prérequis
Mettez à jour votre système et installez les bibliothèques requises. Db2 nécessite des E/S asynchrones, PAM et d'autres librairies d'exécution.

```bash
sudo apt update
sudo apt upgrade -y

# Installer les paquets essentiels (communs pour Db2 sur Ubuntu/Debian)
sudo apt install -y libaio1 libpam0g:i386 libncurses5 libstdc++6:i386 \
    unixodbc unixodbc-dev libxml2 libxslt1.1 wget curl

# Pour Ubuntu 24.04, vous pourriez avoir besoin de :
sudo apt install -y libc6:i386 libgcc-s1:i386

# Vérifier la compatibilité glibc (Db2 12.1 nécessite glibc 2.17+)
ldd --version  # Devrait afficher glibc 2.35+ sur Ubuntu 22.04/24.04
```

Si vous rencontrez des bibliothèques 32 bits manquantes (par exemple, pour les composants Java), activez multiarch :
```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y libc6:i386 libncurses5:i386 libstdc++6:i386
```

#### Étape 2 : Préparer les fichiers d'installation
1. Créez un répertoire temporaire pour l'extraction (par exemple, `/tmp/db2_install`) :
   ```bash
   sudo mkdir -p /tmp/db2_install
   cd /tmp/db2_install
   ```

2. Copiez le fichier tar.gz dans ce répertoire (en supposant que vous l'ayez téléchargé, par exemple dans `~/Downloads`) :
   ```bash
   cp ~/Downloads/ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz .
   ```

3. Extrayez l'archive :
   ```bash
   tar -xzf ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz
   ```
   - Ceci crée un répertoire comme `db2` ou `sqllib` contenant les fichiers de l'installateur (par exemple, `db2setup`).

4. Accédez au répertoire extrait :
   ```bash
   cd db2  # Ou quel que soit le répertoire racine — vérifiez avec `ls`
   ```

#### Étape 3 : Exécuter l'installateur
Db2 fournit un installateur graphique (`db2setup`) ou un fichier de réponse pour les installations silencieuses. Exécutez en tant que root/sudo.

**Option A : Installateur graphique (Recommandé pour une première installation)**
1. Assurez-vous d'avoir un affichage (si sur un serveur sans interface graphique, utilisez le transfert X avec SSH : `ssh -X user@host`).
2. Exécutez l'installateur :
   ```bash
   sudo ./db2setup
   ```
   - L'assistant vous guidera :
     - Acceptez la licence.
     - Choisissez l'installation "Typique" pour la Server Edition.
     - Sélectionnez le chemin d'installation (par défaut : `/opt/ibm/db2/V12.1` — assurez-vous que `/opt/ibm` existe et est accessible en écriture ; créez-le avec `sudo mkdir -p /opt/ibm` si nécessaire).
     - Créez une instance Db2 (par exemple, "db2inst1") — ceci configure l'utilisateur administrateur de la base de données.
     - Définissez l'authentification (par exemple, locale ou LDAP).
     - Activez les fonctionnalités comme SQL Procedural Language si nécessaire.
   - L'installateur compilera et configurera l'instance.

**Option B : Installation silencieuse (Non interactive)**
Si vous préférez le script :
1. Générez un fichier de réponse lors d'une simulation :
   ```bash
   sudo ./db2setup -g  # Génère `db2setup.rsp` dans le répertoire courant
   ```
   Modifiez `db2setup.rsp` (par exemple, définissez `LIC_AGREEMENT=ACCEPT`, `INSTALL_TYPE=TYPICAL`, `CREATE_DB2_INSTANCE=YES`, etc.).

2. Exécutez l'installation silencieuse :
   ```bash
   sudo ./db2setup -u db2setup.rsp
   ```

- L'installation prend 10 à 30 minutes. Surveillez les erreurs dans `/tmp/db2setup.log`.

#### Étape 4 : Configuration post-installation
1. **Vérifier l'installation** :
   - Connectez-vous en tant que propriétaire de l'instance (par exemple, `db2inst1` — créé pendant l'installation) :
     ```bash
     su - db2inst1
     ```
   - Vérifiez la version de Db2 :
     ```bash
     db2level
     ```
   - Démarrez l'instance :
     ```bash
     db2start
     ```
   - Testez la connexion :
     ```bash
     db2 connect to sample  # Crée une base de données exemple si aucune n'existe
     db2 "select * from sysibm.sysdummy1"
     db2 disconnect all
     db2stop  # Quand vous avez terminé
     ```

2. **Créer une base de données (si ce n'est pas fait pendant l'installation)** :
   ```bash
   su - db2inst1
   db2sampl  # Optionnel : Crée une base de données exemple
   # Ou créez une base de données personnalisée :
   db2 "create database MYDB"
   db2 connect to MYDB
   ```

3. **Configuration de l'environnement** :
   - Ajoutez Db2 au PATH pour l'utilisateur de l'instance (ajoutez à `~/.bashrc`) :
     ```bash
     export PATH=/opt/ibm/db2/V12.1/bin:$PATH
     export DB2INSTANCE=db2inst1
     ```
   - Rechargez : `source ~/.bashrc`.

4. **Activer l'accès à distance (Optionnel)** :
   - Mettez à jour les services :
     ```bash
     su - db2inst1
     db2 update dbm cfg using SVCENAME db2i  # Ou votre port
     db2set DB2COMM=TCPIP
     db2start
     ```
   - Modifiez `/etc/services` (en tant que root) pour ajouter :
     ```
     db2i          50000/tcp
     ```
   - Redémarrez l'instance.

5. **Configuration du pare-feu** :
   ```bash
   sudo ufw allow 50000/tcp  # Pour le port par défaut de Db2
   sudo ufw reload
   ```

#### Étape 5 : Appliquer les mises à jour (Recommandé)
- Téléchargez et appliquez le dernier Fix Pack si nécessaire (12.1.2 est FP2 ; vérifiez pour FP3+) :
  - Utilisez l'outil `db2iupdt` ou l'installateur de mise à jour d'IBM.
- Surveillez les journaux : `/tmp/db2` ou `/opt/ibm/db2/V12.1/instance/db2inst1/sqllib/db2dump`.

#### Résolution des problèmes courants
- **"Aucun runtime Java approprié"** : Installez OpenJDK : `sudo apt install openjdk-11-jre-headless`.
- **Erreurs de bibliothèque (par exemple, libaio.so)** : Assurez-vous que `libaio1` est installé et exécutez `sudo ldconfig`.
- **Permission refusée** : Exécutez l'installateur en tant que root ; assurez-vous de la propriété de `/opt/ibm` : `sudo chown -R db2inst1:db2iadm1 /opt/ibm/db2`.
- **Incompatibilité Glibc** : Peu probable sur Ubuntu 22.04/24.04, mais en cas de problème, envisagez une installation par conteneur (Docker).
- **Échec de l'installation silencieuse** : Vérifiez `db2setup.log` pour des indices.
- **Spécifique à Ubuntu 24.04** : Si les dépendances de bibliothèques échouent, vous devrez peut-être ajouter des PPA ou compiler les bibliothèques manquantes. Testez d'abord sur 22.04.
- Des erreurs ? Recherchez sur les forums de support d'IBM ou exécutez `db2diag` en tant qu'utilisateur de l'instance.

Si vous rencontrez des erreurs spécifiques, fournissez des détails pour une aide plus ciblée. Pour une utilisation en production, envisagez les environnements certifiés par IBM ou le support consultatif. Succès ! Votre instance Db2 devrait maintenant être prête pour la création et l'utilisation de bases de données.