---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: इंटेलीजे रिमोट डीबगिंग सेटअप गाइड
translated: true
type: note
---

संक्षिप्त उत्तर: हाँ—यदि आप बिल्ड और चल रहे JVM को सिंक में रखते हैं, तो IntelliJ रिमोट डीबग साफ़ तरीके से अटैच हो जाएगी। यहाँ Liberty को स्थानीय रूप से और Cloud Foundry पर चलाते समय ऐसा करने का एक भरोसेमंद, कम-उलझन भरा तरीका दिया गया है।

## 1) अटैच करने से पहले "क्लास मिसमैच" को रोकें

* हमेशा JDKs को एक जैसा रखें: Maven कंपाइलेशन द्वारा इस्तेमाल किया गया JDK, Liberty का JVM, और (यदि CF पर हो तो) Java बिल्डपैक का JDK सभी का मेजर वर्जन मेल खाना चाहिए। Maven में, इसे `maven-compiler-plugin` (`release` या `source/target`) के साथ पिन करें और सुनिश्चित करें कि Liberty/CF भी वही इस्तेमाल कर रहा हो।
* ब्रांच स्विच करते समय या मॉड्यूल को बदलते समय पुराने बाइटकोड को साफ़ करें: `mvn clean package -DskipTests` सबसे सरल गार्डरेल है।
* IntelliJ में, यदि आपने IDE बिल्ड और Maven बिल्ड को मिलाया है तो एक बार "Rebuild Project" भी करें।

## 2) केवल तभी ऑटो-रीबिल्ड करें जब ज़रूरी हो (30-मिनट का नियम)

यदि आप केवल तभी रीबिल्ड करना चाहते हैं जब कंपाइल्ड क्लासेज़ 30 मिनट से पुरानी हों, तो Maven को एक छोटे से चेक में रैप करें।

### Bash (macOS/Linux)

```bash
#!/usr/bin/env bash
set -euo pipefail

CLASSES_DIR="target/classes"
THRESHOLD_MIN=30

needs_build() {
  # क्या अभी तक कोई क्लासेज़ नहीं हैं?
  [[ ! -d "$CLASSES_DIR" ]] && return 0
  # क्या नवीनतम क्लास का संशोधन समय थ्रेशोल्ड से पुराना है?
  last_mod_epoch=$(find "$CLASSES_DIR" -type f -name '*.class' -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
  [[ -z "${last_mod_epoch:-}" ]] && return 0
  now_epoch=$(date +%s)
  diff_min=$(( ( now_epoch - ${last_mod_epoch%.*} ) / 60 ))
  (( diff_min >= THRESHOLD_MIN ))
}

if needs_build; then
  echo "Classes are old (>= ${THRESHOLD_MIN}m) or missing — building…"
  mvn clean package -DskipTests
else
  echo "Classes are fresh (< ${THRESHOLD_MIN}m) — skipping build."
fi
```

### PowerShell (Windows)

```powershell
$classes = "target\classes"
$thresholdMin = 30

function Needs-Build {
  if (-not (Test-Path $classes)) { return $true }
  $last = Get-ChildItem $classes -Recurse -Filter *.class |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
  if (-not $last) { return $true }
  $age = (New-TimeSpan -Start $last.LastWriteTime -End (Get-Date)).TotalMinutes
  return ($age -ge $thresholdMin)
}

if (Needs-Build) {
  Write-Host "Classes are old (>= $thresholdMin m) or missing — building…"
  mvn clean package -DskipTests
} else {
  Write-Host "Classes are fresh (< $thresholdMin m) — skipping build."
}
```

## 3) Liberty (स्थानीय) — डीबग मोड में शुरू करें और IntelliJ से अटैच करें

आपके पास दो आसान विकल्प हैं:

**A. वन-शॉट डीबग स्टार्ट**

```bash
server debug myServer   # डिफ़ॉल्ट JDWP पोर्ट 7777 पर
```

**B. परमानेंट कॉन्फ़िग**

