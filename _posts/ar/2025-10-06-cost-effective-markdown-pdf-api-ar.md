---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: واجهة برمجة تطبيقات فعالة التكلفة لتحويل ماركداون إلى PDF
translated: true
type: note
---

### الخيار الاقتصادي الموصى به: Google Cloud Run

لواجهة برمجة تطبيقات (API) بسيطة قائمة على جافا تقوم بتحويل Markdown إلى PDF (باستخدام مكتبة مثل Flying Saucer أو iText)، مع حوالي 100 طلب فقط أسبوعيًا للاستخدام الشخصي للمدونة، يُعد **Google Cloud Run** الخيار الأكثر فعالية من حيث التكلفة. إنه منصة لا سيرفر (serverless) تشغل التطبيقات المعتمدة على الحاويات، وتقوم بالتحجيم إلى الصفر عندما تكون خاملة، وتقوم بالفوترة فقط مقابل الاستخدام الفعلي. لا حاجة لإدارة أجهزة افتراضية (VMs) أو القلق بشأن تكاليف التشغيل المستمر – مثالي لحالات الاستخدام منخفضة الحركة مثل حالتك.

#### لماذا Cloud Run بدلاً من الخيارات الأخرى؟
- **مقارنة بـ Compute Engine (VMs)**: أجهزة VMs لها تكاليف ساعية ثابتة حتى عندما تكون خاملة، مما سيكون مبالغًا فيه وأكثر تكلفة (~5-10 دولار/شهر كحد أدنى لنموذج صغير).
- **مقارنة بـ App Engine**: فوائد لا سيرفر (serverless) مشابهة، لكن Cloud Run أكثر مرونة لحاويات جافا وغالبًا ما تكون أقل تكلفة للاستخدام المتقطع.
- عبء العمل الخاص بك يتناسب تمامًا مع الطبقة المجانية (free tier)، لذا من المتوقع أن تصل التكلفة إلى **0 دولار/شهر** عمليًا.

#### التكاليف المقدرة
مع 100 طلب/أسبوع (~400 طلب/شهر):
- لنفترض أن كل طلب يستخدم 1 vCPU و 0.5 جيجابايت من الذاكرة لمدة 10 ثوانٍ (تقدير متحفظ لتحويل Markdown إلى PDF سريع).
- إجمالي الاستخدام: ~4,000 vCPU-ثانية و ~2,000 جيجابايت-ثانية/شهر.
- **الطبقة المجانية (free tier) تغطي كل ذلك**: 180,000 vCPU-ثانية، 360,000 جيجابايت-ثانية، و 2 مليون طلب شهريًا (في معظم المناطق).
- إذا تجاوزت هذا (وهو أمر غير مرجح)، فإن الأسعار المدفوعة هي ~$0.000024/vCPU-ثانية + $0.0000025/جيجابايت-ثانية + $0.40/مليون طلب بعد الحدود المجانية – وستظل أقل من $0.10/شهر.

لا توجد رسوم خروج (egress fees) لحالة استخدامك (مكالمات API الداخلية تبقى مجانية داخل نفس المنطقة).

#### المنطقة الموصى بها: us-central1 (آيوا)
- هذه هي أرخص منطقة من الفئة الأولى (Tier 1) لـ Cloud Run، مع أقل الأسعار للحوسبة وبدون رسوم إضافية للكُمون (latency) في أمريكا الشمالية.
- التسعير متشابه عبر مناطق الفئة الأولى (الولايات المتحدة/أوروبا)، لكن us-central1 تتميز بمتوسط تكاليف أقل قليلاً للنُسخ (instances).
- إذا كنت خارج أمريكا الشمالية (مثل أوروبا أو آسيا)، فقم بالتبديل إلى أقرب منطقة من الفئة الأولى مثل europe-west1 (بلجيكا) للحصول على كُمون أفضل – الفرق في التكاليف أقل من 10%.
- تجنب مناطق الفئة الثانية (مثل asia-southeast1) لأنها أكثر تكلفة بنسبة 20-50%.

#### دليل الإعداد السريع لخادم جافا الخاص بك
1.  **قم ببناء تطبيقك**: استخدم Spring Boot لإنشاء واجهة برمجة تطبيقات (REST API) بسيطة. مثال على النقطة الطرفية (endpoint): POST `/convert` مع نص Markdown، وإرجاع PDF.
    - أضف التبعية: `implementation 'org.xhtmlrenderer:flying-saucer-pdf:9.1.22'` (أو ما شابه).
    - نموذج snippet للكود:
      ```java:disable-run
      @RestController
      public class MarkdownController {
          @PostMapping("/convert")
          public ResponseEntity<byte[]> convert(@RequestBody String markdown) {
              // منطق التحويل هنا (مثال: تحويل markdown إلى HTML، ثم إلى PDF)
              byte[] pdfBytes = // نتيجة التحويل الخاصة بك;
              return ResponseEntity.ok()
                  .header("Content-Type", "application/pdf")
                  .body(pdfBytes);
          }
      }
      ```
2.  **حاوِرة التطبيق (Containerize)**: أنشئ ملف `Dockerfile`:
    ```
    FROM openjdk:17-jdk-slim
    COPY target/your-app.jar app.jar
    ENTRYPOINT ["java", "-jar", "/app.jar"]
    ```
    قم بالبناء: `docker build -t gcr.io/your-project/markdown-api .`
3.  **انشر على Cloud Run**:
    - فعّل Cloud Run API في GCP Console.
    - `gcloud run deploy markdown-api --image gcr.io/your-project/markdown-api --platform managed --region us-central1 --allow-unauthenticated --memory 512Mi --cpu 1 --max-instances 1`
    - احصل على الرابط: `https://markdown-api-abc.run.app/convert`
4.  **اختبر**: أرسل طلب POST يحتوي على Markdown؛ سيقوم بالتحجيم التلقائي.

اشترك في الإصدار التجريبي المجاني بقيمة 300 دولار إذا كنت جديدًا على GCP. راقب التكاليف في لوحة تحكم الفوترة (Billing dashboard).

[تسعير Cloud Run](https://cloud.google.com/run/pricing)  
[دليل مناطق GCP](https://www.cloudzero.com/blog/gcp-regions/)  
[بدء سريع مع Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)