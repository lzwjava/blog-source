---
audio: false
generated: true
lang: ar
layout: post
title: رسائل السجل النظيفة
translated: true
type: note
---

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    يقرأ ملف سجل، يزيل أسطر السجل القياسية المكررة المتتالية بناءً على التشابه،
    ويكتب السجل النظيف إلى ملف محدد، مع افتراض الكتابة فوق ملف الإدخال افتراضيًا.

    Args:
        input_path (str, optional): مسار ملف سجل الإدخال. إذا كان None، يقرأ من stdin.
        output_path (str, optional): مسار ملف سجل الإخراج. إذا كان None، يكتب فوق ملف الإدخال.
        similarity_threshold (float, optional): نسبة التشابه (0.0 إلى 1.0) لاعتبار الأسطر مكررة. الافتراضي هو 1.0 (مطابقة تامة).
        lines_to_compare (int, optional): عدد الأسطر المتتالية للمقارنة. الافتراضي هو 1.
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("يجب أن يكون lines_to_compare عددًا صحيحًا أكبر من أو يساوي 1.")

    # تحديد مصدر الإدخال
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"خطأ: لم يتم العثور على الملف في المسار: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # قراءة جميع الأسطر من stdin

    # تحديد وجهة الإخراج
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"خطأ: غير قادر على فتح الملف للكتابة: {output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # الكتابة فوق ملف الإدخال
        except IOError:
            print(f"خطأ: غير قادر على فتح الملف للكتابة: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # الافتراضي إلى stdout إذا لم يكن هناك input_path

    num_lines = len(lines)
    i = 0
    removed_lines = 0
    while i < num_lines:
        # جمع 'lines_to_compare' أسطر أو الأسطر المتبقية إذا كانت أقل من 'lines_to_compare'
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # المعالجة فقط إذا كان لدينا عدد كافٍ من الأسطر للمقارنة
        if len(current_lines) == lines_to_compare:
            # استخراج المعلومات القياسية من المجموعة الأولى من الأسطر
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"سطر غير قياسي: {line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # إيقاف معالجة هذه المجموعة إذا تم العثور على سطر غير قياسي

            if all_standard:
                # استخراج المعلومات القياسية من المجموعة الثانية من الأسطر (إذا كانت متاحة)
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # معاملة الأسطر التالية كغير قياسية إذا كان أي منها غير قياسي
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"التشابه: {similarity:.4f}, العتبة: {similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"تخطي الأسطر المكررة: { ''.join([line.strip() for line in current_lines])}")
                            removed_lines += len(current_lines)
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # الانتقال إلى المجموعة التالية من الأسطر
        else:
            # معالجة الأسطر المتبقية (أقل من 'lines_to_compare')
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"سطر غير قياسي: {line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

    if output_path or input_path:
        outfile.close()

    print(f"تمت إزالة {removed_lines} سطرًا مكررًا.")


def is_valid_similarity_threshold(value):
    """
    التحقق مما إذا كانت القيمة المعطاة عبارة عن عتبة تشابه صالحة.
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("يجب أن تكون عتبة التشابه رقمًا عشريًا.")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("يجب أن تكون عتبة التشابه بين 0.0 و 1.0.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="تنظيف أسطر السجل المكررة من ملف أو stdin والكتابة إلى ملف، مع افتراض الكتابة فوق ملف الإدخال افتراضيًا.")
    parser.add_argument("input_path", nargs="?", type=str, help="مسار ملف سجل الإدخال (اختياري، الافتراضي هو stdin)")
    parser.add_argument("-o", "--output_path", type=str, help="مسار ملف سجل الإخراج (اختياري، الافتراضي هو الكتابة فوق ملف الإدخال)")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="عتبة التشابه (0.0-1.0) لاعتبار الأسطر مكررة (الافتراضي: 1.0)")
    parser.add_argument("-l", "--lines", type=int, default=1, help="عدد الأسطر المتتالية للمقارنة (الافتراضي: 1)")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

سكريبت Python هذا `clean_log.py` مصمم لإزالة أسطر السجل المكررة من ملف أو الإدخال القياسي. يستخدم عتبة تشابه لتحديد ما إذا كانت أسطر السجل المتتالية متشابهة بما يكفي لاعتبارها مكررة.

فيما يلي تفصيل للكود:

**1. الاستيرادات:**

- `sys`: تُستخدم للتفاعل مع مترجم Python، مثل القراءة من stdin والكتابة إلى stderr.
- `argparse`: تُستخدم لإنشاء واجهة سطر أوامر.
- `difflib.SequenceMatcher`: تُستخدم لمقارنة التشابه بين تسلسلات السلاسل النصية.

**2. دالة `clean_log`:**

- تأخذ `input_path`، `output_path`، `similarity_threshold`، و `lines_to_compare` كوسائط.
- `input_path`: يحدد ملف سجل الإدخال. إذا كان `None`، فإنه يقرأ من stdin.
- `output_path`: يحدد ملف الإخراج. إذا كان `None`، وتم إعطاء `input_path`، فإنه يكتب فوق ملف الإدخال. إذا كان كلاهما `None`، فإنه يكتب إلى stdout.
- `similarity_threshold`: عدد عشري بين 0.0 و 1.0 يحدد الحد الأدنى لنسبة التشابه لاعتبار الأسطر مكررة. قيمة 1.0 تعني أنه يتم إزالة الأسطر المتطابقة فقط.
- `lines_to_compare`: عدد صحيح يحدد عدد الأسطر المتتالية للمقارنة من حيث التشابه.

- **معالجة الإدخال:**
    - يقرأ الأسطر من ملف الإدخال أو stdin.
    - يتعامل مع `FileNotFoundError` إذا كان ملف الإدخال غير موجود.

- **معالجة الإخراج:**
    - يفتح ملف الإخراج للكتابة أو يستخدم stdout.
    - يتعامل مع `IOError` إذا تعذر فتح ملف الإخراج.

- **منطق إزالة التكرار:**
    - يتكرر عبر أسطر ملف السجل في أجزاء من `lines_to_compare`.
    - لكل جزء:
        - يقسم كل سطر إلى أجزاء بناءً على الفاصل " | "، متوقعًا أربعة أجزاء: level، timestamp، thread، و message.
        - إذا لم يكن للسطر أربعة أجزاء، فإنه يعتبر سطرًا "غير قياسي" ويتم طباعته إلى الإخراج دون مقارنة.
        - إذا كانت جميع الأسطر في الجزء الحالي قياسية، فإنه يقارنها بالأسطر `lines_to_compare` التالية.
        - يستخدم `SequenceMatcher` لحساب نسبة التشابه بين السلاسل النصية المجمعة لأجزاء thread و message للجزء الحالي والجزء التالي.
        - إذا كانت نسبة التشابه أقل من `similarity_threshold`، يتم طباعة جزء الأسطر الحالي إلى الإخراج.
        - إذا كانت نسبة التشابه أكبر من أو تساوي `similarity_threshold`، يعتبر جزء الأسطر الحالي مكررًا ويتم تخطيه.
    - يتعامل مع الأسطر المتبقية في نهاية الملف (أقل من `lines_to_compare` أسطر).

- **الإحصائيات:**
    - يتتبع عدد الأسطر التي تمت إزالتها.
    - يطبع عدد الأسطر التي تمت إزالتها إلى وحدة التحكم.

- **إغلاق الملف:**
    - يغلق ملف الإخراج إذا كان مفتوحًا.

**3. دالة `is_valid_similarity_threshold`:**

- دالة مساعدة تستخدمها `argparse` للتحقق من صحة وسيطة عتبة التشابه.
- تتحقق مما إذا كانت قيمة الإدخال عددًا عشريًا بين 0.0 و 1.0.

**4. كتلة `if __name__ == "__main__":`:**

- يتم تنفيذ هذه الكتلة عند تشغيل السكريبت من سطر الأوامر.
- تستخدم `argparse` لإنشاء محلل وسائط سطر الأوامر.
- تحدد الوسائط التالية:
    - `input_path`: مسار ملف سجل الإدخال (اختياري).
    - `-o` أو `--output_path`: مسار ملف سجل الإخراج (اختياري).
    - `-s` أو `--similarity`: عتبة التشابه (الافتراضي: 1.0).
    - `-l` أو `--lines`: عدد الأسطر للمقارنة (الافتراضي: 1).
- تقوم بتحليل وسائط سطر الأوامر باستخدام `parser.parse_args()`.
- تستدعي دالة `clean_log` مع الوسائط التي تم تحليلها.

**باختصار، يوفر السكريبت طريقة مرنة لتنظيف ملفات السجل عن طريق إزالة الأسطر المكررة بناءً على عتبة تشابه قابلة للتكوين وعدد الأسطر للمقارنة. وهو يدعم القراءة من stdin، والكتابة إلى stdout، والكتابة فوق ملف الإدخال.**