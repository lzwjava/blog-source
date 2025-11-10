---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح أخطاء تخصيص ذاكرة CUDA للدفع
translated: true
type: note
---

يشير الخطأ `thrust::system::detail::bad_alloc` مع `cudaErrorUnknown: unknown error` والرسالة اللاحقة `Aborted (core dumped)` إلى وجود مشكلة في وقت التشغيل لبرنامج CUDA الخاص بك، على الأرجح تتعلق بتخصيص الذاكرة أو توافق وحدة معالجة الرسومات عند استخدام Thrust للفرز. يحدث هذا الخطأ عادةً عندما تواجه بيئة وقت تشغيل CUDA مشكلة، مثل عدم كفاية ذاكرة وحدة معالجة الرسومات، أو وحدة معالجة رسومات غير متوافقة، أو بيئة CUDA غير مهيئة بشكل صحيح. أدناه، سأوضح الخطوات لتشخيص وإصلاح المشكلة بناءً على الكود والخطأ المقدمين.

### خطوات الإصلاح

1. **التحقق من توفر ذاكرة وحدة معالجة الرسومات**:
   - برنامجك يخصص مصفوفة كبيرة (`list_size = 50,000,000` عدد صحيح، تقريبًا 200 ميجابايت) على وحدة معالجة الرسومات باستخدام `device_vector` من Thrust. إذا كانت ذاكرة وحدة معالجة الرسومات لديك محدودة أو كانت هناك عمليات أخرى تستخدمها، فقد يتسبب ذلك في خطأ `bad_alloc`.
   - قم بتشغيل `nvidia-smi` للتحقق من استخدام ذاكرة وحدة معالجة الرسومات:
     ```bash
     nvidia-smi
     ```
   - تأكد من وجود مساحة ذاكرة حرة كافية على وحدة معالجة الرسومات. إذا كانت هناك عمليات أخرى تستهلك الذاكرة، قم بإنهائها أو أعد تشغيل النظام لتحرير الموارد.
   - **الإصلاح**: قلل `list_size` لاختبار ما إذا كانت المشكلة متعلقة بالذاكرة. جرب تعيين `list_size = 10,000,000` (40 ميجابايت) في `main`:
     ```cuda
     int list_size = 10000000;
     ```

2. **التحقق من تثبيت CUDA وتوافق وحدة معالجة الرسومات**:
   - يشير `cudaErrorUnknown` إلى وجود مشكلة محتملة في برنامج تشغيل CUDA، أو وقت التشغيل، أو توافق وحدة معالجة الرسومات. تحقق من إعداد CUDA لديك:
     ```bash
     nvcc --version
     nvidia-smi
     ```
   - تأكد من أن إصدار CUDA toolkit يتطابق مع إصدار برنامج التشغيل. على سبيل المثال، يتطلب CUDA 11.x برنامج تشغيل NVIDIA متوافق (تحقق من [جدول التوافق من NVIDIA](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)).
   - **الإصلاح**: قم بتحديث برنامج تشغيل NVIDIA وCUDA toolkit إلى أحدث الإصدارات. بالنسبة لأوبونتو، يمكنك تحديث برامج التشغيل باستخدام:
     ```bash
     sudo apt update
     sudo apt install nvidia-driver-<version> nvidia-cuda-toolkit
     ```
     استبدل `<version>` بأحدث إصدار برنامج تشغيل متوافق مع وحدة معالجة الرسومات الخاصة بك.

3. **التحقق من معالجة أخطاء CUDA**:
   - يفتقر الكود إلى فحص أخطاء CUDA الصريح، مما يمكن أن يساعد في تحديد المشكلة بدقة. قم بتعديل `parallel_sort_gpu` لتشمل فحص الأخطاء لعمليات CUDA:
     ```cuda
     #include <cuda_runtime.h>
     #include <stdio.h>
     #include <stdlib.h>
     #include <thrust/device_vector.h>
     #include <thrust/sort.h>
     #include <time.h>

     void checkCudaError(cudaError_t err, const char *msg) {
         if (err != cudaSuccess) {
             fprintf(stderr, "CUDA Error: %s: %s\n", msg, cudaGetErrorString(err));
             exit(EXIT_FAILURE);
         }
     }

     void parallel_sort_gpu(int *arr, int n) {
         cudaError_t err;
         thrust::device_vector<int> d_vec(arr, arr + n);
         err = cudaGetLastError();
         checkCudaError(err, "After device_vector allocation");
         
         thrust::sort(d_vec.begin(), d_vec.end());
         err = cudaGetLastError();
         checkCudaError(err, "After thrust::sort");
         
         thrust::copy(d_vec.begin(), d_vec.end(), arr);
         err = cudaGetLastError();
         checkCudaError(err, "After thrust::copy");
     }

     double benchmark(int list_size) {
         int *arr = (int*)malloc(list_size * sizeof(int));
         if (!arr) {
             fprintf(stderr, "Host memory allocation failed\n");
             exit(EXIT_FAILURE);
         }
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
         int list_size = 10000000; // Reduced for testing
         int num_runs = 8;

         printf("Run,TimeTakenSeconds\n");
         for (int i = 0; i < num_runs; ++i) {
             double t = benchmark(list_size);
             printf("%d,%.6f\n", i + 1, t);
         }
         return 0;
     }
     ```
   - **الإصلاح**: أعد تجميع وتشغيل الكود المعدل للحصول على رسائل خطأ مفصلة:
     ```bash
     nvcc -o cudamark scripts/benchmark/cudamark.cu
     ./cudamark
     ```

