---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح خطأ رفض إذن npm
translated: true
type: note
---

الخطأ الذي تواجهه، `EACCES: permission denied`، يعني أن المستخدم الحالي **ليس لديه أذونات كتابة** في دليل `/usr/local/lib/node_modules`. هذه مشكلة شائعة عند تثبيت حزم npm العالمية على Linux أو macOS.

### **كيفية إصلاح هذه المشكلة**

#### **الخيار 1: استخدام `sudo` (غير موصى به للاستخدام المنتظم)**
يمكنك استخدام `sudo` لتشغيل الأمر كمسؤول root، لكن هذا **غير موصى به** للاستخدام المنتظم، لأنه قد يؤدي إلى مشاكل أذونات مع حزم npm لاحقًا.

```bash
sudo npm install -g @anthropic-ai/claude-code
```

#### **الخيار 2: تغيير الدليل الافتراضي لـ npm (موصى به)**
أفضل ممارسة هي تكوين npm لاستخدام دليل في مجلد المنزل الخاص بك حيث لديك أذونات كتابة.

1. **إنشاء دليل npm عالمي في مجلد المنزل الخاص بك:**
   ```bash
   mkdir ~/.npm-global
   ```
2. **تكوين npm لاستخدام هذا الدليل:**
   ```bash
   npm config set prefix '~/.npm-global'
   ```
3. **إضافة الدليل الجديد إلى `PATH` الخاص بك:**
   افتح ملف تهيئة shell الخاص بك (مثل `~/.bashrc`، أو `~/.zshrc`، أو `~/.profile`) وأضف هذا السطر:
   ```bash
   export PATH=~/.npm-global/bin:$PATH
   ```
   ثم، أعد تحميل shell:
   ```bash
   source ~/.bashrc  # أو ~/.zshrc، ~/.profile
   ```
4. **أعد محاولة التثبيت:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

#### **الخيار 3: إصلاح أذونات `/usr/local` (متقدم)**
إذا كنت ترغب في الاستمرار في استخدام `/usr/local`، يمكنك تغيير ملكيته إلى مستخدمك:
```bash
sudo chown -R $(whoami) /usr/local/lib/node_modules
```
ثم أعد محاولة التثبيت.

---

**التوصية:** استخدم **الخيار 2** لتجنب مشاكل الأذونات في المستقبل.