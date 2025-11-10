---
audio: false
generated: true
lang: ar
layout: post
title: تدريب نماذج التعلم الآلي على منصة جوجل السحابية باستخدام معالجات إنفيديا الرسومية
translated: true
type: note
---

تقدم منصة Google Cloud Platform (GCP) خيارات قوية لتدريب نماذج التعلم الآلي باستخدام وحدات معالجة الرسومات NVIDIA من خلال خدمات مثل Vertex AI (لوظائف التدريب المدارة) وCompute Engine (للأجهزة الظاهرية المخصصة). ومع ذلك، فإن وحدات معالجة الرسومات NVIDIA RTX 4090 غير متوفرة على GCP. تعتبر RTX 4090 وحدة معالجة رسومات للمستهلكين مصممة primarily لأجهزة الكمبيوتر المكتبية والألعاب، وليست مصممة لمراكز البيانات السحابية. بدلاً من ذلك، تقدم GCP وحدات معالجة رسومات NVIDIA من فئة المؤسسات مثل A100 وH100 وL4 وغيرها، وهي مُحسنة لأحمال عمل الذكاء الاصطناعي وغالبًا ما تتفوق على RTX 4090 في سيناريوهات التدريب بسبب نطاق نطاق ذاكرة أعلى وكفاءة Tensor Core.

لإعدادات وحدات معالجة الرسومات المتعددة (على الأقل 2 GPU)، يمكنك تكوين الموارد لاستخدام 2 أو 4 أو 8 أو أكثر من وحدات معالجة الرسومات اعتمادًا على نوع الجهاز. سأركز على Vertex AI للتبسيط، حيث أنه مصمم خصيصًا للتدريب على التعلم الآلي ويتعامل مع التحجيم تلقائيًا. إذا كنت بحاجة إلى مزيد من التحكم، سأغطي Compute Engine بإيجاز.

## المتطلبات الأساسية
- إعداد حساب Google Cloud وإنشاء مشروع.
- تمكين واجهة برمجة تطبيقات Vertex AI وواجهة برمجة تطبيقات Compute Engine في مشروعك.
- تثبيت Google Cloud SDK (أداة سطر أوامر gcloud) وVertex AI SDK إذا كنت تستخدم Python.
- إعداد كود التدريب الخاص بك في حاوية Docker (على سبيل المثال، باستخدام TensorFlow أو PyTorch مع دعم التدريب الموزع مثل Horovod أو torch.distributed).
- تأكد من أن كود النموذج الخاص بك يدعم التدريب متعدد وحدات معالجة الرسومات (على سبيل المثال، عبر DataParallel أو DistributedDataParallel في PyTorch).

## استخدام Vertex AI للتدريب متعدد وحدات معالجة الرسومات
Vertex AI هو المنصة المدارة من GCP لسير عمل التعلم الآلي. وهو يدعم وظائف التدريب المخصصة حيث يمكنك تحديد أنواع الأجهزة التي تحتوي على وحدات معالجة رسومات متعددة.

### أنواع وحدات معالجة الرسومات المتاحة للتدريب متعدد وحدات معالجة الرسومات
وحدات معالجة الرسومات الشائعة من NVIDIA التي تدعم توصيل至少 2 وحدة:
- NVIDIA H100 (80GB أو Mega 80GB): عالية الأداء للنماذج الكبيرة؛ تدعم 2 أو 4 أو 8 وحدات معالجة رسومات.
- NVIDIA A100 (40GB أو 80GB): مستخدمة على نطاق واسع للتدريب؛ تدعم 2 أو 4 أو 8 أو 16 وحدة معالجة رسومات.
- NVIDIA L4: فعالة من حيث التكلفة للاستدلال والتدريب الخفيف؛ تدعم 2 أو 4 أو 8 وحدات معالجة رسومات.
- NVIDIA T4 أو V100: أقدم ولكنها لا تزال متاحة؛ تدعم 2 أو 4 أو 8 وحدات معالجة رسومات.

تشمل القائمة الكاملة GB200 وB200 وH200 وP4 وP100 — تحقق من توفرها في المناطق، حيث أنها غير متوفرة في كل منطقة.

### خطوات إنشاء مهمة تدريب باستخدام至少 2 وحدة معالجة رسومات
1. **جهز الحاوية الخاصة بك**: أنشئ صورة Docker تحتوي على سكريبت التدريب الخاص بك وادفعها إلى Google Container Registry أو Artifact Registry. مثال على Dockerfile لـ PyTorch:
   ```
   FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
   COPY train.py /app/train.py
   WORKDIR /app
   CMD ["python", "train.py"]
   ```

