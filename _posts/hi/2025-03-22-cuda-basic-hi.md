---
audio: false
generated: true
lang: hi
layout: post
title: मूल क्यूडा उदाहरण
translated: true
type: note
---

यहाँ CUDA C का उपयोग करके लो-लेवल GPU प्रोग्रामिंग को दर्शाने वाला एक बुनियादी CUDA उदाहरण है। यह उदाहरण सबसे मौलिक CUDA कंस्ट्रक्ट्स का उपयोग करके GPU पर एक साधारण वेक्टर जोड़ (vector addition) करता है:

```c
#include <stdio.h>
#include <cuda.h>

// वेक्टर जोड़ के लिए CUDA kernel
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1024;  // वेक्टर का आकार
    size_t size = n * sizeof(float);
    
    // होस्ट मेमोरी allocation
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // होस्ट arrays को initialize करें
    for(int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }

    // डिवाइस मेमोरी pointers
    float *d_a, *d_b, *d_c;
    
    // डिवाइस मेमोरी allocate करें
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_c, size);

    // डेटा को होस्ट से डिवाइस पर कॉपी करें
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // kernel launch parameters configure करें
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    // Kernel launch करें
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);

    // GPU के खत्म होने का इंतज़ार करें
    cudaDeviceSynchronize();

    // रिजल्ट को वापस होस्ट पर कॉपी करें
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    // रिजल्ट verify करें
    for(int i = 0; i < 10; i++) {
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }

    // डिवाइस मेमोरी free करें
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // होस्ट मेमोरी free करें
    free(h_a);
    free(h_b);
    free(h_c);

    // डिवाइस reset करें
    cudaDeviceReset();

    return 0;
}
```

इस कोड को compile और run करने के लिए, आपको चाहिए:
1. CUDA सपोर्ट वाला NVIDIA GPU
2. इंस्टॉल किया हुआ CUDA Toolkit
3. इसे compile करें: `nvcc vector_add.cu -o vector_add`

यह उदाहरण सबसे मौलिक CUDA operations को दर्शाता है:
- `__global__` kernel definition
- `cudaMalloc` के साथ मैन्युअल मेमोरी allocation
- `cudaMemcpy` के साथ एक्सप्लिसिट मेमोरी ट्रांसफर
- `<<<blocks, threads>>>` के साथ kernel launch configuration
- डिवाइस synchronization
- मेमोरी cleanup

मुख्य लो-लेवल पहलू:
1. CUDA runtime helpers का उपयोग किए बिना डायरेक्ट मेमोरी मैनेजमेंट
2. मैन्युअल thread/block configuration
3. एक्सप्लिसिट डिवाइस synchronization
4. रॉ पॉइंटर operations
5. कोई हाई-लेवल अब्स्ट्रैक्शन या लाइब्रेरीज़ नहीं

Kernel बेसिक CUDA thread hierarchy का उपयोग करता है:
- `blockIdx.x`: ब्लॉक इंडेक्स
- `blockDim.x`: प्रति ब्लॉक थ्रेड्स
- `threadIdx.x`: ब्लॉक के भीतर थ्रेड इंडेक्स

यह प्रत्येक एलिमेंट के लिए एक यूनिक थ्रेड ID की गणना करता है और केवल बाउंड्स के भीतर होने पर ही जोड़ करता है। उदाहरण इसे सरल रखता है लेकिन लो लेवल पर CUDA प्रोग्रामिंग की कोर कॉन्सेप्ट्स दिखाता है।

आउटपुट पहले 10 रिजल्ट्स दिखाएगा, जैसे:
```
0.000000 + 0.000000 = 0.000000
1.000000 + 2.000000 = 3.000000
2.000000 + 4.000000 = 6.000000
...
```