4. **تحسين دقة التوقيت**:
   - تقيس دالة `clock()` وقت وحدة المعالجة المركزية، وليس وقت تنفيذ وحدة معالجة الرسومات، مما قد لا يعكس أداء الفرز على وحدة معالجة الرسومات بدقة. استخدم أحداث CUDA للحصول على توقيت دقيق:
     ```cuda
     double benchmark(int list_size) {
         int *arr = (int*)malloc(list_size * sizeof(int));
         if (!arr) {
             fprintf(stderr, "Host memory allocation failed\n");
             exit(EXIT_FAILURE);
         }
         for (int i = 0; i < list_size; ++i) {
             arr[i] = rand() % 1000001;
         }

         cudaEvent_t start, stop;
         cudaEventCreate(&start);
         cudaEventCreate(&stop);
         cudaEventRecord(start);
         parallel_sort_gpu(arr, list_size);
         cudaEventRecord(stop);
         cudaEventSynchronize(stop);
         float milliseconds = 0;
         cudaEventElapsedTime(&milliseconds, start, stop);
         cudaEventDestroy(start);
         cudaEventDestroy(stop);

         free(arr);
         return milliseconds / 1000.0; // Convert to seconds
     }
     ```

5. **تأكد من تهيئة وحدة معالجة الرسومات**:
   - قد يفشل Thrust إذا لم يتم تهيئة سياق CUDA بشكل صحيح. أضف `cudaSetDevice` في بداية `main` لضمان تهيئة وحدة معالجة الرسومات:
     ```cuda
     int main() {
         cudaError_t err = cudaSetDevice(0);
         checkCudaError(err, "cudaSetDevice failed");
         int list_size = 10000000;
         int num_runs = 8;

         printf("Run,TimeTakenSeconds\n");
         for (int i = 0; i < num_runs; ++i) {
             double t = benchmark(list_size);
             printf("%d,%.6f\n", i + 1, t);
         }
         return 0;
     }
     ```

6. **أعد التجميع والاختبار**:
   - احفظ الكود المحدث كـ `cudamark.cu` وقم بتجميعه:
     ```bash
     nvcc -o cudamark scripts/benchmark/cudamark.cu
     ```
   - شغل البرنامج:
     ```bash
     ./cudamark
     ```

7. **معالجة استثناءات Thrust**:
   - قد يلقي Thrust استثناءات لأسباب مختلفة (مثل الوصول غير الصحيح إلى الذاكرة). لف عمليات Thrust في كتلة try-catch لالتقاط المزيد من التفاصيل:
     ```cuda
     void parallel_sort_gpu(int *arr, int n) {
         try {
             thrust::device_vector<int> d_vec(arr, arr + n);
             thrust::sort(d_vec.begin(), d_vec.end());
             thrust::copy(d_vec.begin(), d_vec.end(), arr);
         } catch (thrust::system_error &e) {
             fprintf(stderr, "Thrust error: %s\n", e.what());
             exit(EXIT_FAILURE);
         }
     }
     ```

8. **فحوصات إضافية**:
   - **دعم وحدة معالجة الرسومات**: تأكد من أن وحدة معالجة الرسومات الخاصة بك تدعم CUDA وThrust. وحدات معالجة الرسومات القديمة قد لا تدعم ميزات CUDA الجديدة. تحقق من طراز وحدة معالجة الرسومات مقابل قائمة دعم وحدات معالجة الرسومات من NVIDIA.
   - **موارد النظام**: تحقق من أن نظامك يحتوي على ذاكرة مضيف كافية للمصفوفة الكبيرة (`200 MB` لـ 50 مليون عدد صحيح). استخدم `free -h` للتحقق من ذاكرة الوصول العشوائي المتاحة.
   - **مسار الملف**: تأكد من أنك تقوم بتشغيل الملف الثنائي الصحيح. يشير الخطأ إلى `./test/cudamark`، لكن عملية التجميع كانت لـ `scripts/benchmark/cudamark.c`. تأكد من أن الملف الثنائي محدث وفي المسار الصحيح:
     ```bash
     nvcc -o test/cudamark scripts/benchmark/cudamark.cu
     ./test/cudamark
     ```

9. **إذا استمرت المشكلة**:
   - **التصحيح باستخدام إدخال أصغر**: عيّن `list_size = 1000` لاستبعاد مشاكل الذاكرة.
   - **التحقق من سجلات CUDA**: ابحث عن أخطاء مفصلة في سجلات النظام أو استخدم `cuda-memcheck`:
     ```bash
     cuda-memcheck ./cudamark
     ```
   - **أعد تثبيت CUDA**: إذا كان تثبيت CUDA تالفًا، أعد تثبيته:
     ```bash
     sudo apt purge nvidia* cuda*
     sudo apt install nvidia-cuda-toolkit
     ```

### النتيجة المتوقعة
بعد تطبيق هذه الإصلاحات، يجب أن يعمل البرنامج دون أخطاء `bad_alloc` أو `cudaErrorUnknown` وينتج نتيجة مثل:
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

### إذا واجهت أخطاء إضافية
- شارك ناتج `nvcc --version`، `nvidia-smi`، وأي رسائل خطأ جديدة من الكود المحدث.
- حدد طراز وحدة معالجة الرسومات وإصدار CUDA للحصول على نصائح مخصصة.

دعني أعرف إذا كنت بحاجة إلى مساعدة في خطوة محددة!