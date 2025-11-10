---
audio: false
generated: true
lang: de
layout: post
title: Zählen von Zeilen in Scrollable ResultSet
translated: true
type: note
---

In Java kann das Zählen der Zeilen in einem `ResultSet` (z.B. über `Statement.executeQuery()`) knifflig sein, wenn `fetchSize` auf `0` gesetzt ist (was bedeutet, dass der JDBC-Treiber Zeilen nach Bedarf abruft). Darüber hinaus ermöglicht die Verwendung eines scrollbaren Result Sets (mit `ResultSet.TYPE_SCROLL_INSENSITIVE` oder `ResultSet.TYPE_SCROLL_SENSITIVE`) die Navigation durch das Result Set, erfordert jedoch mehr Speicher, da die Zeilen in den Arbeitsspeicher geladen werden.

Hier ist eine Strategie, die Sie verwenden können, um Zeilen in einem `ResultSet` zu zählen, ohne das gesamte Result Set durchlaufen zu müssen. Sie nutzt die `scrollable`-Funktion des `ResultSet` und die Möglichkeit, "zur letzten Zeile zu springen" und "die Zeilennummer abzurufen".

### Schritte zum Zählen von Zeilen mit einem scrollbaren `ResultSet`:

1. **Erstellen eines scrollbaren ResultSet**: Stellen Sie sicher, dass Sie ein `Statement` verwenden, das scrollbare Result Sets erzeugen kann, indem Sie den entsprechenden Cursor-Typ setzen.
2. **Zur letzten Zeile springen**: Das scrollbare Result Set ermöglicht es Ihnen, mit `last()` zur letzten Zeile zu springen.
3. **Zeilennummer abrufen**: Nachdem Sie zur letzten Zeile gesprungen sind, können Sie `getRow()` aufrufen, um die Anzahl der Zeilen zu bestimmen.
4. **Optional**: Wenn Sie durch das Result Set iterieren müssen, springen Sie mit `first()` zurück zur ersten Zeile.

Hier ist eine Beispielimplementierung in Java:

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
            
            // Zur letzten Zeile springen, um die Gesamtzahl der Zeilen zu zählen
            if (rs.last()) {
                int rowCount = rs.getRow();
                System.out.println("Total rows: " + rowCount);
                
                // Optional zurück zur ersten Zeile springen
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

### Wichtige Punkte:

* **Scrollbares ResultSet**: Wir erstellen ein scrollbares `ResultSet` mit `ResultSet.TYPE_SCROLL_INSENSITIVE`. Diese Art von Result Set ermöglicht es Ihnen, zur letzten Zeile zu springen und die Zeilenanzahl abzurufen.
* **Zeilenzählung**: Die Methode `rs.getRow()` gibt die aktuelle Zeilennummer zurück, wenn der Cursor auf der letzten Zeile positioniert ist. Dieser Wert entspricht effektiv der Gesamtzahl der Zeilen im Result Set.
* **Fetch Size**: Wenn `fetchSize` `0` ist, ruft der Treiber Zeilen dynamisch ab, aber die Verwendung eines scrollbaren Result Sets ermöglicht uns eine effiziente Navigation durch die Zeilen.

### Best Practice:

* **Speichereffizienz**: Während scrollbare Result Sets nützlich zum Zählen von Zeilen sind, sollten Sie beachten, dass sie mehr Speicher verbrauchen können, da alle Zeilen in den Arbeitsspeicher geladen werden müssen. Wenn Sie mit einem großen Datensatz arbeiten und der Speicherverbrauch ein Problem darstellt, erwägen Sie einen anderen Ansatz (wie das inkrementelle Zählen der Zeilen durch Iterieren über das Result Set ohne `last()`).
* **Alternativer Ansatz**: Wenn Speicher ein Problem darstellt und Sie nur die Zeilenanzahl benötigen, können Sie stattdessen eine `SELECT COUNT(*)`-Abfrage ausführen. Dies ist oft effizienter.

```sql
SELECT COUNT(*) FROM your_table;
```

Lassen Sie mich wissen, wenn Sie weitere Erklärungen benötigen!