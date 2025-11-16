---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل تهيئة وظائف Jenkins
translated: true
type: note
---

### تكوين وظيفة في Jenkins

يدعم Jenkins أنواعًا مختلفة من الوظائف (تُسمى أيضًا مشاريع)، وأكثرها شيوعًا هي **مشاريع Freestyle** (لعمليات البناء البسيطة) و **مشاريع Pipeline** (لسيروات العمل المعقدة والمسيّرة باستخدام Jenkinsfile). سأوضح خطوات كل منهما أدناه. تفترض هذه الخطوات أنك قمت بتثبيت Jenkins وجعله يعمل (على سبيل المثال، عبر Docker أو على خادم). قم بالوصول إلى لوحة تحكم Jenkins على `http://localhost:8080` (أو عنوان URL لخادمك) وقم بتسجيل الدخول.

#### خطوات إنشاء وتكوين مشروع Freestyle
مشاريع Freestyle مباشرة وتستخدم واجهة مستخدم رسومية (GUI) لتكوين الخطوات. إنها رائعة للمبتدئين أو للمهام البسيطة مثل بناء واختبار الكود.

1.  **إنشاء وظيفة جديدة**:
    *   من لوحة تحكم Jenkins، انقر على **New Item** في الشريط الجانبي الأيسر.
    *   أدخل اسمًا للوظيفة الخاصة بك (على سبيل المثال، "MyFirstBuild").
    *   اختر **Freestyle project** ثم انقر على **OK**.

2.  **الإعدادات العامة**:
    *   أضف وصفًا للوظيفة.
    *   يمكنك تفعيل ميزات مثل **تجاهل عمليات البناء القديمة** (على سبيل المثال، الاحتفاظ بـ 10 عمليات بناء الأخيرة فقط) أو إضافة **معلمات** (على سبيل المثال، معلمات نصية أو اختيارية لإدخال المستخدم أثناء البناء).

3.  **إدارة كود المصدر**:
    *   اختر أداة إدارة كود المصدر (SCM) الخاصة بك، مثل Git.
    *   أدخل عنوان URL للمستودع (على سبيل المثال، مستودع GitHub).
    *   أضف بيانات الاعتماد إذا لزم الأمر (على سبيل المثال، اسم مستخدم/كلمة مرور أو مفتاح SSH).
    *   حدد الفروع المطلوب بناؤها (على سبيل المثال، `*/main`).

4.  **مشغلات البناء**:
    *   اختر كيفية بدء الوظيفة، مثل:
        *   **Build periodically** (على سبيل المثال، باستخدام صيغة cron مثل `H/5 * * * *` لكل 5 دقائق).
        *   **Poll SCM** للتحقق من وجود تغييرات.
        *   **GitHub hook trigger** لاستخدام webhooks من GitHub.
        *   **Build after other projects** لربط الوظائف ببعضها.

5.  **بيئة البناء**:
    *   حدد خيارات مثل **Delete workspace before build starts** للحصول على بيئة نظيفة.
    *   أضف طابعًا زمنيًا لناتج console أو عيّن متغيرات بيئة.

6.  **خطوات البناء**:
    *   انقر على **Add build step** واختر إجراءات مثل:
        *   **Execute shell** (لـ Linux/Mac: على سبيل المثال، `echo "Hello World"` أو تشغيل سكريبتات).
        *   **Invoke top-level Maven targets** لبناء Java.
        *   **Execute Windows batch command** لـ Windows.
    *   يمكنك إضافة خطوات متعددة تعمل بالتسلسل.

7.  **إجراءات ما بعد البناء**:
    *   أضف إجراءات مثل:
        *   **Archive the artifacts** (على سبيل المثال، حفظ ملفات JAR).
        *   **Publish JUnit test result report**.
        *   **Send email notifications** عند النجاح/الفشل.
        *   **Trigger another project**.

8.  **حفظ وتشغيل**:
    *   انقر على **Save**.
    *   عد إلى صفحة الوظيفة، وانقر على **Build Now** لاختبارها.
    *   اعرض ناتج console للاطلاع على التفاصيل.

#### خطوات إنشاء وتكوين مشروع Pipeline
تُعرّف Pipelines ككود (تصريحية أو مسيّرة) وهي أكثر مرونة لسير عمل CI/CD.

1.  **إنشاء وظيفة جديدة**:
    *   من لوحة التحكم، انقر على **New Item**.
    *   أدخل اسمًا واختر **Pipeline**، ثم **OK**.

2.  **الإعدادات العامة**:
    *   مشابه لـ Freestyle: أضف وصفًا، معلمات، إلخ.

3.  **مشغلات البناء**:
    *   نفس الخيارات المتاحة في Freestyle (على سبيل المثال، webhooks، جداول زمنية).

