---
audio: false
generated: true
lang: fr
layout: post
title: Le Développement de l'Intelligence Artificielle
translated: true
type: note
---

Voici d'autres exemples d'activation de la sortie verbose à travers divers outils et systèmes, développant le thème de la fourniture de retours d'information ou de journalisation plus détaillés :

- **PowerShell** : Pour activer la sortie verbose, utilisez le commutateur `-Verbose` avec les cmdlets qui le prennent en charge. Par exemple :  
  ```powershell
  Get-Process -Verbose
  ```
  Alternativement, définissez la variable `$VerbosePreference` globalement :  
  ```powershell
  $VerbosePreference = "Continue"
  ```

- **CMake** : Pour obtenir une sortie verbose pendant le processus de build, utilisez l'option `--verbose` ou définissez `VERBOSE=1` :  
  ```bash
  cmake --build . --verbose
  ```
  Ou :  
  ```bash
  make VERBOSE=1
  ```

- **Make** : Pour activer la sortie verbose et voir toutes les commandes exécutées, utilisez l'option `-d` pour le débogage ou évitez de réduire le silence de sortie avec `@` :  
  ```bash
  make -d
  ```
  Ou modifiez le Makefile pour supprimer les préfixes `@` des commandes.

- **GCC (GNU Compiler Collection)** : Pour une sortie de compilation verbose, utilisez l'option `-v` :  
  ```bash
  gcc -v -o output source.c
  ```

- **GDB (GNU Debugger)** : Pour augmenter la verbosité, utilisez la commande `set verbose on` dans GDB :  
  ```gdb
  (gdb) set verbose on
  (gdb) run
  ```

- **Ruby** : Exécutez les scripts Ruby en mode verbose en utilisant l'option `-v` ou `--verbose` :  
  ```bash
  ruby -v script.rb
  ```
  Pour des avertissements supplémentaires, utilisez `-w` :  
  ```bash
  ruby -w script.rb
  ```

- **Perl** : Activez la sortie verbose avec l'option `-v` ou utilisez le pragma `diagnostics` pour des messages d'erreur détaillés :  
  ```bash
  perl -v script.pl
  ```
  Ou dans le script :  
  ```perl
  use diagnostics;
  ```

- **PHP** : Exécutez les scripts PHP avec un rapport d'erreurs verbose en définissant `error_reporting` et `display_errors` dans `php.ini` :  
  ```ini
  error_reporting = E_ALL
  display_errors = On
  ```
  Ou depuis la ligne de commande :  
  ```bash
  php -d error_reporting=E_ALL script.php
  ```

- **R** : Pour activer la sortie verbose dans les scripts R, utilisez l'argument `verbose=TRUE` dans les fonctions qui le prennent en charge (par exemple, `install.packages`) :  
  ```R
  install.packages("dplyr", verbose=TRUE)
  ```

- **Go (Golang)** : Pour une sortie verbose pendant la compilation ou les tests, utilisez l'option `-v` :  
  ```bash
  go build -v
  go test -v
  ```

- **Rust (Cargo)** : Activez la sortie verbose avec Cargo en utilisant les options `-v` ou `-vv` :  
  ```bash
  cargo build -v
  cargo run -vv
  ```

- **Jenkins** : Pour activer la journalisation verbose pour un pipeline, ajoutez l'option `verbose` dans le script ou configurez la sortie console dans les paramètres du job. Par exemple, dans un Jenkinsfile :  
  ```groovy
  sh 'some_command --verbose'
  ```
  Alternativement, définissez la propriété système `-Dhudson.model.TaskListener.verbose=true` au démarrage de Jenkins.

- **Vagrant** : Obtenez une sortie verbose avec l'option `--debug` :  
  ```bash
  vagrant up --debug
  ```

- **Puppet** : Exécutez Puppet avec une verbosité accrue en utilisant les options `--verbose` ou `--debug` :  
  ```bash
  puppet apply site.pp --verbose
  puppet apply site.pp --debug
  ```

- **Chef** : Activez la sortie verbose avec l'option `-l` (niveau de log) :  
  ```bash
  chef-client -l debug
  ```

- **SaltStack** : Augmentez la verbosité avec l'option `-l` (par exemple, `debug` ou `trace`) :  
  ```bash
  salt '*' test.ping -l debug
  ```

- **PostgreSQL (psql)** : Pour obtenir une sortie verbose de `psql`, utilisez l'option `-e` pour répéter les requêtes ou `\set VERBOSITY verbose` pour des messages d'erreur détaillés :  
  ```bash
  psql -e -f script.sql
  ```
  Ou dans `psql` :  
  ```sql
  \set VERBOSITY verbose
  ```

- **MySQL** : Exécutez le client MySQL avec une sortie verbose en utilisant `--verbose` :  
  ```bash
  mysql --verbose < script.sql
  ```

- **SQLite** : Utilisez la commande `.explain` pour des plans d'exécution de requête verbose :  
  ```sqlite
  sqlite3 database.db
  sqlite> .explain
  sqlite> SELECT * FROM table;
  ```

- **MongoDB** : Activez la journalisation verbose en démarrant `mongod` avec l'option `-v` (jusqu'à `-vvvvv` pour plus de détails) :  
  ```bash
  mongod -v
  ```

- **Elasticsearch** : Démarrez Elasticsearch avec une journalisation verbose en ajustant le fichier `log4j2.properties` :  
  ```properties
  logger.action.level = debug
  ```
  Ou passez `--verbose` au démarrage :  
  ```bash
  elasticsearch --verbose
  ```

- **NGINX** : Testez la configuration avec une sortie verbose en utilisant `-T` :  
  ```bash
  nginx -T
  ```
  Pour la verbosité à l'exécution, augmentez le niveau de `error_log` dans `nginx.conf` :  
  ```nginx
  error_log /var/log/nginx/error.log debug;
  ```

- **Apache HTTP Server** : Activez la journalisation verbose en définissant la directive `LogLevel` dans `httpd.conf` ou `apache2.conf` :  
  ```apache
  LogLevel debug
  ```

- **OpenSSL** : Obtenez une sortie verbose avec des commandes comme `s_client` :  
  ```bash
  openssl s_client -connect example.com:443 -debug
  ```

- **JUnit (Java Testing)** : Exécutez les tests JUnit avec une sortie verbose en configurant le test runner (par exemple, le plugin Maven Surefire) :  
  ```xml
  <configuration>
      <argLine>-verbose</argLine>
  </configuration>
  ```

Ces exemples couvrent un large éventail d'outils à travers les langages de programmation, les systèmes de build, les bases de données, les serveurs et les utilitaires DevOps. Faites-moi savoir si vous souhaitez des exemples ou des détails plus spécifiques pour un outil particulier !