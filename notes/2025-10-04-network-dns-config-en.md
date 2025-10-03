---
title: Network Proxy and DNS Configuration
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
model: x-ai/grok-4-fast
---

{
  "dns": ["8.8.8.8", "1.1.1.1"],
  "proxies": {
    "http-proxy": "http://localhost:7890",
    "https-proxy": "http://localhost:7890",
    "no-proxy": "localhost,127.0.0.1,.local"
  }
}