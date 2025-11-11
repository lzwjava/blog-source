---
audio: false
generated: true
lang: ar
layout: post
title: نسخ الملفات مع هيكل المجلد
translated: true
type: note
---

باستخدام مخرجات أمر `find` الخاص بك، تريد نسخ جميع ملفات `.log` إلى `/Users/lzwjava/projects/logs` مع الحفاظ على هيكل الدلائل الخاص بها. على سبيل المثال، ملف مثل `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` يجب أن ينتهي به المطاف إلى `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`. سأوضح لك كيفية تحقيق ذلك باستخدام `find` مع `cp` أو `rsync`، مع ضمان الحفاظ على تسلسل الدلائل.

---

### **الحل 1: استخدام `find` مع `cp`**
يمكنك استخدام `find` لتحديد موقع ملفات `.log` و `cp` مع خيار `--parents` لنسخها مع الحفاظ على هيكل الدلائل الخاص بها.

#### **الأمر**
```bash
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

#### **الشرح**
- **`find . -name "*.log"`**: يحدد موقع جميع ملفات `.log` في الدليل الحالي والدلائل الفرعية (كما في مثالك).
- **`-exec cp --parents {} /Users/lzwjava/projects/logs \;`**:
  - `cp --parents`: ينسخ الملف ويعيد إنشاء مسار الدليل الخاص به بالنسبة للمصدر (`.`).
  - `{}`: عنصر نائب لكل ملف يجده `find`.
  - `/Users/lzwjava/projects/logs`: الدليل الوجهة.
  - `\;`: ينهي أمر `-exec`.

#### **النتيجة**
- `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` → `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`
- يتم الحفاظ على هيكل الدلائل تحت `CoreSimulator`.

#### **قبل التشغيل**
- تأكد من وجود `/Users/lzwjava/projects/logs`:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **الحل 2: استخدام `rsync`**
`rsync` أداة أخرى قوية يمكنها نسخ الملفات مع الحفاظ على هيكل الدلائل، وغالبًا ما تكون أكثر كفاءة للعمليات المجمعة.

#### **الأمر**
```bash
find . -name "*.log" -exec rsync -R -a {} /Users/lzwjava/projects/logs \;
```

#### **الشرح**
- **`-R`**: يستخدم المسارات النسبية، مما يحافظ على هيكل الدلائل من المصدر (`.`).
- **`-a`**: وضع الأرشيف (يحافظ على الطوابع الزمنية، الأذونات، إلخ).
- `{}`: كل ملف `.log` يتم العثور عليه.
- `/Users/lzwjava/projects/logs`: الدليل الهدف.

#### **النتيجة**
نفس ما ورد أعلاه — يتم نسخ الملفات مع مساراتها النسبية الكاملة سليمة.

#### **قبل التشغيل**
- أنشئ دليل الوجهة إذا لم يكن موجودًا:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **التحقق من النسخ**
بعد تشغيل أي من الأمرين، تحقق من الوجهة:
```bash
ls -R /Users/lzwjava/projects/logs
```
يجب أن ترى:
```
/Users/lzwjava/projects/logs:
CoreSimulator

/Users/lzwjava/projects/logs/CoreSimulator:
CoreSimulator.log  FC275C39-59CC-4483-A64E-5D459D7A1D57  Simulator.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57:
com.apple.itunesstored  system.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/com.apple.itunesstored:
itunesstored.log
```

---

### **ملاحظات رئيسية**
- **الأذونات:** تأكد من أن لديك صلاحية الكتابة إلى `/Users/lzwjava/projects/logs`. إذا لم يكن الأمر كذلك، استخدم `sudo` (مثل `sudo cp ...`) أو عدل الأذونات:
  ```bash
  chmod -R u+w /Users/lzwjava/projects/logs
  ```
- **الاستبدال:** إذا كانت الملفات موجودة بالفعل في الوجهة:
  - `cp` سوف تستبدل دون سابق إنذار.
  - `rsync -a` سوف تستبدل أيضًا، ولكن يمكنك إضافة `--ignore-existing` لتخطي الملفات الموجودة:
    ```bash
    find . -name "*.log" -exec rsync -R -a --ignore-existing {} /Users/lzwjava/projects/logs \;
    ```
- **التجربة الجافة (اختبر أولاً):**
  - لـ `cp`، أضف `echo` للمعاينة:
    ```bash
    find . -name "*.log" -exec echo cp --parents {} /Users/lzwjava/projects/logs \;
    ```
  - لـ `rsync`، استخدم `--dry-run`:
    ```bash
    find . -name "*.log" -exec rsync -R -a --dry-run {} /Users/lzwjava/projects/logs \;
    ```

---

### **ماذا تختار؟**
- **`cp`**: أبسط، لا حاجة لأدوات إضافية (متوفرة على جميع أنظمة يونكس).
- **`rsync`**: أكثر مرونة (مثلًا للمزامنة، تخطي المكررات)، لكنها تتطلب تثبيت `rsync` (قياسي في معظم الأنظمة).

كلاهما سيعمل في حالتك. أوصي بالبدء بـ `cp --parents` للبساطة.

---

### **الأمر النهائي (موصى به)**
```bash
mkdir -p /Users/lzwjava/projects/logs
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

شغّل هذا من دليل `Logs` الخاص بك (`lzwjava@anonymous Logs %`)، وستكون جاهزًا! أعلمني إذا واجهت أي مشاكل أو أردت تعديل السلوك (مثلًا جعل الهيكل مسطحًا بدلاً من ذلك).