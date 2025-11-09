---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Déploiement du module EAR de remplacement dans WebSphere
translated: true
type: note
---

### Déploiement d'un nouveau fichier EAR pour remplacer un existant dans IBM WebSphere Application Server (WAS)

Remplacer un fichier EAR (Enterprise Archive) dans IBM WAS est une tâche de déploiement standard, mais il est crucial de suivre les bonnes pratiques pour éviter les interruptions de service, les incohérences de configuration ou les erreurs d'exécution. Ci-dessous, je vais détailler les points clés que vous devez vérifier et confirmer avant, pendant et après le processus de téléchargement/déploiement. Ceci suppose que vous utilisez la Console d'Administration WAS (ou le script wsadmin pour l'automatisation), et que vous travaillez dans un environnement pris en charge (par exemple, WAS 8.5, 9.x, ou le profil Liberty).

#### 1. **Préparatifs Pré-Déploiement (À confirmer avant le téléchargement)**
   - **Sauvegarder l'Application Actuelle** :
     - Exportez l'EAR existant depuis la console (Applications > Applications d'entreprise > [Nom App] > Exporter) ou sauvegardez l'intégralité de la configuration en utilisant la commande `backupConfig` via wsadmin.
     - Pourquoi ? Permet une restauration si le nouveau EAR cause des problèmes. Confirmez que la sauvegarde est complète et stockée en sécurité.

   - **Vérifications de Compatibilité** :
     - Vérifiez que le nouveau EAR a été compilé pour la bonne version de WAS (par exemple, version Java, spécifications EJB comme Jakarta EE vs. Java EE).
     - Vérifiez les fonctionnalités dépréciées dans votre version de WAS (par exemple, via la documentation IBM Knowledge Center). Exécutez `wsadmin` avec `AdminConfig.validateAppDeployment` si possible.
     - Confirmez que le descripteur de déploiement de l'EAR (application.xml, ibm-application-ext.xmi) correspond aux modules de votre serveur (WARs, JARs inside the EAR).

   - **Dépendances Environnement et Ressources** :
     - Vérifiez les ressources JNDI : Sources de données, files d'attente JMS, variables d'environnement. Assurez-vous que toutes les ressources référencées (par exemple, les fournisseurs JDBC) sont configurées et saines. Testez les connexions via la console (Ressources > JDBC > Sources de données).
     - Sécurité : Confirmez que les rôles utilisateur, les contraintes de sécurité et les mappages (par exemple, dans ibm-application-bnd.xmi) sont alignés avec votre realm (par exemple, LDAP, fédéré). Vérifiez si le nouveau EAR nécessite de nouveaux realms personnalisés ou certificats.
     - Politiques de Classloader : Notez le mode actuel du classloader WAR (PARENT_FIRST ou PARENT_LAST) et les références aux bibliothèques partagées—assurez-vous qu'il n'y a pas de conflits avec le nouveau EAR.
     - Clustering / Haute Disponibilité : Si dans un environnement en cluster, confirmez que le nouveau EAR est identique sur tous les nœuds et planifiez des déploiements progressifs pour minimiser l'interruption.

   - **Détails Spécifiques à l'Application** :
     - Racine de Contexte et Hôtes Virtuels : Confirmez que la racine de contexte n'est pas en conflit avec d'autres applications (Applications > [Nom App] > Racine de contexte pour les modules Web).
     - Port et Mappage : Vérifiez les mappages de servlets et tous les modèles d'URL.
     - Propriétés Personnalisées : Vérifiez les propriétés personnalisées spécifiques à l'application définies dans la console—celles-ci pourraient nécessiter une réapplication après le déploiement.

   - **Tester le Nouveau EAR** :
     - Compilez et testez l'EAR dans un environnement de staging/dev d'abord. Utilisez des outils comme Rational Application Developer ou Eclipse avec les plugins WAS pour valider.
     - Recherchez les problèmes connus : Utilisez la recherche des Correctifs (Fix Packs) et APARs d'IBM pour votre version de WAS.

