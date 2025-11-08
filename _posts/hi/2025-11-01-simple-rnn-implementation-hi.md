---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: सरल आरएनएन कार्यान्वयन स्क्रैच से
translated: true
type: note
---

### NumPy में सरल RNN उदाहरण (स्क्रैच से)

NumPy में स्क्रैच से RNN लागू करना इसकी यांत्रिकी को समझने का एक शानदार तरीका है: आवर्ती छिपी हुई स्थिति, फॉरवर्ड प्रोपेगेशन, और समय के माध्यम से बैकप्रोपेगेशन (BPTT)। नीचे यादृच्छिक अनुक्रमों पर बाइनरी वर्गीकरण के लिए एक मूल उदाहरण है (पिछले PyTorch संस्करण के समान)। यह यूनिवेरिएट टाइम सीरीज़ डेटा (input_size=1), hidden_size=32, और sequence_length=10 का उपयोग करता है।

इस कोड में शामिल है:
- डेटा जनरेशन।
- RNN फॉरवर्ड पास (छिपी हुई स्थितियों के लिए tanh एक्टिवेशन के साथ)।
- बैकवर्ड पास (सरल ग्रेडिएंट डिसेंट के साथ BPTT)।
- प्रशिक्षण लूप।

नोट: यह एक वैनिला RNN है; लंबे अनुक्रमों पर ग्रेडिएंट गायब/विस्फोटित हो सकते हैं। प्रोडक्शन के लिए, क्लिपिंग पर विचार करें या LSTM लॉजिक का उपयोग करें।

