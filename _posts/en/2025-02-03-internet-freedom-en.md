---
audio: true
lang: en
layout: post
title: The Journey to Pursue Internet Freedom
translated: false
---

## Journey

From 2010 to 2013, I used Goagent and the SwitchyOmega proxy tool to bypass the GFW.

Between 2014 and 2015, I used Qujing (曲径) for proxying and followed its author on Twitter, who now lives in Japan.

From June 2016 to July 2018, I used Digital Ocean to host my shadowsocks proxy server.

Starting in 2019, I began using https://zhs.cloud.

In March 2023, I started using a Macao SIM card in my mobile phone for internet access without a proxy or VPN. This cost around 150 CNY per month for 20GB of cellular data, and I used this method for about a year.

In 2024, I began using Outline Manager again with my shadowsocks proxy server, experimenting with various cloud providers.

Currently, my preferred setup is Outline Manager with an Aliyun Hong Kong server for daily use and a non-Hong Kong server (like Singapore or Japan) for AI tools. I maintain the same proxy rules configuration used in Shadowrocket or Clash.

## The Difference Compared to Reversing Myopia

One challenge is fighting the GFW, which is human-made. The other is addressing the principles of eye muscle function.

It's easy to measure the effectiveness of a proxy solution. However, reversing myopia requires time to determine if the eyeball is changing.

## Similarities to Reversing Myopia

A similarity is that both a proxy solution and eyeglasses with a 200-degree reduction often work well. One involves accessing the internet, and the other involves improving eyesight. Both address very important problems.

The underlying principle is that if we understand how the GFW works and find a way to bypass it, the solution should be straightforward.

## Reasoning and Nuance

I still don't fully understand how the GFW works. When my proxy server's IP gets blocked, I now have more ways to investigate the cause.

I can check if the block occurs on the cellular network or home broadband. If it's the cellular network, I can check if it's on 4G or 5G.

Similarly, if my myopia doesn't improve after six months or a year, I need to investigate if there are differences between my eyes. I also need to consider if I've been seeing things just barely clearly without straining my eyes for most of the year.

## Current Status

My proxy server is currently working very well. Download speeds on my phone reach 80 Mbps, and upload speeds reach 50 Mbps when connecting to the Hong Kong proxy server. The same is true on my laptop.

I use the same proxy configurations on my laptop and phones, and they work perfectly. Normally, I use a proxy server to visit sites outside China, and I use a non-HK server for AI tools.

## Recovery

If things are broken, my recovery method is simple. I just need to change the elastic IP of my Aliyun Hong Kong proxy server and upload the new proxy URL to cloud storage. This means I need to run two scripts, which takes about 1 minute, and my laptop and phones can update the proxy server address.

## Regret

I fought with the GFW too many times and for too much time. I tried many proxy protocols, knowing they would be detected by the GFW and get banned. Without a reliable proxy server, it is hard to set up a proxy on an OpenWrt router.

One thing I regret is not learning the techniques of proxy providers earlier, like [zhs.cloud](https://zhs.cloud). I now know most of their secrets.

The other thing is that whenever my proxy server got banned, I didn't think too deeply. It seemed that you just needed to set up a new proxy server to get a new IP address that hadn't been banned. But that was shallow thinking.

## Metrics

I regret not using Speedtest earlier. I knew the name of the tool a long time ago, but I didn't learn how to use it carefully.

It is good to use Speedtest often when connecting to 5G or 4G mobile signal stations or a home broadband network.

For reversing myopia, it is the same. I bought a C-shape eye chart and a standard eye chart.

No measuring, no improvement. Measuring things helps you learn. Using Speedtest often helps me find that on a 5G network, it is easy to exceed 100 Mbps, while on a home broadband network, it is hard to exceed 100 Mbps.

## It Is Still Early

Will the GFW wall fall down in the next few years? It is hard to say.

When, after reversing myopia for two years, I told my friend that my reversing method needed to be improved and that I needed to wear glasses with 200 degrees less than my actual prescription instead of 150 degrees less.

He said that it was no problem, it was fine, not a waste of time, and that it was still early. Yeah. These things are fundamental. Like myopia, people should discover it earlier. Todd Becker shared this discovery on YouTube in 2014, and the videos gained more than 1 million views. And now it is 2025, how many people really know about it in the world? I guess it will be less than 10 thousand.