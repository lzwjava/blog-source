---
audio: false
generated: true
lang: hi
layout: post
title: ऐतिहासिक डेटा और एलएसटीएम का संयोजन
translated: true
type: note
---

TigerOpen API से ऐतिहासिक स्टॉक डेटा को LSTM मॉडल के साथ विश्लेषण के लिए जोड़ना संभव है और यह वित्तीय टाइम सीरीज भविष्यवाणी में एक सामान्य तरीका है। दूसरी स्क्रिप्ट ऐतिहासिक स्टॉक डेटा (जैसे, OHLCV बार) प्राप्त करती है, जिसका उपयोग पहली स्क्रिप्ट में मौजूद LSTM मॉडल के समान प्रशिक्षण के लिए एक डेटासेट बनाने में किया जा सकता है। नीचे, मैं बताता हूं कि आप इन दोनों को कैसे एकीकृत कर सकते हैं, संभावित चुनौतियों का समाधान कर सकते हैं, और LSTM का उपयोग करके स्टॉक डेटा का विश्लेषण करने के लिए एक उच्च-स्तरीय दृष्टिकोण प्रदान करते हैं।

### दोनों को जोड़ने के लिए उच्च-स्तरीय दृष्टिकोण

1.  **ऐतिहासिक डेटा प्राप्त करें**:
    - दूसरी स्क्रिप्ट से `get_history_data` फ़ंक्शन का उपयोग ऐतिहासिक स्टॉक डेटा (जैसे, प्रतीक '00700' या अन्य के लिए) प्राप्त करने के लिए करें।
    - डेटा में ओपन, हाई, लो, क्लोज प्राइस, वॉल्यूम और टाइमस्टैम्प शामिल हैं, जिनका उपयोग LSTM के लिए फीचर्स के रूप में किया जा सकता है।

2.  **LSTM के लिए डेटा प्रीप्रोसेस करें**:
    - ऐतिहासिक डेटा को LSTM मॉडल के लिए उपयुक्त फॉर्मेट में बदलें। इसमें शामिल है:
        - डेटा को सामान्य करना (जैसे, कीमतों और वॉल्यूम को [0, 1] तक स्केल करना)।
        - ऐतिहासिक डेटा के अनुक्रम बनाना (जैसे, अगले दिन की क्लोजिंग कीमत की भविष्यवाणी करने के लिए पिछले 60 दिनों का उपयोग करना)।
        - फीचर्स (जैसे, क्लोज प्राइस, वॉल्यूम) को LSTM इनपुट के अनुकूल टेंसर फॉर्मेट में एनकोड करना।

3.  **LSTM मॉडल को एडाप्ट करें**:
    - पहली स्क्रिप्ट से `Net` क्लास को संशोधित करें ताकि यह टेक्स्ट अनुक्रमों के बजाय वित्तीय टाइम सीरीज डेटा को हैंडल कर सके।
    - इनपुट आकार को फीचर्स की संख्या (जैसे, क्लोज प्राइस, वॉल्यूम, आदि) से मेल खाने के लिए समायोजित करें, `vocab_size` के बजाय।
    - आउटपुट लेयर को एक सतत मान (जैसे, अगले दिन की क्लोजिंग कीमत) या एक वर्गीकरण (जैसे, कीमत में वृद्धि/कमी) की भविष्यवाणी करने के लिए अपडेट करें।

4.  **मॉडल को ट्रेन करें**:
    - ऐतिहासिक डेटा को ट्रेनिंग, वैलिडेशन और टेस्ट सेट में विभाजित करें।
    - पहली स्क्रिप्ट में ट्रेनिंग लूप के समान, प्रीप्रोसेस्ड डेटा का उपयोग करके LSTM को प्रशिक्षित करें।
    - रिग्रेशन कार्यों के लिए मीन स्क्वेर्ड एरर (MSE) या क्लासिफिकेशन के लिए क्रॉस-एन्ट्रॉपी लॉस जैसे लॉस फ़ंक्शन का उपयोग करें।

5.  **विश्लेषण और भविष्यवाणी करें**:
    - हाल के ऐतिहासिक डेटा के आधार पर भविष्य की स्टॉक कीमतों या रुझानों की भविष्यवाणी करने के लिए प्रशिक्षित LSTM का उपयोग करें।
    - `matplotlib` का उपयोग करके वास्तविक डेटा के साथ भविष्यवाणियों को विज़ुअलाइज़ करें।

