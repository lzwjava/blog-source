---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل جنكينز العملي للتكامل والنشر المستمر الآن
translated: true
type: note
---

ممتاز — دعنا نبني لك **دليل Jenkins نظيفًا وشاملًا** يمكنك استخدامه في العمل فورًا. سأجعله سهل التصفح، بدون جداول عريضة.

# ما هو Jenkins (ومتى تستخدمه)

Jenkins هو خادم أتمتة CI/CD ذاتي الاستضافة: تقوم بتوصيله بمستودع الكود المصدري، وتحدد خطوط الأنابيب في ملف `Jenkinsfile`، فيقوم بتشغيل عمليات البناء والاختبار والنشر على آلة واحدة أو أكثر ("وكلاء"). تأتي خطوط الأنابيب بنوعين — **التعريفية** (المفضلة) و**النصية** — وكلاهما موثقان من قبل المشروع. ([Jenkins][1])

---

# البنية الأساسية (بلغة بسيطة)

* **المتحكم**: واجهة الويب، قائمة الانتظار، وعمليات التنسيق المركزية.
* **الوكلاء/العُقد**: الأجهزة (أجهزة افتراضية، حاويات، أجهزة فعلية) حيث تعمل المهام فعليًا. يمكنك إضافة العديد من الوكلاء ووضع علامات عليهم حسب القدرة (مثل `java8`، `docker`). ([Jenkins][2])
* **المهام/خطوط الأنابيب**: تعريفات العمل (يُفضل تخزينها ككود في مستودعك).
* **الإضافات**: تضيف ميزات (بيانات الاعتماد، استراتيجيات المصادقة، وكلاء السحابة، JCasC، إلخ).

---

# التثبيت وتأمين التشغيل الأولي (قائمة مراجعة سريعة)

1.  **التثبيت** على Linux أو صورة حاوية.
2.  **الوكيل العكسي + TLS** (Nginx/Apache، موزع حمل شركة).
3.  **إدارة Jenkins → تكوين الأمان العام**
    * تعيين **نطاق أمان** حقيقي (LDAP/OIDC/SAML/إلخ).
    * اختيار وضع **تفويض** (انظر أدناه). ([Jenkins][3])
4.  **إنشاء مستخدم مسؤول** (غير مشترك).
5.  **تقييد عمليات التسجيل**، وتعطيل صلاحيات الكتابة للمجهول.
6.  **إضافة بيانات الاعتماد فقط** — لا تقم بتشفير الأسرار داخل المهام أبدًا. ([Jenkins][4])

---

# التحكم في الوصول (RBAC وتحديد نطاق المشروع)

يأتي Jenkins مزودًا بـ **الأمان القائم على المصفوفة** للتحكم الدقيق في الصلاحيات (البناء، التهيئة، الحذف، إلخ). استخدمه للنسخ الصغيرة/المتوسطة أو كأساس. ([Jenkins][3], [إضافات Jenkins][5])

للمؤسسات الأكبر حجمًا وعزل الفرق بشكل أنظف، قم بتثبيت **استراتيجية التفويض القائمة على الأدوار** (إضافة "role-strategy"):

* تعريف **الأدوار العامة** (مثل `admin`، `reader`).
* تعريف **أدوار المشروع** محددة النطاق بواسطة regex للعنصر/المجلد (مثل `team-alpha.*`).
* تعيين المستخدمين/المجموعات للأدوار — الآن الفرق ترى وتُبنى فقط ما تمتلكه. ([إضافات Jenkins][6])

> نصيحة: ضع خطوط أنابيب كل فريق داخل **مجلد**، ثم طبق أدوار المشروع على مستوى المجلد. ادمج مع **المصفوفة** إذا كنت بحاجة إلى تعديلات دقيقة للغاية. ([إضافات Jenkins][5])

---

# بيانات الاعتماد والأسرار (أنماط آمنة)

* أضف الأسرار في **إدارة Jenkins → بيانات الاعتماد** (عامة أو محددة النطاق بمجلد).
* في خط الأنابيب التعريفية، استخدم `credentials()` في `environment` للإشارة إليها، أو اربطها عند الطلب باستخدام `withCredentials { … }`.
* يُفضل استخدام الرموز المميزة قصيرة العمر من خزينة أسرار أو إضافة موفر؛ وقم بتدويرها بانتظام. ([Jenkins][4])

**أمثلة (تعريفية):**

```groovy
pipeline {
  agent any
  environment {
    // تحقن متغيري بيئة USER وPASS من بيانات اعتماد اسم مستخدم/كلمة مرور
    CREDS = credentials('dockerhub-creds-id')
  }
  stages {
    stage('تسجيل الدخول') {
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
    stage('استخدام نص سري') {
      steps {
        withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {
          sh 'curl -H "Authorization: Bearer $SLACK_TOKEN" https://slack.example/api'
        }
      }
    }
  }
}
```

