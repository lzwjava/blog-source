---
audio: true
lang: ar
layout: post
title: تحليل حزم Java في المشروع
translated: true
---

هنا نص Python الذي يحلل مجلدًا بشكل تكراري، ويجد جميع حزم Java المستخدمة في ملفات `.java`، ويزيل التكرار، ويقوم بقائمة جميع الحزم الفريدة المستخدمة في المشروع. يركز النص على ملفات `.java` فقط ويقوم بمعالجة المشاريع التي قد تحتوي على وحدات من خلال عبور جميع المجلدات الفرعية.

### النص Python:

```python
import os
import sys

def find_java_files(root_dir):
    """
    يبحث بشكل تكراري عن جميع ملفات .java في المجلد المحدد ومجلداته الفرعية.

    Args:
        root_dir (str): المجلد الجذر لبدء البحث منه.

    Yields:
        str: المسار الكامل لكل ملف .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    استخراج اسم الحزمة من بيان الاستيراد.

    يستخدم التقاليد التي تكون أسماء الحزم عادة بأحرف صغيرة، بينما تبدأ أسماء الفئات بأحرف كبيرة. بالنسبة للاستيرادات البرية (*)، تكون الحزمة الجزء قبل '*'.

    Args:
        import_statement (str): سطر البيان الاستيراد من ملف Java.

    Returns:
        str: اسم الحزمة، أو سلسلة فارغة إذا لم يتم تحديدها.
    """
    # إزالة 'import' و 'static' إذا كانت موجودة
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]

    # اتحاد الباقي و إزالة ';' النهائي
    import_path = ' '.join(parts).strip(';').strip()

    # تقسيم مسار الاستيراد بواسطة '.'
    identifiers = import_path.split('.')

    # العثور على الفهرس حيث يبدأ أول معرف بأحرف كبيرة أو هو '*'
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []

    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # التحقق من المعلمة السطرية للجلد الجذر
    if len(sys.argv) < 2:
        print("استخدام: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    packages = set()

    # عبور جميع ملفات .java في المجلد ومجلداته الفرعية
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:  # إضافة أسماء الحزم غير الفارغة فقط
                            packages.add(package)
        except Exception as e:
            print(f"تحذير: لم يمكن قراءة الملف {java_file}: {e}")
            continue

    # طباعة القائمة المفرغة من الحزم الفريدة
    for package in sorted(packages):
        print(package)
```

### كيفية استخدام النص:

1. احفظ النص في ملف، مثل `analyze_java_packages.py`.
2. قم بتشغيل النص من السطر الأوامر، تقديم مسار المجلد الجذر للمشروع Java:
   ```
   python analyze_java_packages.py /path/to/your/java/project
   ```
3. سيقوم النص بإخراج قائمة مرتبة من أسماء الحزم الفريدة التي تم استيرادها في ملفات `.java`.

### ما يفعله النص:

- **يجد ملفات `.java`:**
  - يستخدم `os.walk()` للعبور التكراري للمجلد ومجلداته الفرعية.
  - يحدد جميع الملفات التي تنتهي بـ `.java`.

- **يستخرج أسماء الحزم:**
  - يحلل كل ملف `.java` سطرًا بعد سطر.
  - يحدد السطور التي تبدأ بـ `import`.
  - يستخرج أسماء الحزم من بيانات الاستيراد، مع معالجة:
    - الاستيرادات العادية (مثل `import java.util.List;`).
    - الاستيرادات البرية (مثل `import java.util.*;`).
    - الاستيرادات الثابتة (مثل `import static java.util.Collections.sort;`).
  - يستخدم استدلالًا يعتمد على تقاليد Java:
    - أسماء الحزم عادة بأحرف صغيرة (مثل `java.util`).
    - أسماء الفئات تبدأ عادة بأحرف كبيرة (مثل `List`, `Collections`).
    - الاستيرادات البرية تنتهي بـ `*`.

- **يزيل التكرار:**
  - يجمع جميع أسماء الحزم في مجموعة لإزالة التكرار تلقائيًا.

- **يخرج النتائج:**
  - يحول المجموعة إلى قائمة مرتبة ويطبع كل اسم حزمة في سطر جديد.

### الافتراضات والتقييدات:

- **بيانات الاستيراد:**
  - يفترض أن بيانات الاستيراد في سطور منفصلة ولا تكون مدفونة في التعليقات أو الأسلوب.
  - يعالج كل من الاستيرادات العادية والاستيرادات الثابتة، بما في ذلك الاستيرادات البرية.

- **تقاليد التسمية:**
  - يعتمد على التقليد الذي تكون أسماء الحزم بأحرف صغيرة، واسم الفئة يبدأ بأحرف كبيرة.
  - قد لا يعالج بشكل صحيح التسمية غير القياسية (مثل أسماء الحزم بأحرف كبيرة)، ولكن هذا نادر في الممارسة.

- **تشفير الملف:**
  - يفترض أن ملفات `.java` مشفرة في UTF-8. قم بتعديل `encoding` إذا لزم الأمر.

- **معالجة الأخطاء:**
  - يتضمن معالجة الأخطاء الأساسية للملفات غير القابلة للقراءة، طباعة تحذير و الاستمرار.

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

عند تشغيل النص سيخرج:
```
com.example.myapp
java.lang
java.util
```

هذا يدرج جميع الحزم الفريدة المستوردة في المشروع، مرتبة أبجديًا.

### الملاحظات:

- يركز النص على الحزم المستوردة عبر بيانات الاستيراد، والتي تمثل الحزم الخارجية والداخلية التي يستخدمها المشروع.
- لا يشمل بيانات الحزم في ملفات `.java` نفسها (مثل `package com.mycompany.myapp;`)، لأن هذه تعرّف الحزم التي تنتمي إليها الملفات، وليس الحزم التي تستخدمها.
- نظرًا لأن المشروع قد يحتوي على وحدات، يقوم النص بعمل تحليل تكراري لجميع المجلدات الفرعية لضمان معالجة جميع ملفات `.java`.