6.  **ट्रेडिंग के साथ एकीकृत करें**:
    - `place_order` फ़ंक्शन में ट्रेडिंग निर्णयों को सूचित करने के लिए भविष्यवाणियों का उपयोग करें।
    - उदाहरण के लिए, यदि LMSO एक निश्चित सीमा से अधिक कीमत वृद्धि की भविष्यवाणी करता है तो बाय ऑर्डर दें।

### कोड उदाहरण: ऐतिहासिक डेटा को LSTM के साथ जोड़ना

नीचे एक नमूना कोड स्निपेट है जो दोनों स्क्रिप्ट को एकीकृत करती है, जो स्टॉक प्राइस प्रिडिक्शन के लिए ऐतिहासिक डेटा को प्रीप्रोसेस करने और LSTM को एडाप्ट करने पर केंद्रित है।

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tigeropen.common.consts import Language, Market, BarPeriod, QuoteRight
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.util.signature_utils import read_private_key
import os
from datetime import datetime

# --- TigerOpen API सेटअप ---
def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config

def get_history_data(symbol='00700', period=BarPeriod.DAY, begin_time='2024-01-01', end_time=None, limit=100):
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    if not end_time:
        end_time = datetime.now().strftime('%Y-%m-%d')
    bars_dict = quote_client.get_bars(
        symbols=[symbol], period=period, begin_time=begin_time, end_time=end_time, limit=limit, right=QuoteRight.BR
    )
    bars = bars_dict.get(symbol, [])
    return pd.DataFrame([{
        'time': bar.time,
        'open': bar.open,
        'high': bar.high,
        'low': bar.low,
        'close': bar.close,
        'volume': bar.volume
    } for bar in bars])

# --- LSTM मॉडल ---
class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=50, num_layers=1):
        super(StockLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, bidirectional=False)
        self.l_out = nn.Linear(in_features=hidden_size, out_features=1)  # अगली क्लोज प्राइस की भविष्यवाणी करें

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x[:, -1, :]  # अंतिम टाइम स्टेप लें
        x = self.l_out(x)
        return x

# --- डेटा प्रीप्रोसेसिंग ---
def prepare_data(df, sequence_length=60, target_col='close'):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[target_col]].values)
    
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])
    
    X = np.array(X)
    y = np.array(y)
    
    # ट्रेन और टेस्ट में विभाजित करें
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return torch.Tensor(X_train), torch.Tensor(y_train), torch.Tensor(X_test), torch.Tensor(y_test), scaler

# --- ट्रेनिंग लूप ---
def train_model(model, X_train, y_train, X_test, y_test, num_epochs=50, lr=3e-4):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    training_loss, validation_loss = [], []
    
    for epoch in range(num_epochs):
        model.train()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        training_loss.append(loss.item())
        
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_test)
            val_loss = criterion(val_outputs, y_test)
            validation_loss.append(val_loss.item())
        
        if epoch % 5 == 0:
            print(f'Epoch {epoch}, Training Loss: {training_loss[-1]:.4f}, Validation Loss: {validation_loss[-1]:.4f}')
    
    return training_loss, validation_loss

# --- मुख्य एक्सेक्यूशन ---
if __name__ == '__main__':
    # ऐतिहासिक डेटा प्राप्त करें
    df = get_history_data(symbol='00700', limit=1000)
    
    # डेटा तैयार करें
    sequence_length = 60
    X_train, y_train, X_test, y_test, scaler = prepare_data(df, sequence_length=sequence_length, target_col='close')
    
    # LSTM को इनिशियलाइज़ और ट्रेन करें
    model = StockLSTM(input_size=1, hidden_size=50, num_layers=1)
    training_loss, validation_loss = train_model(model, X_train, y_train, X_test, y_test, num_epochs=50)
    
    # ट्रेनिंग और वैलिडेशन लॉस प्लॉट करें
    plt.figure()
    plt.plot(training_loss, 'r', label='Training Loss')
    plt.plot(validation_loss, 'b', label='Validation Loss')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.show()
    
    # भविष्यवाणियां करें
    model.eval()
    with torch.no_grad():
        predicted = model(X_test).numpy()
    
    # भविष्यवाणियों को इनवर्स ट्रांसफॉर्म करें
    predicted = scaler.inverse_transform(predicted)
    y_test_actual = scaler.inverse_transform(y_test.numpy())
    
    # भविष्यवाणियों बनाम वास्तविक को प्लॉट करें
    plt.figure()
    plt.plot(y_test_actual, 'b', label='Actual Close Price')
    plt.plot(predicted, 'r', label='Predicted Close Price')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.show()
