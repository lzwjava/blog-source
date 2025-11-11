---
audio: false
generated: true
lang: ar
layout: post
title: تضمينات ميسترال للذكاء الاصطناعي
translated: true
type: note
---

لتقديم أمثلة على التضمين باستخدام Mistral AI، يمكنك الاستفادة من واجهة برمجة التطبيقات (API) الخاصة بالتضمين لإنشاء تمثيلات رقمية (تضمينات) للنص تلتقط المعنى الدلالي. هذه التضمينات مفيدة لمهام مثل اكتشاف التشابه، والتجميع، والتصنيف، أو البحث. أدناه، سأوضح كيفية إنشاء تضمينات لمجموعة من الجمل وحساب أوجه التشابه بينها باستخدام نقطة نهاية التضمين في Mistral AI. يبني هذا المثال على هيكل الكود المقدم ولكنه يتكيف خصيصًا للتضمين، كما هو موضح في الوثائق: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### المتطلبات الأساسية

قبل تشغيل المثال، تأكد من:
1.  **مفتاح API**: مفتاح Mistral AI API صالح مخزن في متغير البيئة `MISTRAL_API_KEY`.
2.  **التبعيات**: تثبيت حزم Python المطلوبة. يمكنك تثبيتها باستخدام:
    ```bash
    pip install requests numpy
    ```

### مثال على الكود

إليك سكريبت Python كامل يقوم بإنشاء تضمينات لثلاث جمل ويحسب أوجه التشابه بينها زوجياً:

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    استدعاء Mistral AI embeddings API لإنشاء تضمينات لقائمة من النصوص.
    
    الوسائط:
        texts (list): قائمة السلاسل النصية المطلوب تضمينها.
        model (str): نموذج التضمين المراد استخدامه (الافتراضي: "mistral-embed").
    
    الإرجاع:
        list: قائمة بمتجهات التضمين، أو None في حالة فشل الطلب.
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
    حساب التشابه بين تضمينين باستخدام الضرب النقطي.
    
    الوسائط:
        emb1 (list): متجه التضمين الأول.
        emb2 (list): متجه التضمين الثاني.
    
    الإرجاع:
        float: درجة التشابه (الضرب النقطي، يعادل تشابه جيب التمام للمتجهات الطبيعية).
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # النصوص المثال المراد تضمينها
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]
    
    # إنشاء التضمينات
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # طباعة بُعد التضمين
        print(f"Embedding dimension: {len(embeddings[0])}")
        
        # حساب أوجه التشابه الزوجية
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])
        
        # عرض النتائج
        print(f"\nSimilarity Results:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nSimilarity between Text 1 and Text 2: {sim_12:.4f}")
        print(f"Similarity between Text 1 and Text 3: {sim_13:.4f}")
        print(f"Similarity between Text 2 and Text 3: {sim_23:.4f}")
```

### كيفية التشغيل

1.  **تعيين مفتاح API**:
    ```bash
    export MISTRAL_API_KEY="your_api_key_here"
    ```

2.  **الحفظ والتنفيذ**:
    احفظ السكريبت (مثلاً، كـ `embedding_example.py`) وقم بتشغيله:
    ```bash
    python embedding_example.py
    ```

### الناتج المتوقع

بافتراض نجاح استدعاء API، سترى ناتجاً مشابهاً لهذا (القيم الفعلية تعتمد على التضمينات المُرجعة):
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

### الشرح

-   **نقطة نهاية API**: ترسل الدالة `call_mistral_embeddings_api` طلب POST إلى `https://api.mistral.ai/v1/embeddings`، وتمرر قائمة من النصوص ونموذج `"mistral-embed"`. ترجع API استجابة JSON تحتوي على التضمينات تحت المفتاح `"data"`.

-   **التضمينات**: كل تضمين هو متجه ذو 1024 بُعد (حسب الوثائق الخاصة بـ Mistral)، يمثل المحتوى الدلالي للنص المدخل. يتم تسوية التضمينات إلى القاعدة 1.

-   **حساب التشابه**: نظرًا لأن التضمينات طبيعية، فإن الضرب النقطي (`np.dot`) بين تضمينين يساوي تشابه جيب التمام بينهما. تشير القيم الأعلى إلى تشابه دلالي أكبر:
    -   **النص 1 والنص 2**: كلاهما عن البرمجة باستخدام Python، لذا يجب أن يكون تشابههما مرتفعاً (مثلاً، ~0.92).
    -   **النص 1 والنص 3**: أحدهما عن البرمجة والآخر عن الطقس، لذا يجب أن يكون تشابههما أقل (مثلاً، ~0.65).
    -   **النص 2 والنص 3**: نمط مشابه، تشابه أقل بسبب اختلاف الموضوعات.

### حالات استخدام إضافية

يمكن تطبيق تضمينات Mistral AI beyond اكتشاف التشابه:
-   **التجميع**: تجميع النصوص المتشابهة باستخدام خوارزميات مثل K-means (يتطلب `scikit-learn`).
    ```python
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
    print(kmeans.labels_)
    ```
-   **البحث**: تضمين استعلام وإيجاد النص الأكثر تشابهاً:
    ```python
    query = "Tell me about Python."
    query_emb = call_mistral_embeddings_api([query])[0]
    similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
    most_similar = texts[np.argmax(similarities)]
    print(f"Most similar text: '{most_similar}'")
    ```
-   **التصنيف**: استخدام التضمينات كسمات في نموذج تعلم الآلة.

### ملاحظات

-   **النموذج**: نموذج `"mistral-embed"` مُحسّن للتضمين. تحقق من [الوثائق](https://docs.mistral.ai/capabilities/embeddings/) للحصول على التحديثات أو النماذج الإضافية.
-   **المعالجة الدفعية**: تقوم API بمعالجة نصوص متعددة في استدعاء واحد، مما يحسن الكفاءة.
-   **التطبيقات المتقدمة**: للبحث عن التشابه على نطاق واسع، قم بالدمج مع قواعد بيانات المتجهات مثل Faiss أو Milvus.

يوفر هذا المثال مقدمة عملية لاستخدام تضمينات Mistral AI، قابلة للتكيف مع هيكل كود إكمال المحادثة المقدم عن طريق تغيير نقطة النهاية وتنسيق البيانات.