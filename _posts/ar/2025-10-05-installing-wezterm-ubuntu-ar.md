---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تثبيت WezTerm على أوبونتو
translated: true
type: note
---

يحدث الخطأ "Unable to locate package wezterm" لأن WezTerm غير متوفر في مستودعات Ubuntu الافتراضية. تحتاج أولاً إلى إضافة مستودع الطرف الثالث الرسمي. إليك الحل خطوة بخطوة باستخدام طريقة APT الأصلية (موصى بها للتكامل السلس):

1. أضف مفتاح GPG للمستودع:  
   ```
   curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
   ```

2. أضف المستودع إلى مصادرك:  
   ```
   echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
   ```

3. عيّن الأذونات الصحيحة على ملف المفتاح:  
   ```
   sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
   ```

4. حدّث قائمة الحزم الخاصة بك:  
   ```
   sudo apt update
   ```

5. الآن قم بتثبيت WezTerm:  
   ```
   sudo apt install wezterm
   ```

بمجرد التثبيت، يمكنك تشغيله باستخدام `wezterm` من الطرفية. إذا كنت تفضل الإصليل الليلي (الأحدث) بدلاً من ذلك، استخدم `sudo apt install wezterm-nightly` في الخطوة 5—ولكن لاحظ أنه لا يمكن تثبيته جنبًا إلى جنب مع الإصدار المستقر.

### بديل: Flatpak (لا حاجة لإضافة مستودع)
إذا كنت تفضل تثبيت معزول دون تعديل مصادر APT:  
1. قم بتثبيت Flatpak إذا لم يكن مثبتًا مسبقًا: `sudo apt install flatpak`.  
2. أضف Flathub: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.  
3. قم بالتثبيت: `flatpak install flathub org.wezfurlong.wezterm`.  
4. شغّله: `flatpak run org.wezfurlong.wezterm` (أو أضف اسمًا مختصرًا: `alias wezterm='flatpak run org.wezfurlong.wezterm'`).  

تثبيت Flatpak معزول، لذا قد يحد من بعض الميزات المتقدمة، ولكنه أبسط للاختبار.

[دليل تثبيت WezTerm على لينكس](https://wezterm.org/install/linux.html)