---
audio: true
lang: en
layout: post
title: Set Up Your Proxy Server
---

* To set up a server, use Outline Manager: [https://getoutline.org](https://getoutline.org).  
* Recommended hosting providers include DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr, or Linode. Prefer regions in Singapore or Tokyo. Avoid the Hong Kong region, as tools like ChatGPT and Claude are banned there.  
* Protocols such as Shadowsocks, VMess, and Trojan can easily get banned.  
* Use Linode for fast server migration.  
* You may need a script to automatically renew your server every day.  
* If the proxy server gets banned by the GFW or encounters other issues, you can use a China Telecom Macau SIM card to share cellular data with your laptop. This allows you to set up a new server.  
* For cloud services like Google Cloud Platform, configuring a new server requires an existing proxy server. However, providers like DigitalOcean or Vultr can be set up directly without needing a proxy server.
* Use [Auto SS Config](https://github.com/lzwjava/auto-ss-config) to generate and upload Shadowsocks or Clash subscription URLs.
* Use the snapshot functionality in Digital Ocean. If the IP of the server is banned, create a new droplet from the snapshot of the server and run `install.sh` again.
* Use the reserved IP functionality in Digital Ocean. If the server's IP is banned, assign a new reserved IP.
