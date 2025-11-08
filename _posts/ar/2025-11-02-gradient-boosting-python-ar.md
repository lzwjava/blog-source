---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مثال أساسي للتعزيز المتدرج في بايثون
translated: true
type: note
---

### مثال بسيط على تعزيز التدرج (Gradient Boosting) في بايثون

إليك مثالًا أساسيًا باستخدام `GradientBoostingRegressor` من scikit-learn لتطبيق آلة تعزيز التدرج لفريدمان على مجموعة بيانات انحدار مصغرة. هذا يعكس الأفكار الأساسية من الورقة البحثية لعام 2001: التركيب المتسلسل للأشجار للباقي المزيف (pseudo-residuals)، مع التقلص (shrinkage) لتنظيم النموذج.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# الخطوة 1: توليد بيانات اصطناعية (مشابهة لأمثلة الانحدار في الورقة البحثية)
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# الخطوة 2: تهيئة وتدريب نموذج GBM
# المعلمات الرئيسية مستوحاة من الورقة: n_estimators=1000 (تكريرات عديدة)، learning_rate=0.1 (تقلص)،
# max_depth=3 (أشجار ضحلة للمتعلمين الضعفاء)، subsample=0.5 (النموذج العشوائي)
gbm = GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.5,
    random_state=42
)
gbm.fit(X_train, y_train)

# الخطوة 3: التنبؤ والتقييم
y_pred = gbm.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Test MSE: {mse:.4f}")

# الخطوة 4: رسم أهمية الميزات (من قسم قابلية التفسير في الورقة)
importances = gbm.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8, 5))
plt.title("أهمية الميزات")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), [f'الميزة {i}' for i in indices], rotation=45)
plt.tight_layout()
plt.show()

# اختياري: رسم منحنى التعلم (الخسارة مقابل عدد التكرارات)
test_score = np.zeros((gbm.n_estimators,), dtype=np.float64)
for i, y_pred in enumerate(gbm.staged_predict(X_test)):
    test_score[i] = gbm.loss_(y_test, y_pred)
plt.figure(figsize=(8, 5))
plt.title("الانحراف (الخسارة) مقابل عدد تكرارات التعزيز")
plt.plot(test_score, label="انحراف بيانات الاختبار")
plt.xlabel("عدد التكرارات")
plt.ylabel("الانحراف")
plt.legend()
plt.show()
```

### آلية العمل (مرتبطة بالورقة البحثية)
- **البيانات**: بيانات انحدار اصطناعية مع ضوضاء، مشابهة للاختبارات التجريبية في الورقة.
- **النموذج**: يستخدم خسارة المربعات الصغرى افتراضيًا، حيث يلائم الأشجار للتدرجات السالبة (البواقي).
- **التدريب**: الإضافة المتسلسلة للأشجار مع التقلص (`learning_rate=0.1`) لمنع الإفراط في التلائم، كما هو موصى به.
- **التقييم**: MSE يتوافق مع تركيز الورقة على خطأ المربعات؛ تُظهر الرسوم البيانية التقارب والأهمية (إجمالي تقليل الشوائب).
- **تشغيل الكود**: انسخ والصق في دفتر Jupyter أو نص برمجي بايثون. يتطلب `scikit-learn` و `matplotlib`.

هذه نقطة بداية عملية — تنفيذ scikit-learn يتبع خوارزمية فريدمان عن كثب. إذا كنت تريد نسخة مُنشأة من الصفر، فأعلمني!

[وثائق تعزيز التدرج في scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)