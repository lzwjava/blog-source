---
audio: false
generated: true
lang: ar
layout: post
title: استخدام خطوط أنابيب Azure DevOps
translated: true
type: note
---

لنقسم هذا إلى جزأين: **استخدام Azure DevOps Pipelines** و**كتابة YAML للأنابيب**. سأقدم شرحًا واضحًا وعمليًا لكليهما.

---

### **كيفية استخدام Azure DevOps Pipelines**
Azure DevOps Pipelines هو أداة CI/CD (التكامل المستمر/التوزيع المستمر) تؤتمت عملية بناء واختبار ونشر الكود. إليك كيفية البدء:

#### **1. إعداد مشروع**
- سجل الدخول إلى Azure DevOps (dev.azure.com) باستخدام مؤسستك.
- أنشئ مشروعًا جديدًا (أو استخدم مشروعًا موجودًا) بالنقر على "New Project"، وإعطائه اسمًا، وضبط الرؤية (عام/خاص).

#### **2. ربط الكود الخاص بك**
- انتقل إلى **Repos** في مشروعك وادفع الكود الخاص بك إلى مستودع (مثل GitHub، أو Azure Repos، أو Bitbucket، إلخ).
- بدلاً من ذلك، يمكنك ربط مستودع خارجي من خلال **Pipelines > New Pipeline > Connect** واختيار المصدر الخاص بك.

#### **3. إنشاء خط أنابيب**
- انتقل إلى **Pipelines** > **Builds** > **New Pipeline**.
- اختر المستودع والفرع الخاصين بك.
- يقدم Azure خيارين:
  - **Classic Editor**: نهج قائم على واجهة المستخدم الرسومية (لا حاجة لـ YAML).
  - **YAML**: خط أنابيب قائم على الكود (موصى به للمرونة والتحكم في الإصدار).
- لـ YAML، اختر "Starter pipeline" أو قم بالتكوين من ملف موجود في مستودعك.

#### **4. تعريف خط الأنابيب**
- إذا كنت تستخدم YAML، ستقوم بكتابة ملف `.yml` (مثل `azure-pipelines.yml`) في جذر مستودعك. (المزيد عن هذا لاحقًا).
- أضف المحفزات (مثل التشغيل عند كل دفع إلى فرع `main`)، والخطوات (مثل البناء، الاختبار)، وأهداف النشر.

#### **5. التشغيل والمراقبة**
- احفظ وارفع ملف YAML (أو احفظه في Classic Editor).
- انقر على **Run** لتفعيل خط الأنابيب يدويًا، أو اتركه يعمل تلقائيًا بناءً على المحفزات.
- تحقق من السجلات في **Pipelines > Builds** لمراقبة التقدم أو استكشاف الأخطاء وإصلاحها.

#### **6. النشر (اختياري)**
- أضف **Release Pipeline** (ضمن **Releases**) أو وسع تعريف YAML الخاص بك للنشر إلى بيئات مثل Azure App Service، أو Kubernetes، أو الأجهزة الظاهرية.

---

### **كيفية كتابة YAML لـ Azure Pipelines**
YAML (Yet Another Markup Language) هو تنسيق قابل للقراءة البشرية يستخدم لتعريف تكوينات خطوط الأنابيب. إليك دورة مكثفة:

#### **الهيكل الأساسي**
```yaml
trigger:
  - main  # تشغيل خط الأنابيب عند تحديث فرع 'main'

pool:
  vmImage: 'ubuntu-latest'  # حدد عامل البناء (مثل Ubuntu، Windows، macOS)

steps:
  - script: echo Hello, world!  # أمر بسيط للتشغيل
    displayName: 'تشغيل سكريبت من سطر واحد'
```

- **`trigger`**: يحدد متى يعمل خط الأنابيب (مثلًا عند الدفع إلى `main`).
- **`pool`**: يحدد صورة الجهاز الظاهري لعامل البناء.
- **`steps`**: يسرد المهام التي سيتم تنفيذها (مثل السكريبتات، المهام المدمجة، إلخ).

#### **العناصر الشائعة**
1. **المتغيرات**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # يخرج 'Release'
   ```

2. **الوظائف** (تجميع الخطوات):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **المهام** (إجراءات مسبقة البناء):
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

5. **المراحل** (لخطوط الأنابيب متعددة المراحل):
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

#### **مثال من العالم الحقيقي**
إليك خط أنابيب لتطبيق Node.js:
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # تثبيت Node.js
    inputs:
      versionSpec: '16.x'
    displayName: 'تثبيت Node.js'

  - script: |
      npm install
      npm run build
    displayName: 'التثبيت والبناء'

  - task: CopyFiles@2  # نسخ نتائج البناء
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # نشر نتائج البناء
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **نصائح لكتابة YAML**
- استخدم مسافة بادئة متسقة (مسافتان، بدون علامات Tab).
- تحقق من صحة التركيب باستخدام محرر (مثل VS Code مع إضافة "YAML").
- راجع [YAML schema لـ Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) للاطلاع على الخيارات.
- ابدأ بالبسيط، ثم أضف التعقيد (مثل المراحل، المتغيرات) حسب الحاجة.

---

### **الخطوات التالية**
- **جربه**: أنشئ مستودعًا، أضف ملف `azure-pipelines.yml` أساسيًا مثل المذكور أعلاه، وشغله في Azure DevOps.
- **تعلم المزيد**: راجع [الوثائق الرسمية من Microsoft](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) أو ابحث عن أمثلة لخطوط الأنابيب على GitHub.
- **اسألني**: إذا واجهت مشكلة أو أردت مثالًا محددًا (مثل Python، Java)، دعني أعرف!

إلى ماذا تريد التعمق أكثر؟ إعداد خط أنابيب، تركيب YAML، أم شيء آخر؟