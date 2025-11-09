---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Jython dans WebSphere Application Server
translated: true
type: note
---

### Utilisation de Jython dans IBM WebSphere Application Server

Note : "jPython" fait référence à Jython, une implémentation de Python qui s'exécute sur la machine virtuelle Java (JVM). Il est couramment utilisé dans WebSphere pour les scripts d'administration et peut également être intégré dans les applications déployées. WebSphere Application Server (WAS) inclut Jython (généralement la version 2.1 ou ultérieure, selon la version de WAS) dans `<WAS_HOME>/optionalLibraries/jython`, donc une installation séparée n'est généralement pas nécessaire. Ci-dessous, je vais couvrir les deux principaux cas d'utilisation : les tâches administratives et l'utilisation à l'exécution dans les applications.

#### 1. Scripting administratif avec wsadmin
La manière la plus courante d'utiliser Jython dans WebSphere est pour les tâches de gestion de serveur comme le déploiement d'applications, le démarrage/arrêt des serveurs, la configuration des ressources et le listing des applications installées. Cela se fait via l'outil `wsadmin`, qui prend en charge Jython comme langage de script privilégié (remplaçant Jacl qui est déprécié).

**Prérequis :**
- Assurez-vous que le serveur WebSphere est en cours d'exécution.
- Localisez `wsadmin` dans `<WAS_HOME>/bin/wsadmin.sh` (Linux/Unix) ou `wsadmin.bat` (Windows).
- Jython est pré-inclus ; pour des fonctionnalités plus récentes (par exemple, la syntaxe Python 2.5+), vous devrez peut-être effectuer une mise à niveau via un classpath personnalisé (voir les notes avancées ci-dessous).

**Étapes de base pour exécuter un script Jython :**
1. Créez un fichier de script Jython (par exemple, `example.py`) avec votre code. Utilisez les objets AdminConfig, AdminControl et AdminApp pour les opérations spécifiques à WebSphere.
   
   Exemple de script pour lister toutes les applications installées (`listApps.py`) :
   ```
   # Lister toutes les applications
   apps = AdminApp.list()
   print("Applications Installées :")
   for app in apps.splitlines():
       if app.strip():
           print(app.strip())
   AdminConfig.save()  # Optionnel : Sauvegarder les changements de configuration
   ```

2. Exécutez le script en utilisant `wsadmin` :
   - Connexion via SOAP (par défaut pour une connexion distante) :  
     ```
     wsadmin.sh -lang jython -f listApps.py -host <nom_hôte> -port <port_soap> -user <utilisateur_admin> -password <mot_de_passe_admin>
     ```
   - Pour une connexion locale (sans hôte/port) :  
     ```
     wsadmin.sh -lang jython -f listApps.py
     ```
   - Exemple de sortie : Liste les applications comme `DefaultApplication`.

3. Pour le mode interactif (REPL) :  
   ```
   wsadmin.sh -lang jython
   ```
   Puis tapez les commandes Jython directement, par exemple, `print AdminApp.list()`.

**Exemples courants :**
- **Déployer un EAR/WAR :** Créez `deployApp.py` :
  ```
  appName = 'MyApp'
  earPath = '/chemin/vers/MyApp.ear'
  AdminApp.install(earPath, '[-appname ' + appName + ' -server server1]')
  AdminConfig.save()
  print('Application déployée : ' + appName)
  ```
  Exécutez : `wsadmin.sh -lang jython -f deployApp.py`.

- **Démarrer/Arrêter un Serveur :**  
  ```
  server = AdminControl.completeObjectName('type=Server,process=server1,*')
  AdminControl.invoke(server, 'start')  # Ou 'stop'
  ```

- **Spécifier la version de Jython (si nécessaire) :** Pour Jython 2.1 explicitement :  
  `wsadmin.sh -usejython21 true -f script.py`. Pour les versions personnalisées, ajoutez au classpath : `-wsadmin_classpath /chemin/vers/jython.jar`.

**Conseils :**
- Utilisez `AdminConfig.help('type_objet')` pour l'aide sur les commandes.
- Les scripts peuvent être automatisés dans un pipeline CI/CD (par exemple, Jenkins) en appelant `wsadmin` dans des fichiers batch.
- Pour un client léger (sans installation complète de WAS) : Téléchargez les jars client depuis IBM et définissez le classpath.

#### 2. Utilisation de Jython dans les Applications Déployées
Pour exécuter du code Jython au sein d'une application Java (par exemple, une servlet ou un EJB) s'exécutant sur WebSphere, incluez l'environnement d'exécution Jython (jython.jar) dans le classpath de l'application. Cela permet d'intégrer des scripts Python ou d'utiliser Jython comme moteur de script. Téléchargez le dernier jython.jar depuis le site officiel de Jython si la version incluse est obsolète.

