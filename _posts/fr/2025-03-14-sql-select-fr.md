---
audio: false
generated: true
lang: fr
layout: post
title: Instructions de sélection SQL
translated: true
type: note
---

Pour répondre à votre question sur l'utilisation de `SELECT`, `LEFT JOIN`, `RIGHT JOIN`, des `SELECT` complexes, `FROM`, `GROUP BY`, `WHERE NOT IN` et `IN` en SQL, je vais expliquer chaque composant clairement et fournir des exemples pratiques. Ce sont des opérations SQL fondamentales utilisées pour récupérer et manipuler des données dans les bases de données. Décomposons-les étape par étape, en utilisant un schéma de base de données simple pour la cohérence :

- **Tables :**
  - `employees` (colonnes : `employee_id`, `employee_name`, `department_id`, `salary`)
  - `departments` (colonnes : `department_id`, `department_name`)
  - `projects` (colonnes : `project_id`, `project_name`, `employee_id`)

---

### 1. SELECT
La clause `SELECT` est utilisée pour spécifier les colonnes que vous souhaitez récupérer d'une table de base de données. Elle constitue la base de toute requête SQL.

- **Objectif :** Choisir les données à afficher.
- **Exemple :**
  ```sql
  SELECT employee_name, salary
  FROM employees;
  ```
  Cela récupère les colonnes `employee_name` et `salary` de la table `employees`.

---

### 2. FROM
La clause `FROM` identifie la table (ou les tables) à partir de laquelle extraire les données. Elle est toujours utilisée avec `SELECT`.

- **Objectif :** Spécifier la source des données.
- **Exemple :**
  ```sql
  SELECT employee_name
  FROM employees;
  ```
  Ici, `employees` est la table interrogée.

---

### 3. LEFT JOIN
Un `LEFT JOIN` (ou `LEFT OUTER JOIN`) combine les lignes de deux tables. Il renvoie tous les enregistrements de la table de gauche et les enregistrements correspondants de la table de droite. S'il n'y a pas de correspondance, le résultat inclut des valeurs `NULL` pour les colonnes de la table de droite.

- **Objectif :** Inclure toutes les lignes de la table de gauche, indépendamment des correspondances dans la table de droite.
- **Exemple :**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  Cela liste tous les employés et leurs noms de département. Si un employé n'est pas assigné à un département, `department_name` sera `NULL`.

---

### 4. RIGHT JOIN
Un `RIGHT JOIN` (ou `RIGHT OUTER JOIN`) est similaire à un `LEFT JOIN`, mais il renvoie tous les enregistrements de la table de droite et les enregistrements correspondants de la table de gauche. Les lignes de la table de gauche sans correspondance entraînent des valeurs `NULL`.

- **Objectif :** Inclure toutes les lignes de la table de droite, indépendamment des correspondances dans la table de gauche.
- **Exemple :**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  RIGHT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  Cela montre tous les départements et leurs employés. Les départements sans employés auront `NULL` dans `employee_name`.

---

### 5. SELECT complexe
Un "`SELECT` complexe" n'est pas un terme SQL formel mais fait généralement référence à une instruction `SELECT` qui combine plusieurs clauses, jointures, sous-requêtes ou fonctions d'agrégation pour effectuer une récupération de données avancée.

- **Objectif :** Gérer des requêtes complexes impliquant plusieurs opérations.
- **Exemple :**
  ```sql
  SELECT d.department_name, COUNT(e.employee_id) AS employee_count
  FROM departments d
  LEFT JOIN employees e
  ON d.department_id = e.department_id
  GROUP BY d.department_name
  HAVING COUNT(e.employee_id) > 5;
  ```
  Cela trouve les départements ayant plus de 5 employés, en comptant les employés par département et en filtrant les résultats.

---

### 6. GROUP BY
La clause `GROUP BY` regroupe les lignes qui ont les mêmes valeurs dans des colonnes spécifiées en lignes de synthèse, souvent utilisée avec des fonctions d'agrégation comme `COUNT`, `SUM` ou `AVG`.

- **Objectif :** Agréger les données en fonction des valeurs des colonnes.
- **Exemple :**
  ```sql
  SELECT department_id, COUNT(employee_id) AS employee_count
  FROM employees
  GROUP BY department_id;
  ```
  Cela compte le nombre d'employés dans chaque département.

---

### 7. WHERE NOT IN
La clause `WHERE NOT IN` filtre les lignes où la valeur d'une colonne n'est pas présente dans une liste spécifiée ou le résultat d'une sous-requête. Soyez prudent : si la liste/la sous-requête inclut `NULL`, aucune ligne peut être renvoyée.

- **Objectif :** Exclure des lignes basées sur un ensemble de valeurs.
- **Exemple :**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (1, 2);
  ```
  Cela récupère les employés qui ne sont pas dans les départements 1 ou 2.

- **Avec une sous-requête :**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (SELECT department_id FROM departments WHERE department_name = 'Inactive');
  ```
  Cela trouve les employés qui ne sont pas dans les départements marqués comme 'Inactive'.

---

### 8. IN
La clause `IN` filtre les lignes où la valeur d'une colonne correspond à n'importe quelle valeur d'une liste ou d'une sous-requête. C'est un raccourci pour plusieurs conditions `OR`.

- **Objectif :** Inclure des lignes basées sur un ensemble de valeurs.
- **Exemple :**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (3, 4);
  ```
  Cela récupère les employés des départements 3 ou 4.

- **Avec une sous-requête :**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (
      SELECT department_id
      FROM employees
      GROUP BY department_id
      HAVING COUNT(employee_id) > 5
  );
  ```
  Cela trouve les employés dans les départements ayant plus de 5 employés.

---

### Tout mettre ensemble
Voici un exemple combinant plusieurs de ces opérations :
```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id NOT IN (1, 2)
GROUP BY d.department_name;
```
- **Explication :**
  - `FROM departments d` : Commence avec la table `departments`.
  - `LEFT JOIN employees e` : Inclut tous les départements, même ceux sans employés.
  - `WHERE NOT IN (1, 2)` : Exclut les employés des départements 1 et 2.
  - `GROUP BY d.department_name` : Regroupe les résultats par nom de département.
  - `SELECT ... COUNT` : Compte les employés par département.

---

### Conseils clés
- **Jointures :** Choisissez `LEFT JOIN` ou `RIGHT JOIN` en fonction de la table dont vous voulez conserver toutes les lignes (gauche ou droite).
- **NULL avec NOT IN :** Si une sous-requête renvoie `NULL`, `NOT IN` peut exclure toutes les lignes de manière inattendue. Envisagez `NOT EXISTS` comme alternative.
- **Requêtes complexes :** Décomposez-les en parties (par exemple, testez les jointures séparément) pour garantir l'exactitude.
- **L'ordre est important :** Placez `WHERE` avant `GROUP BY`, et utilisez `HAVING` après `GROUP BY` pour les filtres au niveau du groupe.

En comprenant et en combinant ces composants SQL—`SELECT`, `FROM`, `LEFT JOIN`, `RIGHT JOIN`, `GROUP BY`, `WHERE NOT IN` et `IN`—vous pouvez concevoir des requêtes pour récupérer et analyser efficacement les données de toute base de données relationnelle.