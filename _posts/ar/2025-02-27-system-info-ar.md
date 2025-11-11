---
audio: false
generated: true
lang: ar
layout: post
title: معلومات النظام على نظام التشغيل ماك
translated: true
type: note
---

للحصول على معلومات النظام على جهاز macOS الخاص بك، يمكنك استخدام عدة أدوات وأوامر مدمجة. فيما يلي بعض الطرق لاسترداد أنواع مختلفة من معلومات النظام:

### 1. **أداة معلومات النظام**
تطبيق معلومات النظام يقدم نظرة شاملة عن الأجهزة والبرامج في جهاز Mac الخاص بك.

- افتح **البحث في Spotlight** بالضغط على `Cmd + Space` واكتب "System Information"، ثم اضغط على Enter.
- بدلاً من ذلك، يمكنك فتحه من **قائمة Apple** > **About This Mac** > **System Report**.

### 2. **About This Mac**
يوفر هذا نظرة سريعة على مواصفات جهاز Mac الخاص بك.

- انقر على **قائمة Apple** في الزاوية العلوية اليسرى من الشاشة.
- اختر **About This Mac**. سيظهر هذا معلومات أساسية مثل إصدار macOS، والمعالج، والذاكرة، ورقم التسلسل.

### 3. **أوامر Terminal**
يمكنك استخدام Terminal للحصول على معلومات مفصلة عن النظام باستخدام أوامر مختلفة.

- افتح **Terminal** من `Applications` > `Utilities` > `Terminal` أو بالبحث عنه في Spotlight.

#### معلومات النظام الأساسية
```sh
system_profiler SPHardwareDataType
```

#### معلومات النظام التفصيلية
```sh
system_profiler
```

#### معلومات المعالج (CPU)
```sh
sysctl -n machdep.cpu.brand_string
```

#### معلومات الذاكرة
```sh
sysctl hw.memsize
```

#### استخدام القرص
```sh
df -h
```

#### معلومات الشبكة
```sh
ifconfig
```

#### معلومات البطارية (للأجهزة المحمولة)
```sh
pmset -g batt
```

#### قائمة البرامج المثبتة
```sh
ls /Applications
```

#### إصدار macOS
```sh
sw_vers
```

#### معلومات المستخدم
```sh
id
```

#### قائمة العمليات قيد التشغيل
```sh
ps aux
```

#### قائمة حزم Brew المثبتة
```sh
brew list
```

#### قائمة حزم Pip المثبتة
```sh
pip list
```

#### قائمة حزم Gem المثبتة
```sh
gem list
```

### 4. **Activity Monitor**
يوفر هذا التطبيق معلومات في الوقت الفعلي عن استخدام وحدة المعالجة المركزية والذاكرة والطاقة والقرص والشبكة في جهاز Mac الخاص بك.

- افتح **Activity Monitor** من `Applications` > `Utilities` > `Activity Monitor` أو بالبحث عنه في Spotlight.

### 5. **Disk Utility**
يوفر هذا التطبيق معلومات حول أجهزة التخزين الخاصة بك.

- افتح **Disk Utility** من `Applications` > `Utilities` > `Disk Utility` أو بالبحث عنه في Spotlight.

### 6. **أدوات الطرف الثالث**
هناك أيضاً تطبيقات تابعة لجهات خارجية مثل **iStat Menus** و **CoconutBattery** التي توفر معلومات نظام مفصلة وإمكانيات مراقبة.

باستخدام هذه الطرق، يمكنك جمع مجموعة واسعة من معلومات النظام على جهاز macOS الخاص بك.