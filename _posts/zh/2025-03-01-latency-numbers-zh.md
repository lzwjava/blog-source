---
audio: false
generated: false
lang: zh
layout: post
title: 延迟数字
translated: true
---

### 关键要点
- 视频似乎讨论了程序员应该知道的标准延迟数字，根据其标题和相关在线内容。
- 研究表明这些数字包括操作时间，如L1缓存访问（0.5 ns）和网络往返（最多150 ms），具体取决于硬件。
- 证据表明这些数字是近似值，更新反映了技术进步，特别是SSD和网络。

### 引言
视频《程序员应该知道的延迟数字：系统设计速成课程#1》可能涵盖了计算机操作的基本延迟数字，对于系统设计至关重要。这些数字帮助程序员了解性能影响并优化系统。

### 延迟数字及其重要性
延迟是启动和完成操作之间的延迟，如访问内存或通过网络发送数据。视频可能列出了典型的延迟，例如：
- L1缓存引用为0.5纳秒（ns），是最快的内存访问。
- 同一数据中心内的往返时间为500微秒（us）或0.5毫秒（ms），影响分布式系统。

这些数字，虽然是近似值，但指导了系统设计中的决策，如选择内存和磁盘存储。

### 系统设计中的背景
了解这些延迟有助于优化代码、做出权衡并增强用户体验。例如，知道磁盘查找需要10 ms可以影响数据库设计，以最小化此类操作。

### 意外细节
一个有趣的方面是，这些数字，如SSD读取时间，随着技术的进步而改善，但核心CPU延迟，如L1缓存访问，保持稳定，显示了硬件演变的不均衡影响。

---

### 调查笔记：视频中延迟数字的详细分析

本笔记提供了对视频《程序员应该知道的延迟数字：系统设计速成课程#1》中可能讨论的延迟数字的全面探讨，基于可用的在线内容和相关资源。分析旨在为程序员和系统设计师综合信息，提供总结和详细见解，了解这些数字的重要性。

