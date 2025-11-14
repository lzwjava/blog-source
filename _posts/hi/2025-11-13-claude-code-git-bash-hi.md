---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: क्लॉड कोड विंडोज़ पर गिट बैश का उपयोग करता है
translated: true
type: note
---

हाँ, हाल के विकासों के आधार पर, विंडोज़ पर Claude Code (Anthropic का एक AI कोडिंग टूल) शेल कमांड चलाने के लिए वास्तव में `git-bash.exe` को ट्रिगर करता है। यह अक्सर कमांड निष्पादित करने के लिए Git Bash को एनवायरनमेंट के रूप में उपयोग करता है, खासकर WSL के बिना नेटिव विंडोज़ सेटअप में। इसके परिणामस्वरूप कमांड निष्पादन के लिए पॉप-अप टर्मिनल दिखाई दे सकते हैं, और इसमें Git Bash के सही तरीके से डिटेक्ट और उपयोग किए जाने से संबंधित ज्ञात कॉन्फ़िगरेशन, एक्सटेंशन (जैसे VS Code में), और समस्या निवारण कदम शामिल हैं।

उदाहरण के लिए:
- नेटिव विंडोज़ इंस्टॉलेशन में, Claude Code स्क्रिप्ट्स और कमांड्स को हैंडल करने के लिए Unix-जैसी संगतता प्राप्त करने के लिए Git Bash पर निर्भर करता है।
- यदि इसे डिफ़ॉल्ट टर्मिनल के रूप में सेट किया जाता है (जैसे, VS Code या Cursor जैसे इंटीग्रेटेड टूल्स में), तो यह टास्क्स के लिए `git-bash.exe` लॉन्च करेगा।
- Git इंस्टालेशन डायरेक्टरी में पाथ इश्यू या स्पेस से संबंधित बग और गाइड्स सामने आए हैं जो इस इंटीग्रेशन को प्रभावित करते हैं।

यदि आपको कोई समस्या आ रही है, तो अपने सिस्टम PATH को चेक करें, सुनिश्चित करें कि Git सही तरीके से इंस्टॉल है, और अपने IDE में टर्मिनल प्रोफाइल वेरिफाई करें।

संदर्भ:  
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