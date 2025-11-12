---
audio: false
generated: true
lang: ar
layout: post
title: تحليل ملفات بوم لمافن
translated: true
type: note
---

لمعالجة استفسارك، سأقدم حلاً لإنشاء رسم بياني للتبعيات بتنسيق DOT من خلال العثور بشكل متكرر على جميع ملفات `pom.xml` في دليل وتحليل تبعياتها، دون افتراض هيكل ثابت لمشروع Maven متعدد الوحدات النمطية مثل الموجود في المثال (`project/module1/pom.xml`، إلخ). سيركز النص البرمجي على جمع جميع ملفات `pom.xml` أولاً، ثم تحليلها لتحديد تبعيات الوحدات النمطية وإخراج الرسم البياني.

---

## نظرة عامة على الحل

إليك ما سيفعله النص البرمجي:
1. **جمع ملفات `pom.xml` بشكل متكرر**: تجاوز الدليل الجذري المحدد للعثور على جميع ملفات `pom.xml`، بغض النظر عن موقعها أو هيكلها.
2. **تحليل معلومات الوحدة النمطية**: استخراج `groupId`، و`artifactId`، والتبعيات من كل ملف `pom.xml`.
3. **معالجة توريث `groupId`**: إذا لم يحدد ملف `pom.xml` `groupId`، فورثه من تعريف `<parent>`، إذا كان موجودًا.
4. **تحديد التبعيات داخل المشروع**: مطابقة التبعيات مع الوحدات النمطية داخل المشروع بناءً على `groupId` و`artifactId`.
5. **إنشاء إخراج DOT**: إنشاء رسم بياني موجه للتبعيات بين الوحدات النمطية.

لا يعتمد هذا النهج على تسلسل هرمي محدد مسبقًا للدلائل أو يفترض أن ملفات `pom.xml` الأصلية موجودة في الدلائل الأصلية.

---

## النص البرمجي Python

إليك النص البرمجي Python المخصص لمتطلباتك:

