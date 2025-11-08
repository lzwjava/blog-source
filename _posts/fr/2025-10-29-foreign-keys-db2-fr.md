---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Création de clés étrangères dans Db2
translated: true
type: note
---

### Création de clés étrangères dans IBM Db2

Les clés étrangères dans Db2 appliquent l'intégrité référentielle en reliant une colonne (ou un ensemble de colonnes) d'une table (la table enfant) à la clé primaire ou à une clé unique d'une autre table (la table parent). Cela garantit que les valeurs dans la table enfant correspondent à des valeurs existantes dans la table parent, empêchant ainsi les enregistrements orphelins.

Vous pouvez définir des clés étrangères soit lors de la création de la table en utilisant `CREATE TABLE`, soit en les ajoutant à une table existante en utilisant `ALTER TABLE`. La syntaxe est du SQL standard et fonctionne sur toutes les plateformes Db2 (par exemple, LUW, z/OS).

#### 1. Définition d'une clé étrangère lors de la création de la table (`CREATE TABLE`)
Utilisez la clause `FOREIGN KEY` dans les définitions de colonnes ou à la fin de la définition de la table.

**Syntaxe de base :**
```
CREATE TABLE table_enfant (
    colonne_enfant1 type_donnees,
    colonne_cle_etrangere type_donnees,
    -- Autres colonnes...
    CONSTRAINT nom_contrainte
    FOREIGN KEY (colonne_cle_etrangere) 
    REFERENCES table_parent (colonne_cle_parente)
);
```

**Exemple :**
Supposons que vous ayez une table `departments` avec une clé primaire `dept_id` :
```
CREATE TABLE departments (
    dept_id INTEGER NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

Maintenant, créez une table `employees` avec une clé étrangère référençant `dept_id` :
```
CREATE TABLE employees (
    emp_id INTEGER NOT NULL PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INTEGER,
    CONSTRAINT fk_emp_dept 
    FOREIGN KEY (dept_id) 
    REFERENCES departments (dept_id)
);
```

Ceci crée une clé étrangère nommée `fk_emp_dept` sur `dept_id` dans `employees`.

#### 2. Ajout d'une clé étrangère à une table existante (`ALTER TABLE`)
Utilisez `ALTER TABLE` pour ajouter la contrainte après que la table existe. La clé parent doit déjà exister.

**Syntaxe de base :**
```
ALTER TABLE table_enfant 
ADD CONSTRAINT nom_contrainte 
FOREIGN KEY (colonne_cle_etrangere) 
REFERENCES table_parent (colonne_cle_parente);
```

**Exemple :**
Pour ajouter la même clé étrangère à une table `employees` existante :
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id);
```

#### Options supplémentaires
Vous pouvez spécifier des actions pour ce qui se passe lorsqu'une ligne parent est mise à jour ou supprimée :
- `ON DELETE CASCADE` : Supprime les lignes enfants lorsque le parent est supprimé.
- `ON DELETE SET NULL` : Définit la clé étrangère sur NULL dans les lignes enfants.
- `ON UPDATE CASCADE` : Met à jour les clés enfants lorsque la clé parent change.
- `ON UPDATE SET NULL` : Définit sur NULL lors de la mise à jour de la clé parent.

**Exemple avec options :**
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id)
ON DELETE CASCADE
ON UPDATE RESTRICT;
```

#### Règles et considérations clés
- Les colonnes de la clé étrangère doivent correspondre au type de données et à la longueur des colonnes de la clé parent.
- La table parent doit avoir une clé primaire ou unique définie avant de créer la clé étrangère.
- Les clés étrangères peuvent référencer la même table (auto-référentielles).
- Plusieurs colonnes peuvent former une clé étrangère composite : `FOREIGN KEY (col1, col2) REFERENCES parent (pk1, pk2)`.
- Pour supprimer une clé étrangère : `ALTER TABLE table_enfant DROP CONSTRAINT nom_contrainte;`.
- Il est recommandé de créer un index sur les colonnes de clé étrangère pour les performances.

Testez dans un environnement de développement, car l'ajout de contraintes peut échouer si les données existantes les violent (par exemple, lignes orphelines).

#### Références
- [Foreign key (referential) constraints - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=constraints-foreign-key-referential)
- [CREATE TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-create-table)
- [ALTER TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-alter-table)
- [Adding a foreign key with Db2 - Stack Overflow](https://stackoverflow.com/questions/59370149/adding-a-foreign-key-with-db2-of-ibm)