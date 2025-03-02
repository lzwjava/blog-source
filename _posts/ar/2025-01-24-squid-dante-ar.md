---
audio: false
generated: true
lang: ar
layout: post
title: 'أداة الوكيل: Squid و Danted'
translated: true
---

## Danted

تعليمات سطر الأوامر:

```bash
sudo apt-get install dante-server
sudo apt install net-tools
ifconfig
danted
tail -f danted.log
```

تكوين `/etc/danted.conf`:

```bash
logoutput: /home/lzwjava/danted.log

internal: 0.0.0.0 port = 1080  # الاستماع على جميع الواجهات
external: ens4
# المصادقة (السماح للجميع بدون بيانات اعتماد)
method: none

# القواعد
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    method: none  # السماح صراحة بدون مصادقة
}

socks pass {  # استخدام "socks pass" بدلاً من "pass" المهمل
    from: 0.0.0.0/0 to: 0.0.0.0/0
    protocol: tcp udp
    method: none  # مطلوب للسماح بدون مصادقة
}
```

## تكوين Squid

```bash
acl all src all
http_access allow all
http_access deny all
http_port 1128
```

فشلت المحاولة. يجب تنظيف `squid.conf` أولاً.

```
1737725543.236   1822 14.31.165.22 TCP_TUNNEL/200 1232 CONNECT 91.108.56.121:443 - HIER_DIRECT/91.108.56.121 -
```

## أوامر سطر الأوامر لـ Google Cloud

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud compute ssh --zone "asia-east1-a" "i25" --project "graphite-ally-445108-k3"
```