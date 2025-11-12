---
audio: false
generated: true
lang: ar
layout: post
title: تحليل مشاريع Spring Boot
translated: true
type: note
---

لتحليل مشروع Spring Boot (الذي قد يتكون من وحدات متعددة) واستخراج جميع واجهات برمجة التطبيقات المعرفة باستخدام annotations `@GetMapping` أو `@PostMapping`، نحتاج إلى اجتياز دليل المشروع، وتحديد فئات المتحكم (controller)، واستخراج مسارات واجهات برمجة التطبيقات، وطباعتها بتنسيق محدد. فيما يلي نص برمجي كامل بلغة Python يحقق هذه المهمة، مستوحى من هيكل الكود المقدم ولكن معدلاً ليناسب المتطلبات الجديدة. سيخرج النتائج مع قائمة لكل متحكم مع مسارات GET وPOST المرتبطة به بتنسيق "XXController: get path post path".

### المنهجية

1.  **اجتياز الدليل**: البحث بشكل متكرر عن جميع ملفات `.java` في دليل المشروع والمجلدات الفرعية الخاصة به.
2.  **تحديد المتحكمات**: التحقق من كل ملف Java للعثور على annotations `@Controller` أو `@RestController` للتأكد من أنه فئة متحكم.
3.  **استخراج المسارات على مستوى الفئة**: البحث عن annotation `@RequestMapping` على مستوى الفئة لتحديد المسارات الأساسية.
4.  **استخراج واجهات برمجة التطبيقات على مستوى الدالة**: العثور على الدوال المشروحة بـ `@GetMapping` أو `@PostMapping`، واستخراج مساراتها، ودمجها مع المسارات الأساسية إذا كانت موجودة.
5.  **تنظيم وطباعة النتائج**: جمع مسارات GET وPOST لكل متحكم وطباعتها بالتنسيق المحدد.

### النص البرمجي Python

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    البحث بشكل متكرر عن جميع ملفات .java في الدليل المعطى والمجلدات الفرعية الخاصة به.
    
    Args:
        root_dir (str): الدليل الجذر لبدء البحث منه.
    
    Yields:
        str: المسار الكامل لكل ملف .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    استخراج قيم المسار من annotation Spring (@GetMapping, @PostMapping, أو @RequestMapping).
    
    Args:
        line (str): السطر الذي يحتوي على الـ annotation.
        annotation_type (str): نوع الـ annotation ('GetMapping', 'PostMapping', أو 'RequestMapping').
    
    Returns:
        list: قائمة بسلاسل المسارات المستخرجة من الـ annotation.
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # استخراج جميع السلاسل النصية داخل علامات الاقتباس
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # البحث عن سمة 'value' أو 'path'
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # إذا لم يكن هناك 'value' أو 'path'، افترض تحديد المسار مباشرة
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # تحليل وسائط سطر الأوامر
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)
    
    print(f"[INFO] Starting analysis of directory: {root_dir}")
    
    # تهيئة قاموس لتخزين تعيينات المتحكمات
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0
    
    # معالجة جميع ملفات Java
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # التحقق مما إذا كان الملف متحكمًا
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')
                
                # العثور على سطر تعريف الفئة لفصل annotations على مستوى الفئة عن annotations على مستوى الدالة
                class_line_index = None
                for i, line in enumerate(lines):
                    if re.search(r'public\s+(class|abstract\s+class|interface)\s+\w+', line):
                        class_line_index = i
                        break
                if class_line_index is None:
                    continue
                
                # استخراج @RequestMapping على مستوى الفئة كمسارات أساسية
                base_paths = []
                for line in lines[:class_line_index]:
                    if re.search(r'\s*@RequestMapping', line):
                        base_paths = extract_paths(line, 'RequestMapping')
                        break
                if not base_paths:
                    base_paths = ['']
                
                # استخراج @GetMapping و @PostMapping على مستوى الدالة
                get_paths = []
                post_paths = []
                for line in lines[class_line_index:]:
                    if re.search(r'\s*@GetMapping', line):
                        paths = extract_paths(line, 'GetMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                get_paths.append(full_path)
                    elif re.search(r'\s*@PostMapping', line):
                        paths = extract_paths(line, 'PostMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                post_paths.append(full_path)
                
                # تخزين المسارات الفريدة
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))
                
                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths
            
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
    
    # طباعة الملخص
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    print(f"[INFO] Total controllers found: {len(controllers)}")
    
    # طباعة النتائج بالتنسيق المحدد
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### الشرح

