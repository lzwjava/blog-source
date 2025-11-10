---
audio: false
generated: true
lang: hi
layout: post
title: टेक्स लाइव टीएलएमजीआर उपयोगकर्ता मोड को ठीक करना
translated: true
type: note
---

त्रुटि संकेत देती है कि आपके Debian/Ubuntu सिस्टम पर `tlmgr` यूज़र मोड इनिशियलाइज़ नहीं है। यह Ubuntu रिपॉजिटरीज़ से TeX Live इंस्टॉलेशन में एक सामान्य समस्या है। इसे ठीक करने का तरीका यहां बताया गया है:

## समाधान 1: tlmgr यूज़र मोड इनिशियलाइज़ करें

पहले, यूज़र मोड इनिशियलाइज़ करें:

```bash
tlmgr init-usertree
```

अगर यह काम नहीं करता है, तो यह कोशिश करें:

```bash
tlmgr --usermode init-usertree
```

## समाधान 2: apt का उपयोग करें (Ubuntu के लिए सुझाया गया)

चूंकि आप Ubuntu/Debian पर हैं, सिस्टम पैकेज मैनेजर का उपयोग करना अक्सर आसान होता है:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

यह FontAwesome5 को अन्य फ़ॉन्ट पैकेजों के साथ इंस्टॉल कर देगा।

## समाधान 3: जांचें कि क्या FontAwesome5 पहले से इंस्टॉल है

हो सकता है कि यह आपके सिस्टम में पहले से मौजूद हो। जांचने के लिए एक साधारण LaTeX फ़ाइल बनाएं:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome
\end{document}
```

इसे इसके साथ कंपाइल करें:
```bash
pdflatex test.tex
```

## समाधान 4: अगर आपको नवीनतम वर्जन चाहिए

अगर आपको विशेष रूप से FontAwesome5 का नवीनतम वर्जन चाहिए, तो आप यह कर सकते हैं:

1. पैकेज को सीधे CTAN से मैन्युअली डाउनलोड करें
2. इसे अपने लोकल texmf डायरेक्टरी में इंस्टॉल करें:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
# डाउनलोड किए गए पैकेज को इस डायरेक्टरी में एक्सट्रैक्ट करें
texhash ~/texmf
```

## त्वरित जांच

यह देखने के लिए कि आपके पास वर्तमान में कौन से TeX पैकेज इंस्टॉल हैं, यह चलाएं:

```bash
dpkg -l | grep texlive
```

अधिकांश उपयोगकर्ताओं के लिए, `sudo apt install texlive-fonts-extra` सबसे सरल समाधान है जो tlmgr यूज़र मोड की समस्याओं से पूरी तरह बचाता है।