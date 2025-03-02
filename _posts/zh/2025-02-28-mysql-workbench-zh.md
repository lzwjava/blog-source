---
audio: false
generated: false
lang: zh
layout: post
title: 使用 MySQL Workbench
translated: true
---

### 关键要点
- MySQL Workbench 可能是一个免费的开源工具，用于管理 MySQL 数据库，适用于 Windows、macOS 和 Linux。
- 您可以从官方网站下载它，安装它，并使用服务器详细信息（如主机名和用户名）设置连接。
- 研究表明，您可以使用图形和 SQL 方法创建数据库、表并运行查询。
- 证据表明，它提供了高级功能，如数据建模和服务器管理，这对于初学者来说可能是意外的。

### 什么是 MySQL Workbench？
MySQL Workbench 是一个帮助您设计、开发和管理 MySQL 数据库的工具。它是免费的、开源的，并且适用于 Windows、macOS 和 Linux，使其对许多用户都可访问。它提供了图形界面，这意味着您不总是需要编写代码来管理数据库，尽管如果您愿意，您可以这样做。

### 入门
首先，访问官方下载页面 [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/) 并获取适用于您操作系统的版本。按照提供的安装步骤进行操作，这些步骤在各个平台上都是直观且相似的。

### 设置和使用
安装完成后，打开 MySQL Workbench，通过点击“MySQL Connections”旁边的“+”按钮创建新连接。您需要服务器的主机名、端口（通常是 3306）、用户名和密码等详细信息。测试连接以确保其工作。

连接后，您可以：
- **创建数据库：** 在 SQL 编辑器中运行 `CREATE DATABASE database_name;` 或右键点击“Schemas”并选择“Create Schema...”
- **创建表：** 在 SQL 编辑器中编写 CREATE TABLE 语句，或者通过右键点击数据库使用图形选项。
- **运行查询：** 在 SQL 编辑器中编写您的 SQL 查询并执行它以查看结果。

### 高级功能
除了基础功能，MySQL Workbench 还提供意外的功能，如数据建模，您可以使用 ER 图表设计数据库，以及服务器管理工具，如管理用户和配置。这些可以通过“Model”选项卡和其他菜单进行探索。

---

### 调查说明：MySQL Workbench 使用全面指南

本节提供了使用 MySQL Workbench 的详细探讨，扩展了直接答案，并提供了额外的上下文和技术细节。它旨在涵盖研究中讨论的所有方面，确保用户在各个技能水平上都能获得全面的理解。

