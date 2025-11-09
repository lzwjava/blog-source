---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: स्वचालित जेकिल निर्माण और तैनाती वर्कफ़्लो
translated: true
type: note
---

आप यह पूरी प्रक्रिया GitHub Actions में कर सकते हैं: रनर पर साइट बनाएं, फिर डेस्टिनेशन रेपो को एक सबफोल्डर में चेक आउट करें और `_site/` की सामग्री को वहां पुश कर दें।

नीचे एक ड्रॉप-इन वर्कफ़्लो दी गई है जिसे आप अपने **सोर्स** रेपो (जहां आपकी Python स्क्रिप्ट्स और Jekyll कंटेंट हैं) में जोड़ सकते हैं:

```yaml
# .github/workflows/build-and-deploy.yml
name: बिल्ड और डिप्लॉय Jekyll एक्सटर्नल रेपो में

on:
  push:
    branches: [ main ]
  workflow_dispatch:

# हम डेस्टिनेशन रेपो पुश के लिए एक PAT का उपयोग करेंगे
permissions:
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: सोर्स रेपो चेक आउट करें
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Ruby सेट अप करें
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: Jekyll डिपेंडेंसी इंस्टॉल करें
        run: |
          bundle install --jobs 4 --retry 3

      - name: Python सेट अप करें
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Python डिपेंडेंसी इंस्टॉल करें
        if: hashFiles('requirements.txt') != ''
        run: pip install -r requirements.txt

      - name: अपना लोकल वर्कफ़्लो पाइपलाइन चलाएं (CI मोड)
        env:
          # यहां वे सभी कीज़ जोड़ें जिनकी आपकी स्क्रिप्ट्स को आवश्यकता है
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        run: |
          # वही स्टेप्स चलाएं जो आपकी स्क्रिप्ट ऑर्केस्ट्रेट करती है।
          # यदि आप चाहें, तो आप अपनी स्क्रिप्ट को सीधे कॉल कर सकते हैं:
          python scripts/workflow_local.py
          # या, यदि आप एक्सप्लिसिट स्टेप्स पसंद करते हैं:
          # python scripts/generate/update_notes_link.py
          # python scripts/translation/update_lang.py --max_files 9 --model gemini-flash --commits 1000
          # python -m unittest discover -s tests/workflow
          # python scripts/release/update_release.py

      - name: Jekyll बिल्ड करें (_site में)
        run: |
          # यदि आपका Python मॉड्यूल DEFAULT_DESTINATION कहीं और सेट करता है, तो भी आप यहां ओवरराइड कर सकते हैं।
          bundle exec jekyll build --destination _site

      - name: डेस्टिनेशन रेपो चेक आउट करें
        uses: actions/checkout@v4
        with:
          repository: lzwjava/lzwjava.github.io   # <-- आपका DESTINATION_REPO_URL टार्गेट
          token: ${{ secrets.WORKFLOW_ACCESS_TOKEN }}      # <-- "repo" स्कोप वाला PAT
          path: destination
          fetch-depth: 0

      - name: बिल्ट साइट को डेस्टिनेशन रेपो में सिंक करें
        run: |
          mkdir -p destination/_site
          rsync -av --delete _site/ destination/_site/
          cd destination
          # ऑप्शनल: सुनिश्चित करें कि Pages Jekyll को दोबारा प्रोसेस न करे
          touch _site/.nojekyll

          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit --amend --no-edit
            # ब्रांच एडजस्ट करें यदि आपका डेस्टिनेशन कुछ और उपयोग करता है (जैसे, gh-pages)
            git push --force-with-lease origin HEAD:main
          else
            echo "डिप्लॉय के लिए कोई बदलाव नहीं हैं।"
          fi

      - name: (ऑप्शनल) बिल्ट साइट आर्टिफैक्ट अपलोड करें
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site
```

### आपको क्या सेट अप करने की आवश्यकता है

