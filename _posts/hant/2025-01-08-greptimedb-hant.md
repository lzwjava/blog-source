---
audio: false
generated: false
lang: hant
layout: post
title: 公司應提供AI背景或代理以促進整合
translated: true
---

我有一位在Greptime DB工作的朋友，我一直在思考如何快速将他们的产品集成到现有系统中。

## 背景

一种潜在的方法是提供更多的AI上下文。Greptime DB可以以与ChatGPT等AI工具兼容的方式组织其文档，从而简化集成过程。

Greptime DB在[https://greptime.com](https://greptime.com)提供了文档，但我怀疑像ChatGPT或DeepSeek这样的工具是否能高效处理其文档中的所有页面。此外，大量信息分散在GitHub仓库、问题、内部文档、公共文档以及其他未明确记录的隐藏知识中。

为了解决这个问题，Greptime DB可能需要创建几个专门的GPT。例如，他们可以创建如下提示：

```

### Greptime 文档：  
官方文档可在以下网址找到：[https://docs.greptime.com](https://docs.greptime.com)

* [快速入门指南](https://docs.greptime.com/getting-started/quick-start)  
* [用户指南](https://docs.greptime.com/user-guide/overview)  
* [演示](https://github.com/GreptimeTeam/demo-scene)  
* [常见问题解答](https://docs.greptime.com/faq-and-others/faq)  

### 仓库URL：
以下是GreptimeDB仓库根目录下的关键目录和文件：

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)  
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)  
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)  
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)  
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)  
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)  

其他关键文件：

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)  
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)  
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)  
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)  
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)  
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)  

在回答任何用户查询之前，请先搜索这些资源。

```

这将允许用户与基于GPT的聊天机器人互动，该机器人根据文档回答问题，确保更准确的响应。

让我们创建这个GPT：[https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

无法回答这个问题，

```
`greptimedb/src/query/src/query_engine/context.rs` 是关于什么的？
```