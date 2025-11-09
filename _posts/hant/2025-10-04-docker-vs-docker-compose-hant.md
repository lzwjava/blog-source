---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Docker 與 Docker Compose 的差異
translated: true
type: note
---

### Docker vs. Docker Compose：主要差異

Docker 與 Docker Compose 雖然相關，但在容器化工作流程中擔當不同角色。Docker 是基礎技術，而 Docker Compose 則在其之上建構，用於處理更複雜的設定。

#### 什麼是 Docker？
Docker 是一個用於在輕量級、可移植的 **容器** 內開發、運送和執行應用程式的平台。這些容器將應用程式及其所有依賴項（程式碼、執行環境、函式庫等）打包在一起，確保其在開發、測試和生產等不同環境中一致運行。您主要透過命令列介面（CLI）使用 `docker run`、`docker build` 和 `docker ps` 等指令來管理單個容器，與 Docker 進行互動。

#### 什麼是 Docker Compose？
Docker Compose 是一個編排工具，它擴展了 Docker 的功能以處理 **多容器應用程式**。它使用一個簡單的 YAML 檔案（通常是 `docker-compose.yml`）來定義您的整個應用程式堆疊——包括多個服務、網路、儲存卷和環境變數。您無需處理數十個 `docker run` 指令，只需一個 `docker-compose up` 指令即可啟動所有內容。

#### 主要差異
以下是一個快速比較：

| 面向              | Docker                              | Docker Compose                          |
|---------------------|-------------------------------------|-----------------------------------------|
| **主要焦點**   | 建構、運行和管理 **單一容器** | 定義和編排 **多容器應用程式** |
| **設定方式**   | 內嵌的 CLI 參數（例如 `docker run -p 80:80 image`） | 使用 YAML 檔案進行宣告式設定（服務、連接埠、儲存卷） |
| **常用指令**        | `docker run`, `docker build` 等 | `docker-compose up`, `down`, `scale` 等 |
| **適用範圍**           | 底層的容器生命週期管理       | 高階的應用程式堆疊（例如 應用程式 + 資料庫 + 快取） |
| **網路/依賴** | 需為每個容器手動設定          | 自動設定（例如，服務可以透過名稱互相引用） |
| **使用情境**        | 簡單、獨立的服務           | 複雜應用程式，如帶有資料庫的網頁伺服器 |

簡而言之：Docker 就像執行單一任務的單引擎車輛，而 Docker Compose 則是協調多輛車輛完成旅程的車隊管理器。

### 為什麼我們需要 Docker Compose？
雖然 Docker 本身對於單容器應用程式已經很強大，但現實世界的應用程式通常涉及多個相互連接的元件（例如前端、後端 API、資料庫和 Redis 快取）。以下是 Docker Compose 不可或缺的原因：

- **簡化多容器管理**：沒有它，您需要手動啟動/停止容器、配置網路，並透過重複的 CLI 指令處理依賴關係——這會變得混亂且容易出錯。Compose 透過一個檔案和指令將此過程自動化。

- **可重現性與協作**：YAML 檔案如同藍圖。團隊成員可以透過 `docker-compose up` 啟動完全相同的環境，使開發保持一致性和可移植性（非常適合 CI/CD 流程）。

- **提升開發效率**：諸如服務連結（例如，您的應用程式透過主機名自動連接到資料庫）和用於即時程式碼重新載入的儲存卷掛載等功能，可以加速迭代。您還可以擴展服務（例如 `docker-compose scale web=3`）而無需重新建置映像。

- **環境隔離**：它為每個專案建立隔離的網路和儲存卷，避免在本地運行多個應用程式時發生衝突。

本質上，Docker Compose 將 Docker 從一個單打獨鬥的工具轉變為適用於現代基於微服務架構的團隊協作工具。如果您剛開始使用，可以嘗試為一個 WordPress + MySQL 堆疊建立一個簡單的 `docker-compose.yml` 來體驗其魔力。

#### 參考資料
- [Docker vs. Docker Compose: Simple and Fun Explanation](https://medium.com/@ShantKhayalian/docker-vs-docker-compose-simple-and-fun-explanation-4811582127f7)
- [What is the difference between docker and docker-compose](https://stackoverflow.com/questions/37966552/what-is-the-difference-between-docker-and-docker-compose)
- [How To Choose Between Docker Compose vs Docker?](https://cyberpanel.net/blog/docker-compose-vs-docker)
- [Docker Compose - What is It, Example & Tutorial](https://spacelift.io/blog/docker-compose)