---
audio: false
lang: ar
layout: post
title: تحليل الاعتماديات في جاڤا
translated: true
---

### نص Python الذي يجرى مسح جميع ملفات `.java` في مشروع، ويحلل اعتماداتها بناءً على بيانات الاستيراد، ويخرج مخطط الاعتمادات في صيغة DOT ك"نص الاعتمادات." يركز هذا النص على الاعتمادات الداخلية بين الفئات داخل المشروع، ويوفر تمثيلًا واضحًا يمكن رؤيته باستخدام أدوات مثل Graphviz.

### نظرة عامة على النص
يجرى النص:
1. **مسح دليل المشروع** بشكل متكرر لتحديد جميع ملفات `.java`.
2. **تحليل الاعتمادات** من خلال استخراج بيانات الحزمة والاستيراد من كل ملف `.java`.
3. **إخراج نص الاعتمادات** في صيغة DOT، يوضح الحواف الموجهة بين الفئات حيث تستورد فئة أخرى داخل المشروع.

هنا النص الكامل:

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
        print(f"تحذير: لم يمكن قراءة {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    استخراج استيرادات الفئة المحددة من ملف .java، مع استبعاد استيرادات البعد.

    Args:
        file_path (str): مسار الملف .java.

    Returns:
        list: قائمة بأسماء الفئات المستوردة بالكامل.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # استبعاد استيرادات البعد (مثل استيراد java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"تحذير: لم يمكن قراءة {file_path}: {e}")
    return imports

if __name__ == '__main__':
    # التحقق من وجود حجة سطر الأوامر
    if len(sys.argv) != 2:
        print("استخدام: python script.py <دليل الجذر>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_classes = set()

    # المرور الأول: جمع جميع أسماء الفئات الكاملة في المشروع
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # تخزين الاعتمادات: فئة -> مجموعة الفئات التي تعتمد عليها
    dependencies = defaultdict(set)

    # المرور الثاني: تحليل الاعتمادات بناءً على استيرادات محددة
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # فقط تضمين الاعتمادات على الفئات داخل المشروع
                        # استبعاد الاعتمادات الذاتية
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # إخراج مخطط الاعتمادات في صيغة DOT
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')
```

### كيفية عمله
#### 1. **دخول سطر الأوامر**
- يتوقع النص حجة واحدة: دليل الجذر لمشروع Java.
- مثال الاستخدام: `python script.py /path/to/project`
- إذا لم يتم توفير حجة، فإنه يطبع تعليمات الاستخدام ويخرج.

#### 2. **إيجاد ملفات `.java`**
- يستخدم `os.walk()` لتجوال الدليل المحدد بشكل متكرر وتحديد جميع الملفات التي تنتهي بـ `.java`.

#### 3. **استخراج معلومات الفئة**
- **استخراج الحزمة**: تقوم وظيفة `get_package` بقراءة كل ملف `.java` واستخدام تعبير عادي (`^\s*package\s+([\w.]+);` ) لتحديد بيان الحزمة (مثل `package com.mycompany.myproject;`).
  - ترجع `None` إذا لم يتم العثور على حزمة أو إذا لم يمكن قراءة الملف.
- **اسم الفئة**: يتوقع أن اسم الفئة يتطابق مع اسم الملف (مثل `MyClass.java` يحدد `MyClass`).
- **الاسم الكامل**: يجمع بين الحزمة واسم الفئة (مثل `com.mycompany.myproject.MyClass`).

#### 4. **جمع جميع الفئات**
- في المرور الأول، يبني مجموعة من جميع أسماء الفئات الكاملة في المشروع لمشاهدة سريعة لاحقًا.

#### 5. **تحليل الاعتمادات**
- **استخراج الاستيرادات**: تقوم وظيفة `get_specific_imports` باستخراج بيانات الاستيراد باستخدام تعبير عادي (`^\s*import\s+([\w.]+);`)، مع استبعاد استيرادات البعد (مثل `import java.util.*;`).
  - مثال: من `import com.mycompany.myproject.utils.Helper;`، يستخرج `com.mycompany.myproject.utils.Helper`.
- **خريطة الاعتمادات**: لكل ملف `.java`:
  - يحصل على اسم الفئة الكامل.
  - يحدد استيرادات محددة.
  - إذا كانت فئة مستوردة في مجموعة الفئات للمشروع ولا هي الفئة نفسها، يضيف اعتمادية.

#### 6. **إخراج نص الاعتمادات**
- يخرج مخططًا موجهًا في صيغة DOT:
  - يبدأ بـ `digraph G {`.
  - لكل فئة مع اعتمادات، يطبع حواف مثل `"ClassA" -> "ClassB";`.
  - ينتهي بـ `}`.
- الفئات و الاعتمادات مرتبتان للحصول على إخراج مستقر.
- مثال على الإخراج:
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### مثال على الاستخدام
1. احفظ النص باسم `analyze_deps.py`.
2. قم بتشغيله:
   ```bash
   python analyze_deps.py /path/to/java/project
   ```
3. اعرض الإخراج إلى ملف:
   ```bash
   python analyze_deps.py /path/to/java/project > dependencies.dot
   ```
4. قم بالترجمة مع Graphviz:
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   هذا يخلق صورة PNG تظهر مخطط الاعتمادات.

### الافتراضات والحدود
- **فئة عامة واحدة لكل ملف**: يتوقع أن يحتوي كل ملف `.java` على فئة عامة واحدة تحمل اسم الملف، وفقًا لمعيار Java.
- **اعتمادات استيراد**: يعتبر فقط الاعتمادات التي تشير إليها بيانات الاستيراد المحددة (مثل `import com.example.SomeClass;`)، مع تجاهل استيرادات البعد (`import com.example.*;`) و مراجع الحزمة نفسها (التي لا تتطلب استيرادات).
- **التفكير الداخلي**: يتبع فقط الاعتمادات بين الفئات داخل المشروع، مع تجاهل المكتبات الخارجية.
- **تحليل أساسي**: يستخدم تعبيرات عادية للسهولة، والتي قد تفوت حالات حافة (مثل الاستيرادات داخل التعليقات). يمكن أن يكون تحليل Java الكامل أكثر قوة ولكن معقدًا.

### التخصيص
- **صيغة الإخراج**: قم بتعديل بيانات الطباعة لتغيير صيغة نص الاعتمادات (مثل قائمة بسيطة بدلاً من DOT).
- **معالجة الأخطاء**: تم تحسينها باستخدام كتلة try-except لتخطي الملفات غير القابلة للقراءة بشكل رقيق.
- **المنطقة**: يمكن توسيعها لتشمل الاعتمادات الخارجية أو الاعتمادات داخل الحزمة مع تحليل أعمق للكود.

يوفر هذا النص نقطة بداية عملية لتحليل الاعتمادات، مناسبة لفهم بنية مشروع Java من خلال علاقاته الداخلية بين الفئات.