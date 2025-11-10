---
audio: false
generated: true
image: false
lang: hi
layout: post
model: google/gemini-2.5-flash
title: डॉकर ओवरलेएफएस हटाने की त्रुटि को ठीक करना
translated: true
type: note
---

आप जो त्रुटि देख रहे हैं, विशेष रूप से यह पंक्ति:
`Error response from daemon: container ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18: driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged: readdirent merged: bad message`
यह **Docker के storage driver**, विशेष रूप से **OverlayFS (overlay2)** में एक **समस्या** को इंगित करती है, जो अक्सर आपकी host machine पर एक corrupted filesystem state से संबंधित होती है। यह आमतौर पर तब होता है जब Docker daemon container की files तक पहुंचने या उन्हें ठीक से साफ़ नहीं कर पाता।

इसे ठीक करने के लिए यहां एक चरण-दर-चरण दृष्टिकोण दिया गया है, जो सबसे कम invasive तरीकों से शुरू होता है।

-----

## 1. Container को रोकें और जबरन हटाएं

`chat-mongodb` container हटाने में विफल रहा। आपको उस विशिष्ट container को लक्षित करने की आवश्यकता होगी।

### A. जबरन हटाने का प्रयास करें

Container को फिर से हटाने का प्रयास करें, लेकिन इस बार force flag (`-f`) का उपयोग करके यह सुनिश्चित करें कि यह चल नहीं रहा है और एक more aggressive removal का प्रयास करें:

```bash
docker rm -f chat-mongodb
```

या container ID का उपयोग करें:

```bash
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
```

### B. Docker Compose Stack को रोकें

यदि container एक बड़े stack का हिस्सा है जिसे आप हटाने का प्रयास कर रहे हैं (जैसा कि `[+] Running 3/3` सुझाव देता है), तो removal का प्रयास करने से पहले services को gracefully रोकने का प्रयास करें:

```bash
docker compose stop
# फिर मूल command फिर से आज़माएं
# e.g., docker compose down
```

-----

## 2. Docker Daemon को पुनरारंभ करें

Docker service का एक साधारण restart अक्सर transient storage driver errors और lock files को साफ़ कर देता है।

### Linux systems के लिए (systemd का उपयोग कर):

```bash
sudo systemctl restart docker
```

### Docker Desktop (macOS/Windows) के लिए:

1.  अपने system tray/menu bar में **Docker icon** पर क्लिक करें।
2.  **Troubleshoot** (या **Settings** $\rightarrow$ **Daemon** $\rightarrow$ **Restart**) पर नेविगेट करें।
3.  **Restart** पर क्लिक करें।

Restart के बाद, container को फिर से हटाने का प्रयास करें।

-----

## 3. Corrupted Directory को मैन्युअल रूप से साफ़ करें

**⚠️ चेतावनी:** इस चरण में Docker की internal file structure में direct manipulation शामिल है और इसे **केवल अंतिम उपाय के रूप में** और **जब Docker daemon STOPPED हो** तभी किया जाना चाहिए। गलत manual deletion आगे corruption का कारण बन सकती है।

त्रुटि OverlayFS storage के भीतर एक विशिष्ट directory की ओर इशारा करती है: `/var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged`।

1.  **Docker daemon को रोकें:**

    ```bash
    sudo systemctl stop docker
    ```

2.  **समस्या वाली directory को मैन्युअल रूप से हटाएं:**

    ```bash
    # केवल आपके त्रुटि संदेश में दिखाई गई directory को हटाएं
    sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f
    ```

    *यदि आपको सटीक directory नहीं मिल रही है, तो आपको एक अधिक सामान्य सफाई का प्रयास करने की आवश्यकता हो सकती है (अगले चरण देखें)।*

3.  **Docker daemon को शुरू करें:**

    ```bash
    sudo systemctl start docker
    ```

4.  **Container/stack को फिर से हटाने का प्रयास करें।**

-----

## 4. Unused Data को Prune करें

यदि उपरोक्त चरण विफल हो जाते हैं, तो आप Docker के built-in cleanup commands का उपयोग कर सकते हैं। यह command सभी stopped containers, सभी networks जिनका उपयोग कम से कम एक container द्वारा नहीं किया जा रहा है, सभी dangling images, और सभी build cache को हटा देती है।

```bash
docker system prune
```

**नोट:** यह command पुष्टि के लिए पूछेगी और उन डेटा को हटा देगी जिन्हें आप रखना चाहते हैं यदि वे सक्रिय रूप से उपयोग में नहीं हैं (जैसे, stopped containers)। सभी unused images (सिर्फ dangling वाले नहीं) को हटाने के लिए `-a` का उपयोग करें।