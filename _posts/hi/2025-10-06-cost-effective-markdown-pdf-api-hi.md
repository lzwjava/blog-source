---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: लागत-प्रभावी मार्कडाउन से पीडीएफ एपीआई
translated: true
type: note
---

### अनुशंसित सस्ता विकल्प: Google Cloud Run

एक साधारण Java-आधारित API के लिए जो Markdown को PDF में बदलता है (उदाहरण के लिए, Flying Saucer या iText जैसी लाइब्रेरी का उपयोग करके), जिसमें व्यक्तिगत ब्लॉग उपयोग के लिए केवल ~100 अनुरोध प्रति सप्ताह हों, **Google Cloud Run** सबसे किफायती विकल्प है। यह एक सर्वरलेस प्लेटफॉर्म है जो कंटेनराइज्ड ऐप्स चलाता है, निष्क्रिय होने पर शून्य तक स्केल करता है, और केवल वास्तविक उपयोग के लिए शुल्क लेता है। VMs प्रबंधित करने या हमेशा-चालू रहने वाली लागतों की चिंता करने की आवश्यकता नहीं है—आपके जैसे कम ट्रैफिक वाले परिदृश्यों के लिए बिल्कुल उपयुक्त।

#### अन्य विकल्पों पर Cloud Run को प्राथमिकता क्यों?
- **बनाम Compute Engine (VMs)**: VMs में निष्क्रिय रहने पर भी निश्चित प्रति घंटा लागत होती है, जो आवश्यकता से अधिक और अधिक महंगी होगी (एक छोटे इंस्टेंस के लिए न्यूनतम ~$5–10/माह)।
- **बनाम App Engine**: समान सर्वरलेस लाभ, लेकिन Java कंटेनरों के लिए Cloud Run अधिक लचीला है और अक्सर छिटपुट उपयोग के लिए सस्ता होता है।
- आपका वर्कलोड पूरी तरह से मुफ्त टियर के अंतर्गत आता है, इसलिए व्यवहार में **$0/माह** की उम्मीद करें।

#### अनुमानित लागत
100 अनुरोध/सप्ताह (~400/माह) के साथ:
- मान लें कि प्रत्येक अनुरोध 10 सेकंड के लिए 1 vCPU और 0.5 GiB मेमोरी का उपयोग करता है (त्वरित Markdown-to-PDF रूपांतरण के लिए रूढ़िवादी अनुमान)।
- कुल उपयोग: ~4,000 vCPU-सेकंड और ~2,000 GiB-सेकंड/माह।
- **मुफ्त टियर इसे पूरा कवर करता है**: 180,000 vCPU-सेकंड, 360,000 GiB-सेकंड, और 2 मिलियन अनुरोध प्रति माह (अधिकांश क्षेत्रों में)।
- यदि आप सीमा से अधिक हो जाते हैं (जो संभावना नहीं है), तो मुफ्त सीमा के बाद भुगतान दरें ~$0.000024/vCPU-सेकंड + $0.0000025/GiB-सेकंड + $0.40/मिलियन अनुरोध हैं—फिर भी $0.10/माह से कम।

आपके उपयोग के मामले में एग्रेस शुल्क नहीं है (आंतरिक API कॉल एक ही क्षेत्र के भीतर मुफ्त रहती हैं)।

#### अनुशंसित क्षेत्र: us-central1 (आयोवा)
- यह Cloud Run के लिए सबसे सस्ता Tier 1 क्षेत्र है, जिसमें कम्प्यूट के लिए सबसे कम दरें हैं और उत्तरी अमेरिका में विलंबता के लिए कोई प्रीमियम नहीं है।
- Tier 1 क्षेत्रों (US/Europe) में मूल्य निर्धारण समान है, लेकिन us-central1 औसत इंस्टेंस लागतों पर बेहतर है।
- यदि आप उत्तरी अमेरिका से बाहर हैं (उदाहरण के लिए, यूरोप या एशिया), तो बेहतर विलंबता के लिए निकटतम Tier 1 क्षेत्र जैसे europe-west1 (बेल्जियम) पर स्विच करें—लागत में <10% का अंतर होता है।
- Tier 2 क्षेत्रों (जैसे, asia-southeast1) से बचें क्योंकि वे 20–50% अधिक महंगे हैं।

#### आपके Java सर्वर के लिए त्वरित सेटअप गाइड
1. **अपना ऐप बनाएं**: एक साधारण REST API के लिए Spring Boot का उपयोग करें। एंडपॉइंट उदाहरण: POST `/convert` Markdown बॉडी के साथ, PDF वापस करें।
   - निर्भरता जोड़ें: `implementation 'org.xhtmlrenderer:flying-saucer-pdf:9.1.22'` (या इसी तरह)।
   - नमूना कोड स्निपेट:
     ```java:disable-run
     @RestController
     public class MarkdownController {
         @PostMapping("/convert")
         public ResponseEntity<byte[]> convert(@RequestBody String markdown) {
             // रूपांतरण तर्क यहाँ (उदाहरण के लिए, markdown को HTML में, फिर PDF में)
             byte[] pdfBytes = // आपका रूपांतरण परिणाम;
             return ResponseEntity.ok()
                 .header("Content-Type", "application/pdf")
                 .body(pdfBytes);
         }
     }
     ```
2. **कंटेनराइज़ करें**: एक `Dockerfile` बनाएं:
   ```
   FROM openjdk:17-jdk-slim
   COPY target/your-app.jar app.jar
   ENTRYPOINT ["java", "-jar", "/app.jar"]
   ```
   बिल्ड करें: `docker build -t gcr.io/your-project/markdown-api .`
3. **Cloud Run पर डिप्लॉय करें**:
   - GCP कंसोल में Cloud Run API सक्षम करें।
   - `gcloud run deploy markdown-api --image gcr.io/your-project/markdown-api --platform managed --region us-central1 --allow-unauthenticated --memory 512Mi --cpu 1 --max-instances 1`
   - URL प्राप्त करें: `https://markdown-api-abc.run.app/convert`
4. **परीक्षण करें**: एक Markdown POST अनुरोध भेजें; यह स्वचालित रूप से स्केल हो जाएगा।

यदि GCP में नए हैं तो $300 के निःशुल्क ट्रायल के लिए साइन अप करें। बिलिंग डैशबोर्ड में लागतों की निगरानी करें।

[Cloud Run मूल्य निर्धारण](https://cloud.google.com/run/pricing)  
[GCP क्षेत्र गाइड](https://www.cloudzero.com/blog/gcp-regions/)  
[Cloud Run क्विकस्टार्ट](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)