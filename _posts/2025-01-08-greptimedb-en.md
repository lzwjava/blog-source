---
layout: post  
title: "Companies Should Provide AI Context or Agents to Facilitate Integration"
---

I have a friend who works at Greptime DB, and I’ve been thinking about how to quickly integrate their product into existing systems.

## Context

One potential approach is to provide more AI context. Greptime DB could organize its documentation in a way that is compatible with AI tools like ChatGPT, streamlining the integration process.

Greptime DB offers documentation at [https://greptime.com](https://greptime.com), but I wonder if tools like ChatGPT or DeepSeek can efficiently process all the pages in their documentation. Additionally, a wealth of information is spread across GitHub repositories, issues, internal documents, public documents, and other pieces of hidden knowledge that aren’t explicitly documented.

To address this, Greptime DB might need to create several specialized GPTs. For example, they could create prompts like this:

```
Greptime Docs, https://docs.greptime.com
* [Quickstart](https://docs.greptime.com/getting-started/quick-start)
* [User Guide](https://docs.greptime.com/user-guide/overview)
* [Demos](https://github.com/GreptimeTeam/demo-scene)
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

Please review these documents before answering any user queries.
```

This would allow users to interact with a GPT-based chatbot that answers questions based on the documentation, ensuring more accurate responses.

## Agent

I envision a tool called `greptimedb-agent` to simplify the integration process.

Imagine running a simple command like:

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` would intelligently gather information about the current system, such as the machine details and the existing code, in order to understand the context and decide how best to integrate Greptime DB.

This command would automatically update your code to integrate Greptime DB, seamlessly replacing your current database with Greptime DB in just a few steps.

