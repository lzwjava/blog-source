---
audio: false
generated: true
lang: ar
layout: post
title: 'التحقق من ملفات qBittorrent: التجزئة باستخدام SHA-1'
translated: true
type: note
---

عندما تنقل مواقع الملفات في qBittorrent وتقوم بالتحقق من الملفات مرة أخرى قبل التوزيع، فإنها تتأكد من أن الملفات في الموقع الجديد هي نفسها التي كانت تعمل معها في الأصل. هذا التحقق بالغ الأهمية في التورنت لمنع مشاركة بيانات غير صحيحة أو تالفة. إليك كيف تعمل العملية وما هي الخوارزمية التي تستخدمها:

### كيف تتحقق qBittorrent من الملفات
لا تثق qBittorrent ببساطة بأن الملفات المنقولة صحيحة — بل تتحقق من سلامتها بمقارنتها بالمعلومات المخزنة في ملف التورنت. في التورنت، يتم تقسيم البيانات إلى أجزاء أصغر تسمى **قطع**، ولكل قطعة قيمة هاش فريدة. يتم تضمين هذه الهاشات في ملف التورنت وتعمل كبصمة لكل جزء من البيانات. عندما تنقل الملفات إلى موقع جديد، تستخدم qBittorrent هاشات القطع هذه لتأكيد أن الملفات لم تتغير.

يمكن تقسيم العملية إلى هذه الخطوات:

1. **تحديد الموقع الجديد**: تخبر qBittorrent بمكان وجود الملفات الآن عن طريق تعيين مسار الملف الجديد.
2. **ربط الملفات بالتورنت**: تقوم qBittorrent بمطابقة الملفات في الموقع الجديد مع الملفات المدرجة في التورنت، عادةً باستخدام أسماء الملفات وأحجامها (نظرًا لأن هذه المعلومات موجودة في ملف التورنت).
3. **التحقق من هاشات القطع**: تقرأ qBittorrent البيانات من الملفات الجديدة قطعة قطعة، وتحسب هاش لكل قطعة، وتقارنه بالهاش المقابل المخزن في ملف التورنت.
4. **تأكيد السلامة**: إذا تطابقت جميع الهاشات المحسوبة مع هاشات التورنت، يتم تأكيد أن الملفات متطابقة، ويمكن لـ qBittorrent استئناف التوزيع. إذا لم يتطابق هاش أي قطعة، يتم وضع علامة على تلك القطعة على أنها غير مكتملة أو مفقودة، وقد تحتاج qBittorrent إلى إعادة تحميلها.

### ما هي الخوارزمية التي تستخدمها؟
لا تستخدم qBittorrent checksum للملف بالكامل (مثل MD5 أو SHA-256 للملف بأكمله)، لأن ذلك سيكون بطيئًا وغير فعال، خاصة بالنسبة للملفات الكبيرة. بدلاً من ذلك، تعتمد على **هاشات القطع** المحددة بواسطة بروتوكول BitTorrent. الخوارزمية المستخدمة لهاشات القطع هذه هي **SHA-1**، وهي دالة هاش تشفيرية مستخدمة على نطاق واسع. يتم عمل هاش لكل قطعة بيانات (والتي يمكن أن تتراوح من بضعة كيلوبايت إلى بضعة ميجابايت، اعتمادًا على التورنت) باستخدام SHA-1، وهذه الهاشات هي ما تتحقق منه qBittorrent.

استخدام هاشات القطع بدلاً من checksum للملف بالكامل له ميزتان كبيرتان:
- **الكفاءة**: التحقق من القطع الأصغر أسرع من عمل هاش لملف كامل.
- **التفصيل**: إذا كان هناك خطأ ما، يمكن لـ qBittorrent تحديد القطع التي تحتاج إلى إصلاح بدقة، بدلاً من رفض الملف بأكمله.

### لماذا هذا الأمر مهم
يضمن هذا التحقق القائم على الهاش أن البيانات التي تقوم بتوزيعها من الموقع الجديد تطابق ما يتوقعه الأقران الآخرون، مما يحافظ على سلامة سرب التورنت. بدون هذا الفحص، قد يؤدي نقل الملفات إلى مشاركة بيانات تالفة أو غير متطابقة، مما يعطل عملية التورنت.

باختصار، عندما تنقل مواقع الملفات في qBittorrent، فإنها تعيد فحص الملفات عن طريق حساب **هاشات SHA-1** لكل قطعة ومقارنتها بالهاشات في ملف التورنت. هذه هي الطريقة التي تؤكد بها أن كل شيء صحيح قبل استئناف التوزيع.

---

