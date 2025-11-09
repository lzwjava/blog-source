---
audio: false
date: 2025-09-06
generated: true
image: false
lang: hi
layout: post
title: मॉडल आकार सुधार और सुधार
translated: true
type: note
---

यहाँ आपकी स्क्रिप्ट क्या कर रही है, टुकड़े-टुकड़े में समझाया गया है, साथ ही कुछ महत्वपूर्ण सुधार भी दिए गए हैं जिन्हें आप शायद करना चाहेंगे।

# मॉडल क्या है

* आप एक छोटा **कैरेक्टर/वर्ड-लेवल नेक्स्ट-टोकन प्रेडिक्टर** परिभाषित करते हैं:

  * `nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1)` वन-हॉट वेक्टर (साइज = `vocab_size`) के एक सीक्वेंस को प्रोसेस करता है और प्रत्येक टाइम स्टेप पर साइज 50 का एक हिडन स्टेट प्रोड्यूस करता है।
  * `nn.Linear(50, vocab_size, bias=False)` प्रत्येक टाइम स्टेप के हिडन स्टेट को **वोकैबुलरी पर लॉजिट्स** में मैप करता है।

# अपेक्षित टेंसर शेप (महत्वपूर्ण)

PyTorch LSTM का डिफॉल्ट इनपुट शेप **(seq\_len, batch\_size, input\_size)** होता है क्योंकि आपने `batch_first=True` सेट नहीं किया है।

* बैच साइज 1 में एक सिंगल सीक्वेंस के लिए:

  * LSTM को इनपुट `(seq_len, 1, vocab_size)` होना चाहिए।
  * LSTM आउटपुट `x` को `(seq_len, 1, hidden_size)` शेप के साथ देता है।
  * फिर आप `view(-1, hidden_size)` → `(seq_len, hidden_size)` करते हैं ताकि लीनियर लेयर `(seq_len, vocab_size)` प्रोड्यूस करे।
  * `CrossEntropyLoss` अपेक्षा करता है:

    * `outputs`: `(N, C)` = `(seq_len, vocab_size)`
    * `targets`: `(N,)` = `(seq_len,)` टोकन इंडिसेज़

# आपका कोड संभावित रूप से कहाँ गलत हो रहा है (शेप)

आप करते हैं:

```python
inputs_one_hot = inputs_one_hot.permute(0, 2, 1)
```

अगर `one_hot_encode_sequence` `(batch, seq_len, vocab)` रिटर्न करता है, तो डिफॉल्ट LSTM के लिए सही पर्म्यूट है **`permute(1, 0, 2)`** (ताकि `(seq_len, batch, vocab)` मिले)। आपका मौजूदा `permute(0,2,1)` `(batch, vocab, seq_len)` देता है, जो मिसमैच्ड है और या तो एरर देगा या बिना सीखे नॉनसेंस सीखेगा अगर अर्लियर शेप अलग है।

दो साफ विकल्प (एक चुनें):

**A) डिफॉल्ट LSTM रखें (batch\_second):**

```python
# चाहिए (seq_len, batch, input_size)
inputs_one_hot = inputs_one_hot.permute(1, 0, 2)  # (seq_len, 1, vocab_size)
```

**B) इसे बैच-फर्स्ट बनाएं (अक्सर आसान):**

```python
self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, batch_first=True)
# चाहिए (batch, seq_len, input_size)
# फिर पर्म्यूट मत करो; (1, seq_len, vocab_size) के रूप में छोड़ दो
```

# ट्रेनिंग लूप लॉजिक

* आप प्रति युग दो रनिंग सम रखते हैं: `epoch_training_loss` और `epoch_validation_loss`।
* **वैलिडेशन फेज** (`net.eval()` + कोई ग्रेडिएंट स्टेप नहीं):

  * `validation_set` में प्रत्येक (inputs, targets) के लिए:

    * इनपुट को वन-हॉट एनकोड करें, टार्गेट्स को इंडिसेज़ में कन्वर्ट करें
    * फॉरवर्ड पास → लॉजिट्स `(seq_len, vocab_size)` (मानते हुए कि शेप ठीक हैं)
    * `(seq_len,)` शेप के टार्गेट इंडिसेज़ के खिलाफ CE लॉस
    * लॉस जोड़ें
