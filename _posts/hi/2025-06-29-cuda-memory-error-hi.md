---
audio: false
generated: true
lang: hi
layout: post
title: थ्रस्ट क्यूडीए मेमोरी आवंटन त्रुटियों को ठीक करना
translated: true
type: note
---

`thrust::system::detail::bad_alloc` त्रुटि और उसके बाद `cudaErrorUnknown: unknown error` तथा `Aborted (core dumped)` आपके CUDA प्रोग्राम में एक रनटाइम समस्या की ओर इशारा करते हैं, जो संभवतः Thrust का उपयोग करके सॉर्टिंग करते समय मेमोरी एलोकेशन या GPU कम्पैटिबिलिटी से संबंधित है। यह त्रुटि आमतौर पर तब उत्पन्न होती है जब CUDA रनटाइम को कोई समस्या आती है, जैसे अपर्याप्त GPU मेमोरी, असंगत GPU, या गलत तरीके से कॉन्फ़िगर किया गया CUDA वातावरण। नीचे, मैं प्रदान किए गए कोड और त्रुटि के आधार पर समस्या का निदान और समाधान करने के चरणों का वर्णन करूंगा।

### समाधान के चरण

1.  **GPU मेमोरी उपलब्धता जांचें**:
    - आपका प्रोग्राम Thrust के `device_vector` का उपयोग करके GPU पर एक बड़ी ऐरे (`list_size = 50,000,000` इंटीजर्स, लगभग 200 MB) एलोकेट करता है। यदि आपके GPU की मेमोरी सीमित है या अन्य प्रक्रियाएं इसका उपयोग कर रही हैं, तो यह `bad_alloc` त्रुटि का कारण बन सकता है।
    - GPU मेमोरी उपयोग जांचने के लिए `nvidia-smi` चलाएँ:
      ```bash
      nvidia-smi
      ```
    - सुनिश्चित करें कि GPU पर पर्याप्त खाली मेमोरी है। यदि अन्य प्रक्रियाएं मेमोरी का उपयोग कर रही हैं, तो उन्हें समाप्त करें या संसाधनों को मुक्त करने के लिए रीबूट करें।
    - **समाधान**: यह जांचने के लिए कि क्या समस्या मेमोरी से संबंधित है, `list_size` को कम करके परखें। `main` में `list_size = 10,000,000` (40 MB) सेट करके देखें:
      ```cuda
      int list_size = 10000000;
      ```

2.  **CUDA इंस्टालेशन और GPU कम्पैटिबिलिटी सत्यापित करें**:
    - `cudaErrorUnknown` CUDA ड्राइवर, रनटाइम, या GPU कम्पैटिबिलिटी में संभावित समस्या का संकेत दे सकता है। अपना CUDA सेटअप सत्यापित करें:
      ```bash
      nvcc --version
      nvidia-smi
      ```
    - सुनिश्चित करें कि CUDA टूलकिट का संस्करण ड्राइवर संस्करण से मेल खाता हो। उदाहरण के लिए, CUDA 11.x के लिए एक संगत NVIDIA ड्राइवर की आवश्यकता होती है ([NVIDIA की कम्पैटिबिलिटी तालिका](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html) देखें)।
    - **समाधान**: अपने NVIDIA ड्राइवर और CUDA टूलकिट को नवीनतम संस्करणों में अपडेट करें। Ubuntu के लिए, आप ड्राइवर को इस प्रकार अपडेट कर सकते हैं:
      ```bash
      sudo apt update
      sudo apt install nvidia-driver-<version> nvidia-cuda-toolkit
      ```
      `<version>` को आपके GPU के लिए संगत नवीनतम ड्राइवर संस्करण से बदलें।

3.  **CUDA एरर हैंडलिंग जांचें**:
    - कोड में स्पष्ट CUDA एरर चेकिंग का अभाव है, जो समस्या का सटीक पता लगाने में मदद कर सकती है। CUDA ऑपरेशन्स के लिए एरर चेकिंग शामिल करने के लिए `parallel_sort_gpu` को संशोधित करें:
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
          int list_size = 10000000; // परीक्षण के लिए कम किया गया
          int num_runs = 8;

          printf("Run,TimeTakenSeconds\n");
          for (int i = 0; i < num_runs; ++i) {
              double t = benchmark(list_size);
              printf("%d,%.6f\n", i + 1, t);
          }
          return 0;
      }
      ```
    - **समाधान**: विस्तृत एरर संदेश प्राप्त करने के लिए संशोधित कोड को पुनः कंपाइल करें और चलाएँ:
      ```bash
      nvcc -o cudamark scripts/benchmark/cudamark.cu
      ./cudamark
      ```

4.  **टाइमिंग सटीकता में सुधार करें**:
    - `clock()` फ़ंक्शन CPU टाइम को मापता है, GPU एक्सेक्यूशन टाइम को नहीं, जो GPU सॉर्टिंग परफॉर्मेंस को सही ढंग से नहीं दर्शा सकता है। सटीक टाइमिंग के लिए CUDA इवेंट्स का उपयोग करें:
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
          return milliseconds / 1000.0; // सेकंड में बदलें
      }
      ```