Il existe deux méthodes principales : **Classpath** (au niveau du serveur) ou **Bibliothèque Partagée** (réutilisable entre les applications).

**Méthode 1 : Classpath (Ajout direct à la JVM)**
1. Sauvegardez `jython.jar` dans un chemin accessible sur l'hôte WebSphere (par exemple, `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/meslibs/jython.jar`).
2. Connectez-vous à la Console d'Administration WebSphere.
3. Naviguez vers **Serveurs > Types de serveurs > Serveurs d'applications WebSphere > [Votre Serveur]**.
4. Allez dans **Java et Gestion des processus > Définition du processus > Machine virtuelle Java > Classpath**.
5. Ajoutez le chemin complet vers `jython.jar` (par exemple, `/opt/.../jython.jar`).
6. Dans **Arguments génériques de la JVM**, ajoutez le chemin Python :  
   `-Dpython.path=/opt/.../jython.jar/Lib` (pointe vers la bibliothèque standard de Jython).
7. Cliquez sur **OK**, sauvegardez la configuration et redémarrez le serveur.
8. Synchronisez les nœuds si vous êtes dans un environnement en cluster (via **Administration du système > Nœuds > Synchroniser**).
9. Dans votre code Java, utilisez `org.python.util.PythonInterpreter` pour exécuter des scripts Jython :
   ```
   import org.python.util.PythonInterpreter;
   PythonInterpreter interpreter = new PythonInterpreter();
   interpreter.exec("print('Bonjour depuis Jython dans WebSphere !')");
   ```

**Méthode 2 : Bibliothèque Partagée (Recommandée pour plusieurs applications)**
1. Placez `jython.jar` dans un répertoire partagé (par exemple, `/shared/libs/jython.jar`).
2. Dans la Console d'Administration : **Environnement > Bibliothèques partagées > [Portée : Serveur ou Cellule] > Nouveau**.
3. Entrez un nom (par exemple, `JythonLib`), cochez **Utiliser un répertoire de bibliothèque native**, et définissez **Classpath** sur `/shared/libs/jython.jar`.
4. Sauvegardez.
5. Pour une application spécifique : **Applications > Types d'applications > Applications d'entreprise WebSphere > [Votre App] > Référencer les bibliothèques partagées**.
6. Sous **Références aux bibliothèques partagées**, cliquez sur **Ajouter**, sélectionnez `JythonLib`, et définissez **Classpath** pour correspondre.
7. Sauvegardez, mettez à jour l'application (redémarrez si nécessaire), et synchronisez les nœuds.
8. Référencez dans le code comme dans la méthode Classpath.

**Conseils pour les Applications :**
- Pour les applications Jython basées sur les servlets, utilisez PyServlet (inclus dans Jython) pour les gestionnaires Python.
- Testez dans un environnement de développement ; surveillez les journaux pour les problèmes de classpath.
- Si vous utilisez une version plus récente de Jython (par exemple, 2.7), assurez-vous de la compatibilité avec Java 8+.

#### Notes Avancées
- **Compatibilité des versions :** WAS 9.x utilise Jython 2.7+. Pour les mises à niveau, remplacez le jar inclus mais testez minutieusement.
- **Gestion des erreurs :** Dans les scripts, utilisez `try: ... except Exception as e: print(e)`.
- **Support IDE :** Utilisez IBM Rational Application Developer (RAD) ou Eclipse avec les plugins WebSphere pour déboguer les scripts Jython/wsadmin.
- **Ressources :** Pour des tutoriels complets, consultez le livre *WebSphere Application Server Administration Using Jython* ou la documentation wsadmin d'IBM.

Si cela ne correspond pas exactement à votre scénario (par exemple, version spécifique de WAS ou cas d'utilisation), fournissez plus de détails pour un conseil personnalisé.

**Références :**  
- [Utilisation du scripting wsadmin avec Jython (Documentation IBM)](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-using-wsadmin-jython)  
- [Déploiement de Jython sur WebSphere (Guide Oracle)](https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/deploying-jython-on-ais-server-on-ibm-websphere-application.html)  
- [Intégration Jython WebSphere (Stack Overflow)](https://stackoverflow.com/questions/25187577/will-the-ibm-websphere-application-server-run-the-python-jython-script-without-p)  
- [Wiki Jython sur WebSphere](https://wiki.python.org/jython/WebSphere)  
- [Exemple de Déploiement d'Application avec Jython](https://jobhunterssite.wordpress.com/2016/05/12/deploy-an-application-in-websphere-using-jython-automation/)