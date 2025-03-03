---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Azure DevOps Pipelines
translated: true
---

نحن سنقسم هذا إلى قسمين: **استخدام Azure DevOps Pipelines** و **كتابة YAML للممرات**. سأقدم شرحًا واضحًا وممارسًا لكل منهما.

---

### **كيفية استخدام Azure DevOps Pipelines**
Azure DevOps Pipelines هو أداة CI/CD (الدمج المستمر/التوزيع المستمر) التي تتيح لك التلقائي بناء، اختبار، وتوزيع الكود. إليك كيفية البدء:

#### **1. إعداد مشروع**
- قم بتسجيل الدخول إلى Azure DevOps (dev.azure.com) باستخدام منظمة.
- انشئ مشروعًا جديدًا (أو استخدم مشروعًا موجودًا) من خلال النقر على "New Project"، وتحديد اسم، وإعداد الرؤية (عام/خاص).

#### **2. ربط الكود**
- انتقل إلى **Repos** في مشروعك واذهب إلى مخزن الكود (GitHub, Azure Repos, Bitbucket, إلخ.).
- أو ربط مخزن خارجي تحت **Pipelines > New Pipeline > Connect** واختر مصدرك.

#### **3. إنشاء ممر**
- انتقل إلى **Pipelines > Builds > New Pipeline**.
- اختر مخزنك وفروعك.
- يوفر Azure خيارين:
  - **Classic Editor**: طريقة مستندة على GUI (لا تحتاج إلى YAML).
  - **YAML**: ممر مستند على الكود (موصى به من أجل المرونة والتحكم في الإصدارات).
- بالنسبة إلى YAML، اختر "Starter pipeline" أو قم بتكوين من ملف موجود في مخزنك.

#### **4. تعريف الممر**
- إذا كنت تستخدم YAML، فستكتب ملفًا `.yml` (مثل `azure-pipelines.yml`) في جذور مخزنك. (سأشرح المزيد عن ذلك أدناه.)
- أضف مثيرات (مثل تشغيل عند كل دفع إلى `main`), خطوات (مثل بناء، اختبار)، وأهداف التوزيع.

#### **5. تشغيل و مراقبة**
- احفظ واذهب إلى YAML الملف (أو احفظ في Classic Editor).
- انقر على **Run** لتشغيل الممر يدويًا، أو دعه يعمل تلقائيًا بناءً على المثيرات.
- تحقق من السجلات تحت **Pipelines > Builds** لمتابعة التقدم أو حل المشاكل.

#### **6. توزيع (اختياري)**
- أضف ممر **release** (تحت **Releases**) أو توسع YAML لتوزيع إلى بيئات مثل Azure App Service, Kubernetes, أو VMs.

---

### **كيفية كتابة YAML لممرات Azure Pipelines**
YAML (لغة ترميز أخرى) هي صيغة قابلة للقراءة من قبل الإنسان تستخدم لتحديد تكوين الممرات. إليك دورة سريعة:

#### **الهيكل الأساسي**
```yaml
trigger:
  - main  # تشغيل الممر عند تحديث فرع 'main'

pool:
  vmImage: 'ubuntu-latest'  # تحديد صورة آلة افتراضية للممر (مثل Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # أمر بسيط للتنفيذ
    displayName: 'Run a one-line script'
```

- **`trigger`**: يحدد متى يعمل الممر (مثل دفع إلى `main`).
- **`pool`**: يحدد صورة آلة افتراضية للممر.
- **`steps`**: يحدد المهام للتنفيذ (أوامر، مهام مدمجة، إلخ.).

#### **عناصر شائعة**
1. **المتغيرات**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # يخرج 'Release'
   ```

2. **الأعمال** (تجميع الخطوات):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **المهام** (أفعال مدمجة مسبقًا):
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # مثال: بناء مشروع .NET
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **الشروط**:
   ```yaml
   steps:
     - script: echo This runs only on main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **المراحل** (لممرات متعددة المراحل):
   ```yaml
   stages:
   - stage: Build
     jobs:
       - job: BuildJob
         steps:
           - script: echo Building...
   - stage: Deploy
     dependsOn: Build
     jobs:
       - job: DeployJob
         steps:
           - script: echo Deploying...
   ```

#### **مثال واقعي**
هنا ممر لبرنامج Node.js:
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # تثبيت Node.js
    inputs:
      versionSpec: '16.x'
    displayName: 'Install Node.js'

  - script: |
      npm install
      npm run build
    displayName: 'Install and Build'

  - task: CopyFiles@2  # نسخ منتجات البناء
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # نشر المنتجات
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **نصائح لكتابة YAML**
- استخدم التباين المتساوي (2 مسافات، لا تبويبات).
- تحقق من صحة الصيغة باستخدام محرر (مثل VS Code مع امتداد "YAML").
- استعرض [مخطط YAML لممرات Azure](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) للحصول على الخيار.
- ابدأ ببساطة، ثم أضف التعقيد (مثل المراحل، المتغيرات) حسب الحاجة.

---

### **الخطوات التالية**
- **حاول**: انشئ مخزن، أضف `azure-pipelines.yml` أساسيًا مثل المثال أعلاه، واذهب إلى Azure DevOps.
- **تعلم المزيد**: استعرض وثائق Microsoft [الرسمية](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) أو ابحث عن ممرات عينة على GitHub.
- **اسألني**: إذا واجهت مشكلة أو كنت تريد مثالًا معينًا (مثل Python, Java)، أخبرني!

ماذا تريد أن تنزلق إلى عمقه؟ إعداد ممر، صيغة YAML، أو شيء آخر؟