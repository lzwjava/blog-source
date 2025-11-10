---
audio: false
generated: true
lang: hi
layout: post
title: क्लॉड कोड सीएलआई अद्यतन
translated: true
type: note
---

नमस्ते! लगता है आप Anthropic के Claude Code CLI टूल का उपयोग कर रहे हैं। आपके पेस्ट किए गए आउटपुट के आधार पर, ऐसा लगता है कि यह पहले ही स्वचालित रूप से version 1.0.61 में अपडेट करने का प्रयास कर चुका है, लेकिन अगर यह काम नहीं कर रहा है या आपको मैन्युअल रूप से अपडेट करने की आवश्यकता है, तो यहां बताया गया है कि कैसे:

Claude Code CLI को अपडेट करने के लिए:
- अपना टर्मिनल खोलें।
- कमांड चलाएं: `claude update`
यह बिल्ट-इन कमांड नवीनतम version को fetch और install कर देगा।

यदि अपडेट विफल हो जाता है (जैसे कि permissions या network issues के कारण), तो आप npm के माध्यम से इसे पुनः स्थापित करने का प्रयास कर सकते हैं (मानकर कि आपके पास Node.js और npm इंस्टॉल है):
- चलाएं: `npm install -g @anthropic-ai/claude-code`

अपडेट करने के बाद, आपको फिर से लॉग इन करने की आवश्यकता हो सकती है, `claude /login` (या कभी-कभी `claude login`, version के आधार पर) चलाकर। यदि आप अभी भी errors देख रहे हैं, तो अपने internet connection की जांच करें, सुनिश्चित करें कि आपकी API key वैध है, या आधिकारिक troubleshooting docs देखें।

कमांड्स के बारे में अधिक जानकारी के लिए, आप `claude --help` चला सकते हैं जैसा कि आपने किया था, जो अपडेट किए गए version में विकल्प दिखाएगा।

[CLI reference - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
[How to Set Up and Use the Claude CLI Tool Like a Pro](https://medium.com/@riccardo.bernardi.advisor/unlocking-claude-pros-power-how-to-set-up-and-use-the-claude-cli-tool-like-a-pro-against-github-d29f8f682a03)  
[GitHub - anthropics/claude-code](https://github.com/anthropics/claude-code)  
[Claude Code overview - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/overview)