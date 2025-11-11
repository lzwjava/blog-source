---
audio: false
generated: true
lang: ar
layout: post
title: مثال جمع المتجهات المعدنية
translated: true
type: note
---

إذا كنت تستخدم نظام macOS وتريد برمجة وحدة معالجة الرسومات باستخدام Metal (واجهة برمجة تطبيقات الرسومات والحسابية منخفضة المستوى من Apple)، يمكنك تحقيق وظائف مشابهة لمثال CUDA الذي قدمته سابقاً. تم تصميم Metal لمنحك وصولاً مباشراً إلى وحدة معالجة الرسومات على أجهزة Apple، بما في ذلك أجهزة Mac، وهو يدعم عمليات الرسومات والحسابية على حد سواء. فيما يلي مثال أساسي لـ Metal يقوم بإضافة متجهات (مشابه لمثال CUDA) باستخدام هياكل Metal منخفضة المستوى في C++.

### مثال إضافة المتجهات باستخدام Metal

يستخدم هذا المثال Metal لإضافة مصفوفتين على وحدة معالجة الرسومات. يتجنب التجريدات عالية المستوى ويتمسك بواجهة برمجة تطبيقات Metal الأساسية لنهج منخفض المستوى.

```cpp
#include <iostream>
#include <Metal/Metal.hpp>
#include <Foundation/Foundation.hpp>

int main() {
    // تهيئة جهاز Metal
    NS::SharedPtr<MTL::Device> device = NS::TransferPtr(MTL::CreateSystemDefaultDevice());
    if (!device) {
        std::cerr << "Failed to create Metal device" << std::endl;
        return 1;
    }

    // حجم المتجه
    const int n = 1024;
    const size_t bufferSize = n * sizeof(float);

    // بيانات المضيف
    float* h_a = new float[n];
    float* h_b = new float[n];
    float* h_c = new float[n];

    // تهيئة مصفوفات المضيف
    for (int i = 0; i < n; i++) {
        h_a[i] = static_cast<float>(i);
        h_b[i] = static_cast<float>(i * 2);
    }

    // إنشاء buffers في Metal
    NS::SharedPtr<MTL::Buffer> d_a = NS::TransferPtr(device->newBuffer(h_a, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_b = NS::TransferPtr(device->newBuffer(h_b, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_c = NS::TransferPtr(device->newBuffer(bufferSize, MTL::ResourceStorageModeShared));

    // إنشاء قائمة أوامر
    NS::SharedPtr<MTL::CommandQueue> queue = NS::TransferPtr(device->newCommandQueue());

    // تحميل مصدر shader الخاص بـ Metal (نواة إضافة المتجهات)
    const char* kernelSource = R"(
        #include <metal_stdlib>
        using namespace metal;

        kernel void vectorAdd(device const float* a,
                             device const float* b,
                             device float* c,
                             uint id [[thread_position_in_grid]]) {
            c[id] = a[id] + b[id];
        }
    )";

    // إنشاء library و function في Metal
    NS::Error* error = nullptr;
    NS::SharedPtr<NS::String> source = NS::TransferPtr(NS::String::string(kernelSource, NS::UTF8StringEncoding));
    NS::SharedPtr<MTL::Library> library = NS::TransferPtr(device->newLibrary(source.get(), nullptr, &error));
    if (!library) {
        std::cerr << "Failed to create library: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    NS::SharedPtr<MTL::Function> function = NS::TransferPtr(library->newFunction(NS::String::string("vectorAdd", NS::UTF8StringEncoding)));
    if (!function) {
        std::cerr << "Failed to create function" << std::endl;
        return 1;
    }

    // إنشاء حالة خط الأنابيب الحسابية
    NS::SharedPtr<MTL::ComputePipelineState> pipeline = NS::TransferPtr(device->newComputePipelineState(function.get(), &error));
    if (!pipeline) {
        std::cerr << "Failed to create pipeline: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    // إنشاء command buffer و encoder
    NS::SharedPtr<MTL::CommandBuffer> commandBuffer = NS::TransferPtr(queue->commandBuffer());
    NS::SharedPtr<MTL::ComputeCommandEncoder> encoder = NS::TransferPtr(commandBuffer->computeCommandEncoder());

    // تعيين خط الأنابيب و buffers
    encoder->setComputePipelineState(pipeline.get());
    encoder->setBuffer(d_a.get(), 0, 0);
    encoder->setBuffer(d_b.get(), 0, 1);
    encoder->setBuffer(d_c.get(), 0, 2);

    // تكوين مجموعات الخيوط
    MTL::Size gridSize = MTL::Size(n, 1, 1);
    int threadsPerGroup = pipeline->maxTotalThreadsPerThreadgroup();
    if (threadsPerGroup > n) threadsPerGroup = n;
    MTL::Size threadgroupSize = MTL::Size(threadsPerGroup, 1, 1);

    // إرسال نواة الحساب
    encoder->dispatchThreads(gridSize, threadgroupSize);
    encoder->endEncoding();

    // التنفيذ والانتظار
    commandBuffer->commit();
    commandBuffer->waitUntilCompleted();

    // الحصول على النتائج
    float* results = static_cast<float*>(d_c->contents());
    for (int i = 0; i < 10; i++) {
        std::cout << h_a[i] << " + " << h_b[i] << " = " << results[i] << std::endl;
    }

    // التنظيف
    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return 0;
}
```

