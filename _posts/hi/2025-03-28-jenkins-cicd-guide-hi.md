---
audio: false
generated: true
image: false
lang: hi
layout: post
title: प्रैक्टिकल जेंकिन्स सीआई सीडी गाइड नाउ
translated: true
type: note
---

बेहतरीन—चलिए आपके लिए एक **साफ-सुथरा, एंड-टू-एंड जेनकिंस गाइड** बनाते हैं जिसे आप तुरंत काम पर इस्तेमाल कर सकते हैं। मैं इसे स्कैन करने लायक रखूंगा, कोई चौड़ी टेबल्स नहीं।

# जेनकिंस क्या है (और इसका इस्तेमाल कब करें)

जेनकिंस एक सेल्फ-होस्टेड CI/CD ऑटोमेशन सर्वर है: आप इसे अपने सोर्स रेपो से कनेक्ट करते हैं, एक `Jenkinsfile` में पाइपलाइन्स डिफाइन करते हैं, और यह एक या अधिक मशीनों ("एजेंट्स") पर बिल्ड्स, टेस्ट्स और डिप्लॉयमेंट्स चलाता है। पाइपलाइन्स दो प्रकार की होती हैं—**डिक्लेरेटिव** (पसंदीदा) और **स्क्रिप्टेड**—दोनों प्रोजेक्ट द्वारा डॉक्यूमेंटेड हैं। ([Jenkins][1])

---

# कोर आर्किटेक्चर (साधारण भाषा में)

* **कंट्रोलर**: वेब UI, कतार, और ऑर्केस्ट्रेशन दिमाग।
* **एजेंट्स/नोड्स**: मशीनें (VMs, कंटेनर्स, बेयर मेटल) जहां जॉब वास्तव में चलती हैं। आप कई एजेंट्स जोड़ सकते हैं और उन्हें क्षमता के आधार पर लेबल कर सकते हैं (जैसे, `java8`, `docker`)। ([Jenkins][2])
* **जॉब्स/पाइपलाइन्स**: कार्य की परिभाषाएं (आदर्श रूप से कोड के रूप में आपके रेपो में स्टोर)।
* **प्लगइन्स**: फीचर्स जोड़ते हैं (क्रेडेंशियल्स, ऑथ स्ट्रैटेजीज, क्लाउड एजेंट्स, JCasC, आदि)।

---

# इंस्टॉल और फर्स्ट-रन हार्डनिंग (क्विक चेकलिस्ट)

1. **इंस्टॉल** करें Linux या कंटेनर इमेज पर।
2. **रिवर्स प्रॉक्सी + TLS** (Nginx/Apache, कॉर्पोरेट LB)।
3. **मैनेज जेनकिंस → कॉन्फ़िगर ग्लोबल सिक्योरिटी**

   * एक वास्तविक **सिक्योरिटी रियल्म** सेट करें (LDAP/OIDC/SAML/आदि)।
   * एक **ऑथराइजेशन** मोड चुनें (नीचे देखें)। ([Jenkins][3])
4. **एक एडमिन** यूजर बनाएं (शेयर नहीं)।
5. **साइन-अप्स प्रतिबंधित** करें, अनामन्यस राइट डिसेबल करें।
6. **क्रेडेंशियल्स प्लगइन** ही—जॉब्स में सीक्रेट्स कभी हार्डकोड न करें। ([Jenkins][4])

---

# एक्सेस कंट्रोल (RBAC और प्रोजेक्ट स्कोपिंग)

जेनकिंस फाइन-ग्रेन्ड परमिशन्स (बिल्ड, कॉन्फ़िगर, डिलीट, आदि) के लिए **मैट्रिक्स-बेस्ड सिक्योरिटी** के साथ आता है। इसे छोटे/मध्यम इंस्टेंस के लिए या बेस के रूप में इस्तेमाल करें। ([Jenkins][3], [Jenkins Plugins][5])

बड़े ऑर्गनाइजेशन और साफ़ टीम आइसोलेशन के लिए, **रोल-बेस्ड ऑथराइजेशन स्ट्रैटेजी** ("रोल-स्ट्रैटेजी" प्लगइन) इंस्टॉल करें:

* **ग्लोबल रोल्स** डिफाइन करें (जैसे, `admin`, `reader`)।
* **प्रोजेक्ट रोल्स** डिफाइन करें जो आइटम/फोल्डर रेजेक्स द्वारा स्कोप हों (जैसे, `team-alpha.*`)।
* यूजर्स/ग्रुप्स को रोल्स असाइन करें—अब टीमें केवल वही देखती/बनाती हैं जो उनके स्वामित्व में है। ([Jenkins Plugins][6])