#### MySQL Workbench 简介
MySQL Workbench 被描述为数据库架构师、开发人员和数据库管理员（DBAs）的统一视觉工具。它是免费的、开源的，适用于主要操作系统，包括 Windows、macOS 和 Linux，如官方产品页面 [MySQL Workbench](https://www.mysql.com/products/workbench/) 中所述。这种跨平台可用性确保了可访问性，并且它是与 MySQL Server 8.0 开发和测试的，可能与 8.4 及更高版本存在兼容性问题，根据手册 [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/)。该工具集成了数据建模、SQL 开发和管理，使其成为数据库管理的全面解决方案。

#### 安装过程
安装过程因操作系统而异，但 Windows 的详细步骤可以在教程 [Ultimate MySQL Workbench Installation Guide](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation) 中找到。对于 Windows，用户访问 [MySQL Downloads](https://www.mysql.com/downloads/) 选择安装程序，选择自定义设置，并安装 MySQL Server、Workbench 和 shell。该过程涉及授予权限、设置网络和配置根密码，默认设置通常足够。对于其他操作系统，过程类似，用户应遵循特定于平台的说明，确保不需要 Java，因为 MySQL Workbench 使用 Qt 框架。

下面提供了一个总结 Windows 安装步骤的表格，以便更清楚：

| 步骤编号 | 操作                                                                                     | 详细信息                                                                 |
|----------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 0        | 打开 MySQL 网站                                                                         | 访问 [MySQL Downloads](https://www.mysql.com/downloads/)               |
| 1        | 选择下载选项                                                                    | -                                                                       |
| 2        | 选择 MySQL 安装程序 for Windows                                                         | -                                                                       |
| 3        | 选择所需的安装程序并点击下载                                                | -                                                                       |
| 4        | 打开下载的安装程序                                                                  | -                                                                       |
| 5        | 授予权限并选择设置类型                                                     | 点击是，然后选择自定义                                           |
| 6        | 点击下一步                                                                                | -                                                                       |
| 7        | 安装 MySQL 服务器、Workbench 和 shell                                                 | 在安装程序中选择并移动组件                             |
| 8        | 点击下一步，然后执行                                                                   | 下载并安装组件                                         |
| 9        | 配置产品，使用默认类型和网络设置                                | 点击下一步                                                             |
| 10       | 将身份验证设置为强密码加密，设置 MySQL 根密码                  | 点击下一步                                                             |
| 11       | 使用默认 Windows 服务设置，应用配置                                  | 点击执行，然后在配置完成后点击完成                          |
| 12       | 完成安装，启动 MySQL Workbench 和 Shell                                    | 选择本地实例，输入密码以使用                            |

安装后，用户可以通过运行基本的 SQL 命令（如 `Show Databases;`）来验证，如教程中建议的那样，以确保功能。

#### 设置连接
连接到 MySQL 服务器是一个关键步骤，详细指导可以在多个来源中找到，包括 [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/) 和 [w3resource MySQL Workbench Tutorial](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php)。用户打开 MySQL Workbench，点击“MySQL Connections”旁边的“+”按钮，并输入连接名称、方法（通常是标准 TCP/IP）、主机名、端口（默认 3306）、用户名、密码和可选的默认模式。建议测试连接，w3resource 教程中的幻灯片从“MySQL Workbench 新连接步骤 1”到“步骤 4”视觉指导通过该过程。

对于远程连接，额外的考虑因素包括确保 IP 地址在服务器的防火墙中允许，如 [Connect MySQL Workbench](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/) 中所述。这对于连接到基于云的 MySQL 实例（如 Azure Database for MySQL）的用户至关重要，详见 [Quickstart: Connect MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)。

#### 执行数据库操作
连接后，用户可以执行各种操作，图形和 SQL 方法均可用。可以通过 SQL 编辑器使用 `CREATE DATABASE database_name;` 创建数据库，或者通过右键点击“Schemas”并选择“Create Schema...”图形创建，如教程中所示。类似地，创建表涉及编写 CREATE TABLE 语句或使用图形界面，并提供编辑表数据和管理模式的选项，如 [A Complete Guide on MySQL Workbench](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench) 中所述。

运行查询由 SQL 编辑器促进，它提供语法突出显示、自动完成和查询历史记录，增强了可用性。这些功能在 [MySQL Workbench](https://www.mysql.com/products/workbench/) 中得到了突出，使其对初学者和高级用户都友好。

#### 高级功能和工具
MySQL Workbench 除了基础功能外，还提供高级功能，如使用实体关系（ER）图表进行数据建模、正向和反向工程以及更改管理，如 [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/) 中所述。“Model”选项卡允许视觉设计，生成 SQL 脚本，这对于数据库架构师特别有用。服务器管理工具包括管理用户、权限和配置，具有视觉控制台以获得更好的可见性，如 [MySQL Workbench](https://www.mysql.com/products/workbench/) 中所示。

其他功能包括数据库迁移、性能优化和备份/恢复功能，工具如 Data Export 用于备份数据库，详见 [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)。这些高级功能可能对新手数据库管理用户来说是意外的，提供了一套全面的数据库管理工具。

#### 使用技巧和最佳实践
用户应确保 MySQL 服务器正在运行，连接详细信息正确，并检查远程连接的防火墙设置。建议使用强密码和安全方法，特别是对于敏感数据。保存 SQL 脚本并探索版本控制可以增强工作流程，尽管在直接答案中没有详细说明，但这是社区见解的一部分。

#### 结论
本调查说明提供了使用 MySQL Workbench 的全面指南，涵盖安装、连接设置、基本和高级操作以及技巧。它利用了多个可靠的来源，确保截至 2025 年 2 月 28 日的准确性，并旨在为寻求详细技术指导的用户提供帮助。

#### 关键引用
- [MySQL Workbench Manual 约 10 个字](https://dev.mysql.com/doc/workbench/en/)
- [MySQL Workbench 产品页面 约 10 个字](https://www.mysql.com/products/workbench/)
- [Ultimate MySQL Workbench Installation Guide 约 10 个字](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation)
- [SiteGround Tutorials MySQL Workbench 约 10 个字](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)
- [w3resource MySQL Workbench Tutorial 约 10 个字](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php)
- [Connect MySQL Workbench 远程 约 10 个字](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/)
- [Quickstart Connect MySQL Workbench Azure 约 10 个字](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [A Complete Guide on MySQL Workbench 约 10 个字](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench)