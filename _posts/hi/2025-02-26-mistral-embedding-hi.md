---
audio: false
generated: true
lang: hi
layout: post
title: मिस्ट्रल एआई एम्बेडिंग्स
translated: true
type: note
---

Mistral AI का उपयोग करके एम्बेडिंग उदाहरण प्रदान करने के लिए, आप उनकी एम्बेडिंग API का लाभ उठा सकते हैं ताकि पाठ का संख्यात्मक प्रतिनिधित्व (एम्बेडिंग) जनरेट किया जा सके जो शब्दार्थ अर्थ को कैप्चर करता है। ये एम्बेडिंग समानता पहचान, क्लस्टरिंग, वर्गीकरण, या खोज जैसे कार्यों के लिए उपयोगी हैं। नीचे, मैं प्रदर्शित करूंगा कि कैसे वाक्यों के एक सेट के लिए एम्बेडिंग जनरेट की जाती है और Mistral AI एम्बेडिंग एंडपॉइंट का उपयोग करके उनकी समानताओं की गणना की जाती है। यह उदाहरण प्रदान किए गए कोड की संरचना पर आधारित है लेकिन इसे विशेष रूप से एम्बेडिंग के लिए अनुकूलित करता है, जैसा कि दस्तावेज़ीकरण में बताया गया है: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### पूर्वापेक्षाएँ

उदाहरण चलाने से पहले, सुनिश्चित करें कि आपके पास है:
1.  **API Key**: `MISTRAL_API_KEY` environment variable में संग्रहीत एक वैध Mistral AI API कुंजी।
2.  **निर्भरताएँ**: आवश्यक Python पैकेज इंस्टॉल किए गए हैं। आप उन्हें निम्न कमांड से इंस्टॉल कर सकते हैं:
    ```bash
    pip install requests numpy
    ```

### उदाहरण कोड

यहाँ एक पूर्ण Python स्क्रिप्ट है जो तीन वाक्यों के लिए एम्बेडिंग जनरेट करती है और उनकी जोड़ीवार समानताओं की गणना करती है:

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    Mistral AI एम्बेडिंग API को कॉल करके पाठों की सूची के लिए एम्बेडिंग जनरेट करें।
    
    Args:
        texts (list): एम्बेड करने के लिए स्ट्रिंग्स की सूची।
        model (str): उपयोग करने के लिए एम्बेडिंग मॉडल (डिफ़ॉल्ट: "mistral-embed")।
    
    Returns:
        list: एम्बेडिंग वैक्टर की सूची, या अनुरोध विफल होने पर None।
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None
    
    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "input": texts
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and "data" in response_json:
            embeddings = [item["embedding"] for item in response_json["data"]]
            return embeddings
        else:
            print(f"Mistral Embeddings API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral Embeddings API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    डॉट उत्पाद का उपयोग करके दो एम्बेडिंग के बीच समानता की गणना करें।
    
    Args:
        emb1 (list): पहला एम्बेडिंग वेक्टर।
        emb2 (list): दूसरा एम्बेडिंग वेक्टर।
    
    Returns:
        float): समानता स्कोर (डॉट उत्पाद, सामान्यीकृत वैक्टर के लिए कोसाइन समानता के बराबर)।
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # एम्बेड करने के लिए उदाहरण पाठ
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]
    
    # एम्बेडिंग जनरेट करें
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # एम्बेडिंग आयाम प्रिंट करें
        print(f"Embedding dimension: {len(embeddings[0])}")
        
        # जोड़ीवार समानताओं की गणना करें
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])
        
        # परिणाम प्रदर्शित करें
        print(f"\nSimilarity Results:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nSimilarity between Text 1 and Text 2: {sim_12:.4f}")
        print(f"Similarity between Text 1 and Text 3: {sim_13:.4f}")
        print(f"Similarity between Text 2 and Text 3: {sim_23:.4f}")
```

### कैसे चलाएं

1.  **API Key सेट करें**:
    ```bash
    export MISTRAL_API_KEY="your_api_key_here"
    ```

2.  **सेव करें और एक्ज़िक्यूट करें**:
    स्क्रिप्ट को सेव करें (उदाहरण के लिए, `embedding_example.py` के रूप में) और इसे रन करें:
    ```bash
    python embedding_example.py
    ```

### अपेक्षित आउटपुट

यह मानते हुए कि API कॉल सफल होती है, आपको कुछ इस तरह का आउटपुट दिखाई देगा (सटीक मान लौटाई गई एम्बेडिंग पर निर्भर करते हैं):
```
Embedding dimension: 1024

