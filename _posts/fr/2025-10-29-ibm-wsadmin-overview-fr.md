---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation de l'outil IBM WebSphere wsadmin
translated: true
type: note
---

### Aperçu de wsadmin dans IBM WebSphere Application Server (WAS)

L'outil `wsadmin` est une interface de script en ligne de commande pour administrer WebSphere Application Server. Il vous permet d'automatiser des tâches telles que la gestion des serveurs, le déploiement d'applications, la configuration des ressources et la surveillance des opérations d'exécution. Les scripts peuvent être écrits en Jython (basé sur Python) ou en JACL (basé sur Tcl), Jython étant le plus couramment utilisé en raison de sa lisibilité.

- **`wsadmin.bat`** : Utilisé sur les systèmes Windows.
- **`wsadmin.sh`** : Utilisé sur les systèmes Unix/Linux/AIX.

Les deux outils se trouvent dans le répertoire `bin` d'un profil WebSphere (par exemple, `<WAS_HOME>/profiles/<NomDuProfil>/bin/`) ou de l'installation de base (`<WAS_HOME>/bin/`). Il est recommandé de les exécuter à partir du répertoire `bin` du profil pour garantir l'environnement correct.

#### Démarrage interactif de wsadmin
Cela lance un shell où vous pouvez saisir des commandes directement.

**Syntaxe :**
```
wsadmin[.bat|.sh] [options]
```

**Exemple de base (Windows) :**
```
cd C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin
wsadmin.bat -lang jython -user admin -password mypass
```

**Exemple de base (Unix/Linux) :**
```
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
./wsadmin.sh -lang jython -user admin -password mypass
```

- `-lang jython` : Spécifie Jython (utilisez `-lang jacl` pour JACL).
- `-user` et `-password` : Requis si la sécurité globale est activée (omettez si elle est désactivée).
- S'ils sont omis, il se connecte au serveur local en utilisant le connecteur SOAP par défaut sur le port 8879 (ou RMI sur 2809).

Une fois dans l'invite wsadmin (par exemple, `wsadmin>`), vous pouvez exécuter des commandes en utilisant des objets de script :
- **AdminConfig** : Pour les modifications de configuration (par exemple, création de ressources).
- **AdminControl** : Pour les opérations d'exécution (par exemple, démarrage/arrêt des serveurs).
- **AdminApp** : Pour le déploiement/la mise à jour d'applications.
- **AdminTask** : Pour les tâches de haut niveau (par exemple, synchronisation des nœuds).
- **Help** : Pour l'aide intégrée (par exemple, `Help.help()`).

**Exemples de commandes dans le shell :**
- Lister tous les serveurs : `print AdminConfig.list('Server')`
- Démarrer un serveur : `AdminControl.invoke(AdminControl.completeObjectName('type=ServerIndex,process=server1,*'), 'start')`
- Sauvegarder les modifications : `AdminConfig.save()`
- Quitter : `quit`

#### Exécution d'un fichier de script
Utilisez l'option `-f` pour exécuter un script Jython (.py ou .jy) ou JACL (.jacl) de manière non interactive.

**Exemple de script (deployApp.py) :**
```python
# Se connecter et déployer une application
appName = 'MyApp'
AdminApp.install('/path/to/MyApp.ear', '[-appname ' + appName + ']')
AdminConfig.save()
print 'Application ' + appName + ' deployed successfully.'
```

**Exécution sur Windows :**
```
wsadmin.bat -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

**Exécution sur Unix/Linux :**
```
./wsadmin.sh -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

#### Exécution d'une commande unique
Utilisez l'option `-c` pour des commandes ponctuelles (utile dans les fichiers batch ou l'automatisation).

**Exemple (extrait de fichier batch Windows) :**
```batch
@echo off
call "C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin\wsadmin.bat" -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

**Exemple (extrait de script shell Unix) :**
```bash
#!/bin/bash
./wsadmin.sh -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

#### Options principales

| Option | Description | Exemple |
|--------|-------------|---------|
| `-conntype` | Type de connecteur : `SOAP` (par défaut, port 8879) ou `RMI` (port 2809). | `-conntype RMI` |
| `-host` | Hôte distant auquel se connecter. | `-host myhost.example.com` |
| `-port` | Port du connecteur. | `-port 8879` |
| `-tracefile` | Journaliser la sortie dans un fichier. | `-tracefile wsadmin.log` |
| `-profile` | Exécuter un script de profil avant le script principal. | `-profile init.py` |
| `-c` | Exécuter une seule commande (non interactif). | `-c "AdminConfig.save()"` |
| `-f` | Exécuter un fichier de script. | `-f myscript.py` |
| `-job` | Exécuter une commande du gestionnaire de travaux. | `-job deploy.xml` |

#### Conseils et bonnes pratiques
- **Sécurité** : Si la sécurité globale est désactivée, omettez `-user` et `-password`. Pour les configurations sécurisées, utilisez des informations d'identification chiffrées ou des fichiers de clés.
- **Mode client léger** : Pour l'administration à distance sans une installation complète de WAS, utilisez `wsadmin -conntype NONE` avec les JARs du client léger (par exemple, `com.ibm.ws.admin.client_*.jar`).
- **Performance** : Pour plusieurs commandes, utilisez un seul script avec `-f` au lieu d'appels répétés avec `-c` pour éviter la surcharge de la JVM.
- **Gestion des erreurs** : Appelez toujours `AdminConfig.save()` après les modifications de configuration. Utilisez try-except en Jython pour la robustesse.
- **Génération de commandes** : Dans la console d'administration WAS, effectuez une action et cliquez sur "View administrative scripting command for last action" pour obtenir la commande wsadmin équivalente.
- **Notes de version** : Le comportement est cohérent entre WAS 8.5+ et 9.0+, mais vérifiez la documentation IBM pour les détails spécifiques à la version (par exemple, Jython 2.7 dans les versions plus récentes).

Pour une utilisation plus avancée, explorez l'objet AdminTask pour des commandes simplifiées comme `AdminTask.importFile('path/to/file')`.

### Références
- [wsadmin scripting tool - IBM Docs](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-wsadmin-tool)
- [Getting started with wsadmin scripting - IBM Docs](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/txml_script.html)
- [WAS - wsadmin (Jython) Tutorial](http://www.mtitek.com/tutorials/websphere/wsadmin_jython.php)
- [IBM WebSphere - Getting Started with wsadmin](https://www.freekb.net/Article?id=1563)
- [WSADMIN Tutorial – Part1](https://websphereapplicationservernotes.wordpress.com/2012/12/25/wsadmin-tutorial-part1/)