---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: فتح سوبلايم تيكست من سطر الأوامر
translated: true
type: note
---

### فتح Sublime Text من سطر الأوامر (CLI)

لا يتضمن Sublime Text أمر `sublime` (أو `subl`) مدمجًا بشكل افتراضي على نظام macOS (وهو ما يبدو أنك تستخدمه، بناءً على الإشارة إلى `open -a`). ومع ذلك، هناك طريقة رسمية وبسيطة لإضافته باستخدام نص `subl` المرفق مع Sublime. هذا أنظف من الاعتماد على أمر `open`. سأرشدك خلال الخيارات أدناه، بدءًا بالطريقة الموصى بها.

#### 1. **تثبيت أمر `subl` الرسمي لسطر الأوامر (موصى به)**
يتضمن Sublime Text ملفًا تنفيذيًا باسم `subl` في حزمة التطبيق الخاصة به يمكنك إنشاء رابط رمزي له إلى دليل في المسار PATH الخاص بك (مثل `/usr/local/bin`). هذا يتيح لك تشغيل `subl .` (لفتح الدليل الحالي) أو `subl file.txt` من أي مكان في الطرفية.

**الخطوات لنظام macOS (Sublime Text 3 أو 4):**
- افتح Terminal.
- نفّذ هذا الأمر لإنشاء الرابط الرمزي (يتطلب صلاحيات المسؤول، لذا سيتم طلب كلمة المرور الخاصة بك):
  ```
  sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
  ```
  - إذا كنت تستخدم Sublime Text 3، فقد يكون المسار مختلفًا قليلاً: `"/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"` (اضبط رقم الإصدار حسب الحاجة).
  - إذا لم يكن `/usr/local/bin` موجودًا في المسار PATH الخاص بك، أضفه إلى ملف تعريف shell الخاص بك (مثل `~/.zshrc` أو `~/.bash_profile`):
    ```
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

- اختبره: انتقل إلى دليل (مثل `cd ~/Desktop`) وشغّل:
  ```
  subl .
  ```
  يجب أن يفتح هذا Sublime Text مع تحميل المجلد الحالي.

إذا لم يعمل مسار الرابط الرمزي (بسبب اختلافات في الإصدار مثلًا)، تحقق من الموقع الدقيق:
- نفّذ `find /Applications/Sublime\ Text.app -name subl` لتحديد موقع الملف الثنائي.

**لماذا هذه الطريقة جيدة:**
- إنها رسمية وخفيفة الوزن—لا حاجة لأدوات خارجية.
- تعمل على مستوى النظام بالكامل، مثل CLI حقيقي.
- حتى أن Sublime Text 4 لديه خيار في وحدة التحكم (View > Show Console) لتشغيل `sublime_installation` أو ما شابه، ولكن الرابط الرمزي هو الأكثر موثوقية.

**إذا كنت تستخدم Linux أو Windows:**
- Linux: عملية إنشاء رابط رمزي مشابهة—مثل `sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl`.
- Windows: أضف `C:\Program Files\Sublime Text\sublime_text.exe` إلى المسار PATH الخاص بك، أو استخدم ملف batch لـ `subl`.

#### 2. **الخيار الاحتياطي: استخدام أمر `open` (لا حاجة للتثبيت)**
إذا كنت لا تريد التعامل مع الروابط الرمزية أو المسار PATH، فإن الأمر المدمج `open` في نظام macOS يعمل بشكل رائع للاستخدام الأساسي. وهو متاح بالفعل في كل مكان.

- لفتح الدليل الحالي في Sublime:
  ```
  open -a "Sublime Text" .
  ```
  - ملاحظة: استخدم `"Sublime Text"` (مع مسافة) إذا كان هذا هو اسم التطبيق لديك. إذا كان مجرد "Sublime.app"، فاضبط accordingly. يمكنك التحقق من الاسم الدقيق في `/Applications/`.

- لفتح ملف محدد:
  ```
  open -a "Sublime Text" filename.txt
  ```

- اجعله اسمًا مستعارًا للراحة: أضف هذا إلى ملف تعريف shell الخاص بك (`~/.zshrc` أو `~/.bash_profile`) لمحاكاة `subl`:
  ```
  alias subl='open -a "Sublime Text"'
  ```
  ثم أعد التحميل باستخدام `source ~/.zshrc` واستخدم `subl .` كالمعتاد.

**الإيجابيات/السلبيات:**
- بسيط جدًا ولا يتطلب إعداد.
- لكنه مقتصر على نظام macOS وأقل مرونة (على سبيل المثال، لا توجد طريقة سهلة لتحديد الأسطر أو المشاريع كما هو الحال مع `subl`).

#### استكشاف الأخطاء وإصلاحها
- **أمر غير موجود؟** تأكد من أن المسار PATH الخاص بك يتضمن `/usr/local/bin` (نفّذ `echo $PATH` للتحقق).
- **التطبيق غير موجود؟** تحقق من وجود Sublime في `/Applications/`. إذا كان في مكان آخر (عبر Homebrew مثلًا: `brew install --cask sublime-text`)، فاضبط المسارات.
- **مشاكل في الأذونات؟** الرابط الرمزي يحتاج إلى sudo، ولكن بمجرد تعيينه، يكون الأمر على ما يرام.
- إذا كنت تستخدم مدير حزم مثل Homebrew، يمكنك تثبيت Sublime عبر `brew install --cask sublime-text`، وقد يقوم بالتعامل مع CLI نيابة عنك.

هذا يجب أن يجعلك تعمل بشكل جيد! إذا واجهت أخطاء أو حددت نظام التشغيل/الإصدار الخاص بك، يمكنني تحسين الخطوات.