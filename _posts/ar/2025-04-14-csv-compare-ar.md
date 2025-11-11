---
audio: false
generated: true
lang: ar
layout: post
title: مقارنة ملفي CSV أحاديي الصف
translated: true
type: note
---

إليك نصًا برمجيًا بلغة Python يقارن بين ملفّي CSV يحتويان على صف واحد من السلاسل النصية (مثل "P0001") ويحدد:
- العناصر المشتركة (الموجودة في كلا الملفين)
- العناصر الفريدة في الملف الأول
- العناصر الفريدة في الملف الثاني

يستخدم النص البرمجي `argparse` لقبول مساري ملفّي CSV، يقرأ الصف الأول من كل ملف، يُجري مقارنة قائمة على المجموعات (sets)، ويكتب النتائج في ملف `comparison.txt`.

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # إعداد محلل الوسائط
    parser = argparse.ArgumentParser(description='Compare two single-row CSV files for common and unique items')
    parser.add_argument('file1_path', help='Path to the first CSV file')
    parser.add_argument('file2_path', help='Path to the second CSV file')
    
    # تحليل الوسائط
    args = parser.parse_args()
    
    try:
        # قراءة الصف الأول من ملف CSV الأول
        with open(args.file1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                values1 = row
                break
        
        # قراءة الصف الأول من ملف CSV الثاني
        with open(args.file2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                values2 = row
                break
        
        # التحويل إلى مجموعات للمقارنة
        set1 = set(values1)
        set2 = set(values2)
        
        # إيجاد العناصر المشتركة والفريدة
        common_items = set1.intersection(set2)
        unique_to_file1 = set1.difference(set2)
        unique_to_file2 = set2.difference(set1)
        
        # تحديد مجلد الإخراج (استخدم مجلد الملف الأول)
        output_dir = os.path.dirname(args.file1_path) or '.'
        output_file = os.path.join(output_dir, 'comparison.txt')
        
        # كتابة النتائج إلى ملف الإخراج
        with open(output_file, 'w') as file:
            file.write("Comparison Results:\n\n")
            
            file.write("Common Items (in both files):\n")
            if common_items:
                for item in sorted(common_items):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
                
            file.write("\nItems only in first file:\n")
            if unique_to_file1:
                for item in sorted(unique_to_file1):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
                
            file.write("\nItems only in second file:\n")
            if unique_to_file2:
                for item in sorted(unique_to_file2):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
        
        print(f"Comparison complete. Results saved to {output_file}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### آلية العمل:
1. **الإدخال**: يأخذ مساري ملفّي CSV عبر وسائط سطر الأوامر.
2. **القراءة**: يقرأ فقط الصف الأول من كل ملف CSV.
3. **المقارنة**:
   - يحول الصفوف إلى مجموعات (sets) لمقارنة فعالة.
   - يجد:
     - **العناصر المشتركة**: العناصر الموجودة في كلا الصفين (تقاطع المجموعتين).
     - **الفريدة للملف الأول**: العناصر الموجودة فقط في الصف الأول (فرق المجموعتين: file1 - file2).
     - **الفريدة للملف الثاني**: العناصر الموجودة فقط في الصف الثاني (فرق المجموعتين: file2 - file1).
4. **الإخراج**: يكتب النتائج في ملف `comparison.txt` في مجلد الملف الأول، مع سرد:
   - العناصر المشتركة
   - العناصر الموجودة فقط في الملف الأول
   - العناصر الموجودة فقط في الملف الثاني
   - يتم فرز كل قسم أبجديًا؛ يكتب "None" إذا كان القسم فارغًا.
5. **معالجة الأخطاء**: يلتقط أخطاء عدم العثور على الملف والاستثناءات الأخرى.

### مثال للاستخدام:
احفظ النص البرمجي باسم `compare_csv.py`. أنشئ ملفّي CSV، على سبيل المثال:
- `file1.csv`: `P0001,P0002,P0003`
- `file2.csv`: `P0001,P0004,P0003`

شغّل النص البرمجي:
```
python compare_csv.py file1.csv file2.csv
```

**الإخراج** (`comparison.txt`):
```
Comparison Results:

Common Items (in both files):
P0001
P0003

Items only in first file:
P0002

Items only in second file:
P0004
```

### ملاحظات:
- يتجاهل النص البرمجي موقع العناصر ويركز فقط على الوجود/الغياب.
- يتم التعامل مع العناصر المكررة في الصف تلقائيًا (المجموعات تزيل التكرارات).
- يُكتب الإخراج في `comparison.txt` في مجلد ملف الإدخال الأول.
- إذا كان الملف فارغًا أو لا يحتوي على صف، سيعامله النص البرمجي على أنه مجموعة فارغة.