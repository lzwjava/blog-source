---
audio: true
lang: ar
layout: post
title: تحليل حزم Java في المشروع
translated: true
---

هنا هو نص Python الذي يحلل مجلدًا بشكل تكراري، ويجد جميع حزم Java المستخدمة في ملفات `.java`، ويزيل التكرار، ويقوم بفرز جميع الحزم الفريدة المستخدمة في المشروع. يركز النص على ملفات `.java` فقط ويقوم بمعالجة المشاريع التي قد تحتوي على وحدات عن طريق عبور جميع المجلدات الفرعية.

### نص Python:

```python
import os
import sys

def find_java_files(root_dir):
    """
    يحدد ملفات .java في المجلد المحدد ومجلداته الفرعية بشكل تكراري.

    Args:
        root_dir (str): المجلد الجذر لبدء البحث من.

    Yields:
        str: المسار الكامل لكل ملف .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"[INFO] دخول المجلد: {dirpath}")
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    استخراج اسم الحزمة من بيان الاستيراد.

    يستخدم التقاليد التي تكون أسماء الحزم بأحرف صغيرة، بينما تبدأ أسماء الفئات بأحرف كبيرة. يدعم الاستيراد الجلي.

    Args:
        import_statement (str): سطر البيان الاستيراد من ملف Java.

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
    # التحقق من توفر المجلد
    if len(sys.argv) < 2:
        print("استخدام: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]

    # التحقق من وجود المجلد
    if not os.path.isdir(root_dir):
        print(f"[ERROR] المسار المحدد ليس مجلدًا: {root_dir}")
        sys.exit(1)

    # تسجيل بداية التحليل
    print(f"[INFO] بدء تحليل المجلد: {root_dir}")

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
                            packages.add(package)
            total_files += 1
        except Exception as e:
            print(f"[ERROR] لم يمكن قراءة الملف {java_file}: {e}")
            error_files += 1
            continue

    # طباعة الملخص
    print(f"[INFO] إجمالي ملفات Java المحاولة: {total_files + error_files}")
    print(f"[INFO] تم معالجة: {total_files}")
    print(f"[INFO] ملفات مع أخطاء: {error_files}")
    print(f"[INFO] إجمالي الحزم الفريدة التي تم العثور عليها: {len(packages)}")

    # طباعة النتائج
    if packages:
        print("[INFO] انتهى التحليل. طباعة الحزم الفريدة:")
        for package in sorted(packages):
            print(package)
    else:
        print("[INFO] لم يتم العثور على حزم.")
```

### كيفية استخدام النص:

1. احفظ النص في ملف، مثل `analyze_java_packages.py`.
2. قم بتشغيل النص من سطر الأوامر، وتوفير مسار المجلد الجذر للمشروع Java:
   ```
   python analyze_java_packages.py /path/to/your/java/project
   ```
3. سيقوم النص بإخراج قائمة مرتبة من أسماء الحزم الفريدة التي يتم استيرادها في ملفات `.java`.

### ما يفعله النص:

- **يحدد ملفات `.java`:**
  - يستخدم `os.walk()` لتجوال المجلد ومجلداته الفرعية بشكل تكراري.
  - يحدد جميع الملفات التي تنتهي بـ `.java`.

- **يستخرج أسماء الحزم:**
  - يحلل كل ملف `.java` سطرًا سطرًا.
  - يحدد السطور التي تبدأ بـ `import`.
  - يستخرج أسماء الحزم من بيانات الاستيراد، يدعم:
    - الاستيراد العادي (مثل `import java.util.List;`).
    - الاستيراد الجلي (مثل `import java.util.*;`).
    - الاستيراد الثابت (مثل `import static java.util.Collections.sort;`).
  - يستخدم استدلالًا يعتمد على تقاليد تسمية Java:
    - أسماء الحزم عادة بأحرف صغيرة (مثل `java.util`).
    - أسماء الفئات تبدأ بأحرف كبيرة (مثل `List`, `Collections`).
    - الاستيراد الجلي ينتهي بـ `*`.

- **يزيل التكرار:**
  - يجمع جميع أسماء الحزم في مجموعة لتزيل التكرار تلقائيًا.

- **يخرج النتائج:**
  - يحول المجموعة إلى قائمة مرتبة ويطبع كل اسم حزمة في سطر جديد.

### الافتراضات والتقييدات:

- **بيانات الاستيراد:**
  - يفترض أن بيانات الاستيراد في سطور منفصلة ولا تكون محاطة بالتعليقات أو الأوساط.
  - يدعم الاستيراد العادي والاستيراد الثابت، بما في ذلك الاستيراد الجلي.

- **تقاليد التسمية:**
  - يعتمد على التقاليد التي تكون أسماء الحزم بأحرف صغيرة، وأسماء الفئات تبدأ بأحرف كبيرة.
  - قد لا يدعم التسمية غير القياسية (مثل أسماء الحزم بأحرف كبيرة)، ولكن هذا نادر في الممارسة.

- **تشفير الملف:**
  - يفترض أن ملفات `.java` مشفرة في UTF-8. قم بتعديل `encoding` إذا لزم الأمر.

- **معالجة الأخطاء:**
  - يتضمن معالجة الأخطاء الأساسية للملفات غير القابلة للقراءة، ويطبع تحذيرًا ويستمر.

### المثال:

إذا كان مشروعك Java يحتوي على الملفات `.java` التالية:

- **File1.java:**
  ```java
  import java.util.List;
  import java.util.*;
  import java.lang.String;
  ```

- **File2.java:**
  ```java
  import java.util.Collections;
  import static java.util.Collections.sort;
  import com.example.myapp.*;
  ```

عند تشغيل النص، سيخرج:
```
com.example.myapp
java.lang
java.util
```

يستعرض هذا جميع الحزم الفريدة المستوردة في المشروع، مرتبة أبجديًا.

### الملاحظات:

- يركز النص على الحزم المستوردة عبر بيانات الاستيراد، والتي تمثل الحزم الخارجية والداخلية التي يستخدمها المشروع.
- لا يشمل بيانات الحزم في ملفات `.java` نفسها (مثل `package com.mycompany.myapp;`)، حيث أن هذه تعرّف الحزم التي ينتمي إليها الملفات، وليس الحزم التي تستخدمها.
- نظرًا لأن المشروع قد يحتوي على وحدات، يقوم النص بتحليل جميع المجلدات الفرعية بشكل تكراري لضمان معالجة جميع ملفات `.java`.