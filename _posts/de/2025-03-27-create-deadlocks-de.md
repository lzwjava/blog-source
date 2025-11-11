---
audio: false
generated: true
lang: de
layout: post
title: Deadlock Kreationen
translated: true
type: note
---

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class DeadlockGenerator {

    private static final String DB_URL = "jdbc:sqlite:deadlock_example.db"; // Verwendung von SQLite für Einfachheit
    private static final String CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value TEXT)";
    private static final String INSERT_ITEM_SQL = "INSERT OR IGNORE INTO items (id, value) VALUES (?, ?)";
    private static final String UPDATE_ITEM_SQL = "UPDATE items SET value = ? WHERE id = ?";

    public static void main(String[] args) throws InterruptedException {
        createTableAndInitialData();

        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.submit(new UpdateTask(1, "Updated Value 1 - Thread 1", 2, "Updated Value 2 - Thread 1"));
        executor.submit(new UpdateTask(2, "Updated Value 2 - Thread 2", 1, "Updated Value 1 - Thread 2"));

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);

        printFinalData();
    }

    private static void createTableAndInitialData() {
        try (Connection conn = DriverManager.getConnection(DB_URL);
             java.sql.Statement stmt = conn.createStatement()) {
            stmt.execute(CREATE_TABLE_SQL);
            try (PreparedStatement pstmt = conn.prepareStatement(INSERT_ITEM_SQL)) {
                pstmt.setInt(1, 1);
                pstmt.setString(2, "Value 1");
                pstmt.executeUpdate();
                pstmt.setInt(1, 2);
                pstmt.setString(2, "Value 2");
                pstmt.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void printFinalData() {
        System.out.println("\nFinal state of the table:");
        try (Connection conn = DriverManager.getConnection(DB_URL);
             java.sql.Statement stmt = conn.createStatement();
             java.sql.ResultSet rs = stmt.executeQuery("SELECT * FROM items")) {
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") + ", Value: " + rs.getString("value"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    static class UpdateTask implements Runnable {
        private final int id1;
        private final String value1;
        private final int id2;
        private final String value2;

        public UpdateTask(int id1, String value1, int id2, String value2) {
            this.id1 = id1;
            this.value1 = value1;
            this.id2 = id2;
            this.value2 = value2;
        }

        @Override
        public void run() {
            Connection conn = null;
            try {
                conn = DriverManager.getConnection(DB_URL);
                conn.setAutoCommit(false); // Transaktion starten

                System.out.println(Thread.currentThread().getName() + ": Locking row with id " + id1);
                try (PreparedStatement pstmt1 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt1.setString(1, value1);
                    pstmt1.setInt(2, id1);
                    pstmt1.executeUpdate();
                }
                Thread.sleep(100); // Kurze Verzögerung einfügen

                System.out.println(Thread.currentThread().getName() + ": Locking row with id " + id2);
                try (PreparedStatement pstmt2 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt2.setString(1, value2);
                    pstmt2.setInt(2, id2);
                    pstmt2.executeUpdate();
                }

                conn.commit();
                System.out.println(Thread.currentThread().getName() + ": Transaction committed successfully.");

            } catch (SQLException e) {
                if (conn != null) {
                    try {
                        conn.rollback();
                        System.err.println(Thread.currentThread().getName() + ": Transaction rolled back due to error: " + e.getMessage());
                    } catch (SQLException rollbackException) {
                        rollbackException.printStackTrace();
                    }
                } else {
                    e.printStackTrace();
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                if (conn != null) {
                    try {
                        conn.setAutoCommit(true); // Auto-Commit zurücksetzen
                        conn.close();
                    } catch (SQLException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}
```

**Erklärung:**

1.  **Datenbank-Einrichtung:**
    * `DB_URL`: Gibt die Verbindungs-URL für die SQLite-Datenbankdatei (`deadlock_example.db`) an.
    * `CREATE_TABLE_SQL`, `INSERT_ITEM_SQL`, `UPDATE_ITEM_SQL`: Definieren die SQL-Anweisungen zum Erstellen der Tabelle, Einfügen von Initialdaten und Aktualisieren von Zeilen.
    * `createTableAndInitialData()`: Erstellt die Tabelle `items`, falls sie nicht existiert, und fügt zwei initiale Zeilen mit den IDs 1 und 2 ein.

2.  **Parallele Aktualisierungen:**
    * `ExecutorService`: Ein `ExecutorService` mit einem festen Thread-Pool von 2 wird erstellt, um die parallele Ausführung von zwei Tasks zu simulieren.
    * `UpdateTask`: Diese innere Klasse implementiert das `Runnable`-Interface. Jede Instanz von `UpdateTask` stellt eine Transaktion dar, die versucht, zwei Zeilen zu aktualisieren.
        * Der Konstruktor nimmt die IDs und die neuen Werte für die beiden zu aktualisierenden Zeilen entgegen.
        * Die `run()`-Methode führt folgende Schritte aus:
            * Stellt eine Datenbankverbindung her.
            * Setzt `conn.setAutoCommit(false)`, um eine explizite Transaktion zu starten.
            * **Erste Aktualisierung:** Führt eine `UPDATE`-Anweisung für die erste Zeile (`id1`) aus.
            * `Thread.sleep(100)`: Fügt eine kurze Verzögerung ein, um die Wahrscheinlichkeit eines Deadlocks zu erhöhen. Dies ermöglicht es dem ersten Thread, eine Sperre für die erste Zeile zu erlangen, bevor der zweite Thread versucht, diese zu erlangen.
            * **Zweite Aktualisierung:** Führt eine `UPDATE`-Anweisung für die zweite Zeile (`id2`) aus.
            * `conn.commit()`: Versucht, die Transaktion zu committen.
            * **Fehlerbehandlung:** Enthält einen `try-catch`-Block zur Behandlung von `SQLException`. Wenn eine Exception auftritt (was ein Deadlock sein könnte), wird versucht, die Transaktion mit `conn.rollback()` zurückzurollen.
            * **Finally-Block:** Stellt sicher, dass die Verbindung geschlossen und `autoCommit` auf `true` zurückgesetzt wird.

3.  **Konfligierende Reihenfolge:**
    * In der `main`-Methode werden zwei `UpdateTask`-Instanzen an den Executor übergeben:
        * Der erste Task versucht, Zeile 1 und dann Zeile 2 zu aktualisieren.
        * Der zweite Task versucht, Zeile 2 und dann Zeile 1 zu aktualisieren.
    * Diese konfligierende Reihenfolge beim Erlangen von Sperren auf denselben Ressourcen (die Zeilen in der Tabelle `items`) ist die Bedingung, die zu einem Deadlock führen kann.

4.  **Ausführung und Ausgabe:**
    * `executor.shutdown()` und `executor.awaitTermination()`: Stellen sicher, dass der Executor wartet, bis beide Tasks abgeschlossen sind.
    * `printFinalData()`: Nachdem die Threads beendet sind, gibt diese Methode den endgültigen Inhalt der Tabelle `items` aus, um das Ergebnis zu beobachten.

**Ausführung:**

1.  **Speichern:** Speichern Sie den Code als `DeadlockGenerator.java`.
2.  **Kompilieren:** Kompilieren Sie den Code mit einem Java-Compiler: `javac DeadlockGenerator.java`
3.  **Ausführen:** Führen Sie den kompilierten Code aus: `java DeadlockGenerator`

**Erwartetes Ergebnis:**

Wenn Sie diesen Code ausführen, werden Sie wahrscheinlich eine Ausgabe ähnlich dieser sehen (die genaue Ausgabe kann je nach Timing und der Deadlock-Erkennung des Datenbanksystems leicht variieren):

```
Thread-0: Locking row with id 1
Thread-1: Locking row with id 2
Thread-0: Locking row with id 2
Thread-1: Locking row with id 1
Thread-1: Transaction rolled back due to error: database is locked
Thread-0: Transaction committed successfully.

Final state of the table:
ID: 1, Value: Updated Value 1 - Thread 0
ID: 2, Value: Updated Value 2 - Thread 0
```

Oder manchmal wird Thread-0 zurückgerollt. Die wichtige Beobachtung ist, dass einer der Threads auf eine `SQLException` stoßen wird, die auf einen Sperrkonflikt oder Deadlock hinweist, und seine Transaktion wird zurückgerollt. Der andere Thread wird in der Regel erfolgreich sein.

**Wichtige Hinweise:**

*   **Datenbanksystem:** Dieses Beispiel verwendet SQLite der Einfachheit halber. Das Verhalten und die Fehlermeldungen können sich bei anderen Datenbanksystemen wie PostgreSQL, MySQL etc. unterscheiden. Möglicherweise müssen Sie die JDBC-Treiber-URL und potenziell die SQL-Anweisungen anpassen.
*   **Isolationslevel:** Das standardmäßige Transaktionsisolationslevel Ihrer Datenbank kann die Wahrscheinlichkeit von Deadlocks beeinflussen. Höhere Isolationslevel können Deadlocks häufiger auftreten lassen.
*   **Verzögerung:** Der `Thread.sleep()`-Aufruf ist entscheidend für die Demonstration des Deadlocks. Ohne ihn könnte eine Transaktion abgeschlossen sein, bevor die andere eine Chance hat, die erste Sperre zu erlangen.
*   **Fehlerbehandlung:** In einer realen Anwendung sollten Sie eine robuste Fehlerbehandlung und möglicherweise Wiederholungsmechanismen für Transaktionen haben, die aufgrund von Deadlocks fehlschlagen.