* **ट्रेनिंग फेज** (`net.train()`):

  * वही प्रीप्रोसेसिंग
  * फॉरवर्ड → लॉस → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`
* आप एवरेज लॉस रिकॉर्ड करते हैं और हर 5 युग में प्रिंट करते हैं।

# इनफेरेंस और प्रिंटआउट

* आप `test_set` से एक सैंपल पिक करते हैं, मॉडल रन करते हैं, प्रत्येक टाइम स्टेप के लिए लॉजिट्स प्राप्त करते हैं, प्रति टाइम स्टेप `argmax` लेते हैं → प्रेडिक्टेड टोकन।
* आप इनपुट वर्ड्स, टार्गेट वर्ड्स और प्रेडिक्टेड वर्ड्स प्रिंट करते हैं।
* आप युगों पर ट्रेनिंग बनाम वैलिडेशन लॉस प्लॉट करते हैं।

# छोटे, उच्च-प्रभाव वाले सुधार

1.  **इनपुट शेप ठीक करें** (सबसे महत्वपूर्ण)। ऊपर A या B में से एक का उपयोग करें। अगर आप बैच-फर्स्ट चुनते हैं, तो फॉरवर्ड पास को बदलें:

    ```python
    x, (h, c) = self.lstm(x)         # x: (batch, seq, hidden)
    x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
    ```
2.  **ग्रेडिएंट ट्रैकिंग और स्पीड/मेमोरी के लिए eval/inference में `with torch.no_grad()` का उपयोग करें**:

    ```python
    net.eval()
    with torch.no_grad():
        outputs = net(inputs_one_hot)
        loss = criterion(outputs, targets_idx)
    ```

    और numpy कन्वर्जन के लिए:

    ```python
    outputs = net(inputs_one_hot).detach().numpy()
    ```
3.  **रिप्रोड्यूसिबिलिटी के लिए PyTorch को भी सीड करें**:

    ```python
    torch.manual_seed(42)
    ```
4.  **डिवाइस हैंडलिंग** (अगर आप GPU का उपयोग करते हैं):

    ```python
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net.to(device)
    inputs_one_hot = inputs_one_hot.to(device)
    targets_idx = targets_idx.to(device)
    ```
5.  **टार्गेट अलाइनमेंट**: सुनिश्चित करें कि `targets` **अगले टोकन** हैं जो प्रत्येक इनपुट टाइम स्टेप के साथ अलाइन हैं। अगर आपका डेटासेट `(inputs, targets)` को इस तरह पेयर करता है, तो आप ठीक हैं। अन्यथा, `targets = inputs[1:]` बनाएं और आखिरी इनपुट ड्रॉप करें या इसी तरह कुछ करें।
6.  **जब तक कोई कारण न हो `.bias=False` ड्रॉप करें**; आउटपुट लेयर पर बायस आमतौर पर हानिरहित/मददगार होता है।
7.  **पैडिंग/वेरिएबल लेंथ** (ऑप्शनल): अगर सीक्वेंस की लंबाई अलग-अलग है, तो पैडिंग टोकन पर ट्रेनिंग से बचने के लिए `pack_padded_sequence` पर विचार करें।
8.  **मॉनिटरिंग**: नेक्स्ट-टोकन प्रेडिक्शन पर एक्यूरेसी केवल लॉस से अधिक समझने योग्य हो सकती है—वैलिडेशन पर `% correct argmax` कंप्यूट करें।

# मिनिमल करेक्टेड स्निपेट (बैच-फर्स्ट वर्जन)

```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1, batch_first=True)
        self.l_out = nn.Linear(50, vocab_size)

    def forward(self, x):
        # x: (batch, seq, vocab_size)
        x, _ = self.lstm(x)                    # (batch, seq, hidden)
        x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
        x = self.l_out(x)                      # (batch*seq, vocab)
        return x

# ... अपने लूप में, permute हटा दें; सुनिश्चित करें कि inputs_one_hot (batch, seq, vocab) है
# validation/inference में `with torch.no_grad()` और `.detach()` का उपयोग करें
```

अगर आप वह सटीक शेप शेयर करते हैं जो `one_hot_encode_sequence` रिटर्न करता है (जैसे, `(seq, vocab)` बनाम `(1, seq, vocab)`), तो मैं आपके केस के लिए permute/reshape लाइनों को ठीक से टेलर कर सकता हूं।