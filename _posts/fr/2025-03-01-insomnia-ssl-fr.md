---
audio: false
generated: true
lang: fr
layout: post
title: Validation de certificat SSL dans Insomnia
translated: true
---

Pour résoudre l'erreur "SSL peer certificate or SSH remote key was not OK" dans Insomnia, cette erreur survient généralement lorsque Insomnia ne peut pas vérifier le certificat SSL du serveur auquel vous essayez de vous connecter. Voici des solutions étape par étape pour résoudre ce problème :

### 1. **Désactiver la validation du certificat SSL (Pour le développement local uniquement)**
Si vous travaillez avec un serveur de développement local qui utilise un certificat SSL auto-signé ou invalide, vous pouvez désactiver la validation du certificat dans Insomnia :
- Ouvrez Insomnia et allez dans **Application** > **Préférences**.
- Accédez à la section **Request / Response**.
- Décochez la case intitulée **Validate certificates**.
- Rétentez votre requête.

**Important** : Cette option contourne les vérifications de sécurité et ne doit être utilisée **que pour les tests ou le développement local**. Ne l'utilisez pas dans des environnements de production, car elle rend votre connexion vulnérable.

---

### 2. **Vérifier le certificat SSL du serveur**
L'erreur peut indiquer un problème avec le certificat SSL du serveur (par exemple, expiré, auto-signé ou incompatibilité de nom d'hôte). Pour vérifier :
- Ouvrez l'URL du serveur dans un navigateur web.
- Cliquez sur l'icône de cadenas dans la barre d'adresse pour afficher les détails du certificat.
- Assurez-vous que le certificat est valide, non expiré et correspond au nom de domaine.
- Si le certificat est invalide ou mal configuré, contactez l'administrateur du serveur pour le corriger.

---

### 3. **Importer un certificat client (si nécessaire)**
Si le serveur nécessite un certificat client pour l'authentification, vous devrez le configurer dans Insomnia :
- Dans Insomnia, allez dans **Client Certificates** (accessible depuis le tableau de bord principal ou les préférences).
- Cliquez sur **Add Certificate**.
- Importez votre fichier de certificat (formats supportés : PFX ou PEM).
- Assignez-le au domaine ou au nom d'hôte spécifique auquel vous vous connectez.
- Testez à nouveau la requête.

---

### 4. **Mettre à jour Insomnia**
Les problèmes liés au SSL peuvent être dus à un bug dans une version plus ancienne d'Insomnia. Pour vous assurer d'être sur la dernière version :
- Vérifiez les mises à jour dans **Application** > **About** ou téléchargez la dernière version depuis le site officiel d'Insomnia.
- Installez la mise à jour et réessayez votre requête.

---

### 5. **Tester avec Curl**
Si les étapes ci-dessus ne résolvent pas le problème, testez la requête en dehors d'Insomnia pour isoler le problème :
- Ouvrez un terminal et utilisez la commande `curl` avec la même URL et les mêmes paramètres (par exemple, `curl -v https://example.com`).
- Si `curl` échoue également, le problème est probablement lié à la configuration du serveur plutôt qu'à Insomnia.
- Si `curl` réussit, cela peut indiquer un problème spécifique à Insomnia, et vous pouvez le signaler à leur équipe de support.

---

### Résumé
Commencez par désactiver la validation SSL si c'est un serveur local, puis vérifiez le certificat du serveur ou configurez un certificat client si nécessaire. Assurez-vous qu'Insomnia est à jour et utilisez `curl` pour dépanner davantage si nécessaire. Ces étapes devraient résoudre la plupart des cas d'erreur "SSL peer certificate or SSH remote key was not OK".

Si le problème persiste, il peut être dû à une mauvaise configuration côté serveur ou à un bug rare dans Insomnia. Faites-le moi savoir si vous avez besoin de plus d'assistance !