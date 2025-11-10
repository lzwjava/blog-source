---
audio: false
generated: true
lang: fr
layout: post
title: Présentation des outils OpenJDK 21
translated: true
type: note
---

Le répertoire `/usr/lib/jvm/java-21-openjdk-amd64/bin/` contient les outils fournis par le Java Development Kit (JDK) OpenJDK 21. Ces outils sont utilisés pour diverses tâches liées au développement, au débogage, à la surveillance et à l'empaquetage Java. Ci-dessous se trouve une explication concise de chaque outil et de son utilisation courante. Pour une utilisation détaillée, vous pouvez exécuter `nom_du_tool --help` ou `man nom_du_tool` dans le terminal pour la plupart de ces outils.

---

### 1. **jar** - Créer et gérer les fichiers Java ARchive (JAR)
- **Objectif** : Empaqueter des classes et des ressources Java dans un fichier JAR ou en extraire le contenu.
- **Utilisation courante** :
  ```bash
  jar cf monapp.jar *.class  # Créer un fichier JAR
  jar xf monapp.jar          # Extraire le contenu d'un JAR
  jar tf monapp.jar          # Lister le contenu d'un JAR
  ```
- **Exemple** : `jar cvfm monapp.jar manifest.txt *.class` (crée un JAR avec un fichier manifeste).

---

### 2. **java** - Lancer une application Java
- **Objectif** : Exécuter un programme Java en lançant un fichier de classe ou un JAR.
- **Utilisation courante** :
  ```bash
  java MaClasse              # Exécuter un fichier de classe
  java -jar monapp.jar       # Exécuter un fichier JAR
  java -cp . MaClasse        # Exécuter avec un classpath spécifique
  ```
- **Exemple** : `java -Xmx512m -jar monapp.jar` (exécute un JAR avec un tas maximum de 512 Mo).

---

### 3. **javadoc** - Générer la documentation d'API
- **Objectif** : Créer une documentation HTML à partir des commentaires du code source Java.
- **Utilisation courante** :
  ```bash
  javadoc -d docs MaClasse.java  # Générer la documentation dans le dossier 'docs'
  ```
- **Exemple** : `javadoc -d docs -sourcepath src -subpackages com.example` (générer la documentation pour un package).

---

### 4. **jcmd** - Envoyer des commandes de diagnostic à une JVM en cours d'exécution
- **Objectif** : Interagir avec un processus Java en cours d'exécution pour le diagnostic (ex. : dumps de threads, infos du tas).
- **Utilisation courante** :
  ```bash
  jcmd <pid> help           # Lister les commandes disponibles pour un processus JVM
  jcmd <pid> Thread.print   # Afficher un dump des threads
  ```
- **Exemple** : `jcmd 1234 GC.run` (déclencher le garbage collection pour le PID 1234).

---

### 5. **jdb** - Débogueur Java
- **Objectif** : Déboguer des applications Java de manière interactive.
- **Utilisation courante** :
  ```bash
  jdb MaClasse               # Démarrer le débogage d'une classe
  java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MaClasse  # Exécuter avec l'agent de débogage
  jdb -attach localhost:5005  # Se connecter à une JVM en cours d'exécution
  ```
- **Exemple** : `jdb -sourcepath src MaClasse` (déboguer avec le code source).

---

### 6. **jdeps** - Analyser les dépendances de classes et de JAR
- **Objectif** : Identifier les dépendances d'une application ou d'une bibliothèque Java.
- **Utilisation courante** :
  ```bash
  jdeps monapp.jar           # Analyser les dépendances dans un JAR
  jdeps -s MaClasse.class    # Résumé des dépendances
  ```
- **Exemple** : `jdeps -v monapp.jar` (analyse verbose des dépendances).

---

### 7. **jhsdb** - Débogueur Java HotSpot
- **Objectif** : Débogage et analyse avancés des processus JVM (ex. : core dumps).
- **Utilisation courante** :
  ```bash
  jhsdb jmap --heap --pid <pid>  # Analyser le tas d'un processus en cours d'exécution
  jhsdb hsdb                     # Lancer l'interface graphique du débogueur HotSpot
  ```
- **Exemple** : `jhsdb jmap --heap --pid 1234` (afficher les infos du tas pour le processus 1234).

---

### 8. **jinfo** - Voir ou modifier la configuration de la JVM
- **Objectif** : Inspecter ou modifier les options JVM pour un processus en cours d'exécution.
- **Utilisation courante** :
  ```bash
  jinfo <pid>               # Voir les flags et propriétés JVM
  jinfo -flag +PrintGC <pid>  # Activer un flag JVM
  ```
- **Exemple** : `jinfo -sysprops 1234` (afficher les propriétés système pour le processus 1234).

---

### 9. **jmap** - Dumper la mémoire ou les informations du tas de la JVM
- **Objectif** : Générer des dumps du tas ou des statistiques mémoire.
- **Utilisation courante** :
  ```bash
  jmap -heap <pid>          # Afficher un résumé du tas
  jmap -dump:file=dump.hprof <pid>  # Créer un dump du tas
  ```
