---
audio: false
generated: true
lang: hi
layout: post
title: 'PowerShell: नेट टीसीपी कनेक्शन प्राप्त करने का उपयोग'
translated: true
type: note
---

PowerShell में `Get-NetTCPConnection` cmdlet, Windows सिस्टम पर TCP कनेक्शन के बारे में जानकारी प्राप्त करता है। यह `NetTCPIP` मॉड्यूल का हिस्सा है, जो Windows 8/Windows Server 2012 और बाद के संस्करणों पर उपलब्ध है। इसका उपयोग कैसे करें, इसका एक संक्षिप्त मार्गदर्शन नीचे दिया गया है:

### बेसिक उपयोग
सभी सक्रिय TCP कनेक्शनों की सूची देखने के लिए `Get-NetTCPConnection` चलाएँ:

```powershell
Get-NetTCPConnection
```

यह LocalAddress, LocalPort, RemoteAddress, RemotePort, State, और OwningProcess जैसे विवरण लौटाता है।

### सामान्य पैरामीटर
- **-State**: कनेक्शन स्टेट के आधार पर फ़िल्टर करें (जैसे, Established, Listening, TimeWait)।
  ```powershell
  Get-NetTCPConnection -State Established
  ```
- **-LocalPort**: लोकल पोर्ट नंबर के आधार पर फ़िल्टर करें।
  ```powershell
  Get-NetTCPConnection -LocalPort 80
  ```
- **-RemoteAddress**: रिमोट IP एड्रेस के आधार पर फ़िल्टर करें।
  ```powershell
  Get-NetTCPConnection -RemoteAddress 192.168.1.1
  ```
- **-RemotePort**: रिमोट पोर्ट के आधार पर फ़िल्टर करें।
  ```powershell
  Get-NetTCPConnection -RemotePort 443
  ```
- **-OwningProcess**: कनेक्शन के मालिक प्रोसेस ID (PID) के आधार पर फ़िल्टर करें।
  ```powershell
  Get-NetTCPConnection -OwningProcess 1234
  ```

### फ़िल्टर को संयोजित करना
अधिक विशिष्ट परिणामों के लिए आप पैरामीटर्स को संयोजित कर सकते हैं:
```powershell
Get-NetTCPConnection -State Established -LocalPort 80
```

### विशिष्ट गुण दिखाएँ
केवल वांछित गुण दिखाने के लिए `Select-Object` का उपयोग करें:
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### प्रोसेस विवरण ढूँढें
कनेक्शन के पीछे के प्रोसेस की पहचान करने के लिए, `Get-Process` के साथ संयोजित करें:
```powershell
Get-NetTCPConnection -LocalPort 80 | ForEach-Object { Get-Process -Id $_.OwningProcess }
```

### आउटपुट को सॉर्ट और फ़ॉर्मेट करें
परिणामों को सॉर्ट करें (जैसे, LocalPort के आधार पर) और टेबल के रूप में फ़ॉर्मेट करें:
```powershell
Get-NetTCPConnection | Sort-Object LocalPort | Format-Table LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### प्रैक्टिकल उदाहरण
1. **सभी लिसनिंग कनेक्शनों की सूची बनाएँ:**
   ```powershell
   Get-NetTCPConnection -State Listening
   ```
2. **किसी विशिष्ट रिमोट सर्वर से कनेक्शन ढूँढें:**
   ```powershell
   Get-NetTCPConnection -RemoteAddress "8.8.8.8"
   ```
3. **जाँचें कि कोई विशिष्ट पोर्ट किस प्रोसेस द्वारा उपयोग किया जा रहा है:**
   ```powershell
   $connection = Get-NetTCPConnection -LocalPort 8080
   Get-Process -Id $connection.OwningProcess
   ```

### नोट्स
- **एडमिन विशेषाधिकार**: कुछ विवरण (जैसे, सिस्टम प्रोसेस के लिए OwningProcess) के लिए PowerShell को एडमिनिस्ट्रेटर के रूप में चलाने की आवश्यकता हो सकती है।
- **IPv4/IPv6**: यह cmdlet दोनों IPv4 और IPv6 कनेक्शन को हैंडल करता है।
- **परिणाम एक्सपोर्ट करें**: आउटपुट को `Export-Csv` के साथ एक फ़ाइल में सेव करें:
  ```powershell
  Get-NetTCPConnection | Export-Csv -Path "tcp_connections.csv" -NoTypeInformation
  ```

अधिक विवरण के लिए, चलाएँ:
```powershell
Get-Help Get-NetTCPConnection -Full
```

यदि आपको विशिष्ट उदाहरण चाहिए या कोई विशेष उपयोग का मामला है, तो मुझे बताएं!