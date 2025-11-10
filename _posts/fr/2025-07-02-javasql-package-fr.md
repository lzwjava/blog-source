---
audio: false
generated: true
lang: fr
layout: post
title: Java SQL pour la connectivité des bases de données
translated: true
type: note
---

Le package `java.sql` est **une partie fondamentale de l'API JDBC de Java (Java Database Connectivity)**, permettant aux applications Java d'interagir avec des bases de données relationnelles comme MySQL, PostgreSQL, Oracle, SQL Server, et d'autres. Il fournit les interfaces et les classes nécessaires pour **se connecter à une base de données, exécuter des requêtes SQL et récupérer les résultats**.

---

## 📘 **Aperçu de `java.sql`**

Le package `java.sql` inclut des classes et des interfaces pour :

* Se connecter aux bases de données (`DriverManager`, `Connection`)
* Exécuter des requêtes SQL (`Statement`, `PreparedStatement`, `CallableStatement`)
* Traiter les résultats (`ResultSet`)
* Gérer les métadonnées (`DatabaseMetaData`, `ResultSetMetaData`)
* Gérer les transactions
* Gérer les exceptions SQL (`SQLException`)

---

## 🔧 **Configuration : Ce dont vous avez besoin**

### 1. **Pilote JDBC**

* Vous avez besoin d'un pilote JDBC pour votre base de données cible (par exemple, MySQL : `mysql-connector-java`, PostgreSQL : `postgresql`).
* Vous pouvez l'inclure via Maven/Gradle ou ajouter manuellement le fichier `.jar`.

### 2. **URL de la base de données**

Chaque pilote JDBC a un format d'URL de connexion :

```java
jdbc:mysql://localhost:3306/mabase
jdbc:postgresql://localhost:5432/mabase
```

---

## 🧩 **Classes et Interfaces Clés**

### 🔌 1. `DriverManager`

Établit une connexion à une base de données.

```java
Connection conn = DriverManager.getConnection(url, utilisateur, motdepasse);
```

### 🧵 2. `Connection`

Représente une session avec une base de données.

* Créer un `Statement` ou `PreparedStatement`
* Gérer les transactions (commit, rollback)
* Fermer la connexion

```java
Connection conn = DriverManager.getConnection(...);
conn.setAutoCommit(false);  // pour le contrôle manuel des transactions
```

### 📤 3. `Statement` / `PreparedStatement` / `CallableStatement`

#### `Statement`

Utilisé pour exécuter des requêtes SQL statiques.

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM utilisateurs");
```

#### `PreparedStatement`

Utilisé pour exécuter des requêtes paramétrées. Évite l'injection SQL.

```java
PreparedStatement ps = conn.prepareStatement("SELECT * FROM utilisateurs WHERE id = ?");
ps.setInt(1, 101);
ResultSet rs = ps.executeQuery();
```

#### `CallableStatement`

Utilisé pour les procédures stockées.

```java
CallableStatement cs = conn.prepareCall("{call obtenirUtilisateur(?)}");
cs.setInt(1, 5);
ResultSet rs = cs.executeQuery();
```

### 📥 4. `ResultSet`

Contient le résultat d'une requête.

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String nom = rs.getString("nom");
}
```

### 📚 5. Métadonnées

* `DatabaseMetaData` : Informations sur la base de données
* `ResultSetMetaData` : Informations sur les colonnes du résultat

```java
DatabaseMetaData dbMeta = conn.getMetaData();
ResultSetMetaData rsMeta = rs.getMetaData();
```

---

## 🧪 **Exemple de Base**

```java
import java.sql.*;

public class ExempleJdbc {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/basedetest";
        String utilisateur = "root";
        String motdepasse = "motdepasse";

        try (Connection conn = DriverManager.getConnection(url, utilisateur, motdepasse)) {
            String sql = "SELECT * FROM utilisateurs WHERE age > ?";
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setInt(1, 18);

            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " - " + rs.getString("nom"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

---

## 🔁 **Transactions**

```java
conn.setAutoCommit(false);  // Désactiver l'auto-commit

