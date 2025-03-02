---
audio: false
generated: false
lang: ar
layout: post
title: تتبع أموال منزلنا
translated: true
---

مؤخرًا، قمت بإنشاء مستند Markdown لتتبع المعاملات المالية المتعلقة بمنزلنا.

المنزل ملك لي ولزوجتي. قدم لي والداي مبلغًا من المال، وقمنا باقتراض مبلغ آخر من أختي وخالي. على الرغم من أن خالي أرسل لي المال، إلا أن والدي قام لاحقًا بسداد هذا المبلغ.

قمنا بدفع 50% من إجمالي سعر المنزل كدفعة أولى، واقترضنا النصف الآخر من بنك الزراعة الصيني. العقد يمتد لمدة 20 عامًا، ومعدل الفائدة الحالي هو 3.65%.

عندما كنت عاطلًا عن العمل، قدمت لي زوجتي ووالدي الأموال اللازمة لتغطية أقساط الرهن الشهرية. وبالتالي، هناك العديد من المعاملات المتضمنة.

أستخدم بنك China Merchants Bank كبنكي الرئيسي. يسمح بنك China Merchants Bank بتصفية المعاملات حسب ما إذا كانت واردة أو صادرة، وحسب الحد الأدنى للمبلغ. كما يدعم التصفية باستخدام الكلمات الرئيسية، وهو أمر مفيد جدًا.

جانب آخر مفيد هو انتشار الذكاء الاصطناعي. يمكن أن يساعد أيضًا في هذه المهمة. باستخدام تقنية OCR المدعومة بالذكاء الاصطناعي، وتحديدًا Grok، تمكنت من استخراج النصوص من سجلات المعاملات مع مكتب كهرباء Guangzhou.

نظرًا لأن الجدول اللاحق يعتمد على الأرقام السابقة، فمن الأفضل التحقق من الأرقام أولاً للتأكد من أن كل شيء صحيح قبل المضي قدمًا.

الكود أدناه يساعد في إنشاء ملف PDF من مستند Markdown. يحتوي على بعض الإعدادات الخاصة لدعم عرض الأحرف الصينية في ملف PDF.

```python
import os
import subprocess

# الإعدادات
CJK_FONT = "Heiti SC"
GEOMETRY = "margin=1in"
input_markdown_path = "mortgage.md"  # استبدل بمسار ملف Markdown الخاص بك
output_pdf_path = "mortgage.pdf"    # استبدل بمسار ملف PDF المطلوب

# التحقق من وجود ملف الإدخال
if not os.path.exists(input_markdown_path):
    raise Exception(f"ملف الإدخال غير موجود: {input_markdown_path}")

# بناء أمر Pandoc
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]

# تنفيذ أمر Pandoc
try:
    subprocess.run(command, check=True)
    print(f"تم إنشاء ملف PDF بنجاح: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"حدث خطأ أثناء إنشاء ملف PDF: {e}")
```