لتوضيح كيفية تحقق qBittorrent من سلامة الملفات باستخدام هاشات القطع (تحديدًا هاشات SHA-1) عند نقل مواقع الملفات، إليك برنامج نصي بسيط بلغة Python. تتبع qBittorrent، وفقًا لبروتوكول BitTorrent، تقسيم الملفات إلى قطع، وتحسب هاشات SHA-1 لكل قطعة، وتستخدم هذه الهاشات لضمان بقاء محتوى الملف دون تغيير، بغض النظر عن موقعه. يحاكي هذا البرنامج النصي تلك العملية عن طريق إنشاء ملف نموذجي، وحساب هاشات قطعه، والتحقق من نسخة مطابقة له، ثم إظهار كيف يؤدي التعديل إلى فشل التحقق.

### الشرح
- **هاشات القطع**: يقسم البرنامج النصي الملف إلى قطع بحجم ثابت (مثلاً 10 بايت) ويحسب هاشات SHA-1 لكل قطعة، محاكيًا كيفية تخزين ملف التورنت لهذه الهاشات.
- **التحقق**: يتحقق مما إذا كانت الهاشات المحسوبة للملف تطابق الهاشات المتوقعة، مما يضمن السلامة.
- **المحاكاة**: ينشئ ملفًا، وينسخه (محاكاة النقل)، ثم يتحقق منه، ثم يعدل النسخة ويتحقق مرة أخرى لإظهار كيفية اكتشاف التغييرات.

إليك البرنامج النصي مع التعليقات للتوضيح:

```python
import hashlib
import shutil
import os

def compute_piece_hashes(file_path, piece_size):
    """Compute SHA-1 hashes for each piece of the file."""
    hashes = []
    with open(file_path, 'rb') as f:
        while True:
            piece = f.read(piece_size)
            if not piece:
                break
            hash_obj = hashlib.sha1(piece)
            hashes.append(hash_obj.hexdigest())
    return hashes

def verify_file_integrity(file_path, piece_size, expected_hashes):
    """Verify the file's integrity by comparing piece hashes."""
    current_hashes = compute_piece_hashes(file_path, piece_size)
    if len(current_hashes) != len(expected_hashes):
        return False
    for current, expected in zip(current_hashes, expected_hashes):
        if current != expected:
            return False
    return True

# Create a sample file with known content
with open('file1.txt', 'w') as f:
    f.write("Hello, this is a test file.")

piece_size = 10  # bytes, small for demonstration

# Compute expected hashes from file1.txt (simulates torrent hashes)
expected_hashes = compute_piece_hashes('file1.txt', piece_size)
print("Expected hashes:", [h[:8] for h in expected_hashes])  # Show first 8 chars for readability

# Copy file1.txt to file2.txt to simulate moving the file
shutil.copyfile('file1.txt', 'file2.txt')

# Verify file2.txt against expected hashes (should pass)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (unchanged):", "Valid" if is_valid else "Invalid")

# Modify file2.txt to simulate corruption or change
with open('file2.txt', 'a') as f:
    f.write(" Modified")

# Verify again (should fail due to changed content)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (modified):", "Valid" if is_valid else "Invalid")

# Clean up the created files
os.remove('file1.txt')
os.remove('file2.txt')
```

### كيف يعمل
1. **إنشاء الملف**: يكتب "Hello, this is a test file." (25 بايت) في `file1.txt`.
2. **حساب الهاش**: يقسم `file1.txt` إلى قطع بحجم 10 بايت لكل منها (مثلاً، "Hello, thi", "s is a tes", "t file.")، ويحسب هاشات SHA-1، ويخزنها كـ `expected_hashes`.
3. **محاكاة النقل**: ينسخ `file1.txt` إلى `file2.txt`، ممثلًا ملفًا نُقل إلى موقع جديد.
4. **التحقق الأولي**: يتحقق من `file2.txt` مقابل `expected_hashes`. نظرًا لأن المحتوى متطابق، يطبع "Valid".
5. **التعديل**: يلحق " Modified" بـ `file2.txt`، مما يغير محتواه وحجمه (أصبح الآن 34 بايت، مقسم إلى 4 قطع).
6. **التحقق الثاني**: يتحقق من `file2.txt` المعدل. يختلف عدد القطع أو هاشاتها، لذا يطبع "Invalid".
7. **التنظيف**: يحذف الملفات المؤقتة.

### مثال على الناتج
```
Expected hashes: ['dffd6021', 'a2b3c4d5', 'e6f789ab']  # Example hash prefixes
Verification of file2.txt (unchanged): Valid
Verification of file2.txt (modified): Invalid
```
(ستختلف قيم الهاش الفعلية ولكنها تتبع هذا النمط).

يوضح هذا البرنامج النصي كيف تضمن qBittorrent سلامة الملفات من خلال مقارنة هاشات القطع، وكشف أي تغييرات حتى بعد نقل الملف، مما يجعله عرضًا بسيطًا وفعالًا للعملية.