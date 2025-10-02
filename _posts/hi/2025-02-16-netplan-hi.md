---
audio: false
generated: false
image: false
lang: hi
layout: post
title: नेटप्लान, सिस्टमडी, एसएसएच, कोंडा क्लीनअप
translated: true
---

### विषय-सूची

1. [नेटप्लान आज़माना](#trying-netplan)
   - स्टैटिक आईपी कॉन्फ़िगरेशन के कारण SSH का नुकसान
   - वापस लाने के लिए भौतिक पहुँच की आवश्यकता थी
   - सिस्टम की DNS रिसॉल्वर फ़ाइल संशोधित की गई

2. [सिस्टमडी सेवा](#systemd-service)
   - स्थानीय LLM इन्फेरेंस के लिए सेवा कॉन्फ़िगर करें
   - LLM मॉडल के लिए वेब इंटरफ़ेस सेट अप करें
   - नियम-आधारित प्रॉक्सी टूल सेवा स्थापित करें
   - सेवा प्रबंधन के लिए systemctl कमांड का उपयोग करें

3. [SSH कॉन्फ़िगरेशन](#ssh-configuration)
   - कॉर्कस्क्रू के माध्यम से बाहरी कनेक्शन प्रॉक्सी करें
   - स्थानीय नेटवर्क को प्रॉक्सी से बाहर रखें
   - कीचेन और एजेंट के माध्यम से SSH कुंजियों का प्रबंधन करें
   - डिफ़ॉल्ट निजी कुंजी स्थान निर्दिष्ट करें

4. [Linux में कोंडा हटाएँ](#delete-conda-in-linux)
   - पूरी कोंडा इंस्टॉलेशन डायरेक्टरी हटाएँ
   - bashrc से कोंडा इनिशियलाइज़ेशन कोड हटाएँ
   - PATH एन्वायरनमेंट वेरिएबल अपडेट करें
   - सिस्टम पाथ से कोंडा बाइनरीज़ हटाएँ


## नेटप्लान आज़माना

मैंने उबंटू मशीन को एक स्टैटिक आईपी एड्रेस असाइन करने के लिए नीचे दिए गए कॉन्फ़िगरेशन का प्रयास किया। मैं उस सर्वर पर OpenWebUI और llama.cpp चलाता हूँ।

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

`sudo netplan apply` चलाने के बाद, मशीन को अब `ssh lzw@192.168.1.128` के माध्यम से एक्सेस नहीं किया जा सका।

मशीन में लॉग इन करने, फाइलें हटाने और सेटिंग्स को वापस लाने के लिए कीबोर्ड और माउस का उपयोग किया गया था।

`/etc/resolv.conf` बदल दिया गया था।

---

## सिस्टमडी सेवा

*2025.02.13*

## LLaMA सर्वर सेवा कॉन्फ़िगरेशन

यह खंड बताता है कि LLaMA सर्वर चलाने के लिए एक सिस्टमडी सेवा कैसे स्थापित करें, जो स्थानीय LLM इन्फेरेंस क्षमताएं प्रदान करता है।

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## Open WebUI सेवा कॉन्फ़िगरेशन

यह खंड बताता है कि Open WebUI चलाने के लिए एक सिस्टमडी सेवा कैसे स्थापित करें, जो LLM मॉडल के साथ इंटरैक्ट करने के लिए एक वेब इंटरफ़ेस प्रदान करता है।

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```

## Clash सेवा कॉन्फ़िगरेशन

यह खंड बताता है कि Clash, एक नियम-आधारित प्रॉक्सी टूल चलाने के लिए एक सिस्टमडी सेवा कैसे स्थापित करें।

```bash
[Unit]
Description=Clash Service

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# सेवा फ़ाइल बनाएँ
sudo emacs /etc/systemd/system/clash.service 

# सिस्टमडी डेमन को रिलोड करें
sudo systemctl daemon-reload

# सेवा को सक्षम और प्रारंभ करें
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# स्थिति की जाँच करें
sudo systemctl status clash.service
```

---

## SSH कॉन्फ़िगरेशन

*2025.02.09*

यह `ssh-config` फ़ाइल SSH क्लाइंट व्यवहार को कॉन्फ़िगर करती है। आइए प्रत्येक भाग को समझें:

-   `Host * !192.*.*.*`: यह खंड `192.*.*.*` पैटर्न (आमतौर पर, स्थानीय नेटवर्क पते) से मेल खाने वाले सभी होस्ट को छोड़कर सभी होस्ट पर लागू होता है।
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: यह मुख्य भाग है। यह SSH को लक्ष्य होस्ट से कनेक्ट करने के लिए `corkscrew` प्रोग्राम का उपयोग करने के लिए कहता है।
        -   `corkscrew`: एक उपकरण जो आपको HTTP या HTTPS प्रॉक्सी के माध्यम से SSH कनेक्शन को टनल करने की अनुमति देता है।
        -   `localhost 7890`: प्रॉक्सी सर्वर का पता (`localhost`) और पोर्ट (`7890`) निर्दिष्ट करता है। यह मानता है कि आपके स्थानीय मशीन पर एक प्रॉक्सी सर्वर चल रहा है, जो पोर्ट 7890 पर सुन रहा है (जैसे Shadowsocks, एक SOCKS प्रॉक्सी, या कोई अन्य टनलिंग समाधान)।
        -   `%h`: एक विशेष SSH वेरिएबल जो उस लक्ष्य होस्टनाम तक विस्तारित होता है जिससे आप कनेक्ट करने का प्रयास कर रहे हैं।
        -   `%p`: एक और SSH वेरिएबल जो लक्ष्य पोर्ट तक विस्तारित होता है (SSH के लिए आमतौर पर 22)।
    - संक्षेप में, यह `Host` ब्लॉक स्थानीय नेटवर्क के लिए कनेक्शन को छोड़कर सभी कनेक्शनों के लिए `corkscrew` प्रॉक्सी का उपयोग करने के लिए SSH को कॉन्फ़िगर करता है।

-   `Host *`: यह खंड *सभी* होस्ट पर लागू होता है।
    -   `UseKeychain yes`: macOS पर, यह SSH को आपकी Keychain से SSH कुंजियों को स्टोर और पुनर्प्राप्त करने के लिए कहता है, ताकि आपको हर बार अपना पासवर्ड दर्ज न करना पड़े।
    -   `AddKeysToAgent yes`: यह स्वचालित रूप से आपकी SSH कुंजियों को SSH एजेंट में जोड़ता है, ताकि आपको प्रत्येक रिबूट के बाद उन्हें मैन्युअल रूप से जोड़ने की आवश्यकता न पड़े।
    -   `IdentityFile ~/.ssh/id_rsa`: आपकी निजी SSH कुंजी फ़ाइल का पथ निर्दिष्ट करता है। `~/.ssh/id_rsa` RSA निजी कुंजी के लिए डिफ़ॉल्ट स्थान है।

**संक्षेप में, यह कॉन्फ़िगरेशन स्थानीय नेटवर्क पर उन कनेक्शनों को छोड़कर सभी SSH कनेक्शनों के लिए एक प्रॉक्सी सेट करता है, और यह सुविधा के लिए कुंजी प्रबंधन को कॉन्फ़िगर करता है।**


```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa 
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa    
```

---

## Linux में Conda हटाना

*2025.02.07*

```bash
rm -rf ~/anaconda3
```

`.bashrc` में नीचे दिए गए कोड को डिलीट करें:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/lzw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/lzw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/lzw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/lzw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

पाथ अपडेट करें:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/anaconda3/bin:/home/lzw/anaconda3/condabin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```

से:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```