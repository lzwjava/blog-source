---
audio: false
generated: true
lang: fr
layout: post
title: Solution pour Corriger DBeaver qui ne Charge pas les Schémas
translated: true
type: note
---

Si vous pouvez visualiser les schémas dans une base de données IBM DB2 en utilisant Squirrel SQL sur Windows, mais que DBeaver reste bloqué sur « chargement de l'élément 0 % », le problème provient probablement de la manière dont DBeaver récupère les métadonnées par rapport à Squirrel SQL. Voici un guide étape par étape pour diagnostiquer et résoudre ce problème :

---

#### 1. Vérifier le pilote DB2 dans DBeaver
DBeaver nécessite le pilote correct pour se connecter à votre base de données IBM DB2. L'utilisation d'un mauvais pilote (par exemple, "Db2 for LUW" vs "Db2 for z/OS") peut entraîner des problèmes de chargement des schémas.

- **Étapes** :
  1. Ouvrez DBeaver et faites un clic droit sur votre connexion DB2 dans le Navigateur de bases de données.
  2. Sélectionnez **Modifier la connexion**.
  3. Dans la section "Pilote", confirmez que le pilote sélectionné correspond à votre environnement DB2 (par exemple, "Db2 for LUW" pour Linux/Unix/Windows ou "Db2 for z/OS" pour mainframe).
  4. En cas de doute, consultez votre administrateur de base de données ou la documentation pour vous assurer que le pilote correct est sélectionné.
  5. Cliquez sur **Tester la connexion** pour vérifier son bon fonctionnement.

---

#### 2. Ajuster la propriété "Source des métadonnées"
DBeaver utilise une propriété appelée "source des métadonnées" pour contrôler la manière dont il récupère les informations des schémas et des tables. Pour DB2, l'ajustement de ce paramètre peut résoudre les problèmes de chargement des schémas.

- **Étapes** :
  1. Ouvrez les paramètres de votre connexion DB2 dans DBeaver (clic droit sur la connexion > **Modifier la connexion**).
  2. Allez dans l'onglet **Propriétés du pilote**.
  3. Trouvez la propriété "metadata source" (ou ajoutez-la si elle n'est pas listée).
  4. Définissez sa valeur sur `0`.
  5. Cliquez sur **OK** pour enregistrer les modifications.
  6. Reconnectez-vous à la base de données et vérifiez si les schémas se chargent.

- **Pourquoi cela fonctionne** : Définir "metadata source" sur `0` simplifie la façon dont DBeaver récupère les métadonnées, ce qui peut contourner les problèmes spécifiques à la récupération des schémas DB2.

---

#### 3. Vérifier les permissions de l'utilisateur
Bien que Squirrel SQL affiche les schémas, DBeaver peut interroger la base de données différemment, nécessitant des permissions spécifiques pour accéder aux métadonnées.

- **Étapes** :
  1. Confirmez auprès de votre administrateur de base de données que votre compte utilisateur a les privilèges nécessaires pour visualiser les schémas et les métadonnées dans DB2 (par exemple, `SELECT` sur les tables du catalogue système comme `SYSCAT.SCHEMATA`).
  2. Si les permissions sont insuffisantes, demandez à votre DBA d'accorder les droits nécessaires.
  3. Testez à nouveau la connexion dans DBeaver.

---

#### 4. Éliminer les problèmes de réseau ou de pare-feu
Une restriction réseau ou un pare-feu pourrait empêcher DBeaver de récupérer complètement les données du schéma, même si Squirrel SQL fonctionne.

- **Étapes** :
  1. Assurez-vous que le serveur DB2 est accessible depuis votre machine Windows (par exemple, pingez le serveur ou testez le port).
  2. Vérifiez avec votre équipe réseau qu'aucune règle de pare-feu ne bloque la connexion de DBeaver.
  3. Si possible, testez DBeaver depuis une autre machine pour isoler le problème.

---

#### 5. Mettre à jour DBeaver vers la dernière version
Les anciennes versions de DBeaver peuvent contenir des boges affectant le chargement des schémas DB2.

- **Étapes** :
  1. Dans DBeaver, allez dans **Aide** > **Vérifier les mises à jour**.
  2. Installez toutes les mises à jour disponibles.
  3. Redémarrez DBeaver et reconnectez-vous à la base de données.

- **Alternative** : Téléchargez la dernière version depuis le [site web de DBeaver](https://dbeaver.io/) et réinstallez si aucune mise à jour n'est disponible.

---

#### 6. Activer la journalisation de débogage pour un diagnostic approfondi
Si les étapes ci-dessus ne résolvent pas le problème, activez la journalisation de débogage pour identifier les erreurs spécifiques lors du chargement des schémas.

- **Étapes** :
  1. Allez dans **Fenêtre** > **Préférences** > **DBeaver** > **Journalisation**.
  2. Activez la journalisation détaillée et enregistrez les paramètres.
  3. Reconnectez-vous à la base de données et tentez de charger les schémas.
  4. Vérifiez les fichiers journaux (généralement dans le dossier workspace de DBeaver) pour les messages d'erreur liés à la récupération des schémas DB2.
  5. Si nécessaire, partagez les journaux avec le support DBeaver ou un forum pour une assistance supplémentaire.

---

### Pourquoi cela se produit
- **DBeaver vs. Squirrel SQL** : DBeaver est un outil plus riche en fonctionnalités et récupère des métadonnées supplémentaires par rapport à l'approche plus simple de Squirrel SQL. Cela peut entraîner des problèmes de compatibilité avec DB2 si les paramètres ne sont pas optimisés.
- **Solution courante** : Ajuster "metadata source" à `0` est une solution de contournement connue pour les problèmes de chargement des schémas DB2 dans DBeaver.

---

### Prochaines étapes
Commencez par les étapes 1 et 2 (vérification du pilote et ajustement de la source des métadonnées), car ce sont les correctifs les plus probables. Si le problème persiste, poursuivez avec les étapes restantes. Si aucune ne fonctionne, envisagez de publier vos journaux de débogage dans la [communauté DBeaver](https://github.com/dbeaver/dbeaver/issues) pour une aide supplémentaire.

Cela devrait résoudre le problème de « chargement de l'élément 0 % » et vous permettre de visualiser les schémas dans DBeaver comme vous le faites dans Squirrel SQL !