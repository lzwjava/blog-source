---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: पावरशेल के माध्यम से टीम्स स्थिति सेट करें
translated: true
type: note
---

नहीं, Microsoft Teams के पास आपकी उपस्थिति स्थिति (presence status) सेट करने के लिए कोई आधिकारिक स्टैंडअलोन कमांड-लाइन यूटिलिटी (जैसे कि एक साधारण `teams --status offline` एक्ज़िक्यूटेबल) नहीं है। अंतर्निहित स्लैश कमांड (जैसे `/away` या `/offline`) केवल Teams ऐप इंटरफेस के भीतर काम करते हैं, टर्मिनल से नहीं।

हालाँकि, आप PowerShell और Microsoft Graph API का उपयोग करके कमांड लाइन के माध्यम से इसे प्राप्त कर सकते हैं। इसके लिए Microsoft Graph PowerShell SDK इंस्टॉल करना, अपने Microsoft अकाउंट के साथ प्रमाणीकरण (authenticate) करना और आपकी उपस्थिति अपडेट करने के लिए एक cmdlet चलाना आवश्यक है। यहां एक चरण-दर-चरण मार्गदर्शिका दी गई है:

### पूर्वापेक्षाएँ
1. PowerShell इंस्टॉल करें (यदि पहले से उपलब्ध नहीं है; यह Windows 10+ में बिल्ट-इन आता है)।
2. व्यवस्थापक के रूप में PowerShell खोलें और मॉड्यूल इंस्टॉल करें:
   ```
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```

### अपनी स्थिति सेट करें
1. Microsoft Graph से कनेक्ट करें (यह ब्राउज़र के माध्यम से प्रमाणीकरण के लिए संकेत देगा):
   ```
   Connect-MgGraph -Scopes "Presence.ReadWrite"
   ```

2. अपनी स्थिति सेट करने के लिए cmdlet चलाएँ। `YourUserId` को अपने Microsoft Entra ID (Azure AD) यूजर आईडी से बदलें (आप इसे `Get-MgUser -UserId your.email@domain.com` के माध्यम से प्राप्त कर सकते हैं)। सामान्य स्थिति मानों में शामिल हैं:
   - `Available`
   - `Away`
   - `Busy`
   - `DoNotDisturb`
   - `Offline` (दूसरों को ऑफलाइन दिखाई देता है)

   ऑफलाइन सेट करने का उदाहरण:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Offline"
   ```

   Away सेट करने का उदाहरण:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Away"
   ```

3. जब काम पूरा हो जाए, तो डिस्कनेक्ट करने के लिए:
   ```
   Disconnect-MgGraph
   ```

### नोट्स
- यह आपकी उपस्थिति को तुरंत अपडेट कर देता है, लेकिन यह आपकी गतिविधि के आधार पर रीसेट हो सकता है (उदाहरण के लिए, निष्क्रिय समय "Away" को ट्रिगर करता है)।
- ऑटोमेशन के लिए (जैसे, शेड्यूल पर स्थिति टॉगल करने के लिए स्क्रिप्ट), उपरोक्त को एक `.ps1` फ़ाइल में रैप करें और इसे टास्क शेड्यूलर के माध्यम से चलाएँ।
- यदि आप एक कस्टम स्थिति संदेश (जैसे, "Out for lunch") भी सेट करना चाहते हैं, तो `Set-MgUserPresenceStatusMessage` का उपयोग करें।
- यह व्यक्तिगत उपयोग के लिए काम करता है लेकिन इसके लिए उचित अनुमतियों की आवश्यकता होती है; एडमिन को Graph API एक्सेस सक्षम करने की आवश्यकता हो सकती है।

निष्क्रिय अवधि के दौरान अपनी स्थिति को "Available" रखने के लिए (सामान्य वर्कअराउंड), ऐसी स्क्रिप्ट्स मौजूद हैं जो गतिविधि का अनुकरण करती हैं (जैसे, हर कुछ मिनटों में Num Lock टॉगल करना), लेकिन वे वास्तविक स्थिति सेटर नहीं हैं।

संदर्भ:  
[Manage Presence Status in Microsoft Teams Using MS Graph PowerShell](https://m365scripts.com/microsoft-teams/manage-presence-status-in-microsoft-teams-using-ms-graph-powershell/)  
[Set-MgUserPresence PowerShell Cmdlet Docs](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users.actions/set-mguserpresence)  
[Reddit Thread on Teams Status via API/CLI](https://www.reddit.com/r/teams/comments/1h5wee9/teams_status_with_api_command_line/)