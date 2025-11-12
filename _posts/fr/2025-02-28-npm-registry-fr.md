---
audio: false
generated: true
lang: fr
layout: post
title: Test du Registre NPM
translated: true
type: note
---

Pour tester si votre registre NPM fonctionne, surtout parce qu'il nécessite un nom d'utilisateur et un mot de passe, vous pouvez suivre quelques étapes simples pour vérifier sa connectivité, son authentification et sa capacité à servir des packages. Comme il s'agit d'un registre privé (ce qui est sous-entendu par les informations d'identification), vous devrez vous assurer que l'authentification est correctement configurée avant de tester l'installation d'un package. Voici un guide complet pour tester votre registre, ainsi que quelques suggestions de packages NPM à essayer d'installer.

---

### Étapes pour tester le registre

1. **Configurer l'authentification**
   - Puisque le registre nécessite un nom d'utilisateur et un mot de passe, vous devez vous connecter pour authentifier votre client NPM.
   - Exécutez la commande suivante dans votre terminal, en remplaçant `<registry-url>` par l'URL réelle de votre registre :
     ```
     npm login --registry=<registry-url>
     ```
   - Il vous sera demandé de saisir votre nom d'utilisateur et votre mot de passe (et éventuellement un email, selon le registre). Une fois terminé, cela stocke un jeton d'authentification dans votre fichier `.npmrc`, permettant ainsi l'accès au registre.

2. **Vérifier la connexion au registre**
   - Utilisez la commande `npm ping` pour vérifier si le registre est accessible :
     ```
     npm ping --registry=<registry-url>
     ```
   - Si elle réussit, cette commande confirme que le serveur de registre est opérationnel et répond. Vous verrez généralement une sortie comme "Ping success: <registry-url>". Si elle échoue, il peut y avoir un problème de connectivité ou l'URL peut être incorrecte.

3. **Vérifier l'authentification**
   - Pour vous assurer que votre nom d'utilisateur et votre mot de passe sont correctement configurés, utilisez la commande `npm whoami` :
     ```
     npm whoami --registry=<registry-url>
     ```
   - Cette commande devrait retourner votre nom d'utilisateur si l'authentification est réussie. Si elle échoue ou retourne une erreur (par exemple, "not authenticated"), vérifiez à nouveau vos informations d'identification ou l'étape de connexion.

4. **Tester l'installation d'un package**
   - Essayez d'installer un package pour confirmer que le registre peut servir des packages. Comme il s'agit d'un registre privé, vous devrez installer un package dont vous savez qu'il existe dessus. Cependant, si le registre proxyfie le registre public NPM (une configuration courante pour les registres privés comme Verdaccio), vous pouvez tester avec des packages publics populaires.
   - Exemple de commande :
     ```
     npm install <package-name> --registry=<registry-url>
     ```
   - Remplacez `<package-name>` par un package disponible sur votre registre (plus de suggestions de packages ci-dessous).

---

### Quelques packages NPM à essayer

Comme il s'agit d'un registre privé, je ne peux pas savoir exactement quels packages sont disponibles. Cependant, voici quelques suggestions basées sur des scénarios courants :

- **Si le registre proxyfie le registre public NPM :**
  - De nombreux registres privés sont configurés pour refléter le registre public, permettant l'accès aux packages publics après authentification. Dans ce cas, vous pouvez essayer d'installer des packages publics bien connus :
    - `lodash` : Une bibliothèque utilitaire populaire.
      ```
      npm install lodash --registry=<registry-url>
      ```
    - `express` : Un framework web largement utilisé pour Node.js.
      ```
      npm install express --registry=<registry-url>
      ```
    - `react` : Une bibliothèque populaire pour construire des interfaces utilisateur.
      ```
      npm install react --registry=<registry-url>
      ```
  - Si ces installations réussissent, cela confirme que le registre fonctionne et peut servir des packages.

- **Si le registre héberge uniquement des packages privés :**
  - Vous devrez installer un package dont vous savez qu'il existe sur votre registre privé. Vérifiez auprès de votre équipe ou de l'interface web/documentation du registre (si disponible) un nom de package. Par exemple :
    - S'il existe un package nommé `my-org-utils`, essayez :
      ```
      npm install my-org-utils --registry=<registry-url>
      ```
  - Sans noms de packages spécifiques, je ne peux pas lister de packages privés exacts, utilisez donc un package pertinent pour votre organisation.

---

### Notes et dépannage

- **Indicateurs de succès** : Si `npm ping` fonctionne, `npm whoami` retourne votre nom d'utilisateur et qu'un package s'installe sans erreur, votre registre fonctionne correctement.
- **Problèmes courants** :
  - **Erreurs d'authentification** : Re-exécutez `npm login` si `npm whoami` échoue.
  - **Package non trouvé** : Assurez-vous que le package existe sur le registre. Si vous utilisez un package public et que l'installation échoue, votre registre ne proxyfie peut-être pas le registre public.
  - **Problèmes de connexion** : Vérifiez à nouveau l'`<registry-url>` et vos paramètres réseau si `npm ping` échoue.
- **Évitez les changements globaux** : Pour éviter d'affecter votre configuration NPM globale, vous pouvez tester dans un nouveau répertoire avec un fichier `.npmrc` local, mais les commandes ci-dessus avec le drapeau `--registry` sont suffisantes pour les tests.

En suivant ces étapes et en essayant les packages suggérés, vous pouvez confirmer que votre registre est opérationnel et qu'il gère correctement l'authentification et la récupération des packages. Si vous avez des noms de packages spécifiques provenant de votre registre, utilisez-les plutôt que les exemples publics fournis.