> टिप: प्रत्येक टीम की पाइपलाइन्स को एक **फोल्डर** के अंदर रखें, फिर प्रोजेक्ट रोल्स को फोल्डर लेवल पर एप्लाई करें। अल्ट्रा-ग्रेन्युलर ट्वीक्स की जरूरत हो तो **मैट्रिक्स** के साथ कम्बाइन करें। ([Jenkins Plugins][5])

---

# क्रेडेंशियल्स और सीक्रेट्स (सुरक्षित पैटर्न्स)

* सीक्रेट्स **मैनेज जेनकिंस → क्रेडेंशियल्स** में जोड़ें (ग्लोबल या फोल्डर-स्कोप्ड)।
* डिक्लेरेटिव पाइपलाइन में, `environment` में `credentials()` के साथ रेफरेंस करें, या डिमांड पर `withCredentials { … }` के साथ बाइंड करें।
* वॉल्ट या प्रोवाइडर प्लगइन से शॉर्ट-लिव्ड टोकन को प्राथमिकता दें; नियमित रूप से रोटेट करें। ([Jenkins][4])

**उदाहरण (डिक्लेरेटिव):**

```groovy
pipeline {
  agent any
  environment {
    // यूजरनेम/पासवर्ड क्रेडेंशियल से USER और PASS env वैरिएबल इंजेक्ट करता है
    CREDS = credentials('dockerhub-creds-id')
  }
  stages {
    stage('Login') {
      steps {
        sh 'echo $CREDS_USR | docker login -u $CREDS_USR --password-stdin'
      }
    }
  }
}
```

```groovy
pipeline {
  agent any
  stages {
    stage('Use Secret Text') {
      steps {
        withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {
          sh 'curl -H "Authorization: Bearer $SLACK_TOKEN" https://slack.example/api'
        }
      }
    }
  }
}
```

यूसेज और बाइंडिंग्स के लिए डॉक्स यहां हैं। ([Jenkins][7])

---

# स्केल पर एजेंट्स

* **पर्मानेंट** या **इफिमेरल** एजेंट्स जोड़ें; क्षमताओं के आधार पर लेबल करें; लॉन्च मेथड सेट करें (SSH, JNLP, क्लाउड)।
* जेनकिंस डिस्क, स्वैप, टेम्प, क्लॉक ड्रिफ्ट की मॉनिटरिंग करता है और अनहेल्दी नोड्स को ऑटो-ऑफ़लाइन कर सकता है। लेबल्स साफ रखें और रूटिंग के लिए स्टेजेस में `agent { label 'docker' }` का उपयोग करें। ([Jenkins][2])

---

# पाइपलाइन्स जो परेशान नहीं करतीं (मॉडर्न Jenkinsfile)

**डिक्लेरेटिव बनाम स्क्रिप्टेड**: **डिक्लेरेटिव** को प्राथमिकता दें—स्पष्ट स्ट्रक्चर, गार्ड रेल्स (`post`, `options`, `when`, `environment`, `input`, `parallel`)। ([Jenkins][1])

**मिनिमल CI उदाहरण:**

```groovy
pipeline {
  agent { label 'docker' }
  options { timestamps(); durabilityHint('PERFORMANCE_OPTIMIZED') }
  triggers { pollSCM('@daily') } // या अपने SCM में वेबहुक्स का उपयोग करें
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { sh './gradlew test' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
  }
  post {
    always { junit 'build/test-results/test/*.xml'; archiveArtifacts 'build/libs/*.jar' }
    failure { mail to: 'team@example.com', subject: "Build failed ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
  }
}
```

**मुख्य संदर्भ:** पाइपलाइन बुक, सिंटैक्स रेफरेंस, और स्टेप डॉक्स। ([Jenkins][1])

---

# मल्टीब्रांच, GitHub/GitLab, और PRs

**मल्टीब्रांच पाइपलाइन** या GitHub/Bitbucket ऑर्गनाइजेशन जॉब का उपयोग करें ताकि `Jenkinsfile` वाली प्रत्येक रेपो ब्रांच/PR ऑटोमैटिकली बिल्ड हो (वेबहुक्स के माध्यम से)। ब्रांच बिहेवियर को कोड में रखें और क्लिक-ऑप्स से बचें।

---

# स्केल पर पुन: उपयोग: शेयर्ड लाइब्रेरीज

जब आप रेपो में स्टेप्स दोहराते हैं, तो एक **जेनकिंस शेयर्ड लाइब्रेरी** बनाएं (vars फंक्शन्स, पाइपलाइन स्टेप्स) और इसे `Jenkinsfile` में `@Library('your-lib') _` के साथ इम्पोर्ट करें। यह कॉपी-पेस्ट पाइपलाइन्स को रोकता है और फिक्सेस को केंद्रीकृत करता है।