### المتطلبات الأساسية
1.  **macOS**: يعمل هذا الكود على نظام macOS مع وحدة معالجة رسومات متوافقة (يجب أن يعمل على أي جهاز Mac حديث).
2.  **Xcode**: قم بتثبيت Xcode للحصول على إطار عمل Metal وأدوات سطر الأوامر.
3.  **التجميع**: استخدم `clang++` مع أطر عمل Metal:
    ```bash
    clang++ -framework Metal -framework Foundation vector_add.mm -o vector_add
    ```
    ملاحظة: احفظ الملف بامتداد `.mm` لأنه يستخدم Objective-C++ (يتطلب Metal وقت تشغيل Objective-C).

### الجوانب منخفضة المستوى الرئيسية
1.  **إدارة الموارد يدوياً**: إنشاء buffers صراحةً باستخدام `newBuffer` وإدارة الذاكرة دون أغلفة عالية المستوى.
2.  **تحديد Shader مباشرة**: يتم تعريف نواة Metal Shading Language (MSL) مضمنة كسلسلة، ويتم تجميعها أثناء وقت التشغيل.
3.  **تكوين الخيوط**: حساب أحجام الشبكة ومجموعة الخيوط يدوياً، بشكل مشابه لكتل وخيوط CUDA.
4.  **التحكم في Command Buffer**: إنشاء وإرسال command buffers صراحةً لتنفيذ وحدة معالجة الرسومات.
5.  **لا توجد تجريدات**: يتجنب MetalKit أو غيرها من أطر العمل عالية المستوى، ويتمسك بواجهات برمجة تطبيقات Metal الأساسية.

### الناتج
سيؤدي تشغيل هذا إلى إنتاج شيء مثل:
```
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

### الاختلافات عن CUDA
-   **نمط واجهة برمجة التطبيقات**: تستخدم Metal واجهة برمجة تطبيقات قائمة على Objective-C++ مع كائنات `NS::`، على عكس واجهة برمجة تطبيقات C الخاصة بـ CUDA.
-   **نموذج الذاكرة**: وضع التخزين المشترك لـ Metal (`MTL::ResourceStorageModeShared`) يسمح لوحدة المعالجة المركزية/وحدة معالجة الرسومات بالوصول إلى نفس الذاكرة، مما يبسط عمليات النقل مقارنة مع `cudaMemcpy` الصريحة في CUDA.
-   **نموذج الخيوط**: تستخدم Metal `dispatchThreads` مع أحجام الشبكة/مجموعة الخيوط، وهي مشابهة من الناحية المفاهيمية لنموذج الشبكة/الكتلة في CUDA ولكن بمصطلحات وتكوين مختلفين.

### نصائح لاستخدام Metal على macOS
-   **تصحيح الأخطاء**: استخدم أداة تصحيح Metal في Xcode لفحص تنفيذ وحدة معالجة الرسومات.
-   **التوثيق**: تحقق من توثيق Metal الخاص بـ Apple للحصول على تفاصيل أعمق (متوفر في Xcode أو عبر الإنترنت على developer.apple.com).
-   **الأداء**: لمجموعات البيانات الأكبر، قم بتحسين أحجام مجموعة الخيوط بناءً على `maxTotalThreadsPerThreadgroup`.

هذه نقطة انطلاق للبرمجة منخفضة المستوى باستخدام Metal على macOS. يمكنك توسيعه لمهام حسابية أكثر تعقيداً أو تقديم الرسومات حسب الحاجة!