---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Ubuntu 代理繞過主機配置
translated: true
type: note
---

### 在 Ubuntu 手動代理設定中設定多個主機

在 Ubuntu 的手動代理設定（位於**設定 > 網路 > 網路代理 > 手動**）中，「忽略主機」欄位可讓您指定以分號分隔的主機、網域或 IP 範圍清單，以繞過代理。這通常用於本機流量，例如 localhost 或內部網路。您無法將這些設定為*代理伺服器*地址（該欄位預期為單一主機:埠），但它們非常適合填入「忽略主機」欄位。

#### 透過圖形介面設定的步驟：
1. 開啟**設定**（在活動總覽中搜尋）。
2. 前往**網路** > **網路代理**。
3. 將方法設為**手動**。
4. 在**忽略主機**欄位中，輸入以分號分隔的清單（周圍不加空格）：
   ```
   localhost;127.0.0.1;192.168.1.1;192.168.2.1;::1
   ```
   - `localhost`：解析為回送地址。
   - `127.0.0.1`：IPv4 回送地址。
   - `192.168.1.1` 和 `192.168.2.1`：特定本機 IP（可視需要新增更多）。
   - `::1`：IPv6 回送地址。

5. 點擊**套用**儲存。此設定將套用至整個系統（影響瀏覽器、apt 等應用程式）。

#### 使用萬用字元（如 `192.168.1.*`）：
- 「忽略主機」欄位**不支援**直接使用萬用字元（例如 `192.168.1.*`）—該欄位設計用於確切主機、網域尾碼（例如 `*.local`）或 IP 範圍的 CIDR 表示法。
- 請改用 **CIDR 表示法**來設定範圍：
  - 對於 `192.168.1.*`（所有 192.168.1.0/24 子網中的 IP），請使用 `192.168.1.0/24`。
  - 更新後的範例清單：
    ```
    localhost;127.0.0.1;::1;192.168.1.0/24;192.168.2.1
    ```
  - 對於更廣泛的本機網路，可新增 `10.0.0.0/8;172.16.0.0/12;192.168.0.0/16`（常見的私有範圍）。

#### 命令列替代方案（用於腳本或精確設定）：
若偏好使用終端機（或需要自動化），可使用 `gsettings`（適用於現代 Ubuntu）或編輯 `/etc/environment` 進行系統級設定：
- 檢視目前的忽略清單：
  ```
  gsettings get org.gnome.system.proxy ignore-hosts
  ```
- 設定清單（請替換為您的值）：
  ```
  gsettings set org.gnome.system.proxy ignore-hosts "['localhost', '127.0.0.1', '::1', '192.168.1.0/24', '192.168.2.1']"
  ```
- 若要設定永久環境變數（影響部分應用程式）：請新增至 `/etc/environment`：
  ```
  no_proxy="localhost,127.0.0.1,::1,192.168.1.0/24,192.168.2.1"
  ```
  然後重新啟動或執行 `source /etc/environment`。

可透過 ping 清單中的主機或在瀏覽器中檢查代理行為來測試。若出現問題（例如特定應用程式無法運作），環境變數方法通常能涵蓋更多情況。

[設定代理以忽略所有本機地址](https://askubuntu.com/questions/11274/setting-up-proxy-to-ignore-all-local-addresses)  
[如何在 Ubuntu 上設定代理設定](https://phoenixnap.com/kb/ubuntu-proxy-settings)  
[在 no_proxy 環境變數中設定網路範圍](https://unix.stackexchange.com/questions/23452/set-a-network-range-in-the-no-proxy-environment-variable)