---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ مهلة أمان طبقة النقل لحاوية GHCR في Docker
translated: true
type: note
---

الخطأ الذي تواجهه، `Get "https://ghcr.io/v2/": net/http: TLS handshake timeout`، يشير عادةً إلى مشكلة في الشبكة عندما يحاول Docker سحب الصور من سجل حاويات GitHub (GHCR). إليك بعض الخطوات لاستكشاف الأخطاء وإصلاحها:

---

### 1. **تحقق من اتصال الإنترنت لديك**
- تأكد من أن جهازك لديه اتصال إنترنت مستقر.
- حاول الوصول إلى `https://ghcr.io` في متصفحك لتأكيد إمكانية الوصول إلى الموقع.

---

### 2. **تحقق من حالة Docker Daemon**
- أعد تشغيل Docker daemon:
  ```bash
  sudo systemctl restart docker
  ```
- تحقق من أن Docker قيد التشغيل:
  ```bash
  sudo systemctl status docker
  ```

---

### 3. **تكوين DNS لـ Docker**
- إذا كنت خلف شبكة شركة أو وكيل، قد يحتاج Docker إلى إعدادات DNS مخصصة.
- قم بتحرير أو إنشاء الملف `/etc/docker/daemon.json`:
  ```json
  {
    "dns": ["8.8.8.8", "1.1.1.1"]
  }
  ```
- أعد تشغيل Docker:
  ```bash
  sudo systemctl restart docker
  ```

---

### 4. **تحقق من إعدادات الوكيل (Proxy)**
- إذا كنت خلف وكيل، قم بتكوين Docker لاستخدامه:
  ```bash
  mkdir -p ~/.docker
  echo '{
    "proxies": {
      "default": {
        "httpProxy": "http://your-proxy-address:port",
        "httpsProxy": "http://your-proxy-address:port",
        "noProxy": "localhost,127.0.0.1"
      }
    }
  }' > ~/.docker/config.json
  ```
- استبدل `your-proxy-address:port` بتفاصيل الوكيل الفعلية لديك.

---

### 5. **أعد محاولة سحب الصورة يدويًا**
- حاول سحب الصورة يدويًا لمعرفة ما إذا كانت المشكلة مستمرة:
  ```bash
  docker pull ghcr.io/librechat/librechat:latest
  ```
- إذا نجحت، أعد محاولة `docker-compose up -d`.

---

### 6. **تحقق من وجود قيود على الجدار الناري/الشبكة**
- تأكد من أن جدارك الناري أو شبكتك لا يحظران الوصول إلى `ghcr.io`.
- عطل الجدار الناري مؤقتًا للاختبار:
  ```bash
  sudo ufw disable
  ```
  (أعد تمكينه بعد الاختبار إذا لزم الأمر.)

---

### 7. **حدّث Docker و Docker-Compose**
- تأكد من أنك تستخدم أحدث الإصدارات:
  ```bash
  sudo apt update && sudo apt upgrade docker-ce docker-compose-plugin
  ```

---

### 8. **عيّن متغيرات البيئة UID/GID**
- التحذيرات بشأن `UID` و `GID` ليست حرجة، ولكن يمكنك تعيينها في ملف `.env` أو `docker-compose.yml` لإخفاء التحذيرات:
  ```bash
  echo "UID=$(id -u)" >> .env
  echo "GID=$(id -g)" >> .env
  ```

---

### 9. **استخدم مرآة سجل مختلفة (اختياري)**
- إذا كان GHCR غير قابل للوصول باستمرار، يمكنك تجربة استخدام مرآة (على الرغم من أن هذا غير موصى به للإنتاج):
  ```json
  {
    "registry-mirrors": ["https://mirror.example.com"]
  }
  ```
- أضف هذا إلى `/etc/docker/daemon.json` وأعد تشغيل Docker.

---

### 10. **تحقق من مزامنة الوقت**
- تأكد من أن وقت النظام لديك متزامن:
  ```bash
  sudo apt install ntp
  sudo systemctl restart ntp
  ```

---

### جدول ملخص للأوامر

| الخطوة | الأمر/الإجراء |
|------|----------------|
| إعادة تشغيل Docker | `sudo systemctl restart docker` |
| التحقق من حالة Docker | `sudo systemctl status docker` |
| تكوين DNS | تحرير `/etc/docker/daemon.json` |
| سحب الصورة يدويًا | `docker pull ghcr.io/librechat/librechat:latest` |
| تعيين UID/GID | `echo "UID=$(id -u)" >> .env` |

---

إذا استمرت المشكلة بعد تجربة هذه الخطوات، أعلمني بناتج:
```bash
docker info
```
وأي رسائل خطأ تراها عند تشغيل الأوامر أعلاه. سيساعد هذا في التشخيص بشكل أعمق!