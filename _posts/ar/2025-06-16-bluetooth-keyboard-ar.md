---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح مشاكل توصيل لوحة المفاتيح اللاسلكية
translated: true
type: note
---

بناءً على ناتج `bluetoothctl` الذي يظهر `[DEL] Device` عند محاولة الاتصال، إليك الحل الدقيق:

### الإصلاح الفوري لمشكلة حذف الاتصال
1. **إزالة سجلات الجهاز الموجودة** (أمر بالغ الأهمية للتكوينات القديمة):
   ```bash
   bluetoothctl
   remove F4:73:35:78:28:4E  # إزالة لوحة المفاتيح
   remove 24:27:30:24:C8:31   # إزالة الجهاز الذي قد يتسبب في التداخل
   exit
   ```

2. **إعادة تعيين مكدس البلوتوث**:
   ```bash
   sudo systemctl stop bluetooth
   sudo rm -rf /var/lib/bluetooth/*
   sudo systemctl start bluetooth
   ```

3. **إعادة الاقتران باستخدام التسلسل الصحيح**:
   ```bash
   bluetoothctl
   power on
   discoverable on
   pairable on
   agent on  # تمكين وكيل رمز المرور
   scan on
   ```
   - **ضع لوحة المفاتيح K380 في وضع الاقتران** (الضوء الوامض بسرعة)
   - عندما تظهر لوحة المفاتيح:
     ```bash
     pair F4:73:35:78:28:4E
     ```
   - **قم فورًا بكتابة رمز المرور المكون من 6 أرقام** المعروض على الشاشة (مثل `123456`) **على لوحة المفاتيح** ثم اضغط على Enter

4. **الاتصال فقط بعد الاقتران الناجح**:
   ```bash
   connect F4:73:35:78:28:4E
   trust F4:73:35:78:28:4E
   scan off
   quit
   ```

### لماذا يحدث هذا
- يحدث `[DEL] Device` لأن:
  - مكدس البلوتوث يكتشف فشل الاتصال ويقوم بتطهير سجل الجهاز
  - **خطوة الاقتران مفقودة** قبل محاولة الاتصال
  - احتمال وجود تداخل لاسلكي من أجهزة أخرى (مثل جهاز `midea`)

### فحوصات إضافية بالغة الأهمية
1. **التحقق من توصيل الهوائي**:
   - تأكد من أن هوائيات البلوتوث مثبتة في لوحة المنافذ الخلفية MSI motherboard's rear I/O panel

2. **التحقق من برامج التشغيل في النواة**:
   ```bash
   dmesg | grep -i bluetooth
   ```
   ابحث عن أخطاء مثل `hci0: command timeout` أو `Firmware failed to start`

3. **تحديد البرنامج الثابت** (إذا ظهرت أخطاء مهلة):
   ```bash
   sudo apt install linux-firmware
   ```

4. **الاختبار في بيئة محدودة**:
   ```bash
   sudo rfkill unblock all
   sudo systemctl stop NetworkManager  # إيقاف مؤقت
   sudo systemctl restart bluetooth
   ```

### إذا كان لا يزال فاشلاً
1. **طريقة بديلة للاقتران** (تجاوز الوكيل):
   ```bash
   echo -e 'remove F4:73:35:78:28:4E\npair F4:73:35:78:28:4E\nconnect F4:73:35:78:28:4E\ntrust F4:73:35:78:28:4E' | bluetoothctl
   ```

2. **التحقق من بطارية لوحة المفاتيح** (أمر بالغ الأهمية للبلوتوث):
   - استبدل البطارية إذا كان الجهد منخفضًا (تستخدم K380 بطاريتين من نوع CR2032)

3. **اختبار محول بلوتوث USB**:
   - إذا كانت هناك مشكلة في البلوتوث الداخلي، جرب محول CSR4.0 USB

**مؤشرات النجاح المتوقعة**:
- رسالة `Pairing successful`
- `Connection successful` في bluetoothctl
- ظهور `HIDP: Bluetooth HID device driver` في `dmesg`

بعد الاقتران، يجب أن تعمل لوحة المفاتيح K380 بشكل طبيعي بعد إعادة التشغيل. إذا تكرر انقطاع الاتصال، تحقق من `journalctl -u bluetooth -f` للبحث عن الأخطاء في الوقت الفعلي.