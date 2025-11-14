---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: استخدام كلود كود لجيت باش على ويندوز
translated: true
type: note
---

نعم، استنادًا إلى التطورات الأخيرة، فإن Claude Code (أداة الذكاء الاصطناعي للبرمجة من Anthropic) على نظام Windows يقوم بالفعل بتشغيل `git-bash.exe` لتشغيل أوامر shell. غالبًا ما يستخدم Git Bash كبيئة لتنفيذ الأوامر، خاصة في إعدادات Windows الأصلية بدون WSL. يمكن أن يؤدي هذا إلى ظهور نوافذ طرفية منبثقة لتنفيذ الأوامر، وهناك تكوينات وإضافات معروفة (مثل تلك في VS Code) وخطوات استكشاف الأخطاء وإصلاحها تتعلق بضمان الكشف عن Git Bash واستخدامه بشكل صحيح.

على سبيل المثال:
- في تثبيتات Windows الأصلية، يعتمد Claude Code على Git Bash لتوفير توافق يشبه أنظمة Unix للتعامل مع النصوص البرمجية والأوامر.
- إذا تم تعيينه كطرفية افتراضية (مثلًا في الأدوات المدمجة مثل VS Code أو Cursor)، فسيقوم بتشغيل `git-bash.exe` للمهام.
- هناك أخطاء مُبلغ عنها وأدلة للتعامل مع مشاكل المسارات أو المسافات في دليل تثبيت Git التي تؤثر على هذا التكامل.

إذا كنت تواجه مشاكل، تحقق من متغير PATH في نظامك، وتأكد من تثبيت Git بشكل صحيح، وتحقق من ملف تعريف الطرفية في بيئة التطوير المتكاملة (IDE) الخاصة بك.

المراجع:  
[Claude Code Native Windows Bash output not seen - Reddit](https://www.reddit.com/r/ClaudeAI/comments/1m06s2l/claude_code_native_windows_bash_output_not_seen/)  
[BUG Claude Code VS Code Extension Fails to Detect Git Bash on GitHub](https://github.com/anthropics/claude-code/issues/8674)  
[Troubleshooting Claude Code Installation on Windows - Medium](https://medium.com/%40tomhag_17/troubleshooting-claude-code-installation-on-windows-from-tty-errors-to-success-1f44af03c9f2)  
[Running Claude Code on Windows Without WSL - Blog](https://blog.shukebeta.com/2025/06/25/running-claude-code-on-windows-without-wsl/)  
[AI Agent Claude 4 runs commands in PowerShell even when default is Git Bash - Forum](https://forum.cursor.com/t/ai-agent-claude-4-runs-commands-in-powershell-even-when-default-terminal-is-git-bash/137164)  
[How To Install Claude Code on Windows Complete Guide 2025 - Itecsonline](https://itecsonline.com/post/how-to-install-claude-code-on-windows)  
[BUG Claude Code fails to resolve Git Bash path with space - GitHub](https://github.com/anthropics/claude-code/issues/4507)  
[Install Claude Code on Windows Without WSL Step-by-Step Guide - YouTube](https://www.youtube.com/watch?v=LtnxvLZjxAI)  
[47 Claude Code WSL Tricks Every Windows User Should Know - Medium](https://medium.com/%40joe.njenga/47-claude-code-wsl-tricks-every-windows-user-should-know-5d42aaee2d93)  
[Claude Code Installation Guide for Windows 11 Setting Up with WSL2 - Claude AI](https://claude.ai/public/artifacts/03a4aa0c-67b2-427f-838e-63770900bf1d)