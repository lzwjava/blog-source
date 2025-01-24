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

* We use Outline Manager to set up our own servers because it is fast and allows us to enjoy the server by ourselves. VPN provider's nodes can often be unreliable. Our servers may also experience issues, but we have much more detailed knowledge of the situation. We can also choose different cloud providers. Additionally, we know whether we are using China Telecom or China Mobile, and whether we are using home Wi-Fi or cellular data.

* It is probably not useful to install OpenWrt on a router to set up a proxy. The main issue is that the GFW can easily ban your proxy server's IP address. It's better to use a subscription method, like with Clash, to easily change settings on your router.
