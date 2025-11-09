---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: तीस मिनट के निर्माण अंतराल का अनुपालन
translated: true
type: note
---

### बिल्ड्स के बीच 30-मिनट का अंतराल लागू करने के लिए वर्कफ़्लो को संशोधित करें

यह सुनिश्चित करने के लिए कि आपका Jekyll डिप्लॉयमेंट वर्कफ़्लो बहुत बार न चले (यानी, लगातार रन्स के बीच कम से कम 30-मिनट का अंतराल हो), आप `build` जॉब में शुरुआत में ही एक सशर्त चरण जोड़ सकते हैं। यह चरण GitHub API को इस वर्कफ़्लो के सबसे हालिया सफल रन की टाइमस्टैम्प के लिए क्वेरी करेगा। यदि वर्तमान ट्रिगर उस रन के पूरा होने के 30 मिनट के भीतर है, तो जॉब एक संदेश के साथ जल्दी समाप्त हो जाएगी (बिल्ड को छोड़कर)।

यह दृष्टिकोण:
- GitHub REST API का उपयोग करता है (किसी बाहरी टूल की आवश्यकता नहीं)।
- केवल **सफल** पिछले रन्स की जांच करता है (स्थिति: "completed", निष्कर्ष: "success")।
- समय के अंतर को सेकंड में गणना करता है और इसकी तुलना 1800 (30 मिनट) से करता है।
- आपके मौजूदा पुश और `workflow_dispatch` ट्रिगर्स के साथ काम करता है।
- Concurrency सेटअप (जो ओवरलैपिंग रन्स को संभालता है) में हस्तक्षेप नहीं करता है।

