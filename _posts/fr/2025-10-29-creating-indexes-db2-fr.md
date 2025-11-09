---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Création d'indexes dans IBM DB2
translated: true
type: note
---

### Création d'index dans IBM DB2

IBM DB2 prend en charge les index pour optimiser les performances des requêtes en permettant une récupération plus rapide des données. Les index peuvent être créés sur une ou plusieurs colonnes d'une table. Ci-dessous, je couvrirai les bases, y compris les index uniques et les index multi-colonnes (composites). Notez que le terme "union index" n'est pas un terme standard dans la documentation DB2 — il pourrait faire référence à un index composite (couvrant plusieurs clés) ou à une incompréhension des opérations UNION dans les requêtes. Si vous pensiez à autre chose, fournissez plus de détails !

#### Création d'index de base
Utilisez l'instruction `CREATE INDEX` pour construire un index simple sur une seule colonne. Cela accélère les recherches, les tris et les jointures sur cette colonne.

**Syntaxe :**
```sql
CREATE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**Exemple :**
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id ASC);
```

- `ASC` trie en ordre croissant (par défaut) ; utilisez `DESC` pour l'ordre décroissant.
- Les index sont non uniques par défaut, autorisant les valeurs en double.

#### Index unique (Application de clés uniques)
Un index unique garantit l'absence de valeurs en double dans la ou les colonnes indexées, similaire à une contrainte unique. DB2 crée automatiquement un index unique lorsque vous définissez une clé primaire ou une contrainte unique.

**Syntaxe :**
```sql
CREATE UNIQUE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**Exemple :**
```sql
CREATE UNIQUE INDEX uidx_email
ON users (email ASC);
```

- Cela empêche l'insertion d'emails en double.
- Pour une unicité partielle (par exemple, ignorer les NULL), ajoutez `WHERE NOT NULL` :  
  ```sql
  CREATE UNIQUE WHERE NOT NULL INDEX uidx_email
  ON users (email ASC);
  ```
- Vous pouvez inclure des colonnes non clés pour la couverture des requêtes :  
  ```sql
  CREATE UNIQUE INDEX uidx_email
  ON users (email ASC) INCLUDE (first_name, last_name);
  ```

#### Index composite (Clés multiples, par exemple, deux colonnes ou plus)
Un index composite (ou multi-colonnes) couvre plusieurs clés, utile pour les requêtes filtrant/jointant sur des combinaisons de colonnes. L'ordre des colonnes est important — placez la colonne la plus sélective en premier.

**Syntaxe :**
```sql
CREATE INDEX index_name
ON table_name (column1 [ASC | DESC], column2 [ASC | DESC], ...);
```

**Exemple (Deux clés) :**
```sql
CREATE INDEX idx_order_date_customer
ON orders (order_date ASC, customer_id DESC);
```

- Cela optimise les requêtes comme `SELECT * FROM orders WHERE order_date > '2023-01-01' AND customer_id = 123;`.
- Pour un composite unique : Ajoutez `UNIQUE` (par exemple, `CREATE UNIQUE INDEX ...`).

#### Conseils supplémentaires
- **Vérifier l'index :** Utilisez `SELECT * FROM SYSCAT.INDEXES WHERE TABSCHEMA = 'VOTRE_SCHEMA' AND TABNAME = 'VOTRE_TABLE';`.
- **Supprimer un index :** `DROP INDEX index_name;`.
- Les index consomment du stockage et ralentissent les insertions/mises à jour — utilisez-les avec discernement.
- Pour les tables partitionnées ou les options avancées (par exemple, le clustering), référez-vous à la documentation DB2.

[Db2 CREATE INDEX Statement](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statements-create-index)  
[Db2 Unique Indexes](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=attributes-unique-indexes)  
[Db2 Composite Indexes Example](https://stackoverflow.com/questions/21597015/composite-index-creation-in-db2)  
[Db2 Unique Index Tutorial](https://www.db2tutorial.com/db2-index/db2-unique-index/)