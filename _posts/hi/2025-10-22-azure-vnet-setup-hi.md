---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एज़्योर वर्चुअल नेटवर्क सेटअप गाइड
translated: true
type: note
---

### Azure Virtual Network कॉन्फ़िगरेशन अवलोकन

Azure में आपके वर्णित आर्किटेक्चर को सेट अप करने के लिए, हम सादगी के लिए एक ही Virtual Network (VNet) का उपयोग करेंगे, जिसमें कई सबनेट होंगे ताकि पब्लिक-फेसिंग रिसोर्सेज (जैसे आपकी API और एडमिन सर्विस) को आंतरिक रिसोर्सेज (जैसे MQ/Redis VM) से अलग किया जा सके। यह प्राइवेट IPs के माध्यम से सुरक्षित आंतरिक संचार की अनुमति देता है, जबकि Network Security Groups (NSGs) के माध्यम से पब्लिक एक्सेस को नियंत्रित करता है। हम आपकी टीम की IP रेंज तक प्रतिबंधित SSH एक्सेस भी कॉन्फ़िगर करेंगे।

मुख्य सिद्धांत:
- **पब्लिक एक्सेस**: विशिष्ट पोर्ट्स (API के लिए 443, एडमिन के लिए 80) पर इंटरनेट या टीम IPs से इनबाउंड ट्रैफ़िक की अनुमति देने के लिए पब्लिक IPs और NSGs का उपयोग करें।
- **आंतरिक संचार**: एक ही VNet में मौजूद VMs प्राइवेट IPs पर स्वतंत्र रूप से संचार कर सकते हैं; फाइन-ट्यूनिंग के लिए NSGs का उपयोग करें (उदाहरण के लिए, Redis के लिए पोर्ट 6379 पर बैकएंड से MQ की अनुमति दें)।
- **SSH एक्सेस**: टीम IPs से पोर्ट 22 पर बास्टियन या डायरेक्ट SSH तक प्रतिबंधित करें।
- **एडमिन सर्विस**: इसे API की तरह ही समझें लेकिन पोर्ट 80 पर, टीम तक प्रतिबंधित।

यह मानता है कि आप Azure Portal या CLI का उपयोग कर रहे हैं; मैं प्रतिलिपि प्रस्तुत करने योग्यता के लिए CLI उदाहरणों के साथ उच्च-स्तरीय चरण प्रदान करूंगा। VNets, VMs, और पब्लिक IPs के लिए लागत लागू होती है।

#### चरण 1: Virtual Network और सबनेट बनाएँ
दो सबनेट के साथ एक VNet बनाएँ:
- **पब्लिक सबनेट** (उदाहरण के लिए, API और एडमिन VMs के लिए): पब्लिक IPs की अनुमति देता है।
- **प्राइवेट सबनेट** (उदाहरण के लिए, MQ/Redis VM के लिए): कोई पब्लिक IPs नहीं; केवल आंतरिक।

Azure CLI का उपयोग करते हुए (पहले `az login` के माध्यम से इंस्टॉल करें):

```bash
# रिसोर्स ग्रुप बनाएँ
az group create --name myResourceGroup --location eastus

# VNet बनाएँ
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefixes 10.0.0.0/16 \
  --subnet-name PublicSubnet \
  --subnet-prefixes 10.0.1.0/24

# प्राइवेट सबनेट जोड़ें
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --address-prefixes 10.0.2.0/24
```

#### चरण 2: VMs बनाएँ और नेटवर्किंग असाइन करें
- **बैकएंड API VM** (PublicSubnet में): 443 एक्सेस के लिए पब्लिक IP।
- **MQ/Redis VM** (PrivateSubnet में): केवल प्राइवेट IP।
- **एडमिन VM** (PublicSubnet में): 80 एक्सेस के लिए पब्लिक IP।

CLI उदाहरण:

```bash
# बैकएंड API VM
az vm create \
  --resource-group myResourceGroup \
  --name backendVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# API के लिए पब्लिक IP प्राप्त करें
API_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n backendVM --query publicIps -o tsv)

# MQ/Redis VM (कोई पब्लिक IP नहीं)
az vm create \
  --resource-group myResourceGroup \
  --name mqVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PrivateSubnet

# आंतरिक संचार के लिए प्राइवेट IP प्राप्त करें
MQ_PRIVATE_IP=$(az vm show -g myResourceGroup -n mqVM --query privateIps -o tsv)

# एडमिन VM
az vm create \
  --resource-group myResourceGroup \
  --name adminVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# एडमिन के लिए पब्लिक IP प्राप्त करें
ADMIN_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n adminVM --query publicIps -o tsv)
```

VMs पर:
- अपनी API को backendVM पर इंस्टॉल करें (उदाहरण के लिए, SSL के साथ 443 पर सुनें)।
- Redis/MQ को mqVM पर इंस्टॉल करें (6379 पर सुनें)।
- एडमिन सर्विस को adminVM पर इंस्टॉल करें (80 पर सुनें)।

