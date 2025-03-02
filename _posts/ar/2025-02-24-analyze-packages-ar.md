---
audio: false
generated: false
lang: ar
layout: post
title: تحليل حزم جاڤا
translated: true
---

### فهم الطلب
- **عندما يكون `level = 0` أو غير موفر**: استخدم الاسم الكامل للحزمة كما تم استخراجها من بيانات `import` في Java (مثل `java.util` أو `com.google.common.eventbus`) دون تقصيرها.
- **عندما يكون `level > 0`**: تقصير اسم الحزمة إلى أول `level` أجزاء (مثلًا، بالنسبة لـ `com.google.common.eventbus`، `level = 2` يعطي `com.google`).
- يجب أن يستمر النص في معالجة ملفات Java، استخراج أسماء الحزم من بيانات `import`، ومعالجة الحالات الحدودية بشكل مناسب.

### طريقة الحل
1. **تحليل المعلمات**:
   - إذا تم تقديم فقط الدليل الجذر (مثلًا `python script.py /path/to/dir`)، قم بتعيين `level = 0`، مما يعني استخدام الاسم الكامل للحزمة.
   - إذا تم تقديم `level` (مثلًا `python script.py /path/to/dir 2`)، استخدمه لتقصير اسم الحزمة، مع التأكد من أنه عدد صحيح موجب.
   - خروج بالخطأ إذا كانت المعلمات غير صالحة.

2. **استخراج الحزمة**:
   - استخراج اسم الحزمة من بيانات `import` (مثلًا `import java.util.ArrayList;` يعطي `java.util`).
   - استخدام معايير تسمية Java: الحزم عادة ما تكون بأحرف صغيرة، بينما تبدأ أسماء الفئات بحرف كبير.

3. **منطق تقصير الحزمة**:
   - إذا كان `level = 0`، أضف الاسم الكامل للحزمة إلى مجموعة النتائج.
   - إذا كان `level > 0`، قم بتقسيم اسم الحزمة بنقاط (`.`) وخذ أول `level` أجزاء.

4. **تسجيل وإخراج**:
   - توضيح ما إذا كان يتم استخدام أسماء الحزم الكاملة أو المقصوصة.
   - قائمة جميع الحزم الفريدة التي تم العثور عليها.

### التنفيذ
هنا هو النص الكامل لبرنامج Python الذي يفي بطلبك:

```python
import os
import sys
from collections import Counter

def find_java_files(root_dir):
    """
    البحث عن جميع ملفات .java في الدليل المحدد وجميع الدلائل الفرعية.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    استخراج اسم الحزمة من بيان `import`.
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
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("استخدام: python script.py <root_directory> [level] [--count]")
        sys.exit(1)

    root_dir = sys.argv[1]
    level = 0
    count = False

    if len(sys.argv) == 3:
        if sys.argv[2] == "--count":
            count = True
        elif sys.argv[2].isdigit():
            level = int(sys.argv[2])
        else:
            print(f"معلمة غير صالحة: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"معلمات غير صالحة: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)

    # التحقق من وجود الدليل
    if not os.path.isdir(root_dir):
        print(f"[خطأ] الدليل المحدد ليس دليلًا: {root_dir}")
        sys.exit(1)

    # تسجيل بداية التحليل
    level_str = "استخدام أسماء الحزم الكاملة" if level == 0 else f"في مستوى {level}"
    count_str = "مع عدادات الظهور" if count else ""
    print(f"[معلومات] بدء تحليل الدليل: {root_dir} {level_str} {count_str}")

    # تهيئة المتغيرات
    package_counter = Counter()
    total_files = 0
    error_files = 0

    # معالجة ملفات Java
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                file_packages = set()
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level > 0:
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                            else:
                                truncated_package = package
                            file_packages.add(truncated_package)
            for pkg in file_packages:
                package_counter[pkg] += 1
            total_files += 1
        except Exception as e:
            print(f"[خطأ] لم يتم قراءة الملف {java_file}: {e}")
            error_files += 1
            continue

    # طباعة ملخص
    print(f"[معلومات] إجمالي ملفات Java المحاولة: {total_files + error_files}")
    print(f"[معلومات] تم معالجة: {total_files}")
    print(f"[معلومات] ملفات مع أخطاء: {error_files}")
    if count:
        print(f"[معلومات] إجمالي الحزم الفريدة مع العدادات: {len(package_counter)}")
    else:
        print(f"[معلومات] إجمالي الحزم الفريدة: {len(package_counter)}")

    # طباعة النتائج مع الترتيب المناسب
    if package_counter:
        if count:
            print("[معلومات] انتهى التحليل. طباعة الحزم الفريدة مع العدادات (مرتبة حسب العدات تنازليًا):")
            # ترتيب حسب العدات تنازليًا، ثم حسب اسم الحزمة تصاعديًا
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[معلومات] انتهى التحليل. طباعة الحزم الفريدة (مرتبة حسب الاسم تصاعديًا):")
            # ترتيب حسب اسم الحزمة تصاعديًا
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[معلومات] لم يتم العثور على حزم.")
```