- **Exemple** : `jmap -dump:live,format=b,file=dump.hprof 1234` (dumper les objets vivants).

---

### 10. **jpackage** - Empaqueter des applications Java
- **Objectif** : Créer des installateurs ou exécutables natifs pour des applications Java (ex. : .deb, .rpm, .exe).
- **Utilisation courante** :
  ```bash
  jpackage --input target --name MonApp --main-jar monapp.jar --main-class MaClasse
  ```
- **Exemple** : `jpackage --type deb --input target --name MonApp --main-jar monapp.jar` (créer un package Debian).

---

### 11. **jps** - Lister les processus JVM en cours d'exécution
- **Objectif** : Afficher les processus Java avec leurs identifiants de processus (PID).
- **Utilisation courante** :
  ```bash
  jps                       # Lister tous les processus Java
  jps -l                    # Inclure les noms de classe complets
  ```
- **Exemple** : `jps -m` (afficher la classe principale et les arguments).

---

### 12. **jrunscript** - Exécuter des scripts en Java
- **Objectif** : Exécuter des scripts (ex. : JavaScript) en utilisant le moteur de script Java.
- **Utilisation courante** :
  ```bash
  jrunscript -e "print('Hello')"  # Exécuter une seule commande de script
  jrunscript script.js            # Exécuter un fichier de script
  ```
- **Exemple** : `jrunscript -l js -e "print(2+2)"` (exécuter du code JavaScript).

---

### 13. **jshell** - REPL Java interactif
- **Objectif** : Exécuter des fragments de code Java de manière interactive pour tester ou apprendre.
- **Utilisation courante** :
  ```bash
  jshell                    # Démarrer le shell interactif
  jshell script.jsh         # Exécuter un script JShell
  ```
- **Exemple** : `jshell -q` (démarrer JShell en mode silencieux).

---

### 14. **jstack** - Générer des dumps de threads
- **Objectif** : Capturer les traces de pile des threads dans une JVM en cours d'exécution.
- **Utilisation courante** :
  ```bash
  jstack <pid>              # Afficher le dump des threads
  jstack -l <pid>           # Inclure les informations de verrouillage
  ```
- **Exemple** : `jstack 1234 > threads.txt` (sauvegarder le dump des threads dans un fichier).

---

### 15. **jstat** - Surveiller les statistiques de la JVM
- **Objectif** : Afficher les statistiques de performance (ex. : garbage collection, utilisation mémoire).
- **Utilisation courante** :
  ```bash
  jstat -gc <pid>           # Afficher les stats du garbage collection
  jstat -class <pid> 1000   # Afficher les stats de chargement de classe toutes les 1 seconde
  ```
- **Exemple** : `jstat -gcutil 1234 1000 5` (afficher les stats GC 5 fois, toutes les 1 seconde).

---

### 16. **jstatd** - Démon de surveillance JVM
- **Objectif** : Exécuter un serveur de surveillance distant pour permettre à des outils comme `jstat` de se connecter à distance.
- **Utilisation courante** :
  ```bash
  jstatd -J-Djava.security.policy=jstatd.policy
  ```
- **Exemple** : `jstatd -p 1099` (démarrer le démon sur le port 1099).

---

### 17. **keytool** - Gérer les clés cryptographiques et les certificats
- **Objectif** : Créer et gérer des keystores pour des applications Java sécurisées.
- **Utilisation courante** :
  ```bash
  keytool -genkeypair -alias macle -keystore keystore.jks  # Générer une paire de clés
  keytool -list -keystore keystore.jks                     # Lister le contenu du keystore
  ```
- **Exemple** : `keytool -importcert -file cert.pem -keystore keystore.jks` (importer un certificat).

---

### 18. **rmiregistry** - Démarrer le registre RMI
- **Objectif** : Exécuter un registre pour les objets Java Remote Method Invocation (RMI).
- **Utilisation courante** :
  ```bash
  rmiregistry               # Démarrer le registre RMI sur le port par défaut (1099)
  rmiregistry 1234          # Démarrer sur un port spécifique
  ```
- **Exemple** : `rmiregistry -J-Djava.rmi.server.codebase=file:./classes/` (démarrer avec une codebase).

---

### 19. **serialver** - Générer serialVersionUID pour les classes
- **Objectif** : Calculer le `serialVersionUID` pour les classes Java implémentant `Serializable`.
- **Utilisation courante** :
  ```bash
  serialver MaClasse         # Afficher le serialVersionUID pour une classe
  ```
- **Exemple** : `serialver -classpath . com.example.MaClasse` (calculer pour une classe spécifique).

---

### 20. **javac** - Compilateur Java
- **Objectif** : Compiler les fichiers source Java en bytecode.
- **Utilisation courante** :
  ```bash
  javac MaClasse.java        # Compiler un seul fichier
  javac -d bin *.java       # Compiler vers un répertoire spécifique
  ```
