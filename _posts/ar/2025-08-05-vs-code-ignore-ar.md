---
audio: false
generated: true
image: false
lang: ar
layout: post
title: استبعاد الملفات المُهملة في VS Code
translated: true
type: note
---

يمكنك جعل "انتقال إلى الملف" (الفتح السريع، Ctrl + P) يتضمن الملفات الموجودة في `.gitignore` الخاص بك عن طريق تعديل ثلاثة إعدادات في `settings.json`:

1. **أخبر البحث بتجاهل قواعد `.gitignore` الخاصة بك**

   ```jsonc
   "search.useIgnoreFiles": false,      // لا تلتزم بـ .gitignore
   "search.useGlobalIgnoreFiles": false // لا تلتزم بـ gitignore العام الخاص بك
   ```
2. **تأكد من أن أنماط الاستبعاد العامة لا تخفي تلك الملفات**
   بشكل افتراضي، يرث VS Code جميع الأنماط من `files.exclude` إلى `search.exclude`. إذا قمت باستبعاد مجلدات `.gitignore` يدويًا هناك، فأعد تمكينها:

   ```jsonc
   "search.exclude": {
     "**/.git": false,          // قم بفهرسة .git (إذا كنت تريد)
     "**/.gitignore": false     // بالتأكيد لا تخفي ملف .gitignore نفسه
     // …أي أنماط أخرى ترغب في تجاوزها
   }
   ```
3. **أعد تحميل النافذة**
   بعد حفظ إعدادات المستخدم أو مساحة العمل، قم بتشغيل **المطور: إعادة تحميل النافذة** (⇧ ⌘ P → "Reload Window") حتى يلتقط فهرس الملفات التغيير.

الآن عند الضغط على Ctrl + P سترى *جميع* الملفات بالاسم—سواء كانت مُهملة أم لا. ([stackoverflow.com][1])

[1]: https://stackoverflow.com/questions/62855190/how-do-you-include-git-ignored-files-in-vscode-quick-search?utm_source=chatgpt.com "How do you include git ignored files in VSCode quick search"