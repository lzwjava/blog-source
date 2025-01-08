---
layout: post  
title: "公司应提供 AI 上下文或代理来促进集成"
---

我有一个朋友在 Greptime DB 工作，最近我一直在思考如何快速将他们的产品集成到现有系统中。

## 上下文

一种可能的做法是提供更多的 AI 上下文。Greptime DB 可以将其文档组织成与 AI 工具（如 ChatGPT）兼容的形式，从而简化集成过程。

Greptime DB 提供的文档可以在 [https://greptime.com](https://greptime.com) 找到，但我在想像 ChatGPT 或 DeepSeek 这样的工具能否有效处理所有页面的内容。此外，很多信息分布在 GitHub 仓库、问题跟踪、内部文档、公共文档以及其他没有明确记录的隐性知识中。

为了解决这个问题，Greptime DB 可能需要创建几个定制化的 GPT。例如，他们可以编写类似这样的提示：

```
Greptime Docs, https://docs.greptime.com
* [快速入门](https://docs.greptime.com/getting-started/quick-start)
* [用户指南](https://docs.greptime.com/user-guide/overview)
* [示例](https://github.com/GreptimeTeam/demo-scene)
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

在回答用户问题之前，请先查看这些文档。
```

这样，用户就可以与一个基于 GPT 的聊天机器人互动，获取基于文档的回答，从而确保更准确的回应。

## 代理

我设想有一个名为 `greptimedb-agent` 的工具，可以简化集成过程。

想象一下，只需要运行一个简单的命令：

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` 会智能地收集当前系统的信息，例如机器详细信息和现有代码，以了解上下文并决定如何最适合地集成 Greptime DB。

这个命令会自动更新你的代码，将当前数据库替换为 Greptime DB，只需几步即可完成集成。