```python
import os
import sys
import xml.etree.ElementTree as ET

# Define the Maven POM namespace
NS = "{http://maven.apache.org/POM/4.0.0}"

# Cache for groupId to avoid redundant parsing
group_id_cache = {}

def get_group_id(pom_path, pom_map):
    """
    Extract the groupId from a pom.xml file, considering inheritance from parent.

    Args:
        pom_path (str): Path to the pom.xml file.
        pom_map (dict): Mapping of pom.xml paths to their parsed data.

    Returns:
        str: The groupId of the module.
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # Check for parent declaration
        parent = root.find(NS + 'parent')
        if parent is not None:
            parent_group_id = parent.find(NS + 'groupId').text.strip()
            parent_artifact_id = parent.find(NS + 'artifactId').text.strip()
            parent_relative_path = parent.find(NS + 'relativePath')
            if parent_relative_path is not None and parent_relative_path.text:
                parent_pom_path = os.path.normpath(
                    os.path.join(os.path.dirname(pom_path), parent_relative_path.text)
                )
            else:
                # Default to parent directory if relativePath is omitted
                parent_pom_path = os.path.join(os.path.dirname(pom_path), '..', 'pom.xml')
                parent_pom_path = os.path.normpath(parent_pom_path)

            if parent_pom_path in pom_map:
                group_id = get_group_id(parent_pom_path, pom_map)
            else:
                raise ValueError(f"Parent POM not found for {pom_path}: {parent_pom_path}")
        else:
            raise ValueError(f"No groupId or parent specified in {pom_path}")

    group_id_cache[pom_path] = group_id
    return group_id

def get_artifact_id(pom_path):
    """
    Extract the artifactId from a pom.xml file.

    Args:
        pom_path (str): Path to the pom.xml file.

    Returns:
        str: The artifactId of the module.
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"pom.xml must specify artifactId: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    Extract the list of dependencies from a pom.xml file.

    Args:
        pom_path (str): Path to the pom.xml file.

    Returns:
        list: List of tuples (groupId, artifactId) for each dependency.
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    dependencies = []

    for dep in root.findall(NS + 'dependencies/' + NS + 'dependency'):
        dep_group_id_elem = dep.find(NS + 'groupId')
        dep_artifact_id_elem = dep.find(NS + 'artifactId')
        if dep_group_id_elem is not None and dep_artifact_id_elem is not None:
            dep_group_id = dep_group_id_elem.text.strip()
            dep_artifact_id = dep_artifact_id_elem.text.strip()
            dependencies.append((dep_group_id, dep_artifact_id))

    return dependencies

if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a directory")
        sys.exit(1)

    # Step 1: Recursively find all pom.xml files
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"No pom.xml files found in {root_dir}")
        sys.exit(1)

    # Step 2: Build a dictionary of all POMs for parent lookups
    pom_map = {pom_file: None for pom_file in pom_files}

    # Step 3: Extract module information
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"Warning: Skipping {pom_file} due to error: {e}")
            continue

    # Step 4: Analyze dependencies
    dependencies = set()
    for pom_file in pom_files:
        try:
            importer_group_id = get_group_id(pom_file, pom_map)
            importer_artifact_id = get_artifact_id(pom_file)
            importer_key = (importer_group_id, importer_artifact_id)
            deps = get_dependencies(pom_file)
            for dep_group_id, dep_artifact_id in deps:
                dep_key = (dep_group_id, dep_artifact_id)
                if dep_key in modules and dep_key != importer_key:
                    # Add dependency as (importer, imported) tuple using artifactId for simplicity
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"Warning: Error processing dependencies in {pom_file}: {e}")
            continue

    # Step 5: Output in DOT format
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## آلية العمل

### 1. **إدخال سطر الأوامر**
- يأخذ وسيطًا واحدًا: `<root_directory>`، نقطة البداية للبحث المتكرر.
- يتحقق من أنه دليل.

### 2. **العثور على ملفات `pom.xml`**
- يستخدم `os.walk` لتجاوز شجرة الدلائل بشكل متكرر وجمع جميع ملفات `pom.xml` في قائمة.

### 3. **تحليل معلومات الوحدة النمطية**
- **معرف المجموعة (`groupId`)**:
  - يُستخرج من كل ملف `pom.xml`.
  - إذا لم يكن موجودًا، يبحث عن قسم `<parent>` ويحل `groupId` من POM الأصل المشار إليه باستخدام `relativePath` (أو ينتقل افتراضيًا إلى الدليل الأصل في حالة حذفه).
  - يخزن النتائج مؤقتًا لتجنب إعادة التحليل.
- **معرف القطعة الأثرية (`artifactId`)**: يجب أن يكون موجودًا في كل ملف `pom.xml`.
- **التبعيات**: تستخرج أزواج `(groupId, artifactId)` من قسم `<dependencies>`.

### 4. **تحليل التبعيات**
- يبني خريطة لـ `(groupId, artifactId)` إلى `pom_path` لجميع الوحدات النمطية.
- لكل ملف `pom.xml`، يتحقق من تبعياته مقابل خريطة الوحدة النمطية للعثور على التبعيات داخل المشروع.
- يستبعد التبعيات الذاتية (حيث تعتمد الوحدة النمطية على نفسها).
- يسجل التبعيات كأزواج `(importer_artifactId, imported_artifactId)`.

### 5. **إخراج DOT**
- يُخرج رسمًا بيانيًا موجهًا بتنسيق DOT، باستخدام `artifactId` كتسميات للعقد للتبسيط.

---

## مثال على الاستخدام

لنفترض أن هيكل الدلائل الخاص بك غير منتظم:

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", depends on "core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", depends on "core")
```

شغّل النص البرمجي:

```bash
python script.py myproject
```

**الإخراج:**

```
digraph G {
  "app" -> "core";
  "util" -> "core";
}
```

يظهر هذا أن كلًا من `app` و`util` يعتمدان على `core`.

---

## ملاحظات وقيود

- **لا يوجد تجميع حسب الدليل**: على عكس النص البرمجي الأصلي في تتبع التفكير، هذا الإصدار لا يجمع الوحدات النمطية حسب هيكل الدلائل حيث أنك لم تطلب ذلك. يستخدم `artifactId` مباشرة في الرسم البياني.
- **حل الأصل**: يعتمد على `relativePath` في قسم `<parent>` أو يفترض أن POM الأصل موجود في الدليل الأصل إذا تم حذفه. إذا لم يكن POM الأصل موجودًا في المجموعة التي تم جمعها، فإنه يرفع خطأ.
- **مطابقة بسيطة**: يطابق التبعيات بواسطة `groupId` و`artifactId` فقط، متجاهلاً الإصدارات.
- **لا يوجد استبدال للخصائص**: لا يتعامل مع خصائص Maven مثل `${project.groupId}`.
- **معالجة الأخطاء**: يتخطى ملفات `pom.xml` Problematic مع تحذير بدلاً من الفشل تمامًا.

يلبي هذا النص البرمجي متطلباتك "للتكرار بشكل متكرر، والحصول على جميع POMs أولاً، ثم التحليل" دون افتراض هيكل ملف ثابت. دعني أعرف إذا كنت بحاجة إلى تعديلات!