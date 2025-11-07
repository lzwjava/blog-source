---
audio: false
generated: false
image: false
lang: hi
layout: post
title: क्लाउड आईपी, नेटवर्क इंटरफेस और वाईफाई अनुकूलन
translated: true
type: post
---

### विषय-सूची

1. [हेत्ज़नर क्लाउड में फ्लोटिंग आईपी](#हेत्ज़नर-क्लाउड-में-फ्लोटिंग-आइपी)
   - आईपी कॉन्फ़िगरेशन कमांड
   - नेटप्लान कॉन्फ़िगरेशन सेटअप
   - नेटवर्क कॉन्फ़िगरेशन फ़ाइलें

2. [नेटवर्क इंटरफ़ेस प्रबंधन](#नेटवर्क-इंटरफ़ेस-प्रबंधन)
   - TUN इंटरफ़ेस को हटाना
   - इंटरफ़ेस स्थिति निगरानी
   - नेटवर्क समस्या निवारण

3. [LAN आईपी स्कैनर](#lan-आइपी-स्कैनर)
   - पायथन नेटवर्क स्कैनिंग स्क्रिप्ट
   - मल्टीथ्रेडेड होस्ट खोज
   - पोर्ट स्कैनिंग क्षमताएँ
   - स्थानीय नेटवर्क पर डिवाइस पहचान

4. [स्थानीय आईपी को बायपास करना](#स्थानीय-आइपी-को-बायपास-करना)
   - स्थानीय नेटवर्क के लिए प्रॉक्सी कॉन्फ़िगरेशन
   - सबनेट मास्क गणना
   - नेटवर्क रेंज योजना

5. [IPv6 एड्रेस का उपयोग करके SSH कनेक्शन](#ipv6-एड्रेस-का-उपयोग-करके-ssh-कनेक्शन)
   - IPv6 SSH कॉन्फ़िगरेशन
   - SSH कॉन्फ़िग फ़ाइल प्रबंधन
   - विभिन्न एड्रेस प्रकारों के लिए प्रॉक्सी कमांड सेटअप
   - प्रदर्शन अनुकूलन

6. [वाई-फाई स्पीड सुधारना](#वाई-फाई-स्पीड-सुधारना)
   - पुराने vs नए मोडेम प्रदर्शन
   - नेटवर्क सेटअप कॉन्फ़िगरेशन
   - वायर्ड vs वायरलेस ब्रिज मोड
   - नेटवर्क बॉटलनेक का निवारण

7. [OpenWrt रीसेट](#openwrt-रीसेट)
   - वेब इंटरफ़ेस रीसेट विधियाँ
   - कमांड लाइन रीसेट प्रक्रियाएँ
   - फ़ैक्टरी डिफ़ॉल्ट पुनर्स्थापना

---

## हेत्ज़नर क्लाउड में फ्लोटिंग आईपी

### आईपी

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

### नेटप्लान

```bash
touch /etc/netplan/60-floating-ip.yaml
nano /etc/netplan/60-floating-ip.yaml
```

```yaml
network:
   version: 2
   renderer: networkd
   ethernets:
     eth0:
       addresses:
       - 78.47.144.0/32
```

```bash
sudo netplan apply
```

---

## नेटवर्क इंटरफ़ेस प्रबंधन

`tun` इंटरफ़ेस को हटाएं।

```bash
$ ipconfig

outline-tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.85.1  netmask 255.255.255.255  destination 10.0.85.1
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 208  bytes 8712 (8.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 385  bytes 23322 (23.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ sudo ip link delete outline-tun0
```

---

## LAN आईपी स्कैनर

यह पायथन स्क्रिप्ट एक स्थानीय नेटवर्क में सक्रिय आईपी एड्रेस के लिए स्कैन करती है। यह `ping` कमांड का उपयोग करके जांचती है कि कोई होस्ट पहुंच योग्य है या नहीं और मल्टीथ्रेडिंग का उपयोग स्कैनिंग प्रक्रिया को तेज करने के लिए करती है। एक सेमाफोर समवर्ती थ्रेड्स की संख्या को सीमित करता है ताकि सिस्टम पर भारी बोझ न पड़े। स्क्रिप्ट एक नेटवर्क एड्रेस (उदाहरण के लिए, "192.168.1.0/24") इनपुट के रूप में लेती है और प्रत्येक आईपी एड्रेस की स्थिति प्रदर्शित करती है कि वह चालू है या बंद।

यह स्क्रिप्ट नेटवर्क पर डिवाइस की पहचान करने में मदद करती है, जैसे कि TP-LINK मेश राउटर जो वायर्ड ब्रिज मोड में संचालित हो रहा है, सक्रिय आईपी एड्रेस के लिए स्कैन करके।

```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # उपयोग करने के लिए अधिकतम थ्रेड्स की संख्या

def is_host_up(host, port=None):
    """
    पिंग या टेलनेट का उपयोग करके जांचता है कि कोई होस्ट चालू है या नहीं।
    यदि पोर्ट निर्दिष्ट है, तो यह जांचने के लिए टेलनेट का उपयोग करता है कि पोर्ट खुला है या नहीं।
    अन्यथा, पिंग का उपयोग करता है।
    यदि होस्ट चालू है तो True लौटाता है, अन्यथा False।
    """
    if port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
        except socket.error as e:
            return False
        finally:
            sock.close()
    else:
        try:
            # -c 1: केवल 1 पैकेट भेजें
            # -W 1: प्रतिक्रिया के लिए 1 सेकंड प्रतीक्षा करें
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    एक एकल आईपी एड्रेस को स्कैन करता है और उसकी स्थिति प्रदर्शित करता है।
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} चालू है")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} बंद है")

def scan_network(network, port=None):
    """
    थ्रेड्स का उपयोग करके लाइव होस्ट के लिए नेटवर्क को स्कैन करता है, समवर्ती थ्रेड्स की संख्या को सीमित करता है।
    """
    print(f"स्कैन किया जा रहा नेटवर्क: {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # समवर्ती थ्रेड्स की संख्या को सीमित करें
    up_ips = []

    def scan_ip_with_semaphore(ip_str):
        semaphore.acquire()
        try:
            scan_ip(ip_str, up_ips, port)
        finally:
            semaphore.release()

    for ip in ipaddress.IPv4Network(network):
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip_with_semaphore, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return up_ips

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="लाइव होस्ट के लिए नेटवर्क स्कैन करें।")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="स्कैन करने के लिए नेटवर्क (उदाहरण: 192.168.1.0/24)")
    parser.add_argument("-p", "--port", type=int, help="जांचने के लिए पोर्ट (वैकल्पिक)")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\nचालू आईपी:")
    for ip in up_ips:
        print(ip)
```

---

## स्थानीय आईपी को बायपास करना

स्क्रिप्ट सक्रिय आईपी एड्रेस की पहचान करती है। उचित नेटवर्क संचार सुनिश्चित करने के लिए, सुनिश्चित करें कि प्रॉक्सी सेटिंग्स इन स्थानीय आईपी को बायपास करने के लिए कॉन्फ़िगर की गई हैं।

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```

---

## सबनेट मास्क

मेरी दूसरी मशीन आमतौर पर 192.168.1.16 पर होती है।

इसलिए निम्न कमांड का उपयोग करके यह काम करता है:

```bash
python scripts/ip_scan.py 192.168.1.0/27 -p 22
```

क्योंकि 32 - 27 = 5, 2^5 = 32, इसलिए यह `192.168.1.0` से `192.168.1.31` तक को आजमाएगा।

लेकिन `192.168.1.0/28` का उपयोग करते समय यह काम नहीं करता, क्योंकि 2^4 = 16, इसलिए यह `192.168.1.0` से `192.168.1.15` तक को आजमाएगा, जो `192.168.1.16` को कवर नहीं करता।

---

## IPv6 एड्रेस का उपयोग करके SSH कनेक्शन

मैं हेत्ज़नर क्लाउड में IPv6 का उपयोग करके एक मशीन से कनेक्ट करने की कोशिश कर रहा हूँ। `ssh 2a01:4f8:c17:2000::/64` काम नहीं करता, लेकिन `ssh root@2a01:4f8:c17:2000::1` काम करता है।

IPv6 एड्रेस हेत्ज़नर क्लाउड कंसोल से कॉपी किया गया था।

`~/.ssh/config` फ़ाइल को IPv4 और IPv6 एड्रेस के लिए विभिन्न प्रॉक्सी नियम लागू करने के लिए कॉन्फ़िगर किया जा सकता है। यह सेटअप आपको IPv4 एड्रेस के लिए एक प्रॉक्सी कमांड निर्दिष्ट करने की अनुमति देता है जबकि IPv6 एड्रेस को अलग तरीके से हैंडल करता है।

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

जब `ssh root@192.168.1.3` चलाया जाता है, तो निम्नलिखित आउटपुट दिखाता है कि SSH क्लाइंट `~/.ssh/config` फ़ाइल से कॉन्फ़िगरेशन विकल्प लागू कर रहा है:

```bash
debug1: Reading configuration data /Users/lzwjava/.ssh/config
debug1: /Users/lzwjava/.ssh/config line 1: Applying options for 192.168.1.*
debug1: /Users/lzwjava/.ssh/config line 5: Applying options for *.*.*.*
debug2: add_identity_file: ignoring duplicate key ~/.ssh/id_rsa
debug1: /Users/lzwjava/.ssh/config line 10: Applying options for *
debug2: add_identity_file: ignoring duplicate key ~/.ssh/id_rsa
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 21: include /etc/ssh/ssh_config.d/* matched no files
debug1: /etc/ssh/ssh_config line 54: Applying options for *
debug2: resolve_canonicalize: hostname 192.168.1.3 is address
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/Users/lzwjava/.ssh/known_hosts'
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/Users/lzwjava/.ssh/known_hosts2'
debug1: Authenticator provider $SSH_SK_PROVIDER did not resolve; disabling
debug3: channel_clear_timeouts: clearing
debug1: Executing proxy command: exec corkscrew localhost 7890 192.168.1.3 22
```

SSH कनेक्शन स्पीड ध्यान देने योग्य रूप से धीमी थी, इसलिए मैंने निम्नलिखित सरल कॉन्फ़िगरेशन पर वापस आ गया:

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
```

समस्या तब उत्पन्न होती है जब `ProxyCommand corkscrew localhost 7890 %h %p` निर्देश के साथ IPv6 एड्रेस का उपयोग किया जाता है, क्योंकि यह प्रॉक्सी कमांड IPv6 एड्रेस को ठीक से हैंडल नहीं कर सकता।

उपरोक्त कॉन्फ़िगरेशन अभी भी काम नहीं कर रहा है। हालांकि, नीचे वाला ठीक काम कर रहा है।

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host !192.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

---

## वाई-फाई स्पीड सुधारना

### पुराने मोडेम की समस्याएँ

मेरे माता-पिता के घर में मोडेम काफी पुराना है, लगभग 10 साल पुराना। प्रारंभिक नेटवर्क सेटअप था:

मोडेम -> 3m वायरलेस -> TP-Link AX3000 (वायरलेस ब्रिज मोड) -> 2m, एक दीवार, वायरलेस -> लैपटॉप

इससे डाउनलोड स्पीड कम थी, स्पीडटेस्ट परिणाम केवल 10 Mbps था।

सुधारा गया सेटअप वायर्ड कनेक्शन का उपयोग करता था:

मोडेम -> 2m केबल -> TP-Link AX3000 (वायर्ड ब्रिज मोड) -> 4m वायरलेस, एक दीवार -> लैपटॉप

इसने डाउनलोड स्पीड को 90 Mbps तक सुधार दिया।

### नए मोडेम का प्रदर्शन

मेरे अपने घर में, मोडेम नया है, और TP-Link राउटर वायरलेस ब्रिज मोड में अच्छा प्रदर्शन करता है। नेटवर्क सेटअप है:

मोडेम -> 4m वायरलेस -> TP-Link AX3000 (वायरलेस ब्रिज मोड) -> 2m वायरलेस -> लैपटॉप

नेटवर्क की गुणवत्ता अच्छी है।

### समस्या निवारण टिप्स

वाई-फाई स्पीड सुधारने के लिए कोई एक समाधान नहीं है। एक अच्छा तरीका है कि अपने नेटवर्क के प्रत्येक भाग का परीक्षण करने के लिए केबल का उपयोग करें और बोतलगर्दन की पहचान करें। वायर्ड कनेक्शन बनाम वाई-फाई का उपयोग करते समय स्पीड की तुलना करें। इसके अलावा, डिवाइस को सीधे केबल से कनेक्ट करने का प्रयास करें और देखें कि क्या इससे प्रदर्शन में सुधार होता है।

---

## OpenWrt रीसेट

### वेब इंटरफ़ेस के माध्यम से रीसेट करना

राउटर को ईथरनेट केबल के माध्यम से कनेक्ट करने की सलाह दी जाती है। रीसेट के बाद, वाई-फाई SSID अपने डिफ़ॉल्ट सेटिंग्स पर वापस आ जाएगा, जो आपकी अपेक्षा के अनुसार नहीं हो सकता।

### कमांड लाइन (SSH) के माध्यम से रीसेट करना

आप OpenWrt को कमांड लाइन इंटरफ़ेस (SSH) का उपयोग करके डिफ़ॉल्ट सेटिंग्स पर रीसेट कर सकते हैं। यहाँ बताया गया है कि कैसे:

1. अपने OpenWrt राउटर से SSH के माध्यम से कनेक्ट करें।
2. निम्नलिखित कमांड चलाएं:

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3. राउटर डिफ़ॉल्ट सेटिंग्स के साथ रिबूट होगा।

**कमांड्स की व्याख्या:**

* `firstboot`: यह कमांड रीसेट प्रक्रिया शुरू करती है, सभी कॉन्फ़िगरेशन और इंस्टॉल किए गए पैकेज को मिटा देती है।
* `reboot`: यह कमांड राउटर को पुनरारंभ करती है, रीसेट लागू करती है।