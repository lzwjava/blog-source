---
audio: false
generated: true
lang: ar
layout: post
title: تحديث واجهة سطر أوامر كلاود
translated: true
type: note
---

مرحبًا! يبدو أنك تتعامل مع أداة Claude Code CLI من Anthropic. استنادًا إلى الناتج الذي لصقته، يبدو أنه تم محاولة التحديث التلقائي بالفعل إلى الإصدار 1.0.61، ولكن إذا كان ذلك لا يعمل أو كنت بحاجة إلى التحديث يدويًا، فإليك الطريقة:

لتحديث Claude Code CLI:
- افتح طرفيتك.
- نفذ الأمر: `claude update`
هذا الأمر المدمج يجب أن يقوم جلب وتثبيت أحدث إصدار.

إذا فشل التحديث (على سبيل المثال، بسبب مشاكل في الأذونات أو الشبكة)، يمكنك محاولة إعادة التثبيت عبر npm (بافتراض أن لديك Node.js و npm مثبتين):
- نفذ: `npm install -g @anthropic-ai/claude-code`

بعد التحديث، قد تحتاج إلى تسجيل الدخول مرة أخرى عن طريق تنفيذ `claude /login` (أو أحيانًا `claude login`، اعتمادًا على الإصدار). إذا كنت لا تزال ترى أخطاء، فتحقق من اتصالك بالإنترنت، وتأكد من أن مفتاح API الخاص بك صالح، أو راجع وثائق استكشاف الأخطاء وإصلاحها الرسمية.

لمزيد من التفاصيل حول الأوامر، يمكنك تنفيذ `claude --help` كما فعلت، والذي يجب أن يعرض الخيارات في الإصدار المحدث.

[مرجع CLI - واجهة برمجة تطبيقات Anthropic](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
[كيفية إعداد واستخدام أداة Claude CLI مثل المحترفين](https://medium.com/@riccardo.bernardi.advisor/unlocking-claude-pros-power-how-to-set-up-and-use-the-claude-cli-tool-like-a-pro-against-github-d29f8f682a03)  
[GitHub - anthropics/claude-code](https://github.com/anthropics/claude-code)  
[نظرة عامة على Claude Code - واجهة برمجة تطبيقات Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)