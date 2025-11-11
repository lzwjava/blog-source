---
audio: false
generated: true
lang: hi
layout: post
title: धातु वेक्टर योग उदाहरण
translated: true
type: note
---

यदि आप macOS का उपयोग कर रहे हैं और Metal (Apple का लो-लेवल ग्राफिक्स और कंप्यूट API) का उपयोग करके GPU को प्रोग्राम करना चाहते हैं, तो आप मेरे द्वारा पहले दिए गए CUDA उदाहरण के समान कार्यक्षमता प्राप्त कर सकते हैं। Metal को Apple उपकरणों, जिसमें Mac शामिल हैं, पर GPU तक सीधी पहुंच प्रदान करने के लिए डिज़ाइन किया गया है, और यह ग्राफिक्स और कंप्यूट दोनों ऑपरेशन्स को सपोर्ट करता है। नीचे C++ में लो-लेवल Metal कंस्ट्रक्ट्स का उपयोग करके वेक्टर जोड़ (CUDA उदाहरण के समान) करने वाला एक बेसिक Metal उदाहरण दिया गया है।

### Metal वेक्टर एडिशन उदाहरण

यह उदाहरण GPU पर दो ऐरे जोड़ने के लिए Metal का उपयोग करता है। यह हाई-लेवल एब्स्ट्रक्शन से बचता है और लो-लेवल एप्रोच के लिए कोर Metal API पर टिका रहता है।

```cpp
#include <iostream>
#include <Metal/Metal.hpp>
#include <Foundation/Foundation.hpp>

int main() {
    // Metal डिवाइस इनिशियलाइज़ करें
    NS::SharedPtr<MTL::Device> device = NS::TransferPtr(MTL::CreateSystemDefaultDevice());
    if (!device) {
        std::cerr << "Metal डिवाइस बनाने में विफल" << std::endl;
        return 1;
    }

    // वेक्टर साइज़
    const int n = 1024;
    const size_t bufferSize = n * sizeof(float);

    // होस्ट डेटा
    float* h_a = new float[n];
    float* h_b = new float[n];
    float* h_c = new float[n];

    // होस्ट ऐरे इनिशियलाइज़ करें
    for (int i = 0; i < n; i++) {
        h_a[i] = static_cast<float>(i);
        h_b[i] = static_cast<float>(i * 2);
    }

    // Metal बफ़र बनाएं
    NS::SharedPtr<MTL::Buffer> d_a = NS::TransferPtr(device->newBuffer(h_a, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_b = NS::TransferPtr(device->newBuffer(h_b, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_c = NS::TransferPtr(device->newBuffer(bufferSize, MTL::ResourceStorageModeShared));

    // कमांड क्यू बनाएं
    NS::SharedPtr<MTL::CommandQueue> queue = NS::TransferPtr(device->newCommandQueue());

    // Metal शेडर सोर्स लोड करें (वेक्टर एडिशन कर्नेल)
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

    // Metal लाइब्रेरी और फ़ंक्शन बनाएं
    NS::Error* error = nullptr;
    NS::SharedPtr<NS::String> source = NS::TransferPtr(NS::String::string(kernelSource, NS::UTF8StringEncoding));
    NS::SharedPtr<MTL::Library> library = NS::TransferPtr(device->newLibrary(source.get(), nullptr, &error));
    if (!library) {
        std::cerr << "लाइब्रेरी बनाने में विफल: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    NS::SharedPtr<MTL::Function> function = NS::TransferPtr(library->newFunction(NS::String::string("vectorAdd", NS::UTF8StringEncoding)));
    if (!function) {
        std::cerr << "फ़ंक्शन बनाने में विफल" << std::endl;
        return 1;
    }

    // कंप्यूट पाइपलाइन स्टेट बनाएं
    NS::SharedPtr<MTL::ComputePipelineState> pipeline = NS::TransferPtr(device->newComputePipelineState(function.get(), &error));
    if (!pipeline) {
        std::cerr << "पाइपलाइन बनाने में विफल: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    // कमांड बफ़र और एनकोडर बनाएं
    NS::SharedPtr<MTL::CommandBuffer> commandBuffer = NS::TransferPtr(queue->commandBuffer());
    NS::SharedPtr<MTL::ComputeCommandEncoder> encoder = NS::TransferPtr(commandBuffer->computeCommandEncoder());

    // पाइपलाइन और बफ़र सेट करें
    encoder->setComputePipelineState(pipeline.get());
    encoder->setBuffer(d_a.get(), 0, 0);
    encoder->setBuffer(d_b.get(), 0, 1);
    encoder->setBuffer(d_c.get(), 0, 2);

    // थ्रेड ग्रुप कॉन्फ़िगर करें
    MTL::Size gridSize = MTL::Size(n, 1, 1);
    int threadsPerGroup = pipeline->maxTotalThreadsPerThreadgroup();
    if (threadsPerGroup > n) threadsPerGroup = n;
    MTL::Size threadgroupSize = MTL::Size(threadsPerGroup, 1, 1);

    // कंप्यूट कर्नेल डिस्पैच करें
    encoder->dispatchThreads(gridSize, threadgroupSize);
    encoder->endEncoding();

    // एक्ज़िक्यूट करें और प्रतीक्षा करें
    commandBuffer->commit();
    commandBuffer->waitUntilCompleted();

    // परिणाम प्राप्त करें
    float* results = static_cast<float*>(d_c->contents());
    for (int i = 0; i < 10; i++) {
        std::cout << h_a[i] << " + " << h_b[i] << " = " << results[i] << std::endl;
    }

    // क्लीनअप
    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return 0;
}
```

