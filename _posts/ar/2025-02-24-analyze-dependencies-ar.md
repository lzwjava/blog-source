---
audio: false
generated: true
lang: ar
layout: post
title: تحليل تبعيات جافا
translated: true
type: note
---

لمعالجة استفسارك، سأقوم بتعديل البرنامج النصي Python المقدم لإنشاء رسم بياني للتبعيات لفئات Java، حيث يتم تجميع التبعيات حسب "مستوى" محدد من التسلسل الهرمي للحزمة. على سبيل المثال، إذا كان `level=1`، يتم تجميع الحزم على المستوى الأعلى (مثل "org")، وإذا كان `level=2`، يتم تجميعها على المستوى الثاني (مثل "org.springframework"). هذا يعني أنه قبل تحليل التبعيات، نقوم بتجميع الفئات في مجموعات بناءً على الأجزاء `level` الأولى من أسماء حزمها، وسيعرض الرسم البياني التبعيات بين هذه المجموعات بدلاً من الفئات الفردية.

أدناه البرنامج النصي المعدل، يليه شرح للتغييرات وكيفية تلبية المتطلبات.

### البرنامج النصي المعدل

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    استخراج اسم الحزمة من ملف .java.

    الوسائط:
        file_path (str): المسار إلى ملف .java.

    الإرجاع:
        str: اسم الحزمة، أو None إذا لم يتم العثور عليها.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    استخراج استيرادات الفئات المحددة من ملف .java، باستثناء الاستيرادات العامة (wildcard).

    الوسائط:
        file_path (str): المسار إلى ملف .java.

    الإرجاع:
        list: قائمة بالأسماء المؤهلة الكاملة للفئات المستوردة.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # استبعاد الاستيرادات العامة (مثل import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    الحصول على مجموعة الحزمة بناءً على الأجزاء 'level' الأولى من اسم الحزمة.

    الوسائط:
        full_class_name (str): الاسم المؤهل الكامل للفئة (مثال: "org.springframework.boot.App").
        level (int): عدد مستويات الحزمة المطلوب تضمينها (مثال: 1 لـ "org"، 2 لـ "org.springframework").

    الإرجاع:
        str: مجموعة الحزمة (مثال: "org" أو "org.springframework").
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # استخراج الحزمة، باستثناء اسم الفئة
    parts = package.split('.')
    if len(parts) <= level:
        return package  # استخدام الحزمة الكاملة إذا كان عدد أجزائها أقل من أو يساوي المستوى
    else:
        return '.'.join(parts[:level])  # استخدام الأجزاء 'level' الأولى