```

### मुख्य संशोधन और नोट्स

1.  **डेटा रिट्रीवल**:
    - `get_history_data` फ़ंक्शन का उपयोग किसी दिए गए प्रतीक (जैसे, Tencent के लिए '00700') के लिए ऐतिहासिक स्टॉक डेटा प्राप्त करने के लिए किया जाता है।
    - डेटा को आसान हेरफेर के लिए pandas DataFrame में बदल दिया जाता है।

2.  **प्रीप्रोसेसिंग**:
    - डेटा को क्लोजिंग प्राइस को [0, 1] तक स्केल करने के लिए `MinMaxScaler` का उपयोग करके सामान्य किया जाता है।
    - अगले दिन की क्लोजिंग प्राइस की भविष्यवाणी करने के लिए `sequence_length` (जैसे, 60 दिन) के अनुक्रम बनाए जाते हैं।
    - डेटा को ट्रेनिंग (80%) और टेस्टिंग (20%) सेट में विभाजित किया जाता है।

3.  **LSTM मॉडल**:
    - `StockLSTM` क्लास को एकल फीचर (क्लोजिंग प्राइस) या कई फीचर्स (जैसे, क्लोज, वॉल्यूम) को हैंडल करने के लिए `input_size` को समायोजित करके एडाप्ट किया गया है।
    - आउटपुट लेयर एक लीनियर लेयर का उपयोग करके एक एकल मान (अगले दिन की क्लोजिंग प्राइस) की भविष्यवाणी करती है।

4.  **ट्रेनिंग**:
    - ट्रेनिंग लूप स्टॉक प्राइस जैसे सतत मानों की भविष्यवाणी के लिए उपयुक्त MSE लॉस का उपयोग करती है।
    - मॉडल के प्रदर्शन को ट्रैक करने के लिए मॉडल का टेस्ट सेट पर मूल्यांकन किया जाता है।

5.  **विज़ुअलाइज़ेशन**:
    - मॉडल के कन्वर्जेंस का आकलन करने के लिए ट्रेनिंग और वैलिडेशन लॉस को प्लॉट किया जाता है।
    - मॉडल के प्रदर्शन का मूल्यांकन करने के लिए टेस्ट सेट के लिए प्रेडिक्टेड बनाम वास्तविक क्लोजिंग प्राइस को प्लॉट किया जाता है।

### संभावित चुनौतियाँ और विचार

1.  **डेटा गुणवत्ता और मात्रा**:
    - ऐतिहासिक डेटा की मात्रा (जैसे, `limit=1000` बार) मजबूत LSTM प्रशिक्षण के लिए अपर्याप्त हो सकती है। अधिक डेटा प्राप्त करने या छोटे `sequence_length` का उपयोग करने पर विचार करें।
    - स्टॉक डेटा शोर भरा हो सकता है, और LSTM मॉडल लंबी अवधि की निर्भरताओं या अचानक बाजार बदलावों के साथ संघर्ष कर सकते हैं।

2.  **फीचर इंजीनियरिंग**:
    - उदाहरण केवल क्लोजिंग प्राइस का उपयोग करता है। अतिरिक्त फीचर्स (जैसे, वॉल्यूम, मूविंग एवरेज, RSI जैसे तकनीकी संकेतक) शामिल करने से मॉडल प्रदर्शन में सुधार हो सकता है।
    - फीचर चयन और प्रीप्रोसेसिंग (जैसे, लापता डेटा, आउटलायर्स को हैंडल करना) महत्वपूर्ण हैं।

3.  **मॉडल जटिलता**:
    - LSTM आर्किटेक्चर सरल है (1 लेयर, 50 हिडन यूनिट्स)। जटिल वित्तीय डेटा के लिए, गहरे मॉडल, नियमितीकरण के लिए ड्रॉपआउट, या GRU या Transformer जैसी अन्य आर्किटेक्चर पर विचार करें।

4.  **ओवरफिटिंग**:
    - ओवरफिटिंग का पता लगाने के लिए ट्रेनिंग बनाम वैलिडेशन लॉस की निगरानी करें। यदि आवश्यक हो तो ड्रॉपआउट या वेट डिके जोड़ें।

5.  **रियल-टाइम इंटीग्रेशन**:
    - मॉडल का उपयोग रियल-टाइम ट्रेडिंग के लिए करने के लिए, हाल का डेटा प्राप्त करें, उसे प्रीप्रोसेस करें, और भविष्यवाणियां उत्पन्न करने के लिए प्रशिक्षित LSTM में फीड करें।
    - भविष्यवाणियों को एक ट्रेडिंग रणनीति (जैसे, यदि प्रेडिक्टेड प्राइस > करंट प्राइस X% से) के साथ जोड़ें।

6.  **API सीमाएँ**:
    - सुनिश्चित करें कि आपके TigerOpen API क्रेडेंशियल्स पर्यावरण चर (`TIGER_PEM`, `TIGER_TIGER_ID`, `TIGER_ACCOUNT`) में सही ढंग से सेट हैं।
    - कुछ प्रतीकों या समय अवधियों के लिए API दर सीमाओं और डेटा उपलब्धता से अवगत रहें।

### उदाहरण आउटपुट
यह मानते हुए कि कोड सफलतापूर्वक चलता है, आप देख सकते हैं:
- कंसोल आउटपुट जो प्रति युग ट्रेनिंग और वैलिडेशन लॉस दिखाता है (जैसे, `Epoch 0, Training Loss: 0.1234, Validation Loss: 0.1345`)।
- युगों में ट्रेनिंग और वैलिडेशन लॉस का एक प्लॉट, जो कन्वर्जेंस को दर्शाता है।
- टेस्ट सेट के लिए प्रेडिक्टेड बनाम वास्तविक क्लोजिंग प्राइस की तुलना करने वाला एक प्लॉट, जो दर्शाता है कि LMSO रुझानों को कितनी अच्छी तरह पकड़ता है।

### अगले कदम
- **फीचर्स को बढ़ाएँ**: तकनीकी संकेतक (जैसे, MACD, बोलिंगर बैंड) या एक्स पोस्ट से सेंटीमेंट डेटा (यदि सर्च के माध्यम से उपलब्ध हो) शामिल करें।
- **बैकटेस्टिंग**: लाभप्रदता का मूल्यांकन करने के लिए ऐतिहासिक डेटा का उपयोग करके एक सिम्युलेटेड ट्रेडिंग वातावरण में LMSO भविष्यवाणियों का परीक्षण करें।
- **ट्रेडिंग इंटीग्रेशन**: उचित जोखिम प्रबंधन के साथ LMSO भविष्यवाणियों के आधार पर ट्रेड निष्पादित करने के लिए `place_order` फ़ंक्शन का उपयोग करें।
- **हाइपरपैरामीटर ट्यूनिंग**: प्रदर्शन को अनुकूलित करने के लिए `sequence_length`, `hidden_size`, `num_layers`, और लर्निंग रेट के साथ प्रयोग करें।

### क्या यह काम करेगा?
हां, विश्लेषण के लिए ऐतिहासिक स्टॉक डेटा को LMSO के साथ जोड़ना एक व्यवहार्य दृष्टिकोण है, जिसका व्यापक रूप से एल्गोरिडमिक ट्रेडिंग में उपयोग किया जाता है। हालाँकि, सफलता निर्भर करती है:
- पर्याप्त और स्वच्छ डेटा पर।
- उचित प्रीप्रोसेसिंग और फीचर इंजीनियरिंग पर।
- एक अच्छी तरह से ट्यून किए गए LMSO मॉडल पर।
- भविष्यवाणियों पर कार्य करने के लिए एक मजबूत ट्रेडिंग रणनीति पर।

वित्तीय बाजार स्वाभाविक रूप से शोर भरे होते हैं और बाहरी कारकों (जैसे, समाचार, मैक्रोइकॉनॉमिक घटनाएँ) से प्रभावित होते हैं, इसलिए LMSO भविष्यवाणियों का उपयोग सावधानी से किया जाना चाहिए, आदर्श रूप से जोखिम नियंत्रणों के साथ एक व्यापक रणनीति के हिस्से के रूप में।

यदि आप किसी भी भाग (जैसे, फीचर्स जोड़ना, बैकटेस्टिंग, या रियल-टाइम ट्रेडिंग) में गहराई से उतरना चाहते हैं, तो मुझे बताएं!