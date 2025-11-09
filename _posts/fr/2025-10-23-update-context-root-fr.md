---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Mise à jour du contexte racine de WebSphere
translated: true
type: note
---

### Mise à jour de la racine de contexte Web dans IBM WebSphere Application Server (WAS)

La racine de contexte Web définit le chemin URL de base pour votre application web (par exemple, `/myapp`). Dans IBM WebSphere Application Server, vous pouvez la mettre à jour soit lors du déploiement initial, soit pour une application existante via la Console d'administration. Vous trouverez ci-dessous les étapes pour une application existante. Assurez-vous d'avoir un accès administratif à la console WAS.

#### Prérequis
- Accès à la Console d'administration WebSphere (généralement à l'adresse `https://your-server:9043/ibm/console`).
- L'application doit être installée et arrêtée (recommandé) avant d'effectuer des modifications pour éviter les conflits.

#### Étapes pour mettre à jour la racine de contexte
1. **Se connecter à la Console d'administration** :
   - Ouvrez un navigateur web et accédez à l'URL de la console WAS.
   - Saisissez vos identifiants administrateur.

2. **Naviguer vers l'Application** :
   - Dans le volet de navigation de gauche, développez **Applications** > **Types d'applications** > **Applications d'entreprise WebSphere**.
   - Localisez et sélectionnez votre application déployée dans la liste.

3. **Accéder aux paramètres de la racine de contexte** :
   - Sur la page de détails de l'application, descendez jusqu'à la section **Propriétés des modules Web**.
   - Cliquez sur **Racine de contexte pour les modules Web**.

4. **Modifier la racine de contexte** :
   - Dans le tableau qui s'affiche, trouvez le module Web (par exemple, le nom de votre fichier WAR).
   - Mettez à jour le champ **Racine de contexte** avec la nouvelle valeur (par exemple, changez de `/oldapp` à `/newapp`). Évitez les barres obliques initiales si elles ne sont pas nécessaires, mais incluez-les pour les chemins comme `/myapp`.
   - Cliquez sur **OK** pour enregistrer les modifications.

5. **Sauvegarder et synchroniser la configuration** :
   - Cliquez sur **Sauvegarder** dans la console (ou **Sauvegarder directement dans la configuration maître** si vous y êtes invité).
   - Si vous êtes dans un environnement en cluster ou de déploiement réseau :
     - Allez dans **Administration du système** > **Noeuds**.
     - Sélectionnez tous les noeuds concernés et cliquez sur **Resynchronisation complète**.

6. **Redémarrer l'Application** :
   - Retournez dans **Applications** > **Applications d'entreprise WebSphere**.
   - Sélectionnez votre application et cliquez sur **Arrêter**, puis sur **Démarrer**.
   - Alternativement, redémarrez le serveur entier via **Serveurs** > **Types de serveurs** > **Serveurs d'applications WebSphere** > sélectionnez le serveur > **Redémarrer**.

7. **Vérifier le changement** :
   - Accédez à l'URL de l'application dans un navigateur (par exemple, `http://your-server:9080/newapp`).
   - Vérifiez les journaux du serveur (par exemple, `SystemOut.log`) pour toute erreur liée au déploiement.

#### Notes supplémentaires
- **Lors du déploiement initial** : Si vous déployez une nouvelle application, spécifiez la racine de contexte à l'étape **Sélectionner les options d'installation** sous **Racine de contexte** pour chaque module Web.
- **Fichiers EAR** : Pour les applications regroupées dans un EAR, assurez-vous que le `application.xml` ne code pas en dur la racine de contexte ; les remplacements dans la console ont priorité.
- **Problèmes courants** :
  - Les changements peuvent ne pas s'appliquer si l'application est en cours d'exécution — arrêtez-la toujours d'abord.
  - Dans WebSphere Liberty ou Open Liberty, utilisez les configurations du fichier `server.xml` à la place.
  - Pour les hôtes virtuels ou les plugins, mettez à jour la configuration du plugin du serveur web après les modifications.
- Si l'application utilise la sécurité ou des bibliothèques partagées, testez-la minutieusement après la mise à jour.

Pour plus de détails, reportez-vous à la documentation officielle d'IBM ou aux guides de la communauté.

#### Références
- [Paramètres de la racine de contexte pour les modules Web](https://www.ibm.com/docs/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/uweb_contextroot.html)
- [IBM WebSphere - Racine de contexte d'une application](https://www.freekb.net/Article?id=1647)
- [Changement de racine de contexte WebSphere 8.5 ne s'appliquant pas au fichier WAR](https://stackoverflow.com/questions/24472790/websphere-8-5-context-root-change-not-applying-to-war-file)