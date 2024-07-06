---
layout: post
title: "How to Watch YouTube on TV"
---

*This blog post was translated by ChatGPT.*

---

Here we assume you already know how to access the internet using VPN or similar methods. So, how can you watch YouTube on your TV? Flashing the router is a bit troublesome. Here, we use an application to help.

## SmartYoutubeTV

![smart](/assets/images/youtube-tv/smart.png)

Download it and install it on your TV using a USB drive.

![clash](/assets/images/youtube-tv/clash.png)

Next, on the VPN client, select `Allow connect from LAN`. This means allowing other devices on the local network to use this device for internet access.

Then, in the settings of `SmartYoutubeTV`, configure the port.

![proxy1](/assets/images/youtube-tv/proxy1.jpeg)

After setting it up, click the `Test` button to check if it's working. Note that I used a `SOCKS` proxy. I tried using an `HTTP` proxy several times without success. Once the test is successful, click OK, then test it again. Also, you may need to adjust the IP `192.168.1.3` based on your local network address.

That's it, now you can watch YouTube on your TV conveniently.

![tan](/assets/images/youtube-tv/tan.jpeg)

## gfreezy/seeker

This is a GitHub project. The project page has usage instructions. Here, I will supplement some additional points.

![seeker](/assets/images/youtube-tv/seeker.png)

It uses `tun` to implement transparent proxying, similar to Surge's enhanced mode and gateway mode.

I initially used `seeker` to turn my computer into a VPN router. Here is my configuration:

```yml
verbose: true
dns_start_ip: 10.0.0.10
dns_servers:
  - 223.5.5.5:53
  - 114.114.114.114:53  
dns_timeout: 1s
tun_name: utun4
tun_ip: 10.0.0.1
tun_cidr: 10.0.0.0/16
dns_listen: 0.0.0.0:53
gateway_mode: true
ping_timeout: 2s
probe_timeout: 30ms
connect_timeout: 1s
read_timeout: 30s
write_timeout: 5s
max_connect_errors: 2 

servers:
  - name: http proxy server
    addr: 0.0.0.0:7890
    protocol: Http

  - name: https proxy server
    addr: 0.0.0.0:7890
    protocol: Https

rules:
  - 'MATCH,PROXY'
```

Initially, I used a `socks5` proxy, configured like this:

```yml
servers:
  - name: socks5 proxy server
    addr: 0.0.0.0:7891
    protocol: Socks5
```

However, there were many issues, with frequent connection problems. The documentation has a note:

> When using a socks5 proxy, you need to set all direct connection domain names in the configuration file. If you use ss or vmess, you need to add the ss or vmess server domain name to the configuration file. Otherwise, it may cause a dead loop and fail to work properly.

This might be the reason.

Using `seeker` means you need a computer running it as a router. However, using the `proxy` configuration is much more flexible. I can use an iPhone or Android phone to share the proxy port.

## TV Screenshots

While writing this article, I figured out how to take screenshots on the TV. I have a Xiaomi TV. You can double-click the `Home` button on the remote to bring up the app management menu.

![tv_screen](/assets/images/youtube-tv/tv_screen.jpeg)

See the screenshot button? You can easily share it to WeChat. Here you can also close all applications. If some apps are stuck, you can handle them this way.

Alright, let's use the big screen TV to explore the world!