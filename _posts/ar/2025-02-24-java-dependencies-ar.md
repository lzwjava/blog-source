---
audio: true
lang: ar
layout: post
title: تحليل الاعتماديات في جاڤا
translated: true
---

للتعامل مع استفسارك، سأعدل النص البرمجي المقدم لولادة مخطط التبعية لصفوف Java، حيث يتم تجميع التبعيات حسب مستوى محدد من هرمية الحزم. على سبيل المثال، إذا كان `level=1`، يتم تجميع الحزم في المستوى الأعلى (على سبيل المثال، "org")، وإذا كان `level=2`، يتم تجميعها في المستوى الثاني (على سبيل المثال، "org.springframework"). وهذا يعني أن قبل تحليل التبعيات، نجمع الصفوف في مجموعات بناءً على أول `level` أجزاء من أسماء الحزم، وسينظر المخطط في التبعيات بين هذه المجموعات بدلاً من الصفوف الفردية.

أدناه النص البرمجي المعدل، يليه شرح التغييرات وكيفية تحقيق متطلباتك.

### النص البرمجي المعدل

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    استخراج اسم الحزمة من ملف .java.

    Args:
        file_path (str): مسار الملف .java.

    Returns:
        str: اسم الحزمة، أو None إذا لم يتم العثور عليه.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"تحذير: لم يتم قراءة {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    استخراج استيرادات الصفوف المحددة من ملف .java، مع استبعاد استيرادات البعد.

    Args:
        file_path (str): مسار الملف .java.

    Returns:
        list: قائمة بأسماء الصفوف المستوردة بالكامل.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # استبعاد استيرادات البعد (على سبيل المثال، import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"تحذير: لم يتم قراءة {file_path}: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    الحصول على مجموعة الحزم بناءً على أول 'level' أجزاء من اسم الحزمة.

    Args:
        full_class_name (str): اسم الصف الكامل (على سبيل المثال، "org.springframework.boot.App").
        level (int): عدد مستويات الحزم التي يجب تضمينها (على سبيل المثال، 1 لـ "org"، 2 لـ "org.springframework").

    Returns:
        str: مجموعة الحزم (على سبيل المثال، "org" أو "org.springframework").
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # استخراج الحزمة، مع استبعاد اسم الصف
    parts = package.split('.')
    if len(parts) <= level:
        return package  # استخدام الحزمة الكاملة إذا كانت لها أجزاء أقل أو مساوية لـ level
    else:
        return '.'.join(parts[:level])  # استخدام أول 'level' أجزاء

