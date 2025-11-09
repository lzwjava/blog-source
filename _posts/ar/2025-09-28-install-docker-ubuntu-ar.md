---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-sonnet-4
title: دليل تثبيت Docker على أوبونتو
translated: true
type: note
---

استنادًا إلى ناتج نظام Ubuntu الخاص بك، لديك عدة خيارات لتثبيت Docker. إليك الطريقة الموصى بها:

## الخيار 1: تثبيت Docker Engine (موصى به)

الطريقة الأكثر شيوعًا والموصى بها هي تثبيت Docker Engine من مستودع Docker الرسمي:

```bash
# تحديث فهرس الحزم
sudo apt update

# تثبيت المتطلبات الأساسية
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# إضافة مفتاح GPG الرسمي لـ Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# إضافة مستودع Docker
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# تحديث فهرس الحزم مرة أخرى
sudo apt update

# تثبيت Docker Engine
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## الخيار 2: التثبيت السريع عبر APT (أبسط)

من الخيارات المعروضة في طرفيتك، يمكنك استخدام:

```bash
sudo apt install docker.io
```

## الإعداد بعد التثبيت

بعد التثبيت، سترغب في:

1. **بدء وتفعيل خدمة Docker:**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

2. **إضافة مستخدمك إلى مجموعة docker** (لتشغيل Docker دون sudo):
```bash
sudo usermod -aG docker $USER
```

ثم سجل الخروج وأعد تسجيل الدخول، أو شغّل:
```bash
newgrp docker
```

3. **التحقق من التثبيت:**
```bash
docker --version
docker run hello-world
```

## أي خيار تختار؟

- **الخيار 1** يمنحك أحدث إصدار من Docker مباشرة من Docker Inc.
- **الخيار 2** أبسط ولكن قد يكون به إصدار أقدم قليلاً من مستودعات Ubuntu

لمعظم المستخدمين، الخيار 2 (`sudo apt install docker.io`) جيد تمامًا وأبسط بكثير. عادةً ما يكون الفرق في الإصدار ضئيلاً للاستخدام العادي.

هل تريد مني شرح أي من هذه الخطوات بمزيد من التفصيل؟