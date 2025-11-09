---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation d'Oracle 12c sur Ubuntu
translated: true
type: note
---

### Installation d'Oracle Database 12c Release 1 (12.1.0.2 avec le correctif 12.1.2 ?) à partir d'une archive Tarball sur Ubuntu 22.04 x86_64

Le fichier `v12.1.2_linuxx64_server_dec.tar.gz` semble être une archive tarball pour Oracle Database 12c Release 1 (probablement la version 12.1.0.2 regroupée avec le correctif 12.1.2, édition serveur, "dec" pouvant signifier "deconfigured"). Il s'agit d'une version plus ancienne d'Oracle Database (datant d'environ 2013-2014), et Oracle ne **supporte pas officiellement Ubuntu**. L'installation sur Ubuntu 22.04 (qui utilise des bibliothèques modernes comme glibc 2.35) peut fonctionner mais peut nécessiter des solutions de contournement pour les problèmes de compatibilité, tels que le lien de bibliothèques ou les paramètres du noyau. Prévoyez des erreurs potentielles de dépendances—testez d'abord dans une machine virtuelle.

**Avertissements :**
- Oracle 12c est en fin de support étendu (depuis 2022), utilisez-le pour des tests/la production à vos risques et périls. Envisagez des versions plus récentes comme 19c ou 23ai pour la production.
- Vous aurez besoin d'un accès root/sudo.
- Matériel minimum : 2 Go de RAM (8 Go recommandés), 2 cœurs de CPU, 10 Go d'espace disque libre pour le logiciel (plus pour la base de données).
- Sauvegardez votre système avant de continuer.
- Si cette archive ne provient pas d'une source officielle d'Oracle, vérifiez son intégrité (par exemple, avec des sommes de contrôle) pour éviter les logiciels malveillants.

