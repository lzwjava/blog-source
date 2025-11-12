---
audio: false
generated: true
lang: hi
layout: post
title: CUDA ड्राइवर एपीआई
translated: true
type: note
---

`<cuda.h>` हैडर **CUDA ड्राइवर API** का एक हिस्सा है, जो CUDA रनटाइम API (जैसे `cudaMalloc`, `cudaMemcpy`) की तुलना में एक लो-लेवल API है। ड्राइवर API GPU संसाधनों (जैसे contexts, modules, streams) पर बारीक नियंत्रण प्रदान करती है और अक्सर उन्नत परिदृश्यों में उपयोग की जाती है, जैसे मल्टी-GPU प्रोग्रामिंग, डायनामिक kernel लोडिंग, या लो-लेवल ऑप्टिमाइज़ेशन।

### सामान्य CUDA ड्राइवर API फंक्शन
यहां कुछ प्रमुख फ़ंक्शन और उनके उद्देश्य दिए गए हैं:

| फंक्शन                          | विवरण                                                                                   |
|----------------------------------|-----------------------------------------------------------------------------------------------|
| **`cuInit(unsigned int flags)`** | CUDA ड्राइवर को इनिशियलाइज़ करता है। किसी भी अन्य ड्राइवर API फ़ंक्शन से पहले कॉल किया जाना चाहिए। |
| **`cuDeviceGet(CUdevice *dev, int ordinal)`** | निर्दिष्ट ऑर्डिनल (जैसे, पहले GPU के लिए `0`) वाले GPU डिवाइस के लिए एक हैंडल प्राप्त करता है। |
| **`cuCtxCreate(CUcontext *ctx, unsigned int flags, CUdevice dev)`** | निर्दिष्ट डिवाइस पर एक CUDA context बनाता है। |
| **`cuModuleLoad(CUmodule *mod, const char *fname)`** | एक PTX या cubin फ़ाइल को मौजूदा context में एक मॉड्यूल के रूप में लोड करता है। |
| **`cuModuleGetFunction(CUfunction *func, CUmodule mod, const char *name)`** | एक लोड किए गए मॉड्यूल से एक kernel फ़ंक्शन प्राप्त करता है। |
| **`cuMemAlloc(CUdeviceptr *dptr, size_t bytesize)`** | GPU पर मेमोरी आवंटित करता है। |
| **`cuMemcpyHtoD(CUdeviceptr dst, const void *src, size_t bytes)`** | होस्ट (CPU) से डिवाइस (GPU) पर डेटा कॉपी करता है। |
| **`cuMemcpyDtoH(void *dst, CUdeviceptr src, size_t bytes)`** | डिवाइस (GPU) से होस्ट (CPU) पर डेटा कॉपी करता है। |
| **`cuLaunchKernel(CUfunction f, ...)`** | निर्दिष्ट grid/block dimensions और parameters के साथ एक kernel फ़ंक्शन लॉन्च करता है। |

---

### उदाहरण वर्कफ़्लो
नीचे CUDA ड्राइवर API का उपयोग करने का एक सरल उदाहरण दिया गया है:
1. ड्राइवर को इनिशियलाइज़ करना।
2. GPU मेमोरी आवंटित करना।
3. GPU से/पर डेटा कॉपी करना।
4. एक PTX फ़ाइल से kernel लोड करना और उसे execute करना।

```cpp
#include <cuda.h>
#include <stdio.h>

int main() {
    CUdevice dev;
    CUcontext ctx;
    CUmodule mod;
    CUfunction kernel;
    CUresult err;

    // 1. CUDA ड्राइवर को इनिशियलाइज़ करें
    cuInit(0);

    // 2. डिवाइस 0 (पहला GPU) के लिए हैंडल प्राप्त करें
    cuDeviceGet(&dev, 0);

    // 3. डिवाइस पर एक context बनाएं
    cuCtxCreate(&ctx, 0, dev);

    // 4. एक PTX मॉड्यूल लोड करें (उदाहरण के लिए, एक .cu फ़ाइल से जेनरेट किया गया)
    cuModuleLoad(&mod, "my_kernel.ptx");

    // 5. मॉड्यूल से kernel फ़ंक्शन प्राप्त करें
    cuModuleGetFunction(&kernel, mod, "my_kernel");

    // 6. GPU मेमोरी आवंटित करें
    size_t N = 1024;
    CUdeviceptr d_data;
    cuMemAlloc(&d_data, N * sizeof(float));

    // 7. होस्ट से डिवाइस पर डेटा कॉपी करें
    float h_data[N] = {1.0f};
    cuMemcpyHtoD(d_data, h_data, N * sizeof(float));

    // 8. kernel parameters कॉन्फ़िगर करें
    void *args[] = { &d_data, &N };
    int blockSize = 256;
    int gridSize = (N + blockSize - 1) / blockSize;

    // 9. kernel लॉन्च करें
    cuLaunchKernel(
        kernel,
        gridSize, 1, 1,    // Grid dimensions
        blockSize, 1, 1,   // Block dimensions
        0, NULL,           // Shared memory और stream
        args, NULL         // Kernel arguments
    );

    // 10. परिणामों को वापस होस्ट पर कॉपी करें
    cuMemcpyDtoH(h_data, d_data, N * sizeof(float));

    // 11. क्लीनअप
    cuMemFree(d_data);
    cuModuleUnload(mod);
    cuCtxDestroy(ctx);

    return 0;
}
```

---

### मुख्य नोट्स
1. **एरर हैंडलिंग**: हमेशा रिटर्न वैल्यू चेक करें (जैसे, `CUresult err = cuSomeFunction(...);`)। एरर को डिकोड करने के लिए `cuGetErrorString(err)` का उपयोग करें।
2. **Kernel Parameters**: `cuLaunchKernel` के लिए, पैरामीटर arguments के पॉइंटर्स की एक array के रूप में पास किए जाते हैं। सुनिश्चित करें कि क्रम kernel के अपेक्षित parameters से मेल खाता हो।
3. **PTX फाइलें**: Kernels को PTX में कंपाइल किया जाना चाहिए (जैसे, `nvcc --ptx my_kernel.cu -o my_kernel.ptx`)।
4. **Context मैनेजमेंट**: Contexts CPU प्रक्रियाओं के अनुरूप होते हैं - वे GPU के लिए संसाधनों का प्रबंधन करते हैं। मल्टी-थ्रेडेड कोड के लिए `cuCtxPushCurrent`/`cuCtxPopCurrent` का उपयोग करें।

---

### ड्राइवर API का उपयोग कब करें?
- **डायनामिक Kernel लोडिंग**: रनटाइम पर PTX लोड करना।
- **मल्टी-GPU कंट्रोल**: एक्सप्लिसिटली कई GPUs का प्रबंधन करना।
- **लो-लेवल ऑप्टिमाइज़ेशन**: contexts, streams, या मेमोरी पर बारीक नियंत्रण।

अधिकांश एप्लिकेशन के लिए, हाई-लेवल **रनटाइम API** (जैसे `cudaMalloc`, `cudaMemcpy`) पर्याप्त और सरल है। ड्राइवर API का उपयोग तब करें जब आपको इसकी उन्नत सुविधाओं की आवश्यकता हो।