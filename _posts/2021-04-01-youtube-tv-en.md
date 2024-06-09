---
layout: post
title: "如何在电视上看 Youtube"
---

*This blog post was translated by Mistral*

---
 title: "How to Watch Youtube on TV"
---

Assuming we know how to browse the internet scientifically, how can we watch Youtube on TV? Using a router is a bit troublesome. Here we borrow an application.

## SmartYoutubeTV

![smart](/assets/images/youtube-tv/smart.png)
Download it and install it on the TV using a U disk.: In the Scientific Surfing application client, select `Allow connect from Lan`. This means that other devices on our local network can connect to this device for internet access.

Next, in the `SmartYoutubeTV` settings, set up the port.

![proxy1](/assets/images/youtube-tv/proxy1.jpeg)

After setting it up, click the `Test` button to try it out. Note that I used a `SOCKS` type proxy here. I tried with `HTTP` but it didn't work a few times. Once the test is successful, click confirm, and then test it out. However, it's not necessarily set to `192.168.1.3` in your case, it depends on your computer's local network address. This looks good. Very convenient.

This is a GitHub project. The project page has usage instructions. Here, I will add some additional notes. It uses tun to implement transparent proxy. Realized similar functionality to Surge's enhanced mode and gateway mode.

At first, I used `seeker` to turn my computer into a proxy routing server. Here's my configuration:

```yaml
verbose: true
dns_start_ip: 10.0.0.10
``` dns_servers:
- 223.5.5.5:53
- 114.114.114.114:53

dns_timeout: 1s

tun_name: utun4
tun_ip: 10.0.0.1
tun_cidr: 10.0.0.0/16

dns_listen: 0.0.0.0:53

gateway_mode: true

ping_timeout: 2s probe_timeout: 30ms
connect_timeout: 1000ms
read_timeout: 30000ms
write_timeout: 5000ms
max_connect_errors: 2

servers:
- name: http proxy server
- addr: 0.0.0.0:7890
- protocol: Http I initially used a `socks5` proxy with the following configuration:

- name: socks5 proxy
- addr: 0.0.0.0:1080

later I changed it to an `https` proxy with the following configuration:

- name: https proxy server
- addr: 0.0.0.0:7890
- protocol: Https

rules:
- 'MATCH,PROXY':
- name: socks5 proxy server
- addr: 0.0.0.0:7891
- protocol: Socks5

However, there are quite a few issues. It often fails to connect. The documentation has this section:

[Problem description and potential solutions]

You may need to check the following:

1. Ensure that the proxy server is running on the specified address and port.
2. Verify that the firewall or security software is not blocking the connection.
3. Check if the DNS server is resolving the domain name correctly.
4. Make sure that the client application supports Socks5 protocol.
5. If using a password, ensure that it is correct.
6. Try using a different proxy server or changing the connection settings.
7. Check the network connectivity and try connecting to other websites or servers to rule out any network issues.
8. If the issue persists, consider contacting the proxy server provider for further assistance. When using a socks5 proxy, all directly connected domain names need to be set in the configuration file. If using ss or vmess, the ss or vmess server domain names also need to be added to the configuration file. Otherwise, there may be a dead loop and it will not be able to function normally.

This might be the reason.

Using `seeker` means that a computer needs to be running it to be used as a router. Using `proxy` configuration methods, however, offers more flexibility. I can share the proxy port using an iPhone or Android phone.

## TV screenshot

When employing a socks5 proxy, all directly linked domain names need to be included in the configuration file. If ss or vmess are utilized, the domain names of the ss or vmess servers also need to be added to the configuration file to prevent dead loops and ensure normal usage.

This could be the cause.

Using `seeker` requires a computer to run it as a router. Using `proxy` configuration methods, on the other hand, provides more flexibility. The proxy port can be shared using an iPhone or Android phone. I was pondering how to take a screenshot on TV while writing this article. I have a Xiaomi TV at home. You can call up the application management menu by pressing the `Home` button twice on the remote control.

Do you see the screenshot button? After that, you can easily share it on WeChat. You can also turn off all applications here. If some applications freeze, you can handle it this way.

Alright. Let's use a large-screen TV to watch the world.
