---
audio: false
generated: true
lang: fr
layout: post
title: Interblocage de Base de Données
translated: true
type: note
---

Un **interblocage de base de données** se produit lorsque deux transactions ou plus s'attendent mutuellement pour libérer des verrous sur des ressources, créant une dépendance circulaire qui les empêche toutes de progresser. Le système de gestion de base de données (SGBD) détecte généralement cette situation et la résout en annulant l'une des transactions. Voici un exemple détaillé d'un scénario d'interblocage :

---

### Exemple : Interblocage entre deux transactions
- **Scénario** :
  - La transaction T1 met à jour une ligne dans la table `Orders` puis a besoin de mettre à jour une ligne dans la table `Customers`.
  - La transaction T2 met à jour une ligne dans la table `Customers` puis a besoin de mettre à jour une ligne dans la table `Orders`.
  - Les deux transactions verrouillent les ressources dans un ordre différent, conduisant à un interblocage.

- **Étapes détaillées** :
  1. T1 verrouille une ligne dans `Orders`.
  2. T2 verrouille une ligne dans `Customers`.
  3. T1 tente de verrouiller la ligne dans `Customers` (bloqué par T2).
  4. T2 tente de verrouiller la ligne dans `Orders` (bloqué par T1).
  - Résultat : Aucune des deux transactions ne peut progresser, créant un interblocage.

- **Exemple SQL** :
  ```sql
  -- Transaction T1
  BEGIN TRANSACTION;
  UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 100;  -- Verrouille OrderID 100
  -- (un délai ou un traitement)
  UPDATE Customers SET LastOrderDate = '2025-03-27' WHERE CustomerID = 1;  -- Bloqué par T2

  -- Transaction T2
  BEGIN TRANSACTION;
  UPDATE Customers SET Balance = Balance - 50 WHERE CustomerID = 1;  -- Verrouille CustomerID 1
  -- (un délai ou un traitement)
  UPDATE Orders SET PaymentStatus = 'Paid' WHERE OrderID = 100;  -- Bloqué par T1
  ```

- **Ce qui se passe** :
  - T1 détient un verrou exclusif sur `OrderID = 100` et attend `CustomerID = 1`.
  - T2 détient un verrou exclusif sur `CustomerID = 1` et attend `OrderID = 100`.
  - Cette condition d'attente circulaire est un interblocage.
  - Le SGBD détecte cela (par exemple, via un timeout ou un algorithme de détection d'interblocage) et annule une transaction (par exemple, T2), permettant à T1 de se terminer.

---

### Représentation visuelle de l'interblocage
```
T1: Verrouille Orders(100) --> Veut Customers(1)
   |                                ↑
   |                                |
T2: Veut Orders(100)  <-- Verrouille Customers(1)
```

- **Résolution** : Le SGBD pourrait renvoyer une erreur comme :
  ```
  La transaction T2 a été interbloquée sur des ressources de verrou avec un autre processus et a été choisie comme victime de l'interblocage. Relancez la transaction.
  ```

---

### Pourquoi cela arrive
- **Ordre de verrouillage** : T1 et T2 acquièrent les verrous dans une séquence différente (T1: Orders → Customers; T2: Customers → Orders).
- **Concurrence** : Les deux transactions s'exécutent simultanément et ont besoin de ressources qui se chevauchent.
- **Verrous exclusifs** : Les mises à jour nécessitent des verrous exclusifs, qui empêchent les autres transactions d'accéder aux mêmes données.

---

### Comment éviter les interblocages
1. **Ordre de verrouillage cohérent** : Assurez-vous que toutes les transactions acquièrent les verrous dans le même ordre (par exemple, toujours verrouiller `Orders` avant `Customers`).
   ```sql
   -- T1 et T2 doivent toutes deux verrouiller Orders en premier, puis Customers
   ```
2. **Réduire la durée des transactions** : Minimisez les délais dans les transactions pour réduire les risques de chevauchement.
3. **Utiliser des niveaux d'isolation moins stricts** : Si approprié, utilisez un niveau d'isolation moins strict (par exemple, Read Committed) pour réduire la durée des verrous.
4. **Timeouts** : Définissez des timeouts de verrou plus courts pour échouer rapidement et réessayer.

---

Faites-moi savoir si vous souhaitez un exemple plus spécifique (par exemple, avec un SGBD particulier comme PostgreSQL ou SQL Server) ou des clarifications supplémentaires !