* **डेस्टिनेशन पुश के लिए PAT**: अपने GitHub अकाउंट पर `repo` स्कोप वाला एक क्लासिक पर्सनल एक्सेस टोकन बनाएं (या एक फाइन-ग्रेन्ड टोकन का उपयोग करें जो डेस्टिनेशन रेपो को राइट एक्सेस प्रदान करता हो)। इसे सोर्स रेपो की सेटिंग्स में `WORKFLOW_ACCESS_TOKEN` के रूप में सेव करें (यानी, `Settings → Secrets and variables → Actions → New repository secret`)।
* **ब्रांच और रेपो नाम**: `डेस्टिनेशन रेपो चेक आउट करें` स्टेप में, `repository:` को एक्सटर्नल रेपो पर सेट करें (यह पब्लिक या प्राइवेट हो सकता है)। पुश कमांड में, उस ब्रांच को सेट करें जिसमें आप डिप्लॉय करना चाहते हैं (अक्सर `main` या `gh-pages`)।
* **GitHub Pages सेटिंग्स** (यदि आप डेस्टिनेशन रेपो से सर्व कर रहे हैं): उस रेपो की **Settings → Pages** में, सही **Branch** चुनें (जैसे, `main` / root), और `CNAME`/कस्टम डोमेन को अपनी पसंद के अनुसार रखें।
* **हिस्ट्री एक्सपेक्टेशन्स**: डिप्लॉय स्टेप लेटेस्ट कमिट को अमेंड करती है और `--force-with-lease` का उपयोग करती है; सुनिश्चित करें कि यह ब्रांच डिप्लॉय आर्टिफैक्ट्स के लिए समर्पित है ताकि हिस्ट्री को रिव्राइट करना स्वीकार्य हो।

### आपकी Python स्क्रिप्ट के बारे में नोट्स

* आपको CI में `open_destination_repo_in_browser()` की आवश्यकता नहीं है, इसलिए इसे यथावत छोड़ना ठीक है; यहां यह कॉल नहीं होगी। वर्कफ़्लो सीधे रनर से पुश करती है।
* आपको CI में `push_destination_repo()` की भी आवश्यकता नहीं है। वर्कफ़्लो दूसरा चेकआउट और पुश हैंडल करती है, इसलिए आप अपनी स्क्रिप्ट को लोकल रन के लिए अपरिवर्तित रख सकते हैं।
* यदि आपकी `build_site()` एक अलग `DEFAULT_DESTINATION` में लिखती है, तो भी आप ऊपर दिखाए गए एक्सप्लिसिट Jekyll बिल्ड स्टेप को चलाकर ओवरराइड कर सकते हैं, जो `_site/` में लिखती है। डिप्लॉय स्टेप `_site/` से सिंक करती है।

### प्राइवेट डेस्टिनेशन रेपो?

* यह ठीक है। GitHub Pages केवल पब्लिक रेपो सर्व करता है (या उन ऑर्गनाइजेशन्स में पब्लिक ब्रांच जहां Pages एनेबल्ड है), लेकिन यदि आपका लक्ष्य सिर्फ किसी भी कारण से आर्टिफैक्ट्स को एक प्राइवेट रेपो में पुश करना है, तो ऊपर दिया गया तरीका अभी भी काम करता है। यदि आप Pages होस्टिंग चाहते हैं, तो सुनिश्चित करें कि वह डेस्टिनेशन रेपो/ब्रांच Pages सर्व करने के लिए कॉन्फ़िगर है (जहां आवश्यक हो वहां पब्लिक) या किसी अल्टरनेटिव होस्ट (जैसे, Cloudflare Pages, Netlify) का उपयोग करें और वहां डिप्लॉय करें।

बस इतना ही—अब आप GitHub के रनर्स पर बिल्ड करेंगे और `_site/` को क्लाउड में किसी दूसरे रेपो में पुश कर देंगे।