Similarity Results:
Text 1: 'I love programming in Python.'
Text 2: 'Python is a great programming language.'
Text 3: 'The weather is sunny today.'

Similarity between Text 1 and Text 2: 0.9200
Similarity between Text 1 and Text 3: 0.6500
Similarity between Text 2 and Text 3: 0.6700
```

### स्पष्टीकरण

-   **API एंडपॉइंट**: `call_mistral_embeddings_api` फ़ंक्शन `https://api.mistral.ai/v1/embeddings` पर एक POST अनुरोध भेजता है, जिसमें पाठों की एक सूची और `"mistral-embed"` मॉडल पास किया जाता है। API `"data"` कुंजी के तहत एम्बेडिंग वाले एक JSON प्रतिक्रिया लौटाता है।

-   **एम्बेडिंग**: प्रत्येक एम्बेडिंग एक 1024-आयामी वेक्टर होता है (Mistral के दस्तावेज़ीकरण के अनुसार), जो इनपुट पाठ की शब्दार्थ सामग्री का प्रतिनिधित्व करता है। एम्बेडिंग को 1 के मानदंड के लिए सामान्यीकृत किया जाता है।

-   **समानता गणना**: चूंकि एम्बेडिंग सामान्यीकृत हैं, इसलिए दो एम्बेडिंग के बीच का डॉट उत्पाद (`np.dot`) उनकी कोसाइन समानता के बराबर होता है। उच्च मान अधिक शब्दार्थ समानता का संकेत देते हैं:
    -   **Text 1 और Text 2**: दोनों Python में प्रोग्रामिंग के बारे में हैं, इसलिए उनकी समानता अधिक होनी चाहिए (उदा. ~0.92)।
    -   **Text 1 और Text 3**: एक प्रोग्रामिंग के बारे में है, दूसरा मौसम के बारे में है, इसलिए उनकी समानता कम होनी चाहिए (उदा. ~0.65)।
    -   **Text 2 और Text 3**: समान पैटर्न, विभिन्न विषयों के कारण कम समानता।

### अतिरिक्त उपयोग के मामले

Mistral AI से एम्बेडिंग का उपयोग समानता पहचान से परे भी किया जा सकता है:
-   **क्लस्टरिंग**: K-means जैसी एल्गोरिदम का उपयोग करके समान पाठों को समूहित करें (`scikit-learn` की आवश्यकता होती है)।
    ```python
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
    print(kmeans.labels_)
    ```
-   **खोज**: एक क्वेरी को एम्बेड करें और सबसे समान पाठ खोजें:
    ```python
    query = "Tell me about Python."
    query_emb = call_mistral_embeddings_api([query])[0]
    similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
    most_similar = texts[np.argmax(similarities)]
    print(f"Most similar text: '{most_similar}'")
    ```
-   **वर्गीकरण**: एक मशीन लर्निंग मॉडल में एम्बेडिंग को फीचर्स के रूप में उपयोग करें।

### नोट्स

-   **मॉडल**: `"mistral-embed"` मॉडल एम्बेडिंग के लिए अनुकूलित है। अपडेट या अतिरिक्त मॉडल के लिए [दस्तावेज़ीकरण](https://docs.mistral.ai/capabilities/embeddings/) जांचें।
-   **बैचिंग**: API एक कॉल में कई पाठों को प्रोसेस करता है, जिससे दक्षता में सुधार होता है।
-   **उन्नत अनुप्रयोग**: बड़े पैमाने पर समानता खोज के लिए, Faiss या Milvus जैसे वेक्टर डेटाबेस के साथ एकीकृत करें।

यह उदाहरण Mistral AI एम्बेडिंग का उपयोग करने का एक व्यावहारिक परिचय प्रदान करता है, जिसे एंडपॉइंट और डेटा फॉर्मेट बदलकर प्रदान किए गए चैट पूर्णता कोड की संरचना के अनुकूल बनाया जा सकता है।