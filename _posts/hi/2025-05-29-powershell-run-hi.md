---
audio: false
generated: true
lang: hi
layout: post
title: 'पावरशेल: वर्तमान टर्मिनल में कमांड चलाएं'
translated: true
type: note
---

`mvn` या WebSphere सर्वर कमांड्स जैसे कमांड्स को नई कमांड प्रॉम्प्ट खोले बिना सीधे वर्तमान PowerShell टर्मिनल में चलाने के लिए, आप कॉल ऑपरेटर (`&`) का उपयोग कर सकते हैं या सीधे कमांड इनवोक कर सकते हैं। यह दृष्टिकोण सुनिश्चित करता है कि कमांड मौजूदा PowerShell सेशन के भीतर ही एक्ज़िक्यूट हो, जिससे आउटपुट और एरर एक ही टर्मिनल में रहें।

यहां बताया गया है कि इसे कैसे करें:

1.  **सीधे कमांड रन करें**:
    यदि कमांड (जैसे, `mvn`) आपके सिस्टम के PATH में है या करंट डायरेक्टरी में एक्सेसिबल है, तो बस कमांड को वैसे ही टाइप करें जैसे आप टर्मिनल में करते हैं:

    ```powershell
    mvn clean install
    ```

    यह `mvn` को सीधे PowerShell सेशन में रन करता है, और आउटपुट करंट टर्मिनल में ही रहता है।

2.  **कॉल ऑपरेटर (`&`) का उपयोग करें**:
    यदि आपको एक्ज़िक्यूटेबल का पथ स्पष्ट रूप से बताने की आवश्यकता है या कमांड एक वेरिएबल में स्टोर है, तो कॉल ऑपरेटर का उपयोग करें:

    ```powershell
    & "C:\path\to\maven\bin\mvn.cmd" clean install
    ```

    WebSphere सर्वर कमांड्स के लिए, यदि आप `wsadmin` या `startServer` जैसी कोई चीज़ रन कर रहे हैं, तो आप यह कर सकते हैं:

    ```powershell
    & "C:\path\to\WebSphere\AppServer\bin\startServer.bat" server1
    ```

    `&` ऑपरेटर सुनिश्चित करता है कि कमांड करंट PowerShell सेशन में रन हो।

3.  **स्पेस या वेरिएबल्स वाले कमांड्स को हैंडल करें**:
    यदि कमांड पथ में स्पेस हैं या यह एक वेरिएबल में स्टोर है, तो पथ को कोट्स में लपेटकर `&` का उपयोग करें:

    ```powershell
    $mvnPath = "C:\Program Files\Apache Maven\bin\mvn.cmd"
    & $mvnPath clean install
    ```

4.  **एनवायरनमेंट वेरिएबल्स सेट करें (यदि आवश्यक हो)**:
    कुछ कमांड्स जैसे `mvn` या WebSphere स्क्रिप्ट्स को एनवायरनमेंट वेरिएबल्स (जैसे, `JAVA_HOME` या `WAS_HOME`) की आवश्यकता हो सकती है। कमांड रन करने से पहले उन्हें स्क्रिप्ट में सेट करें:

    ```powershell
    $env:JAVA_HOME = "C:\path\to\jdk"
    $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
    mvn --version
    ```

    WebSphere के लिए:

    ```powershell
    $env:WAS_HOME = "C:\path\to\WebSphere\AppServer"
    & "$env:WAS_HOME\bin\startServer.bat" server1
    ```

5.  **आउटपुट कैप्चर करें या एरर हैंडल करें**:
    कमांड का आउटपुट कैप्चर करने या एरर को हैंडल करने के लिए, PowerShell के स्टैंडर्ड मैकेनिज्म का उपयोग करें:

    ```powershell
    try {
        $output = & mvn clean install 2>&1
        Write-Output $output
    } catch {
        Write-Error "Maven चलाने में विफल: $_"
    }
    ```

6.  **`Start-Process` से बचें**:
    `Start-Process` के विपरीत, जो एक नई प्रक्रिया लॉन्च करता है (अक्सर एक अलग विंडो में), उपरोक्त तरीके एक्ज़िक्यूशन को करंट सेशन में ही रखते हैं। `Start-Process` का इस तरह उपयोग करने से बचें:

    ```powershell
    # यह एक नया कमांड प्रॉम्प्ट विंडो खोलेगा
    Start-Process -FilePath "mvn" -ArgumentList "clean install"
    ```

    इसके बजाय, डायरेक्ट एक्ज़िक्यूशन या `&` का उपयोग करें।

### उदाहरण स्क्रिप्ट
यहां `mvn` और एक WebSphere कमांड को करंट टर्मिनल में चलाने के लिए एक नमूना PowerShell स्क्रिप्ट दिया गया है:

```powershell
# एनवायरनमेंट वेरिएबल्स सेट करें यदि आवश्यक हो
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11"
$env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
$env:WAS_HOME = "C:\IBM\WebSphere\AppServer"

# Maven कमांड रन करें
Write-Output "Maven चल रहा है..."
& mvn clean install

# WebSphere सर्वर कमांड रन करें
Write-Output "WebSphere सर्वर शुरू हो रहा है..."
& "$env:WAS_HOME\bin\startServer.bat" server1
```

### नोट्स
- सुनिश्चित करें कि कमांड-लाइन टूल्स (`mvn`, `startServer.bat`, आदि) आपके PATH में हैं या एक्ज़िक्यूटेबल का फुल पथ प्रदान करें।
- यदि कमांड को किसी विशिष्ट वर्किंग डायरेक्टरी की आवश्यकता है, तो इसे रन करने से पहले `Set-Location` (या `cd`) का उपयोग करें:

   ```powershell
   Set-Location "C:\path\to\project"
   & mvn clean install
   ```

- ऐसे कमांड्स के लिए जो `.bat` या `.cmd` फाइल्स पर निर्भर करते हैं (WebSphere के साथ आम), `&` ऑपरेटर अच्छी तरह से काम करता है, लेकिन सुनिश्चित करें कि स्क्रिप्ट PowerShell में रन हो, `cmd.exe` में नहीं।
- यदि आपको एनवायरनमेंट वेरिएबल्स या PATH के साथ कोई समस्या आती है, तो उन्हें `Get-ChildItem Env:` से वेरीफाई करें।

यह दृष्टिकोण हर चीज़ को करंट PowerShell टर्मिनल में रखता है, नई विंडोज़ से बचाता है और एक क्लीन वर्कफ़्लो बनाए रखता है। यदि आपके पास कोई विशिष्ट कमांड या सेटअप है जो समस्या पैदा कर रहा है, तो अधिक जानकारी साझा करें, और मैं समाधान को और अधिक अनुकूलित कर सकता हूं।