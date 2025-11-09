---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: التعامل مع المسارات عبر المنصات في بايثون
translated: true
type: note
---

### التعامل مع المسارات في ملفات إعدادات بايثون (INI) لأنظمة ويندوز ولينكس

توفّر بايثون أدوات قوية مثل `os.path` و `pathlib` و `configparser` لإدارة مسارات الملفات عبر المنصات. التحديات الرئيسية هي:
- **فاصلات المسارات**: يستخدم ويندوز `\` (شرطة مائلة عكسية)، بينما يستخدم لينكس `/` (شرطة مائلة أمامية). قد تخزن ملفات الإعداد INI مسارات تحتوي على `/` أو `\` أو `//` أو `\\` (على سبيل المثال، بسبب الـ Escaping أو الإدخال اليدوي).
- **العمليات الفرعية (Subprocess)**: عند تمرير المسارات إلى `subprocess` (مثل `subprocess.run`)، يجب أن تكون سلسلة نصية صالحة لنظام التشغيل. كل من `/` و `\` يعملان على ويندوز، لكن `\` هو الأصلي.
- **os.path**: هذه الوحدة النمطية واعية بالمنصة ولكنها تتطلب بناءًا دقيقًا (على سبيل المثال، عبر `os.path.join`).
- **عبر المنصات (Cross-platform)**: استخدم الشرطة المائلة الأمامية `/` في كل مكان في ملفات الإعداد للتبسيط — تقوم بايثون بتطبيعها على ويندوز. بالنسبة لفاصلات مختلطة، قم بالتطبيع عند القراءة.

#### أفضل الممارسات
1.  **تخزين المسارات في INI باستخدام الشرطة المائلة الأمامية (`/`)**: هذا يعمل في كل مكان دون مشاكل. تجنب استخدام `\` في ملفات الإعداد لمنع مشاكل الـ Escaping (على سبيل المثال، قد يُفسر `\n` كسطر جديد).
2.  **قراءة المسارات وتطبيعها**: استخدم `pathlib.Path` (موصى به، بايثون 3.4+ ) للمعالجة التلقائية. فهو يقبل الفواصل المختلطة ويطبعها إلى نمط المنصة.
3.  **لـ subprocess**: قم بالتحويل إلى `str(path)` — يستخدم الفواصل الأصلية لكنه يقبل `/` على ويندوز.
4.  **لـ os.path**: استخدم `os.path.normpath` لتنظيف الفواصل، أو فضّل استخدام `pathlib` لأنه أكثر حداثة.
5.  **الحالات الخاصة (Edge cases)**:
    - `//` (مسارات UNC على ويندوز أو المسار الجذر على لينكس): `pathlib` يتعامل مع UNC كـ `\\server\share`.
    - `\\` في ملف الإعداد: عالجها على أنها `\` تم escapeها؛ استبدلها أو اترك لـ `Path` أن يحللها.

#### مثال خطوة بخطوة
افترض وجود ملف INI (`config.ini`) يحتوي على مسارات مختلطة:

```
[settings]
windows_path = C:\Users\example\file.txt  ; شرطات مائلة عكسية
linux_path = /home/user/file.txt          ; شرطات مائلة أمامية
mixed_path = C://dir//file.txt            ; شرطات مائلة مزدوجة
escaped_path = C:\\dir\\file.txt          ; شرطات مائلة عكسية تم escapeها
```

##### 1. قراءة ملف الإعداد
استخدم `configparser` للتحميل. يقرأ القيم كسلاسل نصية خام، محافظًا على الفواصل.

```python
import configparser
from pathlib import Path
import os

config = configparser.ConfigParser()
config.read('config.ini')

# اقرأ المسارات كسلاسل نصية
win_path_str = config.get('settings', 'windows_path')
lin_path_str = config.get('settings', 'linux_path')
mixed_str = config.get('settings', 'mixed_path')
escaped_str = config.get('settings', 'escaped_path')
```

##### 2. تطبيع المسارات باستخدام `pathlib` (عبر المنصات)
`Path` تكتشف المنصة تلقائيًا وتطبع:
- تستبدل `\` أو `\\` بـ `/` داخليًا، وتخرج الفواصل الأصلية عبر `str()`.
- تتعامل مع المضاعفات مثل `//` كـ `/` مفرد.

