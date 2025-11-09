---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Diagnostiquer les Blocages Java avec jstack
translated: true
type: note
---

### Utilisation de jstack pour diagnostiquer les blocages ou les arrêts des applications Java

jstack est un outil en ligne de commande inclus dans le JDK qui génère des instantanés de threads (thread dumps) pour une Machine Virtuelle Java (JVM) en cours d'exécution. Les instantanés de threads capturent l'état de tous les threads à un moment donné, ce qui est crucial pour identifier les causes des blocages, telles que les interblocages (deadlocks), les boucles infinies, les E/S bloquées ou les opérations intensives en CPU. Il est particulièrement utile sur les systèmes Linux/Unix ou dans des environnements multiplateformes.

#### Étapes pour utiliser jstack :
1. **Identifier l'ID de processus Java (PID) :**
   - Exécutez `jps` (également inclus dans le JDK) pour lister tous les processus Java :  
     ```
     jps -l
     ```
     Cela affiche quelque chose comme `12345 MyApp.jar`. Notez le PID (par exemple, 12345).

   - Alternativement, utilisez les commandes du système d'exploitation comme `ps aux | grep java` sur Linux/macOS.

2. **Générer un instantané de threads :**
   - Exécutez jstack avec le PID pour envoyer l'instantané dans un fichier :  
     ```
     jstack <PID> > thread-dump.txt
     ```
     - Remplacez `<PID>` par votre identifiant de processus.
     - Pour un instantané plus détaillé (incluant les verrous), utilisez `jstack -l <PID> > thread-dump.txt`.
     - Si la JVM ne répond pas aux signaux, utilisez `jhsdb jstack --pid <PID>` (disponible à partir de JDK 8+).

3. **Capturer plusieurs instantanés pour l'analyse :**
   - Les blocages nécessitent souvent une comparaison dans le temps. Prenez 3 à 5 instantanés à des intervalles de 10 à 30 secondes :  
     ```
     jstack <PID> > dump1.txt
     sleep 10
     jstack <PID> > dump2.txt
     sleep 10
     jstack <PID> > dump3.txt
     ```
     - Automatisez cela dans une boucle si nécessaire (par exemple, en utilisant un script bash).

4. **Analyser l'instantané :**
   - Ouvrez le fichier texte dans un éditeur ou un IDE.
   - Recherchez :
     - **États des threads :** Concentrez-vous sur les threads dans l'état `RUNNABLE` (actif), `BLOCKED` (en attente d'un verrou, risque d'interblocage), `WAITING` (en attente inactive) ou `TIMED_WAITING`.
     - **Interblocages :** Recherchez le mot "deadlock" ou utilisez des outils comme `jstack -l` qui les signalent.
     - **Traces de la pile d'appel (Stack Traces) :** Identifiez les motifs répétitifs ou les blocages dans des méthodes spécifiques (par exemple, une boucle infinie).
     - **Frames natives :** Si les threads sont bloqués dans du code natif, cela peut indiquer des problèmes JNI ou des blocages au niveau du système d'exploitation.
   - Outils pour une analyse plus approfondie : VisualVM, Eclipse MAT, ou les analyseurs en ligne comme fastThread.io. Par exemple, dans VisualVM, chargez le fichier d'instantané sous l'onglet "Thread" pour visualiser les verrous et les états.

Si la JVM ne répond pas (par exemple, pas de sortie avec `kill -3 <PID>` sur Unix), le blocage pourrait être au niveau du système d'exploitation — envisagez des images mémoire complètes (core dumps) via `gcore <PID>`.

### Utilisation de ProcDump pour diagnostiquer les blocages ou les arrêts de processus

ProcDump est un outil Sysinternals gratuit pour Windows qui crée des images mémoire (dumps) de processus, basées sur la mémoire ou le CPU. Il est excellent pour capturer des instantanés de blocages dans n'importe quelle application (y compris Java), surtout lorsque le processus ne répond pas. Utilisez-le pour des images mémoire complètes à analyser avec des outils comme WinDbg ou Visual Studio.

