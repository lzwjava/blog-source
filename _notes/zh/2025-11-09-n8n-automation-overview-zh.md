---
audio: false
generated: true
image: false
lang: zh
layout: post
model: x-ai/grok-4-fast
title: n8n工作流自动化平台概览
translated: true
---

n8n（发音为"n-eight-n"）是一个面向技术团队和开发者的开源工作流自动化平台。它允许您连接不同的应用程序、服务和API，以自动化重复性任务、数据流和复杂流程，而无需严重依赖自定义代码——尽管在需要时支持代码。可以将其视为Zapier或Make等工具的自托管替代方案，但具有更大的灵活性，包括构建多步骤AI代理、集成任何大型语言模型（LLM）以及在自己的基础设施上运行所有内容以获得更好的数据隐私和控制的能力。

n8n的核心采用基于节点的可视化界面，通过拖放和连接"节点"（代表触发器、操作或转换的构建块）来构建工作流。它采用公平代码许可（在GitHub上源码可用），支持400多个预构建集成（例如Google Sheets、Slack、OpenAI、GitHub），可以处理从简单通知到高级AI驱动自动化（如总结工单或生成内容）的所有任务。

### 主要特性
- **可视化工作流构建器**：拖放节点实现无代码设置，支持嵌入JavaScript、Python甚至npm/Python库以实现自定义逻辑
- **AI集成**：使用LangChain等工具构建多步骤代理，连接任何LLM（本地或云端），并通过Slack、SMS或语音创建用于查询数据或执行任务的聊天界面
- **自托管与安全**：通过Docker或npm完全本地部署；支持SSO、加密密钥、RBAC和审计日志。无供应商锁定——也可托管自己的AI模型
- **混合开发**：将UI与代码结合；重放数据进行测试，内联日志进行调试，提供1,700多个模板快速入门
- **可扩展性**：企业级功能如工作流历史、Git版本控制、隔离环境以及面向客户的自动化嵌入
- **性能示例**：Delivery Hero等公司每月节省200多个小时；StepStone将数周工作压缩至数小时

与Zapier相比，n8n对开发者更友好（代码访问、自托管）、更具成本效益（核心免费、无按任务收费）且更注重隐私（数据不通过第三方路由）。非常适合金融、医疗或内部运营中处理敏感数据的团队。

# n8n使用指南：完整教程

本指南将带您从设置到高级用法。我们将使用一个实际示例：每天发送新文章邮件的RSS订阅监视器（可扩展为AI摘要）。假设您具备基本技术常识；n8n运行在Node.js上。

## 1. 安装与设置

n8n轻量且启动迅速。前提条件：本地安装需要Node.js（推荐v18+）；容器部署需要Docker。生产环境请使用DigitalOcean或AWS等VPS。

### 快速本地启动（开发/测试）
1. 打开终端
2. 运行：`npx n8n`
   - 这将临时下载并启动n8n
3. 在浏览器中访问 `http://localhost:5678`
   - 默认登录：初始无需凭证（后续为安全设置）

### 持久本地安装（npm）
1. 全局安装：`npm install n8n -g`
2. 启动：`n8n start`
3. 访问 `http://localhost:5678`

### Docker（推荐生产环境）
1. 拉取镜像：`docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`
   - 这将映射数据持久化卷
2. 高级设置（如PostgreSQL数据库）：使用文档中的`docker-compose.yml`
3. 访问 `http://localhost:5678`

### 云选项
- **n8n Cloud**：n8n.io的托管服务——注册后几分钟即可部署，免费版有限制
- **第三方PaaS**：使用Render、Railway或Sevalla（一键模板）。Sevalla示例：
  1. 在sevalla.com注册
  2. 选择"n8n"模板，部署资源（如1 CPU、1GB RAM）
  3. 获得类似`https://your-n8n.sevalla.app`的URL

**提示**：自托管时通过HTTPS保护（使用Nginx等反向代理），设置环境变量（如`N8N_BASIC_AUTH_ACTIVE=true`），并备份`~/.n8n`文件夹。高流量工作流使用队列模式扩展。

## 2. 界面概览

打开后：
- **画布**：工作流的空白工作区。点击"+"添加节点
- **节点面板**：可搜索的400多个节点库（如"计划触发器"）
- **执行面板**：测试期间实时显示数据流
- **侧边栏**：工作流设置、执行历史、模板
- **顶部栏**：保存、激活/停用切换、分享/导出选项

工作流自动保存；团队中使用Git进行版本控制。

## 3. 核心概念

