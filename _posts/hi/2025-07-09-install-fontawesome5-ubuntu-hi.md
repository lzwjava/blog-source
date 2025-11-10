---
audio: false
generated: true
lang: hi
layout: post
title: उबुन्टू पर लेटेक में फॉन्टआवेसम५ इंस्टॉल करें
translated: true
type: note
---

Ubuntu पर LaTeX के लिए FontAwesome5 इंस्टॉल करने के लिए, आपके पास कई विकल्प हैं:

## Method 1: tlmgr (TeX Live Manager) का उपयोग करना

यदि आपके पास TeX Live इंस्टॉल है, तो आप पैकेज मैनेजर का उपयोग कर सकते हैं:

```bash
sudo tlmgr update --self
sudo tlmgr install fontawesome5
```

## Method 2: apt पैकेज मैनेजर का उपयोग करना

Ubuntu अपने रिपॉजिटरी के माध्यम से FontAwesome5 प्रदान करता है:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

यह FontAwesome5 सहित फोंट का एक व्यापक संग्रह इंस्टॉल करता है।

## Method 3: मैनुअल इंस्टॉलेशन

यदि उपरोक्त विधियाँ काम नहीं करती हैं, तो आप मैन्युअल रूप से इंस्टॉल कर सकते हैं:

1. CTAN से FontAwesome5 पैकेज डाउनलोड करें
2. इसे अपने लोकल texmf डायरेक्टरी में एक्सट्रैक्ट करें:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
cd ~/texmf/tex/latex/fontawesome5
# डाउनलोड किए गए पैकेज को यहाँ एक्सट्रैक्ट करें
```

3. TeX डेटाबेस अपडेट करें:
```bash
texhash ~/texmf
```

## LaTeX में FontAwesome5 का उपयोग करना

एक बार इंस्टॉल हो जाने पर, आप इसे अपने LaTeX दस्तावेज़ों में उपयोग कर सकते हैं:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome \quad Home icon
\faEnvelope \quad Email icon
\faGithub \quad GitHub icon
\end{document}
```

## समस्या निवारण

यदि आपको कोई समस्या आती है:

1. जांचें कि क्या आपकी TeX Live इंस्टॉलेशन अप-टू-डेट है:
```bash
tlmgr --version
```

2. सत्यापित करें कि पैकेज इंस्टॉल है:
```bash
tlmgr info fontawesome5
```

3. सुनिश्चित करें कि आप FontAwesome5 के साथ पूर्ण यूनिकोड सपोर्ट के लिए XeLaTeX या LuaLaTeX का उपयोग कर रहे हैं।

सबसे आसान तरीका आमतौर पर `apt install texlive-fonts-extra` का उपयोग करके Method 2 है क्योंकि यह स्वचालित रूप से डिपेंडेंसी को हैंडल करता है।