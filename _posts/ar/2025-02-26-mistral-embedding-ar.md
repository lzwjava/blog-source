---
audio: false
generated: true
lang: ar
layout: post
title: مستريال AI التضمينات
translated: true
---

لاستخدام أمثلة التضمين باستخدام Mistral AI، يمكنك استغلال API التضمين الخاص بهم لتوليد تمثيلات رقمية (التضمين) للنص التي تسرب المعنى الدلالي. هذه التضمينات مفيدة لمهام مثل اكتشاف التشابه، التجميع، التصنيف، أو البحث. أدناه، سأوضح كيفية توليد التضمينات لمجموعة من الجمل وتحسيل تشابهاتها باستخدام نقطة النهاية التضمين الخاصة بمستريال AI. هذا المثال يبني على بنية الكود المقدم ولكن يغيره بشكل خاص للتضمينات، كما هو موضح في الوثائق: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### المتطلبات الأساسية

قبل تشغيل المثال، تأكد من أن لديك:
1. **مفتاح API**: مفتاح API صالح لمستريال AI محفوظ في المتغير البيئي `MISTRAL_API_KEY`.
2. **التبعيات**: الحزم Python المطلوبة. يمكنك تثبيتها باستخدام:
   ```bash
   pip install requests numpy
   ```

### مثال الكود

هنا هو كود Python الكامل الذي يولد التضمينات لثلاثة جمل وتحسيل تشابهاتها:

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    استدعاء API التضمين لمستريال AI لتوليد التضمينات لمجموعة من النصوص.

    Args:
        texts (list): قائمة من النصوص لتضمينها.
        model (str): نموذج التضمين المستخدم (الافتراضي: "mistral-embed").

    Returns:
        list: قائمة من متجهات التضمين، أو None إذا فشلت الطلب.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("خطأ: لم يتم تعيين المتغير البيئي MISTRAL_API_KEY.")
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
            print(f"خطأ في API التضمين لمستريال: تنسيق الرد غير صالح: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ في API التضمين لمستريال: {e}")
        if e.response:
            print(f"رمز حالة الرد: {e.response.status_code}")
            print(f"محتوى الرد: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    حساب التشابه بين اثنين من التضمينات باستخدام الضرب النقطي.

    Args:
        emb1 (list): متجه التضمين الأول.
        emb2 (list): متجه التضمين الثاني.

    Returns:
        float: درجة التشابه (ضرب نقطي، معادل التشابه الكوسيني للمتجهات المعيارية).
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # أمثلة النصوص لتضمينها
    texts = [
        "أحب البرمجة باستخدام Python.",
        "Python لغة برمجة رائعة.",
        "الطقس مشمس اليوم."
    ]

    # توليد التضمينات
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # طباعة أبعاد التضمين
        print(f"أبعاد التضمين: {len(embeddings[0])}")

        # حساب التشابهات الزوجية
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])

        # عرض النتائج
        print(f"\nنتائج التشابه:")
        print(f"النص 1: '{texts[0]}'")
        print(f"النص 2: '{texts[1]}'")
        print(f"النص 3: '{texts[2]}'")
        print(f"\nتشابه بين النص 1 والنص 2: {sim_12:.4f}")
        print(f"تشابه بين النص 1 والنص 3: {sim_13:.4f}")
        print(f"تشابه بين النص 2 والنص 3: {sim_23:.4f}")
```

### كيفية التشغيل

1. **تعيين مفتاح API**:
   ```bash
   export MISTRAL_API_KEY="your_api_key_here"
   ```

2. **حفظ وإجراء**:
   احفظ الكود (على سبيل المثال، باسم `embedding_example.py`) واجراه:
   ```bash
   python embedding_example.py
   ```

### الناتج المتوقع

في حال نجاح استدعاء API، ستشاهد الناتج مثل هذا (القيم الدقيقة تعتمد على التضمينات المرجعة):
```
أبعاد التضمين: 1024

نتائج التشابه:
النص 1: 'أحب البرمجة باستخدام Python.'
النص 2: 'Python لغة برمجة رائعة.'
النص 3: 'الطقس مشمس اليوم.'

تشابه بين النص 1 والنص 2: 0.9200
تشابه بين النص 1 والنص 3: 0.6500
تشابه بين النص 2 والنص 3: 0.6700
```

### الشرح

- **نقطة النهاية API**: تقوم دالة `call_mistral_embeddings_api` بإرسال طلب POST إلى `https://api.mistral.ai/v1/embeddings`، مرسلة قائمة من النصوص ونموذج `"mistral-embed"`. يرجع API ردًا JSON يحتوي على التضمينات تحت المفتاح `"data"`.

- **التضمينات**: كل تضمين هو متجه ذو أبعاد 1024 (حسب وثائق Mistral)، يمثل المحتوى الدلالي للنص المدخل. يتم تعيير التضمينات إلى عيار 1.

- **حساب التشابه**: نظرًا لأن التضمينات معيارية، فإن الضرب النقطي (`np.dot`) بين اثنين من التضمينات يساوي تشابههما الكوسيني. القيم الأعلى تشير إلى تشابه دلالي أكبر:
  - **النص 1 والنص 2**: كلاهما عن البرمجة باستخدام Python، لذلك يجب أن يكون تشابههما مرتفعًا (على سبيل المثال، ~0.92).
  - **النص 1 والنص 3**: أحدهما عن البرمجة والآخر عن الطقس، لذلك يجب أن يكون تشابههما أقل (على سبيل المثال، ~0.65).
  - **النص 2 والنص 3**: نمط مشابه، تشابه أقل بسبب الاختلاف في الموضوعات.

### حالات استخدام إضافية

يمكن تطبيق التضمينات من Mistral AI على ما يتجاوز اكتشاف التشابه:
- **التجميع**: تجميع النصوص الشبيهة باستخدام خوارزميات مثل K-means (يحتاج إلى `scikit-learn`).
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
  print(kmeans.labels_)
  ```
- **البحث**: تضمين استعلام واكتشاف النص الأكثر تشابهًا:
  ```python
  query = "أخبرني عن Python."
  query_emb = call_mistral_embeddings_api([query])[0]
  similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
  most_similar = texts[np.argmax(similarities)]
  print(f"النص الأكثر تشابهًا: '{most_similar}'")
  ```
- **التصنيف**: استخدام التضمينات كخصائص في نموذج تعلم الآلة.

### ملاحظات

- **النموذج**: النموذج `"mistral-embed"` مخصص للتضمينات. تحقق من [الوثائق](https://docs.mistral.ai/capabilities/embeddings/) للحصول على تحديثات أو نماذج إضافية.
- **التجميع**: يتيح API معالجة عدة نصوص في طلب واحد، مما يحسن الكفاءة.
- **التطبيقات المتقدمة**: للبحث عن التشابه على نطاق واسع، قم بالدمج مع قواعد بيانات المتجهات مثل Faiss أو Milvus.

يقدم هذا المثال مقدمة عملية لاستخدام التضمينات لمستريال AI، قابلة للتكيف مع بنية الكود المقدم من خلال تغيير نقطة النهاية وتنسيق البيانات.