---
audio: false
generated: true
lang: ar
layout: post
title: مثال أساسي على كودا
translated: true
type: note
---

إليك مثال أساسي على CUDA يوضح برمجة GPU منخفضة المستوى باستخدام CUDA C. يؤدي هذا المثال عملية جمع متجهات بسيطة على وحدة معالجة الرسومات باستخدام البنى الأساسية الأكثر جوهرية في CUDA:

```c
#include <stdio.h>
#include <cuda.h>

// نواة CUDA لجمع المتجهات
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1024;  // حجم المتجه
    size_t size = n * sizeof(float);
    
    // تخصيص ذاكرة المضيف
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // تهيئة مصفوفات المضيف
    for(int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }

    // مؤشرات ذاكرة الجهاز
    float *d_a, *d_b, *d_c;
    
    // تخصيص ذاكرة الجهاز
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_c, size);

    // نسخ البيانات من المضيف إلى الجهاز
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // تكوين معلمات تشغيل النواة
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    // تشغيل النواة
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);

    // انتظار انتهاء وحدة معالجة الرسومات
    cudaDeviceSynchronize();

    // نسخ النتيجة مرة أخرى إلى المضيف
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    // التحقق من النتائج
    for(int i = 0; i < 10; i++) {
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }

    // تحرير ذاكرة الجهاز
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // تحرير ذاكرة المضيف
    free(h_a);
    free(h_b);
    free(h_c);

    // إعادة ضبط الجهاز
    cudaDeviceReset();

    return 0;
}
```

لتجميع وتشغيل هذا الكود، ستحتاج إلى:
1. وحدة معالجة رسومات NVIDIA مع دعم CUDA
2. CUDA Toolkit مثبت
3. التجميع باستخدام: `nvcc vector_add.cu -o vector_add`

يوضح هذا المثال العمليات الأساسية الأكثر جوهرية في CUDA:
- تعريف النواة `__global__`
- تخصيص الذاكرة يدويًا باستخدام `cudaMalloc`
- نقل الذاكرة الصريح باستخدام `cudaMemcpy`
- تكوين تشغيل النواة باستخدام `<<<blocks, threads>>>`
- مزامنة الجهاز
- تنظيف الذاكرة

الجوانب منخفضة المستوى الرئيسية:
1. إدارة الذاكرة المباشرة دون استخدام مساعدات وقت تشغيل CUDA
2. تكوين الخيط/الكتلة يدويًا
3. مزامنة الجهاز الصريحة
4. عمليات المؤشر الأولية
5. عدم وجود تجريدات أو مكتبات عالية المستوى

تستخدم النواة التسلسل الهرمي الأساسي لخيوط CUDA:
- `blockIdx.x`: فهرس الكتلة
- `blockDim.x`: الخيوط لكل كتلة
- `threadIdx.x`: فهرس الخيط داخل الكتلة

يحسب هذا معرفًا فريدًا للخيط لكل عنصر وينفذ عملية الجمع فقط إذا كان ضمن الحدود. يبقي المثال الأمور بسيطة لكنه يظهر المفاهيم الأساسية لبرمجة CUDA على مستوى منخفض.

سيظهر الإخراج النتائج العشر الأولى، مثل:
```
0.000000 + 0.000000 = 0.000000
1.000000 + 2.000000 = 3.000000
2.000000 + 4.000000 = 6.000000
...
```