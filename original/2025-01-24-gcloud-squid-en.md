---
audio: true
lang: en
layout: post
title: Google Cloud Squid Proxy Configuration
---

Squid configuration:

```bash
# DEFINE ACLs
acl local_net src 192.168.1.0/24
acl allowed_ips src 14.19.64.227/32  # Your client IP
acl SSL_ports port 443
acl Safe_ports port 80 443          # HTTP/HTTPS
acl CONNECT method CONNECT

# ALLOW RULES (ORDER MATTERS!)
http_access allow local_net
http_access allow allowed_ips
http_access allow manager localhost
http_access deny manager
http_access allow CONNECT SSL_ports
http_access deny !Safe_ports
http_access deny all

# PROXY SETTINGS
http_port 1128
cache deny all
```

Google Cloud command lines:

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud compute ssh --zone "asia-east1-a" "i25" --project "graphite-ally-445108-k3"
```