-   **الواردات**: نستخدم `os` لاجتياز الدليل، و`sys` لوسائط سطر الأوامر، و`re` للتعبيرات النمطية، و`defaultdict` لتنظيم بيانات المتحكم.
-   **`find_java_files`**: هذه الدالة تنتج بشكل متكرر جميع ملفات `.java` في دليل المشروع، وتتعامل مع الوحدات المتعددة بشكل طبيعي عبر `os.walk`.
-   **`extract_paths`**: هذه الدالة تقوم بتحليل annotations `@GetMapping`، أو `@PostMapping`، أو `@RequestMapping` لاستخراج قيم المسار. تتعامل مع:
    -   المسارات المفردة (مثال: `@GetMapping("/path")`).
    -   المسارات المتعددة (مثال: `@GetMapping({"/path1", "/path2"})`).
    -   السمات المسماة (مثال: `@RequestMapping(value = "/path")`).
-   **المنطق الرئيسي**:
    -   **معالجة سطر الأوامر**: يأخذ دليل جذر كمدخل، مشابه للنص البرمجي المقدم.
    -   **كشف المتحكم**: يتحقق من وجود `@Controller` أو `@RestController` في محتوى الملف.
    -   **المسارات الأساسية**: يستخرج مسارات `@RequestMapping` على مستوى الفئة قبل تعريف الفئة.
    -   **استخراج واجهات برمجة التطبيقات**: يعالج الأسطر بعد تعريف الفئة للبحث عن `@GetMapping` و `@PostMapping`، ويدمج المسارات مع المسارات الأساسية.
    -   **الإخراج**: يطبع كل متحكم مع مسارات GET وPOST الخاصة به، واحد لكل سطر، مسبوقة بـ "get" أو "post".
-   **معالجة الأخطاء**: يلتقط الاستثناءات أثناء قراءة الملف ويبلغ عنها، مما يعكس متانة الكود المقدم.

### نموذج للإخراج

لمشروع Spring Boot به ملف `UserController.java`:

```java
@RestController
@RequestMapping("/users")
public class UserController {
    @GetMapping("/all")
    public ResponseEntity<?> getAllUsers() { ... }

    @PostMapping("/create")
    public ResponseEntity<?> createUser() { ... }
}
```

تشغيل `python script.py /path/to/project` قد ينتج:

```
[INFO] Starting analysis of directory: /path/to/project
[INFO] Total Java files attempted: 10
[INFO] Successfully processed: 10
[INFO] Files with errors: 0
[INFO] Total controllers found: 1
UserController:
get /users/all
post /users/create
```

### ملاحظات

-   **التبسيط**: يفترض النص البرمجي أن الـ annotations تكون في أسطر مفردة وأن المسارات هي سلاسل نصية بدون تعبيرات معقدة. للاستخدام في بيئة الإنتاج، قد يكون محلل Java أكثر متانة.
-   **GET و POST فقط**: كما هو مطلوب، يركز على `@GetMapping` و `@PostMapping`، متجاهلاً الطرق الأخرى مثل PUT أو DELETE (على الرغم من أن تتبع التفكير أخذ بعين الاعتبار `@RequestMapping` مع الطرق).
-   **ربط المسارات**: يجمع مسارات مستوى الفئة ومسارات مستوى الدالة مباشرة (مثال: `/users` + `/all` = `/users/all`). يقوم Spring بتطبيع الشرطات المائلة المتعددة، لذا هذا يكفي لأغراض العرض.

يلبي هذا النص البرمجي متطلبات الاستعلام مع الحفاظ على هيكل مشابه للكود المقدم، مما يضمن الألفة والموثوقية.