2. **تكوين المهمة باستخدام أداة سطر أوامر gcloud**:
   - أنشئ ملف `config.yaml`:
     ```yaml
     workerPoolSpecs:
       machineSpec:
         machineType: a3-highgpu-2g  # مثال: 2x H100 GPUs; بدائل: a2-ultragpu-2g (2x A100), g2-standard-24 (2x L4)
         acceleratorType: NVIDIA_H100_80GB  # أو NVIDIA_A100_80GB, NVIDIA_L4
         acceleratorCount: 2  # على الأقل 2
       replicaCount: 1
       containerSpec:
         imageUri: gcr.io/your-project/your-image:latest  # URI صورة Docker الخاصة بك
     ```
   - شغل الأمر:
     ```bash
     gcloud ai custom-jobs create \
       --region=us-central1 \  # اختر منطقة بتوفر GPU
       --display-name=your-training-job \
       --config=config.yaml
     ```

3. **استخدام Python SDK**:
   ```python
   from google.cloud import aiplatform

   aiplatform.init(project='your-project-id', location='us-central1')

   job = aiplatform.CustomJob(
       display_name='your-training-job',
       worker_pool_specs=[
           {
               'machine_spec': {
                   'machine_type': 'a3-highgpu-2g',  # 2x H100
                   'accelerator_type': 'NVIDIA_H100_80GB',
                   'accelerator_count': 2,
               },
               'replica_count': 1,
               'container_spec': {
                   'image_uri': 'gcr.io/your-project/your-image:latest',
               },
           }
       ],
   )
   job.run()
   ```

4. **المراقبة والتحجيم**:
   - استخدم console Vertex AI لعرض حالة المهمة والسجلات.
   - للتدريب الموزع عبر أجهزة متعددة (مثل نسخ إضافية)، أضف مجموعات عمال إضافية واستخدم خوادم التجميع إذا لزم الأمر للمهام واسعة النطاق.
   - التكاليف: يتم فوترة وحدات معالجة الرسومات بالساعة؛ تحقق من التسعير في منطقتك (على سبيل المثال، قد تبلغ تكلفة 2x H100 حوالي ~$6-10/ساعة).

5. **نصائح للتدريب متعدد وحدات معالجة الرسومات**:
   - مكن التدريب الموزع في الكود الخاص بك (على سبيل المثال، `torch.nn.parallel.DistributedDataParallel`).
   - استخدم Spot VMs أو الحجوزات لتوفير التكاليف إذا كانت المقاطعات مقبولة.
   - تحقق من توفر وحدة معالجة الرسومات في منطقتك/منطقتك عبر console GCP.

## بديل: استخدام Compute Engine VMs
إذا كنت تفضل إعدادًا مخصصًا بدون Vertex AI:
1. إنشاء مثيل VM:
   - انتقل إلى Compute Engine > VM instances > Create instance.
   - نوع الجهاز: اختر من سلاسل A3 (H100) أو A2 (A100) أو G2 (L4)، على سبيل المثال، `a3-highgpu-2g` لـ 2x H100.
   - قرص التمهيد: استخدم صورة Deep Learning VM (مثبتة مسبقًا بـ CUDA وTensorFlow/PyTorch).
   - أضف وحدات معالجة الرسومات: حدد 2 مسرع من النوع المختار.

2. الاتصال عبر SSH بالـ VM وتشغيل سكريبت التدريب الخاص بك:
   ```bash
   gcloud compute ssh your-vm-name --zone=your-zone
   python train.py  # تأكد من اكتشاف CUDA: nvidia-smi
   ```

3. لوحدات معالجة الرسومات المتعددة: يجب أن يتعامل الكود الخاص بك معها (على سبيل المثال، `CUDA_VISIBLE_DEVICES=0,1`).

هذا يتطلب المزيد من التحكم اليدوي ولكنه يمنحك تحكمًا كاملاً.

## القيود والبدائل
- إذا كنت تحتاج تحديدًا إلى أداء مشابه لـ RTX 4090، ففكر في بدائل مثل AWS (التي تقدم وحدات معالجة رسومات للمستهلكين في بعض الحالات) أو الإعدادات المحلية.
- للتدريب المجاني/المحدود بوحدات معالجة الرسومات، جرب Google Colab (حتى 1-2 GPU، ولكن غير مضمون متعدد وحدات معالجة الرسومات أو مكافئ لـ 4090).
- تحقق دائمًا من الحصص واطلب زيادتها إذا لزم الأمر عبر console GCP.

[Configure compute resources for custom training | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/training/configure-compute)  
[GPU machine types | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/gpus)  
[Cloud GPUs (Graphics Processing Units) - Google Cloud](https://cloud.google.com/gpu)