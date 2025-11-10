---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح عدم تطابق مخطط كود DeepSeek Claude
translated: true
type: note
---

إجابة مختصرة: عدم تطابق في المخطط.

Claude Code "يتحدث لغة Anthropic" (يتوقع نمط استخدام أدوات Anthropic-Messages مثل كتل `tool_use` / `tool_result`). بينما DeepSeek V3.1 على OpenRouter "يتحدث لغة OpenAI" (يصدر استدعاءات دوال/وظائف على نمط OpenAI مثل `tool_calls`). إذا قام جهاز التوجيه الخاص بـ Claude Code بتوجيه مهمة إلى DeepSeek V3.1 دون تحويل الطلب/الاستجابة، فلن يتم تحليل رسائل استدعاء الأداة الخاصة بالمساعد — وسترى أخطاءً بالضبط عندما يحاول الوكيل التخطيط/تشغيل الأدوات أو بث المخرجات. ([Anthropic][1], [OpenRouter][2], [DeepSeek API Docs][3])

ما يجب فعله (إصلاحات سريعة):

1. استخدم محولات جهاز التوجيه
   قم بتمكين محولات الطلب/الاستجابة OpenRouter↔︎Anthropic في جهاز توجيه Claude Code الخاص بك حتى يتم تعيين `tool_calls` ⇄ `tool_use` في كلا الاتجاهين. يدعم جهاز التوجيه المجتمعي الشهير هذا بشكل صريح؛ تحقق من قسم "تحويل الطلب/الاستجابة" وأمثلة التكوينات. ([GitHub][4], [ClaudeLog][5])

2. اختر المُعرف الصحيح للنموذج
   لـ DeepSeek V3.1 معرّفات محددة على OpenRouter (مثل إدخالات عائلة V3.1/V3). يمكن للمُعرف الخاطئ أو القديم أن يسبب أخطاء أيضًا أثناء مراحل البث أو استخدام الأدوات. تحقق من معرّف النموذج الدقيق الموجود على صفحة DeepSeek في OpenRouter واستخدمه في تعيين جهاز التوجيه الخاص بك. ([OpenRouter][6])

3. ابق في وضع "المحادثة" (وليس "المُفكر") إلا إذا قمت بتعيين حقوله
   إذا جربت متغيرًا استدلاليًا يبث حقول استدلال خاصة، فيجب على جهاز التوجيه الخاص بك ترجمتها — وإلا فسوف يتعطل Claude Code. فضّل نموذج المحادثة القياسي أو عطّل مخرجات "التفكير" الإضافية حتى يتعامل المحول الخاص بك معها. (توثيق DeepSeek يؤكد على استدعاء الدوال/الوظائف على نمط OpenAI؛ هذا ما يجب أن تعينه.) ([DeepSeek API Docs][3])

4. حدّث إلى أحدث إصدار من جهاز التوجيه
   أضافت الإصدارات المجتمعية الحديثة تعديلات توافق لمزودي الخدمة غير Anthropic؛ قم بالترقية قبل الاختبار. ([GitHub][4])

لماذا يحدث هذا فقط مع V3.1
أضافت V3.1 إمكانات وكيل/استدعاء أدوات أقوى بشكل افتراضي. هذا يزيد من احتمالية أن يصطدم سير عمل Claude Code الخاص بك برسائل الأداة غير المترجمة، وهو بالضبط المكان الذي يظهر فيه عدم تطابق المخطط. ([DeepSeek API Docs][7])

إذا شاركت نص الخطأ الدقيق، يمكنني الإشارة إلى مقتطف المحول الدقيق لإضافته إلى تكوينك.

[1]: https://www.anthropic.com/engineering/claude-code-best-practices?utm_source=chatgpt.com "Claude Code: Best practices for agentic coding"
[2]: https://openrouter.ai/docs/features/tool-calling?utm_source=chatgpt.com "Tool & Function Calling"
[3]: https://api-docs.deepseek.com/guides/function_calling?utm_source=chatgpt.com "Function Calling"
[4]: https://github.com/musistudio/claude-code-router?utm_source=chatgpt.com "musistudio/claude-code-router"
[5]: https://claudelog.com/claude-code-mcps/claude-code-router/?utm_source=chatgpt.com "Claude Code Router"
[6]: https://openrouter.ai/models?q=deepseek&utm_source=chatgpt.com "Models: 'deepseek'"
[7]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"