- **Exemple** : `javac -cp lib/* -sourcepath src -d bin src/MaClasse.java` (compiler avec des dépendances).

---

### 21. **javap** - Désassembler les fichiers de classe
- **Objectif** : Voir le bytecode ou les signatures de méthode d'une classe compilée.
- **Utilisation courante** :
  ```bash
  javap -c MaClasse          # Désassembler le bytecode
  javap -s MaClasse          # Afficher les signatures de méthode
  ```
- **Exemple** : `javap -c -private MaClasse` (afficher les méthodes privées et le bytecode).

---

### 22. **jconsole** - Outil de surveillance graphique de la JVM
- **Objectif** : Surveiller les performances de la JVM (mémoire, threads, CPU) via une interface graphique.
- **Utilisation courante** :
  ```bash
  jconsole                  # Démarrer JConsole et se connecter à une JVM locale
  jconsole <pid>            # Se connecter à un processus spécifique
  ```
- **Exemple** : `jconsole localhost:1234` (se connecter à une JVM distante).

---

### 23. **jdeprscan** - Scanner les API dépréciées
- **Objectif** : Identifier l'utilisation d'API dépréciées dans un JAR ou un fichier de classe.
- **Utilisation courante** :
  ```bash
  jdeprscan monapp.jar       # Scanner un JAR pour les API dépréciées
  ```
- **Exemple** : `jdeprscan --release 11 monapp.jar` (vérifier par rapport aux API Java 11).

---

### 24. **jfr** - Java Flight Recorder
- **Objectif** : Gérer et analyser les données de profilage Java Flight Recorder.
- **Utilisation courante** :
  ```bash
  jfr print recording.jfr   # Afficher le contenu d'un fichier JFR
  jfr summary recording.jfr # Résumer un fichier JFR
  ```
- **Exemple** : `jfr print --events GC recording.jfr` (afficher les événements GC).

---

### 25. **jimage** - Inspecter ou extraire les fichiers JIMAGE
- **Objectif** : Travailler avec les fichiers JIMAGE (utilisés dans les modules JDK).
- **Utilisation courante** :
  ```bash
  jimage extract image.jimage  # Extraire le contenu d'un fichier JIMAGE
  ```
- **Exemple** : `jimage list image.jimage` (lister le contenu d'un JIMAGE).

---

### 26. **jlink** - Créer des images d'exécution Java personnalisées
- **Objectif** : Construire un JRE minimal avec uniquement les modules requis.
- **Utilisation courante** :
  ```bash
  jlink --module-path mods --add-modules java.base --output monjre
  ```
- **Exemple** : `jlink --add-modules java.base,java.sql --output jre-personnalise` (créer un JRE avec des modules spécifiques).

---

### 27. **jmod** - Gérer les fichiers JMOD
- **Objectif** : Créer ou gérer les fichiers JMOD (utilisés pour les modules JDK).
- **Utilisation courante** :
  ```bash
  jmod create --class-path classes monmod.jmod  # Créer un fichier JMOD
  jmod list monmod.jmod                        # Lister le contenu
  ```
- **Exemple** : `jmod extract monmod.jmod` (extraire le contenu JMOD).

---

### 28. **jwebserver** - Serveur HTTP simple
- **Objectif** : Exécuter un serveur web basique pour servir des fichiers statiques.
- **Utilisation courante** :
  ```bash
  jwebserver -d /chemin/vers/dossier  # Démarrer le serveur pour un répertoire
  jwebserver -p 8080          # Démarrer sur un port spécifique
  ```
- **Exemple** : `jwebserver -d ./html -p 8000` (servir les fichiers de ./html sur le port 8000).

---

### Conseils pour Approfondir
- **Documentation** : Exécutez `nom_du_tool --help` ou consultez la documentation du JDK d'Oracle (ex. : https://docs.oracle.com/en/java/javase/21/docs/specs/man/).
- **Pages de manuel** : Utilisez `man nom_du_tool` pour les outils avec des pages de manuel.
- **Pratique** : Expérimentez dans un projet test pour comprendre le comportement des outils.
- **Outils de surveillance** : Pour `jcmd`, `jmap`, `jstack`, etc., utilisez `jps` pour trouver le PID de votre processus Java.
- **Débogage** : Combinez `jdb`, `jhsdb` ou `jconsole` pour un débogage avancé.

Si vous travaillez sur un projet de trading (comme le suggère votre répertoire), les outils comme `javac`, `java`, `jar` et `jpackage` sont probablement les plus pertinents pour compiler, exécuter et empaqueter votre application. Pour le réglage des performances, utilisez `jstat`, `jmap` ou `jfr`. Faites-moi savoir si vous avez besoin d'une exploration plus approfondie d'un outil spécifique ou d'aide avec votre projet de trading !