التوثيق الخاص بالاستخدام والربط موجود هنا. ([Jenkins][7])

---

# الوكلاء على نطاق واسع

* أضف وكلاء **دائمين** أو **مؤقتين**؛ ضع علامات عليهم حسب القدرات؛ عيّن طريقة التشغيل (SSH، JNLP، سحابة).
* يراقب Jenkins المساحة التخزينية، وملفات المبادلة، والمجلدات المؤقتة، وانحراف التوقيت ويمكنه إيقاف العُقد غير الصحية تلقائيًا. حافظ على نظافة العلامات واستخدم `agent { label 'docker' }` في المراحل للتوجيه. ([Jenkins][2])

---

# خطوط أنابيب لا تسبب مشاكل (Jenkinsfile حديث)

**التعريفية مقابل النصية**: يُفضل استخدام **التعريفية** — هيكل أوضح، حواجز حماية (`post`، `options`، `when`، `environment`، `input`، `parallel`). ([Jenkins][1])

**مثال أساسي لـ CI:**

```groovy
pipeline {
  agent { label 'docker' }
  options { timestamps(); durabilityHint('PERFORMANCE_OPTIMIZED') }
  triggers { pollSCM('@daily') } // أو استخدم webhooks في نظام إدارة الكود المصدري الخاص بك
  stages {
    stage('الاستخراج') { steps { checkout scm } }
    stage('البناء')    { steps { sh './gradlew build -x test' } }
    stage('الاختبار')     { steps { sh './gradlew test' } }
    stage('التعبئة')  { when { branch 'main' } steps { sh './gradlew assemble' } }
  }
  post {
    always { junit 'build/test-results/test/*.xml'; archiveArtifacts 'build/libs/*.jar' }
    failure { mail to: 'team@example.com', subject: "فشل البناء ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
  }
}
```

**مراجع أساسية:** كتاب Pipeline، مرجع الصياغة، وتوثيق الخطوات. ([Jenkins][1])

---

# متعدد الفروع، GitHub/ GitLab، وطلبات السحب

استخدم **خط أنابيب متعدد الفروع** أو مهمة منظمة GitHub/Bitbucket بحيث يتم بناء كل فرع/طلب سحب في المستودع يحتوي على `Jenkinsfile` تلقائيًا (عبر webhooks). حافظ على سلوك الفروع في الكود وتجنب العمليات النقرية.

---

# إعادة الاستخدام على نطاق واسع: المكتبات المشتركة

عندما تكرر خطوات عبر مستودعات متعددة، أنشئ **مكتبة Jenkins المشتركة** (دوال vars، خطوات خط الأنابيب) واستوردها في `Jenkinsfile` باستخدام `@Library('your-lib') _`. هذا يمنع نسخ ولصق خطوط الأنابيب ويركز الإصلاحات.

---

# التهيئة ككود (JCasC)

عامل تكوين المتحكم الخاص بك ككود: احفظه في Git، وادرسه عبر طلبات السحب، وشغّل متحكمات جديدة بشكل قابل للتكرار.

* ثبّت إضافة **Configuration as Code**.
* اكتب YAML يلتقط الأمان العام، مشغلات الوكلاء، مثبتات الأدوات، المجلدات، روابط بيانات الاعتماد، إلخ.
* حمّلها عند بدء التشغيل (متغير البيئة `CASC_JENKINS_CONFIG`) أو من واجهة المستخدم. ([إضافات Jenkins][8], [Jenkins][9])

**لمحة صغيرة من JCasC:**

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

التوثيق الرسمي وصفحة الإضافة أعلاه. ([Jenkins][9], [إضافات Jenkins][8])

---

# الإضافات (استخدمها بحكمة)

* **الأساسيات التي يجب معرفتها**: Credentials, Matrix/Role-Strategy, Pipeline, Git, SSH, Email, Artifact Manager (مثل S3/GCS), Cloud agents (Kubernetes), JCasC.
* حافظ على **الحد الأدنى من الإضافات وتحديثها**، ثبّت الإضافات الحرجة، واختبر التحديثات في متحكم تجريبي. يوجد التوثيق العملي للإضافات على jenkins.io وصفحة كل إضافة. ([Jenkins][10])

---

# المراقبة والنظافة

