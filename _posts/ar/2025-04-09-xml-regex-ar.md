---
audio: false
generated: true
lang: ar
layout: post
title: برنامج XML للتعبيرات النمطية
translated: true
type: note
---

سأعدل السكريبت لاستخدام `argparse` للتعامل مع وسائط سطر الأوامر. هذا سيسمح لك بتمرير مسار الملف مباشرة عند تشغيل السكريبت:

```python
import xml.etree.ElementTree as ET
import re
import argparse

def extract_look_tags(xml_file):
    # قراءة محتوى ملف XML
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    
    # العثور على جميع وسوم <c:look> باستخدام التعبير النمطي
    pattern = r'<c:look>(\d+)</c:look>'
    matches = re.findall(pattern, xml_content)
    
    # طباعة الأرقام
    for number in matches:
        print(number)

def main():
    # إعداد محلل الوسائط
    parser = argparse.ArgumentParser(description='Extract numbers from <c:look> tags in an XML file')
    parser.add_argument('file_path', help='Path to the XML file')
    
    # تحليل الوسائط
    args = parser.parse_args()
    
    # معالجة الملف
    extract_look_tags(args.file_path)

if __name__ == "__main__":
    main()
```

الآن يمكنك تشغيل السكريبت من سطر الأوامر هكذا:

```
python script_name.py path/to/your/xml_file.xml
```

سيقوم السكريبت بـ:
1. استخدام `argparse` للتعامل مع وسيط سطر الأوامر لمسار الملف
2. تحليل ملف XML للعثور على جميع وسوم `<c:look>`
3. استخراج وطباعة الأرقام داخل هذه الوسوم

هذا النهج يجعل السكريبت أكثر سهولة في الاستخدام ومناسبًا للبرمجة النصية أو المعالجة المجمعة.