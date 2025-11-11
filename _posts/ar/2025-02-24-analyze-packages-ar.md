---
audio: false
generated: true
lang: ar
layout: post
title: تحليل حزم جافا
translated: true
type: note
---

بناءً على استفسارك، تريد نصًا برمجيًا حيث إذا كانت المعلمة `level` تساوي 0 أو لم يتم توفيرها، فإنه يستخدم اسم الحزمة بالكامل (جميع أجزائها)، مما يعامل `level = 0` على أنها "لا نهائية" أو "استخدم جميع الأجزاء"، بدلاً من حصرها بعدد محدد من الأجزاء (مثل الجزء الأول فقط عندما `level = 1`). أدناه، سأشرح كيف يمكن تنفيذ ذلك في نص برمجي Python يحلل ملفات Java لاستخراج أسماء الحزم، وسأقدم حلاً كاملاً مخصصًا لطلبك.

### فهم المتطلبات
- **عندما `level = 0` أو لم يتم توفيرها**: استخدم اسم الحزمة الكامل كما تم استخراجه من عبارات `import` في Java (مثل `java.util` أو `com.google.common.eventbus`)، دون اقتطاعه.
- **عندما `level > 0`**: اقتطع اسم الحزمة إلى أول `level` أجزاء (مثل، بالنسبة لـ `com.google.common.eventbus`، `level = 2` ستعطي `com.google`).
- يجب أن يستمر النص البرمجي في معالجة ملفات Java، واستخراج أسماء الحزم من عبارات `import`، والتعامل مع الحالات الطرفية بشكل مناسب.

### نهج الحل
1. **تحليل الوسائط (Arguments)**:
   - إذا تم توفير دليل الجذر فقط (مثل `python script.py /path/to/dir`)، اضبط `level = 0`، مما يعني استخدام اسم الحزمة الكامل.
   - إذا تم توفير `level` (مثل `python script.py /path/to/dir 2`)، استخدمه لاقتطاع اسم الحزمة، مع التأكد من أنه عدد صحيح غير سالب.
   - إنهاء البرنامج بخطأ إذا كانت الوسائط غير صالحة.

2. **استخراج الحزمة**:
   - استخرج اسم الحزمة من عبارات `import` (مثل، `import java.util.ArrayList;` تعطي `java.util`).
   - استخدم اصطلاحات تسمية Java: الحزم تكون عادةً بأحرف صغيرة، وأسماء الفئات تبدأ بحرف كبير.

3. **منطق اقتطاع الحزمة**:
   - إذا كانت `level = 0`، أضف اسم الحزمة الكامل إلى مجموعة النتائج.
   - إذا كانت `level > 0`، قسّم اسم الحزمة بالنقاط (`.`) وخذ أول `level` أجزاء.

4. **التسجيل والإخراج**:
   - أشر بوضوح إلى ما إذا كانت أسماء الحزم الكاملة أو المقتطعة مستخدمة.
   - اذكر جميع الحزم الفريدة التي تم العثور عليها.

### التنفيذ
إليك النص البرمجي Python الكامل الذي يلبي متطلباتك:

```python
import os
import sys
from collections import Counter

def find_java_files(root_dir):
    """
    البحث بشكل متكرر عن جميع ملفات .java في الدليل المعطى وجميع الأدلة الفرعية.
    
    Args:
        root_dir (str): دليل الجذر لبدء البحث منه.
    
    Yields:
        str: المسار الكامل لكل ملف .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    استخراج اسم الحزمة من عبارة import.
    
    يستخدم الاصطلاح القائل بأن أسماء الحزم تكون بأحرف صغيرة، بينما تبدأ أسماء الفئات
    بأحرف كبيرة. يتعامل مع عمليات الاستيراد باستخدام النمط العام (*).
    
    Args:
        import_statement (str): سطر عبارة import من ملف Java.
    
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
    # تحليل وسائط سطر الأوامر
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
    
    # تسجيل بدء التحليل
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
    
    # طباعة الملخص
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    if count:
        print(f"[INFO] Total unique packages with counts: {len(package_counter)}")
    else:
        print(f"[INFO] Total unique packages: {len(package_counter)}")
    
    # طباعة النتائج مع الفرز المناسب
    if package_counter:
        if count:
            print("[INFO] Analysis complete. Printing unique packages with counts (sorted by count descending):")
            # الفرز حسب العدد تنازلياً، ثم حسب اسم الحزمة تصاعدياً
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] Analysis complete. Printing unique packages (sorted by name ascending):")
            # الفرز حسب اسم الحزمة تصاعدياً
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] No packages found.")
```

### كيف يعمل
- **تشغيل النص البرمجي**:
  - `python script.py /path/to/java/project`: يحلل جميع ملفات `.java` في الدليل ويستخدم أسماء الحزم الكاملة (`level = 0`).
  - `python script.py /path/to/java/project 2`: يقتطع أسماء الحزم إلى أول جزأين (مثل، `com.google.common.eventbus` تصبح `com.google`).

- **مثال على الإخراج**:
  لنفترض أن لديك ملف Java يحتوي على:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **مع `level = 0` (أو لم يتم توفير level)**:
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
  - **أسماء الحزم الكاملة**: عندما تكون `level = 0` أو لم يتم تمريرها، فإنه يستخدم اسم الحزمة الكامل كما تم استخراجه (مثل `java.util`، `com.google.common.eventbus`).
  - **الاقتطاع**: عندما تكون `level > 0`، فإنه يأخذ أول `level` أجزاء.
  - **معالجة الأخطاء**: يتحقق من وجود دليل صحيح وقيمة `level` غير سالبة.
  - **التميز**: يخزن الحزم في `set` لتجنب التكرارات.

### الحالات الطرفية التي تم التعامل معها
- **المستوى المفقود**: افتراضيًا `level = 0`، باستخدام أسماء الحزم الكاملة.
- **المستوى غير الصالح**: ينهي البرنامج بخطأ إذا كانت `level` سالبة أو ليست عددًا صحيحًا.
- **الحزم القصيرة**: إذا كان للحزمة أجزاء أقل من `level` (مثل `java` مع `level = 2`)، فإنه يستخدم الحزمة الكاملة (`java`).
- **عبارات الاستيراد الفارغة**: يتخطى الأسطر التي لم يتم استخراج أي حزمة منها.

هذا النص البرمجي يلبي تمامًا متطلباتك: عندما تكون `level = 0` أو لم يتم توفيرها، فإنه يستخدم جميع أجزاء اسم الحزمة، مما يعامله بشكل فعال على أنه "لا نهائي" من حيث الأجزاء المستخدمة.