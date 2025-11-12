---
audio: false
generated: true
lang: hi
layout: post
title: डेडलॉक क्रिएशन्स
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

    private static final String DB_URL = "jdbc:sqlite:deadlock_example.db"; // Using SQLite for simplicity
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
                conn.setAutoCommit(false); // Start transaction

                System.out.println(Thread.currentThread().getName() + ": Locking row with id " + id1);
                try (PreparedStatement pstmt1 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt1.setString(1, value1);
                    pstmt1.setInt(2, id1);
                    pstmt1.executeUpdate();
                }
                Thread.sleep(100); // Introduce a small delay

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
                        conn.setAutoCommit(true); // Reset auto-commit
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

**स्पष्टीकरण:**

1.  **डेटाबेस सेटअप:**
    * `DB_URL`: SQLite डेटाबेस फ़ाइल (`deadlock_example.db`) के लिए कनेक्शन URL निर्दिष्ट करता है।
    * `CREATE_TABLE_SQL`, `INSERT_ITEM_SQL`, `UPDATE_ITEM_SQL`: टेबल बनाने, प्रारंभिक डेटा डालने और पंक्तियों को अपडेट करने के लिए SQL स्टेटमेंट को परिभाषित करते हैं।
    * `createTableAndInitialData()`: `items` टेबल बनाता है यदि यह मौजूद नहीं है और आईडी 1 और 2 के साथ दो प्रारंभिक पंक्तियाँ डालता है।

2.  **समवर्ती अपडेट:**
    * `ExecutorService`: 2 कार्यों के समवर्ती निष्पादन को अनुकरण करने के लिए 2 थ्रेड के एक निश्चित पूल के साथ एक `ExecutorService` बनाया जाता है।
    * `UpdateTask`: यह आंतरिक कक्षा `Runnable` इंटरफ़ेस को लागू करती है। `UpdateTask` का प्रत्येक उदाहरण एक लेन-देन का प्रतिनिधित्व करता है जो दो पंक्तियों को अपडेट करने का प्रयास करेगा।
        * कंस्ट्रक्टर अपडेट की जाने वाली दो पंक्तियों के लिए आईडी और नए मान लेता है।
        * `run()` विधि निम्नलिखित कार्य करती है:
            * एक डेटाबेस कनेक्शन स्थापित करता है।
            * एक स्पष्ट लेन-देन शुरू करने के लिए `conn.setAutoCommit(false)` सेट करता है।
            * **पहला अपडेट:** पहली पंक्ति (`id1`) के लिए एक `UPDATE` स्टेटमेंट निष्पादित करता है।
            * `Thread.sleep(100)`: डेडलॉक की संभावना बढ़ाने के लिए एक छोटी देरी पेश करता है। यह दूसरे थ्रेड द्वारा इसे प्राप्त करने का प्रयास करने से पहले पहले थ्रेड को पहली पंक्ति पर लॉक प्राप्त करने की अनुमति देता है।
            * **दूसरा अपडेट:** दूसरी पंक्ति (`id2`) के लिए एक `UPDATE` स्टेटमेंट निष्पादित करता है।
            * `conn.commit()`: लेन-देन को कमिट करने का प्रयास करता है।
            * **त्रुटि प्रबंधन:** `SQLException` को संभालने के लिए एक `try-catch` ब्लॉक शामिल है। यदि कोई अपवाद होता है (जो एक डेडलॉक हो सकता है), तो यह `conn.rollback()` का उपयोग करके लेन-देन को रोल बैक करने का प्रयास करता है।
            * **अंत में ब्लॉक:** यह सुनिश्चित करता है कि कनेक्शन बंद है और `autoCommit` को `true` पर रीसेट कर दिया गया है।

3.  **संघर्षशील क्रम:**
    * `main` विधि में, दो `UpdateTask` उदाहरण एक्सिक्यूटर को सबमिट किए जाते हैं:
        * पहला कार्य पहले पंक्ति 1 और फिर पंक्ति 2 को अपडेट करने का प्रयास करता है।
        * दूसरा कार्य पहले पंक्ति 2 और फिर पंक्ति 1 को अपडेट करने का प्रयास करता है।
    * समान संसाधनों ( `items` टेबल में पंक्तियों) पर लॉक प्राप्त करने का यह संघर्षशील क्रम वह स्थिति है जो डेडलॉक का कारण बन सकती है।

4.  **निष्पादन और आउटपुट:**
    * `executor.shutdown()` और `executor.awaitTermination()`: यह सुनिश्चित करते हैं कि एक्सिक्यूटर दोनों कार्यों के पूरा होने की प्रतीक्षा करता है।
    * `printFinalData()`: थ्रेड्स के समाप्त होने के बाद, यह विधि परिणाम देखने के लिए `items` टेबल की अंतिम सामग्री को प्रिंट करती है।

**कैसे चलाएँ:**

1.  **सेव करें:** कोड को `DeadlockGenerator.java` के रूप में सेव करें।
2.  **कम्पाइल करें:** Java कंपाइलर का उपयोग करके कोड को कम्पाइल करें: `javac DeadlockGenerator.java`
3.  **रन करें:** कम्पाइल किए गए कोड को निष्पादित करें: `java DeadlockGenerator`

**अपेक्षित परिणाम:**

जब आप इस कोड को चलाते हैं, तो आपको इसी तरह का आउटपुट दिखाई देगा (सटीक आउटपुट टाइमिंग और डेटाबेस सिस्टम की डेडलॉक डिटेक्शन के आधार पर थोड़ा भिन्न हो सकता है):

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

या कभी-कभी, Thread-0 को रोल बैक किया जा सकता है। मुख्य अवलोकन यह है कि एक थ्रेड को `SQLException` का सामना करना पड़ेगा जो लॉक संघर्ष या डेडलॉक को इंगित करता है, और उसका लेन-देन रोल बैक हो जाएगा। दूसरा थ्रेड आमतौर पर सफल होगा।

**महत्वपूर्ण नोट्स:**

*   **डेटाबेस सिस्टम:** यह उदाहरण सरलता के लिए SQLite का उपयोग करता है। व्यवहार और त्रुटि संदेश PostgreSQL, MySQL आदि जैसे अन्य डेटाबेस सिस्टम के साथ भिन्न हो सकते हैं। आपको JDBC ड्राइवर URL और संभावित रूप से SQL स्टेटमेंट को समायोजित करने की आवश्यकता हो सकती है।
*   **आइसोलेशन लेवल:** आपके डेटाबेस का डिफ़ॉल्ट लेन-देन आइसोलेशन लेवल डेडलॉक की संभावना को प्रभावित कर सकता है। उच्च आइसोलेशन लेवल डेडलॉक को अधिक बारा कर सकते हैं।
*   **देरी:** डेडलॉक को प्रदर्शित करने के लिए `Thread.sleep()` महत्वपूर्ण है। इसके बिना, एक लेन-देन दूसरे के पहले लॉक प्राप्त करने का मौका मिलने से पहले ही पूरा हो सकता है।
*   **त्रुटि प्रबंधन:** वास्तविक दुनिया के एप्लिकेशन में, आपके पास मजबूत त्रुटि प्रबंधन और संभावित रूप से डेडलॉक के कारण विफल होने वाले लेन-देन के लिए पुनः प्रयास तंत्र होने चाहिए।