```python
# تطبيع جميع المسارات
win_path = Path(win_path_str)      # تصبح Path('C:\\Users\\example\\file.txt') على ويندوز
lin_path = Path(lin_path_str)      # تبقى Path('/home/user/file.txt')
mixed_path = Path(mixed_str)       # تطبع إلى Path('C:\\dir\\file.txt') على ويندوز
escaped_path = Path(escaped_str)   // تحلل \\ كـ \ مفرد، تصبح Path('C:\\dir\\file.txt')

# لإجبار استخدام الشرطة المائلة الأمامية في كل مكان (لكتابة الإعداد أو قابلية النقل)
win_path_forward = str(win_path).replace('\\', '/')
print(win_path_forward)  # 'C:/Users/example/file.txt' على ويندوز
```

- **على ويندوز**: `str(win_path)` → `'C:\\Users\\example\\file.txt'` (أصلي).
- **على لينكس**: جميعها تصبح قائمة على `/`.
- استخدم `Path.resolve()` للمسارات المطلقة: `abs_path = win_path.resolve()` (يوسع `~` أو المسارات النسبية).

##### 3. الاستخدام مع `os.path` (قديم، لكن متوافق)
إذا كان يجب عليك استخدام `os.path`، قم بالتطبيع أولاً:

```python
import os

# تطبيع السلسلة النصية (يستبدل / و \ إلى الأصلي للمنصة)
normalized_win = os.path.normpath(win_path_str)  # 'C:\\Users\\example\\file.txt' على ويندوز
normalized_mixed = os.path.normpath(mixed_str)   // ينظف المضاعفات

# بناء مسارات جديدة
full_path = os.path.join(os.path.dirname(normalized_win), 'newfile.txt')
```

- `os.path.join` يستخدم دائمًا الفاصل الصحيح.
- تجنب ربط `\` يدويًا — استخدم `join`.

##### 4. التمرير إلى Subprocess
`subprocess` يقبل المسارات كسلاسل نصية. استخدم `str(Path)` للفواصل الأصلية، أو `/` (تعمل على كلا النظامين).

```python
import subprocess

# مثال: تشغيل ما يعادل 'ls' (dir على ويندوز، ls على لينكس) مع المسار
cmd = ['dir', str(win_path)] if os.name == 'nt' else ['ls', str(lin_path)]
result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
```

- **آمن عبر المنصات**: استخدم دائمًا `/` في السلسلة النصية: `subprocess.run(['cmd', win_path_forward])`.
- يتعامل مع UNC (`//server/share`) بشكل جيد على ويندوز.

##### 5. الكتابة مرة أخرى إلى ملف الإعداد (الحفاظ على إمكانية النقل)
عند الحفظ، استخدم `/` لضمان العمل في المستقبل:

```python
config.set('settings', 'normalized_path', str(win_path).replace('\\', '/'))
with open('config.ini', 'w') as f:
    config.write(f)
```

#### المزالق المحتملة
- **الـ Escaping في INI**: إذا ظهر `\` في القيم، فإن `configparser` لا يقوم بالـ escape تلقائيًا — `C:\n` تُقرأ كـ `\n` حرفي. استخدم `config.get` واترك لـ `Path` أن يحلل.
- **المسارات النسبية**: استخدم `Path.cwd() / rel_path` للحصول على المسارات المطلقة.
- **التحقق (Validation)**: تحقق من `path.exists()` بعد التطبيع.
- **إصدار بايثون**: `pathlib` في الإصدار 3.4+؛ استخدم `os.path` كبديل للإصدارات الأقدم.

هذا النهج يضمن تشغيل كودك دون تغيير على ويندوز/لينكس. اختبر باستخدام `python -m venv` على كليهما للتحقق.

#### المراجع
- [وثائق pathlib في بايثون](https://docs.python.org/3/library/pathlib.html)
- [وثائق configparser](https://docs.python.org/3/library/configparser.html)
- [وثائق subprocess](https://docs.python.org/3/library/subprocess.html)
- [وثائق os.path](https://docs.python.org/3/library/os.path.html)