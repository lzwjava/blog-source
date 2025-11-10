---
audio: false
generated: true
lang: ar
layout: post
title: الوصول إلى حافظة بايثون على أوبونتو
translated: true
type: note
---

لقراءة البيانات من الحافظة (pasteboard) في أوبنتو باستخدام بايثون، يمكنك استخدام مكتبات مثل `pyperclip` أو التفاعل مع أدوات الحافظة النظامية مثل `xclip` أو `xsel`. فيما يلي طريقتان شائعتان:

### الطريقة 1: استخدام `pyperclip`
`pyperclip` هي مكتبة بايثون متعددة المنصات للوصول إلى الحافظة.

1. **تثبيت pyperclip**:
   ```bash
   pip install pyperclip
   ```

2. **كود بايثون لقراءة محتوى الحافظة**:
   ```python
   import pyperclip

   # قراءة محتويات الحافظة
   clipboard_content = pyperclip.paste()
   print(clipboard_content)
   ```

3. **ملاحظات**:
   - تأكد من تثبيت `xclip` أو `xsel` على أوبنتو، لأن `pyperclip` تعتمد عليهما:
     ```bash
     sudo apt update
     sudo apt install xclip xsel
     ```
   - هذه الطريقة بسيطة وتعمل عبر مختلف المنصات.

### الطريقة 2: استخدام `xclip` مباشرة
إذا كنت تفضل التفاعل مع حافظة النظام مباشرة، يمكنك استخدام `xclip`.

1. **تثبيت xclip**:
   ```bash
   sudo apt update
   sudo apt install xclip
   ```

2. **كود بايثون لقراءة محتوى الحافظة باستخدام `xclip`**:
   ```python
   import subprocess

   # قراءة محتويات الحافظة
   process = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
   clipboard_content = process.stdout
   print(clipboard_content)
   ```

3. **ملاحظات**:
   - هذه الطريقة تستدعي أداة سطر الأوامر `xclip` مباشرة.
   - استخدم `-selection clipboard` للحافظة الحديثة (Ctrl+C/Ctrl+V) أو `-selection primary` لحافظة التحديد بالفأرة.
   - تأكد من تثبيت `xclip`.

### التوصيات
- **استخدم `pyperclip`** للبساطة وإمكانية النقل ما لم يكن لديك أسباب محددة لاستخدام `xclip` أو `xsel`.
- تتطلب كلتا الطريقتين تثبيت `xclip` أو `xsel` للوصول إلى الحافظة على أوبنتو.
- إذا كان محتوى الحافظة ليس نصياً (مثل صورة)، فقد لا تعمل هذه الطرق كما هو متوقع، وسوف تحتاج إلى مكتبة مثل `pyclip` أو معالجة إضافية للبيانات غير النصية.

تم الاختبار على أوبنتو 22.04 مع بايثون 3.10. إذا واجهت مشاكل، تأكد من تثبيت الأدوات المطلوبة (`xclip` أو `xsel`) وأن الحافظة تحتوي على بيانات نصية.