if __name__ == '__main__':
    # التحقق من وجود حجج السطر الأوامر: root_directory و level
    if len(sys.argv) != 3:
        print("استخدام: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("خطأ: يجب أن يكون level عدد صحيح موجب")
        sys.exit(1)

    all_classes = set()

    # المرور الأول: جمع جميع أسماء الصفوف الكاملة في المشروع
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

    # المرور الثاني: تحليل التبعيات بناءً على مجموعات الحزم
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
                        # فقط تضمين التبعيات على الصفوف داخل المشروع
                        # استبعاد التبعيات الذاتية
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # إخراج المخطط التبعي في صيغة DOT
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### شرح التغييرات

1. **حجج السطر الأوامر**:
   - **الأصلية**: `python script.py <root_directory>`
   - **المعدلة**: `python script.py <root_directory> <level>`
   - أضيف دعم للحجج الثانية، `level`، التي تحدد مستوى هرمية الحزم. يتحقق النص البرمجي من وجود حججتين بالضبط وتأكد أن `level` عدد صحيح موجب.

2. **دالة جديدة: `get_package_group`**:
   - أضيفت دالة لحساب مجموعة الحزم لصف بناءً على `level` المحدد.
   - لاسم الصف الكامل (على سبيل المثال، "org.springframework.boot.App")، يستخرج الحزمة ("org.springframework.boot")، ويقسمها إلى أجزاء ("org", "springframework", "boot")، ويأخذ أول `level` أجزاء:
     - إذا كان `level=1`: يعيد "org".
     - إذا كان `level=2`: يعيد "org.springframework".
     - إذا كانت الحزمة لها أجزاء أقل من `level` (على سبيل المثال، "com.example" مع `level=3`), يعيد الحزمة الكاملة ("com.example").

3. **تجميع التبعيات**:
   - **الأصلية**: استخدم `defaultdict(set)` لتخزين التبعيات بين الصفوف الفردية.
   - **المعدلة**: يستخدم `set` (`group_dependencies`) لتخزين الحواف الموجهة بين مجموعات الحزم كزواج `(from_group, to_group)`.
   - لكل صف:
     - يحسب مجموعته (`importer_group`) باستخدام `get_package_group`.
     - لكل استيراد محدد داخل المشروع (`imp in all_classes`) وليس الصف نفسه (`imp != full_class_name`):
       - يحسب مجموعة الصف المستورد (`imported_group`).
       - إذا كانت المجموعات مختلفة (`imported_group != importer_group`), يضيف حافة إلى `group_dependencies`.
   - يضمن `set` الفردية، لذا يؤدي التبعيات المتعددة بين نفس المجموعات إلى حافة واحدة.

4. **إخراج DOT**:
   - **الأصلية**: طباعة الحواف بين الصفوف الفردية (على سبيل المثال، "org.springframework.boot.App" -> "org.apache.commons.IOUtils").
   - **المعدلة**: طباعة الحواف بين مجموعات الحزم (على سبيل المثال، "org.springframework" -> "org.apache" لـ `level=2`).
   - الحواف مرتبة للحصول على إخراج مستقر.

### كيفية تحقيق متطلباتك

- **دعم المستويات**: الآن يقبل النص البرمجي حجة `level` لتجميع الحزم قبل تحليل التبعيات.
- **المستوى = 1**: تجميع جميع الصفوف حسب الحزمة الأعلى (على سبيل المثال، "org"). على سبيل المثال، "org.springframework.boot.App" و"org.apache.commons.IOUtils" كلاهما في مجموعة "org"، لذا لا تظهر استيرادات بينهما داخل "org" كحواف.
- **المستوى = 2**: تجميع الصفوف حسب أول الحزمين (على سبيل المثال، "org.springframework"). على سبيل المثال، استيراد من "org.springframework.boot.App" إلى "org.apache.commons.IOUtils" يخلق حافة من "org.springframework" إلى "org.apache".
- **تجميع الحزم قبل تحليل التبعيات**: يحدد النص البرمجي مجموعة الحزمة لكل صف بناءً على `level` قبل تحليل استيراداته، مما يضمن أن التبعيات بين المجموعات، وليس الصفوف الفردية.
- **التوافق مع المثال**: لمثال الحافة:
  - الأصلية: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - مع `level=2`: كلاهما في "org.springframework"، لذا لا يضيف حافة (مجموعة واحدة).
  - مع `level=3`: "org.springframework.boot.web" -> "org.springframework.boot.convert"، يضيف حافة بين هذه المجموعات المختلفة.

### أمثلة الاستخدام

- **الامر**: `python script.py /path/to/project 1`
  - المجموعات: "org", "com"، إلخ.
  - قد يتضمن الإخراج: `"org" -> "com"` إذا استورد صف في حزمة "org" صف في حزمة "com".

- **الامر**: `python script.py /path/to/project 2`
  - المجموعات: "org.springframework", "org.apache"، إلخ.
  - قد يتضمن الإخراج: `"org.springframework" -> "org.apache"`.

### الملاحظات

- يظل النص البرمجي على سلوكه الأصلي من تضمين التبعيات داخل المشروع فقط (استيرادات داخل `all_classes`) واستبعاد استيرادات البعد والتبعيات الذاتية.
- يتم تجاهل الصفوف بدون إعلان حزمة، موافقًا مع النص البرمجي الأصلي.
- الإخراج هو مخطط موجه في صيغة DOT، يمكن مشاهدته باستخدام أدوات مثل Graphviz.

يجب أن يفي هذا النص البرمجي المعدل بالكامل بطلبك لتجميع التبعيات حسب مستوى هرمية الحزم.