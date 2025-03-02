---
audio: false
generated: false
lang: zh
layout: post
title: 为什么Kafka快
translated: true
---

### 关键要点
- 视频“系统设计：Kafka 为什么快？”似乎通过其架构和设计选择解释了 Apache Kafka 的速度。
- 研究表明，Kafka 的性能得到了追加日志、零拷贝原则、批处理和高效分区的提升。
- 证据表明，Kafka 的速度归因于其分布式事件流平台设计，关键组件包括生产者、代理和消费者。

### 引言
本博客文章基于 ByteByteGo 的 YouTube 视频“系统设计：Kafka 为什么快？”的内容，旨在将其见解转化为书面格式，以便更容易阅读和参考。Apache Kafka 以其在实时数据处理中的高性能而闻名，本文探讨了其速度背后的原因，使其对新手友好。

### Kafka 的核心组件
Apache Kafka 作为一个分布式事件流平台，有三个主要组件：
- **生产者**：向 Kafka 主题发送数据的应用程序。
- **代理**：存储和管理数据的服务器，确保复制和分发。
- **消费者**：从主题读取和处理数据的应用程序。

这种结构使 Kafka 能够高效处理大量数据，从而提高其速度。

### 架构层和性能优化
Kafka 的架构分为两层：
- **计算层**：包括生产者、消费者和流处理的 API，促进交互。
- **存储层**：由代理组成，管理主题和分区中的数据存储，优化性能。

关键优化包括：
- **追加日志**：将数据顺序写入文件末尾，比随机写入更快。
- **零拷贝原则**：直接将数据从生产者传输到消费者，减少 CPU 开销。
- **批处理**：以批处理方式处理数据，降低每条记录的开销。
- **异步复制**：允许主代理在副本更新时处理请求，确保可用性而不影响性能。
- **分区**：将数据分布在多个分区中进行并行处理和高吞吐量。

这些设计选择，详细说明在 ByteByteGo 的支持博客文章中（[Kafka 为什么这么快？它是如何工作的？](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)），解释了 Kafka 在速度和可扩展性方面的卓越表现。

### 数据流和记录结构
当生产者将记录发送到代理时，它会被验证、追加到磁盘上的提交日志中，并进行复制以确保持久性，生产者在提交后会收到通知。这个过程优化了顺序 I/O，提高了性能。

每条记录包括：
- 时间戳：事件创建的时间。
- 键：用于分区和排序。
- 值：实际数据。
- 头部：可选的元数据。

这种结构，如博客文章所述，确保了高效的数据处理，并有助于 Kafka 的速度。

---

### 调查说明：Apache Kafka 性能的详细分析

本节提供了对 Apache Kafka 性能的全面探讨，扩展了 ByteByteGo 的视频“系统设计：Kafka 为什么快？”，并引用了其他资源，以确保全面理解。分析结构涵盖了 Kafka 的架构、组件和具体优化，并提供了详细的解释和示例以便清晰。

#### 背景和上下文
Apache Kafka 作为一个分布式事件流平台，以其高吞吐量、低延迟的数据流处理能力而闻名，成为现代数据架构的重要组成部分。2022 年 6 月 29 日发布的视频，作为系统设计播放列表的一部分，旨在阐明 Kafka 为什么快，这是一个重要的话题，特别是在数据流需求指数增长的背景下。本分析基于 ByteByteGo 的详细博客文章（[Kafka 为什么这么快？它是如何工作的？](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)），该文章补充了视频内容并提供了额外的见解。

#### Kafka 的核心组件和架构
Kafka 的速度始于其核心组件：
- **生产者**：这些是生成并将事件发送到 Kafka 主题的应用程序或系统。例如，Web 应用程序可能会生成用户交互事件。
- **代理**：这些是组成集群的服务器，负责存储数据、管理分区和处理复制。典型的设置可能包括多个代理以实现容错和可扩展性。
- **消费者**：订阅主题以读取和处理事件的应用程序，例如实时数据的分析引擎。

架构将 Kafka 定位为事件流平台，使用“事件”而不是“消息”，区别于传统的消息队列。这在其设计中体现出来，事件是不可变的，并按偏移量在分区中排序，如博客文章所述。

| 组件       | 角色                                                                 |
|------------|----------------------------------------------------------------------|
| 生产者     | 将事件发送到主题，启动数据流。                                        |
| 代理       | 存储和管理数据，处理复制，并为消费者提供服务。                         |
| 消费者     | 从主题读取和处理事件，使实时分析成为可能。                             |

博客文章包括一个图表，位于 [此 URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)，说明了集群模式下生产者、代理和消费者之间的交互。

