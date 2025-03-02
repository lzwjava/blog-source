---
audio: true
generated: false
lang: en
layout: post
title: Mesh Router
---

## TP-Link AX3000 - TL-XDR 3050

I started using a mesh router in 2023. I purchased a TP-Link AX3000 system consisting of two mesh routers: a primary unit and a satellite unit. It cost me around 484 CNY at that time, but now it only costs 395 CNY on JD.com.

I initially used this system in my large house but later moved it to my parents' house.

## ZTE AC1200

During some days of the 2025 Spring Festival, my family stayed in my large house and experienced poor WiFi network quality again. To address this, I purchased another mesh router, the ZTE AC1200, which costs around 108 CNY.

Similar products available at Walmart include the TP-Link WiFi Mesh Router, Eero Dual Band Mesh Router, and NetGear Nighthawk AX3000. The prices of most of these products range from 50 USD to 200 USD.

For the ZTE AC1200 mesh router, I could simply purchase one and use bridge mode, allowing it to receive a WiFi signal and then emit its own WiFi signal. It works perfectly. Originally, the router's domain address was 192.168.5.1. After enabling bridge mode, this IP address is no longer accessible. Instead, 192.168.1.1 will redirect you to the main router in your home network. At this point, you can access the router's control center by navigating to http://zte.home.

If you can access the main router, you can see the connected devices and their IP addresses. Then, you can try to access each device to determine which one is the sub-router. In my case, it was 192.168.1.23, which is the address of the ZTE AC1200 mesh router.

For mobile phones, which we move around the home, it is better to use the 2.4 GHz channel as it is more stable. For laptops or desktop computers, which we typically use in our bedrooms or study rooms, it is better to use the 5 GHz channel as it is faster.

After using it for several days, I find that it is a little poor. The speed or signal is poorer than the TL-XDR 3050.

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*Source: JD.com*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*Source: Walmart.com*{: .caption }

## 12V Power for Routers

A USB voltage step-up cable can be used to power routers using a power bank.

However, in some cases, the step-up cable from a power bank may not be able to set up the router correctly. The router may continuously restart.

{: .centered }
![](assets/images/cable-tester/12v.jpg){: .responsive }
*Source: JD.com*{: .caption }

## Two Ways to Help a Sub-Router Find the Main Router

Sometimes, a sub-router cannot easily find the main router when the signal is weak.

If we have to place the sub-router far from the main router, I wonder if it is faster to first connect it in a nearby location and then move it farther away, rather than trying to connect it when it is already in the far location.

Maintaining a connection while nearby allows them to communicate with each other. I have found this method to be more effective.

