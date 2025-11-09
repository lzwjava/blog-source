---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: क्लॉड कोड को नवीनतम संस्करण में अपग्रेड करना
translated: true
type: note
---

Claude Code को v2.0.0 से नवीनतम संस्करण में अपग्रेड करने के लिए, अपनी इंस्टॉलेशन प्रकार के आधार पर निम्नलिखित में से कोई एक विधि उपयोग करें (सभी संस्करण डिफ़ॉल्ट रूप से ऑटो-अपडेट का समर्थन करते हैं, जो टूल को अगली बार शुरू करने पर लागू होते हैं; आप `DISABLE_AUTOUPDATER=1` सेट करके इन्हें अक्षम कर सकते हैं):

### Claude Code के बिल्ट-इन कमांड के माध्यम से
अपने टर्मिनल में मैन्युअल अपडेट कमांड चलाएँ:
```
claude update
```
यह स्वचालित रूप से नवीनतम संस्करण लागू कर देता है। [1][2]

### npm के माध्यम से (यदि ग्लोबली इंस्टॉल किया गया हो)
यदि आपने मूल रूप से npm के माध्यम से इंस्टॉल किया था, तो इसके साथ अपडेट करें:
```
npm update -g @anthropic-ai/claude-code
```
या नवीनतम को फोर्स-इंस्टॉल करें:
```
npm install -g @anthropic-ai/claude-code@latest
```
[3][4]

### नेटिव बाइनरी के माध्यम से (बीटा इंस्टॉलर)
नेटिव इंस्टॉलेशन के लिए, नवीनतम संस्करण के लिए इंस्टॉलर स्क्रिप्ट को फिर से चलाएँ:
```
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
```
[1]

**सत्यापन:** अपग्रेड करने के बाद, अपने संस्करण की जाँच `claude --version` के साथ करके पुष्टि करें कि यह अपडेट हो गया है (उदाहरण के लिए, वर्तमान स्टेबल रिलीज़ में)। यदि आपको कोई समस्या आती है, तो सुनिश्चित करें कि npm अप टू डेट है (`npm install -g npm@latest`)। सेटिंग्स और कॉन्फ़िगरेशन अपडेट्स के दौरान संरक्षित रहते हैं। [1][3][4]

साइटेशन्स:
[1] https://docs.claude.com/en/docs/claude-code/setup
[2] https://www.reddit.com/r/ClaudeAI/comments/1lvbijz/claude_code_updates_from_version_1045_to_1044/
[3] https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/
[4] https://www.claudelog.com/faq/