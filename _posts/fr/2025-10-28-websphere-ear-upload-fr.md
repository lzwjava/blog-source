---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre les erreurs de téléchargement de fichiers EAR volumineux dans WebSphere
translated: true
type: note
---

### Comprendre le problème
L'erreur "multipart file upload error" (souvent quelque chose comme `org.apache.commons.fileupload.FileUploadException: Processing of multipart/form-data request failed. File too large (errno:27)`) se produit généralement lors de la mise à jour d'un fichier EAR dans IBM WebSphere Application Server (WAS) via la Console Administrative. Ceci est courant pour les fichiers EAR volumineux (par exemple, >20 Mo) en raison de limites sur les téléchargements de fichiers, le stockage temporaire, la mémoire heap ou les contraintes de ressources du système d'exploitation. Ce n'est pas un problème avec le fichier EAR lui-même, mais avec la façon dont la console gère le téléchargement HTTP multipart.

### Correctifs rapides à essayer en premier
1. **Copier le fichier EAR sur le serveur et le déployer localement** :
   - Utilisez FTP/SCP pour transférer le nouveau fichier EAR vers un répertoire sur le serveur WAS (par exemple, `/opt/IBM/WebSphere/AppServer/installableApps/`).
   - Dans la Console d'administration : Allez dans **Applications > Types d'applications > Applications d'entreprise WebSphere**.
   - Sélectionnez votre application existante > **Mettre à jour**.
   - Choisissez **Remplacer ou ajouter un module unique** ou **Remplacer l'application entière**, puis sélectionnez **Système de fichiers local** et pointez vers le chemin du fichier EAR copié.
   - Cela contourne le téléchargement multipart via HTTP.

2. **Augmenter les limites de taille de fichier du système d'exploitation (Serveurs UNIX/Linux)** :
   - L'erreur `errno:27` signifie souvent que le fichier dépasse la limite ulimit pour le processus.
   - Exécutez `ulimit -f` en tant qu'utilisateur WAS (par exemple, `webadmin`) pour vérifier la limite actuelle.
   - Définissez-la sur illimitée : Ajoutez `ulimit -f unlimited` au profil shell de l'utilisateur (par exemple, `~/.bash_profile`) ou au script de démarrage du serveur.
   - Redémarrez le Deployment Manager (dmgr) et réessayez le téléchargement.

### Modifications de configuration dans WAS
1. **Augmenter la taille du Heap pour le Deployment Manager** :
   - Les fichiers EAR volumineux peuvent provoquer des erreurs OutOfMemory pendant le traitement.
   - Dans la Console d'administration : **Serveurs > Types de serveurs > Serveurs administratifs > Deployment Manager**.
   - Sous **Gestion Java et processus > Définition du processus > Machine virtuelle Java** :
     - Définissez **Taille de heap initiale** sur 1024 (ou plus, par exemple 2048 pour les fichiers EAR très volumineux).
     - Définissez **Taille de heap maximale** sur 2048 (ou plus).
   - Sauvegardez, redémarrez le dmgr et réessayez.

2. **Ajuster les limites de taille de session HTTP ou de publication (Post) (le cas échéant)** :
   - Pour les limites du conteneur web : **Serveurs > Types de serveurs > Serveurs d'applications WebSphere > [Votre Serveur] > Conteneur Web > Transports HTTP**.
   - Augmentez la **Taille maximale de publication (post)** (en octets) si elle est définie trop basse.
   - Remarque : Cela affecte indirectement l'application web de la console d'administration.

### Solution recommandée à long terme : Utiliser wsadmin pour les mises à jour
Pour les mises à jour volumineuses ou fréquentes, évitez entièrement la console - elle n'est pas fiable pour les gros fichiers. Utilisez l'outil de script wsadmin (Jython ou JACL) pour mettre à jour l'application.

#### Étapes :
1. Copiez le nouveau fichier EAR vers un chemin accessible par le serveur (par exemple, `/tmp/myapp.ear`).
2. Lancez wsadmin :  
   ```
   /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user admin -password pass
   ```
3. Exécutez ce script Jython pour mettre à jour :  
   ```python
   AdminApp.update('MyAppName', 'app', [-Map ModulesToApps, '[-MapWebModToVH [[default_host MyContext virtual_host]] ]'], [-Operation update], [-appname MyAppName], [-MapModulesToServers [[MyModule MyServer]]], [-nodefaultoptions], [-preCompileJSPs false], [-contextroot MyContext], [-noTxImport], [-connType SERVER], [ -contenturi /tmp/myapp.ear ])
   AdminConfig.save()
   ```
   - Remplacez `MyAppName` par le nom de votre application, `MyContext` par la racine de contexte (context root), `MyServer` par le serveur/cluster cible et `/tmp/myapp.ear` par le chemin du fichier EAR.
4. Synchronisez les nœuds si vous êtes dans un environnement en cluster : `AdminControl.invoke(AdminControl.completeServers(), 'sync')`.
5. Redémarrez l'application : **Applications > [App] > Redémarrer**.

Cette méthode est plus rapide, évite les limites de téléchargement et peut être scriptée pour l'automatisation (par exemple, via Jenkins).

### Conseils supplémentaires
- **Vérifier les journaux (Logs)** : Consultez `SystemOut.log` et `SystemErr.log` dans le profil dmgr pour plus de détails (par exemple, `/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/logs/dmgr/`).
- **Tester avec un fichier EAR plus petit** : Vérifiez si le problème est lié à la taille en créant une version minimale compressée.
- **Version de WAS** : Assurez-vous d'utiliser une version prise en charge (par exemple, 8.5, 9.0). Appliquez les derniers correctifs si nécessaire.
- Si l'erreur persiste (par exemple, timeout), augmentez le timeout HTTP dans **Environnement > Serveurs d'applications Web > [Serveur] > Paramètres du conteneur > Paramètres du conteneur Web > Conteneur web > Gestion des sessions > Configuration > Timeout**.

Si aucune de ces solutions ne fonctionne, partagez le message d'erreur exact et la version de WAS pour obtenir des conseils plus spécifiques.

### Références
- [Error during deploy of war file on Websphere Application Server 7.0](https://coderanch.com/t/459530/application-servers/Error-deploy-war-file-Websphere)
- [OutOfMemory errors while deploying applications in WebSphere Application Server](https://www.ibm.com/support/pages/outofmemory-errors-while-deploying-applications-websphere-application-server)
- [Maximum size limit of an Ear that can be deployed in WAS](https://stackoverflow.com/questions/58748076/maximum-size-limit-of-an-ear-that-can-be-deployed-in-was)
- [Deploying the enterprise archive (EAR) using the WebSphere Administrative Console](https://www.ibm.com/docs/en/configurepricequote/9.5.0?topic=cwaso-deploying-enterprise-archive-ear-using-websphere-admin-console)