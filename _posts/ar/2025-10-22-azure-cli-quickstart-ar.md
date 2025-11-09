---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل البدء السريع لـ Azure CLI
translated: true
type: note
---

Azure CLI (واجهة سطر الأوامر) هي مجموعة أدوات متعددة المنصات لإدارة موارد Azure من سطر الأوامر. إنها مثالية لأتمتة المهام، ونشر البرامج النصية، والتفاعل مع خدمات Azure دون الحاجة إلى البوابة الإلكترونية. وهي تدعم Bash وPowerShell وCommand Prompt على أنظمة Windows وmacOS وLinux.

## التثبيت

1.  **المتطلبات الأساسية**: تأكد من تثبيت Python 3.8 أو إصدار أحدث (تحقق باستخدام `python --version`).

2.  **التثبيت عبر مدير الحزم** (موصى به):
    *   **Windows**: استخدم Winget (`winget install Microsoft.AzureCLI`) أو Chocolatey (`choco install azure-cli`).
    *   **macOS**: استخدم Homebrew (`brew install azure-cli`).
    *   **Linux (Ubuntu/Debian)**: شغّل `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.
    *   **أنظمة Linux أخرى**: استخدم RPM أو التنزيل اليدوي من الموقع الرسمي.

3.  **التحقق من التثبيت**: افتح طرفية وشغّل `az --version`. يجب أن ترى إصدار CLI (مثل 2.64.0 اعتبارًا من أواخر 2025).

للحصول على خطوات مفصلة لكل منصة، راجع وثائق التثبيت الرسمية.

## المصادقة

قبل استخدام Azure CLI، سجّل الدخول إلى حساب Azure الخاص بك:

1.  **تسجيل دخول تفاعلي**: شغّل `az login`. سيؤدي هذا إلى فتح متصفح للمصادقة عبر Microsoft Entra ID. اتبع المطالبات لتسجيل الدخول.

2.  **Service Principal (لأتمتة المهام)**: أنشئ Service Principal باستخدام `az ad sp create-for-rbac --name "MyApp" --role contributor --scopes /subscriptions/{subscription-id}`. ثم استخدم `az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>`.

3.  **التحقق من تسجيل الدخول**: استخدم `az account show` للتحقق من الاشتراك النشط الخاص بك.

4.  **تسجيل الخروج**: `az logout`.

يتم دعم المصادقة متعددة العوامل (MFA)، ويمكنك إدارة اشتراكات متعددة باستخدام `az account set --subscription <id>`.

## الأوامر الأساسية

يستخدم Azure CLI الأمر `az` متبوعًا بمجموعة (مثل `vm`، `storage`) وأوامر فرعية. استخدم `az --help` للحصول على نظرة عامة، أو `az <group> --help` للحصول على تفاصيل محددة.

### خيارات عامة شائعة
*   `--help` أو `-h`: عرض التعليمات.
*   `--output table/json/yaml`: تنسيق المخرجات (الافتراضي: table).
*   `--query`: استعلام JMESPath لتصفية مخرجات JSON (مثال: `--query "[].name"`).

### أمثلة رئيسية
*   **عرض الاشتراكات**: `az account list --output table`
*   **الحصول على مجموعات الموارد**: `az group list --output table`
*   **إنشاء مجموعة موارد**: `az group create --name "MyResourceGroup" --location "eastus"`

## إدارة الأجهزة الافتراضية (VMs)
تتفوق Azure CLI في إدارة دورة حياة الأجهزة الافتراضية.

1.  **إنشاء جهاز افتراضي**:
    ```
    az vm create \
      --resource-group "MyResourceGroup" \
      --name "MyVM" \
      --image Ubuntu2204 \
      --admin-username azureuser \
      --admin-password MyP@ssw0rd123! \
      --location "eastus"
    ```

2.  **عرض قائمة الأجهزة الافتراضية**: `az vm list --output table`

3.  **بدء/إيقاف الجهاز الافتراضي**: `az vm start --name "MyVM" --resource-group "MyResourceGroup"` أو `az vm stop --name "MyVM" --resource-group "MyResourceGroup"`

4.  **الاتصال عبر SSH بالجهاز الافتراضي**: `az vm ssh "MyVM" --resource-group "MyResourceGroup"`

5.  **حذف جهاز افتراضي**: `az vm delete --name "MyVM" --resource-group "MyResourceGroup" --yes`

## إدارة حسابات التخزين
1.  **إنشاء حساب تخزين**:
    ```
    az storage account create \
      --name mystorageaccount \
      --resource-group "MyResourceGroup" \
      --location "eastus" \
      --sku Standard_LRS
    ```

2.  **تحميل Blob**: أولاً، احصل على المفتاح باستخدام `az storage account keys list --account-name mystorageaccount --resource-group "MyResourceGroup" --query "[0].value -o tsv"`. ثم: `az storage blob upload --account-name mystorageaccount --container-name mycontainer --name myfile.txt --file ./myfile.txt --auth-mode key`

## سيناريوهات شائعة أخرى
*   **نشر قوالب ARM**: `az deployment group create --resource-group "MyResourceGroup" --template-file template.json`
*   **استعلام عن الموارد**: `az resource list --resource-group "MyResourceGroup" --output table`
*   **تحديث CLI**: `az upgrade`
*   **الامتدادات**: قم بتثبيت الامتدادات مثل `az extension add --name azure-devops` للحصول على أوامر إضافية.

للبرمجة النصية، اجمع بين أوامر Azure CLI وحلقات Bash/PowerShell أو استخدمها في خطوط أنابيب CI/CD مثل GitHub Actions.

## نصائح وأفضل الممارسات
*   استخدم `--dry-run` للمعاينة (حيثما يكون مدعومًا).
*   تمكين الإكمال التلقائي: في Bash، شغّل `az completion`.
*   معالجة الأخطاء: تحقق من رموز الخروج (0 للنجاح) واستخدم `--debug` لاستكشاف الأخطاء وإصلاحها.
*   الأمان: تجنب تضمين بيانات الاعتماد مباشرة في الكود؛ استخدم متغيرات البيئة أو Azure Key Vault.

## المراجع
[تثبيت Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)  
[مرجع Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)  
[بدء استخدام Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli)