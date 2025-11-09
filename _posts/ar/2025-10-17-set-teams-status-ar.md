---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تعيين حالة الفرق عبر PowerShell
translated: true
type: note
---

لا، لا تمتلك Microsoft Teams أداة مستقلة رسمية لسطر الأوامر (مثل ملف تنفيذي بسيط مثل `teams --status offline`) لتعيين حالة الحضور الخاصة بك. أوامر الشرطة المائلة المدمجة (مثل `/away` أو `/offline`) تعمل فقط داخل واجهة تطبيق Teams، وليس من طرفية.

ومع ذلك، يمكنك تحقيق هذا عبر سطر الأوامر باستخدام PowerShell وواجهة برمجة تطبيقات Microsoft Graph. هذا يتطلب تثبيت Microsoft Graph PowerShell SDK، والمصادقة باستخدام حساب Microsoft الخاص بك، وتشغيل cmdlet لتحديث حالة الحضور الخاصة بك. إليك دليل خطوة بخطوة:

### المتطلبات الأساسية
1. قم بتثبيت PowerShell (إذا لم يكن مثبتًا مسبقًا؛ فهو مدمج في Windows 10 والإصدارات الأحدث).
2. افتح PowerShell كمسؤول وقم بتثبيت الوحدة النمطية:
   ```
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```

### تعيين حالتك
1. الاتصال بـ Microsoft Graph (سيطلب هذا المصادقة عبر المتصفح):
   ```
   Connect-MgGraph -Scopes "Presence.ReadWrite"
   ```

2. قم بتشغيل cmdlet لتعيين حالتك. استبدل `YourUserId` بمعرف مستخدم Microsoft Entra ID (Azure AD) الخاص بك (يمكنك الحصول عليه عبر `Get-MgUser -UserId your.email@domain.com`). تشمل قيم الحالة الشائعة:
   - `Available`
   - `Away`
   - `Busy`
   - `DoNotDisturb`
   - `Offline` (يظهر للآخرين أنك غير متصل)

   مثال لتعيين الحالة إلى غير متصل:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Offline"
   ```

   مثال لتعيين الحالة إلى بعيد:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Away"
   ```

3. للقطع عند الانتهاء:
   ```
   Disconnect-MgGraph
   ```

### ملاحظات
- يقوم هذا بتحديث حالة الحضور فورًا، ولكن قد تتم إعادة تعيينها بناءً على نشاطك (على سبيل المثال، وقت الخمول يؤدي إلى "بعيد").
- للأتمتة (على سبيل المثال، النصوص البرمجية لتبديل الحالة وفقًا لجدول زمني)، قم بتضمين ما سبق في ملف `.ps1` وقم بتشغيله عبر "جدولة المهام".
- إذا كنت تريد تعيين رسالة حالة مخصصة أيضًا (على سبيل المثال، "خارج للغداء")، استخدم `Set-MgUserPresenceStatusMessage`.
- هذا يعمل للاستخدام الشخصي ولكنه يتطلب الأذونات المناسبة؛ قد يحتاج المسؤولون إلى تمكين الوصول إلى Graph API.

للحفاظ على حالتك "متاح" خلال فترات الخمول (طريقة شائعة للحل)، توجد نصوص برمجية تحاكي النشاط (مثل تبديل Num Lock كل بضع دقائق)، لكنها ليست محددات حالة حقيقية.

المراجع:  
[Manage Presence Status in Microsoft Teams Using MS Graph PowerShell](https://m365scripts.com/microsoft-teams/manage-presence-status-in-microsoft-teams-using-ms-graph-powershell/)  
[Set-MgUserPresence PowerShell Cmdlet Docs](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users.actions/set-mguserpresence)  
[Reddit Thread on Teams Status via API/CLI](https://www.reddit.com/r/teams/comments/1h5wee9/teams_status_with_api_command_line/)