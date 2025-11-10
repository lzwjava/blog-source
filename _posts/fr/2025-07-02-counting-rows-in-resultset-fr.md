---
audio: false
generated: true
lang: fr
layout: post
title: Décompte des Lignes dans un ResultSet Déroulant
translated: true
type: note
---

En Java, lorsque vous travaillez avec un `ResultSet` (par exemple via `Statement.executeQuery()`), compter les lignes peut être délicat si le `fetchSize` est défini sur `0` (ce qui signifie que le pilote JDBC récupérera les lignes selon les besoins). De plus, l'utilisation d'un jeu de résultats scrollable (en utilisant `ResultSet.TYPE_SCROLL_INSENSITIVE` ou `ResultSet.TYPE_SCROLL_SENSITIVE`) vous permet de naviguer dans le jeu de résultats mais nécessite plus de mémoire car les lignes sont chargées en mémoire.

Voici une stratégie que vous pouvez utiliser pour compter les lignes dans un `ResultSet` sans nécessiter un parcours complet du jeu de résultats. Elle utilise la fonctionnalité `scrollable` du `ResultSet` et la capacité à "aller à la dernière ligne" et "obtenir le numéro de ligne".

### Étapes pour compter les lignes en utilisant un `ResultSet` scrollable :

1. **Créer un ResultSet scrollable** : Assurez-vous d'utiliser un `Statement` qui peut générer des jeux de résultats scrollables en définissant le type de curseur approprié.
2. **Se déplacer vers la dernière ligne** : Le jeu de résultats scrollable vous permet d'aller à la dernière ligne en utilisant `last()`.
3. **Obtenir le numéro de ligne** : Après vous être déplacé vers la dernière ligne, vous pouvez appeler `getRow()` pour déterminer le nombre de lignes.
4. **Optionnel** : Si vous avez besoin de parcourir le jeu de résultats, revenez à la première ligne en utilisant `first()`.

Voici un exemple d'implémentation en Java :

```java
import java.sql.*;

public class RowCountExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/your_database";
        String username = "your_username";
        String password = "your_password";
        
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        try {
            conn = DriverManager.getConnection(url, username, password);
            stmt = conn.createStatement(
                    ResultSet.TYPE_SCROLL_INSENSITIVE, 
                    ResultSet.CONCUR_READ_ONLY);
            rs = stmt.executeQuery("SELECT * FROM your_table");
            
            // Se déplacer vers la dernière ligne pour compter le nombre total de lignes
            if (rs.last()) {
                int rowCount = rs.getRow();
                System.out.println("Total rows: " + rowCount);
                
                // Optionnellement, revenir à la première ligne
                rs.first();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### Points clés :

* **ResultSet scrollable** : Nous créons un `ResultSet` scrollable en utilisant `ResultSet.TYPE_SCROLL_INSENSITIVE`. Ce type de jeu de résultats vous permet de vous déplacer vers la dernière ligne et d'obtenir le nombre de lignes.
* **Nombre de lignes** : La méthode `rs.getRow()` retourne le numéro de ligne courant lorsque le curseur est positionné sur la dernière ligne. Cette valeur correspond effectivement au nombre total de lignes dans le jeu de résultats.
* **Taille de récupération (Fetch Size)** : Si le `fetchSize` est `0`, le pilote récupère les lignes dynamiquement, mais l'utilisation d'un jeu de résultats scrollable nous permet de naviguer efficacement dans les lignes.

### Bonne pratique :

* **Efficacité mémoire** : Bien que les jeux de résultats scrollables soient utiles pour compter les lignes, soyez conscient qu'ils peuvent consommer plus de mémoire, car toutes les lignes doivent être chargées en mémoire. Si vous travaillez avec un grand jeu de données, envisagez d'utiliser une approche différente (comme parcourir le jeu de résultats sans `last()` pour compter les lignes de manière incrémentielle) si l'utilisation de la mémoire est une préoccupation.
* **Approche alternative** : Si la mémoire est un problème et que vous n'avez besoin que du nombre de lignes, vous pouvez exécuter une requête `SELECT COUNT(*)` au lieu de récupérer l'intégralité du jeu de résultats. C'est souvent plus efficace.

```sql
SELECT COUNT(*) FROM your_table;
```

N'hésitez pas à me demander si vous avez besoin de précisions supplémentaires !