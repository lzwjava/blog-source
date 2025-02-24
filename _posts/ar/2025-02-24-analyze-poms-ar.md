---
audio: false
lang: ar
layout: post
title: تحليل ملفات POM Maven لإنشاء مخطط التبعيات
translated: true
---

للتعامل مع استفسارك، سأقدم حلاً لتوليد مخطط التبعية في صيغة DOT عن طريق العثور على جميع ملفات `pom.xml` في الدليل بشكل تكراري وتحليل تبعياتها، دون افتراض بنية مشروع Maven متعدد الوحدات مثل المثال (`project/module1/pom.xml`، إلخ.). سيتركز النص على جمع جميع ملفات `pom.xml` أولاً، ثم تحليلها لتحديد تبعيات الوحدات وإخراج المخطط.

---

## نظرة عامة على الحل

هنا ما سيقوم به النص:

1. **جمع ملفات `pom.xml` بشكل تكراري**: استعرض الدليل الجذر المحدد للعثور على جميع ملفات `pom.xml`، بغض النظر عن موقعها أو هيكلها.
2. **تحليل معلومات الوحدات**: استخراج `groupId` و `artifactId` و التبعيات من كل `pom.xml`.
3. **معالجة وراثة `groupId`**: إذا لم يحدد `pom.xml` `groupId`، فاستيراده من إعلان `<parent>`، إذا كان موجوداً.
4. **تحديد التبعيات داخل المشروع**: تطابق التبعيات مع الوحدات داخل المشروع بناءً على `groupId` و `artifactId`.
5. **إنشاء خروج DOT**: إنشاء مخطط متجه للتبعيات بين الوحدات.

هذا النهج لا يعتمد على هيكل دليل مسبق أو افتراض أن ملفات `pom.xml` الأب هي في الدلائل الأب.

---

## النص البرمجي Python

هنا النص البرمجي المخصص لحاجتك:

```python
import os
import sys
import xml.etree.ElementTree as ET

# تعريف مساحة الاسم Maven POM
NS = "{http://maven.apache.org/POM/4.0.0}"

# مخزن مؤقت groupId لتجنب التحليل المتكرر
group_id_cache = {}

def get_group_id(pom_path, pom_map):
    """
    استخراج groupId من ملف pom.xml، مع أخذ الوراثة من الأب في الاعتبار.

    Args:
        pom_path (str): مسار ملف pom.xml.
        pom_map (dict): خريطة ملفات pom.xml إلى بياناتها المحلولة.

    Returns:
        str: groupId الوحدة.
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # تحقق من إعلان الأب
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
                # الافتراض على الدليل الأب إذا تم إغفال relativePath
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
    استخراج artifactId من ملف pom.xml.

    Args:
        pom_path (str): مسار ملف pom.xml.

    Returns:
        str: artifactId الوحدة.
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"pom.xml must specify artifactId: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    استخراج قائمة التبعيات من ملف pom.xml.

    Args:
        pom_path (str): مسار ملف pom.xml.

    Returns:
        list: قائمة أزواج (groupId, artifactId) لكل تبعية.
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
    # التحقق من حجج السطر الأوامر
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a directory")
        sys.exit(1)

    # الخطوة 1: العثور على جميع ملفات pom.xml بشكل تكراري
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"No pom.xml files found in {root_dir}")
        sys.exit(1)

    # الخطوة 2: بناء قاموس لجميع POMs للبحث عن الأب
    pom_map = {pom_file: None for pom_file in pom_files}

    # الخطوة 3: استخراج معلومات الوحدات
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"Warning: Skipping {pom_file} due to error: {e}")
            continue

    # الخطوة 4: تحليل التبعيات
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
                    # إضافة تبعية كزوج (importer, imported) باستخدام artifactId للسهولة
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"Warning: Error processing dependencies in {pom_file}: {e}")
            continue

    # الخطوة 5: إخراج في صيغة DOT
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## كيفية عمل النص

### 1. **دخول السطر الأوامر**
- يأخذ حجة واحدة: `<root_directory>`، نقطة البداية للبحث التكراري.
- يثبت أن هذا هو دليل.

### 2. **البحث عن ملفات `pom.xml`**
- يستخدم `os.walk` لتسجيل الدليل التكراري وتجميع جميع ملفات `pom.xml` في قائمة.

### 3. **تحليل معلومات الوحدات**
- **Group ID (`groupId`)**:
  - استخراج من كل `pom.xml`.
  - إذا لم يكن موجوداً، يبحث عن قسم `<parent>` ويحلل `groupId` من POM الأب المرجع باستخدام `relativePath` (أو الافتراض على الدليل الأب إذا تم إغفال).
  - تخزين النتائج لتجنب التحليل المتكرر.
- **Artifact ID (`artifactId`)**: يجب أن يكون موجوداً في كل `pom.xml`.
- **التبعيات**: استخراج أزواج `(groupId, artifactId)` من القسم `<dependencies>`.

### 4. **تحليل التبعيات**
- بناء خريطة `(groupId, artifactId)` إلى `pom_path` لجميع الوحدات.
- لكل `pom.xml`، يحدد التبعيات ضد الخريطة للوحدات للعثور على التبعيات داخل المشروع.
- إغفال التبعيات الذاتية (حيث تعتمد الوحدة على نفسها).
- تسجيل التبعيات كزوجات `(importer_artifactId, imported_artifactId)`.

### 5. **خروج DOT**
- إخراج مخطط متجه في صيغة DOT، باستخدام `artifactId` كعلامات العقد للسهولة.

---

## مثال على الاستخدام

فرض أن هيكل الدليل غير منتظم:

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", يعتمد على "core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", يعتمد على "core")
```

أشغل النص:

```bash
python script.py myproject
```

**الخروج:**

```
digraph G {
  "app" -> "core";
  "util" -> "core";
}
```

هذا يوضح أن كلا من `app` و `util` يعتمدان على `core`.

---

## ملاحظات وتقييدات

- **لا تجميع حسب الدليل**: عكس النص الأصلي في مسار التفكير، هذه النسخة لا تجميع الوحدات حسب هيكل الدليل لأنها لم تطلبها. تستخدم `artifactId` مباشرة في المخطط.
- **حل الأب**: يعتمد على `relativePath` في القسم `<parent>` أو الافتراض على أن POM الأب في الدليل الأب إذا تم إغفال. إذا لم يكن POM الأب في المجموعة المجمع، يرفع خطأ.
- **مطابقة بسيطة**: تطابق التبعيات بواسطة `groupId` و `artifactId` فقط، تجاهل الأصدارات.
- **لا استبدال الخصائص**: لا يعالج خصائص Maven مثل `${project.groupId}`.
- **معالجة الأخطاء**: يتخطى ملفات `pom.xml` المشبوهة مع تحذير بدلاً من الفشل كلياً.

هذا النص يفي بحاجتك "لإتاحة التكرار، الحصول على جميع POMs أولاً، ثم التحليل" دون افتراض بنية ملفات ثابتة. أخبرني إذا كنت بحاجة إلى تعديلات!