#### चरण 3: Network Security Groups (NSGs) कॉन्फ़िगर करें
NSGs फ़ायरवॉल की तरह काम करते हैं। प्रति सबनेट (या बेहतर नियंत्रण के लिए प्रति NIC) एक NSG को संबद्ध करें। अनुमति देने के लिए नियम बनाएँ:
- पब्लिक: backendVM को 443, adminVM को 80।
- आंतरिक: 6379 पर बैकएंड से MQ।
- SSH: टीम IPs से पोर्ट 22 (`TEAM_IPS` को आपके CIDR से बदलें, उदाहरण के लिए, 203.0.113.0/24)।

NSGs के लिए CLI:

```bash
# पब्लिक सबनेट के लिए NSG बनाएँ
az network nsg create \
  --resource-group myResourceGroup \
  --name publicNSG

# पब्लिक NSG के लिए नियम
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name publicNSG \
  --name AllowHTTPS \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 443

az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name publicNSG \
  --name AllowHTTPAdmin \
  --priority 101 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes 'TEAM_IPS' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 80

az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name publicNSG \
  --name AllowSSH \
  --priority 102 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes 'TEAM_IPS' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 22

# पब्लिक NSG को PublicSubnet से संबद्ध करें
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PublicSubnet \
  --network-security-group publicNSG

# प्राइवेट सबनेट के लिए NSG बनाएँ
az network nsg create \
  --resource-group myResourceGroup \
  --name privateNSG

# बैकएंड से MQ के लिए आंतरिक ट्रैफ़िक की अनुमति दें
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name privateNSG \
  --name AllowFromBackend \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '10.0.1.0/24'  # PublicSubnet CIDR
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 6379  # Redis पोर्ट

# यदि आवश्यक हो तो प्राइवेट VM को SSH की अनुमति दें (टीम से बास्टियन या VPN के माध्यम से)
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name privateNSG \
  --name AllowSSHPrivate \
  --priority 101 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes 'TEAM_IPS' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 22

# प्राइवेट NSG को संबद्ध करें
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --network-security-group privateNSG
```

- **आंतरिक संचार**: BackendVM (10.0.1.x) अब बिना पब्लिक एक्सपोजर के mqVM (10.0.2.x:6379) तक पहुँच सकता है।
- **डिफ़ॉल्ट डिनाय**: NSGs अन्य सभी ट्रैफ़िक को अस्वीकार करते हैं।

#### चरण 4: टीम के लिए SSH एक्सेस
- डायरेक्ट SSH: टीम IPs से `ssh azureuser@<VM_PUBLIC_IP> -p 22` का उपयोग करें (पहले से ही NSG में अनुमति है)।
- प्राइवेट VM के लिए: VNet में Azure Bastion (सुरक्षा के लिए अनुशंसित) का उपयोग करें।
  - Bastion बनाएँ: `az network bastion create --name myBastion --resource-group myResourceGroup --vnet-name myVNet --location eastus --sku Standard --bastion-subnet-address-prefix 10.0.3.0/26` (पहले एक नया BastionSubnet जोड़ें)।
  - Azure Portal > Bastion > प्राइवेट IP का उपयोग करके mqVM से कनेक्ट करें।

#### चरण 5: सेवाओं तक पहुँचें
- **पब्लिक API**: `https://$API_PUBLIC_IP` (पोर्ट 443)।
- **एडमिन सर्विस**: `http://$ADMIN_PUBLIC_IP` (पोर्ट 80, केवल टीम)।
- **आंतरिक टेस्ट**: backendVM से, `redis-cli -h $MQ_PRIVATE_IP -p 6379`।

#### अतिरिक्त सर्वोत्तम अभ्यास
- **लोड बैलेंसर/एप्लिकेशन गेटवे**: प्रोडक्शन के लिए, API/एडमिन के सामने WAF/SSL टर्मिनेशन के लिए Azure Application Gateway का उपयोग करें।
- **प्राइवेट एंडपॉइंट्स**: Redis के लिए, सबनेट एक्सपोजर से बचने के लिए Azure Private Link का उपयोग करें।
- **मॉनिटरिंग**: ट्रैफ़िक लॉग्स के लिए Azure Network Watcher सक्षम करें।
- **स्केलिंग**: यदि VMs बढ़ती हैं, तो Availability Sets या Scale Sets का उपयोग करें।
- **क्लीनअप**: `az group delete --name myResourceGroup --yes --no-wait`।

पूर्ण डॉक्स के लिए: [Azure VNet अवलोकन](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), [NSG नियम](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)। यदि आपको Terraform/ARM टेम्प्लेट्स या विशिष्टताओं (जैसे, सटीक टीम IPs) की आवश्यकता है, तो अधिक विवरण प्रदान करें!