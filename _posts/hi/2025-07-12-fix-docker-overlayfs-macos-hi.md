---
audio: false
generated: true
image: false
lang: hi
layout: post
model: google/gemini-2.5-flash
title: मैकओएस पर डॉकर ओवरलेएफएस दोष को ठीक करें
translated: true
type: note
---

आप जो त्रुटि देख रहे हैं, `driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/.../merged: readdirent merged: bad message`, यह Docker की storage mechanism (OverlayFS) में एक गहरी corruption को दर्शाती है, जो अक्सर किसी बीच में रुके ऑपरेशन या host machine के filesystem issue के कारण होती है।

चूंकि आप **macOS** पर हैं (जो Docker Desktop चलाता है), Docker daemon और उसकी storage एक dedicated **Linux Virtual Machine (VM)** के अंदर managed होती है। आपके पास native Linux की तरह सीधा `/var/lib/docker/overlay2` तक access नहीं है, जिससे fix को Docker Desktop app पर ध्यान केंद्रित करके सरल और सुरक्षित बनाया जा सकता है।

macOS पर इसे resolve करने के लिए सबसे सुरक्षित और प्रभावी steps का क्रम यहां दिया गया है:

-----

## 1. कंटेनर को Force-Stop और Force-Remove करें

जो कंटेनर fail हुआ है वह `chat-mongodb` (ID: `ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18`) है। पहले, इसके नाम या ID का उपयोग करके forced removal का प्रयास करें।

1.  **पूरे stack को stop करें** (यह सुनिश्चित करने के लिए कि कोई background process lock नहीं पकड़े हुआ है):

    ```bash
    docker compose stop
    ```

2.  **विशिष्ट कंटेनर को force-remove करें** `-f` flag का उपयोग करके:

    ```bash
    docker rm -f chat-mongodb
    # या ID का उपयोग करके:
    # docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
    ```

3.  **अपने original command को फिर से चलाने का प्रयास करें** (`docker compose down` या समकक्ष)। यदि त्रुटि बनी रहती है, तो step 2 पर जाएं।

-----

## 2. Docker Desktop को Restart करें

एक साधारण restart अक्सर internal VM के अंदर transient lock issues या corrupted states को साफ कर देती है।

### विकल्प A: Menu Bar का उपयोग करके (Recommended)

1.  अपनी macOS menu bar में **Docker Whale icon** पर क्लिक करें।
2.  **Restart** चुनें।

### विकल्प B: Terminal का उपयोग करके

आप application को force quit और फिर से open कर सकते हैं:

```bash
killall Docker && open /Applications/Docker.app
```

Docker के restart होने के बाद, इसे पूरी तरह से start होने के लिए लगभग 30 सेकंड प्रतीक्षा करें, फिर अपने original command को फिर से चलाने का प्रयास करें।

-----

## 3. Docker की Cache और Unused Data को साफ करें (Prune)

यदि restart fail हो जाता है, तो एक शक्तिशाली cleanup command अक्सर unused या "dangling" components को हटाकर deeper corruption issues को resolve कर सकती है जो त्रुटि से संबंधित हो सकते हैं।

**चेतावनी:** यह command सभी stopped containers, unused networks, और dangling images को हटा देती है। यदि आपके पास stopped containers हैं जिन्हें आप रखना चाहते हैं (लेकिन remove नहीं करना चाहते), तो उनका backup लें या इस step को छोड़ दें।

अपने terminal में निम्नलिखित command चलाएँ:

```bash
docker system prune -a --volumes
```

  * **`-a`** (all) सभी unused images को हटाता है (सिर्फ dangling ones ही नहीं)।
  * **`--volumes`** unused anonymous volumes को हटाता है (जो `overlay2` corruption का स्रोत हो सकते हैं)।

आपसे पुष्टि करने के लिए कहा जाएगा। `y` टाइप करें और Enter दबाएं। Prune पूरा होने के बाद, अपने original command को फिर से चलाने का प्रयास करें।

-----

## 4. Docker Desktop को Factory Reset करें

यह **अंतिम उपाय** है क्योंकि यह **आपके सभी containers, images, और volumes को delete कर देगा** (आपके non-mounted volumes में stored कोई भी local data भी शामिल है)। यह internal Docker VM की completely fresh start को force करता है।

1.  अपनी macOS menu bar में **Docker Whale icon** पर क्लिक करें।
2.  **Settings (या Preferences)** $\rightarrow$ **Troubleshoot** पर जाएं।
3.  **Reset to factory settings...** पर क्लिक करें।

Reset के बाद, Docker एक clean slate के साथ restart होगा, और आपको अपने environment को फिर से build करने के लिए अपना `docker compose up` command चलाने में सक्षम होना चाहिए।