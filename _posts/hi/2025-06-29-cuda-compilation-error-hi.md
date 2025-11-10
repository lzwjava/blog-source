---
audio: false
generated: true
lang: hi
layout: post
title: CUDA संकलन त्रुटि को nvcc से ठीक करें
translated: true
type: note
---

त्रुटि संकेत देती है कि CUDA टूलकिट इंस्टॉल या ठीक से कॉन्फ़िगर नहीं है, क्योंकि कंपाइलर `cuda.h` को नहीं ढूंढ पा रहा है। इसके अलावा, आपका कोड एक CUDA स्रोत फ़ाइल (`.cu`) है लेकिन आप इसे `gcc` के साथ कंपाइल करने का प्रयास कर रहे हैं, जो CUDA कोड के लिए उपयुक्त नहीं है। आपको `nvcc`, NVIDIA CUDA कंपाइलर का उपयोग करना होगा। इसे ठीक करने का तरीका यहां बताया गया है:

### ठीक करने के चरण

1.  **CUDA टूलकिट इंस्टॉल करें**:
    *   सुनिश्चित करें कि NVIDIA CUDA टूलकिट आपके सिस्टम पर इंस्टॉल है। आप इसे [NVIDIA CUDA टूलकिट वेबसाइट](https://developer.nvidia.com/cuda-downloads) से डाउनलोड कर सकते हैं।
    *   अपने ऑपरेटिंग सिस्टम (इस मामले में Linux, प्रॉम्प्ट के आधार पर) के लिए इंस्टॉलेशन निर्देशों का पालन करें।
    *   इंस्टॉलेशन के बाद, इसे चलाकर सत्यापित करें:
        ```bash
        nvcc --version
        ```
        अगर सही तरीके से इंस्टॉल किया गया है तो यह CUDA वर्जन दिखाना चाहिए।

2.  **कंपाइल करने के लिए `nvcc` का उपयोग करें**:
    *   चूंकि आपकी फ़ाइल एक CUDA स्रोत फ़ाइल (`.cu`) है, इसे `gcc` के बजाय `nvcc` के साथ कंपाइल करें। इसे बदलें:
        ```bash
        gcc scripts/benchmark/cudamark.c
        ```
        इसके साथ:
        ```bash
        nvcc scripts/benchmark/cudamark.cu
        ```
    *   नोट: सुनिश्चित करें कि फ़ाइल एक्सटेंशन आपकी वास्तविक फ़ाइल से मेल खाता हो (आपके दिए गए कोड में `.cu`, त्रुटि में `.c` नहीं)।

3.  **CUDA एनवायरनमेंट सेट अप करें**:
    *   सुनिश्चित करें कि CUDA टूलकिट पथ आपके एनवायरनमेंट में शामिल हैं। अपनी `~/.bashrc` या समतुल्य शेल कॉन्फ़िगरेशन फ़ाइल में निम्नलिखित जोड़ें:
        ```bash
        export PATH=/usr/local/cuda/bin:$PATH
        export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
        ```
        फिर, फ़ाइल को सोर्स करें:
        ```bash
        source ~/.bashrc
        ```

4.  **Thrust लाइब्रेरी लिंक करें**:
    *   आपका कोड Thrust का उपयोग करता है, जो CUDA टूलकिट का हिस्सा है, इसलिए किसी अतिरिक्त लाइब्रेरी को स्पष्ट रूप से लिंक करने की आवश्यकता नहीं है। हालांकि, सुनिश्चित करें कि आपके पास एक संगत CUDA वर्जन है (Thrust CUDA 7.0 और बाद के वर्जन में शामिल है)।

5.  **कोड समस्याएं ठीक करें**:
    *   कोड `thread_counts` को संदर्भित करता है लेकिन `benchmark` फ़ंक्शन में इसका उपयोग नहीं करता है। `parallel_sort_gpu` फ़ंक्शन Thrust का उपयोग करता है, जो समांतरता को आंतरिक रूप से प्रबंधित करता है, इसलिए `main` में `thread_counts` लूप भ्रामक है। यदि आपका इरादा विभिन्न थ्रेड कॉन्फ़िगरेशन को बेंचमार्क करने का था, तो Thrust का सॉर्ट सीधे थ्रेड काउंट नियंत्रण की अनुमति नहीं देता है। आप इस लॉजिक को स्पष्ट करना चाह सकते हैं या अप्रयुक्त `thread_counts` को हटा सकते हैं।
    *   स्पष्टता के लिए, आप समय में भिन्नता का औसत निकालने के लिए एक ही सूची आकार को कई बार बेंचमार्क करने के लिए कोड को संशोधित कर सकते हैं:

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
            int num_runs = 8; // औसत निकालने के लिए रन की संख्या

            printf("Run,TimeTakenSeconds\n");
            for (int i = 0; i < num_runs; ++i) {
                double t = benchmark(list_size);
                printf("%d,%.6f\n", i + 1, t);
            }
            return 0;
        }
        ```

6.  **अपडेट किए गए कोड को कंपाइल करें**:
    *   कोड को `cudamark.cu` के रूप में सेव करें और इसे कंपाइल करें:
        ```bash
        nvcc -o cudamark scripts/benchmark/cudamark.cu
        ```
    *   यदि आपको लिंकर त्रुटियाँ मिलती हैं, तो सुनिश्चित करें कि CUDA लाइब्रेरीज़ सुलभ हैं (चरण 3 देखें)।

7.  **प्रोग्राम रन करें**:
    *   कंपाइल की गई बाइनरी को एक्ज़िक्यूट करें:
        ```bash
        ./cudamark
        ```

8.  **अतिरिक्त नोट्स**:
    *   **फ़ाइल एक्सटेंशन**: सुनिश्चित करें कि फ़ाइल का एक्सटेंशन `.cu` है, क्योंकि CUDA फ़ाइलों के लिए `nvcc` द्वारा उन्हें सही तरीके से प्रोसेस करने के लिए इसकी आवश्यकता होती है।
    *   **GPU उपलब्धता**: सुनिश्चित करें कि आपके पास एक CUDA-सक्षम GPU और सही ड्राइवर इंस्टॉल हैं। इसके साथ जांचें:
        ```bash
        nvidia-smi
        ```
    *   **Thrust और CUDA वर्जन**: सत्यापित करें कि आपका CUDA वर्जन Thrust को सपोर्ट करता है। आधुनिक Thrust फ़ीचर्स के लिए CUDA 11.x या बाद का वर्जन अनुशंसित है।
    *   **टाइमिंग सटीकता**: `clock()` फ़ंक्शन CPU टाइम को मापता है, GPU एक्ज़िक्यूशन टाइम को नहीं। अधिक सटीक GPU टाइमिंग के लिए, CUDA इवेंट्स का उपयोग करने पर विचार करें:
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
        return milliseconds / 1000.0; // सेकंड में बदलें
        ```

9.  **यदि त्रुटियाँ बनी रहती हैं**:
    *   यदि `cuda.h` अभी भी नहीं मिला है, तो CUDA टूलकिट इंस्टॉलेशन पथ (जैसे, `/usr/local/cuda/include`) सत्यापित करें। आपको शायद include पथ को स्पष्ट रूप से निर्दिष्ट करने की आवश्यकता हो सकती है:
        ```bash
        nvcc -I/usr/local/cuda/include -o cudamark scripts/benchmark/cudamark.cu
        ```
    *   सुनिश्चित करें कि फ़ाइल पथ `scripts/benchmark/cudamark.cu` आपके वर्तमान डायरेक्टरी के सापेक्ष सही है।

### अपडेट किया गया कंपाइलेशन कमांड
```bash
nvcc -o cudamark scripts/benchmark/cudamark.cu
```

### अपेक्षित आउटपुट
समस्याओं को ठीक करने के बाद, `./cudamark` चलाने पर इस तरह का आउटपुट मिलना चाहिए:
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

यदि आपको आगे सहायता की आवश्यकता है या कोई विशिष्ट त्रुटियाँ मिलती हैं, तो कृपया उन्हें साझा करें!