---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: مسار مصادقة GitHub Copilot
translated: true
type: note
---

سؤال جيد — تدفق المصادقة في GitHub Copilot هو في الأساس **منحة رمز الجهاز القياسية OAuth2**، ولكن مع بعض الرموز الخاصة بـ GitHub المطبقة فوقها لخدمة Copilot نفسها. دعني أوضحها خطوة بخطوة:

---

### 1. **تدفق الجهاز (`/login/device/code`)**

* عند تسجيل الدخول لأول مرة، يستدعي عميل Copilot (مثل ملحق VS Code، أو إضافة JetBrains، أو واجهة سطر الأوامر) نقطة نهاية OAuth الخاصة بـ GitHub:

  ```
  POST https://github.com/login/device/code
  ```
* يرسل معه **معرف العميل (client_id)** (المخصص لـ GitHub Copilot).
* ترد GitHub بـ:

  * `device_code` (رمز داخلي يُستخدم للاستقصاء)،
  * `user_code` (الرمز الذي تراه وتدخله في متصفحك)،
  * `verification_uri` (عنوان URL الذي تزوره لإدخال الرمز)،
  * `interval` (عدد مرات استقصاء العميل).

---

### 2. **الاستقصاء للحصول على رمز الوصول**

* بعد ذلك يقوم عميل Copilot بالاستقصاء:

  ```
  POST https://github.com/login/oauth/access_token
  ```
* يتضمن `device_code` و `client_id`.
* بمجرد الموافقة في متصفحك، تعيد GitHub:

  * `access_token` (رمز **GitHub OAuth** مخصص لاستخدام Copilot)،
  * `token_type=bearer`،
  * `expires_in` (مدة الصلاحية).

هذا `access_token` هو **رمز GitHub OAuth2 عادي**.

---

### 3. **الاستبدال بالرمز `copilot_internal`**

* لا يمكن لعميل Copilot استدعاء واجهات برمجة تطبيقات Copilot مباشرة باستخدام رمز GitHub OAuth.
* بدلاً من ذلك، يقوم بتبادله مع خدمة Copilot:

  ```
  POST https://api.github.com/copilot_internal/v2/token
  Authorization: Bearer <GitHub OAuth access_token>
  ```
* الرد هو:

  ```json
  {
    "token": "<copilot_internal token>",
    "expires_at": "...",
    "user": { ... }
  }
  ```
* هذا **الرمز `copilot_internal` الإصدار 2** هو ما يستخدمه عميل Copilot للتواصل مع **خدمة الاستدلال Copilot** (مثل `https://copilot-proxy.githubusercontent.com`).

---

### 4. **استخدام الرمز `copilot_internal`**

* جميع طلبات الإكمال أو الدردشة اللاحقة يتم المصادقة عليها باستخدام:

  ```
  Authorization: Bearer <copilot_internal token>
  ```
* هذا الرمز له عمر قصير (عادةً حوالي ساعة) ومرتبط بحسابك على GitHub + حالة اشتراك Copilot.
* يقوم العميل بتحديثه دوريًا عن طريق إعادة استبدال رمز وصول GitHub OAuth.

---

✅ **باختصار:**

* `/login/device/code` → يمنحك رمزًا للمصادقة في المتصفح.
* `/login/oauth/access_token` → يمنحك رمز GitHub OAuth.
* `/copilot_internal/v2/token` → يستبدل ذلك الرمز برمز Copilot قصير العمر، وهو *البيانات الاعتمادية الحقيقية* المستخدمة للإكمالات.

---

هل تريد مني أيضًا رسم **أمثلة الطلبات/الردود الدقيقة** (مع الرؤوس ونموذج JSON) حتى تتمكن من رؤاء كيف تبدو الحمولات عمليًا؟