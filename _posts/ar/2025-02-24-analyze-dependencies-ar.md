---
audio: false
generated: true
lang: ar
layout: post
title: تحليل الاعتماديات في جاڤا
translated: true
---

للتعامل مع استفسارك، سأعدل النص البرمجي المقدم لولادة مخطط التبعية لصفوف Java، حيث يتم تجميع التبعيات حسب مستوى محدد من هرمية الحزم. على سبيل المثال، إذا كان `level=1`، يتم تجميع الحزم في المستوى الأعلى (مثل "org")، وإذا كان `level=2`، يتم تجميعها في المستوى الثاني (مثل "org.springframework"). وهذا يعني أن قبل تحليل التبعيات، نجمع الصفوف في مجموعات بناءً على أول `level` أجزاء من أسماء الحزم، وسينظر المخطط في التبعيات بين هذه المجموعات بدلاً من الصفوف الفردية.

أدناه النص البرمجي المعدل، يليه شرح التغييرات وكيفية تلبية متطلباتك.

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
    استخراج استيرادات الصفوف المحددة من ملف .java، مع استبعاد استيرادات الجملة.

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
                    # استبعاد استيرادات الجملة (مثل استيراد java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"تحذير: لم يتم قراءة {file_path}: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    الحصول على مجموعة الحزمة بناءً على أول 'level' أجزاء من اسم الحزمة.

    Args:
        full_class_name (str): اسم الصف الكامل (مثل "org.springframework.boot.App").
        level (int): عدد مستويات الحزمة التي يجب تضمينها (مثل 1 لـ "org"، 2 لـ "org.springframework").

    Returns:
        str: مجموعة الحزمة (مثل "org" أو "org.springframework").
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # استخراج الحزمة، مع استبعاد اسم الصف
    parts = package.split('.')
    if len(parts) <= level:
        return package  # استخدام الحزمة الكاملة إذا كانت لها أقل من أو تساوي عدد أجزاء المستوى
    else:
        return '.'.join(parts[:level])  # استخدام أول 'level' أجزاء

if __name__ == '__main__':
    # التحقق من وجود متغيرات السطر الأوامر: root_directory و level
    if len(sys.argv) != 3:
        print("استخدام: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("خطأ: يجب أن يكون المستوى عدد صحيح موجب")
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

1. **متغيرات السطر الأوامر**:
   - **الأصلية**: `python script.py <root_directory>`
   - **المعدلة**: `python script.py <root_directory> <level>`
   - تم إضافة دعم لمتغير السطر الأوامر الثاني، `level`، الذي يحدد مستوى هرمية الحزم. يتحقق النص البرمجي من وجود متغيرين بالضبط وتأكد من أن `level` هو عدد صحيح موجب.

2. **دالة جديدة: `get_package_group`**:
   - تم إضافة دالة لحساب مجموعة الحزمة لصف بناءً على `level` المحدد.
   - بالنسبة لاسم الصف الكامل (مثل "org.springframework.boot.App")، يستخرج الحزمة ("org.springframework.boot")، ويقسمها إلى أجزاء ("org", "springframework", "boot")، ويأخذ أول `level` أجزاء:
     - إذا كان `level=1`: يعيد "org".
     - إذا كان `level=2`: يعيد "org.springframework".
     - إذا كانت الحزمة لديها أقل من عدد أجزاء `level` (مثل "com.example" مع `level=3`), يعيد الحزمة الكاملة ("com.example").

3. **تجميع التبعيات**:
   - **الأصلية**: استخدم `defaultdict(set)` لتخزين التبعيات بين الصفوف الفردية.
   - **المعدلة**: يستخدم `set` (`group_dependencies`) لتخزين حواف الموجهة بين مجموعات الحزم كزواج `(from_group, to_group)`.
   - لكل صف:
     - يحسب مجموعته (`importer_group`) باستخدام `get_package_group`.
     - لكل استيراد محدد داخل المشروع (`imp in all_classes`) ولا يكون الصف نفسه (`imp != full_class_name`):
       - يحسب مجموعة الصف المستوردة (`imported_group`).
       - إذا كانت المجموعات مختلفة (`imported_group != importer_group`), يضيف حافة إلى `group_dependencies`.
   - يضمن `set` الفردية، لذلك تؤدي التبعيات المتعددة بين نفس المجموعات إلى حافة واحدة.

4. **خروج DOT**:
   - **الأصلية**: طباعة حواف بين الصفوف الفردية (مثل "org.springframework.boot.App" -> "org.apache.commons.IOUtils").
   - **المعدلة**: طباعة حواف بين مجموعات الحزم (مثل "org.springframework" -> "org.apache" لـ `level=2`).
   - حواف مرتبة للحصول على خروج مكرر.

### كيفية تلبية متطلباتك

- **دعم المستويات**: الآن يقبل النص البرمجي متغير `level` لتجميع الحزم قبل تحليل التبعيات.
- **المستوى = 1**: تجميع جميع الصفوف حسب الحزمة الأعلى (مثل "org"). على سبيل المثال، "org.springframework.boot.App" و"org.apache.commons.IOUtils" كلاهما في مجموعة "org"، لذلك لا تظهر استيرادات بينهما داخل "org" كحواف.
- **المستوى = 2**: تجميع الصفوف حسب أول مستويين من الحزم (مثل "org.springframework"). على سبيل المثال، استيراد من "org.springframework.boot.App" إلى "org.apache.commons.IOUtils" يخلق حافة من "org.springframework" إلى "org.apache".
- **تجميع الحزم قبل تحليل التبعيات**: يحدد النص البرمجي مجموعة الحزمة لكل صف بناءً على `level` قبل تحليل استيراداته، مما يضمن أن التبعيات بين المجموعات، وليس الصفوف الفردية.
- **مثال التوافق**: بالنسبة لحافة المثال:
  - الأصلية: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - مع `level=2`: كلاهما في "org.springframework"، لذلك لا يتم إضافة حافة (مجموعة واحدة).
  - مع `level=3`: "org.springframework.boot.web" -> "org.springframework.boot.convert"، إضافة حافة بين هذه المجموعات المختلفة.

### أمثلة الاستخدام

- **الامر**: `python script.py /path/to/project 1`
  - المجموعات: "org", "com"، إلخ.
  - قد يتضمن الخرج: `"org" -> "com"` إذا استورد صف في حزمة "org" صف في حزمة "com".

- **الامر**: `python script.py /path/to/project 2`
  - المجموعات: "org.springframework", "org.apache"، إلخ.
  - قد يتضمن الخرج: `"org.springframework" -> "org.apache"`.

### ملاحظات

- يظل النص البرمجي على سلوكه الأصلي من تضمين التبعيات داخل المشروع فقط (استيرادات داخل `all_classes`) واستبعاد استيرادات الجملة والتبعيات الذاتية.
- يتم تجاهل الصفوف بدون إعلان حزمة، موافقًا مع النص البرمجي الأصلي.
- الخرج هو مخطط موجه في صيغة DOT، يمكن مشاهدته باستخدام أدوات مثل Graphviz.

يجب أن يرضي هذا النص البرمجي المعدل طلبك لتجميع التبعيات حسب مستوى هرمية الحزم.