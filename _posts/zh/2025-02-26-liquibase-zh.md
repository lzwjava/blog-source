---
audio: false
generated: false
lang: zh
layout: post
title: 'Liquibase: 数据库模式管理'
translated: true
---

这是一个关于如何在Spring Boot应用程序中使用Liquibase来有效管理数据库模式变化的全面指南：

---

### 1. 添加Liquibase依赖
首先，你需要在项目中包含Liquibase依赖。如果你使用的是**Maven**，将以下内容添加到你的`pom.xml`中：

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

对于**Gradle**，将以下内容添加到你的`build.gradle`中：

```groovy
implementation 'org.liquibase:liquibase-core'
```

这将Liquibase核心库引入到你的项目中。

---

### 2. 配置Liquibase
Liquibase使用一个**变更日志文件**来管理数据库模式变化。默认情况下，Spring Boot会在类路径中查找名为`db/changelog/db.changelog-master.yaml`、`db/changelog/db.changelog-master.xml`或`db/changelog/db.changelog-master.sql`的文件。你可以通过在`application.properties`（或`application.yml`）中添加一个属性来自定义这个位置：

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

这告诉Spring Boot在哪里找到你的变更日志文件。

---

### 3. 创建一个变更日志文件
变更日志文件定义了你想要应用到数据库的变化。你可以用XML、YAML或SQL格式编写它。以下是一个位于`src/main/resources/db/changelog/db.changelog-master.xml`的**XML变更日志文件**的示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="your-name">
        <createTable tableName="users">
            <column name="id" type="int">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="varchar(255)"/>
            <column name="email" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

这个示例创建了一个包含三个列的`users`表：`id`、`username`和`email`。每个`<changeSet>`代表一组要应用的变化。

---

### 4. 运行你的Spring Boot应用程序
当你启动Spring Boot应用程序时，Liquibase会自动：
- 读取变更日志文件。
- 检查哪些变更集已经被应用（在一个名为`DATABASECHANGELOG`的表中跟踪）。
- 将任何新的变更集应用到你的数据库。

不需要额外的代码——Spring Boot的自动配置会处理这些。

---

### 5. 自定义Liquibase（可选）
你可以使用`application.properties`中的属性来调整Liquibase的行为。以下是一些常见的选项：

```properties
spring.liquibase.enabled=true          # 启用或禁用Liquibase
spring.liquibase.drop-first=false      # 在应用变化之前删除数据库（谨慎使用）
spring.liquibase.contexts=dev,prod     # 仅在特定上下文中运行变更集
```

这些设置允许你将Liquibase适应你的环境或工作流程。

---

### 6. 利用高级功能
Liquibase提供了强大的功能来增强模式管理：
- **上下文和标签**：控制哪些变更集在特定环境中运行（例如`dev`与`prod`）。
- **预条件**：在应用变更集之前确保某些条件（例如表存在）。
- **回滚**：定义如何在需要时撤销一个变更集。
- **重构**：使用内置支持进行复杂的数据库变化（例如重命名列）。

例如，为变更集添加一个上下文：

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

这个变更集仅在`dev`上下文中运行。

---

### 7. 使用内存数据库进行测试
对于测试，将Liquibase与内存数据库（如H2）配对使用。添加H2依赖：

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

然后为测试配置你的`application.properties`：

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibase会在测试期间将你的变化应用到内存数据库。

---

### 8. 版本控制你的变更日志
将你的变更日志文件存储在版本控制（例如Git）中，与你的应用程序代码一起。这确保你的数据库模式与代码库同步演变，使部署和回滚更加可预测。

---

### 总结
在Spring Boot应用程序中使用Liquibase：
1. 添加Liquibase依赖。
2. 配置变更日志文件位置。
3. 创建一个包含数据库变化的变更日志文件。
4. 运行你的应用程序——Liquibase会处理其余部分。

Liquibase是一个强大的工具，用于以结构化、版本控制的方式管理数据库模式变化，与Spring Boot无缝集成。