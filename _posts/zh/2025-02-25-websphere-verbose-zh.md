---
audio: true
lang: zh
layout: post
title: 冗长日志记录在WebSphere Liberty服务器
translated: true
---

关于 WebSphere Liberty Profile (WLP) 中 `server` 命令的详细日志选项的查询，让我们澄清 `server` 命令的作用以及如何控制详细程度。

WLP 中的 `server` 命令用于管理服务器实例，执行如 `start`、`stop`、`run` 或 `status` 等操作。例如：

- `server start <serverName>` 在后台启动服务器，输出重定向到日志文件（例如 `logs/console.log`）。
- `server run <serverName>` 在前台启动服务器，直接在终端显示输出。

您的问题提到 `server` 命令的“详细日志选项”，这可能意味着命令本身的更详细输出或其管理的服务器的更详细日志。经过探索，`server` 命令没有直接的标志（如 `--verbose` 或 `-v`）来增加其自身输出的详细程度。相反，详细程度涉及服务器的日志行为，可以在调用命令时影响。

### 启用详细日志
在 WLP 中，日志的详细程度通过服务器的日志配置控制，而不是通过 `server` 命令的直接标志。以下是如何启用详细日志：

#### 1. **在 `server.xml` 中配置日志**
启用详细日志的主要方法是调整服务器的 `server.xml` 文件中的 `<logging>` 元素，通常位于 `<WLP_HOME>/usr/servers/<serverName>/`。您可以设置详细的跟踪规范以增加日志详细程度。例如：

```xml
<logging traceSpecification="*=all" />
```

- `*=all` 启用所有跟踪点，使日志非常详细（适用于调试）。
- 对于更有针对性的详细程度，可以指定组件，例如 `*=info:com.example.*=debug`，将默认级别设置为 `info`，但 `com.example` 包为 `debug`。

其他有用的属性包括：
- `logLevel`：设置一般日志级别（例如 `INFO`、`DEBUG`、`TRACE`）。
- `consoleLogLevel`：控制写入 `console.log` 或终端的消息级别（例如 `DEBUG` 或 `TRACE`）。

示例，设置更细的控制台级别：
```xml
<logging consoleLogLevel="DEBUG" traceSpecification="*=audit" />
```

当您运行 `server start` 时，日志（包括详细输出）将写入 `logs/console.log`。使用 `server run` 时，这些详细输出将直接显示在终端中。

#### 2. **使用环境变量**
您还可以通过环境变量控制日志详细程度，这些变量可以覆盖或补充 `server.xml` 设置。例如，在运行 `server` 命令之前设置 `WLP_LOGGING_CONSOLE_LOGLEVEL` 变量：

```bash
export WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG
server start <serverName>
```

- 这将控制台日志级别设置为 `DEBUG`，确保更详细的输出。
- 有效级别包括 `INFO`、`DEBUG`、`FINE`、`FINER`、`FINEST` 等。

对于 `server run`，这将使终端输出更详细；对于 `server start`，这将影响 `console.log`。

#### 3. **JVM 特定的详细选项**
如果您对特定的详细输出（如垃圾回收日志）感兴趣，可以添加 JVM 选项（虽然这与 `server` 命令本身无关，而是服务器运行时相关）。将 `-verbose:gc` 添加到 `<WLP_HOME>/usr/servers/<serverName>/` 中的 `jvm.options` 文件，或者通过 `server.xml` 包含它：

```xml
<jvmEntries verbose="gc" />
```

这将生成与 GC 相关的日志，通常在 `console.log` 或使用 `server run` 时的终端中。

### 这与 `server` 命令的关系
- **没有直接的 `--verbose` 选项**：`server` 命令本身（例如 `server start`）没有 `--verbose` 或类似的标志来详细说明其执行步骤，超出基本状态消息（例如“服务器已启动”）。
- **服务器日志控制详细程度**：您看到的详细程度取决于服务器的日志配置。使用 `server run` 可以在终端中实时观察日志，或者在 `server start` 后检查日志文件。

例如：
- 使用 `<logging traceSpecification="*=all"/>` 在 `server.xml` 中，运行 `server run <serverName>` 将在终端中显示详细日志。
- 使用 `server start <serverName>`，相同的详细程度将出现在 `logs/console.log` 中。

### 建议
要在使用 `server` 命令时实现详细日志：
1. 编辑 `server.xml` 以包含详细的 `traceSpecification`（例如 `*=all` 以获得最大详细程度，或特定级别如 `*=debug`）。
2. 或者，在环境中设置 `WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG`。
3. 使用 `server run` 直接查看详细输出，或者使用 `server start` 并检查 `logs/console.log`。

这种方法确保您获得所需的详细日志，符合调试或监控需求。

如果您指的是更具体的内容（例如命令执行详细程度而不是服务器日志），请随时澄清！否则，按照上述方法配置服务器日志是在 WLP 中使用 `server` 命令启用详细日志的标准方法。