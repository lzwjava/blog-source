---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل إعداد الشبكة الافتراضية في Azure
translated: true
type: note
---

### نظرة عامة على تكوين شبكة Azure الافتراضية

لإعداد البنية التي وصفتها في Azure، سنستخدم شبكة افتراضية واحدة (VNet) للتبسيط، مع شبكات فرعية متعددة لفصل الموارد الموجهة للعموم (مثل خدمة API وخدمة الإدارة) عن الموارد الداخلية (مثل خادم MQ/Redis الظاهري). هذا يسمح باتصال داخلي آمن عبر عناوين IP الخاصة مع التحكم في الوصول العام عبر مجموعات أمان الشبكة (NSGs). سنقوم أيضًا بتكوين وصول SSH مقصور على نطاقات عناوين IP فريقك.

المبادئ الأساسية:
- **الوصول العام**: استخدم عناوين IP العامة ومجموعات أمان الشبكة للسماح بحركة المرور الواردة فقط على منافذ محددة (443 لـ API، 80 للإدارة) من الإنترنت أو عناوين IP الفريق.
- **الاتصال الداخلي**: يمكن للأجهزة الظاهرية في نفس الشبكة الافتراضية التواصل بحرية عبر عناوين IP الخاصة؛ استخدم مجموعات أمان الشبكة للضبط الدقيق (مثال: السماح للخلفية بالوصول إلى MQ على المنفذ 6379 لـ Redis).
- **وصول SSH**: قصر الوصول على الباستيون أو SSH مباشرة على المنفذ 22 من عناوين IP الفريق.
- **خدمة الإدارة**: عالجها مثل API ولكن على المنفذ 80، ومقيدة للفريق.

يفترض هذا أنك تستخدم بوابة Azure أو سطر الأوامر (CLI); سأقدم خطوات عالية المستوى مع أمثلة لـ CLI لإمكانية إعادة الإنتاج. تنطبق التكاليف على الشبكات الافتراضية، والأجهزة الظاهرية، وعناوين IP العامة.

#### الخطوة 1: إنشاء الشبكة الافتراضية والشبكات الفرعية
أنشئ شبكة افتراضية VNet بشبكتين فرعيتين:
- **شبكة فرعية عامة** (مثال: لأجهزة API والإدارة الظاهرية): تسمح بعناوين IP عامة.
- **شبكة فرعية خاصة** (مثال: لخادم MQ/Redis الظاهري): بدون عناوين IP عامة؛ داخلية فقط.

باستخدام Azure CLI (قم بالتثبيت أولاً عبر `az login`):

```bash
# إنشاء مجموعة موارد
az group create --name myResourceGroup --location eastus

# إنشاء شبكة افتراضية VNet
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefixes 10.0.0.0/16 \
  --subnet-name PublicSubnet \
  --subnet-prefixes 10.0.1.0/24

# إضافة شبكة فرعية خاصة
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --address-prefixes 10.0.2.0/24
```

#### الخطوة 2: إنشاء الأجهزة الظاهرية وتعيين الشبكات
- **خادم Backend API الظاهري** (في PublicSubnet): عنوان IP عام للوصول على المنفذ 443.
- **خادم MQ/Redis الظاهري** (في PrivateSubnet): عنوان IP خاص فقط.
- **خادم الإدارة الظاهري** (في PublicSubnet): عنوان IP عام للوصول على المنفذ 80.

أمثلة لـ CLI:

```bash
# خادم Backend API الظاهري
az vm create \
  --resource-group myResourceGroup \
  --name backendVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# الحصول على عنوان IP عام لـ API
API_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n backendVM --query publicIps -o tsv)

# خادم MQ/Redis الظاهري (بدون عنوان IP عام)
az vm create \
  --resource-group myResourceGroup \
  --name mqVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PrivateSubnet

# الحصول على عنوان IP خاص للاتصال الداخلي
MQ_PRIVATE_IP=$(az vm show -g myResourceGroup -n mqVM --query privateIps -o tsv)

# خادم الإدارة الظاهري
az vm create \
  --resource-group myResourceGroup \
  --name adminVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# الحصول على عنوان IP عام للإدارة
ADMIN_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n adminVM --query publicIps -o tsv)
```

