---
audio: false
generated: false
lang: hi
layout: post
title: मिस्ट्राल एआई एम्बेडिंग्स
translated: true
---

Mistral AI का उपयोग करके embedding उदाहरण प्रदान करने के लिए, आप उनके embeddings API का उपयोग कर सकते हैं ताकि पाठों के सांख्यिकीय प्रतिनिधित्व (embeddings) को उत्पन्न कर सकें जो अर्थपूर्ण अर्थ को पकड़ते हैं। ये embeddings समानता का पता लगाने, क्लस्टरिंग, वर्गीकरण या खोज जैसे कार्य के लिए उपयोगी हैं। नीचे, मैं Mistral AI embeddings endpoint का उपयोग करके एक वाक्य समूह के लिए embeddings उत्पन्न करने और उनके समानताओं को गणना करने का एक उदाहरण दिखाऊंगा। यह उदाहरण प्रदान की गई कोड संरचना पर आधारित है, लेकिन इसे विशेष रूप से embeddings के लिए अनुकूलित किया गया है, जैसा कि दस्तावेज में वर्णित है: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### पूर्वापेक्षाएँ

उदाहरण चलाने से पहले, सुनिश्चित करें कि आपके पास हैं:
1. **API Key**: एक वैध Mistral AI API key जो `MISTRAL_API_KEY` पर्यावरण चर में संग्रहीत है।
2. **Dependencies**: आवश्यक Python पैकेज इंस्टॉल किए गए हैं। आप उन्हें इंस्टॉल कर सकते हैं:
   ```bash
   pip install requests numpy
   ```

### उदाहरण कोड

यह एक पूर्ण Python स्क्रिप्ट है जो तीन वाक्यों के लिए embeddings उत्पन्न करता है और उनके जोड़े के समानताओं को गणना करता है:

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    Mistral AI embeddings API को कॉल करने के लिए एक लिस्ट ऑफ टेक्स्ट्स के लिए embeddings उत्पन्न करें।

    Args:
        texts (list): embed करने के लिए स्ट्रिंग्स की लिस्ट.
        model (str): उपयोग करने वाला embeddings model (default: "mistral-embed").

    Returns:
        list: embeddings vectors की लिस्ट, या अगर अनुरोध विफल हो जाता है तो None.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY पर्यावरण चर नहीं सेट है।")
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
    दो embeddings के बीच समानता को डॉट प्रोडक्ट का उपयोग करके गणना करें।

    Args:
        emb1 (list): पहला embeddings vector.
        emb2 (list): दूसरा embeddings vector.

    Returns:
        float: समानता स्कोर (डॉट प्रोडक्ट, जो नॉर्मलाइज़्ड vectors के लिए कोसाइन समानता के समान है).
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # embed करने के लिए उदाहरण टेक्स्ट्स
    texts = [
        "मैं Python में प्रोग्रामिंग करना पसंद करता हूँ।",
        "Python एक महान प्रोग्रामिंग भाषा है।",
        "आज का मौसम सूर्योदय है।"
    ]

    # embeddings उत्पन्न करें
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # embeddings dimension print करें
        print(f"Embedding dimension: {len(embeddings[0])}")

        # जोड़े के समानताओं को गणना करें
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])

        # परिणाम प्रदर्शित करें
        print(f"\nSimilarity Results:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nText 1 और Text 2 के बीच समानता: {sim_12:.4f}")
        print(f"Text 1 और Text 3 के बीच समानता: {sim_13:.4f}")
        print(f"Text 2 और Text 3 के बीच समानता: {sim_23:.4f}")
```

### कैसे चलाएं

1. **API Key सेट करें**:
   ```bash
   export MISTRAL_API_KEY="your_api_key_here"
   ```

2. **सहेजें और चलाएं**:
   स्क्रिप्ट को (उदाहरण के लिए, `embedding_example.py` के रूप में) सहेजें और इसे चलाएं:
   ```bash
   python embedding_example.py
   ```

### अपेक्षित आउटपुट

अगर API कॉल सफल हो जाता है, तो आप इस तरह के आउटपुट देखेंगे (सटीक मान embeddings के द्वारा लौटाए गए पर निर्भर करते हैं):
```
Embedding dimension: 1024

