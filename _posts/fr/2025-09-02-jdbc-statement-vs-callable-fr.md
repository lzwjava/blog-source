---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Instruction vs Instruction Appelable dans JDBC
translated: true
type: note
---

En Java JDBC (et dans d'autres frameworks basés sur celui-ci, comme Hibernate ou Spring), les concepts de **`Statement`** et **`CallableStatement`** sont tous deux des interfaces utilisées pour envoyer des commandes SQL à la base de données, mais ils servent à des fins différentes.

---

### 1. `Statement`

* **Objectif** : Utilisé pour exécuter des requêtes SQL simples sans paramètres.
* **Utilisation** : Vous créez un objet `Statement` à partir d'une `Connection` et vous l'utilisez pour exécuter des chaînes SQL.
* **Méthodes typiques** :

  * `executeQuery(sql)` → pour les requêtes `SELECT`, retourne un `ResultSet`.
  * `executeUpdate(sql)` → pour `INSERT`, `UPDATE`, `DELETE`.
  * `execute(sql)` → générique, retourne `true` si le résultat est un `ResultSet`.

**Exemple** :

```java
Connection conn = DriverManager.getConnection(url, user, pass);
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT id, name FROM employees");

while (rs.next()) {
    System.out.println(rs.getInt("id") + " " + rs.getString("name"));
}
```

* **Quand l'utiliser** : Pour les instructions SQL statiques sans paramètres.
* **Inconvénient** : Peut conduire à des injections SQL s'il est utilisé avec des entrées utilisateur dynamiques.

---

### 2. `CallableStatement`

* **Objectif** : Utilisé pour exécuter les **procédures stockées** dans la base de données.
* **Utilisation** : Créé avec `Connection.prepareCall()` et permet d'appeler des routines de base de données avec des paramètres **IN**, **OUT** et **INOUT**.
* **Méthodes typiques** :

  * `setInt`, `setString`, etc. → pour définir les paramètres d'entrée.
  * `registerOutParameter` → pour enregistrer les paramètres de sortie.
  * `execute()` ou `executeQuery()` → pour exécuter la procédure stockée.
  * `getInt`, `getString`, etc. → pour récupérer les valeurs de sortie.

**Exemple** :

```java
Connection conn = DriverManager.getConnection(url, user, pass);
CallableStatement cstmt = conn.prepareCall("{call getEmployeeName(?, ?)}");

// Définir le paramètre IN
cstmt.setInt(1, 101);

// Enregistrer le paramètre OUT
cstmt.registerOutParameter(2, java.sql.Types.VARCHAR);

// Exécuter
cstmt.execute();

// Récupérer le paramètre OUT
String empName = cstmt.getString(2);
System.out.println("Employee name: " + empName);
```

* **Quand l'utiliser** : Pour les procédures/fonctions stockées qui encapsulent la logique dans la base de données.
* **Avantages** : Prend en charge une logique complexe, des résultats multiples, des paramètres d'entrée/sortie.

---

### Différences Clés (sans tableau)

* `Statement` est pour le **SQL statique** (requêtes ad-hoc).
* `CallableStatement` est pour les **procédures/fonctions stockées**.
* `Statement` exécute le SQL directement, tandis que `CallableStatement` interagit avec des routines de base de données qui peuvent retourner plusieurs jeux de résultats et paramètres.
* `Statement` est simple mais moins sécurisé avec des entrées dynamiques, tandis que `CallableStatement` offre un moyen structuré d'appeler une logique réutilisable stockée dans la base de données.

---

👉 Si vous le souhaitez, je peux également expliquer comment **`PreparedStatement`** se situe entre ces deux interfaces (SQL paramétré plus sûr, mais pas pour les procédures stockées). Souhaitez-vous que je l'ajoute ?