---
audio: false
generated: false
image: false
lang: hi
layout: post
title: Awesome-CV का उपयोग करके एक पेशेवर रिज्यूमे बनाना
translated: true
---

### परिचय

[ZhiyeApp](https://www.zhiyeapp.com) का उपयोग करने से पहले, मैं शक्तिशाली और अनुकूलन योग्य [Awesome-CV](https://github.com/posquit0/Awesome-CV) पर स्विच कर गया। यह LaTeX-आधारित टेम्पलेट पेशेवर रिज्यूमे बनाने को आसान और अत्यधिक अनुकूलन योग्य बनाता है।

---

### Awesome-CV क्यों?  
- अनुकूलन योग्य: आप अनुभाग, रंग और फॉर्मेटिंग को अपने अनुसार बदल सकते हैं।  
- पेशेवर दिखावट: नौकरी के आवेदन के लिए एकदम साफ और सुंदर डिज़ाइन।  
- उपयोग में आसान: इसे इस्तेमाल करने के लिए LaTeX का बहुत कम ज्ञान चाहिए।

---

### मेरा रिज्यूमे उदाहरण

यहां मेरे द्वारा उपयोग किए जाने वाले `resume.tex` फ़ाइल का एक सरलीकृत संस्करण है:

```latex
%-------------------------------------------------------------------------------
% कॉन्फ़िगरेशन
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}
```

% पृष्ठ मार्जिन और अनुभाग हाइलाइट्स
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% व्यक्तिगत जानकारी
%-------------------------------------------------------------------------------
\name{Zhiwei}{Li}
\position{फुल स्टैक इंजीनियर{\enskip\cdotp\enskip}बैकएंड इंजीनियर}
\address{गुआंगज़ौ, चीन}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``स्वतंत्रता सत्य"}

%-------------------------------------------------------------------------------
\begin{document}

% हेडर और फुटर
\makecvheader[C]
\makecvfooter{\today}{Zhiwei Li~~~·~~~रिज्यूम}{\thepage}

% सामग्री अनुभाग
\input{resume/summary.tex}
\input{resume/experience.tex}
\input{resume/education.tex}
\input{resume/corporateprojects.tex}
\input{resume/personalprojects.tex}
\input{resume/blogposts.tex}
\input{resume/papers.tex}
\input{resume/books.tex}
\input{resume/skills.tex}
\input{resume/tools.tex}
\input{resume/knowledge.tex}
\input{resume/certificates.tex}

यह LaTeX दस्तावेज़ का समापन टैग है। इसे हिंदी में अनुवाद करने की आवश्यकता नहीं है।

# स्वचालन के लिए Makefile

Makefile एक शक्तिशाली टूल है जो आपके प्रोजेक्ट में स्वचालन को सरल बनाता है। यह विशेष रूप से सॉफ्टवेयर डेवलपमेंट में उपयोगी है, जहां आपको बार-बार कमांड चलाने की आवश्यकता होती है। Makefile का उपयोग करके आप इन कमांड्स को एक स्थान पर परिभाषित कर सकते हैं और उन्हें आसानी से चला सकते हैं।

## Makefile का बेसिक स्ट्रक्चर

एक साधारण Makefile का स्ट्रक्चर निम्नलिखित होता है:

```makefile
target: dependencies
    command
```

- **target**: यह एक लक्ष्य है जिसे आप बनाना चाहते हैं। यह एक फाइल नाम या एक कार्य हो सकता है।
- **dependencies**: ये वे फाइलें या लक्ष्य हैं जिनकी आवश्यकता target को बनाने के लिए होती है।
- **command**: यह वह कमांड है जो target को बनाने के लिए चलाई जाएगी।

## उदाहरण

मान लीजिए आपके पास एक साधारण C प्रोजेक्ट है, और आप इसे कंपाइल करना चाहते हैं। आप निम्नलिखित Makefile बना सकते हैं:

```makefile
# Makefile for a simple C project

CC = gcc
CFLAGS = -Wall -g

all: my_program

my_program: main.o utils.o
    $(CC) $(CFLAGS) -o my_program main.o utils.o

main.o: main.c
    $(CC) $(CFLAGS) -c main.c

utils.o: utils.c
    $(CC) $(CFLAGS) -c utils.c

clean:
    rm -f *.o my_program
```

### व्याख्या

- **CC**: कंपाइलर को परिभाषित करता है (इस मामले में `gcc`)।
- **CFLAGS**: कंपाइलर फ्लैग्स को परिभाषित करता है (इस मामले में `-Wall` और `-g`)।
- **all**: डिफ़ॉल्ट लक्ष्य जो `my_program` बनाता है।
- **my_program**: मुख्य प्रोग्राम जो `main.o` और `utils.o` ऑब्जेक्ट फाइल्स से बनता है।
- **main.o** और **utils.o**: ये ऑब्जेक्ट फाइल्स हैं जो संबंधित सोर्स फाइल्स से बनती हैं।
- **clean**: यह लक्ष्य सभी ऑब्जेक्ट फाइल्स और प्रोग्राम को हटा देता है।

## Makefile का उपयोग

Makefile का उपयोग करने के लिए, आप टर्मिनल में निम्नलिखित कमांड्स चला सकते हैं:

- **प्रोग्राम बनाने के लिए**:
  ```bash
  make
  ```

- **सफाई करने के लिए**:
  ```bash
  make clean
  ```

## निष्कर्ष

Makefile आपके प्रोजेक्ट में स्वचालन को सरल और प्रभावी बनाता है। यह आपको बार-बार कमांड टाइप करने से बचाता है और आपके वर्कफ्लो को तेज करता है। चाहे आप एक छोटे प्रोजेक्ट पर काम कर रहे हों या एक बड़े, Makefile आपकी मदद कर सकता है।

PDF जनरेशन प्रक्रिया को स्वचालित करने के लिए, मैं निम्नलिखित Makefile का उपयोग करता हूँ:

```Makefile
.PHONY: awesome-cv
```

(यह कोड ब्लॉक है और इसे अनुवादित नहीं किया जाना चाहिए।)

```makefile
CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/resume
RESUME_ZH_DIR = awesome-cv/resume-zh
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')
```

यह एक Makefile का हिस्सा है जो LaTeX दस्तावेज़ों को संकलित करने के लिए उपयोग किया जाता है। इसमें `xelatex` कंपाइलर का उपयोग किया जाता है और विभिन्न निर्देशिकाओं में `.tex` फ़ाइलों को खोजा जाता है।

awesome-cv: $(foreach x, coverletter resume-zh resume, $x.pdf)

(यह एक Makefile कमांड है, जिसे अनुवादित करने की आवश्यकता नहीं है। यह `coverletter.pdf`, `resume-zh.pdf`, और `resume.pdf` फ़ाइलों को बनाने के लिए एक लूप का उपयोग करता है।)

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

इस कोड को हिंदी में समझाया जाए तो:

`resume.pdf` फ़ाइल बनाने के लिए, `$(EXAMPLES_DIR)/resume.tex` और `$(RESUME_SRCS)` फ़ाइलों की आवश्यकता होती है। जब इन फ़ाइलों में कोई बदलाव होता है, तो `$(CC)` कमांड का उपयोग करके `resume.tex` फ़ाइल को संकलित किया जाता है और आउटपुट `$(EXAMPLES_DIR)` डायरेक्टरी में `resume.pdf` के रूप में सहेजा जाता है।

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

यह एक Makefile नियम है जो `coverletter.pdf` फ़ाइल को बनाने के लिए है। यह नियम `coverletter.tex` फ़ाइल को संकलित (compile) करके `coverletter.pdf` बनाता है। `$(CC)` एक चर है जो संकलक (compiler) को दर्शाता है, और `-output-directory=$(EXAMPLES_DIR)` विकल्प संकलित आउटपुट को `$(EXAMPLES_DIR)` डायरेक्टरी में सहेजता है। `$<` एक स्वचालित चर है जो पहले प्राथमिकता वाले (prerequisite) फ़ाइल को दर्शाता है, जो इस मामले में `coverletter.tex` है।

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

### यह कैसे काम करता है

1. PDF जनरेट करें:
   - निम्नलिखित PDF फ़ाइलें जनरेट करने के लिए `make awesome-cv` चलाएँ:
     - `resume.pdf`: अंग्रेजी रिज्यूमे
     - `resume-zh.pdf`: चीनी रिज्यूमे
     - `coverletter.pdf`: कवर लेटर
     
2. सफाई करें:
   - सभी जनरेट की गई PDF फ़ाइलों को हटाने के लिए `make clean` चलाएँ।

### निष्कर्ष

Awesome-CV और इस Makefile सेटअप का उपयोग करके, पेशेवर रिज्यूमे बनाना और उन्हें बनाए रखना आसान हो जाता है। चाहे आप तकनीकी भूमिकाओं के लिए आवेदन कर रहे हों या अपनी उपलब्धियों को साझा कर रहे हों, Awesome-CV आपको अपने काम को सुंदर और कुशलता से प्रस्तुत करने में मदद करता है।

अधिक जानकारी के लिए Awesome-CV रिपॉजिटरी देखें: Awesome-Cv on GitHub.