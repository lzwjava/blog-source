---
audio: false
generated: true
lang: ar
layout: post
title: ملف مضغوط نظيف
translated: true
type: note
---

1. **يقرأ ملف ZIP** باستخدام `zipfile.ZipFile` ويحصل على قائمة بجميع الملفات الموجودة داخله.
2. **يُرشّح الملفات التي لا تحتوي على امتدادات**، مع الاحتفاظ بالمجلدات (المدخلات التي تنتهي بـ `/`).
3. **يسجل الملفات المُزالَة** لإعلام المستخدم بالملفات التي تم استبعادها.
4. **ينشئ ملف ZIP جديدًا** يحتوي فقط على الملفات الصالحة (تلك التي تحتوي على امتدادات أو مجلدات).
5. **يستخدم `argparse` لقبول مسار ملف ZIP** كوسيطة سطر أوامر.

هذا يضمن بقاء الملفات الصحيحة فقط مع الحفاظ على هياكل المجلدات. 🚀

```python
import zipfile
import os
import argparse

def clean_zip(zip_path):
    output_path = os.path.splitext(zip_path)[0] + "_output.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        
        # فصل الملفات الصالحة والملفات بدون امتدادات (باستثناء المجلدات)
        valid_files = [f for f in file_names if os.path.splitext(os.path.basename(f))[1] or f.endswith('/')]
        removed_files = [f for f in file_names if not os.path.splitext(os.path.basename(f))[1] and not f.endswith('/')]
        
        if not valid_files:
            print("No valid files with extensions found. Exiting.")
            return
        
        # تسجيل الملفات المُزالَة
        if removed_files:
            print("Removing the following files (no extensions detected):")
            for f in removed_files:
                print(f" - {f}")
        
        # إنشاء ملف zip جديد باستبعاد الملفات غير الصالحة
        with zipfile.ZipFile(output_path, 'w') as clean_zip:
            for file in valid_files:
                with zip_ref.open(file) as source:
                    clean_zip.writestr(file, source.read())

    print(f"Cleaned ZIP file created: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean a ZIP file by removing files without extensions.")
    parser.add_argument("zip_path", help="Path to the input ZIP file")
    args = parser.parse_args()
    clean_zip(args.zip_path)

```