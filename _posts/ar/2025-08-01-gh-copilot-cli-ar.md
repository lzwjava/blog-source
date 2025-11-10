---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تكامل GitHub Copilot مع سطر الأوامر
translated: true
type: note
---

لا يمكنك استدعاء GitHub Copilot مباشرة كإضافة من سطر الأوامر باستخدام بناء جملة مثل `code --plugin copilot "hi"` للحصول على رد. ومع ذلك، يوفر GitHub Copilot تكاملاً مع سطر الأوامر من خلال GitHub CLI مع إضافة `gh copilot`، والتي توفر واجهة تشبه الدردشة للحصول على اقتراحات وتفسيرات للأوامر. هذا ليس مطابقًا تمامًا لإضافة عامة يتم استدعاؤها عبر أمر `code`، لكنه يخدم غرضًا مشابهًا للتفاعلات في سطر الأوامر.

### تفاصيل حول GitHub Copilot في سطر الأوامر (CLI)
- **المتطلبات**: تحتاج إلى اشتراك في GitHub Copilot، وتثبيت GitHub CLI (`gh`)، وتثبيت إضافة `gh-copilot`. تتوفر تعليمات الإعداد في مستودع GitHub CLI أو الوثائق [GitHub CLI Installation](https://cli.github.com/) و [Installing GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).
- **طريقة الاستخدام**: بعد الإعداد، يمكنك استخدام أوامر مثل:
  - `gh copilot suggest -t shell "hi"` للحصول على اقتراح لأمر shell.
  - `gh copilot explain "hi"` للحصول على تفسير لأمر.
  - مثال: تشغيل `gh copilot suggest -t shell "say hello"` قد يقترح `echo "hello"` أو أمر تحويل النص إلى كلام مثل `say "hello"` على نظام macOS، اعتمادًا على السياق.
- **القيود**: تم تصميم واجهة سطر الأوامر للمهام المتعلقة بسطر الأوامر (مثل أوامر shell، أو Git، أو GitHub CLI) ولا تدعم الردود المحادثية العامة مثل روبوت الدردشة. كما أنها تدعم فقط المطالبات (Prompts) باللغة الإنجليزية [Responsible use of GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use/copilot-in-the-cli)[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)
- **الوضع التفاعلي**: بعد تشغيل أمر `suggest`، يبدأ Copilot جلسة تفاعلية حيث يمكنك تحسين الاقتراح، أو تنفيذه (ينسخ إلى الحافظة)، أو تقييمه. للتنفيذ التلقائي، تحتاج إلى إعداد اسم مستعار (alias) يسمى `ghcs` [Using GitHub Copilot in the command line](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).[](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)[](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

### لماذا لا يعمل `code --plugin copilot "hi"`
- **سطر أوامر Visual Studio Code**: يدعم أمر `code` (خاص بـ VS Code) خيارات مثل `--install-extension` لتثبيت الإضافات، لكنه لا يحتوي على علم `--plugin` لاستدعاء الإضافات مباشرة بإدخال مثل `"hi"`. تعمل الإضافات مثل GitHub Copilot عادةً داخل محرر VS Code، حيث تقدم اقتراحات مدمجة أو واجهات دردشة، وليست كأدوات مستقلة لسطر الأوامر [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview).[](https://code.visualstudio.com/docs/copilot/overview)
- **هيكلية Copilot**: تتصل إضافة GitHub Copilot لـ VS Code بخادم لغة (language server) وخلفية GitHub لإكمال الكود والدردشة. لا توجد واجهة برمجة تطبيقات (API) عامة أو آلية في سطر الأوامر لتمرير سلاسل نصية عشوائية مثل `"hi"` مباشرة إلى الإضافة من سطر الأوامر والحصول على رد [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- **بديل للإدخال العام**: إذا كنت تريد إرسال مطالبة مثل `"hi"` إلى Copilot والحصول على رد، فستحتاج إلى استخدام Copilot Chat داخل VS Code أو بيئة التطوير المتكاملة (IDE) أخرى مدعومة، أو استكشاف أدوات أخرى لسطر الأوامر مدعومة بالذكاء الاصطناعي والتي تدعم المطالبات المحادثية (مثل Microsoft’s AI Shell لـ Azure CLI) [Use Microsoft Copilot in Azure with AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)

### حل بديل لتحقيق هدفك
إذا كان هدفك هو استدعاء مساعد ذكي اصطناعي مثل Copilot من سطر الأوامر بمطالبة مثل `"hi"` والحصول على رد، يمكنك:
1. **استخدام `gh copilot` لمهام سطر الأوامر**:
   - قم بتثبيت GitHub CLI وإضافة Copilot.
   - شغِّل `gh copilot suggest -t shell "greet with hi"` للحصول على أمر مثل `echo "hi"`.
   - هذا يقتصر على سياقات سطر الأوامر، لذا فإن `"hi"` وحدها قد لا تنتج ردًا ذا معنى إلا إذا تم صياغتها كطلب لأمر.
2. **استخدام Copilot Chat في VS Code**:
   - افتح VS Code، واستخدم واجهة Copilot Chat (يمكن الوصول إليها عبر `⌃⌘I` أو أيقونة الدردشة)، واكتب `"hi"` للحصول على رد محادثي.
   - يتطلب هذا تفاعلاً يدويًا داخل المحرر، وليس استدعاءً من سطر الأوامر [GitHub Copilot in VS Code cheat sheet](https://code.visualstudio.com/docs/copilot/copilot-cheat-sheet).[](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
3. **استكشاف أدوات أخرى للذكاء الاصطناعي في سطر الأوامر**:
   - **AI Shell**: يسمح AI Shell من Microsoft باستخدام مطالبات باللغة الطبيعية في سطر الأوامر للمهام المتعلقة بـ Azure. يمكنك تثبيته وتجربة مطالبات مثل `"hi"`، على الرغم من أنه مُحسّن لأوامر Azure CLI و PowerShell [Use Microsoft Copilot in Azure with AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)
   - **نصوص برمجية مخصصة**: يمكنك كتابة نص برمجي للتفاعل مع واجهة برمجة تطبيقات (API) لنموذج ذكاء اصطناعي (مثل واجهة OpenAI's API، إذا كانت متاحة) لمعالجة مطالبات مثل `"hi"`. ومع ذلك، فإن واجهة برمجة تطبيقات GitHub Copilot غير متاحة للجمهور لمثل هذا الاستخدام [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
4. **محاكاة سلوك الإضافة**:
   - أنشئ نصًا برمجيًا لـ shell أو اسمًا مستعارًا (alias) يوجه الإدخال إلى `gh copilot suggest` أو أداة أخرى للذكاء الاصطناعي في سطر الأوامر.
   - مثال:
     ```bash
     alias ai='gh copilot suggest -t shell'
     ai "greet with hi"
     ```
     هذا من شأنه أن يقترح أمرًا مثل `echo "hi"` أو ما شابه.

### الاستدعاء البرمجي
إذا كنت تبحث عن استدعاء وظيفة مشابهة لـ Copilot برمجيًا (كما هو موضح في مثالك)، لاحظ أن:
- GitHub Copilot لا يعرض واجهة برمجة تطبيقات (API) عامة للوصول البرمجي المباشر. بذلت بعض الجهود المجتمعية لعكس هندسة خادم اللغة أو استخدام وكلاء (proxies) لالتقاط الاقتراحات، لكن هذه معقدة ومحفوفة بالمخاطر (مثل احتمالية حظر الحساب) [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- يمكنك استكشاف البدائل مفتوحة المصدر أو نماذج الذكاء الاصطناعي الأخرى ذات التكاملات مع سطر الأوامر (مثل أدوات Hugging Face's CLI أو النماذج اللغوية الكبيرة المحلية مثل LLaMA مع أغلفة مخصصة).

### خاتمة
بينما لا يتم دعم `code --plugin copilot "hi"`، يمكنك تحقيق وظيفة مماثلة باستخدام `gh copilot` لمهام سطر الأوامر أو Copilot Chat في VS Code للمطالبات المحادثية. للحصول على تجربة ذكاء اصطناعي عامة في سطر الأوامر، فكر في أدوات مثل AI Shell أو النصوص البرمجية المخصصة مع واجهات برمجة تطبيقات الذكاء الاصطناعي الأخرى. تحقق دائمًا من الاقتراحات، حيث قد تحتوي ردود Copilot في سطر الأوامر على أخطاء أو تحيزات من بيانات التدريب [Responsible use of GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)

إذا كان لديك حالة استخدام محددة (مثل الذكاء الاصطناعي المحادثي مقابل توليد الأوامر)، فأخبرني، ويمكنني تخصيص الحل بشكل أكبر!