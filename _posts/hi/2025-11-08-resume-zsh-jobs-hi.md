---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: zsh में निलंबित नौकरियों को फिर से शुरू करना
translated: true
type: note
---

zsh के अंदर Ghostty में एक suspended job (जैसे आपका `bundle exec jekyll serve --incremental` command, जिसे संभवतः Ctrl+Z से रोका गया था) को resume करने के लिए, उसी terminal session में इन steps का पालन करें:

1.  सभी background/suspended jobs की सूची बनाएं यह पुष्टि करने के लिए कि वह मौजूद है:
    ```
    jobs
    ```
    इसका आउटपुट कुछ इस तरह दिखेगा: `[1]+  Suspended  bundle exec jekyll serve --incremental`।

2.  इसे foreground में resume करें (यह फिर से आपके terminal पर नियंत्रण ले लेगा):
    ```
    fg
    ```
    - अगर आपके multiple jobs हैं, तो `jobs` के आउटपुट से job number लेकर `fg %1` का उपयोग करके उस विशेष job को निर्दिष्ट करें (`1` को job number से बदलकर)।

अगर आप इसे background में चलाना चाहते हैं (ताकि यह serve करते समय आप terminal का उपयोग दूसरे कामों के लिए कर सकें), तो `bg %1` का उपयोग करें (फिर से, job number के साथ)।

एक बार resume होने के बाद, Jekyll को वहीं से काम शुरू करना चाहिए, बशर्ते कोई बड़ी रुकावट न आई हो। अगर process अटका हुआ लगे या error दे, तो आपको `kill %1` का उपयोग करके इसे खत्म करके दोबारा शुरू करना पड़ सकता है।