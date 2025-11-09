---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: GitHub एक्शन्स पुश प्रमाणीकरण त्रुटियों को ठीक करना
translated: true
type: note
---

वह 403 त्रुटि का मतलब है कि पुश **`lzwjava` के रूप में प्रमाणीकरण कर रहा है, लेकिन उसके पास लेखन पहुंच वाला कोई टोकन नहीं है** (अक्सर ऐसा इसलिए होता है क्योंकि जॉब अभी भी डिफ़ॉल्ट `GITHUB_TOKEN` का उपयोग कर रही है, जो किसी दूसरे रेपो में पुश नहीं कर सकता)। इसे **डेस्टिनेशन चेकआउट/पुश के लिए एक वास्तविक क्रेडेंशियल इंजेक्ट करके** ठीक करें।

यहां तीन विश्वसनीय तरीके दिए गए हैं—एक को चुनें। मैं सबसे तेज़ तरीका पहले दिखाऊंगा।

---

### विकल्प A — एक PAT का उपयोग करें और उसे रिमोट में एम्बेड करें (सबसे तेज़)

1. एक **क्लासिक PAT** बनाएं जिसमें `repo` स्कोप हो (या एक फाइन-ग्रेन्ड PAT जिसमें **Contents: Read & Write** की अनुमति `lzwjava/lzwjava.github.io` के लिए हो)। इसे सोर्स रेपो में `DEPLOY_TOKEN` के रूप में सेव करें।

2. अपने वर्कफ़्लो के डिप्लॉय स्टेप को अपडेट करें ताकि **रिमोट उस टोकन का उपयोग करने के लिए फोर्स हो**:

```yaml
- name: Check out destination repo
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    token: ${{ secrets.DEPLOY_TOKEN }}
    path: destination
    fetch-depth: 0

- name: Push built site to destination
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll

    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # रिमोट को PAT का स्पष्ट रूप से उपयोग करने के लिए फोर्स करें (क्रेडेंशियल-हेल्पर कॉन्फ्लिक्ट्स से बचाता है)
    git remote set-url origin https://${{ secrets.DEPLOY_TOKEN }}@github.com/lzwjava/lzwjava.github.io.git

    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

यदि आपको अभी भी 403 दिखाई देता है, तो आपके PAT में स्कोप्स की कमी है या (अगर रेपो किसी ऑर्गनाइजेशन में होता तो) उसे SSO ऑथराइजेशन की आवश्यकता होती। `repo` स्कोप के साथ इसे दोबारा जेनरेट करें और फिर से कोशिश करें।

---

### विकल्प B — क्रेडेंशियल लीक से बचें: पहले चेकआउट पर डिफ़ॉल्ट क्रेडेंशियल्स को अक्षम करें

कभी-कभी **पहला चेकआउट** डिफ़ॉल्ट `GITHUB_TOKEN` को क्रेडेंशियल हेल्पर में लिख देता है और बाद में इसका पुन: उपयोग हो जाता है। इसे अक्षम करें:

```yaml
- name: Check out source repo
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    persist-credentials: false   # <- महत्वपूर्ण
```

फिर डेस्टिनेशन चेकआउट को विकल्प A में दिखाए गए अपने PAT के साथ रखें (अगर चीजें पहले से ही काम कर रही हैं तो आप `remote set-url` लाइन को छोड़ सकते हैं, लेकिन यह हानिरहित है)।

---

### विकल्प C — SSH डिप्लॉय कुंजी (बहुत मजबूत)

1. अपनी मशीन पर: `ssh-keygen -t ed25519 -C "deploy@actions" -f deploy_key`
2. **पब्लिक कुंजी** (`deploy_key.pub`) को `lzwjava/lzwjava.github.io` में एक **डिप्लॉय कुंजी** के रूप में जोड़ें, जिसमें **लेखन पहुंच** हो।
3. **प्राइवेट कुंजी** (`deploy_key`) को **सोर्स** रेपो में `ACTIONS_DEPLOY_KEY` सीक्रेट के रूप में जोड़ें।

वर्कफ़्लो:

```yaml
- name: Check out destination repo via SSH
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    ssh-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
    path: destination
    fetch-depth: 0

- name: Push built site (SSH)
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll
    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

---

### यदि फिर से विफल हो तो त्वरित निदान

यह देखने के लिए कि वास्तव में कौन सा ऑथ कॉन्फ़िगर किया गया है, पुश करने से ठीक पहले इन कमांड्स को चलाएं:

```bash
cd destination
git remote -v
git config --get user.name
git config --get user.email
git config --get url.https://github.com/.insteadof || true
git config --global --list | sed -n 's/^credential\.helper.*/&/p'
```

यदि `remote -v` एक सादा `https://github.com/...` दिखाता है **बिना** आपके PAT के (विकल्प A) या `git@github.com:` (विकल्प C) नहीं दिखाता, तो आप अभी भी गलत क्रेडेंशियल का उपयोग कर रहे हैं।

---

### सामान्य गलतियाँ

* **फाइन-ग्रेन्ड PAT** को स्पष्ट रूप से **Contents: Read & Write** की अनुमति **उसी एक्सैक्ट रेपो** के लिए देनी होगी।
* `main` ब्रांच पर **ब्रांच प्रोटेक्शन** बॉट पुश को ब्लॉक कर सकता है (आवश्यक चेक/सिग्नेचर)। यदि ऐसा है, तो एक अनप्रोटेक्टेड ब्रांच (जैसे, `gh-pages`) पर डिप्लॉय करें या नियमों को एडजस्ट करें।
* **एक्सपायर्ड PAT** → दोबारा जेनरेट करें।
* **ऑर्गनाइजेशन SSO** (आपके केस में नहीं है अगर यह यूज़र रेपो है) → PAT को ऑर्गनाइजेशन के लिए ऑथराइज़ करें।

उपरोक्त तीन विकल्पों में से एक को करें और 403 त्रुटि चली जाएगी।