على الأجهزة الظاهرية:
- قم بتثبيت API الخاص بك على backendVM (مثال: الاستماع على المنفذ 443 مع SSL).
- قم بتثبيت Redis/MQ على mqVM (الاستماع على المنفذ 6379).
- قم بتثبيت خدمة الإدارة على adminVM (الاستماع على المنفذ 80).

#### الخطوة 3: تكوين مجموعات أمان الشبكة (NSGs)
تعمل مجموعات أمان الشبكة كجدران حماية. اربط مجموعة NSG واحدة بكل شبكة فرعية (أو بكل بطاقة واجهة شبكة NIC للتحكم الأكثر دقة). أنشئ قواعد للسماح بـ:
- العام: 443 إلى backendVM، 80 إلى adminVM.
- الداخلي: من Backend إلى MQ على المنفذ 6379.
- SSH: المنفذ 22 من عناوين IP الفريق (استبدل `TEAM_IPS` بـ CIDR الخاص بك، مثال: 203.0.113.0/24).

CLI لمجموعات أمان الشبكة NSGs:

```bash
# إنشاء NSG للشبكة الفرعية العامة
az network nsg create \
  --resource-group myResourceGroup \
  --name publicNSG

# قواعد لـ NSG العامة
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

# ربط NSG العامة بالشبكة الفرعية العامة PublicSubnet
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PublicSubnet \
  --network-security-group publicNSG

# إنشاء NSG للشبكة الفرعية الخاصة
az network nsg create \
  --resource-group myResourceGroup \
  --name privateNSG

# السماح بحركة المرور الداخلية من Backend إلى MQ
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name privateNSG \
  --name AllowFromBackend \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '10.0.1.0/24'  # CIDR للشبكة الفرعية العامة PublicSubnet
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 6379  # منفذ Redis

# السماح بـ SSH للخادم الظاهري الخاص إذا لزم الأمر (من الفريق عبر Bastion أو VPN)
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

# ربط NSG الخاصة
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --network-security-group privateNSG
```

- **الاتصال الداخلي**: يمكن الآن لـ BackendVM (10.0.1.x) الوصول إلى mqVM (10.0.2.x:6379) بدون تعريضه للعامة.
- **الرفض الافتراضي**: ترفض مجموعات أمان الشبكة NSGs ضمنيًا جميع حركات المرور الأخرى.

#### الخطوة 4: وصول SSH للفريق
- SSH مباشر: استخدم `ssh azureuser@<VM_PUBLIC_IP> -p 22` من عناوين IP الفريق (مسموح به مسبقًا في NSG).
- للخادم الظاهري الخاص: استخدم Azure Bastion (موصى به للأمان) في الشبكة الافتراضية VNet.
  - إنشاء Bastion: `az network bastion create --name myBastion --resource-group myResourceGroup --vnet-name myVNet --location eastus --sku Standard --bastion-subnet-address-prefix 10.0.3.0/26` (أضف شبكة فرعية جديدة لـ BastionSubnet أولاً).
  - الاتصال عبر بوابة Azure > Bastion > الاتصال بـ mqVM باستخدام عنوان IP الخاص.

#### الخطوة 5: الوصول إلى الخدمات
- **API العام**: `https://$API_PUBLIC_IP` (المنفذ 443).
- **خدمة الإدارة**: `http://$ADMIN_PUBLIC_IP` (المنفذ 80، للفريق فقط).
- **اختبار داخلي**: من backendVM، `redis-cli -h $MQ_PRIVATE_IP -p 6379`.

#### أفضل ممارسات إضافية
- **موزع الحمل / بوابة التطبيقات**: للإنتاج، ضع خدمة API/الإدارة خلف Azure Application Gateway لـ WAF/إنهاء SSL.
- **نقاط النهاية الخاصة**: لـ Redis، استخدم Azure Private Link لتجنب تعريض الشبكة الفرعية.
- **المراقبة**: قم بتمكين Azure Network Watcher لسجلات حركة المرور.
- **التوسع**: إذا نمت الأجهزة الظاهرية، استخدم Availability Sets أو Scale Sets.
- **التنظيف**: `az group delete --name myResourceGroup --yes --no-wait`.

للحصول على الوثائق الكاملة: [نظرة عامة على شبكة Azure الافتراضية](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)، [قواعد NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview). إذا كنت تحتاج إلى قوالب Terraform/ARM أو تفاصيل محددة (مثال: عناوين IP الفريق بالضبط)، قدم المزيد من التفاصيل!