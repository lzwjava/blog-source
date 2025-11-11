---
audio: false
generated: true
lang: ar
layout: post
title: سكريبت فرز سي إس في
translated: true
type: note
---

سأقوم بإنشاء سكريبت Python يستخدم argparse لتحليل مسار ملف CSV، وفرز سطر واحد من القيم المفصولة بفواصل أبجديًا، وإخراج النتيجة إلى ملف باسم "name_sorted.csv".

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # إعداد محلل الوسائط
    parser = argparse.ArgumentParser(description='Sort a single-line CSV file alphabetically')
    parser.add_argument('file_path', help='Path to the input CSV file')
    
    # تحليل الوسائط
    args = parser.parse_args()
    
    try:
        # الحصول على الدليل واسم الملف
        file_dir = os.path.dirname(args.file_path)
        file_name = os.path.basename(args.file_path)
        
        # إنشاء اسم ملف الإخراج
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{base_name}_sorted{ext}")
        
        # قراءة ملف CSV المدخل
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # الحصول على السطر الأول فقط
            for row in reader:
                values = row
                break
        
        # فرز القيم أبجديًا
        sorted_values = sorted(values)
        
        # الكتابة إلى ملف الإخراج
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"Successfully sorted values and saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{args.file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

هذا السكريبت:
1. يستخدم argparse للحصول على مسار ملف الإدخال
2. يفتح ملف CSV ويقرأ السطر الأول فقط
3. يرتب القيم أبجديًا
4. يكتب القيم المرتبة إلى "name_sorted.csv"

لتشغيل السكريبت، احفظه في ملف (مثل "sort_csv.py"، اجعله قابلاً للتنفيذ إذا لزم الأمر، وقم بتشغيله مع المسار إلى ملف CSV الخاص بك:

```
python sort_csv.py path/to/your/file.csv
```

هل تريد مني شرح أي جزء من الكود بمزيد من التفصيل؟