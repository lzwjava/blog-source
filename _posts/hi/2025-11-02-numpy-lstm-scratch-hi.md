---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: NumPy एलएसटीएम कार्यान्वयन
translated: true
type: note
---

यह लॉन्ग शॉर्ट-टर्म मेमोरी (LSTM) नेटवर्क का एक बेसिक इम्प्लीमेंटेशन है, जो सिर्फ NumPy का उपयोग करके बनाया गया है और क्रिस्टोफर ओलाह के ब्लॉग पोस्ट "अंडरस्टैंडिंग LSTM नेटवर्क्स" की अवधारणाओं से प्रेरित है। इसमें कोर गेट्स (फॉरगेट, इनपुट, कैंडिडेट सेल, और आउटपुट) शामिल हैं और यह फॉरवर्ड पास पर केंद्रित है। क्लास एक सिंगल टाइम स्टेप को `forward()` के जरिए और पूरी सीक्वेंस को `forward_sequence()` के जरिए हैंडल करती है।

वेट्स को रैंडमली इनिशियलाइज़ किया गया है (प्रैक्टिस में, बेहतर इनिशियलाइज़ेशन जैसे Xavier/Glorot का उपयोग करें)। यहां कोई बैकवर्ड पास या ट्रेनिंग शामिल नहीं है—उसके लिए बैकप्रोपागेशन थ्रू टाइम (BPTT) के साथ एक्सटेंड करें।

```python
import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # Initialize weights and biases for forget, input, cell, and output gates
        self.Wf = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wi = np.random.randn(hidden_size, hidden_size + input_size)
        self.WC = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wo = np.random.randn(hidden_size, hidden_size + input_size)
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bC = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def tanh(self, z):
        return np.tanh(z)

    def forward(self, x, h_prev, C_prev):
        # x: (input_size, 1), h_prev and C_prev: (hidden_size, 1)
        # Concatenate hidden state and input
        concat = np.vstack((h_prev, x))
        # Forget gate
        f_t = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        # Input gate
        i_t = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        C_tilda = self.tanh(np.dot(self.WC, concat) + self.bC)
        # Cell state update
        C_t = f_t * C_prev + i_t * C_tilda
        # Output gate
        o_t = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        # Hidden state update
        h_t = o_t * self.tanh(C_t)
        return h_t, C_t

    def forward_sequence(self, X):
        # X: (seq_len, input_size)
        h = np.zeros((self.hidden_size, 1))
        C = np.zeros((self.hidden_size, 1))
        outputs = []
        for x in X:
            h, C = self.forward(x.reshape(-1, 1), h, C)
            outputs.append(h)
        return np.hstack(outputs).T  # Returns (seq_len, hidden_size)

# Example usage
input_size = 3
hidden_size = 5
lstm = LSTM(input_size, hidden_size)

# Single step
x_t = np.random.randn(input_size, 1)
h_prev = np.zeros((hidden_size, 1))
C_prev = np.zeros((hidden_size, 1))
h_t, C_t = lstm.forward(x_t, h_prev, C_prev)
print("Single step - Hidden state shape:", h_t.shape)

# Sequence
X = np.random.randn(4, input_size)  # seq_len=4
outputs = lstm.forward_sequence(X)
print("Sequence outputs shape:", outputs.shape)
```

### क्विक एक्सप्लेनेशन
- **इनिशियलाइज़ेशन**: वेट्स कॉन्कैटीनेटेड इनपुट (पिछली हिडन स्टेट + करंट इनपुट) को हर गेट से कनेक्ट करते हैं। बायसेज को जीरो-इनिशियलाइज़ किया गया है।
- **गेट्स**:
  - **फॉरगेट गेट** (`f_t`): तय करता है कि पिछली सेल स्टेट से क्या भूलना है (सिग्मॉइड: 0-1)।
  - **इनपुट गेट** (`i_t`) और **कैंडिडेट सेल** (`C_tilda`): तय करते हैं कि कौन सी नई जानकारी जोड़नी है (सिग्मॉइड + टैनह)।
  - **आउटपुट गेट** (`o_t`): हिडन स्टेट प्रोड्यूस करने के लिए सेल स्टेट को फिल्टर करता है (सेल पर सिग्मॉइड + टैनह)।
- **सेल स्टेट** (`C_t`): लॉन्ग-टर्म मेमोरी के लिए एडिटिव अपडेट्स के साथ लीनियर फ्लो।
- **यूसेज**: सीक्वेंस के लिए, टाइम स्टेप्स के जरिए लूप करें, हिडन और सेल स्टेट्स को प्रोग्रेसिवली अपडेट करते हुए।

यह कोलाह के ब्लॉग से LSTM आर्किटेक्चर से मेल खाता है: सेल स्टेट एक "हाईवे" के रूप में जो गेट्स द्वारा कंट्रोल होती है।

[Understanding LSTMs: Implementation from Scratch](https://medium.com/@samina.amin/understanding-lstms-lstm-implementation-from-scratch-18965a150eca)