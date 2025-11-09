---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: مستخرج حزم بايثون المستوردة
translated: true
type: note
---

### نص برمجي بلغة Python لاستخراج جميع الحزم المستوردة

يمشي هذا النص البرمجي عبر دليل محدد وجميع أدلته الفرعية، يجد جميع ملفات Python (`.py`)، يحلل عبارات الاستيراد الخاصة بها باستخدام وحدة `ast` في Python (لتحليل آلي واعي بالتركيب النحوي)، ويجمع جميع أسماء الوحدات الأساسية الفريدة (مثل `os` من `import os`، أو `collections` من `from collections import defaultdict`). يتجاهل الوحدات المضمنة ويركز على الوحدات الخارجية.

احفظ هذا كملف `.py` (مثل `extract_imports.py`) وشغله باستخدام مسار الدليل كوسيطة، مثل `python extract_imports.py /path/to/directory`.

```python
import os
import ast
import sys

def extract_imports_from_file(file_path):
    """
    Parses a Python file and extracts imported module names.
    Handles 'import mod' and 'from mod import item' styles.
    """
    modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split('.')[0])  # Get base module (e.g., 'import os.path' -> 'os')
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])  # Get base module from 'from mod.sub import ...'
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    
    return modules

def get_all_imported_modules(directory):
    """
    Walks through the directory and subdirectories, collects all unique imported modules.
    """
    all_modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules = extract_imports_from_file(file_path)
                all_modules.update(modules)
    
    # Exclude common builtins (optional, as they are rarely external packages)
    excluded = {'sys', 'os', 're', 'math', 'random', 'json', 'time', 'datetime', 'collections', 'itertools', 'functools'}
    all_modules -= excluded
    
    return sorted(all_modules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_imports.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    modules = get_all_imported_modules(directory)
    print("All unique imported packages:")
    for mod in modules:
        print(mod)
```

### آلية العمل
- **المرور عبر الأدلة**: يستخدم `os.walk` لزيارة جميع الأدلة الفرعية والملفات بشكل متكرر.
- **تصفية الملفات**: يعالج فقط ملفات `.py`.
- **تحليل عبارات الاستيراد**: يوظف `ast` لتحليل الكود المصدري بشكل آلي وتحديد عُقد `Import` و `ImportFrom`. يقسم على `.` لالتقاط الوحدة ذات المستوى الأعلى (مثل `numpy` من `import numpy.linalg`).
- **التجميع**: يجمع الوحدات في مجموعة لضمان التفرد، ثم يرتبها ويطبعها.
- **الحالات الخاصة**: يتخطى الوحدات المضمنة (يمكنك تخصيص مجموعة `excluded`)، يتعامل مع أخطاء التركيب النحوي بأسلوب متحضر، ويدعم ملفات Unicode.
- **المخرجات**: قائمة مرتبة بأسماء الحزم الفريدة. إذا شُغّل على دليل مشروعك الخاص، فسيسرد حزمًا مثل `requests`، `pandas`، إلخ، والتي ستحتاج إلى تثبيتها.

هذا الأسلوب فعال لتحليل قاعدة الكود ويتجنب تنفيذ كود قد يكون غير آمن. إذا كنت تحتاج إلى تحسينات (مثل التعامل مع عمليات الاستيراد النسبية بشكل مختلف أو إنشاء ملف requirements.txt)، قدم المزيد من التفاصيل!