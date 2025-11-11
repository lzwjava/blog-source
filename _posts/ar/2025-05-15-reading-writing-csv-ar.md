---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: قراءة وكتابة ملفات CSV
translated: true
type: note
---

### مقدمة عن وحدة `csv` في بايثون

وحدة `csv` هي جزء من المكتبة القياسية لبايثون وتُستخدم لقراءة وكتابة ملفات CSV (قيم مفصولة بفواصل). وهي تتعامل مع تحليل الصفوف والأعمدة بكفاءة. لاستخدامها، قم أولاً باستيراد الوحدة: `import csv`. ستتعامل مع كائنات الملفات، التي تُفتح عادةً في وضع القراءة (`'r'`) أو وضع الكتابة (`'w'`).

المكونات الرئيسية:
- **القارئ (Reader)**: يحلل بيانات CSV من ملف (مثل `csv.reader()` للوصول القائم على الصفوف).
- **الكاتب (Writer)**: يُخرج البيانات إلى ملف CSV (مثل `csv.writer()`).
- يتم التعامل مع ملفات CSV كسلسلة من الصفوف، حيث يمثل كل صف قائمة من السلاسل النصية (الأعمدة).

لأسباب تتعلق بالأمان والسهولة، تعامل دائمًا مع الملفات باستخدام عبارات `with` لضمان الإغلاق السليم.

### قراءة ملف CSV أساسي

لقراءة ملف CSV:
```python
import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # كل 'row' هي قائمة بالأعمدة
```
- يقرأ هذا الكود الملف سطرًا بسطر. يمكنك الوصول إلى أعمدة محددة عن طريق الفهرس (مثل `row[0]` للعمود الأول).
- للعناوين، اقرأ الصف الأول بشكل منفصل: `headers = next(reader)`.

### مقارنة ملفّي CSV: الصفوف والأعمدة

لمقارنة ملفّي CSV (مثل `file1.csv` و `file2.csv`)، قم بتحميلهما في هياكل مثل قوائم القوائم (صفوف)، ثم قارن. الافتراضات: كلا ملفّي CSV لهما نفس الهيكل (نفس عدد الأعمدة/الصفوف). يمكن أن تتحقق المقارنات من التطابقات التامة، أو الاختلافات، أو منطق محدد (مثل المطابقة بناءً على عمود مفتاح).

#### المثال 1: مقارنة الصفوف (الصفوف بأكملها)
استخدم القواميس لتخزين الصفوف (إذا كان لها عمود معرف فريد) أو القوائم للمقارنة المباشرة.

```python
import csv

def compare_rows(file1, file2, key_column=0):
    # اقرأ file1 إلى قاموس (باستخدام key_column كمفتاح، والصف بأكمله كقيمة)
    data1 = {}
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        headers1 = next(reader1, None)  # تخطى العنوان إذا كان موجودًا
        for row in reader1:
            data1[row[key_column]] = row  # المفتاح هو العمود الأول على سبيل المثال

    # اقرأ file2 بطريقة مشابهة
    data2 = {}
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        headers2 = next(reader2, None)
        for row in reader2:
            data2[row[key_column]] = row

    # قارن
    common_keys = set(data1.keys()) & set(data2.keys())
    differing_rows = []
    for key in common_keys:
        if data1[key] != data2[key]:
            differing_rows.append((key, data1[key], data2[key]))
    
    return differing_rows  # قائمة من (key, row_from_file1, row_from_file2)

# الاستخدام
differences = compare_rows('file1.csv', 'file2.csv', key_column=0)  # المفتاح على العمود 0
print("Differing rows:", differences)
```

- **كيف يعمل**: يحول ملفات CSV إلى قواميس باستخدام عمود كمفتاح (مثل المعرف). يقارن الصفوف المتطابقة مباشرة. اضبط `key_column` لتحديد العمود الذي سيُستخدم كمفتاح.
- **الاختلافات**: للمقارنة سطرًا بسطر بدون مفاتيح، كرّر كلا القارئين في نفس الوقت (إذا كانا بنفس الترتيب/الطول).

#### المثال 2: مقارنة الأعمدة
قارن أعمدة محددة عبر الملف بأكمله (مثل التحقق مما إذا كانت قيم العمود 1 متطابقة في كلا الملفين).

```python
import csv

def compare_columns(file1, file2, col_index=0):
    # استخراج بيانات العمود كقوائم
    col1 = []
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        next(reader1, None)  # تخطى العنوان إذا لزم الأمر
        for row in reader1:
            if len(row) > col_index:
                col1.append(row[col_index])

    col2 = []
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        next(reader2, None)
        for row in reader2:
            if len(row) > col_index:
                col2.append(row[col_index])

    # قارن الأعمدة
    are_equal = col1 == col2
    differences = []
    for i, (val1, val2) in enumerate(zip(col1, col2)):
        if val1 != val2:
            differences.append((i, val1, val2))
    
    return are_equal, differences  # منطقية للمطابقة، قائمة من (row_index, val1, val2)

# الاستخدام
equal, diffs = compare_columns('file1.csv', 'file2.csv', col_index=1)  # قارن العمود 1
print("Columns equal?", equal)
print("Differences (row, val1, val2):", diffs)
```

- **كيف يعمل**: يستخرج العمود المحدد في قوائم، ثم يقارن عنصرًا بعنصر. يفترض أن ملفات CSV لها نفس عدد الصفوف؛ تعامل مع عدم التطابق إذا لزم الأمر.
- **الاختلافات**: استخدم `pandas` للعمليات المتقدمة على الأعمدة (مثل `df1['column'] == df2['column']`)، ولكن التزم بـ `csv` لاستخدام المكتبة القياسية البحتة.

#### نصائح وحالات خاصة
- **العناوين**: إذا كان لملفات CSV عناوين، فتخطها باستخدام `next(reader)`.
- **أنواع البيانات**: يقرأ CSV البيانات كسلاسل نصية؛ قم بتحويلها إلى int/float إذا لزم الأمر (مثل `int(row[0])`).
- **الملفات الكبيرة**: لملفات CSV الكبيرة، استخدم DictReader للوصول بالمفتاح: `csv.DictReader(file)` يُرجع الصفوف كـ OrderedDicts.
- **المُفَصِّل (Delimiter)**: استخدم `delimiter=';'` في القارئ/الكاتب إذا لم تكن البيانات مفصولة بفواصل.
- **الأخطاء**: ضع الكود داخل try-except لمشاكل الملفات؛ تحقق من أطوال الأعمدة لتجنب أخطاء الفهرس.
- **البدائل**: للمقارنات المعقدة، فكر في استخدام مكتبات مثل `pandas` (`df1.equals(df2)` للـ dataframes).

للحصول على الوثائق الكاملة، راجع [دليل وحدة csv الرسمي في بايثون](https://docs.python.org/3/library/csv.html). إذا كان لديك ملفات CSV محددة أو منطق مقارنة معين، قدم المزيد من التفاصيل للحصول على كود مخصص!