### आवश्यक शर्तें
1.  **macOS**: यह कोड एक कंपेटिबल GPU (कोई भी मॉडर्न Mac काम करना चाहिए) के साथ macOS पर चलता है।
2.  **Xcode**: Metal फ्रेमवर्क और कमांड-लाइन टूल्स पाने के लिए Xcode इंस्टॉल करें।
3.  **कंपाइल**: Metal फ्रेमवर्क के साथ `clang++` का उपयोग करें:
    ```bash
    clang++ -framework Metal -framework Foundation vector_add.mm -o vector_add
    ```
    नोट: फ़ाइल को `.mm` एक्सटेंशन के साथ सेव करें क्योंकि यह Objective-C++ का उपयोग करता है (Metal को Objective-C रनटाइम की आवश्यकता होती है)।

### मुख्य लो-लेवल पहलू
1.  **मैनुअल रिसोर्स मैनेजमेंट**: `newBuffer` के साथ एक्सप्लिसिटली बफ़र बनाना और हाई-लेवल रैपर के बिना मेमोरी मैनेज करना।
2.  **डायरेक्ट शेडर डेफिनिशन**: Metal शेडिंग लैंग्वेज (MSL) कर्नेल को इनलाइन एक स्ट्रिंग के रूप में डिफाइन किया गया है, जो रनटाइम पर कंपाइल होता है।
3.  **थ्रेड कॉन्फ़िगरेशन**: ग्रिड और थ्रेडग्रुप साइज़ को मैन्युअली कैलकुलेट करना, CUDA के ब्लॉक्स और थ्रेड्स के समान।
4.  **कमांड बफ़र कंट्रोल**: GPU एक्ज़िक्यूशन के लिए एक्सप्लिसिटली कमांड बफ़र बनाना और कमिट करना।
5.  **कोई एब्स्ट्रक्शन नहीं**: MetalKit या अन्य हाई-लेवल फ्रेमवर्क से बचता है, और कोर Metal API पर टिका रहता है।

### आउटपुट
इसे चलाने पर कुछ इस तरह का आउटपुट मिलेगा:
```
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

### CUDA से अंतर
-   **API स्टाइल**: Metal, CUDA के C-स्टाइल API के विपरीत, `NS::` ऑब्जेक्ट्स के साथ एक Objective-C++-आधारित API का उपयोग करता है।
-   **मेमोरी मॉडल**: Metal का शेयर्ड स्टोरेज मोड (`MTL::ResourceStorageModeShared`) CPU/GPU को एक ही मेमोरी तक पहुंच की अनुमति देता है, जो CUDA के एक्सप्लिसिट `cudaMemcpy` की तुलना में ट्रांसफर को सरल बनाता है।
-   **थ्रेड मॉडल**: Metal ग्रिड/थ्रेडग्रुप साइज़ के साथ `dispatchThreads` का उपयोग करता है, जो कॉन्सेप्चुअली CUDA के ग्रिड/ब्लॉक मॉडल के समान है लेकिन अलग टर्मिनोलॉजी और कॉन्फ़िगरेशन के साथ।

### macOS पर Metal के लिए टिप्स
-   **डीबगिंग**: GPU एक्ज़िक्यूशन का निरीक्षण करने के लिए Xcode के Metal डीबगर का उपयोग करें।
-   **डॉक्यूमेंटेशन**: गहरी जानकारी के लिए Apple की Metal डॉक्यूमेंटेशन देखें (Xcode में या ऑनलाइन developer.apple.com पर उपलब्ध)।
-   **परफॉर्मेंस**: बड़े डेटासेट के लिए, `maxTotalThreadsPerThreadgroup` के आधार पर थ्रेडग्रुप साइज़ को ऑप्टिमाइज़ करें।

यह macOS पर लो-लेवल Metal प्रोग्रामिंग के लिए एक शुरुआती बिंदु है। आप इसे अधिक कॉम्प्लेक्स कंप्यूट टास्क्स या ग्राफिक्स रेंडरिंग के लिए एक्सटेंड कर सकते हैं!