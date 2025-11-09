---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: قراءة سجلات AWS CloudWatch
translated: true
type: note
---

### مقدمة حول سجلات القراءة في AWS CloudWatch
تعد سجلات AWS CloudWatch خدمة لمركزة ومراقبة وتخزين ملفات السجل من موارد AWS (مثل مثيلات EC2، أو دوال Lambda، أو قواعد بيانات RDS) والتطبيقات الخاصة بك. لقراءة السجلات، تحتاج أولاً إلى التأكد من إرسال السجلات إلى CloudWatch (على سبيل المثال، عبر وكيل CloudWatch على EC2 أو التكامل التلقائي مع الخدمات الأخرى). بعد الإعداد، يمكنك عرض السجلات من خلال وحدة تحكم إدارة AWS، أو AWS CLI، أو برمجيًا عبر SDKs.

### المتطلبات الأساسية
- **أذونات AWS**: تأكد من أن مستخدم IAM أو الدور الخاص بك لديه أذونات `logs:DescribeLogGroups`، و`logs:DescribeLogStreams`، و`logs:GetLogEvents`، و`logs:FilterLogEvents` (قم بإرفاق سياسة `CloudWatchLogsReadOnlyAccess`).
- **تكوين السجلات**: يجب توجيه السجلات إلى CloudWatch. على سبيل المثال:
  - تثبيت وكيل سجلات CloudWatch على مثيلات EC2.
  - تمكين التسجيل في خدمات مثل Lambda أو ECS.
- **AWS CLI (اختياري)**: إذا كنت تستخدم سطر الأوامر CLI، قم بتثبيته وتكوينه باستخدام `aws configure`.

### عرض السجلات في وحدة تحكم إدارة AWS
1. سجل الدخول إلى [وحدة تحكم إدارة AWS](https://console.aws.amazon.com/) وافتح خدمة CloudWatch.
2. في جزء التنقل الأيسر، اختر **Logs** > **Log groups**.
3. حدد مجموعة السجلات التي تحتوي على سجلاتك (على سبيل المثال، `/aws/lambda/my-function` لسجلات Lambda).
4. في قائمة تدفقات السجلو (ضمن مجموعة السجلات المحددة)، اختر التدفق المحدد (على سبيل المثال، تدفق لكل مثيل أو تنفيذ).
5. سيتم تحميل أحداث السجل. خصص طريقة العرض:
   - **توسيع الأحداث**: انقر على السهم بجوار الحدث لتوسيعه، أو انتقل إلى عرض **Text** فوق القائمة للنص العادي.
   - **التصفية/البحث**: أدخل عامل تصفية في مربع البحث (على سبيل المثال، "ERROR" لعرض أسطر الأخطاء فقط).
   - **النطاق الزمني**: انقر على محدد الوقت بجوار مربع البحث. اختر **Relative** (على سبيل المثال، آخر ساعة) أو **Absolute** (تواريخ مخصصة)، وبدل بين التوقيت العالمي المنسق UTC والوقت المحلي.
6. قم بالتمرير خلال الأحداث أو تنزيلها حسب الحاجة.

للاستعلام المتقدم عبر تدفقات أو مجموعات متعددة، استخدم **CloudWatch Logs Insights** (ضمن Logs > Logs Insights). اكتب استعلامات مثل `fields @timestamp, @message | filter @level = "ERROR" | sort @timestamp desc` لتحليل السجلات وتصورها.

### قراءة السجلات باستخدام AWS CLI
استخدم هذه الأوامر لإدراج واسترداد السجلات برمجيًا. استبدل العناصر النائبة مثل `my-log-group` بالأسماء الفعلية الخاصة بك.

1. **إدراج مجموعات السجلات**:
   ```
   aws logs describe-log-groups --log-group-name-prefix my-log-group
   ```
   هذا يُرجع بيانات وصفية مثل ARN، والاحتفاظ، وعدد البايتات المخزنة.

2. **إدراج تدفقات السجلات في مجموعة**:
   ```
   aws logs describe-log-streams --log-group-name my-log-group --log-stream-name-prefix 2025
   ```
   يقوم بتصفية التدفقات حسب البادئة (على سبيل المثال، أسماء مبنية على التاريخ) ويظهر وقت الإنشاء والحجم.

3. **الحصول على أحداث السجل من تدفق**:
   ```
   aws logs get-log-events --log-group-name my-log-group --log-stream-name my-stream --start-time 1730137600000
   ```
   - `--start-time` و `--end-time`: طابع زمني يونيكس (بالميلي ثانية) للنطاق الزمني.
   - `--limit`: الحد الأقصى للأحداث المراد إرجاعها (الافتراضي 1,000).
   - يتضمن الإخراج الطوابع الزمنية، ووقت الابتلاع، ونص الرسالة.
   - استخدم `--next-token` من الاستجابة للترحيل.

للبحث المصفى عبر التدفقات، استخدم `filter-log-events`:
```
aws logs filter-log-events --log-group-name my-log-group --filter-pattern "ERROR" --start-time 1730137600000
```

### نصائح وأفضل الممارسات
- **الاحتفاظ**: يتم الاحتفاظ بالسجلات إلى أجل غير مسمى افتراضيًا؛ اضبطها لكل مجموعة لإدارة التكاليف (على سبيل المثال، 30 يومًا).
- **التكاليف**: العرض مجاني، لكن الابتلاع والتخزين يتضمنان رسومًا — راقبها عبر مقاييس CloudWatch.
- **استكشاف الأخطاء وإصلاحها**: إذا لم تظهر أي سجلات، تحقق من تثبيت الوكيل أو تمكين تسجيل الخدمة.
- للمراقبة في الوقت الفعلي، قم بإعداد مرشحات المقاييس أو إنذارات على أنماط السجل.

[Working with log groups and log streams - Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)  
[CloudWatch Logs examples using AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli_cloudwatch-logs_code_examples.html)  
[Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)