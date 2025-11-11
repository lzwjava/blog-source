---
audio: false
generated: true
lang: hi
layout: post
title: गिटहब एक्शन्स को ट्रिगर करना
translated: true
type: note
---

हाँ, एक GitHub Action दूसरी GitHub Action को ट्रिगर कर सकती है, हालाँकि सीधे तौर पर नहीं। GitHub Actions वर्कफ़्लो आमतौर पर विशिष्ट घटनाओं जैसे पुश, पुल रिक्वेस्ट, या शेड्यूल द्वारा ट्रिगर होते हैं, लेकिन एक वर्कफ़्लो को दूसरे को ट्रिगर करवाने के कई अप्रत्यक्ष तरीके हैं। नीचे प्राथमिक तरीके दिए गए हैं जिनसे यह हासिल किया जा सकता है:

---

### 1. `workflow_dispatch` इवेंट का उपयोग करना
आप GitHub API के माध्यम से `workflow_dispatch` इवेंट का उपयोग करके प्रोग्रामेटिकली एक वर्कफ़्लो को ट्रिगर कर सकते हैं। यह एक वर्कफ़्लो को दूसरे वर्कफ़्लो को शुरू करने की अनुमति देता है जो इस इवेंट को सुनने के लिए कॉन्फ़िगर किया गया है।

- **यह कैसे काम करता है**: पहला वर्कफ़्लो दूसरे वर्कफ़्लो को ट्रिगर करने के लिए एक API कॉल करता है।
- **उदाहरण**:
  ```yaml
  name: Trigger Another Workflow
  on: [push]
  jobs:
    trigger:
      runs-on: ubuntu-latest
      steps:
        - name: Trigger Workflow
          run: |
            curl -X POST \
              -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
              -H "Accept: application/vnd.github.v3+json" \
              https://api.github.com/repos/<owner>/<repo>/actions/workflows/<workflow_id>/dispatches \
              -d '{"ref": "main"}'
  ```
  `<owner>`, `<repo>`, और `<workflow_id>` को अपने रिपॉजिटरी के विवरण और टार्गेट वर्कफ़्लो के ID से बदलें। दूसरे वर्कफ़्लो में इसके कॉन्फ़िगरेशन में `on: [workflow_dispatch]` शामिल होना चाहिए।

---

### 2. Repository Dispatch इवेंट्स का उपयोग करना
एक वर्कफ़्लो GitHub API का उपयोग करके एक कस्टम इवेंट भेज सकता है, जिसे दूसरा वर्कफ़्लो सुन सकता है और उस पर ट्रिगर हो सकता है।

- **यह कैसे काम करता है**: पहला वर्कफ़्लो एक repository dispatch इवेंट GitHub API के माध्यम से भेजता है, और दूसरा वर्कफ़्लो उस इवेंट पर प्रतिक्रिया देता है।
- **उदाहरण**:
  - पहला वर्कफ़्लो (इवेंट भेजता है):
    ```yaml
    name: Send Dispatch Event
    on: [push]
    jobs:
      send-dispatch:
        runs-on: ubuntu-latest
        steps:
          - name: Send Dispatch
            run: |
              curl -X POST \
                -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/<owner>/<repo>/dispatches \
                -d '{"event_type": "custom_event"}'
    ```
  - दूसरा वर्कफ़्लो (इवेंट द्वारा ट्रिगर होता है):
    ```yaml
    name: Triggered by Dispatch
    on:
      repository_dispatch:
        types: [custom_event]
    jobs:
      respond:
        runs-on: ubuntu-latest
        steps:
          - name: Respond to Event
            run: echo "Triggered by custom_event"
    ```

---

### 3. Git इवेंट्स के माध्यम से ट्रिगर करना
एक वर्कफ़्लो Git इवेंट उत्पन्न करके, जैसे कि एक कमिट बनाना या पुल रिक्वेस्ट खोलना, दूसरे वर्कफ़्लो को ट्रिगर कर सकता है, जो उस इवेंट (जैसे `on: [push]`) के लिए सेट किया गया है।

- **यह कैसे काम करता है**: पहला वर्कफ़्लो रिपॉजिटरी को संशोधित करता है (उदाहरण के लिए, एक कमिट पुश करके), जो दूसरे वर्कफ़्लो को ट्रिगर करता है जो उस इवेंट के लिए कॉन्फ़िगर किया गया है।
- **उदाहरण**:
  ```yaml
  name: Create Commit
  on: [push]
  jobs:
    create-commit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout
          uses: actions/checkout@v2
        - name: Create File
          run: echo "New file" > newfile.txt
        - name: Commit and Push
          run: |
            git config user.name "GitHub Action"
            git config user.email "action@github.com"
            git add newfile.txt
            git commit -m "Add new file"
            git push
  ```
  यह किसी अन्य वर्कफ़्लो को ट्रिगर कर सकता है जो `push` इवेंट पर चलने के लिए सेट है।

---

### मुख्य बातें ध्यान में रखें
- **अनुमतियाँ**: API कॉल में उपयोग किया गया GitHub टोकन में वर्कफ़्लो को ट्रिगर करने या dispatch इवेंट भेजने के लिए पर्याप्त अनुमतियाँ होनी चाहिए।
- **दर सीमाएँ**: GitHub की API दर सीमाओं के बारे में जागरूक रहें, विशेष रूप से बार-बार चलने वाले वर्कफ़्लो के लिए।
- **लूप से बचें**: वर्कफ़्लो को एक-दूसरे को अंतहीन रूप से ट्रिगर करने से रोकने के लिए शर्तें जोड़कर अनंत लूप को रोकें।
- **कॉन्फ़िगरेशन**: सुनिश्चित करें कि टार्गेट वर्कफ़्लो इच्छित इवेंट को सुनने के लिए सही ढंग से सेट अप है।

---

### निष्कर्ष
हालाँकि GitHub Actions एक वर्कफ़्लो को दूसरे को सीधे कॉल करने का कोई प्रत्यक्ष तंत्र प्रदान नहीं करता है, आप इसे अप्रत्यक्ष रूप से `workflow_dispatch`, repository dispatch इवेंट्स, या Git इवेंट्स जैसे कमिट या पुल रिक्वेस्ट का उपयोग करके हासिल कर सकते हैं। ये तरीके आपको अपनी आवश्यकताओं के आधार पर वर्कफ़्लो को प्रभावी ढंग से चेन करने या ट्रिगर करने की अनुमति देते हैं।