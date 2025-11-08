---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: पायथन में बुनियादी ग्रेडिएंट बूस्टिंग उदाहरण
translated: true
type: note
---

### पायथन में सरल ग्रेडिएंट बूस्टिंग उदाहरण

यहाँ scikit-learn के `GradientBoostingRegressor` का उपयोग करके एक खिलौना रिग्रेशन डेटासेट पर फ्राइडमैन के ग्रेडिएंट बूस्टिंग मशीन को लागू करने का एक मूल उदाहरण दिया गया है। यह 2001 के पेपर के मुख्य विचारों को दर्शाता है: छद्म-अवशेषों पर पेड़ों का क्रमिक फिटिंग, नियमितीकरण के लिए सिकुड़न के साथ।

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# चरण 1: सिंथेटिक डेटा जनरेट करें (पेपर में रिग्रेशन उदाहरणों की तरह)
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# चरण 2: GBM को इनिशियलाइज़ और ट्रेन करें
# पेपर से प्रेरित मुख्य पैरामीटर: n_estimators=1000 (कई पुनरावृत्तियाँ), learning_rate=0.1 (सिकुड़न),
# max_depth=3 (कमजोर लर्नर के लिए उथले पेड़), subsample=0.5 (स्टोकेस्टिक वेरिएंट)
gbm = GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.5,
    random_state=42
)
gbm.fit(X_train, y_train)

# चरण 3: भविष्यवाणी करें और मूल्यांकन करें
y_pred = gbm.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"टेस्ट MSE: {mse:.4f}")

# चरण 4: फीचर महत्व प्लॉट करें (पेपर के व्याख्यात्मकता अनुभाग से)
importances = gbm.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8, 5))
plt.title("फीचर महत्व")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), [f'फीचर {i}' for i in indices], rotation=45)
plt.tight_layout()
plt.show()

# वैकल्पिक: लर्निंग कर्व प्लॉट करें (लॉस बनाम पुनरावृत्तियाँ)
test_score = np.zeros((gbm.n_estimators,), dtype=np.float64)
for i, y_pred in enumerate(gbm.staged_predict(X_test)):
    test_score[i] = gbm.loss_(y_test, y_pred)
plt.figure(figsize=(8, 5))
plt.title("डेविएंस (लॉस) बनाम बूस्टिंग पुनरावृत्तियों की संख्या")
plt.plot(test_score, label="टेस्ट डेविएंस")
plt.xlabel("पुनरावृत्तियों की संख्या")
plt.ylabel("डेविएंस")
plt.legend()
plt.show()
```

### यह कैसे काम करता है (पेपर से जुड़ा हुआ)
- **डेटा**: सिंथेटिक रिग्रेशन डेटा शोर के साथ, पेपर के अनुभवजन्य परीक्षणों के समान।
- **मॉडल**: डिफ़ॉल्ट रूप से लीस्ट-स्क्वेयर्स लॉस का उपयोग करता है, नकारात्मक ग्रेडिएंट (अवशेषों) पर पेड़ों को फिट करता है।
- **ट्रेनिंग**: ओवरफिटिंग को रोकने के लिए सिकुड़न (`learning_rate=0.1`) के साथ पेड़ों का क्रमिक जोड़, जैसा कि सिफारिश की गई है।
- **मूल्यांकन**: MSE पेपर के स्क्वेर्ड एरर फोकस से मेल खाता है; प्लॉट अभिसरण और महत्व (कुल अशुद्धि में कमी) दिखाते हैं।
- **इसे चलाएँ**: इसे Jupyter नोटबुक या Python स्क्रिप्ट में कॉपी-पेस्ट करें। इसके लिए `scikit-learn` और `matplotlib` की आवश्यकता होती है।

यह एक व्यावहारिक शुरुआती बिंदु है—scikit-learn का कार्यान्वयन फ्राइडमैन के एल्गोरिदम का बारीकी से पालन करता है। स्क्रैच से वर्जन के लिए, मुझे बताएं!

[scikit-learn Gradient Boosting Docs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)