* **السجلات**: استخدم مسجل السجلات في المتحكم + أرسل السجلات إلى ELK/CloudWatch.
* **المنتجات**: احفظ فقط ما تحتاجه.
* **JUnit**: انشر تقارير الاختبار دائمًا؛ أوقف عمليات البناء عند فشل الاختبارات.
* **صحة قائمة الانتظار**: راقب طابور البناء واستخدام الوكلاء؛ وزّع الوكلاء وفقًا لذلك.
* **النسخ الاحتياطي**: احفظ نسخة احتياطية من `$JENKINS_HOME` أو استخدم JCasC + متحكمات مؤقتة.

---

# تحسينات أمنية سريعة

* عطّل CLI حيث لا حاجة له؛ فضّل رموز API.
* افصل حسابات **الخدمة** عن حسابات البشر.
* أسرار محددة النطاق بالمجلد فقط؛ لا تعيد عرض الأسرار أبدًا.
* اقفل عمليات الموافقة على النصوص النصية؛ قلل من خطوات `script` في التعريفية.
* راجع الأدوار بانتظام. التوجيه موجود في وثائق أمان Jenkins. ([Jenkins][3])

---

# تحسينات "اليوم الثاني" النموذجية

* **اختبارات متوازية** لتقليل وقت البناء.
* **التخزين المؤقت** (مثل تخزين Gradle/Maven المؤقت على الوكلاء).
* **Docker-in-Docker** أو **وكلاء Kubernetes** لصور بناء نظيفة وقابلة للتكرار.
* **بوابات الجودة** (فحص الكود، SAST/DAST) في المراحل المبكرة.
* ترقيات **الترويج** أو مراحل النشر متعددة البيئات مع شروط `when` و `input` يدوي.

---

# غشيات استكشاف الأخطاء وإصلاحها

* عمليات بناء عالقة؟ تحقق من سجلات الوكيل، مساحة التخزين، وانحراف توقيت العقدة. سيقوم Jenkins بإيقاف العُقد التي تتجاوز عتبات الصحة تلقائيًا. ([Jenkins][2])
* بيانات الاعتماد غير موجودة؟ تأكد من النطاق (مجلد مقابل عام) وصحة `credentialsId`. ([Jenkins][4])
* مشاكل غريبة في المصادقة؟ تحقق مرة أخرى من اقتران نطاق الأمان ↔ استراتيجية التفويض (Matrix/Role-strategy). ([Jenkins][3], [إضافات Jenkins][6])
* أخطاء في صياغة خط الأنابيب؟ تحقق من الصحة باستخدام خطوة التحقق من **التعريفية** / المحرر عبر الإنترنت. ([Jenkins][11])

---

# نقطة بداية "ذهبية" جاهزة للنسخ

```groovy
pipeline {
  agent { label 'k8s || docker || linux' }
  options { timestamps(); buildDiscarder(logRotator(numToKeepStr: '50')); ansiColor('xterm') }
  environment { JAVA_TOOL_OPTIONS = '-XX:+UseContainerSupport' }
  stages {
    stage('الاستخراج') { steps { checkout scm } }
    stage('الإعداد')    { steps { sh 'python -V || true' } }
    stage('البناء')    { steps { sh './gradlew build -x test' } }
    stage('الاختبار')     { steps { junit 'build/test-results/test/*.xml' } }
    stage('التعبئة')  { when { branch 'main' } steps { sh './gradlew assemble' } }
    stage('النشر')   { when { branch 'main' } steps { input 'الشحن إلى بيئة التجربة؟'; sh './scripts/deploy_staging.sh' } }
  }
  post {
    failure { echo "فشل: ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
    always  { archiveArtifacts artifacts: 'build/libs/*.jar', fingerprint: true }
  }
}
```

---

# أين تقرأ المزيد (وثائق عالية الجودة)

* **خط الأنابيب: نظرة عامة وصياغة** (التعريفية مقابل النصية، جميع التوجيهات والخطوات). ([Jenkins][1])
* **الأمان والتفويض** (المصفوفة)، بالإضافة إلى **إضافة Role-Strategy** لـ RBAC. ([Jenkins][3], [إضافات Jenkins][5])
* **الوكلاء والعُقد** (الإضافة، الصحة، العلامات). ([Jenkins][2])
* **استخدام بيانات الاعتماد** (واجهة المستخدم ومساعدو/روابط خط الأنابيب). ([Jenkins][4])
* **التهيئة ككود (JCasC)** (المفاهيم + الإضافة). ([Jenkins][9], [إضافات Jenkins][8])

---

إذا أردت، يمكنني تخصيص هذا **لإعداداتك الدقيقة** (GitHub مقابل GitLab، وكلاء داخلية مقابل k8s، ونموذج RBAC الخاص بك) وصياغة:

* بذرة **JCasC** YAML،
* تعيين **استراتيجية الأدوار** لفرقك، و
* هيكل **مكتبة مشتركة** للمراحل الموحدة.

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