---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: सरल पाइटॉर्च आरएनएन उदाहरण
translated: true
type: note
---

### PyTorch में सरल RNN उदाहरण

रिकरंट न्यूरल नेटवर्क (RNN) सीक्वेंशियल डेटा जैसे टाइम सीरीज़ या टेक्स्ट को हैंडल करने के लिए बहुत अच्छे होते हैं। यहाँ PyTorch का उपयोग करके सीक्वेंस को वर्गीकृत करने (जैसे, यादृच्छिक सीक्वेंस पर बाइनरी वर्गीकरण) के लिए एक साधारण RNN बनाने का एक बुनियादी उदाहरण दिया गया है। यह मानता है कि आपके पास PyTorch इंस्टॉल है (`import torch` और `import torch.nn as nn`)।

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# हाइपरपैरामीटर्स
input_size = 1      # फीचर साइज़ (जैसे, यूनिवेरिएट टाइम सीरीज़)
hidden_size = 32    # हिडन स्टेट साइज़
output_size = 1     # बाइनरी आउटपुट (क्लासिफिकेशन के लिए सिग्मॉइड)
sequence_length = 10  # प्रत्येक सीक्वेंस की लंबाई
batch_size = 32
num_epochs = 10

# डमी डेटा जनरेट करें: लंबाई 10 के सीक्वेंस, योग के आधार पर लेबल (बाइनरी)
def generate_data(num_samples):
    X = torch.randn(num_samples, sequence_length, input_size)
    y = (torch.sum(X, dim=1) > 0).float().unsqueeze(1)
    return X, y

# सरल RNN मॉडल
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # x आकार: (batch, seq_len, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # प्रारंभिक हिडन स्टेट
        out, _ = self.rnn(x, h0)
        # वर्गीकरण के लिए अंतिम आउटपुट लें
        out = self.fc(out[:, -1, :])  # अंतिम टाइम स्टेप
        return self.sigmoid(out)

# मॉडल, लॉस, ऑप्टिमाइज़र इनिशियलाइज़ करें
model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# ट्रेनिंग लूप
num_samples = 1000
X, y = generate_data(num_samples)
dataset = torch.utils.data.TensorDataset(X, y)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    for batch_X, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# इनफेरेंस उदाहरण
test_seq = torch.randn(1, sequence_length, input_size)
prediction = model(test_seq)
print(f'Prediction: {prediction.item():.4f}')
```

#### यह कैसे काम करता है:
- **डेटा जनरेशन**: लंबाई 10 के यादृच्छिक सीक्वेंस बनाता है जिसमें एक बाइनरी लेबल होता है (1 यदि योग > 0, अन्यथा 0)।
- **मॉडल**: `nn.RNN` (बेसिक RNN सेल) का उपयोग करता है। फॉरवर्ड पास सीक्वेंस को स्टेप-बाय-स्टेप प्रोसेस करता है, आउटपुट के लिए अंतिम हिडन स्टेट का उपयोग करता है।
- **ट्रेनिंग**: बाइनरी वर्गीकरण के लिए BCE लॉस के साथ स्टैंडर्ड PyTorch लूप।
- **आउटपुट**: सिग्मॉइड एक्टिवेशन 0 और 1 के बीच की प्रायिकता देता है।

यह एक वैनिला RNN है; लंबे सीक्वेंस पर बेहतर परफॉर्मेंस के लिए, LSTM या GRU वेरिएंट पर विचार करें (जैसे, `nn.RNN` को `nn.LSTM` से बदलें)।

### LSTM वेरिएंट (त्वरित एक्सटेंशन)
वैनिशिंग ग्रेडिएंट के लिए, LSTM पर स्विच करें:

```python
# मॉडल क्लास में, बदलें:
self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)

# और फॉरवर्ड में:
h0 = torch.zeros(1, x.size(0), self.hidden_size)
c0 = torch.zeros(1, x.size(0), self.hidden_size)  # LSTM को सेल स्टेट की आवश्यकता होती है
out, (hn, cn) = self.rnn(x, (h0, c0))
```

इसे एक्सपेरिमेंट करने के लिए PyTorch एनवायरनमेंट में रन करें!

[PyTorch RNN डॉक्यूमेंटेशन](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)  
[PyTorch LSTM डॉक्यूमेंटेशन](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)