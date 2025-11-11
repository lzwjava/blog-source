---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: قراءة ملفات إكسل باستخدام باندا
translated: true
type: note
---

### المتطلبات الأساسية
لقراءة ملفات Excel في Python، تحتاج إلى مكتبة `pandas` ومحرك Excel. قم بتثبيت pandas إذا لم تكن مثبتة مسبقًا:
```
pip install pandas
```
لصيغ Excel الحديثة (.xlsx)، قم بتثبيت `openpyxl`:
```
pip install openpyxl
```
لملفات (.xls)، استخدم `xlrd`:
```
pip install xlrd
```

### الاستخدام الأساسي
توفر Pandas الدالة `pd.read_excel()` لتحميل بيانات Excel إلى DataFrame.

1. استيراد pandas:
   ```python
   import pandas as pd
   ```

2. قراءة ملف Excel (حدد مسار الملف):
   ```python
   df = pd.read_excel('path/to/your/file.xlsx')
   ```
   - يقوم هذا بتحميل الورقة الأولى افتراضيًا.
   - النتيجة هي DataFrame يحتوي على بيانات Excel.

3. فحص البيانات:
   ```python
   print(df.head())  # عرض أول 5 صفوف
   print(df.info())  # ملخص للأعمدة وأنواع البيانات
   ```

### خيارات متقدمة
- **تحديد ورقة**: استخدم معامل `sheet_name` (القيمة الافتراضية هي 0 للورقة الأولى):
  ```python
  df = pd.read_excel('file.xlsx', sheet_name='Sheet2')  # بالاسم
  df = pd.read_excel('file.xlsx', sheet_name=1)        # بالفهرس (يبدأ من 0)
  ```
- **قراءة أوراق متعددة**: مرر قائمة أو `None` لتحميل جميع الأوراق كقاموس:
  ```python
  all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # قاموس من DataFrames مفتاحه اسم الورقة
  ```
- **تحديد نطاق البيانات**: استخدم `usecols` للأعمدة (مثال: `'A:C'` للأعمدة من A إلى C) و `skiprows` لتخطي الصفوف الأولية:
  ```python
  df = pd.read_excel('file.xlsx', usecols='A,C,E', skiprows=2)
  ```
- **معالجة العناوين**: إذا لم يكن العنوان في الصف 0، حدد ذلك باستخدام `header`:
  ```python
  df = pd.read_excel('file.xlsx', header=1)  # العنوان في الصف 1 (فهرس يبدأ من 0)
  ```
- **تعيين الفهرس**: استخدم `index_col` لتعيين عمود كفهرس:
  ```python
  df = pd.read_excel('file.xlsx', index_col='Column Name')
  ```

### مثال
لنفترض أن لديك ملف Excel `sales.xlsx` به ورقة باسم "Data" تحتوي على بيانات المبيعات.

```python
import pandas as pd

# قراءة الورقة المحددة
df = pd.read_excel('sales.xlsx', sheet_name='Data')

# عرض DataFrame
print(df)

# حفظ كملف CSV إذا لزم الأمر
df.to_csv('sales.csv', index=False)
```

لمزيد من التفاصيل، راجع [توثيق pandas حول read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html). إذا واجهت أخطاء، تحقق من تنسيق ملف Excel وتأكد من تثبيت الحزم المطلوبة.