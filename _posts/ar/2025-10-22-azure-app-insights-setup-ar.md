---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل إعداد Azure Application Insights
translated: true
type: note
---

## ما هو Azure Application Insights؟

Azure Application Insights هو خدمة إدارة أداء التطبيقات (APM) في Azure Monitor تساعدك على مراقبة تطبيقات الويب الحية. فهو يوفر أدوات لاكتشاف المشكلات وتشخيصها وفهم سلوك المستخدمين من خلال بيانات التليمتري مثل الطلبات والتبعيات والتتبع والمقاييس والسجلات. وهو الآن مدعوم بـ OpenTelemetry لتوفير توافق أوسع.

## المتطلبات الأساسية
- اشتراك Azure نشط.
- أذونات لإنشاء الموارد في Azure (مثل دور المالك أو المساهم).
- كود التطبيق الخاص بك (يدعم .NET، Java، Node.js، Python، والمزيد).

## الخطوة 1: إنشاء مورد Application Insights
1. سجل الدخول إلى [بوابة Azure](https://portal.azure.com).
2. انقر فوق **إنشاء مورد** في القائمة العلوية اليسرى.
3. ابحث عن "Application Insights" وحدده من النتائج تحت **المراقبة والإدارة**.
4. املأ التفاصيل:
   - **الاشتراك**: اختر اشتراك Azure الخاص بك.
   - **مجموعة الموارد**: حدد مجموعة موجودة أو أنشئ مجموعة جديدة.
   - **الاسم**: أعطِ موردك اسمًا فريدًا.
   - **المنطقة**: اختر منطقة قريبة من مستخدميك أو تطبيقك.
   - **مساحة العمل**: قم بربطها بمساحة عمل Log Analytics موجودة اختياريًا؛ وإلا، سيتم إنشاء واحدة جديدة تلقائيًا.
5. راجع وانقر فوق **إنشاء**. يستغرق النشر بضع دقائق.
6. بمجرد الإنشاء، انتقل إلى صفحة **نظرة عامة** الخاصة بموردك وانسخ **سلسلة الاتصال** (مرر فوقها وانقر على أيقونة النسخ). هذا يحدد المكان الذي يرسل إليه تطبيقك بيانات التليمتري.

**نصيحة**: استخدم موارد منفصلة لبيئات التطوير والاختبار والإنتاج لتجنب خلط البيانات.

## الخطوة 2: إعداد تطبيقك للتتبع
أضف دعم OpenTelemetry لجمع التليمتري تلقائيًا (الطلبات، الاستثناءات، المقاييس، إلخ). قم بتعيين سلسلة الاتصال عبر متغير بيئة باسم `APPLICATIONINSIGHTS_CONNECTION_STRING` (موصى به للإنتاج).

### لـ .NET (ASP.NET Core)
1. قم بتثبيت حزمة NuGet:
   ```
   dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
   ```
2. في `Program.cs`:
   ```csharp
   using Azure.Monitor.OpenTelemetry.AspNetCore;

   var builder = WebApplication.CreateBuilder(args);
   builder.Services.AddOpenTelemetry().UseAzureMonitor();
   var app = builder.Build();
   app.Run();
   ```
3. عيّن متغير البيئة باستخدام سلسلة الاتصال الخاصة بك وشغّل التطبيق.

### لـ Java
1. حمّل ملف Azure Monitor OpenTelemetry Distro JAR (مثل `applicationinsights-agent-3.x.x.jar`).
2. أنشئ ملف تكوين `applicationinsights.json` في نفس الدليل:
   ```json
   {
     "connectionString": "سلسلة الاتصال الخاصة بك هنا"
   }
   ```
3. شغّل تطبيقك مع الوكيل: `java -javaagent:applicationinsights-agent-3.x.x.jar -jar your-app.jar`.

### لـ Node.js
1. قم بتثبيت الحزمة:
   ```
   npm install @azure/monitor-opentelemetry
   ```
2. قم بالتكوين في نقطة دخول تطبيقك:
   ```javascript
   const { AzureMonitorOpenTelemetry } = require('@azure/monitor-opentelemetry');
   const provider = new AzureMonitorOpenTelemetry({
     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
   });
   provider.start();
   ```
3. عيّن متغير البيئة وابدأ تشغيل تطبيقك.

### لـ Python
1. قم بتثبيت الحزمة:
   ```
   pip install azure-monitor-opentelemetry
   ```
2. في تطبيقك:
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   configure_azure_monitor(connection_string="سلسلة الاتصال الخاصة بك هنا")
   ```
3. شغّل التطبيق.

بالنسبة للغات الأخرى أو التتبع التلقائي (مثلًا لـ Azure App Service)، تحقق من الوثائق الرسمية. اختبر محليًا أولاً.

## الخطوة 3: عرض البيانات وتحليلها
1. شغّل تطبيقك المُجهز للتتبع وقم بتوليد بعض النشاط (مثل إرسال طلبات).
2. في بوابة Azure، افتح مورد Application Insights الخاص بك.
3. تحقق من صفحة **نظرة عامة**: شاهد المقاييس الحية وأعداد الطلبات وأوقات الاستجابة (تظهر البيانات خلال ~1-2 دقيقة).
4. استكشف الميزات:
   - **المقاييس الحية**: بث في الوقت الفعلي لتطبيقات الإنتاج.
   - **الإخفاقات**: تعمق في الاستثناءات والتتبع.
   - **الأداء**: حلل التبعيات والطلبات البطيئة.
   - **الاستخدام**: تتبع جلسات المستخدمين والأحداث المخصصة.
   - **التنبيهات**: أنشئ إشعارات للمشكلات (مثل معدلات الفشل العالية).
5. استعلام عن البيانات باستخدام لغة استعلام Kusto (KQL) في **السجلات** لإجراء تحليلات مخصصة.

## أفضل الممارسات
- ابدأ بالتليمتري الأساسي؛ أضف الأحداث/المقاييس المخصصة حسب الحاجة.
- راقب التكاليف عبر صفحة **الاستخدام والتكاليف المقدرة** (يتم الفوترة عبر Log Analytics).
- لمراقبة المتصفح، أضف مقتطف JavaScript SDK إلى صفحات الويب الخاصة بك.

[إنشاء موارد Application Insights وتكوينها](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource)  
[تمكين OpenTelemetry في Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)  
[نظرة عامة على Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)