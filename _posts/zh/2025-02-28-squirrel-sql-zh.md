---
audio: false
generated: false
lang: zh
layout: post
title: 连接到数据库的Squirrel SQL
translated: true
---

### 关键要点
- 看起来 Squirrel SQL 是一个基于 Java 的 SQL 客户端，用于通过 JDBC 驱动程序连接数据库。
- 研究表明，你需要安装 Java，获取适合你数据库的 JDBC 驱动程序，并创建一个包含连接详细信息的别名来使用它。
- 证据表明，步骤包括下载 Squirrel SQL，设置驱动程序，并通过用户友好的界面连接。

### 使用 Squirrel SQL 入门
Squirrel SQL 是一个帮助你管理和查询数据库的工具，设计上友好，适合新手。以下是如何开始的方法：

#### 安装
首先，确保你的电脑上安装了 Java，可以从 [这个网站](https://www.java.com/download) 下载。然后，从 [SourceForge](https://sourceforge.net/p/squirrel-sql) 下载 Squirrel SQL，并按照安装向导进行设置。

#### 连接到数据库
要连接，你需要特定数据库的 JDBC 驱动程序（例如 MySQL、PostgreSQL）。可以在数据库供应商的网站上找到这些驱动程序，例如 [MySQL](https://dev.mysql.com/downloads/connector/j) 或 [PostgreSQL](https://jdbc.postgresql.org/download.html)。在 Squirrel SQL 中的“查看驱动程序”下添加驱动程序，然后创建一个别名，包含你的数据库 URL（例如，“jdbc:mysql://localhost:3306/mydatabase”），用户名和密码。双击别名以连接。

#### 使用界面
连接后，使用“对象”选项卡浏览数据库结构和数据，使用“SQL”选项卡运行查询。它还支持数据导入和图形可视化等功能，这对于专注于 SQL 管理的工具来说可能是意外的。

---

### 使用 Squirrel SQL 和连接数据库的综合指南

这个笔记提供了使用 Squirrel SQL，一个基于 Java 的图形 SQL 客户端，进行数据库管理的详细探讨，特别是连接到数据库。它扩展了初步指导，提供了基于可用资源的专业和全面的概述，适合寻求深入理解的用户。

#### Squirrel SQL 简介
Squirrel SQL 是一个开源的 Java SQL 客户端程序，适用于任何符合 JDBC 的数据库，使用户能够查看结构、浏览数据和执行 SQL 命令。它在 GNU 更小的通用公共许可证下发布，确保了可访问性和灵活性。由于其 Java 基础，它可以在任何具有 JVM 的平台上运行，使其适用于 Windows、Linux 和 macOS 用户。

#### 安装过程
安装过程从确保安装 Java 开始，因为 Squirrel SQL 至少需要 Java 6 版本 3.0，尽管较新版本可能需要更新。用户可以从 [这个网站](https://www.java.com/download) 下载 Java。接下来，从 [SourceForge](https://sourceforge.net/p/squirrel-sql) 下载 Squirrel SQL，作为 JAR 文件（例如，“squirrel-sql-version-install.jar”）。安装涉及使用 Java 运行 JAR 文件并使用设置助手，提供“基本”或“标准”安装选项，后者包括有用的插件，如代码补全和语法突出显示。

#### 连接到数据库：分步指南
连接到数据库涉及几个关键步骤，每个步骤都需要注意细节，以确保成功集成：

1. **获取 JDBC 驱动程序**：每种数据库类型都需要特定的 JDBC 驱动程序。例如，MySQL 用户可以从 [MySQL](https://dev.mysql.com/downloads/connector/j) 下载，PostgreSQL 从 [PostgreSQL](https://jdbc.postgresql.org/download.html)，Oracle 从 [Oracle](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html)。驱动程序通常是 JAR 文件，促进 Squirrel SQL 和数据库之间的通信。

2. **在 Squirrel SQL 中添加驱动程序**：打开 Squirrel SQL，导航到“窗口”>“查看驱动程序”，然后点击“+”图标添加新驱动程序。命名它（例如，“MySQL 驱动程序”），输入类名（例如，“com.mysql.cj JDBC 驱动程序”用于最近的 MySQL 版本，注意版本差异），并在“额外类路径”选项卡中添加 JAR 文件路径。蓝色勾号表示驱动程序在 JVM 类路径中；红色 X 表示需要从供应商下载。

3. **创建别名**：从菜单中，选择“别名”>“新建别名...”或使用 Ctrl+N。输入别名名称，选择驱动程序，并输入数据库 URL。URL 格式各异：
   - MySQL: “jdbc:mysql://hostname:port/database_name”
   - PostgreSQL: “jdbc:postgresql://hostname:port/database_name”
   - Oracle: “jdbc:oracle:thin:@//hostname:port/SID”
   提供用户名和密码，确保详细信息与数据库管理员提供的信息一致。

4. **建立连接**：在“别名”窗口中双击别名以打开会话。Squirrel SQL 支持多个同时会话，适用于比较数据或在连接之间共享 SQL 语句。

#### 使用 Squirrel SQL：界面和功能
连接后，Squirrel SQL 提供了一个强大的界面进行数据库交互：

- **对象选项卡**：此选项卡允许浏览数据库对象，如目录、模式、表、触发器、视图、序列、过程和 UDTs。用户可以导航树形，编辑值，插入或删除行，并导入/导出数据，增强数据管理能力。

- **SQL 选项卡**：SQL 编辑器基于 fifesoft.com 的 RSyntaxTextArea，提供语法突出显示，并支持打开、创建、保存和执行 SQL 文件。它适合运行查询，包括复杂的连接，结果以包含元数据的表格返回。

- **额外功能**：Squirrel SQL 包括 Excel/CSV 数据导入插件、DBCopy 插件、SQL 书签插件（用于用户定义的代码模板，例如常见的 SQL 和 DDL 语句）、SQL 验证插件和特定于数据库的插件，如 DB2、Firebird 和 Derby。图形插件可视化表关系和外键，这对于期望仅基本 SQL 功能的用户来说可能是意外的。用户可以使用 Ctrl+J 插入书签 SQL 模板，简化重复任务。

#### 故障排除和考虑事项
用户可能会遇到连接问题，可以通过以下方法解决：
- 确保数据库服务器正在运行并可访问。
- 验证 JDBC 驱动程序安装和类名的准确性，因为版本可能不同（例如，较旧的 MySQL 驱动程序使用“com.mysql JDBC 驱动程序”）。
- 检查 URL 是否有拼写错误或缺少参数，例如 SSL 设置（例如，MySQL 的“?useSSL=false”）。
- 咨询数据库供应商的文档，了解特定要求，例如安全连接的信任存储。

界面支持如保加利亚语、巴西葡萄牙语、中文、捷克语、法语、德语、意大利语、日语、波兰语、西班牙语和俄语等语言的 UI 翻译，满足全球用户的需求。

#### 比较见解
与其他 SQL 客户端相比，Squirrel SQL 的优势在于其插件架构，允许数据库供应商特定的扩展和广泛兼容性。然而，安装可能不如预期那样直观，因为有 Java 依赖，文档可能稀疏，通常需要第三方教程，如 [SqlBot](https://www.sqlbot.co/blog/squirrel-sql-review-and tutorial) 提供的详细指导。

#### 表：连接到 MySQL 的关键步骤示例
为了说明，以下是连接到 MySQL 的表格，这是一个常见的用例：

| 步骤                  | 详细信息                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------|
| 1. 安装 Java           | 所需版本：至少 Java 6 适用于 SQuirreL SQL 版本 3.0；从 [这个网站](https://www.java.com/download) 下载 |
| 2. 下载 SQuirreL SQL   | 从 [SourceForge](https://sourceforge.net/p/squirrel-sql) 可用，作为 JAR 文件（例如，“squirrel-sql-version-install.jar”） |
| 3. 安装 SQuirreL SQL   | 使用设置助手；选择“基本”或“标准”安装，包括代码补全等插件 |
| 4. 定义驱动程序       | 指向 MySQL 的 JDBC JAR 文件（例如，mysql-connector-java-8.0.32.jar）；在驱动程序窗口中检查状态（蓝色勾号表示在 JVM 类路径中，红色 X 表示未在 JVM 类路径中）；从 [MySQL](https://dev.mysql.com/downloads/connector/j) 获取驱动程序 |
| 5. 创建别名           | 从菜单栏中，选择别名 > 新建别名... 或使用 Ctrl+N；输入数据库 URL（例如，“jdbc:mysql://localhost:3306/mydatabase”），用户名和密码；咨询数据库管理员获取详细信息 |

这个表格，源自教程，突出了过程，注意双击别名打开会话，通过对象或 SQL 选项卡进行交互。

#### 结论
Squirrel SQL 提供了一个全面的数据库管理解决方案，详细步骤连接和丰富的功能集，包括插件和可视化。用户应确保正确设置，利用供应商文档和第三方资源进行故障排除，确保在数据库交互中获得顺利体验，截至 2025 年 2 月 28 日。

#### 关键引用
- [SQuirreL SQL - 评论和教程 SqlBot](https://www.sqlbot.co/blog/squirrel-sql-review-and tutorial)
- [SQuirreL SQL 客户端 Wikipedia](https://en.wikipedia.org/wiki/SQuirreL_SQL Client)
- [SQuirreL SQL 客户端下载 SourceForge](https://sourceforge.net/p/squirrel-sql)
- [Java 下载官方网站](https://www.java.com/download)
- [MySQL Connector/J 下载页面](https://dev.mysql.com/downloads/connector/j)
- [PostgreSQL JDBC 驱动程序下载](https://jdbc.postgresql.org/download.html)
- [Oracle JDBC 驱动程序下载](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html)