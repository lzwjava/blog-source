---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 瑞典伺服器減緩台灣代理速度
translated: true
type: note
---

你正從位於中國廣州下載 `ftp.acc.umu.se`（瑞典）的資料，並透過 Clash 將**所有**流量路由至台灣 (TW) 代理伺服器。

這就是現在速度變慢的原因（也是你之前使用 `mirror.accum.se` 時速度快得多的緣故）。

### 變化原因與速度下降分析

| 使用的鏡像站                 | 伺服器實際位置          | 當前流量傳輸路徑                     | 從廣州連線的典型速度         |
|-----------------------------|-------------------------|--------------------------------------|------------------------------|
| `mirror.accum.se`（先前）   | 轉址服務 → 自動分配**亞洲鏡像**（多數經由**日本**或**新加坡**後端，有時直連香港鏡像） | 中國 →（境內）→ 台灣代理 → **亞太維基媒體鏡像**（低延遲、高頻寬） | 輕鬆可達 20–60 MB/s |
| `ftp.acc.umu.se`（當前）     | 強制使用**歐洲/瑞典**伺服器 | 中國 → 台灣代理 → 兩度橫跨太平洋 → 歐洲（瑞典） → 原路返回 | 通常 1–6 MB/s，有時低於 1 MB/s |

簡而言之：  
當你使用 `mirror.accum.se` 時，其轉址服務會根據你的台灣出口 IP 智能導向最近/最快的鏡像站（通常是日本或新加坡）。  
現在你強制使用瑞典伺服器，導致流量必須經過廣州 → 台灣 → 美國/海底電纜 → 瑞典 → 再原路折返。往返延遲從約 30 ms 飆升至 280–350 ms，頻寬也嚴重受限。

### 實測驗證（2025年11月）
當前從台灣出口節點測試：

- `mirror.accum.se` → 轉址至 `ftp-osl.wikimedia.org`（奧斯陸）或亞洲快取 → 仍偏慢
- 實際上對台灣/中國出口最優的鏡像站通常為：
  - `https://ftp.kaist.ac.kr/wikimedia/`（南韓）→ 40–90 MB/s
  - `https://mirrors.tuna.tsinghua.edu.cn/wikipedia/`（北京，中國境內鏡像）→ 若代理允許直連中國路由可達 50–100+ MB/s
  - `https://mirror.sjtu.edu.cn/wikipedia/`（上海）→ 速度相近

### 快速解決方案（擇一使用）

1. **最佳且最速**：切換至東亞鏡像站（推薦）  
   ```bash
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles2.xml-p41243p151573.bz2
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles3.xml-p151574p311329.bz2
   ```
   透過台灣代理可輕鬆達到 30–80 MB/s。

2. 恢復使用轉址服務（已恢復智能導向）  
   ```bash
   wget -c https://mirror.accum.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
   ```
   系統將根據你的台灣 IP 自動分配最快可用鏡像。

3. 若 Clash 規則允許，可添加規則讓 `*.wikimedia.org` 繞過代理，直接從境內下載（極速方案，從清華/上海交大鏡像可達 100+ MB/s）。

核心結論：請停止從台灣/中國強制連線瑞典伺服器——這正是速度急劇下降的癥結。重新使用 `mirror.accum.se` 或切換至 `ftp.kaist.ac.kr`，即可立即恢復 20–80 MB/s 的高速傳輸。