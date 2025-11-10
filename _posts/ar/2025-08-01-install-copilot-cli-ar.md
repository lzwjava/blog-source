---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تثبيت امتداد GitHub Copilot لسطر الأوامر
translated: true
type: note
---

أمر `gh extension install github/gh-copilot` يقوم بتثبيت إضافة GitHub Copilot لأداة GitHub CLI، مما يمكّن من استخدام ميزات Copilot مثل الاقتراحات والشروحات في سطر الأوامر. بالنسبة لمستخدمي المؤسسات، فإن تطبيق هذا الأمر يعتمد على شروط محددة:

- **تكوين المؤسسة**: يمكن لمستخدمي المؤسسات استخدام إضافة Copilot CLI إذا كانت مؤسستهم أو شركتهم مشتركة في باقة GitHub Copilot Business أو Copilot Enterprise، وتم تمكين ميزة CLI من قبل المسؤولين. إذا قام مالك المؤسسة أو مسؤول المؤسسة بتعطيل Copilot في الـ CLI، فلا يمكن استخدام الإضافة حتى لو تم تثبيتها. [](https://docs.github.com/fr/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli) [](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
- **المصادقة**: يجب على مستخدمي المؤسسات المصادقة على أداة GitHub CLI باستخدام حساب GitHub لديهم مقعد Copilot مخصص له. بالنسبة للحسابات المُدارة للمستخدمين على GitHub Enterprise Cloud (GHE.com)، قد تكون هناك حاجة لإعدادات إضافية، مثل تحديث الإعدادات قبل تسجيل الدخول. [](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)
- **متطلبات التثبيت**: يجب تثبيت أداة GitHub CLI قبل تشغيل الأمر. عملية التثبيت نفسها متشابهة لمستخدمي المؤسسات والأفراد، ولكن سياسات المؤسسة قد تقيد الاستخدام. [](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)

**خطوات لمستخدمي المؤسسات**:
1. تأكد من تثبيت أداة GitHub CLI (راجع [مستودع GitHub CLI](https://github.com/cli/cli) للحصول على التعليمات).
2. تحقق من مسؤول المؤسسة لديك أن Copilot CLI مفعل لمؤسستك.
3. شغّل الأمر `gh extension install github/gh-copilot` في طرفيتك.
4. قم بالمصادقة باستخدام `gh auth login` باستخدام حساب GitHub المخصص لك من قبل المؤسسة.
5. إذا كنت تستخدم حساب مستخدم مُدار على GHE.com، فاتبع خطوات الإعداد الإضافية الموضحة في [استخدام GitHub Copilot مع حساب على GHE.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/configuring-github-copilot-in-your-environment/using-github-copilot-with-an-account-on-ghecom). [](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)

إذا كانت مؤسستك تقيد الوصول إلى CLI أو لم تقم بتمكين Copilot، فقد يتم تثبيت الإضافة ولكنها لن تعمل. تحقق من سياسات المؤسسة مع المسؤول لديك.

[تثبيت GitHub Copilot في الـ CLI](https://docs.github.com/en/enterprise-cloud@latest/copilot/installing-github-copilot-in-the-cli) [](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
[إعداد GitHub Copilot لمؤسستك](https://docs.github.com/en/enterprise-cloud@latest/copilot/setting-up-github-copilot-for-your-enterprise) [](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/set-up-for-enterprise)