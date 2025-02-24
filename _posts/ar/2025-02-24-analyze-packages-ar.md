---
audio: false
lang: ar
layout: post
title: تحليل حزم جافا
translated: true
---

### فهم الطلب
- **عندما يكون `level = 0` أو غير موفر**: استخدم الاسم الكامل للحزمة كما تم استخراجه من إعلانات `import` في Java (مثل `java.util` أو `com.google.common.eventbus`), دون تقصيرها.
- **عندما يكون `level > 0`**: تقصير اسم الحزمة إلى أول `level` أجزاء (مثلًا، بالنسبة لـ `com.google.common.eventbus`، `level = 2` يعطي `com.google`).
- يجب أن يستمر النص في معالجة ملفات Java، استخراج أسماء الحزم من إعلانات `import`، ومعالجة الحالات الحدودية بشكل مناسب.

### طريقة الحل
1. **تحليل المعلمات**:
   - إذا تم تقديم فقط الدليل الجذر (مثلًا `python script.py /path/to/dir`), قم بتعيين `level = 0`، مما يعني استخدام الاسم الكامل للحزمة.
   - إذا تم تقديم `level` (مثلًا `python script.py /path/to/dir 2`), استخدمه لتقصير اسم الحزمة، مع التأكد من أنه عدد صحيح موجب.
   - خروج بالخطأ إذا كانت المعلمات غير صالحة.

2. **استخراج الحزمة**:
   - استخراج اسم الحزمة من إعلانات `import` (مثلًا `import java.util.ArrayList;` يعطي `java.util`).
   - استخدام معايير تسمية Java: عادة ما تكون أسماء الحزم بالخط الصغير، بينما تبدأ أسماء الفئات بالحرف الكبير.

3. **منطق تقصير الحزمة**:
   - إذا كان `level = 0`، أضف الاسم الكامل للحزمة إلى مجموعة النتائج.
   - إذا كان `level > 0`، قم بفصل اسم الحزمة بالنقاط (`.`) وخذ أول `level` أجزاء.

4. **التسجيل والإخراج**:
   - إظهار بوضوح ما إذا كان يتم استخدام أسماء الحزم الكاملة أو المقصورة.
   - قائمة جميع الحزم الفريدة التي تم العثور عليها.

### التنفيذ
هنا هو النص الكامل لبرنامج Python الذي يفي بطلبك:

```python
import os
import sys
from collections import Counter

def find_java_files(root_dir):
    """
    البحث عن جميع ملفات .java في الدليل المحدد وجميع الدلائل الفرعية منه بشكل تكراري.

    Args:
        root_dir (str): الدليل الجذر لبدء البحث منه.

    Yields:
        str: المسار الكامل لكل ملف .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    استخراج اسم الحزمة من إعلان `import`.

    يستخدم المعيار أن أسماء الحزم بالخط الصغير، بينما تبدأ أسماء الفئات بالحرف الكبير. يدعم استيراد الفئات (*).

    Args:
        import_statement (str): سطر الإعلان من ملف Java.

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
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python script.py <root_directory> [level] [--count]")
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
            print(f"Invalid argument: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"Invalid arguments: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)

    # التحقق من وجود الدليل
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)

    # تسجيل بداية التحليل
    level_str = "using full package names" if level == 0 else f"at level {level}"
    count_str = "with appearance counts" if count else ""
    print(f"[INFO] Starting analysis of directory: {root_dir} {level_str} {count_str}")

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
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
            continue

    # طباعة ملخص
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    if count:
        print(f"[INFO] Total unique packages with counts: {len(package_counter)}")
    else:
        print(f"[INFO] Total unique packages: {len(package_counter)}")

    # طباعة النتائج بالترتيب المناسب
    if package_counter:
        if count:
            print("[INFO] Analysis complete. Printing unique packages with counts (sorted by count descending):")
            # ترتيب حسب العدد تنازليًا، ثم حسب اسم الحزمة تصاعديًا
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] Analysis complete. Printing unique packages (sorted by name ascending):")
            # ترتيب حسب اسم الحزمة تصاعديًا
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] No packages found.")
```

### كيفية عمله
- **تشغيل النص**:
  - `python script.py /path/to/java/project`: تحليل جميع ملفات `.java` في الدليل واستخدام أسماء الحزم الكاملة (`level = 0`).
  - `python script.py /path/to/java/project 2`: تقصير أسماء الحزم إلى أول 2 أجزاء (مثلًا، `com.google.common.eventbus` يصبح `com.google`).

- **مثال على الإخراج**:
  افترض أنك لديك ملف Java يحتوي على:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **مع `level = 0` (أو بدون مستوى موفر)**:
    ```
    [INFO] Starting analysis of directory: /path/to/java/project with full package names.
    [INFO] Entering directory: /path/to/java/project
    [INFO] Processing file: /path/to/java/project/MyFile.java
    [INFO] Total Java files attempted: 1
    [INFO] Successfully processed: 1
    [INFO] Files with errors: 0
    [INFO] Total unique full packages: 2
    [INFO] Analysis complete. Printing unique full packages:
    com.google.common.eventbus
    java.util
    ```
  - **مع `level = 2`**:
    ```
    [INFO] Starting analysis of directory: /path/to/java/project at level: 2
    [INFO] Entering directory: /path/to/java/project
    [INFO] Processing file: /path/to/java/project/MyFile.java
    [INFO] Total Java files attempted: 1
    [INFO] Successfully processed: 1
    [INFO] Files with errors: 0
    [INFO] Total unique packages at level 2: 2
    [INFO] Analysis complete. Printing unique packages at level 2:
    com.google
    java.util
    ```

- **الميزات الرئيسية**:
  - **أسماء الحزم الكاملة**: عندما يكون `level = 0` أو غير موفر، يستخدم الاسم الكامل للحزمة كما تم استخراجها (مثل `java.util`, `com.google.common.eventbus`).
  - **التقصير**: عندما يكون `level > 0`، يأخذ أول `level` أجزاء.
  - **معالجة الأخطاء**: التحقق من الدليل الصالحة و `level` غير سالب أو غير عدد صحيح.
  - **الفردية**: تخزين الحزم في مجموعة لتجنب التكرار.

### الحالات الحدودية التي تم التعامل معها
- **عدم وجود مستوى**: الافتراض `level = 0`، واستخدام أسماء الحزم الكاملة.
- **مستوى غير صالح**: الخروج بالخطأ إذا كان `level` سالبًا أو غير عدد صحيح.
- **حزم قصيرة**: إذا كانت الحزمة لديها أقل من `level` أجزاء (مثل `java` مع `level = 2`), يستخدم الاسم الكامل للحزمة (`java`).
- **استيرادات فارغة**: تخطي السطور التي لم يتم استخراج الحزمة منها.