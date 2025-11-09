---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: بدء العمل مع AWS Lambda
translated: true
type: note
---

### البدء مع AWS Lambda

AWS Lambda هي خدمة حوسبة بدون خوادم تشغل الكود الخاص بك استجابة للأحداث دون الحاجة إلى إدارة الخوادم. إليك دليل خطوة بخطوة للمبتدئين لإنشاء ونشر واستخدام أول دالة Lambda الخاصة بك. هذا الدليل مبني على الوثائق الرسمية من AWS.

#### المتطلبات الأساسية
- حساب AWS نشط. سجل في [aws.amazon.com](https://aws.amazon.com/) إذا لم يكن لديك حساب.
- معرفة أساسية بلغة برمجة مثل Node.js أو Python (تدعم Lambda العديد من بيئات التشغيل).

#### الخطوة 1: إنشاء دالة Lambda
1. سجل الدخول إلى وحدة تحكم إدارة AWS وانتقل إلى خدمة Lambda (ابحث عن "Lambda" في قائمة الخدمات).
2. في صفحة الدوال، انقر على **إنشاء دالة**.
3. اختر **الكتابة من الصفر**.
4. أدخل **اسم الدالة** (مثال: `my-first-function`).
5. اختر **بيئة التشغيل** (مثال: Node.js 22.x أو Python 3.13).
6. اترك بنية المعالج الافتراضية (x86_64) وانقر على **إنشاء دالة**.

سيؤدي هذا تلقائياً إلى إنشاء دور تنفيذ (دور IAM) بأذونات أساسية، مثل كتابة السجلات إلى Amazon CloudWatch.

#### الخطوة 2: كتابة الكود الخاص بك
في محرر الكود في وحدة تحكم Lambda (ضمن علامة التبويب **Code**)، استبدل كود "Hello World" الافتراضي بشيء بسيط. إليك مثالاً يحسب مساحة المستطيل بناءً على إدخال JSON يحتوي على مفاتيح `length` و `width`.

- **مثال Node.js**:
  ```javascript
  exports.handler = async (event) => {
    const length = event.length;
    const width = event.width;
    const area = length * width;
    console.log(`The area is ${area}`);
    console.log('Log group: /aws/lambda/' + process.env.AWS_LAMBDA_FUNCTION_NAME);
    return { area: area };
  };
  ```

- **مثال Python**:
  ```python
  import json

  def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = length * width
    print(f"The area is {area}")
    print(f"Log group: /aws/lambda/{context.function_name}")
    return {
        'statusCode': 200,
        'body': json.dumps({'area': area})
    }
  ```

احفظ التغييرات — يتم النشر تلقائياً للغات المفسرة.

بالنسبة للغات المترجمة (مثل Java)، قم بإنشاء حزمة نشر محلياً وقم برفعها عبر وحدة التحكم أو AWS CLI.

#### الخطوة 3: اختبار الدالة الخاصة بك
1. في علامة التبويب **Test**، انقر على **Create new test event**.
2. قم بتسميته (مثال: `test-area-calc`).
3. الصق إدخال JSON نموذجي:
   ```json
   {
     "length": 6,
     "width": 7
   }
   ```
4. احفظ وانقر على **Test**.

اعرض النتائج في قسم **Execution results** (مثال: `{"area": 42}`). تحقق من السجلات في CloudWatch للحصول على تفاصيل مثل المدة الزمنية واستخدام الذاكرة.

#### الخطوة 4: استدعاء الدالة ومراقبتها
- **الاستدعاء اليدوي**: استخدم زر Test في وحدة التحكم أو AWS CLI: `aws lambda invoke --function-name my-first-function output.json`.
- **الاستدعاء المعتمد على الأحداث**: قم بتوصيل محفزات مثل API Gateway، أو دلاء S3، أو تدفقات DynamoDB. انتقل إلى علامة التبويب **Configuration** > **Triggers** لإضافتها.
- **السجلات**: يتم إرسالها تلقائياً إلى CloudWatch Logs. اعرضها على [console.aws.amazon.com/cloudwatch/home#logsV2:log-groups](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) تحت `/aws/lambda/your-function-name`.

المفاهيم الأساسية:
- **مصادر/محفزات الأحداث**: الخدمات (مثل رفع ملف إلى S3) التي تستدعي الدالة الخاصة بك مع بيانات الحدث (حمولة JSON).
- **المعالج**: نقطة الدخول (مثال: `index.handler` لـ Node.js) التي تعالج الحدث.

#### الخطوة 5: التنظيف (اختياري)
احذف الدالة عبر وحدة التحكم: Actions > Delete. قم أيضاً بإزالة السجلات وأدوار IAM المرتبطة بها لتجنب الرسوم.

#### نصائح
- ابدأ باستخدام الطبقة المجانية (1 مليون طلب/شهر).
- استخدم AWS SAM أو Serverless Framework للنشر المتقدم.
- للإنتاج، قم بتكوين متغيرات البيئة، والطبقات، وإعدادات VPC في علامة التبويب **Configuration**.

[أنشئ أول دالة Lambda الخاصة بك](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)