---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح أمر Go غير موجود على نظام macOS
translated: true
type: note
---

تشير رسالة الخطأ `/bin/sh: go: command not found` إلى أن لغة البرمجة Go غير مثبتة على نظام macOS الخاص بك، أو أنها غير مضبوطة بشكل صحيح في متغير PATH الخاص بك. أمر `make` يحاول تشغيل عملية بناء باستخدام Go، الأمر الذي يتطلب مترجم Go (`go`). فيما يلي الخطوات لتثبيت Go على نظام macOS وحل هذه المشكلة.

### خطوات تثبيت Go على macOS

هناك طريقتان رئيسيتان لتثبيت Go على macOS: استخدام مثبت Go الرسمي أو استخدام Homebrew. سأغطي كلا الطريقتين، لكن Homebrew غالبًا ما يكون أبسط لمستخدمي macOS. اختر إحدى الطريقتين بناءً على تفضيلك الشخصي.

#### المتطلبات الأساسية
- تأكد من أن إصدار macOS الخاص بك هو 10.10 أو أحدث لتكون متوافقًا مع إصدارات Go الحديثة.
- تحتاج إلى صلاحيات المسؤول لتثبيت Go وتعديل ملفات النظام.
- تطبيق Terminal (موجود في Applications > Utilities > Terminal).

#### الطريقة 1: تثبيت Go باستخدام Homebrew (موصى بها)
Homebrew هو مدير حزم شائع لنظام macOS يبسط عملية تثبيت البرامج.

1. **تثبيت Homebrew (إذا لم يكن مثبتًا بالفعل)**:
   - افتح Terminal وقم بتشغيل الأمر:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - اتبع التعليمات الظاهرة على الشاشة لإكمال التثبيت.

2. **تثبيت Go**:
   - قم بتشغيل الأمر التالي لتثبيت أحدث إصدار من Go:
     ```bash
     brew install go
     ```
   - يقوم هذا بتثبيت Go في المسار `/usr/local/Cellar/go` (أو مسار مشابه) وإضافة ملف Go الثنائي إلى `/usr/local/bin`.

3. **التحقق من التثبيت**:
   - تحقق من إصدار Go المثبت عن طريق تشغيل:
     ```bash
     go version
     ```
   - يجب أن ترى ناتجًا مشابهًا لـ `go version go1.23.x darwin/amd64`، مما يؤكد أن Go مثبت.

4. **إعداد متغيرات البيئة** (إذا لزم الأمر):
   - عادةً ما يضيف Homebrew Go إلى متغير PATH الخاص بك تلقائيًا، ولكن إذا لم تعمل أوامر `go`، أضف مسار الملف الثنائي لـ Go إلى ملف تعريف shell الخاص بك:
     - افتح أو أنشئ ملف التكوين المناسب لـ shell (مثل `~/.zshrc` لـ Zsh، وهو الافتراضي على macOS منذ Catalina، أو `~/.bash_profile` لـ Bash):
       ```bash
       nano ~/.zshrc
       ```
     - أضف السطور التالية:
       ```bash
       export PATH=$PATH:/usr/local/go/bin
       ```
     - احفظ الملف (Ctrl+X، ثم Y، ثم Enter في nano) وطبق التغييرات:
       ```bash
       source ~/.zshrc
       ```
     - إذا كنت ترغب في استخدام مساحة عمل مخصصة، قم بتعيين `GOPATH` (اختياري، حيث أن وحدات Go غالبًا ما تلغي الحاجة إلى هذا):
       ```bash
       export GOPATH=$HOME/go
       export PATH=$PATH:$GOPATH/bin
       ```
     - أعد تحميل الملف مرة أخرى:
       ```bash
       source ~/.zshrc
       ```

5. **اختبار تثبيت Go**:
   - قم بتشغيل `go version` مرة أخرى للتأكد من أن الأمر معترف به.
   - اختياريًا، أنشئ برنامج Go بسيط للتأكد من أن كل شيء يعمل:
     ```bash
     mkdir -p ~/go/src/hello
     nano ~/go/src/hello/main.go
     ```
     - أضف الكود التالي:
       ```go
       package main
       import "fmt"
       func main() {
           fmt.Println("Hello, World!")
       }
       ```
     - احفظ واخرج (Ctrl+X، Y، Enter)، ثم قم بالتجميع والتشغيل:
       ```bash
       cd ~/go/src/hello
       go run main.go
       ```
     - يجب أن ترى `Hello, World!` كناتج.

#### الطريقة 2: تثبيت Go باستخدام المثبت الرسمي
إذا كنت تفضل عدم استخدام Homebrew، يمكنك تثبيت Go باستخدام حزمة macOS الرسمية.

1. **تنزيل مثبت Go**:
   - قم بزيارة صفحة تنزيل Go الرسمية: https://go.dev/dl/
   - قم بتنزيل حزمة macOS (`.pkg`) لهندسة نظامك (مثل `go1.23.x.darwin-amd64.pkg` لأجهزة Mac ذات معالجات Intel أو `go1.23.x.darwin-arm64.pkg` لأجهزة Apple Silicon).

2. **تشغيل المثبت**:
   - انقر نقرًا مزدوجًا على ملف `.pkg` الذي تم تنزيله في Finder.
   - اتبع التعليمات الظاهرة على الشاشة لتثبيت Go. سيتم تثبيته في `/usr/local/go` افتراضيًا.
   - قد تحتاج إلى إدخال كلمة مرور المسؤول.

