---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: تدفق رمز جهاز OAuth لـ GitHub
translated: true
type: note
---

### نظرة عامة

ينفذ كود JavaScript هذا عملية منح تفويض جهاز OAuth 2.0 (المعروفة أيضًا باسم منح كود الجهاز) للمصادقة مع GitHub والحصول على رمز وصول. تُستخدم هذه العملية عادةً للتطبيقات غير التفاعلية (مثل أدوات سطر الأوامر أو الأنظمة المضمنة) حيث لا يمكن للمستخدم التفاعل مباشرة مع متصفح ويب للموافقة على المصادقة.

في هذه الحالة بالذات، يبدو أنها تحاكي طلبات إضافة GitHub Copilot (مثل تلك الخاصة بـ Neovim أو Vim)، باستخدام رؤوس تتظاهر بأنها عميل Copilot للتكامل مع نظام مصادقة GitHub أو الوصول إليه. الهدف هو إنشاء رمز وصول يمكن استخدامه لمكالمات GitHub API التي تتطلب مصادقة المستخدم، مثل قراءة معلومات المستخدم (حسب النطاق `scope: "read:user"`).

يعمل الكود كسكريبت Node.js، باستخدام `fetch` لطلبات HTTP و `process` لمتغيرات البيئة. يفترض أن Node.js لديه `fetch` متاحًا (كما في الإصدارات الأحدث أو عبر polyfill). إذا نجح، فإنه يطلب بشكل متكرر من خوادم GitHub حتى يقوم المستخدم بتفويض الطلب أو انتهاء المهلة.

**ملاحظات مهمة:**
- يتطلب هذا الكود تعيين متغير بيئة `MY_COPILOT_CLIENT_ID`، والذي يُرجح أنه معرف عميل GitHub OAuth App مسجل لـ GitHub Copilot.
- يتعامل مع الأخطاء بشكل بسيط—على سبيل المثال، إذا فشل جلب البيانات، يقوم بتسجيل الخطأ والمتابعة أو الخروج.
- من ناحية الأمان، يعد تخزين أو تسجيل رموز الوصول أمرًا محفوفًا بالمخاطر (حيث أنها تمنح وصولاً إلى API). يطبع هذا الكود كائن الرمز بالكامل مباشرة إلى وحدة التحكم، مما قد يمثل مشكلة خصوصية/أمان في الاستخدام الحقيقي. يجب التعامل مع رموز الوصول بأمان (مثل تخزينها مشفرة وتدويرها).
- تتضمن العملية تفاعلاً من المستخدم: يجب على المستخدم زيارة عنوان URL وإدخال كود على موقع GitHub للتفويض.
- هذا ليس كودًا "رسميًا" من وثائق GitHub؛ يبدو أنه تم استنساخه من سلوك GitHub Copilot. استخدم واجهات برمجة التطبيقات (APIs) بمسؤولية ووفقًا لشروط الخدمة الخاصة بـ GitHub.

### تفصيل خطوة بخطوة

#### 1. فحص البيئة
```javascript
const clientId = process.env.MY_COPILOT_CLIENT_ID;

if (!clientId) {
  console.error("MY_COPILOT_CLIENT_ID is not set");
  process.exit(1);
}
```
- يسترد `MY_COPILOT_CLIENT_ID` من متغيرات البيئة (مثل تعيينه عبر `export MY_COPILOT_CLIENT_ID=your_client_id` في الطرفية).
- إذا لم يتم تعيينه، يسجل خطأ ويخرج من السكريبت (كود العملية 1 يشير إلى فشل).
- هذا المعرف الخاص بالعميل (client ID) يأتي من تطبيق GitHub OAuth App مسجل (مطلوب لعمليات OAuth).

#### 2. إعداد الرؤوس المشتركة
```javascript
const commonHeaders = new Headers();
commonHeaders.append("accept", "application/json");
commonHeaders.append("editor-version", "Neovim/0.6.1");
commonHeaders.append("editor-plugin-version", "copilot.vim/1.16.0");
commonHeaders.append("content-type", "application/json");
commonHeaders.append("user-agent", "GithubCopilot/1.155.0");
commonHeaders.append("accept-encoding", "gzip,deflate,b");
```
- ينشئ كائن `Headers` بأزواج مفتاح-قيمة لطلبات HTTP.
- تجعل هذه الرؤوس الطلبات تبدو وكأنها قادمة من إضافة GitHub Copilot لـ Vim (الإصدار 1.16.0 لـ Neovim 0.6.1). يُرجح أن هذا للتظاهر بـ user-agent ومحاكاة مكالمات Copilot's API، والتي قد تكون مطلوبة أو مفيدة لقبول GitHub للطلبات.
- `"accept": "application/json"`: يتوقع استجابات بصيغة JSON.
- `"content-type": "application/json"`: يرسل JSON في هيئة الطلبات.
- `"accept-encoding"`: يسمح بضغط gzip/deflate لتوفير عرض النطاق الترددي.

#### 3. دالة `getDeviceCode()`
```javascript
async function getDeviceCode() {
  const raw = JSON.stringify({
    "client_id": clientId,
    "scope": "read:user",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  const data = await fetch(
    "https://github.com/login/device/code",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
  return data;
}
```
- **الغرض**: يبدأ عملية Device Code بطلب كود جهاز من GitHub.
- ينشئ حمل بيانات JSON بـ:
  - `client_id`: معرف العميل OAuth (لمصادقة تطبيقك).
  - `scope`: `"read:user"`—يحدد صلاحية الرمز لقراءة معلومات الملف الشخصي الأساسية للمستخدم (مثل اسم المستخدم، البريد الإلكتروني عبر GitHub API). هذا نطاق صلاحيات محدود.