#### 分层架构：计算和存储
Kafka 的架构分为：
- **计算层**：通过 API 促进通信：
  - **生产者 API**：用于应用程序发送事件。
  - **消费者 API**：用于读取事件。
  - **Kafka Connect API**：与外部系统（如数据库）集成。
  - **Kafka Streams API**：支持流处理，例如为主题（如“订单”）创建 KStream，使用 Serdes 进行序列化，并使用 ksqlDB 进行流处理作业，通过 REST API。提供的示例是订阅“订单”，按产品聚合，并将其发送到“按产品订单”进行分析。
- **存储层**：由集群中的 Kafka 代理组成，数据组织在主题和分区中。主题类似于数据库表，分区分布在节点上，确保可扩展性。分区中的事件按偏移量排序，不可变，追加日志，删除被视为事件，增强写性能。

博客文章详细说明了这一点，指出代理管理分区、读取、写入和复制，图表位于 [此 URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)，说明了复制，例如“订单”中的分区 0 具有三个副本：主代理在代理 1 上（偏移量 4），副本在代理 2 上（偏移量 2），代理 3 上（偏移量 3）。

| 层           | 描述                                                                 |
|--------------|-----------------------------------------------------------------------------|
| 计算层       | 交互 API：生产者、消费者、连接、流和 ksqlDB。                         |
| 存储层       | 集群中的代理，主题/分区分布，事件按偏移量排序。                         |

#### 控制和数据平面
- **控制平面**：管理集群元数据，历史上使用 Zookeeper，现在被 KRaft 模块替代，具有选定代理上的控制器。这种简化消除了 Zookeeper，使配置更容易，通过特殊主题使元数据传播更高效，如博客文章所述。
- **数据平面**：处理数据复制，副本发出 FetchRequest，主代理发送数据，并在某个偏移量之前提交记录，确保一致性。分区 0 具有偏移量 2、3 和 4 的示例，图表位于 [此 URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)。

#### 记录结构和代理操作
每条记录，事件的抽象，包括：
- 时间戳：创建时。
- 键：用于排序、共存和保留，对分区至关重要。
- 值：数据内容。
- 头部：可选的元数据。

键和值是字节数组，使用 serdes 进行编码/解码，确保灵活性。代理操作包括：
- 生产者请求到达套接字接收缓冲区。
- 网络线程将其移动到共享请求队列。
- I/O 线程验证 CRC，追加到提交日志（磁盘段，包含数据和索引）。
- 请求存储在 purgatory 中进行复制。
- 响应排队，网络线程通过套接字发送缓冲区。

这个过程，优化了顺序 I/O，如博客文章所述，图表说明了流程，显著提高了 Kafka 的速度。

| 记录组件 | 目的                                                                 |
|----------|-------------------------------------------------------------------------|
| 时间戳  | 记录事件创建的时间。                                                 |
| 键      | 确保排序、共存和保留以进行分区。                                     |
| 值      | 包含实际数据内容。                                                   |
| 头部    | 可选的元数据以提供额外信息。                                         |

#### 性能优化
几项设计决策增强了 Kafka 的速度：
- **追加日志**：将数据顺序写入文件末尾，最小化磁盘寻道时间，类似于在日记末尾添加条目，比在文档中间插入更快。
- **零拷贝原则**：直接将数据从生产者传输到消费者，减少 CPU 开销，类似于将箱子从卡车移动到仓库而不拆包，节省时间。
- **批处理**：以批处理方式处理数据，降低每条记录的开销，提高效率。
- **异步复制**：主代理在副本更新时处理请求，确保可用性而不影响性能。
- **分区**：将数据分布在分区中进行并行处理，增加吞吐量，这是处理大数据量的关键因素。

这些优化，如博客文章所述，是 Kafka 实现高吞吐量和低延迟的原因，使其适用于实时应用。

#### 结论和额外见解
Apache Kafka 的速度是其精心设计的架构和性能优化的结果，利用追加日志、零拷贝原则、批处理、异步复制和高效分区。本分析基于视频，并补充了博客文章，提供了全面的视图，意外地深入，超出了预期的简单概述，揭示了设计选择的微妙平衡，使 Kafka 成为数据流领域的领导者。

博客文章还提供了 7 天的免费试用，以访问完整档案，位于 [此订阅链接](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)，为有兴趣的读者提供了更多资源。

这种详细的探讨确保了全面的理解，与视频的教育意图一致，旨在教育 Kafka 的性能，并基于从各种来源收集的研究和见解，确保准确性和深度。

#### 关键引用
- [系统设计：Kafka 为什么快？YouTube 视频](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [Kafka 为什么这么快？它是如何工作的？ByteByteGo 博客文章](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Kafka 架构图 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Kafka 复制图 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Kafka 代理操作图 ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [ByteByteGo 订阅 Kafka 文章](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)