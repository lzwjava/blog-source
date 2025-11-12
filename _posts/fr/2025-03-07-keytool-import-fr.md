---
audio: false
generated: true
lang: fr
layout: post
title: Importer des certificats avec Keytool
translated: true
type: note
---

Pour répondre à votre question concernant l'utilisation de la commande `keytool -importcert` pour importer un certificat dans le fichier `jre/lib/security/cacerts` et la rencontre d'une erreur "password verification failed" avec une `java.security.UnrecoverableException`, décomposons cela étape par étape pour comprendre le problème, comment le résoudre et quel pourrait être le mot de passe possible.

### Comprendre le problème

L'utilitaire `keytool` est un outil en ligne de commande inclus dans le Java Development Kit (JDK) utilisé pour gérer les keystores. Un keystore est un fichier qui stocke des clés cryptographiques et des certificats, souvent pour sécuriser les communications réseau comme SSL/TLS. Le fichier `cacerts`, situé dans `jre/lib/security`, est un keystore spécifique livré avec l'Environment d'exécution Java (JRE). Il contient une collection de certificats racines de confiance provenant d'Autorités de Certification (CA) bien connues, que les applications Java utilisent par défaut pour vérifier les connexions sécurisées.

Lorsque vous exécutez la commande `keytool -importcert` pour ajouter un nouveau certificat au fichier `cacerts`, vous devez fournir le mot de passe correct pour le keystore. Le message d'erreur que vous voyez—"password verification failed" suivi de `java.security.UnrecoverableException`—indique que le mot de passe que vous avez fourni (ou que vous n'avez pas fourni correctement) ne correspond pas au mot de passe du keystore. Cette exception se produit généralement lorsque le mot de passe fourni est incorrect, empêchant `keytool` d'accéder ou de modifier le keystore.

### La commande en question

La commande que vous utilisez probablement ressemble à ceci :

```
keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
```

- `-file mycert.crt` : Spécifie le fichier de certificat que vous souhaitez importer.
- `-keystore /path/to/jre/lib/security/cacerts` : Pointe vers le keystore `cacerts`.
- `-alias myalias` : Attribue un nom unique (alias) au certificat dans le keystore.

Lorsque vous exécutez cette commande, `keytool` vous invite à saisir le mot de passe du keystore. Si le mot de passe que vous saisissez est incorrect, vous obtenez l'erreur décrite.

### Identifier le mot de passe possible

Pour le fichier `cacerts` dans une installation JRE standard (telle que celles d'Oracle ou OpenJDK), le **mot de passe par défaut** est **"changeit"**. C'est un défaut bien documenté à travers les versions et distributions de Java. Le nom "changeit" sert de rappel que les administrateurs pourraient vouloir le changer pour des raisons de sécurité, mais dans la plupart des installations standard non modifiées, il reste inchangé.

Puisque votre commande échoue avec une erreur de vérification du mot de passe, le problème le plus probable est que soit :
1. Vous n'avez pas saisi "changeit" correctement (par exemple, une faute de frappe ou une casse incorrecte—les mots de passe sont sensibles à la casse).
2. L'invite de mot de passe n'a pas été gérée correctement.
3. Dans votre environnement spécifique, le mot de passe par défaut a été modifié (bien que cela soit moins courant pour `cacerts` sauf modification explicite par un administrateur système).

Étant donné que votre question n'indique pas une configuration personnalisée, supposons une installation JRE standard où "changeit" devrait s'appliquer.

### Comment résoudre le problème

Voici comment vous pouvez résoudre le problème :

1. **Assurer une saisie correcte du mot de passe à l'invite**
   Exécutez à nouveau la commande :

   ```
   keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
   ```

   Lorsque vous êtes invité à saisir le mot de passe, tapez soigneusement **"changeit"** (tout en minuscules, sans espaces) et appuyez sur Entrée. Vérifiez l'absence de fautes de frappe ou de problèmes de disposition de clavier.

2. **Spécifier le mot de passe dans la ligne de commande**
   Pour éviter les problèmes avec l'invite interactive (par exemple, un comportement erroné du terminal ou dans un script), vous pouvez inclure le mot de passe directement en utilisant l'option `-storepass` :

   ```
   keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
   ```

   Cela passe explicitement "changeit" comme mot de passe, contournant l'invite. Si cela fonctionne sans erreur, le problème était probablement lié à la façon dont le mot de passe a été saisi précédemment.

3. **Vérifier les permissions**
   Puisque `cacerts` réside dans le répertoire JRE (par exemple, `/usr/lib/jvm/java-11-openjdk/lib/security/cacerts` sur Linux ou un chemin similaire sur Windows), assurez-vous d'avoir les permissions en écriture. Exécutez la commande avec des privilèges d'administration si nécessaire :
   - Sur Linux/Mac : `sudo keytool ...`
   - Sur Windows : Exécutez l'invite de commandes en tant qu'Administrateur.

   Cependant, puisque votre erreur concerne la vérification du mot de passe, et non l'accès au fichier, ce n'est probablement pas le problème central—mais il est bon de le confirmer.

4. **Vérifier le mot de passe**
   Si "changeit" échoue toujours, le mot de passe a peut-être été modifié dans votre environnement. Pour tester le mot de passe sans modifier le keystore, essayez de lister son contenu :

   ```
   keytool -list -keystore /path/to/jre/lib/security/cacerts
   ```

   Saisissez "changeit" lorsque vous y êtes invité. S'il liste les certificats, le mot de passe est correct. Si vous obtenez la même erreur, le mot de passe est différent du défaut.

### Et si "changeit" n'est pas le mot de passe ?

Si "changeit" ne fonctionne pas, envisagez ces possibilités :
- **Mot de passe personnalisé** : Dans de rares cas, un administrateur système pourrait avoir modifié le mot de passe de `cacerts`. Vous devriez consulter la documentation système ou votre administrateur pour l'obtenir. Il n'y a aucun moyen de récupérer directement un mot de passe de keystore perdu ; s'il est vraiment inconnu, vous devrez peut-être remplacer le fichier `cacerts` par une nouvelle copie provenant d'une nouvelle installation JRE (ce qui le réinitialise à "changeit").
- **Défauts spécifiques à l'environnement** : Certaines distributions Java non standard (par exemple, IBM JDK) pourraient utiliser un défaut différent, mais cela est peu courant, et votre question suggère une configuration typique.

Sans contexte supplémentaire, "changeit" reste le mot de passe le plus probable dans un JRE standard.

### Résolution finale

Pour résoudre votre problème :
- Utilisez cette commande, en supposant un JRE standard :

  ```
  keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
  ```

- Si cela échoue, vérifiez le mot de passe avec la commande `-list` ou vérifiez auprès de votre administrateur système.

Le **mot de passe possible** dans ce scénario, basé sur les conventions Java standard, est **"changeit"**. Cela devrait résoudre le `java.security.UnrecoverableException` s'il est saisi correctement et si le fichier `cacerts` n'a pas été personnalisé.