3. **إعداد متغيرات البيئة**:
   - افتح Terminal وقم بتحرير ملف تكوين shell الخاص بك (مثل `~/.zshrc` أو `~/.bash_profile`):
     ```bash
     nano ~/.zshrc
     ```
   - أضف السطور التالية:
     ```bash
     export GOROOT=/usr/local/go
     export GOPATH=$HOME/go
     export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
     ```
   - احفظ وطبق التغييرات:
     ```bash
     source ~/.zshrc
     ```
   - ملاحظة: `GOROOT` اختياري ما لم تكن تقوم بتطوير Go نفسه أو تحتاج إلى مسار تثبيت غير قياسي. غالبًا ما لا تتطلب إصدارات Go الحديثة تعيين `GOROOT`.

4. **التحقق من التثبيت**:
   - قم بتشغيل:
     ```bash
     go version
     ```
   - يجب أن ترى إصدار Go المثبت (مثل `go version go1.23.x darwin/amd64`).

5. **اختبار تثبيت Go**:
   - اتبع نفس الخطوات الواردة في الطريقة 1، الخطوة 5 لإنشاء وتشغيل برنامج "Hello, World!".

#### استكشاف الأخطاء وإصلاحها للمشكلة الأصلية
بعد تثبيت Go، عد إلى دليل `clash-core` الخاص بك وأعد تجربة أمر `make`:
```bash
cd /path/to/clash-core
make
```

إذا واجهت مشاكل:
- **إعدادات الوكيل**: يظهر ناتج Terminal الخاص بك أن `HTTP_PROXY` و `HTTPS_PROXY` مضبوطان على `http://127.0.0.1:7890`. تأكد من أن الوكيل الخاص بك نشط ولا يتعارض مع وصول Go إلى الشبكة (مثل تنزيل التبعيات). يمكنك تعطيل الوكيل مؤقتًا للاختبار:
  ```bash
  unset HTTP_PROXY HTTPS_PROXY
  make
  ```
- **الصلاحيات**: إذا ظهرت أخطاء متعلقة بالصلاحيات، تأكد من أن لديك حق الوصول للكتابة في دليل المشروع ومساحة عمل Go (`$GOPATH` أو `$HOME/go`).
- **وحدات Go**: من المرجح أن مشروع `clash-core` يستخدم وحدات Go. تأكد من أنك في الدليل الصحيح الذي يحتوي على `go.mod`، وقم بتشغيل `go mod tidy` لجلب التبعيات قبل `make`:
  ```bash
  go mod tidy
  make
  ```
- **عدم تطابق البنية**: أمر `make` يقوم بالبناء لـ `linux-amd64` (`GOOS=linux GOARCH=amd64`). إذا كنت تنوي تشغيل الملف الثنائي على macOS، قد تحتاج إلى تعديل ملف Makefile أو أمر البناء لاستهداف `darwin-amd64` (لأجهزة Intel Mac) أو `darwin-arm64` (لأجهزة Apple Silicon). تحقق من الهدف `linux-amd64` في ملف Makefile وقم بتعديله، أو قم بتشغيل:
  ```bash
  GOARCH=amd64 GOOS=darwin CGO_ENABLED=0 go build -trimpath -ldflags '-X "github.com/Dreamacro/clash/constant.Version=1.18" -X "github.com/Dreamacro/clash/constant.BuildTime=Sat Jun 28 12:24:27 UTC 2025" -w -s -buildid=' -o bin/clash-darwin-amd64
  ```
  استبدل `amd64` بـ `arm64` إذا كنت تستخدم جهاز Apple Silicon.

#### ملاحظات إضافية
- **إلغاء تثبيت إصدارات Go السابقة**: إذا كان Go مثبتًا مسبقًا، قم بإزالته لتجنب التعارضات:
  ```bash
  sudo rm -rf /usr/local/go
  sudo rm -f /etc/paths.d/go
  ```
  ثم أعد التثبيت باستخدام إحدى الطريقتين أعلاه.
- **مساحة عمل Go**: إذا قمت بتعيين `GOPATH`، قم بإنشاء الدليل:
  ```bash
  mkdir -p $HOME/go/{bin,src,pkg}
  ```
  ومع ذلك، مع وحدات Go (والتي تستخدمها معظم المشاريع الحديثة مثل `clash-core`)، تصبح أهمية `GOPATH` أقل.
- **أدوات سطر أوامر Xcode**: بعض مشاريع Go تتطلب تبعيات لغة C (مثل `CGO_ENABLED=1`). قم بتثبيت أدوات سطر أوامر Xcode إذا لزم الأمر:
  ```bash
  xcode-select --install
  ```
- **إصدارات Go متعددة**: إذا كنت تحتاج إلى إصدارات متعددة من Go، ففكر في استخدام مدير إصدارات مثل `gvm` (قم بتثبيته عبر Homebrew أو سكريبت).

#### التحقق
بمجرد تثبيت Go ونجاح أمر `make`، يجب أن يظهر الملف الثنائي `clash-core` في دليل `bin/` (مثل `bin/clash-linux-amd64` أو `bin/clash-darwin-amd64`). تحقق من أنه يعمل عن طريق تشغيل:
```bash
./bin/clash-darwin-amd64 --version
```

إذا كنت بحاجة إلى مزيد من المساعدة أو واجهت أخطاء محددة، دعني أعرف رسالة الخطأ الدقيقة أو السياق، وسأكون قادرًا على تقديم مساعدة أكثر استهدافًا!