#### Étapes pour utiliser ProcDump :
1. **Téléchargement et configuration :**
   - Obtenez ProcDump sur le site Microsoft Sysinternals (procdump.exe).
   - Exécutez l'invite de commandes en tant qu'Administrateur.
   - Accédez au dossier contenant procdump.exe.

2. **Identifier le processus :**
   - Utilisez le Gestionnaire des tâches ou `tasklist | findstr <nom-du-processus>` pour obtenir le PID ou le nom de l'image (par exemple, `java.exe`).

3. **Capturer une image mémoire pour blocage :**
   - Pour une image mémoire complète immédiate (utile pour les processus bloqués) :  
     ```
     procdump -ma <nom-du-processus-ou-PID>
     ```
     - `-ma` : Image mémoire complète (inclut tous les threads et le tas mémoire - heap).
     - Exemple : `procdump -ma java.exe` ou `procdump -ma 12345`.

   - Pour la détection automatique de blocage (se déclenche sur un manque de réponse) :  
     ```
     procdump -h <nom-du-processus-ou-PID> -o
     ```
     - `-h` : Surveille les blocages (processus ne répondant pas aux messages de fenêtre pendant plus de 5 secondes ; pour les services sans fenêtres, utilisez des seuils CPU comme `-h 80` pour 80% de CPU).
     - `-o` : Écrase les images existantes.
     - Pour les services : Combinez avec `-e` pour les exceptions ou surveillez le CPU : `procdump -c 80 -h <service-exe>`.

   - Prenez plusieurs images : Ajoutez `-n 3` pour 3 images à des intervalles (par exemple, `-t 10` pour un délai de 10 secondes) :  
     ```
     procdump -ma -n 3 -t 10 <PID>
     ```

4. **Analyser l'image mémoire :**
   - Les images sont enregistrées sous forme de fichiers `.dmp` dans le répertoire courant.
   - Ouvrez-les avec WinDbg (gratuit de Microsoft) ou le Débogueur Visual Studio.
   - Commandes clés dans WinDbg :
     - `!threads` : Liste les threads et leurs états (recherchez les états bloqué/en attente).
     - `~<id-du-thread>s` : Passe à un thread et utilisez `k` pour la trace de la pile.
     - `!analyze -v` : Analyse automatique pour les blocages/interblocages.
   - Pour une analyse spécifique à Java, chargez l'image dans Eclipse MAT ou utilisez `jhat` sur une image du tas mémoire (si capturée avec l'option `-mh`).

ProcDump fonctionne bien pour les processus non interactifs comme les services ; si le blocage est lié au CPU, utilisez `-c` pour déclencher sur une charge CPU élevée.

### Conseils généraux pour les deux outils
- **Sécurité :** Les images mémoire peuvent être volumineuses (Go pour la mémoire complète) ; assurez-vous d'avoir assez d'espace disque.
- **Combinez les outils :** Pour Java sur Windows, utilisez d'abord jstack (plus léger), puis ProcDump pour une analyse plus approfondie au niveau du système d'exploitation.
- **Prévention :** Activez les options JVM comme `-XX:+PrintGCDetails` pour la journalisation, ou utilisez des agents comme JFR pour le profilage.
- Si les images mémoire ne montrent aucun problème clair, vérifiez les ressources système (CPU, mémoire, E/S) avec des outils comme `top` ou le Moniteur de performance.

[Oracle Java Troubleshooting Guide](https://docs.oracle.com/en/java/javase/17/troubleshoot/troubleshoot-process-hangs-and-loops.html)  
[Taking a Hang Dump with ProcDump](https://www.poppastring.com/blog/taking-a-hang-dump-or-crash-dump-with-procdump)  
[Java Thread Dump Analysis](https://www.baeldung.com/java-analyze-thread-dumps)  
[ProcDump Usage for Hangs](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)