---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 公司應提供AI背景以促進整合
translated: true
type: post
---

我有一個朋友在 Greptime DB 工作，而我一直在思考如何快速將他們的產品整合到現有系統中。

## 背景

一個潛在的方法是提供更多 AI 上下文。Greptime DB 可以將其文檔組織成與 AI 工具如 ChatGPT 相容的方式，從而簡化整合流程。

Greptime DB 提供文檔於 [https://greptime.com](https://greptime.com)，但我不確定像 ChatGPT 或 DeepSeek 這樣的工具是否能有效處理他們文檔中的所有頁面。此外，大量資訊分散在 GitHub 存儲庫、問題、內部文檔、公開文檔和其他未明確記錄的知識中。

為此，Greptime DB 可能需要創建幾個專用的 GPT。例如，他們可以創建如下的提示：

```

### Greptime 文檔：
官方文檔可於以下位置找到：[https://docs.greptime.com](https://docs.greptime.com)

* [快速入門指南](https://docs.greptime.com/getting-started/quick-start)
* [用戶指南](https://docs.greptime.com/user-guide/overview)
* [演示](https://github.com/GreptimeTeam/demo-scene)
* [常見問題](https://docs.greptime.com/faq-and-others/faq)

### 存儲庫 URL：
以下是 GreptimeDB 存儲庫根目錄的主要目錄和文件：

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

其他主要文件：

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

請在回覆任何用戶查詢前搜索這些資源。

```

這將允許用戶與基於 GPT 的聊天機器人互動，根據文檔回答問題，從而確保更準確的回覆。

讓我們創建這個 GPT：[https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

無法回答此問題，

```
`greptimedb/src/query/src/query_engine/context.rs` 是關於什麼的？
```

## Agent

我設想一個名為 `greptimedb-agent` 的工具來簡化整合流程。

想像執行一個簡單的命令：

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` 將智能地收集有關當前系統的資訊，例如機器詳細資料和現有代碼，以便理解上下文並決定如何最佳整合 Greptime DB。

此命令將自動更新您的代碼以整合 Greptime DB，在幾個步驟中無縫替換您當前的資料庫。