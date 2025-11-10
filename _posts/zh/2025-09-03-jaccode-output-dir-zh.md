---
audio: false
generated: true
image: false
lang: zh
layout: post
title: 配置JaCoCo代理输出目录
translated: true
type: note
---

是的——完全正确 👍。

默认情况下，如果你这样配置：

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=jacoco.exec,output=file
```

那么 `jacoco.exec` 文件会生成在 JVM 进程的**当前工作目录**下（通常是服务器根目录或启动 Liberty 的位置）。

如果想控制生成路径，可以指定**绝对路径或相对路径**，例如：

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=/opt/coverage-data/jacoco.exec,output=file
```

或者

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=target/jacoco.exec,output=file
```

（其中 `target/` 是相对于启动目录的路径）。

所以没错，若想确保 `.exec` 文件的生成位置，请使用完整路径。

👉 提示：在 Maven/Gradle 项目中，通常会将路径指向 `target/`（Maven）或 `build/`（Gradle）目录，这样后续报告插件就能自动读取该文件。

需要我展示一个配置了完整路径的 Liberty `jvm.options` 示例吗？