#### 背景和背景
该视频，可在[YouTube](https://www.youtube.com/watch?v=FqR5vESuKe0)上访问，是系统设计系列的一部分，专注于程序员关键的延迟数字。延迟，定义为操作启动和完成之间的时间延迟，是理解系统性能的关键。根据视频的标题和相关搜索，它似乎涵盖了由Google的Jeff Dean等人推广的标准延迟数字，这些数字在编程社区中常被引用。

在线搜索揭示了几个讨论这些数字的资源，包括一个名为《每个程序员都应该知道的延迟数字》的GitHub Gist ([GitHub Gist](https://gist.github.com/jboner/2841832)) 和2023年的Medium文章 ([Medium文章](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a))。这些来源，加上2013年的High Scalability帖子 ([High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/))，为编译视频的可能内容提供了基础。

#### 延迟数字汇编
根据收集到的信息，以下表总结了视频中可能讨论的标准延迟数字，并对每个操作进行了解释：

| 操作                                      | 延迟（ns） | 延迟（us） | 延迟（ms） | 解释                                                          |
|-------------------------------------------|------------|------------|------------|----------------------------------------------------------------------|
| L1缓存引用                                | 0.5        | -          | -          | 访问CPU附近的Level 1缓存中的数据，这是最快的内存。 |
| 分支误判                                  | 5          | -          | -          | CPU在条件分支上错误预测时的惩罚。                       |
| L2缓存引用                                | 7          | -          | -          | 访问Level 2缓存中的数据，比L1大但慢。                   |
| 互斥锁/解锁                                | 25         | -          | -          | 多线程程序中获取和释放互斥锁的时间。                   |
| 主内存引用                                  | 100        | -          | -          | 访问主随机存取存储器（RAM）中的数据。                   |
| 使用Zippy压缩1KB字节                       | 10,000     | 10         | -          | 使用Zippy算法压缩1千字节的时间。                       |
| 通过1Gbps网络发送1KB字节                   | 10,000     | 10         | -          | 通过每秒1千兆比特网络传输1千字节的时间。               |
| 从SSD随机读取4KB                          | 150,000    | 150        | -          | 从固态驱动器随机读取4千字节。                         |
| 从内存顺序读取1MB                          | 250,000    | 250        | -          | 从主内存顺序读取1兆字节。                         |
| 同一数据中心内的往返                      | 500,000    | 500        | 0.5        | 同一数据中心内的网络往返时间。                         |
| 从SSD顺序读取1MB                          | 1,000,000  | 1,000      | 1          | 从SSD顺序读取1兆字节。                         |
| HDD查找                                    | 10,000,000 | 10,000     | 10         | 硬盘驱动器寻找新位置的时间。                         |
| 从磁盘顺序读取1MB                          | 20,000,000 | 20,000     | 20         | 从HDD顺序读取1兆字节。                         |
| 发送数据包CA->荷兰->CA                    | 150,000,000| 150,000    | 150        | 加利福尼亚到荷兰的网络数据包往返时间。               |

这些数字主要来自2012年，部分更新反映了典型硬件性能，最近的讨论中注意到SSD和网络的变化，特别是由于技术进步。

#### 分析与影响
这些延迟数字并非固定，可能因特定硬件和配置而异。例如，2020年Ivan Pesin的博客文章 ([Pesin Space](http://pesin.space/posts/2020-09-22-latencies/))指出，由于更好的SSD（NVMe）和更快的网络（10/100Gb），磁盘和网络延迟有所改善，但核心CPU延迟，如L1缓存访问，保持稳定。这种不均衡的演变突显了系统设计中的上下文重要性。

在实践中，这些数字指导了几个方面：
- **性能优化**：最小化高延迟操作，如磁盘查找（10 ms），可以显著提高应用程序速度。例如，将频繁访问的数据缓存在内存（250 us读取1 MB）而不是磁盘中，可以减少等待时间。
- **权衡决策**：系统设计师经常面临选择，例如使用内存缓存还是数据库。知道主内存引用（100 ns）比L1缓存引用（0.5 ns）快200倍，可以帮助做出此类决策。
- **用户体验**：在Web应用程序中，网络延迟，如数据中心往返（500 us），会影响页面加载时间，从而影响用户满意度。2024年的Vercel博客文章 ([Vercel博客](https://vercel.com/blog/latency-numbers-every-web-developer-should-know))强调了这一点，指出网络瀑布可以累积延迟。

#### 历史背景和更新
这些原始数字由Jeff Dean提出并由Peter Norvig推广，大约在2010年，研究人员如Colin Scott ([Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html))进行了更新。2019年Dan Hon的Medium文章 ([Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d))添加了幽默但相关的延迟，如重新启动MacBook Pro（90秒），说明了更广泛的技术相关延迟。然而，核心延迟数字变化不大，GitHub Gist建议它们在2023年仍然“非常相似”，基于物理限制。

#### 结论和建议
对于程序员和系统设计师，记住这些延迟数字提供了性能调优的心理模型。它们应该被视为指南，具体硬件应进行实际基准测试。了解更新，特别是在新兴技术如量子计算或5G网络方面，将至关重要。GitHub Gist和Medium文章提供了进一步探索的起点。

本分析基于视频的可能内容，并补充了广泛的在线研究，强调了延迟数字在计算中的持久相关性，呼吁适应技术变化以实现最佳系统设计。

#### 关键引用
- [每个程序员都应该知道的延迟数字GitHub Gist](https://gist.github.com/jboner/2841832)
- [程序员应该知道的延迟数字YouTube视频](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [更新的延迟数字Medium文章](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [每个优秀程序员都必须知道的更多数字High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [每个Web开发人员都应该知道的延迟数字Vercel博客](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [每个工程师都应该知道的延迟数字Pesin Space博客](http://pesin.space/posts/2020-09-22-latencies/)
- [每个程序员都应该知道的更多延迟数字Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [每年程序员应该知道的数字互动延迟](https://colin-scott.github.io/personal_website/research/interactive_latency.html)