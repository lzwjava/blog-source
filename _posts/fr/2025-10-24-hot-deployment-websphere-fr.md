---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Déploiement à chaud dans WebSphere WAS
translated: true
type: note
---

### Comprendre le Hot Deployment et le Hotswap dans WebSphere Application Server (WAS)

Le hot deployment (également appelé rechargement à chaud ou hot swapping) est une technique de développement qui permet de mettre à jour et de déployer des modifications sur votre application—telles que du code, de la configuration ou des ressources—sans nécessiter un redémarrage complet du serveur d'applications. Ceci est particulièrement précieux lors des cycles de développement itératifs, où des modifications fréquentes du code (par exemple, corriger des bugs, ajuster la logique ou mettre à jour des éléments d'interface utilisateur) seraient autrement ralenties par les longs temps de démarrage du serveur, surtout dans des environnements d'entreprise comme IBM WebSphere Application Server (WAS). Redémarrer une instance WAS peut prendre des minutes, voire plus pour les grandes applications, perturbant ainsi les flux de travail et les tests.

L'extrait que vous avez fourni se concentre sur les stratégies pratiques pour obtenir des itérations plus rapides dans WAS, en mettant l'accent sur les déploiements WAR "explosés" et les outils pour un hot swapping amélioré. Je vais décomposer cela étape par étape, en expliquant les concepts, leur fonctionnement, leurs limites et des conseils de mise en œuvre.

#### 1. Déployer en tant que WAR "Explosé" (Déploiement Décompressé)
Un fichier WAR (Web Application Archive) est essentiellement un bundle zippé contenant les ressources de votre application web : JSP, servlets, classes Java, fichiers statiques (HTML/CSS/JS), bibliothèques (JARs) et fichiers de configuration (par exemple, web.xml). Par défaut, les WARs sont déployés en tant que fichiers **packagés** (zippés), que WAS traite comme immuables—toute modification nécessite de re-packager et de redéployer l'archive entière.

Un **WAR explosé** fait référence au fait de décompresser (dézipper) le fichier WAR dans une structure de répertoires avant le déploiement. Cela permet de modifier des fichiers ou des sous-répertoires individuels directement sur le système de fichiers du serveur sans toucher à l'archive entière.

**Pourquoi cela permet des itérations plus rapides :**
- **Mises à jour au niveau fichier :** Vous pouvez modifier un seul fichier JSP ou une classe Java, et WAS peut détecter et recharger uniquement ce composant.
- **Pas de re-packaging :** Évite la surcharge liée au zip/dézip répété de gros WARs.
- **Synergie avec le rechargement à chaud :** Facilite la surveillance et l'actualisation des fichiers modifiés par le serveur.

