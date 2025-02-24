---
audio: false
lang: ar
layout: post
title: تحليل حزم جاڤا
translated: true
---

مستندًا على استفسارك، تريدك أن يكون لديك نصًا حيث إذا كان `level` 0 أو لم يتم تقديمه، فإنه يستخدم اسم الحزمة الكامل (جميع أجزاءه)، مما يعني أن `level = 0` يعامل ك"لا نهائي" أو "استخدم جميع الأجزاء"، بدلاً من تقليلها إلى عدد محدد من الأجزاء (مثل الجزء الأول فقط عندما `level = 1`). أدناه، سأشرح كيفية تنفيذ ذلك في نص Python الذي يحلل ملفات Java لاستخراج أسماء الحزم، وسأقدم حلًا كاملًا مخصصًا لطلبك.

### فهم الطلب
- **عندما `level = 0` أو لم يتم تقديمه**: استخدم الاسم الكامل للحزمة كما تم استخراجها من بياتات `import` في Java (مثل `java.util` أو `com.google.common.eventbus`), دون تقليمها.
- **عندما `level > 0`**: تقليم اسم الحزمة إلى أول `level` أجزاء (مثلًا، بالنسبة لـ `com.google.common.eventbus`، `level = 2` يعطي `com.google`).
- يجب أن يستمر النص في معالجة ملفات Java، واستخراج أسماء الحزم من بياتات `import`، ومعالجة الحالات الحدودية بشكل مناسب.

### نهج الحل
1. **تحليل المعلمات**:
   - إذا تم تقديم فقط الدليل الجذر (مثلًا `python script.py /path/to/dir`), قم بتعيين `level = 0`، مما يعني استخدام الاسم الكامل للحزمة.
   - إذا تم تقديم `level` (مثلًا `python script.py /path/to/dir 2`), استخدمه لتقليم اسم الحزمة، مع التأكد من أنه عدد صحيح موجب.
   - خروج بالخطأ إذا كانت المعلمات غير صالحة.

2. **استخراج الحزمة**:
   - استخراج اسم الحزمة من بياتات `import` (مثلًا `import java.util.ArrayList;` يعطي `java.util`).
   - استخدم معايير تسمية Java: الحزم عادة تكون بالأحرف الصغيرة، وأسماء الفئات تبدأ بحرف كبير.

3. **منطق تقليم الحزمة**:
   - إذا `level = 0`، أضف الاسم الكامل للحزمة إلى مجموعة النتائج.
   - إذا `level > 0`، قم بفصل اسم الحزمة بنقاط (`.`) وخذ أول `level` أجزاء.

4. **تسجيل ونتائج**:
   - أظهر بشكل واضح ما إذا كان يتم استخدام أسماء الحزم الكاملة أو المقطوعة.
   - قم بتسجيل جميع الحزم الفريدة التي تم العثور عليها.

### التنفيذ
هنا النص الكامل Python الذي يفي بطلبك:

```python
import os
import sys

def find_java_files(root_dir):
    """
    البحث عن جميع ملفات .java في الدليل المحدد ودلائله الفرعية بشكل تكراري.

    Args:
        root_dir (str): الدليل الجذر لبدء البحث منه.

    Yields:
        str: المسار الكامل لكل ملف .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"[INFO] الدخول إلى الدليل: {dirpath}")
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    استخراج اسم الحزمة من بيان `import`.

    يُفترض أن أسماء الحزم بالأحرف الصغيرة، وتوقف عند أسماء الفئات (أحرف كبيرة) أو النجمات (*).

    Args:
        import_statement (str): سطر البيان `import` من ملف Java.

    Returns:
        str: اسم الحزمة، أو سلسلة فارغة إذا لم يتم تحديدها.
    """
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    import_path = ' '.join(parts).strip(';').strip()
    identifiers = import_path.split('.')
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # تحليل المعلمات السطرية
    if len(sys.argv) == 2:
        root_dir = sys.argv[1]
        level = 0  # لم يتم تقديم مستوى، استخدم أسماء الحزم الكاملة
    elif len(sys.argv) == 3:
        root_dir = sys.argv[1]
        try:
            level = int(sys.argv[2])
            if level < 0:
                raise ValueError
        except ValueError:
            print("[ERROR] يجب أن يكون المستوى عدد صحيح موجب.")
            sys.exit(1)
    else:
        print("استخدام: python script.py <root_directory> [level]")
        sys.exit(1)

    # التحقق من وجود الدليل
    if not os.path.isdir(root_dir):
        print(f"[ERROR] المسار المحدد ليس دليلًا: {root_dir}")
        sys.exit(1)

    # تسجيل بداية التحليل
    if level == 0:
        print(f"[INFO] بدء تحليل الدليل: {root_dir} مع أسماء الحزم الكاملة.")
    else:
        print(f"[INFO] بدء تحليل الدليل: {root_dir} على مستوى: {level}")

    # تهيئة المتغيرات
    packages = set()
    total_files = 0
    error_files = 0

    # معالجة ملفات Java
    for java_file in find_java_files(root_dir):
        print(f"[INFO] معالجة الملف: {java_file}")
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level == 0:
                                # استخدام الاسم الكامل للحزمة
                                packages.add(package)
                            else:
                                # تقليم إلى أول 'level' أجزاء
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                                packages.add(truncated_package)
            total_files += 1
        except Exception as e:
            print(f"[ERROR] لم يتم قراءة الملف {java_file}: {e}")
            error_files += 1
            continue

    # طباعة ملخص
    print(f"[INFO] إجمالي ملفات Java المحاولة: {total_files + error_files}")
    print(f"[INFO] تم معالجة: {total_files}")
    print(f"[INFO] ملفات مع أخطاء: {error_files}")
    if level == 0:
        print(f"[INFO] إجمالي الحزم الفريدة الكاملة: {len(packages)}")
    else:
        print(f"[INFO] إجمالي الحزم الفريدة على مستوى {level}: {len(packages)}")

    # طباعة النتائج
    if packages:
        if level == 0:
            print("[INFO] انتهى التحليل. طباعة الحزم الفريدة الكاملة:")
        else:
            print(f"[INFO] انتهى التحليل. طباعة الحزم الفريدة على مستوى {level}:")
        for package in sorted(packages):
            print(package)
    else:
        print("[INFO] لم يتم العثور على حزم.")
```