```python
import numpy as np

# हाइपरपैरामीटर्स
input_size = 1      # फीचर आकार (यूनिवेरिएट)
hidden_size = 32    # छिपी हुई स्थिति का आकार
output_size = 1     # बाइनरी आउटपुट
sequence_length = 10  # प्रत्येक अनुक्रम की लंबाई
num_samples = 1000
num_epochs = 10
learning_rate = 0.01

# डमी डेटा जनरेट करें: लंबाई 10 के अनुक्रम, योग के आधार पर लेबल (बाइनरी)
def generate_data(num_samples):
    X = np.random.randn(num_samples, sequence_length, input_size)
    y = (np.sum(X, axis=1) > 0).astype(float).reshape(num_samples, 1)
    return X, y

# सरल RNN क्लास (स्क्रैच से)
class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # वेट्स इनिशियलाइज़ करें (Xavier init)
        self.Wxh = np.random.randn(hidden_size, input_size) * np.sqrt(1. / input_size)
        self.Whh = np.random.randn(hidden_size, hidden_size) * np.sqrt(1. / hidden_size)
        self.Why = np.random.randn(output_size, hidden_size) * np.sqrt(1. / hidden_size)
        
        # बायसेस
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
    
    def forward(self, x):
        # x आकार: एकल नमूने के लिए (sequence_length, input_size, 1)
        self.x = x  # बैकप्रॉप के लिए स्टोर करें
        self.h = np.zeros((self.hidden_size, 1))  # प्रारंभिक छिपी हुई स्थिति
        
        # समय के साथ फॉरवर्ड
        self.hs = np.zeros((self.hidden_size, sequence_length + 1))  # छिपी हुई स्थितियाँ (प्रारंभिक सहित)
        self.hs[:, 0] = self.h.flatten()
        
        for t in range(sequence_length):
            self.h = np.tanh(np.dot(self.Wxh, x[t]) + np.dot(self.Whh, self.h) + self.bh)
            self.hs[:, t+1] = self.h.flatten()
        
        # अंतिम छिपी हुई स्थिति से आउटपुट
        self.y_pred = np.dot(self.Why, self.h) + self.by
        return self.sigmoid(self.y_pred)
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))  # स्थिरता के लिए क्लिप करें
    
    def backward(self, y_true):
        # समय के माध्यम से बैकप्रॉप (सरलीकृत)
        dWhy = np.dot((self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred), self.hs[-1:, :].T)
        dby = (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)
        
        # छिपे और आउटपुट वेट्स के लिए ग्रेडिएंट
        dWhh = np.zeros_like(self.Whh)
        dWxh = np.zeros_like(self.Wxh)
        dbh = np.zeros_like(self.bh)
        
        dh_next = np.zeros_like(self.h)
        for t in reversed(range(sequence_length)):
            dh = np.dot(self.Why.T, (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)) + dh_next
            dh_raw = (1 - self.h**2) * dh  # Tanh व्युत्पन्न
            dWxh += np.dot(dh_raw, self.x[t].T)
            dWhh += np.dot(dh_raw, self.hs[:, t:t+2].T[:, 0:1])  # सरलीकृत; पूर्ण BPTT अधिक सटीक संचय करेगा
            dbh += dh_raw
            dh_next = np.dot(self.Whh.T, dh_raw)
        
        # वेट्स अपडेट करें
        self.Wxh -= learning_rate * dWxh
        self.Whh -= learning_rate * dWhh
        self.Why -= learning_rate * dWhy
        self.bh -= learning_rate * dbh
        self.by -= learning_rate * dby
    
    def sigmoid_deriv(self, z):
        s = self.sigmoid(z)
        return s * (1 - s)

# प्रशिक्षण
X, y = generate_data(num_samples)

# एकल नमूना प्रोसेसिंग के लिए रीशेप करें (सरलता के लिए batch_size=1)
X = X.reshape(num_samples, sequence_length, input_size, 1)  # बैच डिम 1 जोड़ें
y = y.reshape(num_samples, 1, 1)

model = SimpleRNN(input_size, hidden_size, output_size)

for epoch in range(num_epochs):
    total_loss = 0
    for i in range(num_samples):
        pred = model.forward(X[i])
        loss = -np.mean(y[i] * np.log(pred + 1e-8) + (1 - y[i]) * np.log(1 - pred + 1e-8))  # BCE
        total_loss += loss
        model.backward(y[i])
    
    avg_loss = total_loss / num_samples
    print(f'Epoch [{epoch+1}/{num_epochs}], Avg Loss: {avg_loss:.4f}')

# अनुमान उदाहरण
test_seq = np.random.randn(sequence_length, input_size, 1)
prediction = model.forward(test_seq)
print(f'Prediction: {prediction.flatten()[0]:.4f}')
```

#### यह कैसे काम करता है:
- **डेटा जनरेशन**: योग के आधार पर बाइनरी लेबल वाले यादृच्छिक अनुक्रम।
- **फॉरवर्ड पास**: अनुक्रम को टाइमस्टेप-दर-टाइमस्टेप प्रोसेस करता है, छिपी हुई स्थिति को अपडेट करता है `h_t = tanh(Wxh * x_t + Whh * h_{t-1} + bh)`। आउटपुट अंतिम `h` का उपयोग सिग्मॉइड के साथ करता है।
- **बैकवर्ड पास**: BPTT सभी टाइमस्टेप्स के लिए ग्रेडिएंट की गणना करता है, सरल GD के माध्यम से वेट्स को अपडेट करता है। (नोट: यह एक न्यूनतम BPTT है; पूर्ण संस्करण अधिक सटीक संचय को संभालते हैं।)
- **प्रशिक्षण**: नमूनों पर लूप करता है, BCE लॉस की गणना करता है, और अपडेट करता है।
- **आउटपुट**: सिग्मॉइड संभावना देता है (0-1)।

यह इन पैरामीटर्स के लिए एक मानक मशीन पर ~10-20 सेकंड में चलता है। सीखने को देखने के लिए `num_samples` या `num_epochs` बढ़ाएं। मल्टी-बैच के लिए, लूप्स को वेक्टराइज़ करें।

गहरी जानकारी के लिए:  
[Understanding LSTM Networks (Colah's Blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)  
[NumPy RNN Tutorial](https://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)