**Comment déployer un WAR explosé dans WAS :**
- **En utilisant la Console d'Administration :**
  1. Connectez-vous à la WAS Integrated Solutions Console (généralement à `http://localhost:9060/ibm/console`).
  2. Naviguez vers **Applications > New Application > New Enterprise Application**.
  3. Au lieu de sélectionner un fichier WAR packagé, pointez vers le répertoire racine de votre WAR décompressé (par exemple, `/chemin/vers/myapp.war/`—notez la barre oblique finale indiquant qu'il s'agit d'un répertoire).
  4. Complétez l'assistant de déploiement, en vous assurant que les options "Deploy Web services" et autres correspondent à votre application.
- **En utilisant wsadmin (outil de script) :**
  ```bash
  wsadmin.sh -c "AdminApp.install('/chemin/vers/myapp', '[ -MapWebModToVH [[myapp .* default_host.* virtual_host ]]]')"
  ```
  Remplacez `/chemin/vers/myapp` par votre répertoire explosé.
- **Serveurs de développement (par exemple, Liberty Profile) :** Pour des tests plus légers, utilisez Open Liberty (une variante de WAS) avec `server start` et placez votre application explosée dans le dossier `dropins` pour un déploiement automatique.

**Bonnes pratiques :**
- Utilisez un outil de contrôle de source (par exemple, Git) pour synchroniser les changements de votre IDE vers le répertoire explosé.
- Surveillez l'espace disque, car les déploiements explosés consomment plus de stockage.
- En production, utilisez des WARs packagés pour la sécurité et la cohérence—le hot deployment est principalement pour dev/test.

Une fois déployé de manière explosée, les mécanismes intégrés de WAS peuvent s'enclencher pour un rechargement partiel à chaud.

#### 2. Support Natif du Hot-Reload par WAS
WAS fournit un support natif pour le rechargement à chaud de certains composants sans redémarrage complet, mais il est limité. Cela repose sur le mécanisme de **scrutage de fichiers** du serveur, où WAS scanne périodiquement le répertoire de déploiement explosé à la recherche de modifications (configurable via des arguments JVM comme `-DwasStatusCheckInterval=5` pour des vérifications toutes les 5 secondes).

**Ce que WAS supporte nativement :**
- **JSPs (JavaServer Pages) :**
  - Les JSPs sont compilées dynamiquement en servlets lors du premier accès. Si vous modifiez un fichier JSP dans un WAR explosé, WAS peut détecter le changement, le recompiler et recharger la servlet.
  - **Comment cela fonctionne :** Définissez `reloadInterval` dans `ibm-web-ext.xmi` (sous WEB-INF) à une valeur faible (par exemple, 1 seconde) pour des vérifications fréquentes. Ou utilisez le paramètre global dans **Servers > Server Types > WebSphere application servers > [votre_serveur] > Java and Process Management > Process definition > Java Virtual Machine > Custom properties** avec `com.ibm.ws.webcontainer.invokefilterscompatibility=true`.
  - **Limitations :** Ne fonctionne que pour les JSPs qui n'ont pas été mises en cache de manière agressive. Les JSPs complexes avec des includes ou des tags pourraient nécessiter un redémarrage de module.
- **Certaines classes Java (servlets et EJBs) :**
  - Pour les déploiements explosés, WAS peut recharger des fichiers de classe individuels s'ils se trouvent dans les répertoires WEB-INF/classes ou lib.
  - **Comment cela fonctionne :** Activez "Application reload" dans le descripteur de déploiement ou via la console : **Applications > [votre_app] > Manage Modules > [module] > Reload behavior > Reload enabled**.
  - Cela déclenche un **rechargement au niveau module**, qui est plus rapide qu'un redémarrage complet de l'application mais décharge/recharge tout de même le module entier (par exemple, votre application web).

**Limitations du support natif :**
- **Pas un vrai hotswap :** Les changements apportés à la logique principale de l'application (par exemple, modifier une méthode dans une classe de servlet en cours d'exécution) ne prendront pas effet sans décharger l'ancien classloader. Vous pourriez voir des `ClassNotFoundException` ou du code obsolète.
- **Perte d'état :** Les sessions, singletons ou connexions base de données peuvent être réinitialisés.
- **Spécificités du JDK IBM :** WAS utilise souvent le JDK d'IBM, qui présente des particularités concernant le rechargement de classes par rapport à OpenJDK/HotSpot.
- **Aucun support pour les changements structurels :** L'ajout de nouvelles classes, la modification de signatures de méthode ou la mise à jour d'annotations nécessitent un redémarrage.
- **Surcharge des performances :** Un scrutation fréquente peut solliciter les ressources en dev.

Pour des ajustements d'interface utilisateur basiques (modifications JSP) ou des mises à jour simples de classes, cela est suffisant et gratuit. Mais pour un "hotswap complet"—où vous pouvez modifier du code en cours d'exécution depuis un IDE avec débogueur attaché, comme Eclipse ou IntelliJ, et voir la modification appliquée instantanément—vous avez besoin d'outils tiers.

#### 3. Solutions de Hotswap Complet
Pour obtenir des modifications de code transparentes (par exemple, éditer le corps d'une méthode dans un IDE avec débogueur attaché comme Eclipse ou IntelliJ, et voir la modification s'appliquer instantanément), utilisez des plugins qui modifient le chargement de classes et l'instrumentation de la JVM.

**Option 1 : JRebel (Plugin Payant)**
- **Ce que c'est :** Un outil commercial de Perforce (anciennement ZeroTurnaround) qui fournit un hotswap complet pour les applications Java. Il instrumente votre bytecode au démarrage, permettant le rechargement des classes, des ressources et même des changements spécifiques aux frameworks (par exemple, les beans Spring, les entités Hibernate).
- **Pourquoi l'utiliser avec WAS :**
  - Intégration profonde avec WAS, incluant le support des WARs explosés, des bundles OSGi et du JDK IBM.
  - Gère des scénarios complexes comme la modification de signatures de méthode ou l'ajout de champs (au-delà des limites standard du hotswap JVMTI).
  - **Fonctionnalités :** Détection automatique des changements depuis votre IDE ; pas de redéploiement manuel ; préserve l'état de l'application.
