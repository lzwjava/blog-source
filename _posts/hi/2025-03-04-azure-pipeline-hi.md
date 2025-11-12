---
audio: false
generated: true
lang: hi
layout: post
title: एज़्योर डेवऑप्स पाइपलाइन्स का उपयोग
translated: true
type: note
---

आइए इसे दो भागों में समझते हैं: **Azure DevOps Pipelines का उपयोग** और **पाइपलाइनों के लिए YAML लिखना**। मैं दोनों के लिए एक स्पष्ट, व्यावहारिक व्याख्या प्रदान करूंगा।

---

### **Azure DevOps Pipelines का उपयोग कैसे करें**
Azure DevOps Pipelines एक CI/CD (Continuous Integration/Continuous Deployment) टूल है जो कोड के निर्माण, परीक्षण और तैनाती को स्वचालित करता है। यहां बताया गया है कि कैसे शुरुआत करें:

#### **1. एक प्रोजेक्ट सेट अप करें**
- अपने संगठन के साथ Azure DevOps (dev.azure.com) में लॉग इन करें।
- "New Project" पर क्लिक करके, उसे एक नाम देकर और दृश्यता (सार्वजनिक/निजी) सेट करके एक नया प्रोजेक्ट बनाएं (या मौजूदा का उपयोग करें)।

#### **2. अपने कोड को कनेक्ट करें**
- अपने प्रोजेक्ट में **Repos** पर जाएं और अपने कोड को एक रिपॉजिटरी (GitHub, Azure Repos, Bitbucket, आदि) में पुश करें।
- वैकल्पिक रूप से, **Pipelines > New Pipeline > Connect** के तहत एक बाहरी रिपो को लिंक करें और अपना स्रोत चुनें।

#### **3. एक पाइपलाइन बनाएं**
- **Pipelines** > **Builds** > **New Pipeline** पर नेविगेट करें।
- अपना रिपो और ब्रांच चुनें।
- Azure दो विकल्प प्रदान करता है:
  - **Classic Editor**: एक GUI-आधारित दृष्टिकोण (YAML की आवश्यकता नहीं)।
  - **YAML**: एक कोड-आधारित पाइपलाइन (लचीलापन और संस्करण नियंत्रण के लिए अनुशंसित)।
- YAML के लिए, "Starter pipeline" चुनें या अपने रिपो में मौजूदा फ़ाइल से कॉन्फ़िगर करें।

#### **4. पाइपलाइन को परिभाषित करें**
- यदि YAML का उपयोग कर रहे हैं, तो आप अपने रिपो की रूट में एक `.yml` फ़ाइल (उदाहरण के लिए, `azure-pipelines.yml`) लिखेंगे। (इस पर नीचे और अधिक जानकारी।)
- ट्रिगर्स (जैसे, `main` पर हर पुश पर चलना), स्टेप्स (जैसे, बिल्ड, टेस्ट), और डिप्लॉयमेंट टार्गेट जोड़ें।

#### **5. रन करें और मॉनिटर करें**
- YAML फ़ाइल को सेव और कमिट करें (या Classic Editor में सेव करें)।
- पाइपलाइन को मैन्युअल रूप से ट्रिगर करने के लिए **Run** पर क्लिक करें, या ट्रिगर्स के आधार पर इसे स्वचालित रूप से चलने दें।
- प्रगति की निगरानी करने या विफलताओं का समाधान करने के लिए **Pipelines > Builds** के तहत लॉग्स जांचें।

#### **6. डिप्लॉय करें (वैकल्पिक)**
- एक **रिलीज़ पाइपलाइन** (**Releases** के तहत) जोड़ें या Azure App Service, Kubernetes, या VMs जैसे वातावरणों में तैनाती करने के लिए अपने YAML को विस्तारित करें।

---

### **Azure Pipelines के लिए YAML कैसे लिखें**
YAML (Yet Another Markup Language) एक मानव-पठनीय प्रारूप है जिसका उपयोग पाइपलाइन कॉन्फ़िगरेशन को परिभाषित करने के लिए किया जाता है। यहां एक क्रैश कोर्स दिया गया है:

#### **बुनियादी संरचना**
```yaml
trigger:
  - main  # पाइपलाइन चलाएं जब 'main' ब्रांच अपडेट हो

pool:
  vmImage: 'ubuntu-latest'  # बिल्ड एजेंट निर्दिष्ट करें (उदाहरण के लिए, Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # चलाने के लिए एक साधारण कमांड
    displayName: 'Run a one-line script'
```

- **`trigger`**: परिभाषित करता है कि पाइपलाइन कब चलती है (जैसे, `main` पर पुश होने पर)।
- **`pool`**: बिल्ड एजेंट के लिए वर्चुअल मशीन इमेज निर्दिष्ट करता है।
- **`steps`**: निष्पादित करने के लिए कार्यों की सूची बनाता है (स्क्रिप्ट्स, बिल्ट-इन टास्क्स, आदि)।

#### **सामान्य तत्व**
1. **Variables**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # 'Release' आउटपुट करता है
   ```

2. **Jobs** (समूह चरण):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **Tasks** (पूर्व-निर्मित क्रियाएं):
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # उदाहरण: एक .NET प्रोजेक्ट बनाएं
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **Conditions**:
   ```yaml
   steps:
     - script: echo This runs only on main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **Stages** (बहु-चरण पाइपलाइनों के लिए):
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

#### **वास्तविक दुनिया का उदाहरण**
यहां एक Node.js ऐप के लिए एक पाइपलाइन है:
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # Node.js इंस्टॉल करें
    inputs:
      versionSpec: '16.x'
    displayName: 'Install Node.js'

  - script: |
      npm install
      npm run build
    displayName: 'Install and Build'

  - task: CopyFiles@2  # बिल्ड आर्टिफैक्ट्स कॉपी करें
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # आर्टिफैक्ट्स प्रकाशित करें
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **YAML लिखने के लिए टिप्स**
- सुसंगत इंडेंटेशन का उपयोग करें (2 स्पेस, टैब नहीं)।
- एक एडिटर (जैसे, "YAML" एक्सटेंशन के साथ VS Code) के साथ सिंटैक्स वैलिडेट करें।
- विकल्पों के लिए [Azure Pipelines YAML schema](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) देखें।
- सरल शुरुआत करें, फिर आवश्यकतानुसार जटिलता जोड़ें (जैसे, स्टेजेस, वेरिएबल्स)।

---

### **अगले कदम**
- **इसे आज़माएं**: एक रिपो बनाएं, ऊपर दिए गए जैसी एक बुनियादी `azure-pipelines.yml` जोड़ें, और इसे Azure DevOps में चलाएं।
- **और जानें**: Microsoft के [आधिकारिक दस्तावेज़](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) देखें या GitHub पर नमूना पाइपलाइनों की खोज करें।
- **मुझसे पूछें**: यदि आपको कोई समस्या आती है या आप एक विशिष्ट उदाहरण चाहते हैं (जैसे, Python, Java), तो मुझे बताएं!

आप और गहराई से किस पर जाना चाहेंगे? पाइपलाइन सेट अप करना, YAML सिंटैक्स, या कुछ और?