---

# कॉन्फ़िगरेशन ऐज़ कोड (JCasC)

अपने कंट्रोलर के कॉन्फ़िगरेशन को कोड की तरह ट्रीट करें: इसे Git में चेक इन करें, PRs के माध्यम से रिव्यू करें, और नए कंट्रोलर्स को रिप्रोड्यूसिबली बूटस्ट्रैप करें।

* **कॉन्फ़िगरेशन ऐज़ कोड** प्लगइन इंस्टॉल करें।
* YAML लिखें जो ग्लोबल सिक्योरिटी, एजेंट लॉन्चर्स, टूल इंस्टॉलर्स, फोल्डर्स, क्रेडेंशियल्स बाइंडिंग्स, आदि को कैप्चर करे।
* इसे स्टार्टअप पर लोड करें (env var `CASC_JENKINS_CONFIG`) या UI से। ([Jenkins Plugins][8], [Jenkins][9])

**JCasC का छोटा सा स्वाद:**

```yaml
jenkins:
  systemMessage: "Jenkins managed by JCasC"
  authorizationStrategy:
    roleBased:
      roles:
        global:
          - name: "viewer"
            permissions:
              - "Overall/Read"
            assignments:
              - "devs"
  securityRealm:
    local:
      allowsSignup: false
      users:
        - id: "admin"
          password: "${ADMIN_PW}"
unclassified:
  location:
    url: "https://ci.example.com/"
```

ऑफिशियल डॉक्स और प्लगइन पेज ऊपर दिए गए हैं। ([Jenkins][9], [Jenkins Plugins][8])

---

# प्लगइन्स (उन्हें समझदारी से इस्तेमाल करें)

* **जानना जरूरी**: क्रेडेंशियल्स, मैट्रिक्स/रोल-स्ट्रैटेजी, पाइपलाइन, Git, SSH, ईमेल, आर्टिफैक्ट मैनेजर (जैसे, S3/GCS), क्लाउड एजेंट्स (Kubernetes), JCasC।
* प्लगइन्स को **मिनिमल और अपडेटेड** रखें, क्रिटिकल वाले पिन करें, और अपडेट्स को स्टेजिंग कंट्रोलर में टेस्ट करें। प्रैक्टिकल प्लगइन डॉक्स jenkins.io और प्रत्येक प्लगइन के पेज पर मौजूद हैं। ([Jenkins][10])

---

# ऑब्ज़र्वेबिलिटी और हाइजीन

* **लॉग्स**: कंट्रोलर लॉग रिकॉर्डर का उपयोग करें + लॉग्स को ELK/CloudWatch पर शिप करें।
* **आर्टिफैक्ट्स**: केवल वही आर्काइव करें जिसकी आपको जरूरत है।
* **JUnit**: हमेशा टेस्ट रिपोर्ट्स पब्लिश करें; टेस्ट फेल्योर पर बिल्ड्स तोड़ें।
* **क्यू हेल्थ**: बिल्ड क्यू और एजेंट यूटिलाइजेशन देखें; तदनुसार एजेंट्स स्केल करें।
* **बैकअप्स**: `$JENKINS_HOME` का बैकअप लें या JCasC + इफिमेरल कंट्रोलर्स का उपयोग करें।

---

# सिक्योरिटी क्विक विंस

* CLI को जहां जरूरी न हो डिसेबल करें; API टोकन को प्राथमिकता दें।
* **सर्विस** अकाउंट्स को इंसानों से अलग करें।
* केवल फोल्डर-स्कोप्ड सीक्रेट्स; सीक्रेट्स को कभी इको न करें।
* स्क्रिप्ट अप्रूवल्स को लॉक डाउन करें; डिक्लेरेटिव में `script` स्टेप्स को सीमित करें।
* रोल्स का नियमित ऑडिट करें। जेनकिंस की सिक्योरिटी डॉक्स में गाइडेंस है। ([Jenkins][3])

---

# टिपिकल "डे-2" इम्प्रूवमेंट्स

* **पैरेलल** टेस्ट शार्ड्स बिल्ड टाइम काटने के लिए।
* **कैशिंग** (जैसे, एजेंट्स पर Gradle/Maven कैश)।
* **Docker-in-Docker** या **Kubernetes एजेंट्स** साफ, रिप्रोड्यूसिबल बिल्ड इमेज के लिए।
* **क्वालिटी गेट्स** (लिंट, SAST/DAST) अर्ली स्टेजेस में।
* **प्रोमोशन** जॉब्स या मल्टी-एन्व डिप्लॉय स्टेजेस `when` कंडीशन और मैनुअल `input` के साथ।

---

# ट्रबलशूटिंग चीट्स