### كيفية عمل النص
- **تنفذ النص**:
  - `python script.py /path/to/java/project`: يحلل جميع ملفات `.java` في الدليل ويستخدم أسماء الحزم الكاملة (`level = 0`).
  - `python script.py /path/to/java/project 2`: يقصير أسماء الحزم إلى أول 2 أجزاء (مثلًا، `com.google.common.eventbus` يصبح `com.google`).

- **مثال على الإخراج**:
  افترض أن لديك ملف Java يحتوي على:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **مع `level = 0` (أو بدون مستوى موفر)**:
    ```
    [معلومات] بدء تحليل الدليل: /path/to/java/project باستخدام أسماء الحزم الكاملة.
    [معلومات] دخول الدليل: /path/to/java/project
    [معلومات] معالجة الملف: /path/to/java/project/MyFile.java
    [معلومات] إجمالي ملفات Java المحاولة: 1
    [معلومات] تم معالجة: 1
    [معلومات] ملفات مع أخطاء: 0
    [معلومات] إجمالي الحزم الفريدة الكاملة: 2
    [معلومات] انتهى التحليل. طباعة الحزم الفريدة الكاملة:
    com.google.common.eventbus
    java.util
    ```
  - **مع `level = 2`**:
    ```
    [معلومات] بدء تحليل الدليل: /path/to/java/project في مستوى: 2
    [معلومات] دخول الدليل: /path/to/java/project
    [معلومات] معالجة الملف: /path/to/java/project/MyFile.java
    [معلومات] إجمالي ملفات Java المحاولة: 1
    [معلومات] تم معالجة: 1
    [معلومات] ملفات مع أخطاء: 0
    [معلومات] إجمالي الحزم الفريدة في مستوى 2: 2
    [معلومات] انتهى التحليل. طباعة الحزم الفريدة في مستوى 2:
    com.google
    java.util
    ```

- **الميزات الرئيسية**:
  - **أسماء الحزم الكاملة**: عندما يكون `level = 0` أو غير موفر، يستخدم الاسم الكامل للحزمة كما تم استخراجها (مثلًا `java.util`، `com.google.common.eventbus`).
  - **تقصير**: عندما يكون `level > 0`، يأخذ أول `level` أجزاء.
  - **معالجة الأخطاء**: التحقق من الدليل الصالحة و `level` غير سالب.
  - **الفردية**: تخزين الحزم في مجموعة لتجنب التكرار.

### الحالات الحدودية المعالجة
- **العدد المفقود**: الافتراض `level = 0`، باستخدام أسماء الحزم الكاملة.
- **العدد غير الصالح**: الخروج بالخطأ إذا كان `level` سالبًا أو غير عدد صحيح.
- **الحزم القصيرة**: إذا كانت الحزمة أقل من `level` أجزاء (مثلًا `java` مع `level = 2`)، يستخدم الاسم الكامل للحزمة (`java`).
- **الاستيراد الفارغ**: تخطي السطور التي لم يتم استخراج الحزمة منها.