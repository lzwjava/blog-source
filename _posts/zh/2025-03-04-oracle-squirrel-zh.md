---
audio: false
generated: true
lang: zh
layout: post
title: 将 Oracle JDBC 驱动程序添加到 Squirrel SQL 客户端
translated: true
---

要将 Oracle JDBC 驱动程序添加到 Squirrel SQL Client，请按照以下详细步骤操作。此过程涉及配置驱动程序并为您的 Oracle 数据库设置连接别名。

### 第 1 步：定位所需文件
您需要 Oracle JDBC 驱动程序文件，具体是 `ojdbc.jar`。该文件包含使 Squirrel SQL Client 能够连接到 Oracle 数据库所需的类。请确保您已下载此文件（例如，从 Oracle 网站或您的数据库管理员处）并知道其在系统中的位置。

### 第 2 步：启动 Squirrel SQL Client
在计算机上打开 Squirrel SQL Client 应用程序。

### 第 3 步：访问驱动程序选项卡
在 Squirrel SQL Client 接口的左侧，找到并点击 **驱动程序** 选项卡。此部分允许您管理应用程序可用的 JDBC 驱动程序。

### 第 4 步：添加新驱动程序
- 在驱动程序选项卡中，点击 **“+”** 按钮以打开“添加驱动程序”对话框。

### 第 5 步：命名驱动程序
- 在“添加驱动程序”对话框的“名称”字段中，输入 **Oracle Thin Driver**。这是一个描述性名称，用于在 Squirrel SQL Client 中标识 Oracle 驱动程序。

### 第 6 步：添加 `ojdbc.jar` 文件
- 在“添加驱动程序”对话框中切换到 **额外类路径** 选项卡。
- 点击 **添加** 按钮。
- 导航到系统中 `ojdbc.jar` 文件的位置，选择它并确认添加到驱动程序的类路径。

### 第 7 步：指定 Java 驱动程序类
- 在“类名称”字段中，输入 Java 驱动程序类： **oracle.jdbc.OracleDriver**。这告诉 Squirrel SQL Client 从 `ojdbc.jar` 文件中使用哪个类来处理 Oracle 数据库连接。

### 第 8 步：提供示例 URL
- 可选地，您可以为连接到 Oracle 数据库指定示例 URL 格式：
  - **通过 SID 连接**： `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **通过服务名称连接**： `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- 在设置连接时（在别名配置中），用实际值替换 `HOST`、`PORT` 和 `DB`。

### 第 9 步：保存驱动程序配置
- 点击 **确定** 以保存驱动程序设置并关闭“添加驱动程序”对话框。现在，“Oracle Thin Driver” 应该会出现在驱动程序选项卡中，带有绿色勾号，表示已正确配置。

### 第 10 步：为您的数据库创建别名
- 在 Squirrel SQL Client 的左侧切换到 **别名** 选项卡。
- 点击 **“+”** 按钮以打开“添加别名”对话框。

### 第 11 步：配置别名
- 在“添加别名”对话框中：
  - **名称**：输入此连接的名称（例如，“My Oracle DB”）。
  - **驱动程序**：从下拉菜单中选择 **Oracle Thin Driver**。
  - **URL**：输入特定 Oracle 数据库的连接 URL：
    - 通过 SID： `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - 通过服务名称： `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - 用数据库的详细信息替换 `HOST`（例如，localhost 或 IP 地址）、`PORT`（默认值为 1521）和 `DB`（SID 或服务名称）。
  - **用户名**：输入数据库用户名。
  - **密码**：输入数据库密码。

### 第 12 步：测试连接
- 在“添加别名”对话框中点击 **测试** 按钮，以验证 Squirrel SQL Client 是否可以使用提供的详细信息连接到您的 Oracle 数据库。如果成功，您将看到确认消息。

### 第 13 步：保存别名
- 如果测试连接成功，点击 **确定** 以保存别名。新别名现在将出现在别名选项卡中。

### 第 14 步：连接到数据库
- 在别名选项卡中，选择您新创建的别名（例如，“My Oracle DB”）。
- 点击 **连接** 按钮以建立与 Oracle 数据库的连接。连接后，您可以开始使用 Squirrel SQL Client 查询数据库。

### 关键信息摘要
- **所需文件**： `ojdbc.jar`
- **Java 驱动程序类**： `oracle.jdbc.OracleDriver`
- **URL 格式**：
  - SID： `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - 服务名称： `jdbc:oracle:thin:@//HOST[:PORT]/DB`

按照这些步骤，您将成功将 Oracle JDBC 驱动程序添加到 Squirrel SQL Client，并配置与 Oracle 数据库的连接。请确保所有详细信息（文件路径、URL、凭据）准确无误，以避免连接问题。