* स्टक बिल्ड्स? एजेंट लॉग्स, वर्कस्पेस डिस्क, और नोड क्लॉक स्क्यू चेक करें। जेनकिंस हेल्थ थ्रेशोल्ड से बाहर के नोड्स को ऑटो-ऑफ़लाइन कर देगा। ([Jenkins][2])
* क्रेडेंशियल नहीं मिल रहा? स्कोप (फोल्डर बनाम ग्लोबल) और सही `credentialsId` सुनिश्चित करें। ([Jenkins][4])
* ऑथ वीर्डनेस? रियल्म ↔ ऑथराइजेशन स्ट्रैटेजी पेयरिंग को दोबारा वेरिफाई करें (मैट्रिक्स/रोल-स्ट्रैटेजी)। ([Jenkins][3], [Jenkins Plugins][6])
* पाइपलाइन सिंटैक्स एरर? **डिक्लेरेटिव** वैलिडेटर स्टेप / ऑनलाइन एडिटर से वैलिडेट करें। ([Jenkins][11])

---

# कॉपी-रेडी "गोल्डन" स्टार्टिंग पॉइंट

```groovy
pipeline {
  agent { label 'k8s || docker || linux' }
  options { timestamps(); buildDiscarder(logRotator(numToKeepStr: '50')); ansiColor('xterm') }
  environment { JAVA_TOOL_OPTIONS = '-XX:+UseContainerSupport' }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Setup')    { steps { sh 'python -V || true' } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { junit 'build/test-results/test/*.xml' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
    stage('Deploy')   { when { branch 'main' } steps { input 'Ship to staging?'; sh './scripts/deploy_staging.sh' } }
  }
  post {
    failure { echo "Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
    always  { archiveArtifacts artifacts: 'build/libs/*.jar', fingerprint: true }
  }
}
```

---

# और कहां पढ़ें (हाई-सिग्नल डॉक्स)

* **पाइपलाइन: ओवरव्यू और सिंटैक्स** (डिक्लेरेटिव बनाम स्क्रिप्टेड, सभी डायरेक्टिव्स और स्टेप्स)। ([Jenkins][1])
* **सिक्योरिटी और ऑथराइजेशन** (मैट्रिक्स), साथ ही RBAC के लिए **रोल-स्ट्रैटेजी प्लगइन**। ([Jenkins][3], [Jenkins Plugins][5])
* **एजेंट्स और नोड्स** (जोड़ना, हेल्थ, लेबल्स)। ([Jenkins][2])
* **क्रेडेंशियल्स यूसेज** (UI और पाइपलाइन हेल्पर्स/बाइंडिंग्स)। ([Jenkins][4])
* **कॉन्फ़िगरेशन ऐज़ कोड (JCasC)** (कॉन्सेप्ट्स + प्लगइन)। ([Jenkins][9], [Jenkins Plugins][8])

---

यदि आप चाहें, तो मैं इसे **आपके एक्जैक्ट सेटअप** (GitHub बनाम GitLab, ऑन-प्रेम बनाम k8s एजेंट्स, और आपके RBAC मॉडल) के अनुरूप ढाल सकता हूं और ड्राफ्ट कर सकता हूं:

* एक **JCasC** YAML सीड,
* आपकी टीमों के लिए एक **रोल-स्ट्रैटेजी** मैपिंग, और
* स्टैंडर्डाइज्ड स्टेजेस के लिए एक **शेयर्ड लाइब्रेरी** स्केलेटन।

[1]: https://www.jenkins.io/doc/book/pipeline/?utm_source=chatgpt.com "Pipeline"
[2]: https://www.jenkins.io/doc/book/managing/nodes/?utm_source=chatgpt.com "Managing Nodes"
[3]: https://www.jenkins.io/doc/book/security/managing-security/?utm_source=chatgpt.com "Managing Security"
[4]: https://www.jenkins.io/doc/book/using/using-credentials/?utm_source=chatgpt.com "Using credentials"
[5]: https://plugins.jenkins.io/matrix-auth/?utm_source=chatgpt.com "Matrix Authorization Strategy"
[6]: https://plugins.jenkins.io/role-strategy/?utm_source=chatgpt.com "Role-based Authorization Strategy"
[7]: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/?utm_source=chatgpt.com "Using a Jenkinsfile"
[8]: https://plugins.jenkins.io/configuration-as-code/?utm_source=chatgpt.com "Configuration as Code | Jenkins plugin"
[9]: https://www.jenkins.io/doc/book/managing/casc/?utm_source=chatgpt.com "Configuration as Code"
[10]: https://www.jenkins.io/doc/developer/publishing/documentation/?utm_source=chatgpt.com "Plugin Documentation"
[11]: https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/?utm_source=chatgpt.com "Pipeline: Declarative"