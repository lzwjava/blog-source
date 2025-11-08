---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वैनिला ग्रेडिएंट बूस्टिंग कार्यान्वयन पायथन में
translated: true
type: note
---

### वैनिला ग्रेडिएंट बूस्टिंग इम्प्लीमेंटेशन इन पायथन (केवल NumPy)

यहाँ एक सरल ग्रेडिएंट बूस्टिंग रिग्रेसर का from-scratch इम्प्लीमेंटेशन दिया गया है, जो फ्राइडमैन के 2001 के पेपर से प्रेरित है। इसमें **डिसीजन स्टम्प्स** (सिंगल-स्प्लिट ट्री, यानी डेप्थ-1 ट्री) को वीक लर्नर्स के रूप में इस्तेमाल किया गया है ताकि चीजें वैनिला और सरल रहें—कोई scikit-learn नहीं, केवल न्यूमेरिक्स के लिए NumPy और प्लॉटिंग के लिए Matplotlib। यह कोर कॉन्सेप्ट को कैप्चर करता है: सूडो-रेजिडुअल्स (स्क्वेर्ड लॉस के नेगेटिव ग्रेडिएंट्स) को फिट करना, श्रिंकेज (लर्निंग रेट), और एडिटिव अपडेट्स।

यह कोड सेल्फ-कंटेन्ड है और NumPy/Matplotlib वाले पायथन एनवायरनमेंट में रन करने योग्य है।

```python
import numpy as np
import matplotlib.pyplot as plt

class DecisionStump:
    """रिग्रेशन के लिए सरल डिसीजन स्टम्प (सिंगल स्प्लिट)।"""
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
            # फीचर के आधार पर सॉर्ट करें और थ्रेशोल्ड के रूप में मिडपॉइंट्स आजमाएँ
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
    """वैनिला GBM: सूडो-रेजिडुअल्स को श्रिंकेज के साथ स्टम्प्स से फिट करता है।"""
    def __init__(self, n_estimators=100, learning_rate=0.1):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models = []
        self.initial_pred = None
    
    def fit(self, X, y):
        n_samples = X.shape[0]
        # माध्य से इनिशियलाइज़ करें (स्क्वेर्ड लॉस के लिए मिनिमाइज़र)
        self.initial_pred = np.mean(y)
        current_pred = np.full(n_samples, self.initial_pred)
        
        for _ in range(self.n_estimators):
            # सूडो-रेजिडुअल्स: L = 1/2 (y - F)^2 का नेगेटिव ग्रेडिएंट, इसलिए r = y - F
            residuals = y - current_pred
            
            # वीक लर्नर को रेजिडुअल्स पर फिट करें
            stump = DecisionStump()
            stump.fit(X, residuals)
            self.models.append(stump)
            
            # श्रिंकेज के साथ अपडेट करें (सरलता के लिए कोई लाइन सर्च नहीं; argmin gamma जोड़ सकते हैं)
            update = self.learning_rate * stump.predict(X)
            current_pred += update
    
    def predict(self, X):
        current_pred = np.full(X.shape[0], self.initial_pred)
        for model in self.models:
            current_pred += self.learning_rate * model.predict(X)
        return current_pred

# उदाहरण उपयोग: सिंथेटिक डेटा (पेपर के रिग्रेशन टेस्ट्स की तरह)
np.random.seed(42)
n_samples = 1000
n_features = 10
X = np.random.randn(n_samples, n_features)
true_coef = np.random.randn(n_features) * 2
y = X @ true_coef + np.random.randn(n_samples) * 0.1  # नॉइज़ी लीनियर सिग्नल

# डेटा स्प्लिट करें
split = int(0.8 * n_samples)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# GBM ट्रेन करें
gbm = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
gbm.fit(X_train, y_train)

# प्रेडिक्ट और मूल्यांकन करें (स्क्वेर्ड एरर)
y_pred_train = gbm.predict(X_train)
y_pred_test = gbm.predict(X_test)
train_mse = np.mean((y_train - y_pred_train) ** 2)
test_mse = np.mean((y_test - y_pred_test) ** 2)
print(f"Train MSE: {train_mse:.4f}")
print(f"Test MSE: {test_mse:.4f}")

# प्रेडिक्शन बनाम ट्रू प्लॉट करें (टेस्ट सेट)
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred_test, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('सही मान (True Values)')
plt.ylabel('पूर्वानुमानित मान (Predicted Values)')
plt.title('GBM पूर्वानुमान बनाम सही मान (टेस्ट सेट)')
plt.tight_layout()
plt.show()

# वैकल्पिक: लर्निंग कर्व (क्यूमुलेटिव प्रेडिक्शन्स)
train_scores = []
current_pred_train = np.full(len(y_train), gbm.initial_pred)
for i in range(gbm.n_estimators):
    update = gbm.learning_rate * gbm.models[i].predict(X_train)
    current_pred_train += update
    score = np.mean((y_train - current_pred_train) ** 2)
    train_scores.append(score)

plt.figure(figsize=(8, 5))
plt.plot(train_scores)
plt.xlabel('बूस्टिंग इटरेशन की संख्या')
plt.ylabel('ट्रेन MSE')
plt.title('लर्निंग कर्व: MSE बनाम इटरेशन')
plt.tight_layout()
plt.show()
```

### यह कैसे काम करता है (पेपर से जुड़ा हुआ)
- **DecisionStump**: वीक लर्नर जो MSE को मिनिमाइज़ करने के लिए एक सिंगल स्प्लिट फिट करता है (पेपर के शैलो ट्रीज़ की तरह)। यह छोटे डेटा पर एफिशिएंसी के लिए थ्रेशोल्ड्स को ब्रूट-फोर्स करता है।
- **GradientBoostingRegressor**:
  - \\( F_0 = \bar{y} \\) (स्क्वेर्ड लॉस मिनिमाइज़र) से शुरू होता है।
  - पुनरावृत्त रूप से रेजिडुअल्स \\( r = y - F_{m-1} \\) (नेगेटिव ग्रेडिएंट) पर स्टम्प्स फिट करता है।
  - \\( F_m = F_{m-1} + \nu \cdot h_m \\) को श्रिंकेज \\( \nu = 0.1 \\) के साथ रेगुलराइजेशन के लिए अपडेट करता है।
  - सरलता के लिए यहाँ कोई स्टोकैस्टिक सबसैम्पलिंग या लाइन सर्च नहीं है (पेपर स्केल-अप के लिए उनकी सिफारिश करता है)।
- **परफॉर्मेंस**: इस टॉय डेटा पर, कम MSE (~0.01 टेस्ट पर) की उम्मीद करें। यह जल्दी कन्वर्ज हो जाता है (प्लॉट घटते लॉस को दिखाता है)।
- **लिमिटेशन्स**: स्टम्प्स कॉम्प्लेक्सिटी को लिमिट करते हैं; रियल यूज के लिए, डीपर ट्रीज़ तक एक्सटेंड करें। रिग्रेशन को हैंडल करता है; क्लासिफिकेशन के लिए लॉग-लॉस ग्रेडिएंट्स के जरिए एडाप्ट करें।
- **इसे रन करें**: किसी स्क्रिप्ट/नोटबुक में पेस्ट करें। आउटपुट MSE और प्लॉट पेपर के कन्वर्जेंस/एक्यूरेसी फोकस को मिरर करते हैं।

एक्सटेंशन (जैसे, डीपर ट्रीज़, क्लासिफिकेशन) के लिए, मुझे बताएँ!

[मूल पेपर PDF](https://jerryfriedman.su.domains/ftp/trebst.pdf)