- **工作流**：定义自动化逻辑的连接节点序列。活动工作流在触发时运行；非活动工作流用于测试
- **节点**：模块化块：
  - **触发器**：启动工作流（如计划任务的Schedule、HTTP事件的Webhook、订阅源的RSS Read）
  - **操作**：执行工作（如发送邮件、API的HTTP请求、自定义代码的Function）
  - **核心节点**：IF（条件）、Merge（合并数据）、Set（操作变量）
- **连接**：节点间的箭头显示数据流（JSON格式）。一个节点的数据馈送到下一个节点
- **表达式**：动态占位符如`{{ $json.title }}`提取数据（如文章标题）到字段。使用`$now`获取时间戳或`$input.all()`处理批次
- **凭证**：API密钥/OAuth的安全存储。每个服务设置一次（如Gmail OAuth）并在节点间重用
- **执行**：工作流的运行；查看日志、重放数据或调试错误

## 4. 创建第一个工作流：分步指南

让我们构建"每日RSS摘要邮件"。

1. **创建新工作流**：
   - 点击"新建" > 命名为"RSS摘要"
   - 画布打开

2. **添加触发器节点**：
   - 点击"+" > 搜索"Schedule Trigger"
   - 配置：触发器"每天"上午9:00（cron：`0 9 * * *`）
   - 测试：点击"执行节点"（立即运行一次）

3. **添加数据获取节点**：
   - 触发器后点击"+" > "RSS Read"
   - URL：`https://blog.cloudflare.com/rss/`
   - 执行：获取项目（如包含title、link、pubDate的JSON）

4. **转换数据（可选函数节点）**：
   - "+" > "Function"
   - 代码：
     ```
     // 限制为前3个项目
     return items.slice(0, 3);
     ```
   - 这对传入数据运行JS

5. **添加操作节点**：
   - "+" > "Gmail"（或SMTP的"Email Send"）
   - 凭证：点击"创建新凭证" > Gmail的OAuth（遵循Google认证流程）
   - 收件人：您的邮箱
   - 主题：`每日摘要：{{ $input.first().json.title }}`
   - 消息：使用表达式循环项目：
     ```
     {{#each $input.all()}}
     - {{ $json.title }}: {{ $json.link }} ({{ $json.pubDate }})
     {{/each}}
     ```
   - （使用类似Handlebars的语法进行循环）

6. **连接与测试**：
   - 拖拽箭头：触发器 → RSS → 函数 → 邮件
   - "执行工作流"：观察数据流；检查收件箱
   - 修复错误：红色节点高亮问题（如无效凭证）

7. **激活**：
   - 切换"活动"开启。现在每天运行

保存并导出为JSON以供分享。

## 5. 构建更复杂的工作流

- **条件**：在RSS后添加"IF"节点：`{{ $json.pubDate }} > {{ $now.minus({days:1}) }}`过滤新项目
- **循环与批次**：使用"Split In Batches"处理大型数据集
- **错误处理**：添加"Error Trigger"工作流或"IF"进行重试。使用"Set"记录错误
- **API集成**：自定义端点的"HTTP Request"节点（如POST到Slack webhook）
- **数据操作**：使用"Edit Fields"或函数节点调整JSON
- **测试**：重放特定执行；在节点中模拟数据

示例：Twitter监视器
1. 触发器："Twitter Trigger"提及
2. AI节点："OpenAI"分类情感
3. IF：正面 → CRM添加；负面 → Slack警报

## 6. 高级用法与最佳实践

- **AI工作流**：添加"AI Agent"节点 > 与工具链式连接（如搜索、摘要）。通过"Ollama"节点集成本地LLM
- **自定义节点**：通过JS构建（文档教程）；发布到社区
- **扩展**：使用队列模式（`N8N_WORKER=1`）、外部数据库（PostgreSQL）和实时webhook
- **安全**：加密密钥、团队使用RBAC、审计日志
- **调试**：函数中的内联日志（`console.log(items)`）；使用Git版本控制
- **常见陷阱**：注意数据类型（全部JSON）；处理节点中的速率限制；在AI之前从简单开始
- **扩展**：嵌入应用、使用模板（1,700多个可用）或npm获取额外功能

生产环境通过外部工具监控；自托管节省成本（对比Zapier的$20+/月）。

## 参考资料
- [n8n官网](https://n8n.io/)
- [n8n文档 - 安装](https://docs.n8n.io/hosting/installation/)
- [freeCodeCamp初学者指南](https://www.freecodecamp.org/news/a-beginners-guide-to-automation-with-n8n/)
- [n8n工作流文档](https://docs.n8n.io/workflows/)
- [Medium：掌握n8n指南](https://medium.com/data-science-collective/mastering-n8n-from-scratch-a-step-by-step-guide-for-beginners-its-easier-than-you-think-2d7ca5d47277)
- [维基百科：n8n](https://en.wikipedia.org/wiki/N8n)