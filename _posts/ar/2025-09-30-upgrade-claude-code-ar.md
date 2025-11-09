---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: ترقية كود كلود إلى أحدث إصدار
translated: true
type: note
---

لترقية Claude Code من الإصدار v2.0.0 إلى أحدث إصدار، استخدم إحدى الطرق التالية بناءً على نوع تثبيتك (جميع الإصدارات تدعم التحديثات التلقائية افتراضيًا، والتي يتم تطبيقها في المرة التالية التي تبدأ فيها الأداة؛ يمكنك تعطيلها عن طريق تعيين `DISABLE_AUTOUPDATER=1`):

### عبر الأمر المدمج في Claude Code
شغِّل أمر التحديث اليدوي في الطرفية:
```
claude update
```
هذا يطبق أحدث إصدار تلقائيًا. [1][2]

### عبر npm (إذا كان مثبتًا بشكل عام)
إذا قمت بالتثبيت originally عبر npm، فقم بالتحديث باستخدام:
```
npm update -g @anthropic-ai/claude-code
```
أو قم بتثبيت أحدث إصدار إجباريًا:
```
npm install -g @anthropic-ai/claude-code@latest
```
[3][4]

### عبر Binary الأصلي (مثبيت Beta)
للتثبيتات الأصلية، أعد تشغيل سكريبت المثبّت لأحدث إصدار:
```
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
```
[1]

**التحقق:** بعد الترقية، تحقق من إصدارك باستخدام `claude --version` للتأكد من تحديثه (على سبيل المثال، إلى الإصدار المستقر الحالي). إذا واجهت مشاكل، تأكد من أن npm محدث (`npm install -g npm@latest`). يتم الحفاظ على الإعدادات والتكوينات عبر التحديثات. [1][3][4]

المراجع:
[1] https://docs.claude.com/en/docs/claude-code/setup
[2] https://www.reddit.com/r/ClaudeAI/comments/1lvbijz/claude_code_updates_from_version_1045_to_1044/
[3] https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/
[4] https://www.claudelog.com/faq/