#### अपडेट किया गया YAML स्निपेट
इस नए चरण को आपके `build` जॉब में "Checkout Repository" चरण के ठीक बाद डालें। वर्कफ़्लो का बाकी हिस्सा अपरिवर्तित रहता है।

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Enforce 30-Minute Build Gap
        id: cooldown
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # इस वर्कफ़्लो का सबसे हालिया सफल रन प्राप्त करें
          RUNS_RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${{ github.repository }}/actions/workflows/${{ github.workflow_ref }}/runs?status=completed&conclusion=success&per_page=1&sort=timestamp&direction=desc")

          # नवीनतम सफल रन की completed_at टाइमस्टैम्प निकालें (ISO 8601 प्रारूप)
          LAST_COMPLETED_AT=$(echo "$RUNS_RESPONSE" | jq -r '.[0].completed_at // empty')
          
          if [ -z "$LAST_COMPLETED_AT" ] || [ "$LAST_COMPLETED_AT" = "null" ]; then
            echo "कोई पिछला सफल रन नहीं मिला। बिल्ड जारी रखा जा रहा है।"
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

          # तुलना के लिए टाइमस्टैम्प्स को Unix सेकंड में बदलें
          CURRENT_TIME=$(date -u +%s)
          LAST_TIME=$(date -d "$LAST_COMPLETED_AT" +%s)
          TIME_DIFF=$((CURRENT_TIME - LAST_TIME))

          echo "अंतिम सफल रन इस समय पूरा हुआ: $LAST_COMPLETED_AT (अंतर: ${TIME_DIFF}s)"

          if [ $TIME_DIFF -lt 1800 ]; then  # 1800 सेकंड = 30 मिनट
            echo "बिल्ड छोड़ा गया: अंतिम सफल रन के बाद से 30 मिनट से कम समय बीता है।"
            echo "skip_build=true" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "पर्याप्त समय अंतराल है। बिल्ड जारी रखा जा रहा है।"
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

      # यदि कोलडाउन जांच विफल होती है तो पूरे बिल्ड को छोड़ दें (बाद के चरणों में इस शर्त को जोड़ें या बिल्ड को एक if में लपेटें)
      - name: Set up Python 3.13.2
        if: steps.cooldown.outputs.skip_build != 'true'
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      # ... (इसके बाद के सभी शेष चरणों पर 'if: steps.cooldown.outputs.skip_build != 'true'' शर्त दोहराएं)
```

#### मुख्य परिवर्तनों की व्याख्या
1. **API क्वेरी**:
   - वर्कफ़्लो रन्स के लिए GitHub Actions API एंडपॉइंट को हिट करने के लिए `curl` का उपयोग करता है।
   - केवल समाप्त, सफल रन्स प्राप्त करने के लिए `status=completed` और `conclusion=success` के लिए फ़िल्टर करता है।
   - सबसे हालिया रन के लिए `per_page=1` तक सीमित करता है और `timestamp desc` के अनुसार क्रमबद्ध करता है।
   - `completed_at` (पिछले रन का सटीक समापन समय) निकालता है।

2. **समय गणना**:
   - `date` का उपयोग करके वर्तमान समय और अंतिम पूर्णता समय दोनों को Unix टाइमस्टैम्प में बदलता है।
   - अंतर को सेकंड में गणना करता है।
   - यदि `< 1800` सेकंड है, तो `skip_build=true` सेट करता है और चरण को जल्दी समाप्त कर देता है।

3. **सशर्त निष्पादन**:
   - **प्रत्येक बाद के चरण** (जैसे, Python सेटअप, Install Dependencies, Sync built site तक) में `if: steps.cooldown.outputs.skip_build != 'true'` जोड़ें।
   - यह सुनिश्चित करता है कि यदि कोलडाउन ट्रिगर होता है, तो जॉब GitHub UI में "skipped" रिपोर्ट करती है, लेकिन फिर भी कारण लॉग करती है।

4. **हैंडल किए गए एज केस**:
   - कोई पिछला रन नहीं: आगे बढ़ता है (पहला बिल्ड)।
   - विफल/चल रहे पिछले रन: उन्हें अनदेखा करता है और आगे बढ़ता है।
   - API त्रुटियाँ: आगे बढ़ने के लिए फ़ॉलबैक करता है (सुरक्षित डिफ़ॉल्ट)।
   - `jq` `ubuntu-latest` पर पहले से इंस्टॉल है, इसलिए किसी अतिरिक्त सेटअप की आवश्यकता नहीं है।

#### परिवर्तन का परीक्षण
- इसे अपनी `main` ब्रांच में कमिट करें (यह वर्कफ़्लो को ट्रिगर करेगा)।
- एकाधिक त्वरित पुश/डिस्पैच ट्रिगर करें: 30 मिनट के भीतर दूसरा वाला छोड़ देना चाहिए।
- "Build skipped" संदेश के लिए जॉब लॉग्स की निगरानी करें।
- यदि आप अंतराल को समायोजित करना चाहते हैं (जैसे, 1 घंटा), `1800` को `3600` में बदलें।

#### विकल्प
- **Schedule Trigger**: यदि आप *आवधिक* बिल्ड्स चाहते हैं (हर 30 मिनट में, पुश की परवाह किए बिना), इसे `on:` सेक्शन में जोड़ें:
  ```yaml
  schedule:
    - cron: '*/30 * * * *'  # हर 30 मिनट
  ```
  लेकिन यह पुश ट्रिगर्स पर अंतराल लागू नहीं करता है—यदि आवश्यक हो तो कोलडाउन स्टेप के साथ इसका उपयोग करें।
- **Custom Action**: पुन: प्रयोज्यता के लिए, कोलडाउन लॉजिक को एक पुन: प्रयोज्य वर्कफ़्लो या कंपोजिट एक्शन में लपेटें।
- **सीमाएँ**: यह रन स्टार्ट टाइम नहीं, बल्कि रन कम्प्लीशन टाइम की जांच करता है। यदि कोई पिछला रन अभी भी >30 मिनट चल रहा है, तो concurrency वैसे भी इसे रद्द कर देगी।

यदि यह आपके सटीक इरादे के अनुरूप नहीं है (जैसे, आपका मतलब *कम से कम* हर 30 मिनट में शेड्यूलिंग करना था), तो अधिक विवरण प्रदान करें!