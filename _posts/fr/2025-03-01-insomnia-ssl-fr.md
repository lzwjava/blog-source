---
audio: false
generated: true
lang: fr
layout: post
title: Validation de certificat SSL dans Insomnia
translated: true
type: note
---

Pour corriger l'erreur « SSL peer certificate or SSH remote key was not OK » dans Insomnia, cette erreur se produit généralement lorsqu'Insomnia ne peut pas vérifier le certificat SSL du serveur auquel vous essayez de vous connecter. Voici des solutions étape par étape pour résoudre ce problème :

### 1. **Désactiver la validation des certificats SSL (uniquement pour le développement local)**
Si vous travaillez avec un serveur de développement local qui utilise un certificat SSL auto-signé ou non valide, vous pouvez désactiver la validation des certificats dans Insomnia :
- Ouvrez Insomnia et allez dans **Application** > **Préférences**.
- Accédez à la section **Requête / Réponse**.
- Décochez la case **Valider les certificats**.
- Réessayez votre requête.

**Important** : Cette option contourne les vérifications de sécurité et ne doit être utilisée **que pour des tests ou du développement local**. Ne l'utilisez pas pour des environnements de production, car elle rend votre connexion vulnérable.

---

### 2. **Vérifier le certificat SSL du serveur**
L'erreur peut indiquer un problème avec le certificat SSL du serveur (par exemple, expiré, auto-signé ou non concordant avec le nom d'hôte). Pour vérifier :
- Ouvrez l'URL du serveur dans un navigateur web.
- Cliquez sur l'icône de cadenas dans la barre d'adresse pour voir les détails du certificat.
- Assurez-vous que le certificat est valide, n'est pas expiré et correspond au nom de domaine.
- Si le certificat est non valide ou mal configuré, contactez l'administrateur du serveur pour le corriger.

---

### 3. **Importer un certificat client (si nécessaire)**
Si le serveur nécessite un certificat client pour l'authentification, vous devrez le configurer dans Insomnia :
- Dans Insomnia, allez dans **Certificats clients** (accessible depuis le tableau de bord principal ou les préférences).
- Cliquez sur **Ajouter un certificat**.
- Importez votre fichier de certificat (les formats pris en charge incluent PFX ou PEM).
- Affectez-le au domaine ou nom d'hôte spécifique auquel vous vous connectez.
- Testez à nouveau la requête.

---

### 4. **Mettre à jour Insomnia**
Les problèmes liés au SSL peuvent être dus à un bogue dans une ancienne version d'Insomnia. Pour vous assurer d'utiliser la dernière version :
- Vérifiez les mises à jour dans **Application** > **À propos** ou téléchargez la dernière version sur le site officiel d'Insomnia.
- Installez la mise à jour et réessayez votre requête.

---

### 5. **Tester avec Curl**
Si les étapes ci-dessus ne résolvent pas le problème, testez la requête en dehors d'Insomnia pour isoler le problème :
- Ouvrez un terminal et utilisez la commande `curl` avec la même URL et les mêmes paramètres (par exemple, `curl -v https://example.com`).
- Si `curl` échoue également, le problème vient probablement de la configuration du serveur plutôt que d'Insomnia.
- Si `curl` réussit, cela peut indiquer un problème spécifique à Insomnia, et vous pouvez le signaler à leur équipe de support.

---

### Résumé
Commencez par désactiver la validation SSL s'il s'agit d'un serveur local, puis vérifiez le certificat du serveur ou configurez un certificat client si nécessaire. Assurez-vous qu'Insomnia est à jour et utilisez `curl` pour approfondir le dépannage si nécessaire. Ces étapes devraient résoudre la plupart des cas de l'erreur « SSL peer certificate or SSH remote key was not OK ».

Si le problème persiste, il peut être dû à une mauvaise configuration côté serveur ou à un bogue rare dans Insomnia. Faites-moi savoir si vous avez besoin d'une aide supplémentaire !