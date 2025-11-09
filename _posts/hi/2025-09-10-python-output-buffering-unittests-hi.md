---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: यूनिटटेस्ट में पायथन आउटपुट बफरिंग का समाधान
translated: true
type: note
---

हाँ — वह देरी लगभग हमेशा **आउटपुट बफरिंग** के कारण होती है, और Windows पर Git-Bash/mintty इसे और अधिक ध्यान देने योग्य बना सकता है। जब तक आप मल्टी-प्रोसेस लॉगिंग नहीं कर रहे हैं, तब तक आपको कतार (queue) की आवश्यकता नहीं है; पहले stdout/stderr को अनबफर्ड बनाएं और unittest की अपनी बफरिंग से बचें।

### यह करें जब आप रन करें

```bash
# PowerShell / CMD:
py -3.11 -u -m unittest -v

# Git-Bash:
PYTHONUNBUFFERED=1 py -3.11 -u -m unittest -v
# या
PYTHONUNBUFFERED=1 python -u -m unittest -v
```

* `-u` = अनबफर्ड stdio
* `PYTHONUNBUFFERED=1` = वही, चाइल्ड प्रोसेसेज को भी प्रभावित करता है

यदि आप सीधे `xx.py` का उपयोग कर रहे हैं:

```bash
python -u xx.py -v
```

### इसे अपने कोड के अंदर तत्काल बनाएं (ड्रॉप-इन)

इसे अपने टेस्ट बूटस्ट्रैप (या `if __name__ == "__main__":` ब्लॉक) के सबसे ऊपर रखें:

```python
import os, sys
os.environ.setdefault("PYTHONUNBUFFERED", "1")

# Python 3.7+
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True, write_through=True)
    sys.stderr.reconfigure(line_buffering=True, write_through=True)

print("booting tests...", flush=True)
```

और जब भी आप `print(...)` करें, महत्वपूर्ण स्थानों के लिए `flush=True` जोड़ें।

### यदि आप `logging` मॉड्यूल का उपयोग करते हैं

```python
import logging, sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,  # 3.8+
)
# StreamHandler प्रत्येक रिकॉर्ड को फ्लश करता है; यह सुनिश्चित करता है कि यह stdout की ओर इशारा करता है
```

### unittest बफरिंग पर नजर रखें

यदि आपने (या किसी फ्रेमवर्क ने) इसे सक्षम किया है, तो आउटपुट टेस्ट के अंत तक रोककर रखा जाता है:

* **बचें**: `unittest.main(buffer=True)` या `python -m unittest -b`
* डिफ़ॉल्ट (बिना `-b` के) का उपयोग करें ताकि लॉग जैसे ही हो प्रिंट हो जाएं।

### Git-Bash विशिष्ट सुझाव

* Mintty कभी-कभी प्रोग्रामों को यह सोचने पर मजबूर कर देता है कि stdout एक TTY नहीं है → अधिक बफरिंग। इसके लिए आपके दो सबसे अच्छे उपाय ऊपर बताया गया **`-u`/`PYTHONUNBUFFERED`** कॉम्बो है या फिर तुलना के लिए **Windows Terminal/PowerShell/CMD** से रन करें।
* यदि आप सबप्रोसेसेज स्पॉन करते हैं, तो वे भी तब तक बफर करेंगे जब तक कि वे env को इनहेरिट नहीं करते। `PYTHONUNBUFFERED=1` एक्सपोर्ट करने पर, चाइल्ड Python प्रोसेसेज ऐसा ही व्यवहार करती हैं।

### जब एक कतार *उपयोगी* होती है

केवल तभी जब आप **मल्टीप्रोसेसिंग** लॉगिंग कर रहे हों: वर्कर्स से मुख्य प्रोसेस में लॉग भेजने के लिए `logging.handlers.QueueHandler/QueueListener` का उपयोग करें; नहीं तो चाइल्ड बफर या इंटरलीविंग आपको परेशानी में डाल सकता है।

यदि आप टेस्ट चलाने का एक छोटा सा स्निपेट (कमांड + कोई भी `unittest.main(...)` आर्ग्स) और आप कैसे लॉग/प्रिंट करते हैं, पेस्ट करते हैं, तो मैं सभी आउटपुट को तत्काल बनाने के लिए न्यूनतम परिवर्तन तैयार करूंगा।