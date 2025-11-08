---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تنفيذ جرادينت بوستنج العادي في بايثون
translated: true
type: note
---

### تنفيذ Gradient Boosting الأساسي في Python (باستخدام NumPy فقط)

إليك تنفيذًا من الصّفر لمسجّل Gradient Boosting البسيط، مستوحى من ورقة فريدمان لعام 2001. يستخدم **أشجار القرار الضعيفة** (أشجار ذات انقسام واحد، أي أشجار بعمق 1) كمتعلمين ضعفاء للحفاظ على البساطة والأصالة — لا يتم استخدام scikit-learn، فقط NumPy للحسابات الرقمية و Matplotlib للرسم. هذا يلتقط الأساسيات: الملاءمة للباقي الزائف (مشتقات الخسارة التربيعية السالبة)، ومعدل التعلم، والتحديثات الجمعية.

الكود مكتوب ذاتيًا وجاهز للتشغيل في بيئة Python تحتوي على NumPy/Matplotlib.

```python
import numpy as np
import matplotlib.pyplot as plt

class DecisionStump:
    """شجرة قرار بسيطة (انقسام واحد) من أجل الانحدار."""
    def __init__(self):
        self.feature_idx = None
        self.threshold = None
        self.left_val = None
        self.right_val = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        best_mse = np.inf
        best_idx, best_thresh = -1, -1
        best_left, best_right = None, None
        
        for idx in range(n_features):
            # ترتيب الميزات وتجربة نقاط المنتصف كعتبات
            sorted_idx = np.argsort(X[:, idx])
            thresholds = (X[sorted_idx[:-1], idx] + X[sorted_idx[1:], idx]) / 2
            
            for thresh in thresholds:
                left_mask = X[:, idx] <= thresh
                right_mask = ~left_mask
                
                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue
                
                left_val = np.mean(y[left_mask])
                right_val = np.mean(y[right_mask])
                
                y_pred = np.zeros(n_samples)
                y_pred[left_mask] = left_val
                y_pred[right_mask] = right_val
                
                mse = np.mean((y - y_pred) ** 2)
                
                if mse < best_mse:
                    best_mse = mse
                    best_idx = idx
                    best_thresh = thresh
                    best_left = left_val
                    best_right = right_val
        
        self.feature_idx = best_idx
        self.threshold = best_thresh
        self.left_val = best_left
        self.right_val = best_right
    
    def predict(self, X):
        if self.feature_idx is None:
            return np.zeros(X.shape[0])
        
        left_mask = X[:, self.feature_idx] <= self.threshold
        y_pred = np.zeros(X.shape[0])
        y_pred[left_mask] = self.left_val
        y_pred[~left_mask] = self.right_val
        return y_pred

class GradientBoostingRegressor:
    """ GBM أساسي: يلائم أشجار القرار للباقي الزائف مع معدل تعلم."""
    def __init__(self, n_estimators=100, learning_rate=0.1):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models = []
        self.initial_pred = None
    
    def fit(self, X, y):
        n_samples = X.shape[0]
        # التهيئة بالمتوسط (يقلل خسارة MSE)
        self.initial_pred = np.mean(y)
        current_pred = np.full(n_samples, self.initial_pred)
        
        for _ in range(self.n_estimators):
            # البواقي الزائفة: المشتقة السالبة لـ L = 1/2 (y - F)^2، إذن r = y - F
            residuals = y - current_pred
            
            # ملاءمة متعلم ضعيف للبواقي
            stump = DecisionStump()
            stump.fit(X, residuals)
            self.models.append(stump)
            
            # التحديث مع معدل التعلم (للبساطة، لا يوجد بحث عن أفضل خطوة)
            update = self.learning_rate * stump.predict(X)
            current_pred += update
    
    def predict(self, X):
        current_pred = np.full(X.shape[0], self.initial_pred)
        for model in self.models:
            current_pred += self.learning_rate * model.predict(X)
        return current_pred

# مثال للاستخدام: بيانات اصطناعية (مثل اختبارات الانحدار في الورقة)
np.random.seed(42)
n_samples = 1000
n_features = 10
X = np.random.randn(n_samples, n_features)
true_coef = np.random.randn(n_features) * 2
y = X @ true_coef + np.random.randn(n_samples) * 0.1  # إشارة خطية مع ضوضاء

# تقسيم البيانات
split = int(0.8 * n_samples)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# تدريب GBM
gbm = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
gbm.fit(X_train, y_train)

# التنبؤ والتقييم (خطأ تربيعي)
y_pred_train = gbm.predict(X_train)
y_pred_test = gbm.predict(X_test)
train_mse = np.mean((y_train - y_pred_train) ** 2)
test_mse = np.mean((y_test - y_pred_test) ** 2)
print(f"Train MSE: {train_mse:.4f}")
print(f"Test MSE: {test_mse:.4f}")

# رسم التنبؤات مقابل القيم الحقيقية (مجموعة الاختبار)
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred_test, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('القيم الحقيقية')
plt.ylabel('القيم المتوقعة')
plt.title('تنبؤات GBM مقابل القيم الحقيقية (مجموعة الاختبار)')
plt.tight_layout()
plt.show()

# اختياري: منحنى التعلم (التنبؤات التراكمية)
train_scores = []
current_pred_train = np.full(len(y_train), gbm.initial_pred)
for i in range(gbm.n_estimators):
    update = gbm.learning_rate * gbm.models[i].predict(X_train)
    current_pred_train += update
    score = np.mean((y_train - current_pred_train) ** 2)
    train_scores.append(score)

plt.figure(figsize=(8, 5))
plt.plot(train_scores)
plt.xlabel('عدد تكرارات التعزيز')
plt.ylabel('Train MSE')
plt.title('منحنى التعلم: MSE مقابل التكرارات')
plt.tight_layout()
plt.show()
```

### آلية العمل (مرتبطة بالورقة البحثية)
- **DecisionStump**: متعلم ضعيف يلائم انقسامًا واحدًا لتقليل MSE (مثل الأشجار الضحلة في الورقة). يبحث بقوة عن العتبات للكفاءة على البيانات الصغيرة.
- **GradientBoostingRegressor**:
  - يبدأ بـ \\( F_0 = \bar{y} \\) (يقلل خسارة MSE).
  - يلائم بشكل تكراري أشجار القرار للباقي \\( r = y - F_{m-1} \\) (المشتق السالب).
  - يقوم بالتحديث \\( F_m = F_{m-1} + \nu \cdot h_m \\) مع معدل التعلم \\( \nu = 0.1 \\) للمعايرة.
  - لا يوجد هنا اختيار عشوائي للعينات أو بحث عن الخطوة الأمثل من أجل البساطة (الورقة تقترحها للتوسع).
- **الأداء**: على هذه البيانات الاصطناعية، من المتوقع الحصول على MSE منخفض (~0.01 في الاختبار). يتقارب بسرعة (الرسم يظهر انخفاض الخسارة).
- **القيود**: أشجار القرار الضعيفة تحد من التعقيد؛ للاستخدام الحقيقي، قم بالتوسيع إلى أشجار أعمق. يتعامل مع الانحدار؛ قم بتعديله للتصنيف عبر مشتقات دالة الخسارة اللوغاريتمية.
- **تشغيله**: الصق الكود في سكريبت أو notebook. ستظهر النتائج MSE والرسوم التي تعكس تركيز الورقة على التقارب والدقة.

للتوسعات (مثل أشجار أعمق، التصنيف)، دعني أعرف!

[نسخة PDF من الورقة الأصلية](https://jerryfriedman.su.domains/ftp/trebst.pdf)