#### Étape 1 : Préparer votre système
1. **Mettre à jour Ubuntu** :
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **Installer les dépendances requises** :
   Oracle 12c a besoin de bibliothèques spécifiques. Installez-les via apt :
   ```
   sudo apt install -y oracle-java8-installer bc binutils libaio1 libaio-dev libelf-dev libnuma-dev libstdc++6 unixodbc unixodbc-dev
   ```
   - Si `oracle-java8-installer` n'est pas disponible (il se trouve dans des dépôts plus anciens), ajoutez le PPA Java d'Oracle ou téléchargez JDK 8 manuellement :
     ```
     sudo add-apt-repository ppa:webupd8team/java -y
     sudo apt update
     sudo apt install oracle-java8-installer -y
     ```
     Acceptez la licence pendant l'installation. Définissez JAVA_HOME :
     ```
     echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **Créer l'utilisateur et les groupes Oracle** :
   Exécutez en tant que root ou avec sudo :
   ```
   sudo groupadd -g 54321 oinstall
   sudo groupadd -g 54322 dba
   sudo useradd -u 54321 -g oinstall -G dba -s /bin/bash oracle
   sudo passwd oracle  # Définissez un mot de passe pour l'utilisateur oracle
   ```

4. **Configurer les paramètres du noyau** :
   Modifiez `/etc/sysctl.conf` :
   ```
   sudo nano /etc/sysctl.conf
   ```
   Ajoutez ces lignes (ajustez pour votre RAM/disque ; ce sont des minimums) :
   ```
   fs.file-max = 6815744
   kernel.sem = 250 32000 100 128
   kernel.shmmni = 4096
   kernel.shmall = 1073741824
   kernel.shmmax = 4398046511104
   kernel.panic_on_oops = 1
   net.core.rmem_default = 262144
   net.core.rmem_max = 4194304
   net.core.wmem_default = 262144
   net.core.wmem_max = 1048576
   fs.aio-max-nr = 1048576
   vm.swappiness = 0
   ```
   Appliquez les changements :
   ```
   sudo sysctl -p
   ```

5. **Définir les limites du shell pour l'utilisateur Oracle** :
   Modifiez `/etc/security/limits.conf` :
   ```
   sudo nano /etc/security/limits.conf
   ```
   Ajoutez :
   ```
   oracle soft nproc 2047
   oracle hard nproc 16384
   oracle soft nofile 1024
   oracle hard nofile 65536
   oracle soft stack 10240
   oracle hard stack 32768
   ```
   Modifiez `/etc/pam.d/login` et ajoutez :
   ```
   sudo nano /etc/pam.d/login
   ```
   Ajoutez : `session required pam_limits.so`

6. **Créer les répertoires** :
   ```
   sudo mkdir -p /u01/app/oracle/product/12.1.0/dbhome_1
   sudo mkdir -p /u01/app/oraInventory
   sudo chown -R oracle:oinstall /u01
   sudo chmod -R 775 /u01
   ```

7. **Espace d'échange (Swap)** (si RAM < 8 Go, ajoutez du swap) :
   Pour 2 Go de RAM, créez un fichier d'échange de 2 Go :
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

8. **Désactiver le pare-feu/SElinux** (si activé) :
   ```
   sudo ufw disable  # Ou configurez les ports 1521, 5500 si nécessaire
   sudo apt remove apparmor -y  # Si AppArmor interfère
   ```

#### Étape 2 : Extraire l'archive Tarball
Passez à l'utilisateur oracle :
```
su - oracle
cd ~/Téléchargements  # Ou là où se trouve le fichier
```
Extrayez (cela crée la structure du répertoire d'installation de la base de données) :
```
tar -xzf v12.1.2_linuxx64_server_dec.tar.gz -C /u01/app/oracle/product/12.1.0/
```
- Ceci devrait créer `/u01/app/oracle/product/12.1.0/dbhome_1` avec des fichiers comme `runInstaller`.
- Si l'archive extrait vers une structure différente, ajustez les chemins en conséquence (par exemple, répertoire `database/`).

#### Étape 3 : Exécuter le programme d'installation
Toujours en tant qu'utilisateur oracle :
```
cd /u01/app/oracle/product/12.1.0/dbhome_1
./runInstaller
```
- Le programme d'installation graphique va démarrer (nécessite le transfert X11 si SSH ; utilisez `ssh -X` ou activez X11).
- **Options d'installation** :
  - Sélectionnez "Créer et configurer un logiciel de base de données uniquement" ou "Installation d'instance de base de données unique" (pour l'édition serveur).
  - ORACLE_HOME : `/u01/app/oracle/product/12.1.0/dbhome_1`
  - Inventaire : `/u01/app/oraInventory`
  - S'il s'agit uniquement du logiciel (sans création de base de données), choisissez "Installer uniquement le logiciel de base de données".
- Suivez l'assistant : Acceptez les paramètres par défaut lorsque c'est possible, mais définissez les mots de passe pour SYS/SYSTEM.
- Ignorez initialement tous les avertissements de "prérequis"—corrigez-les après l'installation si nécessaire.

Si l'interface graphique échoue (par exemple, erreur DISPLAY), exécutez l'installation silencieuse :
```
./runInstaller -silent -responseFile /chemin/vers/le/fichier_reponse.rsp
```
Vous devrez préparer un fichier de réponse (exemple dans le répertoire extrait, par exemple `db_install.rsp`). Modifiez-le avec vos paramètres (ORACLE_HOME, etc.) et exécutez.

#### Étape 4 : Post-installation
1. **Exécuter root.sh** (en tant que root) :
   ```
   sudo /u01/app/oraInventory/orainstRoot.sh
   sudo /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
   ```

2. **Définir les variables d'environnement** (pour l'utilisateur oracle, ajoutez à `~/.bash_profile`) :
   ```
   export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1
   export PATH=$ORACLE_HOME/bin:$PATH
   export ORACLE_SID=orcl  # Changez pour votre SID
   export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
   export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
   ```
   ```
   source ~/.bash_profile
   ```

3. **Créer une base de données** (si ce n'est pas fait pendant l'installation) :
   ```
   dbca  # Database Configuration Assistant (interface graphique/silencieuse)
   ```
   Ou utilisez SQL*Plus pour une création manuelle.

4. **Démarrer/Arrêter les services** :
   ```
   sqlplus / as sysdba
   STARTUP;  # Ou shutdown
   ```
   Ajoutez à systemd pour le démarrage automatique (créez `/etc/systemd/system/oracle.service` avec exec vers `dbstart`).

#### Dépannage des problèmes courants sur Ubuntu 22.04
- **Erreurs Glibc/Dépendances** : Oracle 12c attend glibc <=2.17. Ubuntu 22.04 a la 2.35—utilisez `ldd` pour vérifier, ou installez les bibliothèques de compatibilité :
  ```
  sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
  ```
  Si erreurs de l'éditeur de liens, définissez `LD_PRELOAD` ou utilisez un conteneur Docker avec Oracle Linux.
- **Problèmes Java/Affichage** : Assurez-vous que JDK 8 est défini (`java -version` doit afficher 1.8). Pour un mode sans affichage : `export DISPLAY=:0`.
- **Mémoire insuffisante** : Augmentez ulimit ou la RAM. Modifiez les paramètres de `runInstaller` si nécessaire.
- **Correctif 12.1.2** : S'il n'est pas inclus, téléchargez-le depuis My Oracle Support et appliquez-le avec `opatch` après l'installation.
- **Journaux** : Vérifiez `/u01/app/oraInventory/logs/installActions*.log` pour les erreurs.
- **Correctif de compatibilité** : Certains utilisateurs créent des liens symboliques vers les bibliothèques (par exemple, `sudo ln -s /lib/x86_64-linux-gnu/libpthread.so.0 /u01/app/oracle/product/12.1.0/dbhome_1/lib/libpthread_nonshared.a`—recherchez en fonction de l'erreur).

#### Vérification
- Exécutez `sqlplus / as sysdba` et exécutez `SELECT * FROM v$version;`.
- Écouteur : `lsnrctl start`.

Si vous rencontrez des erreurs spécifiques, fournissez la sortie du journal pour plus d'aide. Pour la documentation officielle (bien que centrée sur RHEL), consultez le guide d'installation d'Oracle 12c. S'il s'agit d'un produit différent (pas une base de données), clarifiez le contenu de l'archive !