try {
    PreparedStatement ps1 = conn.prepareStatement("UPDATE comptes SET solde = solde - ? WHERE id = ?");
    ps1.setDouble(1, 100.0);
    ps1.setInt(2, 1);
    ps1.executeUpdate();

    PreparedStatement ps2 = conn.prepareStatement("UPDATE comptes SET solde = solde + ? WHERE id = ?");
    ps2.setDouble(1, 100.0);
    ps2.setInt(2, 2);
    ps2.executeUpdate();

    conn.commit(); // Valider la transaction

} catch (SQLException ex) {
    conn.rollback(); // Annuler en cas d'erreur
}
```

---

## ❗ **Gestion des Exceptions**

```java
try {
    // Code base de données
} catch (SQLException ex) {
    System.err.println("Code d'Erreur : " + ex.getErrorCode());
    System.err.println("État SQL : " + ex.getSQLState());
    ex.printStackTrace();
}
```

---

## 🧰 **Fonctionnalités Utiles dans `java.sql`**

| Fonctionnalité              | Interface/Classe                     | Objectif                                      |
| --------------------------- | ----------------------------------- | --------------------------------------------- |
| Métadonnées                 | `DatabaseMetaData`                  | Version de la BD, fonctionnalités, tables, etc. |
| Informations sur les colonnes | `ResultSetMetaData`                 | Nombre, type, libellé des colonnes, etc.       |
| Gestion BLOB/CLOB           | `Blob`, `Clob`                      | Stocker/récupérer des données binaires/texte volumineuses |
| Exécution par Lots          | `addBatch()`, `executeBatch()`      | Exécuter plusieurs instructions ensemble      |
| ResultSet Scrollable        | `ResultSet.TYPE_SCROLL_INSENSITIVE` | Déplacer le curseur avant et arrière          |
| ResultSet Modifiable        | `ResultSet.CONCUR_UPDATABLE`        | Modifier les lignes directement dans le `ResultSet` |

---

## 📦 **Exemple de Dépendance Maven (MySQL)**

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
```

---

## 🧠 **Bonnes Pratiques**

* Fermez toujours `Connection`, `Statement`, `ResultSet` dans un bloc `finally` ou utilisez try-with-resources.
* Utilisez `PreparedStatement` plutôt que `Statement` pour prévenir l'injection SQL.
* Utilisez le pool de connexions en production (via des bibliothèques comme HikariCP, Apache DBCP).
* Utilisez les transactions pour des requêtes multiples liées.
* Ne codez pas le SQL en dur dans la logique métier — envisagez les modèles DAO ou ORM (comme JPA, Hibernate).

---

## 🧮 **Sujets Avancés**

* **RowSet** : Version déconnectée de ResultSet (`javax.sql.rowset`)
* **Pool de Connexions** : Utilisez `DataSource` avec des pools
* **Fonctionnalités JDBC 4+** : Chargement automatique des pilotes, support try-with-resources
* **JDBC + Spring** : Intégration avec Spring JDBC Template
* **JDBC + ORM** : Utilisez `java.sql` sous-jacent à Hibernate, JPA, MyBatis

---

## 🧾 **Tableau Récapitulatif**

| Tâche                  | Classe/Interface                     |
| ---------------------- | ----------------------------------- |
| Connexion à la BD      | `DriverManager`, `Connection`       |
| Exécution SQL          | `Statement`, `PreparedStatement`    |
| Procédures Stockées    | `CallableStatement`                 |
| Lecture des Résultats  | `ResultSet`                         |
| Informations sur la BD | `DatabaseMetaData`                  |
| Informations sur les Colonnes | `ResultSetMetaData`          |
| Transactions           | `Connection.commit()`, `rollback()` |
| Gestion des Exceptions | `SQLException`                      |

---

Si vous le souhaitez, je peux aussi fournir :

* Une anti-sèche
* Une classe wrapper réutilisable de style DAO
* Des exemples avec une vraie base de données (MySQL/PostgreSQL)

Dites-moi !