4.  **تعريف Pipeline**:
    *   اختر **Pipeline script** للكتابة المضمنة أو **Pipeline script from SCM** للسحب من مستودع (على سبيل المثال، ملف `Jenkinsfile` في Git).
    *   مثال على سكريبت pipeline تصريحي:
        ```
        pipeline {
            agent any
            stages {
                stage('Build') {
                    steps {
                        echo 'Building...'
                        sh 'mvn clean install'  // مثال لبناء Maven
                    }
                }
                stage('Test') {
                    steps {
                        echo 'Testing...'
                        sh 'mvn test'
                    }
                }
                stage('Deploy') {
                    steps {
                        echo 'Deploying...'
                    }
                }
            }
            post {
                always {
                    echo 'This runs always'
                }
            }
        }
        ```
    *   هذا يُعرّف مراحل (Build, Test, Deploy) مع خطوات.

5.  **حفظ وتشغيل**:
    *   احفظ الوظيفة.
    *   شغّلها وراقب عرض pipeline لمتابعة تقدم المراحل.

يحتوي Jenkins على العديد من الخيارات في كل قسم، لذا استكشف بناءً على احتياجاتك (على سبيل المثال، للأمان، أضف بيانات اعتماد؛ للتشغيل المتوازي، استخدم وكلاء/عُقد). إذا كنت جديدًا على Jenkins، ابدأ بـ Freestyle ثم انتقل إلى Pipelines للحصول على قابلية التوسع.

### تكاملات البرامج والتعاون مع Jenkins

يتمتع Jenkins بقابلية عالية للتوسع من خلال **الإضافات** (أكثر من 2000 إضافة متاحة)، مما يسمح له بالتكامل مع أي أداة تقريبًا في نظام DevOps. تمكن هذه التكاملات من تشغيل عمليات البناء، والنشر، والاختبار، والإشعارات، والمزيد. يمكن تثبيت الإضافات عبر **Manage Jenkins > Manage Plugins**.

#### التكاملات الشائعة حسب الفئة
*   **التحكم في الإصدار**: Git، GitHub، GitLab، Bitbucket، SVN – لسحب الكود وتشغيل عمليات البناء عند عمليات commit/push باستخدام webhooks.
*   **الحاوية والتنسيق**: Docker (بناء/رفع الصور)، Kubernetes (النشر إلى المجموعات)، Helm – لسير العمل القائمة على الحاويات.
*   **مزودو السحابة**: AWS (EC2، S3، Lambda عبر الإضافات)، Azure، Google Cloud – للنشر إلى البنية التحتية السحابية.
*   **الاختبار والجودة**: SonarQube (فحوصات جودة الكود)، Selenium (اختبار واجهة المستخدم)، JUnit (اختبارات الوحدة)، Cucumber (BDD) – دمجها في خطوات البناء للاختبار الآلي.
*   **النشر والمراقبة**: Ansible، Terraform (البنية التحتية ككود)، Prometheus، Grafana – للتنسيق والمراقبة بعد البناء.
*   **الإشعارات والتعاون**: Slack، Microsoft Teams، البريد الإلكتروني، Jira، Trello – إرسال تنبيهات أو تحديث التذاكر حول حالة البناء.
*   **أدوات البناء**: Maven، Gradle (Java)، npm (Node.js)، pip (Python) – تنفيذ عمليات البناء للغات مختلفة.
*   **الأمان**: OWASP Dependency-Check، Trivy (فحص الثغرات) – فحص المشكلات أثناء CI.
*   **أخرى**: Artifactory/Nexus (مستودعات القطع الأثرية)، Zapier (تكاملات no-code)، Octopus Deploy (عمليات نشر متقدمة).

على سبيل المثال، مع GitHub، قم بتثبيت إضافة GitHub لتمكين مشغلات webhook. مع Docker، استخدم إضافة Docker Pipeline لبناء الصور في pipelines. حتى أنه يمكن إنشاء إضافات مخصصة للأدوات المتخصصة.

لاستكشاف المزيد، تحقق من فهرس الإضافات الرسمي. قم دائمًا بتحديث الإضافات بانتظام لأسباب أمنية.

#### المراجع
*   [Working with projects - Jenkins](https://www.jenkins.io/doc/book/using/working-with-projects/)
*   [Jenkins - Setup Build Jobs - Tutorials Point](https://www.tutorialspoint.com/jenkins/jenkins_setup_build_jobs.htm)
*   [How to Create and Configure Build Jobs in Jenkins | BrowserStack](https://www.browserstack.com/guide/build-jobs-in-jenkins)
*   [Jenkins Build: Set Up Freestyle Project in Jenkins {Step-by-Step}](https://phoenixnap.com/kb/jenkins-build-freestyle-project)
*   [Managing Plugins - Jenkins](https://www.jenkins.io/doc/book/managing/plugins/)
*   [How to Integrate Jenkins with Different Tools and Technologies?](https://www.addwebsolution.com/blog/integrating-jenkins-with-other-tools-and-technologies)
*   [Jenkins Plugins](https://plugins.jenkins.io/)
*   [Jenkins](https://www.jenkins.io/)
*   [10 Of Our Favorite Jenkins Plugins | Octopus blog](https://octopus.com/blog/jenkins-ten-plugins)