if __name__ == '__main__':
    # التحقق من وسائط سطر الأوامر: root_directory و level
    if len(sys.argv) != 3:
        print("Usage: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("Error: level must be a positive integer")
        sys.exit(1)

    all_classes = set()

    # المسح الأول: جمع جميع الأسماء المؤهلة الكاملة للفئات في المشروع
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # تخزين التبعيات بين مجموعات الحزم
    group_dependencies = set()

    # المسح الثاني: تحليل التبعيات بناءً على مجموعات الحزم
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    importer_group = get_package_group(full_class_name, level)
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # تضمين التبعيات على الفئات داخل المشروع فقط
                        # استبعاد التبعيات الذاتية
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # إخراج الرسم البياني للتبعيات بتنسيق DOT
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### شرح التغييرات

1. **وسائط سطر الأوامر**:
   - **الأصلي**: `python script.py <root_directory>`
   - **المعدل**: `python script.py <root_directory> <level>`
   - تمت إضافة دعم لوسيطة ثانية، `level`، والتي تحدد مستوى التسلسل الهرمي للحزمة. يتحقق البرنامج النصي من توفير وسيطتين بالضبط وأن `level` هو عدد صحيح موجب.

2. **دالة جديدة: `get_package_group`**:
   - تمت إضافة دالة لحساب مجموعة الحزمة لفئة بناءً على `level` المحدد.
   - بالنسبة لاسم فئة مؤهل بالكامل (مثال: "org.springframework.boot.App")، تستخرج الحزمة ("org.springframework.boot")، وتقسمها إلى أجزاء ("org", "springframework", "boot")، وتأخذ الأجزاء `level` الأولى:
     - إذا كان `level=1`: تُرجع "org".
     - إذا كان `level=2`: تُرجع "org.springframework".
     - إذا كانت الحزمة تحتوي على أجزاء أقل من `level` (مثال: "com.example" مع `level=3`)، فإنها تُرجع الحزمة الكاملة ("com.example").

3. **تجميع التبعيات**:
   - **الأصلي**: استخدام `defaultdict(set)` لتخزين التبعيات بين الفئات الفردية.
   - **المعدل**: استخدام `set` (`group_dependencies`) لتخزين الحواف الموجهة بين مجموعات الحزم كـ tuples `(from_group, to_group)`.
   - لكل فئة:
     - حساب مجموعة الحزمة الخاصة بها (`importer_group`) باستخدام `get_package_group`.
     - لكل استيراد محدد موجود داخل المشروع (`imp in all_classes`) وليس نفس الفئة (`imp != full_class_name`):
       - حساب مجموعة الحزمة للفئة المستوردة (`imported_group`).
       - إذا اختلفت المجموعات (`imported_group != importer_group`)، يتم إضافة حافة إلى `group_dependencies`.
   - يضمن `set` التفرد، بحيث تؤدي التبعيات المتعددة بين نفس المجموعات إلى حافة واحدة.

4. **إخراج DOT**:
   - **الأصلي**: طباعة الحواف بين الفئات الفردية (مثال: "org.springframework.boot.App" -> "org.apache.commons.IOUtils").
   - **المعدل**: طباعة الحواف بين مجموعات الحزم (مثال: "org.springframework" -> "org.apache" لـ `level=2`).
   - يتم فرز الحواف لإخراج متسق.

### كيف يلبي المتطلبات

- **الدعم للمستويات**: يقبل البرنامج النصي الآن معامل `level` لتجميع الحزم قبل تحليل التبعيات.
- **المستوى = 1**: تجميع جميع الفئات حسب حزمة المستوى الأعلى (مثل "org"). على سبيل المثال، "org.springframework.boot.App" و "org.apache.commons.IOUtils" كلاهما ينتميان إلى مجموعة "org"، لذلك لا تظهر الاستيرادات بينهما داخل "org" كحواف.
- **المستوى = 2**: تجميع الفئات حسب أول مستويين من الحزمة (مثل "org.springframework"). على سبيل المثال، استيراد من "org.springframework.boot.App" إلى "org.apache.commons.IOUtils" ينشئ حافة من "org.springframework" إلى "org.apache".
- **تجميع الحزم قبل تحليل التبعيات**: يحدد البرنامج النصي مجموعة الحزمة لكل فئة بناءً على `level` قبل تحليل استيراداتها، مما يضمن أن التبعيات تكون بين المجموعات، وليس الفئات الفردية.
- **الامتثال للمثال**: بالنسبة لحافتك المثال:
  - الأصلية: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - مع `level=2`: كلتا الفئتين في "org.springframework"، لذلك لا تتم إضافة حافة (نفس المجموعة).
  - مع `level=3`: "org.springframework.boot.web" -> "org.springframework.boot.convert"، مضيفًا حافة بين هاتين المجموعتين المتميزتين.

### أمثلة الاستخدام

- **الأمر**: `python script.py /path/to/project 1`
  - المجموعات: "org", "com"، إلخ.
  - قد يتضمن الإخراج: `"org" -> "com"` إذا قامت فئة في حزمة "org" باستيراد فئة في حزمة "com".

- **الأمر**: `python script.py /path/to/project 2`
  - المجموعات: "org.springframework", "org.apache"، إلخ.
  - قد يتضمن الإخراج: `"org.springframework" -> "org.apache"`.

### ملاحظات

- يحافظ البرنامج النصي على السلوك الأصلي المتمثل في تضمين تبعيات المشروع الداخلية فقط (الاستيرادات داخل `all_classes`) واستبعاد الاستيرادات العامة والتبعيات الذاتية.
- يتم تخطي الفئات بدون تعريف حزمة، بما يتوافق مع البرنامج النصي الأصلي.
- الإخراج هو رسم بياني موجه بتنسيق DOT، يمكن عرضه بأدوات مثل Graphviz.

يجب أن يلبي هذا البرنامج النصي المعدل طلبك بالكامل لتجميع التبعيات حسب مستوى التسلسل الهرمي للحزمة.