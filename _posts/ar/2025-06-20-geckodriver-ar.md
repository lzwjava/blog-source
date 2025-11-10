---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت سيلينيوم جيكو درايفر على أوبونتو
translated: true
type: note
---

لتركيب مشغل فايرفوكس لـ Selenium (geckodriver) على أوبونتو، اتبع الخطوات التالية:

1. **ثبّت فايرفوكس** (إذا لم يكن مثبتًا بالفعل):
   ```bash
   sudo apt update
   sudo apt install firefox
   ```

2. **حمّل geckodriver**:
   - زر [صفحة إصدارات geckodriver](https://github.com/mozilla/geckodriver/releases).
   - اختر أحدث إصدار متوافق مع إصدار فايرفوكس لديك. لأوبونتو، حمّل إصدار Linux 64-bit (مثل `geckodriver-vX.XX.X-linux64.tar.gz`).
   - مثال لأمر التحميل (استبدل `X.XX.X` بأحدث إصدار):
     ```bash
     wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
     ```

3. **استخرج الملف المحمّل**:
   ```bash
   tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
   ```

4. **انقل geckodriver إلى مسار النظام**:
   - انقل الملف المستخرج `geckodriver` إلى `/usr/local/bin` لجعله متاحًا على مستوى النظام:
     ```bash
     sudo mv geckodriver /usr/local/bin/
     ```
   - اجعله قابلاً للتنفيذ:
     ```bash
     sudo chmod +x /usr/local/bin/geckodriver
     ```

5. **ثبّت Selenium لـ Python** (إذا كنت تستخدم Python):
   ```bash
   pip install selenium
   ```

6. **تحقق من التثبيت**:
   - تحقق من إصدار geckodriver:
     ```bash
     geckodriver --version
     ```
   - اختبر باستخدام سكريبت Python بسيط:
     ```python
     from selenium import webdriver

     driver = webdriver.Firefox()
     driver.get("https://www.example.com")
     print(driver.title)
     driver.quit()
     ```

**ملاحظات**:
- تأكد من أن إصدار فايرفوكس لديك متوافق مع إصدار geckodriver (راجع ملاحظات الإصدار على صفحة geckodriver في GitHub).
- إذا واجهت مشاكل، تأكد من تثبيت `python3-pip`:
  ```bash
  sudo apt install python3-pip
  ```
- إذا لم يتم العثور على geckodriver، أضف `/usr/local/bin` إلى `PATH` الخاص بك:
  ```bash
  export PATH=$PATH:/usr/local/bin
  ```

هذا يجب أن يجهز مشغل فايرفوكس لـ Selenium على أوبونتو. أعلمني إذا واجهت أي مشاكل!

---

الفرق بين `geckodriver-v0.36.0-linux-aarch64.tar.gz` و `geckodriver-v0.36.0-linux64.tar.gz` يكمن في بنية المعالج المستهدف:

- **linux-aarch64**: هذا مخصص لبنى ARM 64-bit (مثل ARMv8-A)، شائع الاستخدام في أجهزة مثل Raspberry Pi، أو بعض الخوادم، أو أنظمة Linux الحديثة القائمة على ARM. "aarch64" ترمز إلى بنية ARM 64-bit.

- **linux64**: هذا مخصص لبنى x86 64-bit (المعروفة أيضًا باسم x86_64 أو AMD64)، وهي المعيارية لمعظم أجهزة الكمبيوتر المكتبية والخوادم التي تشغل Linux.

**نقاط رئيسية**:
- اختر `linux-aarch64` إذا كان نظامك يحتوي على معالج ARM 64-bit.
- اختر `linux64` إذا كان نظامك يحتوي على معالج x86 64-bit.
- يمكنك التحقق من بنية نظامك على Linux بتشغيل الأمر `uname -m`. إذا أظهر الناتج `aarch64`، استخدم إصدار ARM؛ إذا أظهر `x86_64`، استخدم إصدار linux64.

ملفات `.asc` هي توقيعات GPG للتحقق من سلامة وصحة ملفات `.tar.gz` المقابلة.