- يقوم بطلب POST إلى `https://github.com/login/device/code` (نقطة نهاية كود جهاز OAuth الخاص بـ GitHub).
- يحلل استجابة JSON (الحقول المتوقعة: `device_code`, `user_code`, `verification_uri`, `expires_in`—غير موضحة في الكود، ولكنها معيارية لهذه العملية).
- في حالة الخطأ (مثل مشاكل الشبكة)، يسجله لكنه يستمر (قد يُرجع `undefined`).
- يُرجع كائن البيانات المحلل JSON من GitHub.

#### 4. دالة `getAccessToken(deviceCode: string)`
```javascript
async function getAccessToken(deviceCode: string) {
  const raw = JSON.stringify({
    "client_id": clientId,
    "device_code": deviceCode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  return await fetch(
    "https://github.com/login/oauth/access_token",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
}
```
- **الغرض**: يطلب بشكل متكرر من GitHub لاستبدال كود الجهاز برمز وصول بمجرد أن يقوم المستخدم بالتفويض.
- يأخذ `device_code` من الخطوة السابقة.
- ينشئ JSON بـ:
  - `client_id`: نفس القيمة السابقة.
  - `device_code`: الكود الفريد الذي يحدد هذا الجهاز/محاولة المصادقة.
  - `grant_type`: يحدد أن هذا منح Device Code (URN القياسي لـ OAuth2).
- يقوم بطلب POST إلى `https://github.com/login/oauth/access_token`.
- يُرجع استجابة JSON المحللة، والتي يمكن أن تكون:
  - عند النجاح: `{ access_token: "...", token_type: "bearer", scope: "read:user" }`.
  - في الانتظار/الخطأ: `{ error: "...", error_description: "..." }` (مثل "authorization_pending" أو "slow_down").
- لا يتم التعامل مع الأخطاء (مثل فشل fetch) بشكل صريح، لذا يجب على المتصل التحقق من القيمة المرجعة.

#### 5. التنفيذ الرئيسي (دالة غير متزامنة مستدعاة فورًا)
```javascript
(async function () {
  const { device_code, user_code, verification_uri, expires_in } =
    await getDeviceCode();
  console.info(`enter user code:\n${user_code}\n${verification_uri}`);
  console.info(`Expires in ${expires_in} seconds`);
  while (true) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const accessToken = await getAccessToken(device_code);
    if (accessToken.error) {
      console.info(`${accessToken.error}: ${accessToken.error_description}`);
    }
    if (accessToken.access_token) {
      console.info(`access token:\n${JSON.stringify(accessToken, null, 1)}`);
      break;
    }
  }
})();
```
- **التدفق العام**: ينظم عملية منح Device Code لـ OAuth 2.0 بالكامل.
- يستدعي `getDeviceCode()` ويفكك الاستجابة إلى متغيرات (يفترض أنها تنجح وتمتلك هذه الخصائص).
- يسجل تعليمات للمستخدم:
  - `user_code`: كود أبجدي رقمي قصير (مثل "ABCD-EFGH").
  - `verification_uri`: عادةً `https://github.com/login/device`، حيث يقوم المستخدم بالمصادقة.
  - `expires_in`: الوقت بالثواني حتى انتهاء صلاحية الكود (مثل 900 لـ 15 دقيقة).
- يجب على المستخدم زيارة عنوان URL، وتسجيل الدخول إلى GitHub، وإدخال كود المستخدم لتفويض التطبيق.
- يدخل في حلقة لا نهائية للطلب المتكرر للحصول على الرمز:
  - ينتظر 5 ثوانٍ بين المحاولات (فترة التكرار؛ توصي GitHub بـ slow_down للطلبات المتكررة جدًا).
  - يستدعي `getAccessToken(device_code)`.
  - إذا كانت الاستجابة تحتوي على `error`: يسجلها (مثل الاستمرار في الانتظار إذا كانت "authorization_pending").
  - إذا كانت تحتوي على `access_token`: يسجل كائن الرمز بالكامل (مُنسق بمسافات بادئة) ويخرج من الحلقة.
- **الحالات/المشاكل الحدية**:
  - إذا فشلت `getDeviceCode()`، قد يحدث خطأ أثناء التفكيك (الكود لا يتحقق من هذا).
  - لا يوجد حد زمني للحلقة—يستمر في التكرار إلى أجل غير مسمى ما لم يتم استلام رمز الوصول أو تعطل السكريبت.
  - تسجيل رمز الوصول في وحدة التحكم يعرضه للخطر؛ في بيئة الإنتاج، يجب حفظه بأمان (مثل حفظه في ملف أو قاعدة بيانات).

### كيف يعمل من البداية إلى النهاية
1. **الخطوة 1: طلب كود الجهاز** → يحصل السكريبت على كود مؤقت من GitHub.
2. **الخطوة 2: تفويض المستخدم** → يزور المستخدم GitHub ويدخل الكود لمنح الإذن.
3. **الخطوة 3: التكرار للحصول على الرمز** → يستمر السكريبت في سؤال GitHub حتى يتم إصدار الرمز.
4. **النتيجة**: رمز وصول للنطاق المحدد (مثل قراءة بيانات المستخدم عبر GitHub API).

هذه محاكاة لكيفية عمل أدوات مثل GitHub CLI، مُعدة لـ Copilot. للوثائق الرسمية لـ GitHub OAuth، راجع https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow. إذا كنت تبني شيئًا مشابهًا، تأكد من الامتثال لمعايير OAuth وسياسات GitHub. إذا كانت لديك أسئلة حول تعديل أو تشغيل هذا، دعني أعلم!