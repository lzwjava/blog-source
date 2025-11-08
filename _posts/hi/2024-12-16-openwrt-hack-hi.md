---
audio: false
generated: false
image: false
lang: hi
layout: post
title: OpenWRT को OpenClash और Shadowsocks
translated: true
type: post
---

### पैकेज सूचियों को अपडेट करना

```bash
root@OpenWrt:~# opkg update
Downloading https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.gz
/var/opkg-lists/openwrt_core में उपलब्ध पैकेजों की सूची अपडेट की गई।
Downloading https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.sig
सिग्नेचर चेक पास हो गया।
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.gz
/var/opkg-lists/openwrt_base में उपलब्ध पैकेजों की सूची अपडेट की गई।
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.sig
सिग्नेचर चेक पास हो गया।
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.gz
/var/opkg-lists/openwrt_luci में उपलब्ध पैकेजों की सूची अपडेट की गई।
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.sig
सिग्नेचर चेक पास हो गया।
root@OpenWrt:~#
```

### Shadowsocks प्लगइन इंस्टॉल करना

`luci-app-shadowsocks-libev` प्लगइन को इंस्टॉल करने के लिए:

```bash
root@OpenWrt:~# opkg install luci-app-shadowsocks-libev
luci-app-shadowsocks-libev (git-22.066.30464-cea4277) को रूट में इंस्टॉल किया जा रहा है...
https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/luci-app-shadowsocks-libev_git-22.066.30464-cea4277_all.ipk डाउनलोड किया जा रहा है
luci-app-shadowsocks-libev को कॉन्फ़िगर किया जा रहा है।
```

### OpenClash इंस्टॉलेशन

अधिक जानकारी के लिए OpenClash के [GitHub रिपॉजिटरी](https://github.com/vernesong/OpenClash?tab=readme-ov-file) को देखें। नीचे आवश्यक घटकों को स्थापित करने के चरण दिए गए हैं।

1. OpenSSH SFTP सर्वर इंस्टॉल करें:

```bash
opkg install openssh-sftp-server
```

(नोट: यह कमांड बिल्कुल वैसी ही रहती है क्योंकि यह एक कोड ब्लॉक है और इसे अनुवादित नहीं किया जाता है।)

2. OpenClash पैकेज को राउटर पर कॉपी करने के लिए `scp` का उपयोग करें:

```bash
   scp luci-app-openclash_0.46.050-beta_all.ipk root@192.168.1.1:~/
   ```

यह कमांड `luci-app-openclash_0.46.050-beta_all.ipk` फ़ाइल को स्थानीय मशीन से IP पते `192.168.1.1` वाले रिमोट मशीन के रूट यूजर के होम डायरेक्टरी (`~/`) में कॉपी करता है।

### OpenClash कॉन्फ़िगरेशन का नमूना

नीचे OpenClash के लिए एक नमूना कॉन्फ़िगरेशन दिया गया है:

```yaml
port: 7890
socks-port: 7891
mixed-port: 7892
allow-lan: true
mode: Rule
log-level: info
external-controller: 0.0.0.0:9090
experimental:
  ignore-resolve-fail: true
```

(यह YAML कॉन्फ़िगरेशन फ़ाइल है और इसे अनुवादित करने की आवश्यकता नहीं है।)

```yaml
dns:
  enable: true
  # ipv6: false
  listen: 0.0.0.0:53
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
    - 119.29.29.29
    - 223.5.5.5
    #- 223.6.6.6
  nameserver:
    - https://223.5.5.5/dns-query
    - https://1.12.12.12/dns-query
    #- https://doh.pub/dns-query
    #- https://dns.alidns.com/dns-query
  fake-ip-filter:
    - "*.lan"
    - "*.localdomain"
    - "*.example"
    - "*.invalid"
    - "*.localhost"
    - "*.test"
    - "*.local"
```

```yaml
proxies:
  - name: "My SS Proxy"
    type: ss
    server: 209.97.0.0
    port: 57500
    cipher: chacha20-ietf-poly1305
    password: "jHLE54zNC000000"
    udp: true
    plugin: ""
    plugin-opts: {}
```

```yaml
proxy-groups:
  - name: "Proxy"
    type: select
    proxies:
      - "My SS Proxy"
```

rules:
  - GEOIP,CN,DIRECT
  - MATCH,Proxy
```

इन चरणों के साथ, आप अपने OpenWRT डिवाइस को उन्नत नेटवर्किंग कॉन्फ़िगरेशन और प्रॉक्सी कार्यक्षमताओं का समर्थन करने के लिए बढ़ा सकते हैं। अपडेट और सर्वोत्तम प्रथाओं के लिए हमेशा आधिकारिक दस्तावेज़ीकरण का संदर्भ लें।