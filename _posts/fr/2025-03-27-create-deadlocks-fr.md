---
audio: false
generated: true
lang: fr
layout: post
title: Créations de l'Impasse
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

    private static final String DB_URL = "jdbc:sqlite:deadlock_example.db"; // Utilisation de SQLite pour la simplicité
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
        System.out.println("\nÉtat final de la table:");
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
                conn.setAutoCommit(false); // Début de la transaction

                System.out.println(Thread.currentThread().getName() + ": Verrouillage de la ligne avec id " + id1);
                try (PreparedStatement pstmt1 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt1.setString(1, value1);
                    pstmt1.setInt(2, id1);
                    pstmt1.executeUpdate();
                }
                Thread.sleep(100); // Introduit un petit délai

                System.out.println(Thread.currentThread().getName() + ": Verrouillage de la ligne avec id " + id2);
                try (PreparedStatement pstmt2 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt2.setString(1, value2);
                    pstmt2.setInt(2, id2);
                    pstmt2.executeUpdate();
                }

                conn.commit();
                System.out.println(Thread.currentThread().getName() + ": Transaction validée avec succès.");

            } catch (SQLException e) {
                if (conn != null) {
                    try {
                        conn.rollback();
                        System.err.println(Thread.currentThread().getName() + ": Transaction annulée en raison d'une erreur: " + e.getMessage());
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
                        conn.setAutoCommit(true); // Réinitialise l'auto-commit
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

**Explication :**

1.  **Configuration de la base de données :**
    * `DB_URL` : Spécifie l'URL de connexion pour le fichier de base de données SQLite (`deadlock_example.db`).
    * `CREATE_TABLE_SQL`, `INSERT_ITEM_SQL`, `UPDATE_ITEM_SQL` : Définissent les instructions SQL pour créer la table, insérer les données initiales et mettre à jour les lignes.
    * `createTableAndInitialData()` : Crée la table `items` si elle n'existe pas et insère deux lignes initiales avec les ID 1 et 2.

2.  **Mises à jour concurrentes :**
    * `ExecutorService` : Un `ExecutorService` avec un pool de threads fixe de 2 est créé pour simuler l'exécution concurrente de deux tâches.
    * `UpdateTask` : Cette classe interne implémente l'interface `Runnable`. Chaque instance de `UpdateTask` représente une transaction qui tentera de mettre à jour deux lignes.
        * Le constructeur prend les ID et les nouvelles valeurs pour les deux lignes à mettre à jour.
        * La méthode `run()` effectue les opérations suivantes :
            * Établit une connexion à la base de données.
            * Définit `conn.setAutoCommit(false)` pour démarrer une transaction explicite.
            * **Première mise à jour :** Exécute une instruction `UPDATE` pour la première ligne (`id1`).
            * `Thread.sleep(100)` : Introduit un petit délai pour augmenter la probabilité d'un interblocage. Cela permet au premier thread d'acquérir un verrou sur la première ligne avant que le deuxième thread ne tente de l'acquérir.
            * **Deuxième mise à jour :** Exécute une instruction `UPDATE` pour la deuxième ligne (`id2`).
            * `conn.commit()` : Tente de valider la transaction.
            * **Gestion des erreurs :** Inclut un bloc `try-catch` pour gérer `SQLException`. Si une exception se produit (ce qui pourrait être un interblocage), elle tente d'annuler la transaction en utilisant `conn.rollback()`.
            * **Bloc Finally :** Garantit que la connexion est fermée et que `autoCommit` est réinitialisé à `true`.

3.  **Ordre conflictuel :**
    * Dans la méthode `main`, deux instances de `UpdateTask` sont soumises à l'exécuteur :
        * La première tâche tente de mettre à jour la ligne 1 puis la ligne 2.
        * La deuxième tâche tente de mettre à jour la ligne 2 puis la ligne 1.
    * Cet ordre conflictuel d'acquisition de verrous sur les mêmes ressources (les lignes de la table `items`) est la condition qui peut conduire à un interblocage.

4.  **Exécution et sortie :**
    * `executor.shutdown()` et `executor.awaitTermination()` : Garantissent que l'exécuteur attend que les deux tâches se terminent.
    * `printFinalData()` : Après que les threads ont terminé, cette méthode affiche le contenu final de la table `items` pour observer le résultat.

**Comment exécuter :**

1.  **Sauvegarder :** Sauvegardez le code sous `DeadlockGenerator.java`.
2.  **Compiler :** Compilez le code en utilisant un compilateur Java : `javac DeadlockGenerator.java`
3.  **Exécuter :** Exécutez le code compilé : `java DeadlockGenerator`

**Résultat attendu :**

Lorsque vous exécutez ce code, vous verrez probablement une sortie similaire à ceci (la sortie exacte peut varier légèrement selon le timing et la détection d'interblocage du système de base de données) :

```
Thread-0: Verrouillage de la ligne avec id 1
Thread-1: Verrouillage de la ligne avec id 2
Thread-0: Verrouillage de la ligne avec id 2
Thread-1: Verrouillage de la ligne avec id 1
Thread-1: Transaction annulée en raison d'une erreur: database is locked
Thread-0: Transaction validée avec succès.

État final de la table:
ID: 1, Value: Updated Value 1 - Thread 0
ID: 2, Value: Updated Value 2 - Thread 0
```

Ou parfois, Thread-0 pourrait être annulé à la place. L'observation clé est que l'un des threads rencontrera une `SQLException` indiquant un conflit de verrou ou un interblocage, et sa transaction sera annulée. L'autre thread réussira généralement.

**Notes importantes :**

*   **Système de base de données :** Cet exemple utilise SQLite pour la simplicité. Le comportement et les messages d'erreur peuvent différer avec d'autres systèmes de base de données comme PostgreSQL, MySQL, etc. Vous devrez peut-être ajuster l'URL du pilote JDBC et potentiellement les instructions SQL.
*   **Niveaux d'isolation :** Le niveau d'isolation de transaction par défaut de votre base de données peut influencer la probabilité d'interblocages. Des niveaux d'isolation plus élevés pourraient rendre les interblocages plus fréquents.
*   **Délai :** Le `Thread.sleep()` est crucial pour démontrer l'interblocage. Sans cela, une transaction pourrait se terminer avant que l'autre n'ait eu la chance d'acquérir le premier verrou.
*   **Gestion des erreurs :** Dans une application réelle, vous devriez avoir une gestion robuste des erreurs et potentiellement des mécanismes de nouvelle tentative pour les transactions qui échouent en raison d'interblocages.