---
audio: false
generated: false
lang: zh
layout: post
title: 公司应提供 AI 上下文或代理以促进集成
translated: true
---

我有一个朋友在 Greptime DB 工作，最近我一直在思考如何将他们的产品快速集成到现有系统中。

## 上下文

一种可能的方法是提供更多的 AI 上下文。Greptime DB 可以将其文档组织成适合 AI 工具（如 ChatGPT）使用的方式，从而简化集成过程。

Greptime DB 在 [https://greptime.com](https://greptime.com) 提供了文档，但我想知道像 ChatGPT 或 DeepSeek 这样的工具是否能够高效处理它们文档中的所有页面。此外，大量信息分散在 GitHub 仓库、问题追踪、内部文档、公开文档和其他未显式记录的知识中。

为了解决这个问题，Greptime DB 可能需要创建几个专门的 GPT。例如，他们可以创建类似以下的提示：

```

### Greptime 文档：  
官方文档请访问：[https://docs.greptime.com](https://docs.greptime.com)

* [快速入门指南](https://docs.greptime.com/getting-started/quick-start)  
* [用户指南](https://docs.greptime.com/user-guide/overview)  
* [演示示例](https://github.com/GreptimeTeam/demo-scene)  
* [常见问题](https://docs.greptime.com/faq-and-others/faq)  

### 仓库 URL：  
以下是 GreptimeDB 仓库根目录下的关键目录和文件：

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)  
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)  
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)  
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)  
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)  
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)  

附加的关键文件：

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)  
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)  
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)  
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)  
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)  
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)  

在回应用户提问之前，请先查阅这些资源。

```

这将使用户能够与基于 GPT 的聊天机器人互动，基于文档回答问题，从而确保更准确的答案。

让我们创建这个 GPT：[https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

无法回答以下问题：

```
`greptimedb/src/query/src/query_engine/context.rs` 是关于什么的？
```



## 代理

我设想有一个名为 `greptimedb-agent` 的工具，以简化集成过程。

试想一下，运行一个简单的命令：

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` 将智能地收集有关当前系统的信息，比如机器详细信息和现有代码，以理解上下文并决定如何最佳集成 Greptime DB。

此命令将自动更新您的代码，将 Greptime DB 无缝集成到现有系统中，只需几步便可轻松替换您当前的数据库。

