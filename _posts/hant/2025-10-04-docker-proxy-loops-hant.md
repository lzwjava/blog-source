---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 避免 Docker 守護程式代理循環
translated: true
type: note
---

### 為何在 Docker 的 `daemon.json` 中設定 `"no-proxy": "localhost,127.0.0.1,.local"` 至關重要

當您使用如 `"http-proxy": "http://localhost:7890"` 的代理設定來配置 Docker daemon（常見於在本機運行的工具如 Clash）時，daemon 預設會將這些規則應用於**所有**外送網路流量。這包括連接到外部 registry 的連線（例如從 `registry-1.docker.io` 拉取 `hello-world` 這類映像）。

然而，若沒有 `no-proxy` 指令，Docker daemon 也會嘗試將**本機連線**——例如連接到您代理伺服器本身的初始 TCP 交握（位於 `localhost:7890`）——透過同一代理進行路由。這會造成典型的**代理迴圈**：

1. Docker 需要從 `registry-1.docker.io` 獲取映像。
2. 它嘗試透過位於 `localhost:7890` 的代理進行連接。
3. 但為了連接到 `localhost:7890`，代理設定再次生效，強制 Docker... 透過位於 `localhost:7890` 的代理進行連接。
4. 這種無限遞迴在 TCP 層級會失敗，因為代理無法代理連接到自身的連線（這導致無解的自指迴圈）。
5. 連線意外中止，產生 `proxyconnect tcp: EOF` 錯誤（EOF 意為「檔案結尾」，表示在代理協商/交握期間過早關閉）。

加入 `"no-proxy": "localhost,127.0.0.1,.local"` 明確告知 daemon 對以下目標的流量**繞過代理**：
- `localhost`（您機器的回送主機名稱），
- `127.0.0.1`（IPv4 回送位址），
- `.local` 網域（常用於 mDNS/區域網路解析）。

這讓 Docker 能夠**直接**連接到位於 localhost 的代理伺服器，而不會透過自身進行迴圈。一旦連接成功，代理便能正常處理對 Docker registry 的外部請求（例如，對 HTTPS 流量透過 HTTP CONNECT）。

簡而言之：它防止 daemon「代理代理伺服器本身」，確保本機代理存取正常運作，同時仍將網際網路導向的流量（如映像拉取）透過代理路由。

若您的設定涉及其他本機服務（例如內部 registry 或本機通訊的容器），在 `no-proxy` 中擴充這些網域/IP 可以防止類似問題。

[Docker Daemon 代理配置](https://docs.docker.com/engine/daemon/proxy/)  
[Docker 代理設定論壇討論](https://forums.docker.com/t/proxy-settings-for-the-docker-daemon/132089)  
[企業防火牆的 Docker 代理指南](https://www.datacamp.com/tutorial/docker-proxy)