- **Comment le configurer :**
  1. Téléchargez JRebel depuis le site officiel et installez-le en tant que plugin Eclipse/IntelliJ.
  2. Générez un fichier de configuration `rebel.xml` pour votre projet (généré automatiquement ou manuel).
  3. Ajoutez des arguments JVM à votre serveur WAS : `-javaagent:/chemin/vers/jrebel.jar` (chemin complet vers le JAR de l'agent).
  4. Démarrez WAS en mode debug (`-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000`).
  5. Attachez le débogueur de votre IDE et modifiez le code—JRebel synchronise les changements en direct.
- **Coût :** Basé sur un abonnement (~400$/utilisateur/an pour les individus ; les licences entreprise varient). Essai gratuit disponible.
- **Pour :** Fiable, convivial, excellent support WAS.
- **Contre :** Payant ; nécessite une configuration par projet.

**Option 2 : DCEVM + HotSwapAgent (Alternative Gratuite)**
- **Ce que c'est :** Une combinaison open-source pour un hotswapping avancé.
  - **DCEVM (Dynamic Code Evolution VM) :** Une JVM modifiée qui étend la JVMTI (Java Virtual Machine Tool Interface) de HotSpot pour permettre des redéfinitions de classe plus agressives (par exemple, ajouter/supprimer des méthodes, changer les hiérarchies).
  - **HotSwapAgent :** Un agent qui s'appuie sur DCEVM, fournissant une intégration IDE pour le rechargement automatique de classes.
- **Pourquoi l'utiliser avec WAS :**
  - Gratuit et puissant pour le développement, imitant les capacités de JRebel.
  - Supporte les modifications du corps des méthodes, les mises à jour de ressources et même certains rechargements de frameworks (via des plugins).
- **Note de compatibilité avec le JDK IBM de WAS :**
  - WAS est généralement livré avec le JDK J9 d'IBM, qui **ne supporte pas nativement DCEVM** (DCEVM est spécifique à HotSpot).
  - **Solution de contournement :** Passez à OpenJDK/HotSpot pour le développement (par exemple, via un remplacement de `JAVA_HOME` dans `setInitial.sh` ou les `jvm.options` de Liberty). Testez minutieusement—le garbage collection et les fonctionnalités de sécurité du JDK IBM pourraient différer.
  - En production, revenez au JDK IBM ; ceci est réservé au développement.
- **Comment le configurer :**
  1. **Installez DCEVM :**
     - Téléchargez le JAR du patcher DCEVM depuis GitHub (par exemple, `dcevm-11.0.0+7-full.jar` pour JDK 11+).
     - Exécutez : `java -jar dcevm.jar /chemin/vers/votre/jdk/jre/lib/server/jvm.dll server` (Windows) ou équivalent pour Linux (`libjvm.so`).
     - Cela modifie le binaire JVM de votre JDK—faites une sauvegarde d'abord !
  2. **Installez HotSwapAgent :**
     - Téléchargez `hotswap-agent.jar` depuis GitHub.
     - Ajoutez aux arguments JVM de WAS : `-XXaltjvm=dcevm -XX:+TraceClassLoading -javaagent:/chemin/vers/hotswap-agent.jar=DCEVM` (plus tous plugins, par exemple `=hotswap-spring` pour Spring).
  3. **Intégration IDE :**
     - Installez le plugin HotSwapAgent pour IntelliJ/Eclipse.
     - Démarrez WAS avec les arguments de debug comme ci-dessus.
     - Éditez et sauvegardez le code dans l'IDE—l'agent recharge automatiquement.
  4. **Test de compatibilité :**
     - Exécutez un test de fumée : Déployez une servlet simple, modifiez une méthode (par exemple, ajoutez une ligne de log), appelez l'endpoint, et vérifiez le changement sans redémarrage.
     - Vérifiez les logs pour des erreurs comme `HotSwap failed: method limit reached` (DCEVM a des limites sur les changements par classe).
- **Pour :** Gratuit, personnalisable (via des plugins pour Spring, CDI, etc.), supporté par la communauté.
- **Contre :** La configuration est délicate ; instabilité potentielle avec les JVMs non standard ; limité à HotSpot (testez soigneusement le changement de JDK IBM) ; moins abouti que JRebel.

#### Quand Utiliser Quoi
- **WAR explosé + Rechargement natif :** Pour des ajustements rapides de JSP/fichiers statiques en début de développement.
- **JRebel :** Si le budget le permet et que vous avez besoin d'une fiabilité de niveau entreprise.
- **DCEVM + HotSwapAgent :** Pour un hotswap complet gratuit, mais prévoyez du temps pour tester la compatibilité JVM.

En résumé, ces techniques transforment WAS d'un serveur lourd en un environnement de développement plus agile, réduisant les temps d'itération de plusieurs minutes à quelques secondes. Commencez avec les WARs explosés pour des gains immédiats, puis superposez les outils si nécessaire. Si vous rencontrez des erreurs spécifiques, partagez plus de détails pour le dépannage.

**Références :**  
[Documentation JRebel pour WebSphere](https://www.jrebel.com/products/jrebel/tutorials/deploy-jrebel-websphere)  
[Dépôt GitHub DCEVM](https://github.com/dcevm/dcevm)  
[Dépôt GitHub HotSwapAgent](https://github.com/HotswapProjects/HotswapAgent)  
[IBM Knowledge Center : Hot Deployment WebSphere](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-hot-deployment)