5.  **GPU इनिशियलाइजेशन सुनिश्चित करें**:
    - Thrust विफल हो सकता है यदि CUDA कॉन्टेक्स्ट ठीक से इनिशियलाइज़ नहीं है। यह सुनिश्चित करने के लिए कि GPU इनिशियलाइज़ हो गया है, `main` की शुरुआत में `cudaSetDevice` जोड़ें:
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

6.  **पुनः कंपाइल करें और परीक्षण करें**:
    - अपडेट किए गए कोड को `cudamark.cu` के रूप में सेव करें और कंपाइल करें:
      ```bash
      nvcc -o cudamark scripts/benchmark/cudamark.cu
      ```
    - प्रोग्राम चलाएँ:
      ```bash
      ./cudamark
      ```

7.  **Thrust एक्सेप्शन्स को हैंडल करें**:
    - Thrust विभिन्न कारणों से (जैसे, अमान्य मेमोरी एक्सेस) एक्सेप्शन्स फेंक सकता है। अधिक विवरण प्राप्त करने के लिए Thrust ऑपरेशन्स को try-catch ब्लॉक में लपेटें:
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

8.  **अतिरिक्त जांचें**:
    - **GPU सपोर्ट**: सुनिश्चित करें कि आपका GPU CUDA और Thrust को सपोर्ट करता है। पुराने GPU नए CUDA फीचर्स को सपोर्ट नहीं कर सकते हैं। NVIDIA की CUDA GPU सपोर्ट सूची के विरुद्ध अपने GPU मॉडल की जांच करें।
    - **सिस्टम रिसोर्सेज**: सत्यापित करें कि आपके सिस्टम में बड़ी ऐरे (50M इंटीजर्स के लिए `200 MB`) के लिए पर्याप्त होस्ट मेमोरी है। उपलब्ध RAM जांचने के लिए `free -h` का उपयोग करें।
    - **फ़ाइल पाथ**: पुष्टि करें कि आप सही बाइनरी चला रहे हैं। त्रुटि में `./test/cudamark` का उल्लेख है, लेकिन कंपाइलेशन `scripts/benchmark/cudamark.cu` के लिए थी। सुनिश्चित करें कि बाइनरी अप-टू-डेट है और सही डायरेक्टरी में है:
      ```bash
      nvcc -o test/cudamark scripts/benchmark/cudamark.cu
      ./test/cudamark
      ```

9.  **यदि समस्या बनी रहती है**:
    - **छोटे इनपुट के साथ डीबग करें**: मेमोरी समस्याओं से निपटने के लिए `list_size = 1000` सेट करें।
    - **CUDA लॉग्स जांचें**: सिस्टम लॉग्स में विस्तृत त्रुटियों की तलाश करें या `cuda-memcheck` का उपयोग करें:
      ```bash
      cuda-memcheck ./cudamark
      ```
    - **CUDA पुनः इंस्टॉल करें**: यदि CUDA इंस्टालेशन खराब है, तो इसे पुनः इंस्टॉल करें:
      ```bash
      sudo apt purge nvidia* cuda*
      sudo apt install nvidia-cuda-toolkit
      ```

### अपेक्षित परिणाम
इन समाधानों को लागू करने के बाद, प्रोग्राम `bad_alloc` या `cudaErrorUnknown` त्रुटियों के बिना चलना चाहिए और इस प्रकार आउटपुट उत्पन्न करना चाहिए:
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

### यदि आपको और त्रुटियाँ मिलती हैं
- `nvcc --version`, `nvidia-smi` के आउटपुट और अपडेट किए गए कोड से किसी भी नई एरर मैसेज को साझा करें।
- विशिष्ट सलाह के लिए अपने GPU मॉडल और CUDA संस्करण को निर्दिष्ट करें।

यदि आपको किसी विशिष्ट चरण में सहायता की आवश्यकता हो तो मुझे बताएं!