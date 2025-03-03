---
audio: false
generated: true
lang: hi
layout: post
title: Azure DevOps Pipelines का उपयोग
translated: true
---

इसको दो हिस्सों में तोड़ें: **Azure DevOps Pipelines का उपयोग** और **पाइपलाइन्स के लिए YAML लिखना**. मैं दोनों के लिए एक स्पष्ट, व्यावहारिक व्याख्या प्रदान करूँगा।

---

### **Azure DevOps Pipelines का उपयोग कैसे करें**

Azure DevOps Pipelines एक CI/CD (Continuous Integration/Continuous Deployment) टूल है जो कोड को बनाना, टेस्ट करना और डिप्लॉय करना स्वचालित करता है। यहाँ शुरू करने के लिए:

#### **1. एक प्रोजेक्ट सेट अप करें**
- अपने संगठन के साथ Azure DevOps (dev.azure.com) में लॉग इन करें।
- "नया प्रोजेक्ट" पर क्लिक करके एक नया प्रोजेक्ट बनाएं (या मौजूदा का उपयोग करें), इसे नाम दें और दृश्यता (सार्वजनिक/निजी) सेट करें।

#### **2. अपने कोड को कनेक्ट करें**
- अपने प्रोजेक्ट में **Repos** जाएं और अपने कोड को एक रिपोजिटरी (GitHub, Azure Repos, Bitbucket, आदि) में पुश करें।
- या, एक बाहरी रिपोजिटरी को **Pipelines > New Pipeline > Connect** के नीचे लिंक करें और अपना स्रोत चुनें।

#### **3. एक पाइपलाइन बनाएं**
- **Pipelines > Builds > New Pipeline** पर जाएं।
- अपना रिपोजिटरी और ब्रांच चुनें।
- Azure दो विकल्प प्रदान करता है:
  - **Classic Editor**: एक GUI-based approach (YAML की आवश्यकता नहीं).
  - **YAML**: एक कोड-आधारित पाइपलाइन (लचीलापन और वर्सन नियंत्रण के लिए अनुशंसित).
- YAML के लिए, "Starter pipeline" चुनें या अपने रिपोजिटरी में मौजूद एक फाइल से कॉन्फ़िगर करें।

#### **4. पाइपलाइन को परिभाषित करें**
- YAML का उपयोग करते हुए, आप अपने रिपोजिटरी के रूट में एक `.yml` फाइल (e.g., `azure-pipelines.yml`) लिखेंगे। (इसके बारे में नीचे अधिक जानकारी मिलेगी.)
- ट्रिगर्स (e.g., हर बार `main` पर पुश करने पर चलाएं), स्टेप्स (e.g., बनाएं, टेस्ट करें), और डिप्लॉयमेंट टारगेट्स जोड़ें।

#### **5. चलाएं और निगरानी करें**
- YAML फाइल को सेट और कमिट करें (या Classic Editor में सेट करें).
- पाइपलाइन को मैन्युअल रूप से ट्रिगर करने के लिए **Run** पर क्लिक करें, या ट्रिगर्स के आधार पर इसे स्वचालित रूप से चलने दें।
- **Pipelines > Builds** के नीचे लॉग्स देखें ताकि प्रगति को निगरानी करें या विफलताओं को ट्रबलशूट करें।

#### **6. डिप्लॉय करें (वैकल्पिक)**
- एक **रिलीज़ पाइपलाइन** बनाएं (**Releases** के नीचे) या अपने YAML को Azure App Service, Kubernetes, या VMs जैसे पर्यावरणों में डिप्लॉय करने के लिए विस्तारित करें।

---

### **Azure Pipelines के लिए YAML कैसे लिखें**

YAML (Yet Another Markup Language) एक मानव-पढ़ने योग्य प्रारूप है जो पाइपलाइन कॉन्फ़िगरेशन को परिभाषित करने के लिए उपयोग किया जाता है। यहाँ एक क्रैश कोर्स है:

#### **बेसिक स्ट्रक्चर**
```yaml
trigger:
  - main  # पाइपलाइन को 'main' ब्रांच अपडेट होने पर चलाएं

pool:
  vmImage: 'ubuntu-latest'  # बिल्ड एजेंट के लिए वर्चुअल मशीन इमेज (e.g., Ubuntu, Windows, macOS) को परिभाषित करें

steps:
  - script: echo Hello, world!  # एक सरल कमांड चलाएं
    displayName: 'Run a one-line script'
```

- **`trigger`**: पाइपलाइन को कब चलाएं (e.g., `main` पर पुश करने पर).
- **`pool`**: बिल्ड एजेंट के लिए वर्चुअल मशीन इमेज को परिभाषित करता है।
- **`steps`**: कार्यान्वयन करने के लिए टास्क्स की सूची (स्क्रिप्ट, बिल्ट-इन टास्क्स, आदि)।

#### **सामान्य तत्व**
1. **Variables**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # 'Release' को आउटपुट करता है
   ```

2. **Jobs** (स्टेप्स को समूहित करें):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **Tasks** (प्री-बिल्ट एक्शन):
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

5. **Stages** (बहु-फेज पाइपलाइन्स के लिए):
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
यह एक Node.js ऐप के लिए पाइपलाइन है:
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

  - task: CopyFiles@2  # बिल्ड आर्टिफैक्ट्स को कॉपी करें
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # आर्टिफैक्ट्स को प्रकाशित करें
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **YAML लिखने के लिए टिप्स**
- एकसमान इंडेंटेशन का उपयोग करें (2 स्पेस, टैब नहीं).
- एक संपादक (e.g., VS Code के साथ "YAML" एक्सटेंशन) के साथ सिंटैक्स को वैलिडेट करें।
- [Azure Pipelines YAML schema](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) के लिए विकल्पों का संदर्भ लेना।
- सरल से शुरू करें, फिर आवश्यकता के अनुसार जटिलता (e.g., स्टेज, वेरिएबल्स) जोड़ें।

---

### **अगले कदम**
- **इसको ट्राई करें**: एक रिपोजिटरी बनाएं, ऊपर दिए गए जैसा एक बेसिक `azure-pipelines.yml` जोड़ें और Azure DevOps में इसे चलाएं।
- **अधिक सीखें**: Microsoft के [अधिकारिक दस्तावेज़](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) देखें या GitHub पर सैंपल पाइपलाइन्स खोजें।
- **मुझे पूछें**: अगर आप किसी बाधा में फंस जाते हैं या किसी विशेष उदाहरण (e.g., Python, Java) की आवश्यकता होती है, मुझे बताएं!

आप क्या गहरे में जाना चाहते हैं? एक पाइपलाइन सेट अप करना, YAML सिंटैक्स, या कुछ और?