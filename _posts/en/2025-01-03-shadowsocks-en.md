---
audio: true
generated: false
lang: en
layout: post
title: Shadowsocks Proxy Issues
translated: false
---


Zhiwei: 

I went out for a barbeque with a friend and used Shadowsocks with a Singapore-based server as my proxy to bypass the Great Firewall (GFW). While using 5G outside, I couldn't connect, and the test timed out when trying to access YouTube. However, when I'm at home using 4G or my China Telecom home network, Shadowsocks works fine. Why is this happening?

Mistral:

It sounds like you're experiencing connectivity issues with your Shadowsocks proxy when using 5G outside, but not when using 4G or your home network. There could be several reasons for this:

1. Network Configuration Differences:
   - 5G Network: The 5G network might have different configurations or restrictions compared to 4G. Some carriers might have stricter firewall rules or different network routing for 5G, which could affect the performance of your Shadowsocks proxy.
   - 4G Network: The 4G network might have more relaxed settings or better routing that allows your Shadowsocks proxy to function correctly.

2. ISP Restrictions:
   - Carrier Policies: Different carriers might have different policies regarding the use of VPNs or proxies. Your 5G carrier might have stricter policies that block or throttle VPN traffic, including Shadowsocks.
   - Home Network: Your home network, provided by China Telecom, might have fewer restrictions, allowing Shadowsocks to work without issues.

3. Signal Strength and Stability:
   - 5G Signal: The stability and strength of the 5G signal can vary, especially in outdoor environments. Weak or unstable signals can cause connectivity issues, including timeouts.
   - 4G Signal: The 4G signal might be more stable and consistent, providing a better connection for your Shadowsocks proxy.

4. Proxy Server Location:
   - Singapore Server: The location of your Shadowsocks server in Singapore might affect latency and connectivity. The 5G network might have higher latency or less optimal routing to the Singapore server compared to the 4G network or your home network.

5. Device Settings:
   - Configuration: Ensure that your device settings are correctly configured for using Shadowsocks. Sometimes, switching networks (from 5G to 4G or home Wi-Fi) can cause settings to reset or change.
   - App Permissions: Make sure that the Shadowsocks app has the necessary permissions to operate on different networks.

### Troubleshooting Steps:

1. Check Network Settings:
   - Ensure that your Shadowsocks settings are correctly configured for both 5G and 4G networks.
   - Verify that there are no specific restrictions or settings on your 5G network that might be blocking the proxy.

2. Test Different Servers:
   - Try connecting to different Shadowsocks servers to see if the issue is specific to the Singapore server.
   - Check the latency and stability of the connection to the server.

3. Contact Your Carrier:
   - If the issue persists, contact your 5G carrier to inquire about any restrictions or settings that might be affecting your Shadowsocks connection.

4. Update Software:
   - Ensure that your Shadowsocks app and device software are up to date. Sometimes, updates can resolve connectivity issues.

5. Use Alternative Proxies:
   - Consider using alternative proxy services or VPNs that might have better compatibility with your 5G network.

By systematically checking these factors, you should be able to identify the cause of the connectivity issue and find a suitable solution.

-- 

Update:

Actually, my home Wi-Fi uses China Mobile Communications Corporation, and its address is like 120.235.8.xx.

Interestingly, I've observed inconsistent connectivity patterns - while my proxy server functions normally on cellular data and China Telecom networks, it occasionally fails to connect when using my home Wi-Fi network.
