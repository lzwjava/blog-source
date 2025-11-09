---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एज़्योर सीएलआई क्विक स्टार्ट गाइड
translated: true
type: note
---

Azure CLI (कमांड-लाइन इंटरफ़ेस) एक क्रॉस-प्लेटफ़ॉर्म टूलसेट है जो Azure संसाधनों को कमांड लाइन से प्रबंधित करने के लिए है। यह कार्यों को स्वचालित करने, तैनाती स्क्रिप्टिंग और वेब पोर्टल की आवश्यकता के बिना Azure सेवाओं के साथ इंटरैक्ट करने के लिए आदर्श है। यह Windows, macOS और Linux पर Bash, PowerShell और Command Prompt का समर्थन करता है।

## इंस्टालेशन

1. **पूर्वापेक्षाएँ**: सुनिश्चित करें कि आपके पास Python 3.8 या बाद का संस्करण इंस्टॉल है (`python --version` से जाँचें)।

2. **पैकेज मैनेजर के माध्यम से इंस्टॉल करें** (अनुशंसित):
   - **Windows**: Winget (`winget install Microsoft.AzureCLI`) या Chocolatey (`choco install azure-cli`) का उपयोग करें।
   - **macOS**: Homebrew (`brew install azure-cli`) का उपयोग करें।
   - **Linux (Ubuntu/Debian)**: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash` चलाएँ।
   - **अन्य Linux**: RPM या आधिकारिक साइट से मैन्युअल डाउनलोड का उपयोग करें।

3. **इंस्टालेशन सत्यापित करें**: एक टर्मिनल खोलें और `az --version` चलाएँ। आपको CLI संस्करण दिखाई देना चाहिए (उदाहरण के लिए, 2025 के अंत तक 2.64.0)।

विस्तृत प्लेटफ़ॉर्म-विशिष्ट चरणों के लिए, आधिकारिक इंस्टालेशन दस्तावेज़ देखें।

## प्रमाणीकरण

Azure CLI का उपयोग करने से पहले, अपने Azure अकाउंट में साइन इन करें:

1. **इंटरैक्टिव लॉगिन**: `az login` चलाएँ। यह Microsoft Entra ID प्रमाणीकरण के लिए एक ब्राउज़र खोलता है। साइन इन करने के लिए संकेतों का पालन करें।

2. **सर्विस प्रिंसिपल (स्वचालन के लिए)**: `az ad sp create-for-rbac --name "MyApp" --role contributor --scopes /subscriptions/{subscription-id}` के साथ एक सर्विस प्रिंसिपल बनाएँ। फिर `az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>` का उपयोग करें।

3. **लॉगिन जाँचें**: अपने सक्रिय सब्सक्रिप्शन को सत्यापित करने के लिए `az account show` का उपयोग करें।

4. **लॉगआउट**: `az logout`।

मल्टी-फ़ैक्टर प्रमाणीकरण (MFA) समर्थित है, और आप `az account set --subscription <id>` के साथ कई सब्सक्रिप्शन प्रबंधित कर सकते हैं।

## बेसिक कमांड्स

Azure CLI `az` कमांड का उपयोग करता है, जिसके बाद एक समूह (जैसे `vm`, `storage`) और उप-कमांड आते हैं। अवलोकन के लिए `az --help` का उपयोग करें, या विशिष्ट जानकारी के लिए `az <group> --help` का उपयोग करें।

### सामान्य ग्लोबल विकल्प
- `--help` या `-h`: सहायता दिखाएँ।
- `--output table/json/yaml`: आउटपुट फ़ॉर्मेट करें (डिफ़ॉल्ट: table)।
- `--query`: JSON आउटपुट को फ़िल्टर करने के लिए JMESPath क्वेरी (उदाहरण के लिए, `--query "[].name"`)।

### मुख्य उदाहरण
- **सब्सक्रिप्शन सूचीबद्ध करें**: `az account list --output table`
- **रिसोर्स ग्रुप प्राप्त करें**: `az group list --output table`
- **एक रिसोर्स ग्रुप बनाएँ**: `az group create --name "MyResourceGroup" --location "eastus"`

## वर्चुअल मशीन (VM) प्रबंधन
Azure CLI VM लाइफ़साइकल प्रबंधन में उत्कृष्ट है।

1. **एक VM बनाएँ**:
   ```
   az vm create \
     --resource-group "MyResourceGroup" \
     --name "MyVM" \
     --image Ubuntu2204 \
     --admin-username azureuser \
     --admin-password MyP@ssw0rd123! \
     --location "eastus"
   ```

2. **VM सूचीबद्ध करें**: `az vm list --output table`

3. **VM स्टार्ट/स्टॉप करें**: `az vm start --name "MyVM" --resource-group "MyResourceGroup"` या `az vm stop --name "MyVM" --resource-group "MyResourceGroup"`

4. **VM में SSH करें**: `az vm ssh "MyVM" --resource-group "MyResourceGroup"`

5. **VM डिलीट करें**: `az vm delete --name "MyVM" --resource-group "MyResourceGroup" --yes`

## स्टोरेज अकाउंट प्रबंधन
1. **स्टोरेज अकाउंट बनाएँ**:
   ```
   az storage account create \
     --name mystorageaccount \
     --resource-group "MyResourceGroup" \
     --location "eastus" \
     --sku Standard_LRS
   ```

2. **ब्लॉब अपलोड करें**: पहले, `az storage account keys list --account-name mystorageaccount --resource-group "MyResourceGroup" --query "[0].value -o tsv"` के साथ कुंजी प्राप्त करें। फिर: `az storage blob upload --account-name mystorageaccount --container-name mycontainer --name myfile.txt --file ./myfile.txt --auth-mode key`

## अन्य सामान्य परिदृश्य
- **ARM टेम्प्लेट तैनात करें**: `az deployment group create --resource-group "MyResourceGroup" --template-file template.json`
- **संसाधन क्वेरी करें**: `az resource list --resource-group "MyResourceGroup" --output table`
- **CLI अपडेट करें**: `az upgrade`
- **एक्सटेंशन**: अतिरिक्त कमांड्स के लिए `az extension add --name azure-devops` जैसे एक्सटेंशन इंस्टॉल करें।

स्क्रिप्टिंग के लिए, Bash/PowerShell लूप्स के साथ संयोजित करें या CI/CD पाइपलाइन्स जैसे GitHub Actions में Azure CLI का उपयोग करें।

## टिप्स और बेस्ट प्रैक्टिसेज़
- पूर्वावलोकन के लिए `--dry-run` का उपयोग करें (जहाँ समर्थित हो)।
- ऑटो-कम्प्लीशन सक्षम करें: Bash पर, `az completion` चलाएँ।
- त्रुटियों को हैंडल करें: एक्ज़िट कोड जाँचें (सफलता के लिए 0) और समस्या निवारण के लिए `--debug` का उपयोग करें।
- सुरक्षा: क्रेडेंशियल्स को हार्डकोड करने से बचें; एनवायरनमेंट वेरिएबल या Azure Key Vault का उपयोग करें।

## संदर्भ
[Azure CLI इंस्टॉल करें](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)  
[Azure CLI संदर्भ](https://learn.microsoft.com/en-us/cli/azure/)  
[Azure CLI क्विकस्टार्ट](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli)