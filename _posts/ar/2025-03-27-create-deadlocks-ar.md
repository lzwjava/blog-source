---
audio: false
generated: true
lang: ar
layout: post
title: إبداعات الجمود
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

    private static final String DB_URL = "jdbc:sqlite:deadlock_example.db"; // استخدام SQLite للتبسيط
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
        System.out.println("\nالحالة النهائية للجدول:");
        try (Connection conn = DriverManager.getConnection(DB_URL);
             java.sql.Statement stmt = conn.createStatement();
             java.sql.ResultSet rs = stmt.executeQuery("SELECT * FROM items")) {
            while (rs.next()) {
                System.out.println("المعرف: " + rs.getInt("id") + ", القيمة: " + rs.getString("value"));
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
                conn.setAutoCommit(false); // بدء المعاملة

                System.out.println(Thread.currentThread().getName() + ": تأمين الصف بالمعرف " + id1);
                try (PreparedStatement pstmt1 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt1.setString(1, value1);
                    pstmt1.setInt(2, id1);
                    pstmt1.executeUpdate();
                }
                Thread.sleep(100); // إدخال تأخير بسيط

                System.out.println(Thread.currentThread().getName() + ": تأمين الصف بالمعرف " + id2);
                try (PreparedStatement pstmt2 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt2.setString(1, value2);
                    pstmt2.setInt(2, id2);
                    pstmt2.executeUpdate();
                }

                conn.commit();
                System.out.println(Thread.currentThread().getName() + ": تم تنفيذ المعاملة بنجاح.");

            } catch (SQLException e) {
                if (conn != null) {
                    try {
                        conn.rollback();
                        System.err.println(Thread.currentThread().getName() + ": تم التراجع عن المعاملة بسبب خطأ: " + e.getMessage());
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
                        conn.setAutoCommit(true); // إعادة تعيين الالتزام التلقائي
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

**الشرح:**

1.  **إعداد قاعدة البيانات:**
    * `DB_URL`: يحدد عنوان الاتصال لملف قاعدة بيانات SQLite (`deadlock_example.db`).
    * `CREATE_TABLE_SQL`, `INSERT_ITEM_SQL`, `UPDATE_ITEM_SQL`: تُعرِّف عبارات SQL لإنشاء الجدول وإدخال البيانات الأولية وتحديث الصفوف.
    * `createTableAndInitialData()`: تنشئ جدول `items` إذا لم يكن موجودًا وتدخل صفين أوليين بالمعرفات 1 و 2.

2.  **التحديثات المتزامنة:**
    * `ExecutorService`: تم إنشاء `ExecutorService` بمجموعة خيوط ثابتة مكونة من 2 لمحاكاة التنفيذ المتزامن لمهمتين.
    * `UpdateTask`: هذه الفئة الداخلية تنفذ واجهة `Runnable`. يمثل كل كائن من `UpdateTask` معاملة ستحاول تحديث صفين.
        * يأخذ المُنشئ المعرفات والقيم الجديدة للصفين المراد تحديثهما.
        * تنفذ طريقة `run()` ما يلي:
            * تُنشئ اتصالاً بقاعدة البيانات.
            * تضبط `conn.setAutoCommit(false)` لبدء معاملة صريحة.
            * **التحديث الأول:** ينفذ عبارة `UPDATE` للصف الأول (`id1`).
            * `Thread.sleep(100)`: يُدخل تأخيرًا بسيطًا لزيادة فرصة حدوث deadlock. هذا يسمح للخيط الأول بالحصول على قفل على الصف الأول قبل أن يحاول الخيط الثاني الحصول عليه.
            * **التحديث الثاني:** ينفذ عبارة `UPDATE` للصف الثاني (`id2`).
            * `conn.commit()`: يحاول تنفيذ المعاملة.
            * **معالجة الأخطاء:** يتضمن كتلة `try-catch` لمعالجة `SQLException`. إذا حدث استثناء (والذي قد يكون deadlock)، فإنه يحاول التراجع عن المعاملة باستخدام `conn.rollback()`.
            * **كتلة Finally:** تضمن إغلاق الاتصال وإعادة ضبط `autoCommit` إلى `true`.

3.  **ترتيب التعارض:**
    * في طريقة `main`، يتم إرسال كائنين من `UpdateTask` إلى المُنفذ:
        * تحاول المهمة الأولى تحديث الصف 1 ثم الصف 2.
        * تحاول المهمة الثانية تحديث الصف 2 ثم الصف 1.
    * هذا الترتيب المتعارض لاكتساب الأقفال على نفس الموارد (الصفوف في جدول `items`) هو الشرط الذي يمكن أن يؤدي إلى deadlock.

4.  **التنفيذ والإخراج:**
    * `executor.shutdown()` و `executor.awaitTermination()`: يضمنان أن المُنفذ ينتظر انتهاء كلا المهمتين.
    * `printFinalData()`: بعد انتهاء الخيوط، تطبع هذه الطريقة المحتويات النهائية لجدول `items` لملاحظة النتيجة.

**كيفية التشغيل:**

1.  **حفظ:** احفظ الكود كـ `DeadlockGenerator.java`.
2.  **ترجمة:** اترجم الكود باستخدام مترجم Java: `javac DeadlockGenerator.java`
3.  **تشغيل:** نفذ الكود المترجم: `java DeadlockGenerator`

**النتيجة المتوقعة:**

عند تشغيل هذا الكود، من المحتمل أن ترى إخراجًا مشابهًا لهذا (قد يختلف الإخراج الدقيق قليلاً اعتمادًا على التوقيت وكشف نظام قاعدة البيانات لـ deadlock):

```
Thread-0: تأمين الصف بالمعرف 1
Thread-1: تأمين الصف بالمعرف 2
Thread-0: تأمين الصف بالمعرف 2
Thread-1: تأمين الصف بالمعرف 1
Thread-1: تم التراجع عن المعاملة بسبب خطأ: قاعدة البيانات مؤمنة
Thread-0: تم تنفيذ المعاملة بنجاح.

الحالة النهائية للجدول:
المعرف: 1, القيمة: Updated Value 1 - Thread 0
المعرف: 2, القيمة: Updated Value 2 - Thread 0
```

أو في بعض الأحيان، قد يتم التراجع عن Thread-0 بدلاً من ذلك. الملاحظة الرئيسية هي أن أحد الخيوط سيواجه `SQLException` يشير إلى تعارض في القفل أو deadlock، وسيتم التراجع عن معاملته. عادةً ما ينجح الخيط الآخر.

**ملاحظات مهمة:**

* **نظام قاعدة البيانات:** يستخدم هذا المثال SQLite للتبسيط. قد يختلف السلوك ورسائل الخطأ مع أنظمة قواعد البيانات الأخرى مثل PostgreSQL و MySQL وما إلى ذلك. قد تحتاج إلى تعديل عنوان برنامج تشغيل JDBC وربما عبارات SQL.
* **مستويات العزل:** يمكن لمستوى عزل المعاملة الافتراضي لقاعدة البيانات أن يؤثر على احتمالية حدوث deadlocks. قد تجعل مستويات العزل الأعلى deadlocks أكثر تكرارًا.
* **التأخير:** `Thread.sleep()` ضروري لتوضيح deadlock. بدونه، قد تكمل معاملة واحدة قبل أن تتاح لل其他 فرصة لاكتساب القفل الأول.
* **معالجة الأخطاء:** في التطبيق الواقعي، يجب أن يكون لديك معالجة قوية للأخطاء وآليات إعادة محاولة محتملة للمعاملات التي تفشل بسبب deadlocks.