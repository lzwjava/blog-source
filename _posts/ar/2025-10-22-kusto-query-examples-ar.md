---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: أمثلة متقدمة على لغة استعلام كوستو
translated: true
type: note
---

لغة استعلام كوستو (KQL) هي أداة قوية لاستعلام مجموعات البيانات الكبيرة في خدمات Azure مثل Azure Data Explorer وAzure Monitor. فيما يلي عدة أمثلة معقدة تجمع بين مشغلات ووظائف وميزات متقدمة متعددة مثل تحليل السلاسل الزمنية، واكتشاف الشذوذ، والتدوير، والوظائف المعرفة من قبل المستخدم. هذه الأمثلة مأخوذة من سيناريوهات واقعية مثل تحليل أحداث العواصف أو بيانات المبيعات. يتضمن كل منها الاستعلام وشرحًا موجزًا.

### 1. اكتشاف الشذوذ في بيانات السلسلة الزمنية
يجمع هذا الاستعلام بين المتوسطات اليومية من جدول المقاييس ويستخدم تحليل تحلل السلسلة لتحديد الشذوذ، وهو مثالي لمراقبة الأنماط غير المعتادة في السجلات أو بيانات القياس عن بُعد.

```
TableName
| make-series Metric = avg(Value) on Timestamp step 1d
| extend Anomalies = series_decompose_anomalies(Metric)
```

### 2. وظيفة معرّفة من قبل المستخدم للتصفية المعلمة والتلخيص
هنا، تقوم دالة قابلة لإعادة الاستخدام بتصفية بيانات المبيعات حسب المنطقة والحد الأدنى، ثم تحسب الإجماليات—مفيدة لإعداد التقارير الديناميكية في لوحات تحكم Azure Data Explorer.

```
let CalculateSales = (region: string, minSales: int) {
    SalesData
    | where Region == region and Sales > minSales
    | summarize TotalSales = sum(Sales)
};
CalculateSales("North America", 1000)
```

### 3. تدوير البيانات المجمعة للتحليل العرضي
يقوم هذا بتجميع القيم حسب الفئة والمنطقة، ثم يقوم بتدوير المناطق إلى أعمدة لتسهيل المقارنة، وهو شائع في استعلامات ذكاء الأعمال.

```
TableName
| summarize Total = sum(Value) by Category, Region
| evaluate pivot(Region, sum(Total))
```

### 4. تحليل الارتباط بين مقاييس السلسلة الزمنية
باستخدام بيانات أحداث العواصف، ينشئ هذا سلاسل يومية لمقياسين ويحسب الارتباط بينهما للكشف عن العلاقات، مثل العلاقة بين الأضرار والوفيات.

```
StormEvents
| make-series PropertyDamage = avg(DamageProperty), Fatalities = avg(Fatalities) on BeginTime step 1d
| extend Correlation = series_correlation(PropertyDamage, Fatalities)
```

### 5. التصفية، تحديد العناصر الأولى، وحساب المدة لتحليل الأحداث
يقوم هذا بتصفية أحداث الفيضانات في تكساس، ويختار أهم 5 أحداث من حيث الأضرار، ويضيف عمود مدة محسوب—ممتاز لاستجابة الحوادث في Azure Sentinel.

```
StormEvents
| where State == 'TEXAS' and EventType == 'Flood'
| top 5 by DamageProperty
| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty
```

### 6. تعيين القيم الثابتة باستخدام عبارة Let لتحويل البيانات
يحدد قاموسًا لتعيين أنواع المصادر، يقوم بتصفية الأحداث، ويعرض الأسماء الودية—مفيد لتوحيد البيانات الفئوية في السجلات.

```
let sourceMapping = dynamic(
  {
    "Emergency Manager" : "Public",
    "Utility Company" : "Private"
  });
StormEvents
| where Source == "Emergency Manager" or Source == "Utility Company"
| project EventId, Source, FriendlyName = sourceMapping[Source]
```

يمكن تشغيل هذه الأمثلة مباشرة في واجهة المستخدم الويب لـ Azure Data Explorer أو في Log Analytics. للمزيد، استكشف معرض العينات الرسمي.

[دليل شامل إلى لغة استعلام كوستو (KQL)](https://medium.com/@danushidk507/comprehensive-guide-to-kusto-query-language-kql-from-beginner-to-advanced-8dff3bd7568e)  
[برنامج تعليمي: تعلّم مشغلي لغة استعلام كوستو الشائعة](https://learn.microsoft.com/en-us/kusto/query/tutorials/learn-common-operators?view=microsoft-fabric)