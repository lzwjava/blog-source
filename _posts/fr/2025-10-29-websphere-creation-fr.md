---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Création correcte de WebSphere Application Server
translated: true
type: note
---

Non, la commande `nodeName -name serverName admin create applciation server` (en notant la faute de frappe dans "applciation") n'est pas correcte pour créer un serveur d'applications dans IBM WebSphere Application Server (WAS) en utilisant le script wsadmin.

### Syntaxe Correcte
La commande appropriée utilise la méthode `AdminTask.createApplicationServer` en Jython (le langage de script recommandé pour wsadmin). Elle nécessite :
- Le **nom du nœud** comme premier argument (une chaîne de caractères).
- Une **liste d'options** comme second argument, incluant `-name` pour le nom du serveur.

**Exemple de base :**
```jython
AdminTask.createApplicationServer('YourNodeName', ['-name', 'YourServerName'])
```

- Remplacez `'YourNodeName'` par le nom du nœud réel (par exemple, `ndnode1`).
- Remplacez `'YourServerName'` par le nom de serveur souhaité (par exemple, `appServer1`).
- Des paramètres optionnels peuvent être ajoutés à la liste, comme `'-templateName', 'default'` pour utiliser un modèle de serveur par défaut.

### Étapes pour l'Exécuter
1. Démarrez wsadmin en mode Jython : `./wsadmin.sh -lang jython -user admin -password pass`.
2. Exécutez la commande ci-dessus.
3. Sauvegardez la configuration : `AdminConfig.save()`.
4. Quittez : `quit`.

Cela crée un serveur d'applications de base sur le nœud spécifié. Pour plus d'options (par exemple, les ports, les paramètres JVM), référez-vous à la documentation complète d'AdminTask.

[Groupe de commandes ServerManagement pour l'objet AdminTask](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-servermanagement-command-group-admintask-object)  
[Création d'un serveur à l'aide de scripts](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-creating-server-using)