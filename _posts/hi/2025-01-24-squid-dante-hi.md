---
audio: false
generated: false
image: false
lang: hi
layout: post
title: 'प्रॉक्सी टूल: Squid और Danted'
translated: true
type: post
---

## Danted

कमांड लाइन निर्देश:

```bash
sudo apt-get install dante-server
sudo apt install net-tools
ifconfig
danted
tail -f danted.log
```

`/etc/danted.conf` कॉन्फ़िगरेशन:

```bash
logoutput: /home/lzwjava/danted.log

internal: 0.0.0.0 port = 1080  # सभी इंटरफेस पर सुनें
external: ens4
# प्रमाणीकरण (क्रेडेंशियल्स के बिना सभी को अनुमति दें)
method: none

# नियम
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    method: none  # स्पष्ट रूप से बिना प्रमाणीकरण की अनुमति दें
}

socks pass {  # "pass" के बजाय "socks pass" का उपयोग करें
    from: 0.0.0.0/0 to: 0.0.0.0/0
    protocol: tcp udp
    method: none  # बिना प्रमाणीकरण के लिए आवश्यक
}
```

## Squid कॉन्फ़िगरेशन

```bash
acl all src all
http_access allow all
http_access deny all
http_port 1128
```

प्रयास विफल। पहले `squid.conf` को साफ़ करने की आवश्यकता है।

```
1737725543.236   1822 14.31.165.22 TCP_TUNNEL/200 1232 CONNECT 91.108.56.121:443 - HIER_DIRECT/91.108.56.121 -
```

## Google Cloud कमांड लाइन्स

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud compute ssh --zone "asia-east1-a" "i25" --project "graphite-ally-445108-k3"
```