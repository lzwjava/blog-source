---
audio: false
generated: true
lang: fr
layout: post
title: Blocage de base de données
translated: true
type: note
---

Je suppose que vous demandez des exemples de blocage de base de données dans le contexte des systèmes de gestion de base de données (SGBD). Le blocage se produit lorsqu'une transaction dans une base de données empêche une autre transaction de progresser parce qu'elles tentent d'accéder ou de modifier les mêmes données simultanément. Ceci est généralement géré à l'aide de verrous pour assurer la cohérence et l'intégrité des données. Voici quelques exemples de scénarios de blocage de base de données :

---

### Exemple 1 : Blocage Lecture-Écriture
- **Scénario** : La transaction T1 met à jour une ligne dans une table (par exemple, en modifiant le solde d'un client), et la transaction T2 tente de lire cette même ligne.
- **Ce qui se passe** : T1 acquiert un verrou exclusif sur la ligne pour empêcher d'autres transactions de la lire ou de la modifier jusqu'à ce que la mise à jour soit terminée. T2 est bloquée et doit attendre que T1 valide ou annule.
- **Exemple SQL** :
  ```sql
  -- Transaction T1
  BEGIN TRANSACTION;
  UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;

  -- Transaction T2 (bloquée)
  SELECT Balance FROM Accounts WHERE AccountID = 1;
  ```
  T2 attend que T1 se termine à cause du verrou exclusif sur la ligne.

---

### Exemple 2 : Blocage Écriture-Écriture
- **Scénario** : La transaction T1 met à jour la quantité en stock d'un produit, et la transaction T2 tente de mettre à jour le stock du même produit en même temps.
- **Ce qui se passe** : T1 détient un verrou exclusif sur la ligne, et T2 est bloquée jusqu'à ce que T1 se termine. Cela empêche des mises à jour conflictuelles qui pourraient entraîner une incohérence des données.
- **Exemple SQL** :
  ```sql
  -- Transaction T1
  BEGIN TRANSACTION;
  UPDATE Products SET Stock = Stock - 5 WHERE ProductID = 100;

  -- Transaction T2 (bloquée)
  UPDATE Products SET Stock = Stock + 10 WHERE ProductID = 100;
  ```
  T2 est bloquée jusqu'à ce que T1 valide ou annule.

---

### Exemple 3 : Interblocage (Blocage menant à une impasse)
- **Scénario** : La transaction T1 verrouille la Ligne A et a besoin de mettre à jour la Ligne B, tandis que la transaction T2 verrouille la Ligne B et a besoin de mettre à jour la Ligne A.
- **Ce qui se passe** : T1 est bloquée par le verrou de T2 sur la Ligne B, et T2 est bloquée par le verrou de T1 sur la Ligne A. Cela crée un interblocage, et le SGBD doit intervenir (par exemple, en annulant une transaction).
- **Exemple SQL** :
  ```sql
  -- Transaction T1
  BEGIN TRANSACTION;
  UPDATE Table1 SET Value = 10 WHERE ID = 1;  -- Verrouille la Ligne A
  UPDATE Table2 SET Value = 20 WHERE ID = 2;  -- Bloquée par T2

  -- Transaction T2
  BEGIN TRANSACTION;
  UPDATE Table2 SET Value = 30 WHERE ID = 2;  -- Verrouille la Ligne B
  UPDATE Table1 SET Value = 40 WHERE ID = 1;  -- Bloquée par T1
  ```
  Aucune transaction ne peut progresser jusqu'à ce que le SGBD résolve l'interblocage.

---

### Exemple 4 : Blocage au niveau de la table
- **Scénario** : La transaction T1 effectue une mise à jour importante sur une table entière sans indexation appropriée, et la transaction T2 tente de lire une seule ligne de la même table.
- **Ce qui se passe** : T1 pourrait escalader ses verrous au niveau des lignes vers un verrou au niveau de la table, bloquant T2 même pour la lecture de lignes non concernées jusqu'à ce que T1 se termine.
- **Exemple SQL** :
  ```sql
  -- Transaction T1
  BEGIN TRANSACTION;
  UPDATE Employees SET Salary = Salary * 1.1;  -- Verrouille la table entière

  -- Transaction T2 (bloquée)
  SELECT Name FROM Employees WHERE EmployeeID = 5;
  ```
  T2 est bloquée parce que T1 a un verrou exclusif au niveau de la table.

---

### Gestion du blocage
- **Verrous** : Les bases de données utilisent des verrous partagés (pour la lecture) et des verrous exclusifs (pour l'écriture) pour contrôler l'accès.
- **Niveaux d'isolement** : Des niveaux d'isolement plus élevés (par exemple, Sérialisable) augmentent le blocage pour garantir la cohérence, tandis que des niveaux plus bas (par exemple, Read Uncommitted) réduisent le blocage mais risquent des lectures sales.
- **Timeouts** : Les transactions peuvent expirer si elles sont bloquées trop longtemps, forçant une annulation.
- **Détection des interblocages** : Le SGBD détecte et résout les interblocages en terminant une transaction.

N'hésitez pas à me demander plus de détails ou des exemples spécifiques à un système de base de données particulier (par exemple, MySQL, PostgreSQL, SQL Server) !