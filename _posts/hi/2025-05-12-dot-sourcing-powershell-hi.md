---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: डॉट सोर्सिंग पॉवरशेल स्क्रिप्ट्स
translated: true
type: note
---

### डॉट सोर्सिंग PowerShell Functions in .ps1 Files

डॉट सोर्सिंग (`.` ऑपरेटर का उपयोग करके) एक PowerShell स्क्रिप्ट (.ps1 फ़ाइल) को वर्तमान सेशन की मेमोरी में लोड करता है, जिससे उसके functions और variables उपयोग के लिए उपलब्ध हो जाते हैं बिना स्क्रिप्ट के top-level code को execute किए। यह modules या reusable code को import करने के लिए उपयोगी है।

#### बेसिक सिंटैक्स
अपने PowerShell सेशन में यह कमांड चलाएँ:
```
. Path\To\YourScript.ps1
```
- `Path\To\YourScript.ps1` को वास्तविक फ़ाइल पथ से बदलें (विश्वसनीयता के लिए absolute paths का उपयोग करें)।
- उदाहरण: `. C:\Scripts\MyFunctions.ps1` – यह उस फ़ाइल के functions को आपके सेशन में लोड करता है।

#### यह कैसे काम करता है
- स्क्रिप्ट में परिभाषित functions आपके वर्तमान सेशन में callable हो जाते हैं।
- Variables भी import हो जाते हैं, लेकिन केवल तभी जब वे locally scoped न हों।
- Production scripts में डॉट सोर्सिंग से बचें; बेहतर organization के लिए modules का उपयोग करें।
- टिप: यदि पथ में spaces हैं, तो उसे quotes में wrap करें: `. "C:\My Scripts\Functions.ps1"`

Common issue: यदि स्क्रिप्ट में syntax errors हैं, तो डॉट सोर्सिंग fail हो जाएगी और एक error देगी। `PowerShell -Command ". .\YourScript.ps1"` को command prompt से चलाकर test करें।

### Using PowerShell Execution Policy

Execution policies security settings होती हैं जो यह प्रतिबंधित करती हैं कि PowerShell कौन सी scripts चला सकता है, जिससे malicious code execution रोकी जा सके। ये per-scope (जैसे, machine-wide, user-specific) होती हैं।

#### वर्तमान Policy जांचना
PowerShell में यह चलाएँ:
```
Get-ExecutionPolicy
```
- Output उदाहरण: `Restricted` (सभी scripts को ब्लॉक करता है), `AllSigned` (केवल signed scripts), `RemoteSigned` (signed remote scripts, local allowed), या `Unrestricted`।

#### Policy सेट या बदलना
`Set-ExecutionPolicy` का उपयोग करें (machine-level changes के लिए admin rights की आवश्यकता होती है):
- Locally written scripts को allow करने का उदाहरण: `Set-ExecutionPolicy RemoteSigned`
- बिना prompts के force करें: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force`
- Per-scope: `Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser` (केवल आपके user account को प्रभावित करता है)।

#### Common Policies
- `Restricted`: Default; कोई scripts नहीं चलती।
- `AllSigned`: Digital signatures की आवश्यकता होती है (secure लेकिन inconvenient)।
- `RemoteSigned`: Security को संतुलित करती है—local scripts allow करती है, remote ones को sign करती है।
- `Unrestricted`: सभी scripts चलाती है (risky; सावधानी से उपयोग करें)।
- `Bypass`: पूरी तरह से unrestricted, automation के लिए।

टिप: Policies console sessions पर लागू होती हैं, लेकिन ISE या VS Code पर तब तक नहीं जब तक set न की गई हों। `Write-Host "Hello"` जैसी sample script चलाकर changes को test करें। अधिक जानकारी के लिए, Microsoft की docs देखें: `help about_Execution_Policies`। यदि enterprise में हैं, तो Group Policy local settings को override कर सकती है।