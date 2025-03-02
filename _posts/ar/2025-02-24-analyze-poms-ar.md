---
audio: true
generated: true
lang: ar
layout: post
title: تحليل ملفات POM Maven
translated: true
---

للتعامل مع استفسارك، سأقدم حلًا لتوليد مخطط التبعية في صيغة DOT عن طريق العثور على جميع ملفات `pom.xml` في دليل بشكل تكراري وتحليل تبعياتها، دون افتراض بنية مشروع Maven متعدد الأجزاء الثابتة مثل تلك في المثال (`project/module1/pom.xml`، إلخ.). سيركز النص على جمع جميع ملفات `pom.xml` أولاً، ثم تحليلها لتحديد تبعيات الوحدات وإخراج المخطط.

---

## نظرة عامة على الحل

هنا ما سيقوم به النص:

1. **جمع ملفات `pom.xml` بشكل تكراري**: استعرض الدليل الجذر المحدد للعثور على جميع ملفات `pom.xml`، بغض النظر عن موقعها أو هيكلها.
2. **تحليل معلومات الوحدات**: استخراج `groupId` و `artifactId` و التبعيات من كل `pom.xml`.
3. **معالجة وراثة `groupId`**: إذا لم يحدد `pom.xml` `groupId`، فاستيراده من إعلان `<parent>`، إذا كان موجودًا.
4. **تحديد التبعيات داخل المشروع**: تطابق التبعيات مع الوحدات داخل المشروع بناءً على `groupId` و `artifactId`.
5. **إنشاء إخراج DOT**: إنشاء مخطط موجه للتبعيات بين الوحدات.

يستخدم هذا النهج لا يعتمد على هيكل دليل مسبق أو افتراض أن ملفات `pom.xml` الأبوة في الدلائل الأبوة.

---

## النص البرمجي Python

هنا النص البرمجي المخصص لطلبك:

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

    المعلمات:
        pom_path (str): مسار ملف pom.xml.
        pom_map (dict): خريطة ملفات pom.xml إلى بياناتها المحلولة.

    العائد:
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
        # التحقق من إعلان الأب
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
                raise ValueError(f"لم يتم العثور على POM الأب لـ {pom_path}: {parent_pom_path}")
        else:
            raise ValueError(f"لم يتم تحديد groupId أو الأب في {pom_path}")

    group_id_cache[pom_path] = group_id
    return group_id

def get_artifact_id(pom_path):
    """
    استخراج artifactId من ملف pom.xml.

    المعلمات:
        pom_path (str): مسار ملف pom.xml.

    العائد:
        str: artifactId الوحدة.
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"يجب على pom.xml تحديد artifactId: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    استخراج قائمة التبعيات من ملف pom.xml.

    المعلمات:
        pom_path (str): مسار ملف pom.xml.

    العائد:
        list: قائمة من أزواج (groupId, artifactId) لكل تبعية.
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
    # التحقق من المعلمات السطرية
    if len(sys.argv) != 2:
        print("استخدام: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"خطأ: {root_dir} ليس دليل")
        sys.exit(1)

    # الخطوة 1: العثور على جميع ملفات pom.xml بشكل تكراري
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"لم يتم العثور على ملفات pom.xml في {root_dir}")
        sys.exit(1)

    # الخطوة 2: بناء خريطة لجميع POMs للبحث عن الأب
    pom_map = {pom_file: None for pom_file in pom_files}

    # الخطوة 3: استخراج معلومات الوحدات
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"تحذير: تخطي {pom_file} بسبب الخطأ: {e}")
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
                    # إضافة التبعية كزوج (importer, imported) باستخدام artifactId للسهولة
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"تحذير: خطأ في معالجة التبعيات في {pom_file}: {e}")
            continue

    # الخطوة 5: إخراج في صيغة DOT
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## كيفية عمله

### 1. **المدخل السطرية**
- يأخذ معلمة واحدة: `<root_directory>`, نقطة البدء للبحث التكراري.
- يثبت أن هذا دليل.

### 2. **البحث عن ملفات `pom.xml`**
- يستخدم `os.walk` لاستعراض شجرة الدليل بشكل تكراري وجمع جميع ملفات `pom.xml` في قائمة.

### 3. **تحليل معلومات الوحدات**
- **Group ID (`groupId`)**:
  - يستخرج من كل `pom.xml`.
  - إذا لم يكن موجودًا، يبحث عن قسم `<parent>` ويحل `groupId` من POM الأب المرجع باستخدام `relativePath` (أو الافتراض على الدليل الأب إذا تم إغفاله).
  - يحفظ النتائج لتجنب التحليل المتكرر.
- **Artifact ID (`artifactId`)**: يجب أن يكون موجودًا في كل `pom.xml`.
- **التبعيات**: يستخرج أزواج `(groupId, artifactId)` من القسم `<dependencies>`.

### 4. **تحليل التبعيات**
- يبني خريطة `(groupId, artifactId)` إلى `pom_path` لجميع الوحدات.
- لكل `pom.xml`، يحدد التبعيات ضد خريطة الوحدات للعثور على التبعيات داخل المشروع.
- يبعد التبعيات الذاتية (حيث تعتمد الوحدة على نفسها).
- يسجل التبعيات كزوجات `(importer_artifactId, imported_artifactId)`.

### 5. **إخراج DOT**
- يخرج مخططًا موجهًا في صيغة DOT، باستخدام `artifactId` كعلامات العقد للسهولة.

---

## مثال على الاستخدام

فرض أن هيكل الدليل غير منتظم:

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", يعتمد على "core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", يعتمد على "core")
```

أشغل النص البرمجي:

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

يظهر أن كل من `app` و `util` يعتمد على `core`.

---

## ملاحظات وقيود

- **لا تجميع حسب الدليل**: عكس النص الأصلي في مسار التفكير، لا تجميع الوحدات حسب هيكل الدليل، لأنه لم تطلب ذلك. يستخدم `artifactId` مباشرة في المخطط.
- **حل الأب**: يعتمد على `relativePath` في القسم `<parent>` أو الافتراض على أن POM الأب في الدليل الأب إذا تم إغفاله. إذا لم يكن POM الأب في مجموعة الملفات المحلولة، يرفع خطأ.
- **مطابقة بسيطة**: تطابق التبعيات بواسطة `groupId` و `artifactId` فقط، تجاهل الإصدارات.
- **لا استبدال الخصائص**: لا يعالج خصائص Maven مثل `${project.groupId}`.
- **معالجة الأخطاء**: يخطي ملفات `pom.xml` المشكوك فيها مع تحذير بدلاً من الفشل بالكامل.

يحقق هذا النص طلبك "التردد بشكل تكراري، الحصول على جميع POMs أولاً، ثم التحليل" دون افتراض بنية ملفات ثابتة. أخبرني إذا كنت تحتاج إلى تعديلات!