### كيفية عمله
- **تشغيل النص**:
  - `python script.py /path/to/java/project`: يحلل جميع ملفات `.java` في الدليل ويستخدم أسماء الحزم الكاملة (`level = 0`).
  - `python script.py /path/to/java/project 2`: يقليم أسماء الحزم إلى أول 2 أجزاء (مثلًا، `com.google.common.eventbus` يصبح `com.google`).

- **مثال على الخرج**:
  افترض أن لديك ملف Java يحتوي على:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **مع `level = 0` (أو بدون مستوى)**:
    ```
    [INFO] بدء تحليل الدليل: /path/to/java/project مع أسماء الحزم الكاملة.
    [INFO] الدخول إلى الدليل: /path/to/java/project
    [INFO] معالجة الملف: /path/to/java/project/MyFile.java
    [INFO] إجمالي ملفات Java المحاولة: 1
    [INFO] تم معالجة: 1
    [INFO] ملفات مع أخطاء: 0
    [INFO] إجمالي الحزم الفريدة الكاملة: 2
    [INFO] انتهى التحليل. طباعة الحزم الفريدة الكاملة:
    com.google.common.eventbus
    java.util
    ```
  - **مع `level = 2`**:
    ```
    [INFO] بدء تحليل الدليل: /path/to/java/project على مستوى: 2
    [INFO] الدخول إلى الدليل: /path/to/java/project
    [INFO] معالجة الملف: /path/to/java/project/MyFile.java
    [INFO] إجمالي ملفات Java المحاولة: 1
    [INFO] تم معالجة: 1
    [INFO] ملفات مع أخطاء: 0
    [INFO] إجمالي الحزم الفريدة على مستوى 2: 2
    [INFO] انتهى التحليل. طباعة الحزم الفريدة على مستوى 2:
    com.google
    java.util
    ```

- **الميزات الرئيسية**:
  - **أسماء الحزم الكاملة**: عندما `level = 0` أو لم يتم تقديمه، يستخدم الاسم الكامل للحزمة كما تم استخراجها (مثل `java.util`, `com.google.common.eventbus`).
  - **تقليم**: عندما `level > 0`، يأخذ أول `level` أجزاء.
  - **معالجة الأخطاء**: التحقق من الدليل الصالحة و `level` غير سالب.
  - **الفردية**: تخزين الحزم في مجموعة لتجنب التكرار.

### الحالات الحدودية المعالجة
- **مفقود مستوى**: الافتراض `level = 0`، باستخدام أسماء الحزم الكاملة.
- **مستوى غير صالح**: الخروج بالخطأ إذا كان `level` سالبًا أو غير عدد صحيح.
- **حزم قصيرة**: إذا كانت الحزمة أقل من `level` (مثل `java` مع `level = 2`), يستخدم الاسم الكامل (`java`).
- **استيراد فارغ**: تخطي السطور التي لم يتم استخراج الحزمة منها.

يفي هذا النص بالكامل بطلبك: عندما `level = 0` أو لم يتم تقديمه، يستخدم جميع أجزاء اسم الحزمة، مما يعامله ك"لا نهائي" في ما يتعلق بالأجزاء المستخدمة.