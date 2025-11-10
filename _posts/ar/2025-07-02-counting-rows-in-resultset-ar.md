---
audio: false
generated: true
lang: ar
layout: post
title: عدّ الصفوف في مجموعة النتائج القابلة للتمرير
translated: true
type: note
---

في جافا، عند العمل مع `ResultSet` (على سبيل المثال، من خلال `Statement.executeQuery()`)، قد يكون حساب عدد الصفوف صعبًا إذا تم تعيين `fetchSize` على `0` (مما يعني أن مشغل JDBC سيجلب الصفوف حسب الحاجة). علاوة على ذلك، فإن استخدام مجموعة نتائج قابلة للتمرير (باستخدام `ResultSet.TYPE_SCROLL_INSENSITIVE` أو `ResultSet.TYPE_SCROLL_SENSITIVE`) يسمح لك بالتنقل عبر مجموعة النتائج ولكنه يتطلب ذاكرة أكبر حيث يتم تحميل الصفوف في الذاكرة.

إليك إستراتيجية يمكنك استخدامها لحساب الصفوف في `ResultSet` دون الحاجة إلى اجتياز كامل مجموعة النتائج. تستخدم هذه الإستراتيجية ميزة `scrollable` الخاصة بـ `ResultSet` والقدرة على "الانتقال إلى الصف الأخير" و"الحصول على رقم الصف".

### خطوات حساب الصفوف باستخدام `ResultSet` قابل للتمرير:

1.  **إنشاء ResultSet قابل للتمرير**: تأكد من استخدام `Statement` يمكنه إنشاء مجموعات نتائج قابلة للتمرير عن طريق تعيين نوع المؤشر المناسب.
2.  **الانتقال إلى الصف الأخير**: تسمح لك مجموعة النتائج القابلة للتمرير بالانتقال إلى الصف الأخير باستخدام `last()`.
3.  **الحصول على رقم الصف**: بعد الانتقال إلى الصف الأخير، يمكنك استدعاء `getRow()` لتحديد عدد الصفوف.
4.  **اختياري**: إذا كنت بحاجة إلى التكرار عبر مجموعة النتائج، ارجع إلى الصف الأول باستخدام `first()`.

إليك مثال على التنفيذ بلغة جافا:

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
            
            // الانتقال إلى الصف الأخير لحساب العدد الإجمالي للصفوف
            if (rs.last()) {
                int rowCount = rs.getRow();
                System.out.println("Total rows: " + rowCount);
                
                // اختياريًا، العودة إلى الصف الأول
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

### النقاط الرئيسية:

*   **ResultSet قابل للتمرير**: نقوم بإنشاء `ResultSet` قابل للتمرير باستخدام `ResultSet.TYPE_SCROLL_INSENSITIVE`. يسمح لك هذا النوع من مجموعات النتائج بالانتقال إلى الصف الأخير والحصول على عدد الصفوف.
*   **عدد الصفوف**: تُرجع طريقة `rs.getRow()` رقم الصف الحالي عندما يكون المؤشر في موضع الصف الأخير. هذه القيمة تمثل بشكل فعال العدد الإجمالي للصفوف في مجموعة النتائج.
*   **حجم الجلب**: إذا كان `fetchSize` هو `0`، فإن المشغل يجلب الصفوف ديناميكيًا، لكن استخدام مجموعة نتائج قابلة للتمرير يسمح لنا بالتنقل عبر الصفوف بكفاءة.

### أفضل الممارسات:

*   **كفاءة الذاكرة**: بينما تكون مجموعات النتائج القابلة للتمرير مفيدة لحساب الصفوف، انتبه إلى أنها قد تستهلك ذاكرة أكبر، حيث يجب تحميل جميع الصفوف في الذاكرة. إذا كنت تعمل مع مجموعة بيانات كبيرة، ففكر في استخدام نهج مختلف (مثل التكرار عبر مجموعة النتائج دون استخدام `last()` لحساب الصفوف تدريجيًا) إذا كان استخدام الذاكرة يمثل مصدر قلق.
*   **نهج بديل**: إذا كانت الذاكرة تمثل مشكلة وتحتاج فقط إلى عدد الصفوف، يمكنك تنفيذ استعلام `SELECT COUNT(*)` بدلاً من استرداد مجموعة النتائج بالكامل. غالبًا ما يكون هذا أكثر كفاءة.

```sql
SELECT COUNT(*) FROM your_table;
```

دعني أعلم إذا كنت بحاجة إلى مزيد من التوضيح!