#### 2. **Pendant le Téléchargement et le Déploiement**
   - **Arrêter l'Application Actuelle** :
     - Dans la console : Applications > Applications d'entreprise > [Nom App] > Arrêter. Confirmez qu'elle est complètement arrêtée (pas de sessions actives si l'affinité de session est activée).
     - Sauvegardez la configuration et synchronisez les nœuds dans un environnement en cluster (Administration du système > Nœuds > Synchroniser).

   - **Télécharger le Nouveau EAR** :
     - Allez dans Applications > Nouvelle Application > Nouvelle Application d'entreprise.
     - Téléchargez le fichier EAR. Pendant l'assistant :
       - Sélectionnez "Remplacer l'application existante" si demandé (ou désinstallez d'abord l'ancienne via Applications > [Nom App] > Désinstaller).
       - Passez en revue les options de déploiement : Mappez les modules aux serveurs, ciblez les clusters et les bibliothèques partagées.
       - Confirmez étape par étape dans l'assistant : Les liaisons des rôles de sécurité, les références de ressources et l'exhaustivité des métadonnées.
     - Si vous utilisez wsadmin : Scriptez avec `AdminApp.update` ou `installInteractive` pour les remplacements. Exemple :
       ```
       wsadmin> AdminApp.update('AppName', '[-operation update -contenturi /path/to/new.ear]')
       ```
       Validez toujours avec `AdminConfig.validateAppDeployment` avant d'appliquer.

   - **Synchronisation de la Configuration** :
     - Après le téléchargement, sauvegardez la configuration maître et synchronisez vers les gestionnaires de déploiement/nœuds.
     - Vérifiez les avertissements/erreurs dans le résumé de déploiement—traitez immédiatement tout problème de liaison de module.

   - **Démarrer l'Application** :
     - Démarrez via la console et confirmez qu'elle s'initialise sans erreur (surveillez les fichiers SystemOut.log et SystemErr.log dans le répertoire logs du profil).

#### 3. **Vérification Post-Déploiement**
   - **Journaux et Surveillance** :
     - Surveillez les journaux en temps réel (par exemple, `tail -f profile/logs/server1/SystemOut.log`) pour confirmer le succès du déploiement, les erreurs de liaison ou les exceptions au démarrage.
     - Utilisez la section Dépannage > Journaux et traces de la console pour des traces détaillées si nécessaire. Confirmez l'absence de ClassNotFoundException ou NoSuchMethodError.

   - **Tests Fonctionnels** :
     - Test de fumée : Accédez à l'application via son URL et vérifiez les fonctions principales (par exemple, connexion, appels d'API).
     - Test de charge si critique—vérifiez les fuites de mémoire ou les régressions de performance.
     - Intégrations Base de Données/Externes : Exécutez des requêtes ou des appels pour confirmer le flux de données.

   - **Plan de Retour Arrière** :
     - Confirmez que vous pouvez redéployer rapidement l'EAR sauvegardé. Mettez en place des contrôles de santé (par exemple, via IBM Health Center ou des scripts personnalisés).

#### Pièges Courants à Surveiller
- **Gestion des Sessions** : Si l'application utilise HTTPSession, drainez les sessions actives avant l'arrêt pour éviter la perte de données.
- **Permissions de Fichiers** : Assurez-vous que le fichier EAR a les permissions de lecture pour l'utilisateur WAS (par exemple, wasadmin).
- **Taille et Temps** : Les EAR volumineux peuvent prendre du temps à déployer—planifiez pendant les fenêtres de maintenance.
- **Différences du Profil Liberty** : Si vous utilisez WAS Liberty, les déploiements se font via des modifications de server.xml ou `install-feature` ; confirmez que les configurations XML correspondent.
- **Notes Spécifiques à la Version** : Pour WAS 9+, vérifiez les changements liés à microProfile ou CDI. Référez-vous toujours à la documentation IBM pour votre version exacte.

Si vous fournissez plus de détails (par exemple, version de WAS, configuration en cluster, ou erreurs spécifiques rencontrées), je peux affiner ces conseils. Pour des directives officielles, consultez l'IBM Knowledge Center ou le portail de support. Faites-moi savoir comment je peux vous aider davantage !