---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ تكوين libcurl
translated: true
type: note
---

هذا الخطأ يعني أن سكريبت `configure` يحاول العثور على **libcurl** (مكتبة لطلبات HTTP/HTTPS)، لكنه لا يستطيع تحديد موقع `curl-config` — وهو ملف ثنائي مساعد يخبر عن مكان تثبيت libcurl.

إليك كيفية إصلاحه حسب نظامك:

---

### 🧩 لنظام Ubuntu / Debian

نفّذ:

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

ثم حاول مرة أخرى:

```bash
./configure
```

---

### 🧩 لنظام Fedora / CentOS / RHEL

نفّذ:

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 لنظام Arch / Manjaro

نفّذ:

```bash
sudo pacman -S curl
```

---

### 🔍 للتحقق من التثبيت

بعد التثبيت، تأكد من أن `curl-config` متاح:

```bash
which curl-config
```

إذا أعاد مسارًا مثل `/usr/bin/curl-config`، فأنت على ما يرام.

ثم أعد التشغيل:

```bash
./configure
make
sudo make install
```

---

هل تريد مني شرح ما يفعله `curl-config` بالفعل ولماذا يحتاجه `configure`؟