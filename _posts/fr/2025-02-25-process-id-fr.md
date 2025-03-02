---
audio: false
generated: true
lang: fr
layout: post
title: Identifiant de processus (PID) du serveur en cours d'exécution
translated: true
---

Étant donné que vous utilisez WebSphere Liberty Profile (WLP) version 24.0.0.9 et que vous devez trouver l'ID de processus (PID) du serveur en cours d'exécution, mais vous avez indiqué que le fichier `.pid` attendu à `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` n'est pas disponible, voici comment vous pouvez localiser le PID en utilisant des méthodes alternatives.

L'approche standard décrite dans les instructions repose sur le fait que Liberty stocke le PID dans un fichier `.pid` après le démarrage du serveur. Cependant, si ce fichier est manquant—probablement en raison d'un problème de configuration, d'un démarrage échoué ou d'une installation différente—vous pouvez toujours identifier le PID en utilisant des outils système, à condition que le serveur soit en cours d'exécution. Voici des étapes fiables pour trouver le PID sur un système de type Unix (par exemple, Linux). Si vous utilisez Windows, faites-le moi savoir, et je pourrai ajuster les instructions en conséquence.

### Étape 1 : Vérifier que le serveur est en cours d'exécution
Avant de rechercher le PID, assurez-vous que le serveur Liberty est actif. Vous pouvez :
- **Vérifier les journaux** : Recherchez dans `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` ou `messages.log` des messages de démarrage, tels que "Server <serverName> started."
- **Accéder au serveur** : Si le serveur héberge une application web, essayez d'y accéder via un navigateur (par exemple, `http://localhost:<port>`).

Si le serveur n'est pas en cours d'exécution, il n'y aura pas de PID à trouver, donc cette étape est cruciale.

### Étape 2 : Utiliser des commandes système pour trouver le PID
Étant donné que le fichier `.pid` n'est pas disponible, vous pouvez utiliser des outils en ligne de commande pour localiser le processus Java associé au serveur Liberty. Liberty s'exécute comme un processus Java, donc des outils qui listent les processus Java ou réseau peuvent aider. Voici deux méthodes efficaces :

#### Méthode 1 : Utiliser `ps` pour lister les processus Java
La commande `ps` affiche les processus en cours d'exécution. Pour filtrer les processus Java, y compris le serveur Liberty, exécutez :
```bash
ps -ef | grep java
```
Cela liste tous les processus avec "java" dans leur ligne de commande. La sortie pourrait ressembler à :
```
user  12345  1  0  10:00 ?  00:00:00 /path/to/java -jar /path/to/liberty/wlp/bin/tools/ws-server.jar <serverName>
```
- La deuxième colonne (par exemple, `12345`) est le PID.
- Recherchez une ligne mentionnant "liberty", "wlp" ou votre `<serverName>` (par exemple, `defaultServer`) pour identifier le processus correct.

Pour affiner davantage, si vous connaissez le nom du serveur, essayez :
```bash
ps -ef | grep <serverName>
```

#### Méthode 2 : Utiliser `jps` (outil spécifique à Java)
Si vous avez le Java Development Kit (JDK) installé, la commande `jps` est une manière plus simple de lister les processus Java. Exécutez :
```bash
jps -l
```
La sortie pourrait ressembler à :
```
12345 com.ibm.ws.kernel.boot.Launcher
```
- La première colonne (par exemple, `12345`) est le PID.
- Recherchez un nom de classe lié à Liberty, tel que `com.ibm.ws.kernel.boot.Launcher`, qui est couramment associé au démarrage de Liberty.

Cette méthode est souvent plus propre que `ps` car elle ne montre que les processus Java.

### Étape 3 : Optionnel - Utiliser le numéro de port (si connu)
Si vous connaissez le numéro de port sur lequel le serveur Liberty écoute (par exemple, à partir de `server.xml` ou des journaux), vous pouvez utiliser `netstat` pour trouver le PID :
```bash
netstat -anp | grep <port_number>
```
La sortie pourrait inclure :
```
tcp  0  0  0.0.0.0:<port_number>  0.0.0.0:*  LISTEN  12345/java
```
- Le PID (par exemple, `12345`) apparaît après les détails du port.

### Recommandation
- **Méthode préférée** : Utilisez `jps -l` si le JDK est disponible, car il est adapté aux processus Java et identifie probablement clairement le serveur Liberty.
- **Méthode de secours** : Utilisez `ps -ef | grep java` si `jps` n'est pas une option, et identifiez manuellement le processus Liberty en inspectant les détails de la commande.

### Conseils de dépannage
Si aucune des commandes ne trouve le processus Liberty :
- Vérifiez à nouveau que le serveur est en cours d'exécution (Étape 1).
- Vérifiez vos chemins `<WLP_HOME>` et `<serverName>` ; le processus pourrait faire référence à un répertoire inattendu.
- Redémarrez le serveur avec `server start <serverName>` et vérifiez si le fichier `.pid` apparaît, ou consultez les journaux de démarrage pour des indices sur la raison de son absence.

En utilisant ces étapes, vous devriez pouvoir localiser le PID de votre serveur Liberty 24.0.0.9 en cours d'exécution malgré l'absence du fichier `.pid`. Faites-le moi savoir si vous avez besoin d'une assistance supplémentaire !