* `wlp/usr/servers/myServer/jvm.options` में:

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777
```

* या env वेरिएबल के ज़रिए:

```
WLP_DEBUG_ADDRESS=7777
WLP_DEBUG_SUSPEND=false
```

**IntelliJ अटैच**

* Run → “Edit Configurations…” → “Remote JVM Debug”.
* Host: `localhost`, Port: `7777`.
* Debug पर क्लिक करें; आपको "Connected to the target VM…" दिखना चाहिए और ब्रेकपॉइंट्स बाइंड हो जाएंगे।

> टिप: रीबिल्ड के बाद, Liberty ज़्यादातर फीचर्स के लिए अपडेटेड क्लासेज़ को हॉट स्वैप के ज़रिए पिक कर लेता है। यदि किसी मेथड सिग्नेचर या क्लास स्ट्रक्चर में बदलाव हुआ है, तो उन बदलावों को लोड करने के लिए आपको सर्वर रीस्टार्ट की ज़रूरत पड़ेगी।

## 4) Cloud Foundry (PCF) — यथार्थवादी दृष्टिकोण

CF एप्स को अपनी रूटिंग लेयर के पीछे चलाता है; आप आमतौर पर सीधे एक JDWP पोर्ट एक्सपोज़ नहीं कर सकते। आपके पास दो काम करने लायक पैटर्न हैं:

**विकल्प 1: बिल्डपैक डीबग + SSH टनल (केवल डेव/स्टेजिंग के लिए)**

1. Java बिल्डपैक में JVM डीबग सक्षम करें:

   * पुश से पहले env सेट करें (नाम बिल्डपैक वर्जन के अनुसार थोड़े अलग हो सकते हैं):

   ```
   cf set-env <APP> JBP_CONFIG_DEBUG '{enabled: true, port: 7777}'
   ```
2. रीस्टेज करें:

   ```
   cf restage <APP>
   ```
3. एक SSH टनल खोलें:

   ```
   cf ssh -N -L 7777:localhost:7777 <APP>
   ```
4. IntelliJ में, `localhost:7777` से अटैच करें।

**विकल्प 2: JDWP के बजाय CF SSH JMX/डायग्नोस्टिक्स का उपयोग करें**

* जब सीधा JDWP की अनुमति नहीं हो, तो इन पर भरोसा करें:

  * ऐप लॉग + टार्गेटेड लॉगर्स,
  * `cf ssh` + `jcmd`/`jmap` (यदि मौजूद हो) के ज़रिए थ्रेड/हीप डंप,
  * Liberty के ट्रेस और हेल्थ एंडपॉइंट्स जैसे फीचर फ्लैग।

> यथार्थ जाँच: कई CF संगठन प्रोड में डीबग पोर्ट्स को डिसेबल कर देते हैं। CF पर रिमोट JDWP को गैर-प्रोड स्पेस के लिए एक डीबग-ओन्ली पथ के रूप में देखें। यदि आपकी प्लेटफ़ॉर्म टीम इसे ब्लॉक करती है, तो लॉग + SSH डायग्नोस्टिक्स पर वापस आ जाएँ।

## 5) आम "ब्रेकपॉइंट्स बाइंड नहीं हो पाए" के कारण (और उनके समाधान)

* **क्लास फ़ाइल मिसमैच**: क्लीन रीबिल्ड करें; रनटाइम क्लासपाथ पर क्लास की केवल एक कॉपी हो, यह सुनिश्चित करें (फैट JARs या डुप्लिकेट मॉड्यूल्स पर नज़र रखें)।
* **गलत JDWP पोर्ट**: पुष्टि करें कि Liberty वास्तव में सुन रहा है (स्थानीय रूप से `server debug` लॉग या `netstat`; CF के लिए, SSH टनल लाइन मेल खानी चाहिए)।
* **अलग JDK मेजर वर्जन**: सुनिश्चित करें कि Maven/Liberty/CF JDKs एक जैसे हैं (उदा., सभी Java 17)।
* **कंपाइलर डीबग इनफॉर्मेशन स्ट्रिप हो गई**: सुनिश्चित करें कि `maven-compiler-plugin` `-g:none` का उपयोग नहीं कर रहा है। डिफ़ॉल्ट ठीक है; यदि कस्टमाइज़ किया गया है, तो `-g` शामिल करें।
* **रीलोड ज़रूरी**: सिग्नेचर बदलाव के बाद, Liberty को रीस्टार्ट करें (या CF पर रीस्टेज करें)।

---

यदि आप ऊपर बताए गए तरीके से सेटअप करते हैं—या तो हमेशा `mvn clean package` चलाएँ या "30-मिनट फ्रेशनेस" रैपर का उपयोग करें—तो IntelliJ रिमोट डीबग Liberty से विश्वसनीय रूप से अटैच हो जाएगी, और यह गैर-प्रोड में CF पर SSH टनल के ज़रिए काम कर सकती है।