Similarity Results:
Text 1: 'मैं Python में प्रोग्रामिंग करना पसंद करता हूँ।'
Text 2: 'Python एक महान प्रोग्रामिंग भाषा है।'
Text 3: 'आज का मौसम सूर्योदय है।'

Text 1 और Text 2 के बीच समानता: 0.9200
Text 1 और Text 3 के बीच समानता: 0.6500
Text 2 और Text 3 के बीच समानता: 0.6700
```

### व्याख्या

- **API Endpoint**: `call_mistral_embeddings_api` function एक POST request `https://api.mistral.ai/v1/embeddings` पर भेजता है, एक टेक्स्ट्स की लिस्ट और `"mistral-embed"` model को पास करता है। API एक JSON response लौटाता है जिसमें embeddings `"data"` key के नीचे होते हैं।

- **Embeddings**: प्रत्येक embedding एक 1024-आयामी vector है (Mistral के दस्तावेज के अनुसार), जो input text के अर्थपूर्ण सामग्री का प्रतिनिधित्व करता है। embeddings को 1 के norm पर नॉर्मलाइज़ किया जाता है।

- **Similarity Calculation**: क्योंकि embeddings नॉर्मलाइज़ किए गए हैं, दो embeddings के बीच डॉट product (`np.dot`) उनके कोसाइन समानता के बराबर होता है। उच्च मान अधिक अर्थपूर्ण समानता को दर्शाते हैं:
  - **Text 1 और Text 2**: दोनों Python में प्रोग्रामिंग के बारे में हैं, इसलिए उनकी समानता उच्च होनी चाहिए (उदाहरण के लिए, ~0.92).
  - **Text 1 और Text 3**: एक प्रोग्रामिंग के बारे में है, दूसरा मौसम के बारे में, इसलिए उनकी समानता कम होनी चाहिए (उदाहरण के लिए, ~0.65).
  - **Text 2 और Text 3**: समान पैटर्न, कम समानता अलग विषयों के कारण।

### अतिरिक्त उपयोग मामले

Mistral AI embeddings को समानता का पता लगाने से परे लागू किया जा सकता है:
- **Clustering**: समान टेक्स्ट्स को K-means जैसे एल्गोरिथम का उपयोग करके समूहित करें (जिसे `scikit-learn` की आवश्यकता होती है).
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
  print(kmeans.labels_)
  ```
- **Search**: एक query embed करें और सबसे समान टेक्स्ट खोजें:
  ```python
  query = "Python के बारे में मुझे बताएं।"
  query_emb = call_mistral_embeddings_api([query])[0]
  similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
  most_similar = texts[np.argmax(similarities)]
  print(f"सबसे समान टेक्स्ट: '{most_similar}'")
  ```
- **Classification**: embeddings को एक मशीन लर्निंग model में features के रूप में उपयोग करें।

### नोट्स

- **Model**: `"mistral-embed"` model embeddings के लिए ऑप्टिमाइज़ किया गया है। दस्तावेज में अपडेट या अतिरिक्त models के लिए जांच करें [documentation](https://docs.mistral.ai/capabilities/embeddings/).
- **Batching**: API एक ही कॉल में कई टेक्स्ट्स को प्रोसेस करता है, जो दक्षता को बढ़ाता है।
- **उन्नत अनुप्रयोग**: बड़े पैमाने पर समानता खोज के लिए Faiss या Milvus जैसे vector databases के साथ एकीकृत करें।

यह उदाहरण Mistral AI embeddings का उपयोग करने का एक व्यावहारिक परिचय प्रदान करता है, जो प्रदान की गई चैट समापन कोड की संरचना को बदलकर endpoint और data format को अनुकूलित कर सकता है।