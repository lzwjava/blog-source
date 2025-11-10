---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح خطأ تجميع كودا باستخدام إن في سي سي
translated: true
type: note
---

يشير الخطأ إلى أن أدوات CUDA غير مثبتة أو مضبوطة بشكل صحيح، لأن المترجم لا يستطيع العثور على `cuda.h`. بالإضافة إلى ذلك، ملفك البرمجي هو ملف مصدر CUDA (`.cu`) ولكنك تحاول ترجمته باستخدام `gcc`، وهو غير مناسب لشفرة CUDA. أنت بحاجة إلى استخدام `nvcc`، مترجم NVIDIA CUDA. إليك كيفية إصلاح المشكلة:

### خطوات الإصلاح

1. **تثبيت CUDA Toolkit**:
   - تأكد من تثبيت NVIDIA CUDA Toolkit على نظامك. يمكنك تنزيله من [موقع NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads).
   - اتبع تعليمات التثبيت لنظام التشغيل الخاص بك (في هذه الحالة Linux، بناءً على موجه الأوامر).
   - بعد التثبيت، تحقق منه عن طريق تشغيل:
     ```bash
     nvcc --version
     ```
     يجب أن يعرض هذا إصدار CUDA إذا تم تثبيته بشكل صحيح.

2. **استخدم `nvcc` للترجمة**:
   - نظرًا لأن ملفك هو ملف مصدر CUDA (`.cu`)، قم بترجمته باستخدام `nvcc` بدلاً من `gcc`. استبدل:
     ```bash
     gcc scripts/benchmark/cudamark.c
     ```
     بـ:
     ```bash
     nvcc scripts/benchmark/cudamark.cu
     ```
   - ملاحظة: تأكد من أن امتداد الملف يطابق ملفك الفعلي (`.cu` في الكود الذي قدمته، وليس `.c` كما في الخطأ).

3. **إعداد بيئة CUDA**:
   - تأكد من تضمين مسارات أدوات CUDA في بيئتك. أضف ما يلي إلى ملف `~/.bashrc` الخاص بك أو ملف تكوين shell المكافئ:
     ```bash
     export PATH=/usr/local/cuda/bin:$PATH
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     ثم، قم بتشغيل الأمر `source` للملف:
     ```bash
     source ~/.bashrc
     ```

4. **ربط مكتبة Thrust**:
   - يستخدم كودك Thrust، وهو جزء من أدوات CUDA، لذلك لا حاجة لربط مكتبات إضافية بشكل صريح. ومع ذلك، تأكد من أن لديك إصدار CUDA متوافق (يتم تضمين Thrust في CUDA 7.0 والإصدارات الأحدث).

5. **إصلاح مشاكل الكود**:
   - يشير الكود إلى `thread_counts` ولكنه لا يستخدمه في دالة `benchmark`. دالة `parallel_sort_gpu` تستخدم Thrust، الذي يدير التوازي داخليًا، لذا فإن حلقة `thread_counts` في `main` مضللة. إذا كنت تنوي تقييم أداء تكوينات الخيوط المختلفة، فإن دالة الفرز في Thrust لا تسمح بالتحكم المباشر في عدد الخيوط. قد ترغب في توضيح هذا المنطق أو إزالة `thread_counts` غير المستخدم.
   - من أجل الوضوح، يمكنك تعديل الكود لتقييم أداء حجم القائمة نفسه عدة مرات لمتوسط تباينات التوقيت:

     ```cuda
     #include <stdio.h>
     #include <stdlib.h>
     #include <cuda.h>
     #include <thrust/device_vector.h>
     #include <thrust/sort.h>
     #include <time.h>

     void parallel_sort_gpu(int *arr, int n) {
         thrust::device_vector<int> d_vec(arr, arr + n);
         thrust::sort(d_vec.begin(), d_vec.end());
         thrust::copy(d_vec.begin(), d_vec.end(), arr);
     }

     double benchmark(int list_size) {
         int *arr = (int*)malloc(list_size * sizeof(int));
         for (int i = 0; i < list_size; ++i) {
             arr[i] = rand() % 1000001;
         }

         clock_t start = clock();
         parallel_sort_gpu(arr, list_size);
         clock_t end = clock();

         free(arr);
         return (double)(end - start) / CLOCKS_PER_SEC;
     }

     int main() {
         int list_size = 50000000;
         int num_runs = 8; // عدد مرات التشغيل للمتوسط

         printf("Run,TimeTakenSeconds\n");
         for (int i = 0; i < num_runs; ++i) {
             double t = benchmark(list_size);
             printf("%d,%.6f\n", i + 1, t);
         }
         return 0;
     }
     ```

6. **ترجمة الكود المحدث**:
   - احفظ الكود باسم `cudamark.cu` وقم بترجمته:
     ```bash
     nvcc -o cudamark scripts/benchmark/cudamark.cu
     ```
   - إذا واجهت أخطاء في الربط، فتأكد من إمكانية الوصول إلى مكتبات CUDA (انظر الخطوة 3).

7. **تشغيل البرنامج**:
   - نفذ الملف الثنائي المترجم:
     ```bash
     ./cudamark
     ```

8. **ملاحظات إضافية**:
   - **امتداد الملف**: تأكد من أن الملف له امتداد `.cu`، لأن ملفات CUDA تتطلب هذا لكي يعالجها `nvcc` بشكل صحيح.
   - **توفر GPU**: تأكد من أن لديك GPU متوافق مع CUDA وأن برامج التشغيل الصحيحة مثبتة. تحقق من ذلك باستخدام:
     ```bash
     nvidia-smi
     ```
   - **Thrust وإصدار CUDA**: تحقق من أن إصدار CUDA الخاص بك يدعم Thrust. يُوصى بـ CUDA 11.x أو إصدار أحدث لميزات Thrust الحديثة.
   - **دقة التوقيت**: تقيس دالة `clock()` وقت CPU، وليس وقت تنفيذ GPU. للحصول على توقيت GPU أكثر دقة، فكر في استخدام أحداث CUDA:
     ```cuda
     cudaEvent_t start, stop;
     cudaEventCreate(&start);
     cudaEventCreate(&stop);
     cudaEventRecord(start);
     parallel_sort_gpu(arr, list_size);
     cudaEventRecord(stop);
     cudaEventSynchronize(stop);
     float milliseconds = 0;
     cudaEventElapsedTime(&milliseconds, start, stop);
     return milliseconds / 1000.0; // التحويل إلى ثوانٍ
     ```

9. **إذا استمرت الأخطاء**:
   - إذا لم يتم العثور على `cuda.h` بعد، فتحقق من مسار تثبيت أدوات CUDA (مثل `/usr/local/cuda/include`). قد تحتاج إلى تحديد مسار التضمين بشكل صريح:
     ```bash
     nvcc -I/usr/local/cuda/include -o cudamark scripts/benchmark/cudamark.cu
     ```
   - تأكد من أن مسار الملف `scripts/benchmark/cudamark.cu` صحيح بالنسبة لدليل العمل الحالي الخاص بك.

### أمر الترجمة المحدث
```bash
nvcc -o cudamark scripts/benchmark/cudamark.cu
```

### الناتج المتوقع
بعد إصلاح المشكلات، يجب أن ينتج عن تشغيل `./cudamark` ناتجًا مشابهًا لما يلي:
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

إذا كنت بحاجة إلى مزيد من المساعدة أو واجهت أخطاء محددة، فيرجى مشاركتها!