---
audio: false
generated: true
image: false
lang: ar
layout: post
model: moonshotai/kimi-k2-thinking
title: تراجع معاملات DB2 وكشف الأخطاء
translated: true
type: note
---

## عندما يقوم DB2 بتراجع بسبب أخطاء النظام

يقوم IBM DB2 تلقائيًا بتراجع المعاملات عند مواجهة أخطاء نظام حرجة تهدد سلامة البيانات. السيناريوهات الشائعة تشمل:

- **المشاجرات (Deadlocks) أو انتهاء المهلة**: SQLCODE -911 مع SQLSTATE 40001، رمز السبب "2" يشير إلى تراجع المعاملة بسبب مشاجرة
- **إنهاء غير طبيعي للعملية (Process abend)**: في جميع بيئات DB2، يؤدي إنهاء العملية إلى触发 تراجع ضمني
- **فشل موارد النظام**: فشل في الذاكرة أو القرص أو الشبكة يمنع اكتمال المعاملة
- **تعارض الطوابع الزمنية (Timestamp conflicts)**: يحدث SQLCODE -818 عندما لا تتطابق الطوابع الزمنية الداخلية بين الوحدة النمطية و DBRM
- **شبكات الأمان لـ Connection pooling**: بعض التطبيقات تتراجع تلقائيًا عن الاتصالات عند تحريرها لمنع تسبب المعاملات غير الملتزمة في مشاكل القفل

## كيفية اكتشاف معلومات الخطأ التفصيلية

### 1. آليات الكشف الأساسية عن الأخطاء

**SQLCODE و SQLSTATE**
بعد كل عبارة SQL، يقوم DB2 بتعيين هذه المتغيرات:

```sql
-- التحقق فورًا بعد تنفيذ العبارة
IF SQLCODE < 0 THEN
    -- حدث خطأ
    ROLLBACK;
END IF;
```

رموز فئة SQLSTATE تحدد أنواع الأخطاء بشكل خاص:
- **الفئة 58**: خطأ في النظام (مثل عدم توفر المورد، تدخل المشغل)
- **الفئة 40**: تراجع المعاملة
- **الفئة 25**: حالة معاملة غير صالحة

**عبارة GET DIAGNOSTICS**
للحصول على معلومات تفصيلية عن الخطأ في الإجراءات المخزنة SQL PL:

```sql
DECLARE v_sqlcode INTEGER;
DECLARE v_sqlstate CHAR(5);
DECLARE v_sqlmessage VARCHAR(256);

GET DIAGNOSTICS CONDITION 1
    v_sqlcode = DB2_RETURNED_SQLCODE,
    v_sqlstate = RETURNED_SQLSTATE,
    v_sqlmessage = MESSAGE_TEXT;
```

### 2. الكشف عن الأخطاء عبر سطر الأوامر

عند تنفيذ البرامج النصية عبر سطر أوامر `db2`، تحقق من رموز الخروج:

- **رمز الخروج 8**: خطأ في النظام
- **رمز الخروج 4**: خطأ في DB2 (انتهاك قيد، كائن غير موجود)
- **رمز الخروج 2**: تحذير من DB2
- **رمز الخروج 1**: لم يتم العثور على صفوف

**النمط الموصى به للبرنامج النصي**:
```bash
db2 -l migration.log +c -stf migration.sql
if [ $? -ge 4 ]; then
    db2 rollback
    tail -10 migration.log  # مراجعة الخطأ التفصيلي
else
    db2 commit
fi
```

### 3. معالجة الأخطاء في الإجراءات المخزنة

للكشف الشامل عن الأخطاء في SQL PL، استخدم المعالجات المعلنة:

```sql
CREATE PROCEDURE my_procedure()
BEGIN
    DECLARE v_sqlcode INTEGER DEFAULT 0;
    DECLARE v_sqlstate CHAR(5) DEFAULT '00000';
    DECLARE v_error_message VARCHAR(256);
    
    -- Declare exit handler for any exception
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            v_sqlcode = DB2_RETURNED_SQLCODE,
            v_sqlstate = RETURNED_SQLSTATE,
            v_error_message = MESSAGE_TEXT;
            
        -- تسجيل تفاصيل الخطأ في جدول أو ملف
        INSERT INTO error_log (sqlcode, sqlstate, message, timestamp)
        VALUES (v_sqlcode, v_sqlstate, v_error_message, CURRENT_TIMESTAMP);
        
        ROLLBACK;
    END;
    
    -- منطق المعاملات الخاص بك هنا
    UPDATE employee SET salary = salary + 1000 WHERE job = 'MANAGER';
    INSERT INTO audit_log VALUES (CURRENT_TIMESTAMP, 'Salary update');
    
    COMMIT;
END
```

### 4. ملفات سجل تشخيص DB2

لأخطاء مستوى النظام، تحقق دائمًا من:

- **db2diag.log**: سجل التشخيص الأساسي الذي يحتوي على معلومات مفصلة عن أخطاء النظام
- **سجل الإشعارات (Notification log)**: يحتوي على ملخصات الأخطاء
- **سجلات سطر الأوامر**: استخدم خيار `-l logfile.txt` لالتقاط الأخطاء

## أفضل الممارسات للكشف عن الأخطاء

1. **تحقق دائمًا من SQLCODE/SQLSTATE فورًا** بعد العمليات الحرجة
2. **استخدم GET DIAGNOSTICS** للحصول على سياق غني للخطأ في الإجراءات المخزنة
3. **نفذ مراقبة نسبة تراجع المعاملات** - أي شيء يزيد عن 1% يستدعي التحقيق
4. **مكّن خيارات الأوامر** لتنفيذ البرامج النصية:
   ```bash
   db2 +c -s -v -l error.log -f script.sql
   ```
   حيث `+c` يعطل الالتزام التلقائي و `-s` يتوقف عند الخطأ
5. **استخدم نقاط الحفظ (Savepoints)** للتراجعات الجزئية داخل المعاملات المعقدة
6. **سجل تفاصيل الخطأ** في جداول دائمة قبل التراجع للحفاظ على معلومات التشخيص

## رموز SQLSTATE لأخطاء النظام الرئيسية للمراقبة

| SQLSTATE | الوصف | الإجراء |
|----------|-------------|--------|
| **58004** | خطأ في النظام (أسباب متنوعة) | تحقق من db2diag.log فورًا |
| **58008** | خطأ في الاتصال | تحقق من الشبكة / الاتصال |
| **HY000** | خطأ عام في المشغل (driver) | تحقق من سجلات مشغل ODBC/JDBC |
| **40001** | مشاجرة / انتهاء مهلة | أعد محاولة المعاملة مع تراجع (backoff) |

بالنسبة لبيئات الإنتاج، يجب أن تنبه أدوات المراقبة على **SQLCODE < 0** و **رموز SQLSTATE من الفئة 58** لاكتشاف المشكلات على مستوى النظام بشكل استباقي قبل أن تتفاقم.