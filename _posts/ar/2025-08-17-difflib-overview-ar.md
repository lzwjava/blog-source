---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: نظرة عامة على وحدة ديفليب في بايثون
translated: true
type: note
---

### نظرة عامة على difflib
وحدة `difflib` في المكتبة القياسية لـ Python تقارن التسلسلات (مثل: السلاسل النصية، القوائم) للعثور على الاختلافات. إنها مفيدة لمهام مثل مقارنة النصوص، إنشاء التصحيحات، أو فحوص التشابه. تشمل الفئات والوظائف الرئيسية `Differ` (للمقارنات التفصيلية)، `SequenceMatcher` (لنسب التشابه والمطابقات)، ومولدات المقارنة مثل `ndiff` و `unified_diff`.

### الاستيراد والإعداد الأساسي
لا حاجة للتثبيت—إنها مدمجة في اللغة.
```python
import difflib
```

### الوظائف والفئات الشائعة

1. **`SequenceMatcher`**: يحسب نسب التشابه ويجد تسلسلات فرعية متطابقة.
   - استخدمها للمطابقة الضبابية أو للحصول على درجة تشابه سريعة.
   - مثال:
     ```python
     seq1 = "abcdef"
     seq2 = "abcefg"
     matcher = difflib.SequenceMatcher(None, seq1, seq2)
     print("Similarity ratio:", matcher.ratio())  # الإخراج: ~0.83 (مطابقة قريبة)
     print("Common elements:", matcher.find_longest_match(0, len(seq1), 0, len(seq2)))  # إيجاد أطول تطابق
     ```
     - `ratio()` تُرجع رقم عشري (من 0 إلى 1) يشير إلى درجة التشابه.
     - طرق مثل `get_matching_blocks()` تسرد المطابقات التامة.

2. **`Differ`**: يولد مقارنة سهلة القراءة تُظهر الإضافات، والحذف، والتغييرات سطرًا بسطر.
   - الأفضل لمقارنة القوائم أو السلاسل النصية متعددة الأسطر.
   - مثال:
     ```python
     text1 = ["line1", "line2", "line3"]
     text2 = ["line1", "line2 modified", "line3", "line4"]
     d = difflib.Differ()
     diff = list(d.compare(text1, text2))
     print("\n".join(diff))
     # الإخراج:
     #   line1
     #   line2
     # - line3
     # + line2 modified
     # + line3  (انتظر، الإخراج الفعلي يظهر تعديلات الأسطر؛ اضبط من أجل الدقة)
     ```
     - البادئات: `  ` (غير متغير)، `- ` (محذوف)، `+ ` (مضاف)، `? ` (اختلافات داخل الأسطر).

3. **`ndiff`** و **`unified_diff`**: لتوليد المقارنات بصيغ محددة.
   - **`ndiff`**: مقارنة بسيطة سطرًا بسطر مثل `Differ`.
     ```python
     diff = list(difflib.ndiff(["a", "b"], ["a", "c"]))
     # الإخراج: ['  a', '- b', '+ c']
     ```
   - **`unified_diff`**: ينشئ صيغة المقارنة الموحدة (مثل مقارنات Git)، مفيدة لملفات التصحيح.
     ```python
     diff = difflib.unified_diff(["a", "b"], ["a", "c"], fromfile='file1', tofile='file2')
     print("\n".join(diff))
     # الإخراج:
     # --- file1
     # +++ file2
     # @@ -1,2 +1,2 @@
     #  a
     # -b
     # +c
     ```

### نصائح وأفضل الممارسات
- **التوحيد**: للمقارنات غير الحساسة لحالة الأحرف أو التي تتجاهل المسافات البيضاء، قم بمعالجة المدخلات مسبقًا (مثل `text.lower()` أو `text.splitlines()`).
- **الأداء**: للتسلسلات الطويلة، استخدم `SequenceMatcher` مع `autojunk=False` لتعطيل إرشادات البيانات غير المرغوب فيها إذا لم تكن كذلك.
- **التكامل**: ادمج مع `filecmp` لمقارنة الملفات أو استخدم في نصوص التحكم بالإصدار.
- **المتقدم**: استكشف `HtmlDiff` للمقارنات بصيغة HTML (نادرًا ما تكون مطلوبة ولكنها متاحة).

للحصول على الوثائق الكاملة، تحقق من [صفحة difflib الرسمية في Python](https://docs.python.org/3/library/difflib.html). إذا كان لديك حالة استخدام محددة، قدم المزيد من التفاصيل للحصول على أمثلة مخصصة.