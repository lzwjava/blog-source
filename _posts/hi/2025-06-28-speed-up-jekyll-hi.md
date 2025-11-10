---
audio: false
generated: true
lang: hi
layout: post
title: 'जेकिल बिल्ड को तेज़ करना: मल्टीथ्रेडिंग तरीकों की खोज'
translated: true
type: note
---

जेकिल की बिल्ड प्रक्रिया डिफ़ॉल्ट रूप से सिंगल-थ्रेडेड होती है, जो बड़ी साइटों के लिए धीमी हो सकती है। हालांकि जेकिल में मल्टीथ्रेडेड बिल्ड सक्षम करने के लिए कोई अंतर्निहित कॉन्फ़िगरेशन विकल्प नहीं है, आप समानांतरता प्राप्त करने के लिए कुछ तरीकों का पता लगा सकते हैं। नीचे, मैं उपलब्ध जानकारी और तकनीकी विचारों के आधार पर संभावनाओं, चुनौतियों और व्यावहारिक कदमों को रेखांकित करता हूं।

### जेकिल बिल्ड सिंगल-थ्रेडेड क्यों होते हैं
जेकिल पृष्ठों को क्रमिक रूप से संसाधित करता है ताकि यह सुनिश्चित हो सके कि निर्भरताएं (जैसे `site.related_posts` या लिक्विड टेम्पलेट्स) सही ढंग से संभाली गई हैं। कुछ घटक, जैसे लिक्विड और कुछ प्लगइन्स, थ्रेड-सुरक्षित नहीं हो सकते हैं, जो मल्टीथ्रेडिंग को जटिल बनाता है ()। यह डिज़ाइन गति पर शुद्धता को प्राथमिकता देता है, लेकिन बड़ी साइटों के लिए, इसके परिणामस्वरूप बिल्ड का समय कई मिनट तक का हो सकता है (,)।[](https://github.com/jekyll/jekyll/issues/9485)[](https://github.com/jekyll/jekyll/issues/1855)[](https://github.com/jekyll/jekyll/issues/4297)

### मल्टीथ्रेडेड जेकिल बिल्ड के तरीके
जेकिल बिल्ड में समानांतरता लाने के संभावित तरीके यहां दिए गए हैं, विशेष रूप से आपके द्वारा प्रदान किए गए GitHub Actions वर्कफ़्लो जैसे संदर्भ में:

#### 1. **मल्टीथ्रेडेड रेंडरिंग के लिए कस्टम प्लगइन का उपयोग करें**
मल्टीथ्रेडेड रेंडरिंग के लिए एक प्रूफ-ऑफ-कंसेप्ट प्लगइन प्रस्तावित किया गया है ()। इसने एक टेस्ट केस में बिल्ड का समय 45 सेकंड से घटाकर 10 सेकंड कर दिया, लेकिन इसमें थ्रेड सुरक्षा के मुद्दे थे, जिसके परिणामस्वरूप पृष्ठ सामग्री गलत हो गई। यह प्लगइन `jekyll-feed` जैसे प्लगइन्स से भी टकराता है, जो क्रमिक रेंडरिंग पर निर्भर करते हैं।[](https://github.com/jekyll/jekyll/issues/9485)

**कस्टम प्लगइन आज़माने के चरण:**
- **प्लगइन बनाएं**: एक Ruby प्लगइन लागू करें जो जेकिल के `Site` क्लास को पृष्ठ रेंडरिंग को समानांतर करने के लिए एक्सटेंड करे। उदाहरण के लिए, आप `render_pages` मेथड को Ruby के `Thread` क्लास या थ्रेड पूल का उपयोग करने के लिए संशोधित कर सकते हैं ()।[](https://github.com/jekyll/jekyll/issues/9485)
  ```ruby
  module Jekyll
    module UlyssesZhan::MultithreadRendering
      def render_pages(*args)
        @rendering_threads = []
        super # Call original method
        @rendering_threads.each(&:join) # Wait for threads to complete
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::UlyssesZhan::MultithreadRendering)
  ```
- **Gemfile में जोड़ें**: प्लगइन को अपनी `_plugins` डायरेक्टरी में रखें और सुनिश्चित करें कि यह जेकिल द्वारा लोड किया गया है।
- **थ्रेड सुरक्षा के लिए टेस्ट करें**: चूंकि लिक्विड और कुछ प्लगइन्स (जैसे, `jekyll-feed`) टूट सकते हैं, अच्छी तरह से टेस्ट करें। आपको लिक्विड को पैच करने की आवश्यकता हो सकती है या कुछ फीचर्स के लिए मल्टीथ्रेडिंग से बचने की आवश्यकता हो सकती है ()।[](https://github.com/jekyll/jekyll/issues/9485)
- **GitHub Actions के साथ एकीकृत करें**: अपने वर्कफ़्लो को अपने रिपॉजिटरी में प्लगइन शामिल करने के लिए अपडेट करें। सुनिश्चित करें कि `jekyll-build-pages` एक्शन आपके कस्टम जेकिल सेटअप का उपयोग करता है:
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
    env:
      BUNDLE_GEMFILE: ./Gemfile # Ensure your custom Gemfile with the plugin is used
  ```

**चुनौतियां**:
- लिक्विड और `jekyll-feed` जैसे प्लगइन्स के साथ थ्रेड सुरक्षा के मुद्दे ()।[](https://github.com/jekyll/jekyll/issues/9485)
- गलत पृष्ठ रेंडरिंग की संभावना (जैसे, एक पृष्ठ की सामग्री दूसरे में दिखाई देना)।
- डीबग और मेंटेन करने के लिए Ruby विशेषज्ञता की आवश्यकता होती है।

#### 2. **मल्टीपल कॉन्फ़िगरेशन के साथ बिल्ड को समानांतर करें**
एक सिंगल बिल्ड को मल्टीथ्रेड करने के बजाय, आप अपनी साइट को छोटे हिस्सों में विभाजित कर सकते हैं (जैसे, कलेक्शन या डायरेक्टरी द्वारा) और उन्हें मल्टीपल जेकिल प्रक्रियाओं का उपयोग करके समानांतर में बिल्ड कर सकते हैं। यह तरीका थ्रेड-सुरक्षा के मुद्दों से बचता है लेकिन अधिक सेटअप की आवश्यकता होती है।

**चरण**:
- **साइट को विभाजित करें**: अपनी साइट को कलेक्शन (जैसे, `posts`, `pages`, `docs`) या डायरेक्टरी में व्यवस्थित करें और प्रत्येक के लिए अलग-अलग `_config.yml` फाइलें बनाएं (,)।[](https://amcrouch.medium.com/configuring-environments-when-building-sites-with-jekyll-dd6eb2603c39)[](https://coderwall.com/p/tfcj2g/using-different-build-configuration-in-jekyll-site)
  ```yaml
  # _config_posts.yml
  collections:
    posts:
      output: true
  destination: ./_site/posts

  # _config_pages.yml
  collections:
    pages:
      output: true
  destination: ./_site/pages
  ```
- **GitHub Actions वर्कफ़्लो अपडेट करें**: अपने वर्कफ़्लो को संशोधित करें ताकि यह समानांतर में मल्टीपल जेकिल बिल्ड चलाए, प्रत्येक एक अलग कॉन्फ़िगरेशन फाइल के साथ।
  ```yaml
  name: Build Jekyll Site
  on:
    push:
      branches: [main]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Setup Ruby
          uses: ruby/setup-ruby@v1
          with:
            ruby-version: '3.1'
            bundler-cache: true
        - name: Build Posts
          run: bundle exec jekyll build --config _config_posts.yml
        - name: Build Pages
          run: bundle exec jekyll build --config _config_pages.yml
        - name: Combine Outputs
          run: |
            mkdir -p ./_site
            cp -r ./_site/posts/* ./_site/
            cp -r ./_site/pages/* ./_site/
        - name: Deploy
          uses: actions/upload-artifact@v4
          with:
            name: site
            path: ./_site
  ```
- **आउटपुट को संयोजित करें**: समानांतर बिल्ड के बाद, आउटपुट डायरेक्टरी को डिप्लॉयमेंट के लिए एक सिंगल `_site` फोल्डर में मर्ज करें।

**चुनौतियां**:
- कलेक्शन के बीच अंतर्निर्भरताओं का प्रबंधन (जैसे, `site.related_posts`)।
- कॉन्फ़िगरेशन और डिप्लॉयमेंट में जटिलता बढ़ना।
- कसकर जुड़ी हुई सामग्री वाली साइटों के लिए अच्छी तरह से स्केल नहीं हो सकता है।

#### 3. **बड़ी साइटों के लिए थ्रेड पूल का उपयोग करें**
`amp-jekyll` प्लगइन के लिए एक पुल रिक्वेस्ट ने सिस्टम को अभिभूत करने से बचने के लिए कॉन्फ़िगर करने योग्य थ्रेड्स की संख्या के साथ पृष्ठों को प्रोसेस करने के लिए थ्रेड पूल का उपयोग करने का सुझाव दिया ()। यह तरीका प्रदर्शन और संसाधन उपयोग को संतुलित करता है।[](https://github.com/juusaw/amp-jekyll/pull/26)

**चरण**:
- **थ्रेड पूल लागू करें**: एक फिक्स्ड नंबर वाले वर्कर थ्रेड्स (जैसे, 4 या 8, आपके सिस्टम पर निर्भर करता है) को प्रबंधित करने के लिए Ruby के `Thread::Queue` का उपयोग करने के लिए एक प्लगइन को संशोधित करें या बनाएं।
  ```ruby
  require 'thread'

  module Jekyll
    module ThreadPoolRendering
      def render_pages(*args)
        queue = Queue.new
        site.pages.each { |page| queue << page }
        threads = (1..4).map do # 4 threads
          Thread.new do
            until queue.empty?
              page = queue.pop(true) rescue nil
              page&.render_with_liquid(site)
            end
          end
        end
        threads.each(&:join)
        super
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::ThreadPoolRendering)
  ```
- **कॉन्फ़िगरेशन विकल्प जोड़ें**: उपयोगकर्ताओं को `_config.yml` में मल्टीथ्रेडिंग को टॉगल करने या थ्रेड्स की संख्या सेट करने की अनुमति दें:
  ```yaml
  multithreading:
    enabled: true
    thread_count: 4
  ```
- **वर्कफ़्लो के साथ एकीकृत करें**: सुनिश्चित करें कि प्लगइन आपके रिपॉजिटरी में शामिल है और GitHub Actions बिल्ड के दौरान लोड किया गया है।

**चुनौतियां**:
- पहले तरीके के समान थ्रेड-सुरक्षा के मुद्दे।
- कई छोटे टास्क वाली बड़ी साइटों के लिए कॉन्टेक्स्ट-स्विचिंग ओवरहेड ()।[](https://github.com/juusaw/amp-jekyll/pull/26)
- सभी प्लगइन्स के साथ कम्पेटिबिलिटी सुनिश्चित करने के लिए टेस्टिंग की आवश्यकता होती है।

#### 4. **बिना मल्टीथ्रेडिंग के ऑप्टिमाइज़ करें**
यदि मल्टीथ्रेडिंग बहुत जटिल या जोखिम भरा साबित होता है, तो आप सिंगल-थ्रेडेड बिल्ड प्रक्रिया को ऑप्टिमाइज़ कर सकते हैं:
- **इंक्रीमेंटल बिल्ड सक्षम करें**: केवल बदली हुई फाइलों को रीबिल्ड करने के लिए `jekyll build --incremental` का उपयोग करें (,)। अपने वर्कफ़्लो में जोड़ें:[](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/commands/build.rb)[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
      incremental: true
  ```
- **प्लगइन उपयोग कम करें**: कस्टम प्लगइन बिल्ड को काफी धीमा कर सकते हैं ()। ऑडिट करें और अनावश्यक प्लगइन्स को हटा दें।[](https://github.com/jekyll/jekyll/issues/4297)
- **तेज कन्वर्टर्स का उपयोग करें**: Kramdown से CommonMark जैसे तेज मार्कडाउन प्रोसेसर पर स्विच करें, या विशिष्ट उपयोग के मामलों के लिए Pandoc का टेस्ट करें ()।[](https://github.com/jekyll/jekyll/issues/9485)
- **निर्भरताओं को कैश करें**: जेम्स को दोबारा इंस्टॉल करने से बचने के लिए अपने GitHub Actions वर्कफ़्लो में `bundler-cache: true` सुनिश्चित करें ()।[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

### सिफारिशें
- **इंक्रीमेंटल बिल्ड से शुरुआत करें**: यह थ्रेड-सुरक्षा के मुद्दों को जोखिम में डाले बिना बिल्ड को तेज करने का सबसे सरल तरीका है। अपने वर्कफ़्लो में `--incremental` जोड़ें और इसके प्रभाव का टेस्ट करें।
- **थ्रेड पूल प्लगइन के साथ प्रयोग करें**: यदि आपके पास Ruby विशेषज्ञता है, तो कॉन्फ़िगर करने योग्य थ्रेड्स की संख्या के साथ थ्रेड पूल प्लगइन लागू करने का प्रयास करें (विकल्प 3)। थ्रेड सुरक्षा का टेस्ट करने के लिए एक छोटी साइट से शुरुआत करें।
- **अभी के लिए फुल मल्टीथ्रेडिंग से बचें**: लिक्विड और प्लगइन्स () के साथ थ्रेड-सुरक्षा चिंताओं को देखते हुए, फुल मल्टीथ्रेडिंग के लिए महत्वपूर्ण रीफैक्टरिंग या कस्टम लिक्विड फोर्क की आवश्यकता हो सकती है, जो तब तक व्यावहारिक नहीं हो सकता जब तक कि आप जेकिल के कोर डेवलपमेंट में योगदान नहीं दे रहे हैं।[](https://github.com/jekyll/jekyll/issues/9485)
- **बिल्ड टाइम मॉनिटर करें**: बिल्ड टाइम मापने और बॉटलनेक की पहचान करने के लिए GitHub Actions लॉग का उपयोग करें। उदाहरण के लिए, 6 मिनट का बिल्ड टाइम लेने वाली एक साइट () सुझाव देती है कि प्लगइन्स या बड़ी एसेट प्रोसेसिंग समस्या हो सकती है।[](https://github.com/jekyll/jekyll/issues/1855)

### इंक्रीमेंटल बिल्ड के साथ GitHub Actions उदाहरण
यहां इंक्रीमेंटल बिल्ड सक्षम के साथ आपके वर्कफ़्लो का अपडेटेड वर्जन दिया गया है:
```yaml
name: Build Jekyll Site
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
          incremental: true
      - name: Deploy
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: ./_site
```

### चेतावनियां
- **थ्रेड सुरक्षा**: जेकिल में मल्टीथ्रेडिंग प्रायोगिक है और यह प्लगइन्स को तोड़ सकती है या गलत आउटपुट उत्पन्न कर सकती है ()। पहले एक छोटी साइट पर अच्छी तरह से टेस्ट करें।[](https://github.com/jekyll/jekyll/issues/9485)
- **GitHub Actions सीमाएं**: समानांतर बिल्ड (विकल्प 2) संसाधन उपयोग बढ़ाते हैं, इसलिए सुनिश्चित करें कि आपका वर्कफ़्लो GitHub की फ्री-टियर सीमा के भीतर रहता है।
- **जेकिल 5 की संभावना**: जेकिल के भविष्य के वर्जन मल्टीथ्रेडिंग को मूल रूप से संबोधित कर सकते हैं, क्योंकि इस पर चर्चा की गई है ()। अभी के लिए, कस्टम समाधानों की आवश्यकता है।[](https://github.com/jekyll/jekyll/issues/9485)

यदि आपको किसी विशिष्ट तरीके (जैसे, प्लगइन लिखना या बिल्ड को विभाजित करना) को लागू करने में मदद की आवश्यकता है, तो मुझे बताएं, और मैं अधिक विस्तृत मार्गदर्शन या कोड प्रदान कर सकता हूं!