---
lang: hant
layout: post
title: 云计算与大数据入门
---

這節課包含以下話題：

* Spark
* Hadoop
* Kubernetes
* Docker
* Flink
* MongoDB

说起云计算，似乎离不开众多的工具，如Hadoop、Hive、Hbase、ZooKeeper、Docker、Kubernetes、Spark、Kafka、MongoDB、Flink、Druid、Presto、Kylin、Elastic Search。这些工具你都有所耳闻吗？其中一些是我从`大数据工程师`和`分布式后端工程师`的职位描述中发现的。这些都是高薪职位。我们不妨尝试将它们一一安装，稍作探索。
## 初探 Spark

官网介绍，`Spark` 是一个用于大规模数据分析的引擎。`Spark` 实际上是一套库，它不像 `Redis` 那样分为服务端和客户端。`Spark` 主要是在客户端使用的。从官网下载了最新版本，文件名为 `spark-3.1.1-bin-hadoop3.2.tar`。

```shell
$ tree . -L 1
.
├── LICENSE
├── NOTICE
├── R
├── README.md
├── RELEASE
├── bin
├── conf
├── data
├── examples
├── jars
├── kubernetes
├── licenses
├── python
├── sbin
└── yarn
```

11個目錄，4個文件
```

似乎就是各种语言编写的一些分析库。

同时，官网提到可以直接在Python上安装依赖库。使用命令 `pip install pyspark` 即可完成安装。

```shell
$ pip install pyspark
正在收集 pyspark
  下載 pyspark-3.1.1.tar.gz (212.3 MB)
     |████████████████████████████████| 212.3 MB 14 kB/s
正在收集 py4j==0.10.9
  下載 py4j-0.10.9-py2.py3-none-any.whl (198 kB)
     |████████████████████████████████| 198 kB 145 kB/s
正在為收集的套件構建輪子：pyspark
  正在為 pyspark 構建輪子 (setup.py) ... 完成
  已為 pyspark 創建輪子：檔案名=pyspark-3.1.1-py2.py3-none-any.whl 大小=212767604 sha256=0b8079e82f3a5bcadad99179902d8c8ff9f8eccad928a469c11b97abdc960b72
  儲存於目錄：/Users/lzw/Library/Caches/pip/wheels/23/bf/e9/9f3500437422e2ab82246f25a51ee480a44d4efc6c27e50d33
成功構建 pyspark
正在安裝收集的套件：py4j, pyspark
成功安裝 py4j-0.10.9 pyspark-3.1.1
```

装上了。

现在访问官网，查看一些示例。

```shell
./bin/run-example SparkPi 10
``` 

這行命令的意思是執行 Spark 提供的範例程式 `SparkPi`，並將參數 `10` 傳遞給它。這個範例程式通常用於計算圓周率 π 的近似值，而參數 `10` 可能代表計算的迭代次數或精度等級。執行此命令後，Spark 會運行該範例並輸出計算結果。

哦，原來可以運行剛剛下載的安裝包裡的程式。但出錯了。

```shell
$ ./bin/run-example SparkPi 10
21/03/11 00:06:15 WARN NativeCodeLoader: 無法為您的平台加載原生Hadoop庫...在適用的情況下使用內建的Java類
21/03/11 00:06:16 INFO ResourceUtils: 未為spark.driver配置自定義資源。
21/03/11 00:06:16 WARN Utils: 服務 'sparkDriver' 無法綁定到隨機空閒端口。您可能需要檢查是否配置了適當的綁定地址。
```

> Spark 是一个快速且通用的处理引擎，兼容 Hadoop 数据。它可以通过 YARN 或 Spark 的独立模式在 Hadoop 集群中运行，并且能够处理 HDFS、HBase、Cassandra、Hive 以及任何 Hadoop InputFormat 中的数据。Spark 设计用于执行批处理（类似于 MapReduce）以及新的工作负载，如流处理、交互式查询和机器学习。

出现了好几次`hadoop`。在谷歌搜索`spark depends hadoop`之后，找到了这样一段话。看来这依赖于`Hadoop`格式的数据。让我们先研究一下`Hadoop`。

## Hadoop

简单浏览了官网后，现在来安装一下。

```shell
brew install hadoop
```

在安装的过程中，让我们来了解一下。

> Apache Hadoop 软件库是一个框架，它允许使用简单的编程模型在计算机集群上分布式处理大型数据集。它旨在从单一服务器扩展到数千台机器，每台机器都提供本地计算和存储。该库本身并不依赖硬件来提供高可用性，而是设计用于在应用层检测和处理故障，从而在计算机集群之上提供高可用性服务，尽管集群中的每台计算机都可能出现故障。

简而言之，Hadoop 是一套用于处理分布式数据集的框架。这些数据集可能分布在众多计算机上，通过极其简洁的编程模型进行处理。Hadoop 的设计初衷是从单一服务器扩展至成千上万台机器。不同于依赖硬件的高可用性，该库旨在应用层面就能检测并处理错误。因此，即便集群中的每台计算机都可能出现故障，高可用服务依然能够部署于整个集群之中。

```shell
$ brew install hadoop
错误：
  homebrew-core 是一个浅克隆。
  homebrew-cask 是一个浅克隆。
要执行 `brew update`，首先运行：
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow
这些命令可能需要几分钟才能运行，因为仓库的大小较大。
由于 Homebrew/homebrew-core 和 Homebrew/homebrew-cask 的树形结构和流量，更新浅克隆是一项极其昂贵的操作，因此 GitHub 提出了这一限制。我们没有自动为您执行此操作，以避免在 CI 系统中重复执行昂贵的非浅克隆操作（这些系统应修复为不使用浅克隆）。对此带来的不便，我们深表歉意！
==> 正在下载 https://homebrew.bintray.com/bottles/openjdk-15.0.1.big_sur.bottle.tar.gz
已下载：/Users/lzw/Library/Caches/Homebrew/downloads/d1e3ece4af1d225bc2607eaa4ce85a873d2c6d43757ae4415d195751bc431962--openjdk-15.0.1.big_sur.bottle.tar.gz
==> 正在下载 https://www.apache.org/dyn/closer.lua?path=hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
已下载：/Users/lzw/Library/Caches/Homebrew/downloads/764c6a0ea7352bb8bb505989feee1b36dc628c2dcd6b93fef1ca829d191b4e1e--hadoop-3.3.0.tar.gz
==> 正在安装 hadoop 的依赖项：openjdk
==> 正在安装 hadoop 依赖项：openjdk
==> 正在解压 openjdk-15.0.1.big_sur.bottle.tar.gz
==> 注意事项
为了让系统 Java 包装器找到此 JDK，请使用以下命令创建符号链接：
  sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
```

openjdk 是 keg-only 的，这意味着它没有被符号链接到 /usr/local 中，
因为它会遮蔽 macOS 的 `java` 包装器。

如果您需要将 openjdk 放在 PATH 的首位，请运行：
  echo 'export PATH="/usr/local/opt/openjdk/bin:$PATH"' >> /Users/lzw/.bash_profile

为了让编译器找到 openjdk，您可能需要设置：
  export CPPFLAGS="-I/usr/local/opt/openjdk/include"

==> 摘要
🍺  /usr/local/Cellar/openjdk/15.0.1: 614 个文件，324.9MB
==> 正在安装 hadoop
🍺  /usr/local/Cellar/hadoop/3.3.0: 21,819 个文件，954.7MB，构建用时 2 分钟 15 秒
==> 升级 1 个依赖项：
maven 3.3.3 -> 3.6.3_1
==> 正在升级 maven 3.3.3 -> 3.6.3_1
==> 正在下载 https://www.apache.org/dyn/closer.lua?path=maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
==> 正在从 https://mirror.olnevhost.net/pub/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz 下载
######################################################################## 100.0%
错误：`brew link` 步骤未成功完成
该公式已构建，但未符号链接到 /usr/local
无法符号链接 bin/mvn
目标 /usr/local/bin/mvn
是属于 maven 的符号链接。您可以取消链接它：
  brew unlink maven

要强制链接并覆盖所有冲突的文件：
  brew link --overwrite maven

要列出所有将被删除的文件：
  brew link --overwrite --dry-run maven

可能产生冲突的文件有：
/usr/local/bin/mvn -> /usr/local/Cellar/maven/3.3.3/bin/mvn
/usr/local/bin/mvnDebug -> /usr/local/Cellar/maven/3.3.3/bin/mvnDebug
/usr/local/bin/mvnyjp -> /usr/local/Cellar/maven/3.3.3/bin/mvnyjp
==> 摘要
🍺  /usr/local/Cellar/maven/3.6.3_1: 87个文件，10.7MB，7秒内构建完成
正在移除：/usr/local/Cellar/maven/3.3.3...（92个文件，9MB）
==> 检查升级公式的依赖项...
==> 未发现损坏的依赖项！
==> 注意事项
==> openjdk
为了让系统Java包装器找到这个JDK，请使用以下命令创建符号链接：
  sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk 是 keg-only 的，这意味着它没有被符号链接到 /usr/local 中，
因为它会遮蔽 macOS 的 `java` 包装器。

如果您需要将 openjdk 置于 PATH 的首位，请运行：
  echo 'export PATH="/usr/local/opt/openjdk/bin:$PATH"' >> /Users/lzw/.bash_profile

为了让编译器找到openjdk，您可能需要设置：
  export CPPFLAGS="-I/usr/local/opt/openjdk/include"
```

注意到`brew`的輸出日誌中`maven`沒有很好地被連結。接下來，進行強制連結到`3.6.3_1`版本。

```shell
  brew link --overwrite maven
```

翻譯為：

```shell
  brew 強制連結並覆蓋 maven
```

`Hadoop` 已成功安裝。

> ## 模块
>
> 该项目包含以下模块：
>
> - **Hadoop Common**：支持其他Hadoop模块的通用工具集。
> - **Hadoop分布式文件系统（HDFS™）**：一种分布式文件系统，为应用程序数据提供高吞吐量的访问。
> - **Hadoop YARN**：一个用于作业调度和集群资源管理的框架。
> - **Hadoop MapReduce**：基于YARN的系统，用于大规模数据集的并行处理。
> - **Hadoop Ozone**：Hadoop的对象存储系统。

说有这些模块。这会敲入`hadoop`出现了：

```shell
$ hadoop
用法：hadoop [選項] 子命令 [子命令選項]
 或    hadoop [選項] 類名 [類名選項]
  其中，類名是用戶提供的Java類
```

OPTIONS 為空或包含以下任意選項：

--config dir                     Hadoop 配置目錄
--debug                          開啟 shell 腳本調試模式
--help                           使用信息
buildpaths                       嘗試從構建樹中添加類文件
hostnames list[,of,host,names]   在從屬模式下使用的主機名列表
hosts filename                   在從屬模式下使用的主機列表文件
loglevel level                   設置此命令的 log4j 日誌級別
workers                          開啟工作模式

 子命令是以下之一：
    管理命令：

daemonlog     获取/设置每个守护进程的日志级别

客户端命令：

archive       创建Hadoop归档文件
checknative   检查Hadoop原生库及压缩库的可用性
classpath     打印获取Hadoop jar及所需库的类路径
conftest      验证配置XML文件
credential    与凭证提供者交互
distch        分布式元数据更改器
distcp        递归复制文件或目录
dtutil        与委托令牌相关的操作
envvars       显示计算出的Hadoop环境变量
fs            运行通用文件系统用户客户端
gridmix       提交混合的合成作业，模拟生产负载的配置文件
jar <jar>     运行jar文件。注意：请使用"yarn jar"来启动YARN应用程序，而非此命令。
jnipath       打印java.library.path
kdiag         诊断Kerberos问题
kerbname      显示auth_to_local主体转换
key           通过KeyProvider管理密钥
rumenfolder   缩放rumen输入跟踪
rumentrace    将日志转换为rumen跟踪
s3guard       管理S3上的元数据
trace         查看和修改Hadoop跟踪设置
version       打印版本信息

守护进程命令：

kms           运行KMS，即密钥管理服务器
registrydns   运行注册表DNS服务器

子命令在调用时不带参数或使用`-h`时，可能会打印帮助信息。

官网上提供了一些示例。

```shell
  $ mkdir input
  $ cp etc/hadoop/*.xml input
  $ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar grep input output 'dfs[a-z.]+'
  $ cat output/*
```

注意到有`share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar`。這意味著可能有些樣例文件我們沒有得到。猜測用`Homebrew`安裝會沒有這些文件。我們從官網下載了安裝文件包。

```shell
$ tree . -L 1
.
├── LICENSE-binary
├── LICENSE.txt
├── NOTICE-binary
├── NOTICE.txt
├── README.txt
├── bin
├── etc
├── include
├── lib
├── libexec
├── licenses-binary
├── sbin
└── share
```

出現了`share`目錄。然而`Homebrew`真的沒有附加的這些文件嗎？找到`Homebrew`安裝的目錄。

```shell
$ type hadoop
hadoop 是 /usr/local/bin/hadoop
$ ls -alrt /usr/local/bin/hadoop
lrwxr-xr-x  1 lzw  admin  33 3月 11 00:48 /usr/local/bin/hadoop -> ../Cellar/hadoop/3.3.0/bin/hadoop
$ cd /usr/local/Cellar/hadoop/3.3.0
```

这是在`/usr/local/Cellar/hadoop/3.3.0/libexec/share/hadoop`下打印的目录树

```shell
$ tree . -L 2
.
├── client
│   ├── hadoop-client-api-3.3.0.jar
│   ├── hadoop-client-minicluster-3.3.0.jar
│   └── hadoop-client-runtime-3.3.0.jar
├── common
│   ├── hadoop-common-3.3.0-tests.jar
│   ├── hadoop-common-3.3.0.jar
│   ├── hadoop-kms-3.3.0.jar
│   ├── hadoop-nfs-3.3.0.jar
│   ├── hadoop-registry-3.3.0.jar
│   ├── jdiff
│   ├── lib
│   ├── sources
│   └── webapps
├── hdfs
│   ├── hadoop-hdfs-3.3.0-tests.jar
│   ├── hadoop-hdfs-3.3.0.jar
│   ├── hadoop-hdfs-client-3.3.0-tests.jar
│   ├── hadoop-hdfs-client-3.3.0.jar
│   ├── hadoop-hdfs-httpfs-3.3.0.jar
│   ├── hadoop-hdfs-native-client-3.3.0-tests.jar
│   ├── hadoop-hdfs-native-client-3.3.0.jar
│   ├── hadoop-hdfs-nfs-3.3.0.jar
│   ├── hadoop-hdfs-rbf-3.3.0-tests.jar
│   ├── hadoop-hdfs-rbf-3.3.0.jar
│   ├── jdiff
│   ├── lib
│   ├── sources
│   └── webapps
├── mapreduce
│   ├── hadoop-mapreduce-client-app-3.3.0.jar
│   ├── hadoop-mapreduce-client-common-3.3.0.jar
│   ├── hadoop-mapreduce-client-core-3.3.0.jar
│   ├── hadoop-mapreduce-client-hs-3.3.0.jar
│   ├── hadoop-mapreduce-client-hs-plugins-3.3.0.jar
│   ├── hadoop-mapreduce-client-jobclient-3.3.0-tests.jar
│   ├── hadoop-mapreduce-client-jobclient-3.3.0.jar
│   ├── hadoop-mapreduce-client-nativetask-3.3.0.jar
│   ├── hadoop-mapreduce-client-shuffle-3.3.0.jar
│   ├── hadoop-mapreduce-client-uploader-3.3.0.jar
│   ├── hadoop-mapreduce-examples-3.3.0.jar
│   ├── jdiff
│   ├── lib-examples
│   └── sources
├── tools
│   ├── dynamometer
│   ├── lib
│   ├── resourceestimator
│   ├── sls
│   └── sources
└── yarn
    ├── csi
    ├── hadoop-yarn-api-3.3.0.jar
    ├── hadoop-yarn-applications-catalog-webapp-3.3.0.war
    ├── hadoop-yarn-applications-distributedshell-3.3.0.jar
    ├── hadoop-yarn-applications-mawo-core-3.3.0.jar
    ├── hadoop-yarn-applications-unmanaged-am-launcher-3.3.0.jar
    ├── hadoop-yarn-client-3.3.0.jar
    ├── hadoop-yarn-common-3.3.0.jar
    ├── hadoop-yarn-registry-3.3.0.jar
    ├── hadoop-yarn-server-applicationhistoryservice-3.3.0.jar
    ├── hadoop-yarn-server-common-3.3.0.jar
    ├── hadoop-yarn-server-nodemanager-3.3.0.jar
    ├── hadoop-yarn-server-resourcemanager-3.3.0.jar
    ├── hadoop-yarn-server-router-3.3.0.jar
    ├── hadoop-yarn-server-sharedcachemanager-3.3.0.jar
    ├── hadoop-yarn-server-tests-3.3.0.jar
    ├── hadoop-yarn-server-timeline-pluginstorage-3.3.0.jar
    ├── hadoop-yarn-server-web-proxy-3.3.0.jar
    ├── hadoop-yarn-services-api-3.3.0.jar
    ├── hadoop-yarn-services-core-3.3.0.jar
    ├── lib
    ├── sources
    ├── test
    ├── timelineservice
    ├── webapps
    └── yarn-service-examples
```

可以看到有很多的`jar`包。

```shell
$ mkdir input
$ ls
bin			hadoop-config.sh	hdfs-config.sh		libexec			sbin			yarn-config.sh
etc			hadoop-functions.sh	input			mapred-config.sh	share
$ cp etc/hadoop/*.xml input
$ cd input/
$ ls
capacity-scheduler.xml	hadoop-policy.xml	hdfs-site.xml		kms-acls.xml		mapred-site.xml
core-site.xml		hdfs-rbf-site.xml	httpfs-site.xml		kms-site.xml		yarn-site.xml
$ cd ..
$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar grep input output 'dfs[a-z.]+'
JAR 文件不存在或不是普通文件: /usr/local/Cellar/hadoop/3.3.0/libexec/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar
$
$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.0.jar grep input output 'dfs[a-z.]+'
2021-03-11 01:54:30,791 WARN util.NativeCodeLoader: 无法为您的平台加载原生 hadoop 库... 在适用的情况下使用内置的 Java 类
2021-03-11 01:54:31,115 INFO impl.MetricsConfig: 从 hadoop-metrics2.properties 加载属性
2021-03-11 01:54:31,232 INFO impl.MetricsSystemImpl: 计划每 10 秒进行一次指标快照。
...
```

按照官网的例子操作。注意到`bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar grep input`，这里的`jar`包前带有版本号。因此需要将其替换为我们使用的`3.3.0`版本。

日志的结尾：

```shell
2021-03-11 01:54:35,374 INFO mapreduce.Job:  map 100% reduce 100%
2021-03-11 01:54:35,374 INFO mapreduce.Job: 作業 job_local2087514596_0002 成功完成
2021-03-11 01:54:35,377 INFO mapreduce.Job: 計數器: 30
	檔案系統計數器
		FILE: 讀取的字節數=1204316
		FILE: 寫入的字節數=3565480
		FILE: 讀取操作次數=0
		FILE: 大型讀取操作次數=0
		FILE: 寫入操作次數=0
	Map-Reduce 框架
		Map 輸入記錄=1
		Map 輸出記錄=1
		Map 輸出字節=17
		Map 輸出實體化字節=25
		輸入分割字節=141
		合併輸入記錄=0
		合併輸出記錄=0
		Reduce 輸入組=1
		Reduce 混洗字節=25
		Reduce 輸入記錄=1
		Reduce 輸出記錄=1
		溢出記錄=2
		混洗的 Map 數量=1
		失敗的混洗=0
		合併的 Map 輸出=1
		GC 時間耗時 (毫秒)=57
		總提交的堆使用量 (字節)=772800512
	混洗錯誤
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	檔案輸入格式計數器
		讀取的字節=123
	檔案輸出格式計數器
		寫入的字節=23
```

继续查看。

```shell
$ cat output/*
1	dfsadmin
```

翻譯成繁體中文為：

```shell
$ cat output/*
1	dfsadmin
```

（注：此處的內容是命令和其輸出結果，屬於代碼範疇，無需翻譯，保持原樣即可。）

这到底是什么意思呢？不要紧，总之我们把`Hadoop`成功启动了，并且运行了第一个单机版的计算示例。

## 星火

回到 Spark 上。来看一个例子。

```python
text_file = sc.textFile("hdfs://...")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://...")
```

这里出现了`hdfs`文件。查阅後，得知可以這樣創建`hdfs`文件：

```shell
hdfs dfs -mkdir /test
``` 

這行指令在Hadoop分布式文件系統（HDFS）中創建一個名為`/test`的目錄。翻譯成繁體中文為：

```shell
hdfs dfs -mkdir /測試
``` 

請注意，雖然路徑名稱可以翻譯，但在實際操作中，路徑名稱通常保持英文以避免兼容性問題。因此，即使翻譯成“/測試”，在實際使用時仍建議使用“/test”。

来看看`hdfs`命令。

```shell
$ hdfs
用法：hdfs [選項] 子命令 [子命令選項]
```

OPTIONS 為空或包含以下任意選項：

--buildpaths                       尝试从构建树中添加类文件
--config dir                       Hadoop 配置目录
--daemon (start|status|stop)       对守护进程进行操作
--debug                            开启 shell 脚本调试模式
--help                             使用信息
--hostnames list[,of,host,names]   在 worker 模式下使用的主机名列表
--hosts filename                   在 worker 模式下使用的主机列表文件
--loglevel level                   设置此命令的 log4j 日志级别
--workers                          开启 worker 模式

 子命令（SUBCOMMAND）是以下之一：
    管理员命令：

cacheadmin           配置HDFS缓存
crypto               配置HDFS加密区域
debug                运行调试管理员以执行HDFS调试命令
dfsadmin             运行DFS管理客户端
dfsrouteradmin       管理基于路由器的联邦
ec                   运行HDFS纠删编码命令行界面
fsck                 运行DFS文件系统检查工具
haadmin              运行DFS高可用性管理客户端
jmxget               从NameNode或DataNode获取JMX导出值
oev                  将离线编辑查看器应用于编辑文件
oiv                  将离线fsimage查看器应用于fsimage
oiv_legacy           将离线fsimage查看器应用于旧版fsimage
storagepolicies      列出/获取/设置/满足块存储策略

客户端命令：

classpath            打印获取Hadoop jar及所需库的类路径
dfs                  在文件系统上运行文件系统命令
envvars              显示计算出的Hadoop环境变量
fetchdt              从NameNode获取委托令牌
getconf              从配置中获取配置值
groups               获取用户所属的组
lsSnapshottableDir   列出当前用户拥有的所有可快照目录
snapshotDiff         比较目录的两个快照或比较当前目录内容与快照
version              打印版本信息

守护进程命令：

balancer             运行集群平衡工具
datanode             运行DFS数据节点
dfsrouter            运行DFS路由器
diskbalancer         在给定节点上的磁盘间均匀分布数据
httpfs               运行HttpFS服务器，即HDFS HTTP网关
journalnode          运行DFS日志节点
mover                运行工具以跨存储类型移动块副本
namenode             运行DFS名称节点
nfs3                 运行NFS版本3网关
portmap              运行端口映射服务
secondarynamenode    运行DFS辅助名称节点
sps                  运行外部存储策略满足器
zkfc                 运行ZK故障转移控制器守护进程

子命令在调用时若不带参数或使用 -h 参数，可能会显示帮助信息。

继续修改代码。

```python
from pyspark.sql import SparkSession
```

spark = SparkSession.builder.master("local[*]")\
           .config('spark.driver.bindAddress', '127.0.0.1')\
           .getOrCreate()
sc = spark.sparkContext

翻译为：

spark = SparkSession.builder.master("local[*]")\
           .config('spark.driver.bindAddress', '127.0.0.1')\
           .getOrCreate()
sc = spark.sparkContext

这段代码创建了一个Spark会话，并设置了驱动程序的绑定地址为本地回环地址（127.0.0.1），然后获取或创建了一个Spark上下文（sc）。在中文环境中，这段代码的功能和结构保持不变，因此翻译后的代码与原文相同。

```python
text_file = sc.textFile("a.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("b.txt")
```

注意到`.config('spark.driver.bindAddress', '127.0.0.1')`非常重要。否则，可能会遇到错误提示`Service 'sparkDriver' could not bind on a random free port. You may check whether configuring an appropriate binding address`。

然而，這時又出現了錯誤。

```shell
原因：org.apache.spark.api.python.PythonException: 回溯（最近一次调用最后）：
  文件 "/usr/local/lib/python3.9/site-packages/pyspark/python/lib/pyspark.zip/pyspark/worker.py"，第 473 行，在 main 函数中
    抛出异常(("工作节点中的 Python 版本 %s 与驱动程序中的版本不同 " +
异常：工作节点中的 Python 版本为 3.8，而驱动程序中的版本为 3.9，PySpark 无法在不同的次要版本下运行。请检查环境变量 PYSPARK_PYTHON 和 PYSPARK_DRIVER_PYTHON 是否正确设置。
```

表示運行了不同版本的`Python`。

修改 `.bash_profile` 文件通常是为了自定义你的 shell 环境，比如设置环境变量、别名、路径等。以下是一些常见的修改步骤：

### 1. 打开 `.bash_profile` 文件
你可以使用任何文本编辑器来打开 `.bash_profile` 文件。例如，使用 `nano` 编辑器：

```bash
nano ~/.bash_profile
```

### 2. 添加或修改内容
在 `.bash_profile` 文件中，你可以添加或修改以下内容：

#### 设置环境变量
```bash
export PATH="$HOME/bin:$PATH"
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk"
```

#### 设置别名
```bash
alias ll='ls -la'
alias gs='git status'
```

#### 设置提示符 (PS1)
```bash
export PS1="\u@\h:\w\$ "
```

#### 加载其他配置文件
```bash
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi
```

### 3. 保存并退出
在 `nano` 编辑器中，按 `Ctrl + X` 退出，然后按 `Y` 确认保存，最后按 `Enter` 确认文件名。

### 4. 使更改生效
为了使更改立即生效，你可以运行以下命令：

```bash
source ~/.bash_profile
```

或者你也可以重新启动终端。

### 5. 检查更改
你可以通过运行 `echo $PATH` 或 `alias` 等命令来检查你的更改是否生效。

### 注意事项
- 如果你使用的是 `zsh`，你可能需要修改 `.zshrc` 或 `.zprofile` 文件。
- 如果你不确定某个设置的作用，建议先备份 `.bash_profile` 文件。

```bash
cp ~/.bash_profile ~/.bash_profile.bak
```

这样，即使修改出错，你也可以恢复到之前的状态。

```shell
PYSPARK_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
PYSPARK_DRIVER_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
```

翻譯成繁體中文：

```shell
PYSPARK_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
PYSPARK_DRIVER_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
```

這段代碼是設置環境變量，指定 PySpark 使用的 Python 解釋器路徑。在繁體中文環境下，這段代碼保持不變，因為它主要是路徑和變量名稱，不需要翻譯。

然而还是报同样的错。了解一番后，可能是因为`spark`运行的时候，没有载入这个环境变量，没有使用终端默认的环境变量。

需要在代码中设置：

```python
import os
```

# 设置 Spark 环境
os.environ['PYSPARK_PYTHON'] = '/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3'
```

這會運行。

```shell
$ python sc.py
21/03/11 02:54:52 警告 NativeCodeLoader: 無法為您的平台加載原生Hadoop庫...在適用的地方使用內建的Java類
使用Spark的默認log4j配置文件：org/apache/spark/log4j-defaults.properties
將默認日誌級別設置為“WARN”。
要調整日誌級別，請使用sc.setLogLevel(newLevel)。對於SparkR，請使用setLogLevel(newLevel)。
PythonRDD[6] 位於 PythonRDD.scala:53 的 RDD
```

這時生成了`b.txt`。

```shell
├── b.txt
│   ├── _SUCCESS
│   ├── part-00000
│   └── part-00001
```

打開一下。

```shell
$ cat b.txt/part-00000
('college', 1)
('two', 1)
('things', 2)
('worked', 1)
('on,', 1)
('of', 8)
('school,', 2)
('writing', 2)
('programming.', 1)
("didn't", 4)
('then,', 1)
('probably', 1)
('are:', 1)
('short', 1)
('awful.', 1)
('They', 1)
('plot,', 1)
('just', 1)
('characters', 1)
('them', 2)
...
```

成功了！这场景是不是很熟悉？就像在`Hadoop`示例中一样。

```shell
$ cat output/*
1	dfs管理員
```

這些文件就叫做`HDFS`。可見這裡使用`Spark`來統計單詞。短短幾句，操作起來非常方便的樣子。

## Kubernetes

接下来我们来探讨一下`Kubernetes`，也被称为`k8s`，其中间的8个字母被简化为8。这是一套开源系统，用于自动化部署、扩展和管理容器化应用程序。

`kubectl` 命令行工具是用來執行一些操作 Kubernetes (k8s) 集群的命令。可以用它來部署應用程式、查看和管理集群資源，以及查看日誌。

同样可以使用Homebrew来安装。

```shell
brew install kubectl
``` 

翻譯成繁體中文為：

```shell
使用 brew 安裝 kubectl
``` 

這裡的 `brew` 是 macOS 上的一個套件管理工具，`kubectl` 是用來與 Kubernetes 叢集進行互動的命令列工具。

輸出日誌：

```shell
==> 正在下載 https://homebrew.bintray.com/bottles/kubernetes-cli-1.20.1.big_sur.bottle.tar.gz
==> 從 https://d29vzk4ow07wi7.cloudfront.net/0b4f08bd1d47cb913d7cd4571e3394c6747dfbad7ff114c5589c8396c1085ecf?response-content-disposition=a 下載
######################################################################## 100.0%
==> 正在解壓 kubernetes-cli-1.20.1.big_sur.bottle.tar.gz
==> 注意事項
Bash 自動補全功能已安裝至：
  /usr/local/etc/bash_completion.d
==> 總結
🍺  /usr/local/Cellar/kubernetes-cli/1.20.1: 246 個文件，共 46.1MB
```

裝好了。

```shell
$ kubectl version --client
客戶端版本：version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.1", GitCommit:"c4d752765b3bbac2237bf87cf0b1c2e307844666", GitTreeState:"clean", BuildDate:"2020-12-19T08:38:20Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"darwin/amd64"}
```

```shell
$ kubectl
kubectl 控制 Kubernetes 集群管理器。
```

欲了解更多信息，请访问：https://kubernetes.io/docs/reference/kubectl/overview/

基本命令（初学者）：
  create        从文件或标准输入创建资源。
  expose        将复制控制器、服务、部署或Pod暴露为新的Kubernetes服务。
  run           在集群上运行特定的镜像。
  set           设置对象上的特定功能。

基本命令（中级）：
  explain       查看资源的文档说明
  get           显示一个或多个资源
  edit          在服务器上编辑资源
  delete        通过文件名、标准输入、资源及名称，或资源及标签选择器删除资源

部署命令：
  rollout       管理资源的部署过程
  scale         为 Deployment、ReplicaSet 或 Replication Controller 设置新的规模
  autoscale     自动调整 Deployment、ReplicaSet 或 ReplicationController 的规模

集群管理命令：
  certificate   修改证书资源。
  cluster-info  显示集群信息。
  top           显示资源（CPU/内存/存储）使用情况。
  cordon        将节点标记为不可调度。
  uncordon      将节点标记为可调度。
  drain         排空节点以准备维护。
  taint         更新一个或多个节点的污点。

故障排查与调试命令：
  describe      显示特定资源或资源组的详细信息
  logs          打印 Pod 中容器的日志
  attach        连接到正在运行的容器
  exec          在容器内执行命令
  port-forward  将一个或多个本地端口转发到 Pod
  proxy         运行一个指向 Kubernetes API 服务器的代理
  cp            在容器之间复制文件和目录
  auth          检查授权信息
  debug         为工作负载和节点创建调试会话以进行故障排查

高级命令：
  diff          对比当前版本与即将应用的版本
  apply         通过文件名或标准输入将配置应用到资源
  patch         更新资源的字段
  replace       通过文件名或标准输入替换资源
  wait          实验性功能：等待一个或多个资源达到特定条件
  kustomize     从目录或远程URL构建kustomization目标

设置命令：
  label         更新资源的标签
  annotate      更新资源的注解
  completion    输出指定 shell（bash 或 zsh）的 shell 补全代码

其他命令：
  api-resources 打印服务器上支持的API资源
  api-versions  打印服务器上支持的API版本，格式为“组/版本”
  config        修改kubeconfig文件
  plugin        提供与插件交互的实用工具
  version       打印客户端和服务器的版本信息

用法：
  kubectl [标志] [选项]

使用 "kubectl <命令> --help" 获取有关特定命令的更多信息。
使用 "kubectl options" 查看全局命令行选项列表（适用于所有命令）。
```

來創建一個配置文件。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  minReadySeconds: 5
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

```
```

```shell
$ kubectl apply -f simple_deployment.yaml
連接到伺服器 localhost:8080 被拒絕 - 您是否指定了正確的主機或端口？
```

```shell
$ kubectl 集群信息
```

要进一步调试和诊断集群问题，请使用 'kubectl cluster-info dump'。
连接服务器 localhost:8080 被拒绝——您是否指定了正确的主机或端口？
```

當用官網的終端試著運行下。

```shell
$ start.sh
正在启动 Kubernetes...minikube 版本：v1.8.1
提交：cbda04cf6bbe65e987ae52bb393c10099ab62014
* minikube v1.8.1 运行于 Ubuntu 18.04
* 根据用户配置使用 none 驱动
* 在 localhost 上运行（CPU=2，内存=2460MB，磁盘=145651MB）...
* 操作系统版本为 Ubuntu 18.04.4 LTS
```

* 正在Docker 19.03.6上准备Kubernetes v1.17.3...
  - kubelet.resolv-conf=/run/systemd/resolve/resolv.conf
* 启动Kubernetes中...
* 启用附加组件：default-storageclass, storage-provisioner
* 配置本地主机环境...
* 完成！kubectl现已配置为使用"minikube"
* 'dashboard'附加组件已启用
Kubernetes已启动
```

继续回到我们的终端。

```shell
$ kubectl version --client
客戶端版本：version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.1", GitCommit:"c4d752765b3bbac2237bf87cf0b1c2e307844666", GitTreeState:"clean", BuildDate:"2020-12-19T08:38:20Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"darwin/amd64"}
$ kubectl version
客戶端版本：version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.1", GitCommit:"c4d752765b3bbac2237bf87cf0b1c2e307844666", GitTreeState:"clean", BuildDate:"2020-12-19T08:38:20Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"darwin/amd64"}
連接到伺服器 localhost:8080 被拒絕 - 您是否指定了正確的主機或端口？
```

有趣的是，加上 `--client` 选项并没有引发错误。

文档指出，需要先安装`Minikube`。

```shell
$ brew install minikube
==> 正在下載 https://homebrew.bintray.com/bottles/minikube-1.16.0.big_sur.bottle.tar.gz
==> 從 https://d29vzk4ow07wi7.cloudfront.net/1b6d7d1b97b11b6b07e4fa531c2dc21770da290da9b2816f360fd923e00c85fc?response-content-disposition=a 下載
######################################################################## 100.0%
==> 正在解壓 minikube-1.16.0.big_sur.bottle.tar.gz
==> 注意事項
Bash 自動補全功能已安裝至：
  /usr/local/etc/bash_completion.d
==> 總結
🍺  /usr/local/Cellar/minikube/1.16.0: 8 個文件，共 64.6MB
```

```shell
$ minikube start
😄  minikube v1.16.0 在 Darwin 11.2.2 上运行
🎉  minikube 1.18.1 已发布！下载地址：https://github.com/kubernetes/minikube/releases/tag/v1.18.1
💡  要禁用此通知，请运行：'minikube config set WantUpdateNotification false'
```

✨ 自動選擇了 virtualbox 驅動程序
💿 正在下載虛擬機啟動鏡像...
    > minikube-v1.16.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
    > minikube-v1.16.0.iso: 212.62 MiB / 212.62 MiB [] 100.00% 5.32 MiB p/s 40s
👍 正在集群 minikube 中啟動控制平面節點 minikube
💾 正在下載 Kubernetes v1.20.0 預加載...
    > preloaded-images-k8s-v8-v1....: 491.00 MiB / 491.00 MiB  100.00% 7.52 MiB
🔥 正在創建 virtualbox 虛擬機（CPU=2，內存=4000MB，磁盤=20000MB）...
❗ 此虛擬機在訪問 https://k8s.gcr.io 時遇到問題
💡 要拉取新的外部鏡像，您可能需要配置代理：https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
🐳 正在 Docker 20.10.0 上準備 Kubernetes v1.20.0 ...
    ▪ 生成證書和密鑰...
    ▪ 啟動控制平面...
    ▪ 配置 RBAC 規則...
🔎 正在驗證 Kubernetes 組件...
🌟 已啟用插件：storage-provisioner, default-storageclass
🏄 完成！kubectl 現在已配置為默認使用 "minikube" 集群和 "default" 命名空間
```

接著來訪問這個集群。

```shell
$ kubectl get po -A
命名空間      名稱                                就緒   狀態     重啟次數  年齡
kube-system   coredns-74ff55c5b-ndbcr            1/1    運行中    0          60秒
kube-system   etcd-minikube                      0/1    運行中    0          74秒
kube-system   kube-apiserver-minikube            1/1    運行中    0          74秒
kube-system   kube-controller-manager-minikube   1/1    運行中    0          74秒
kube-system   kube-proxy-g2296                   1/1    運行中    0          60秒
kube-system   kube-scheduler-minikube            0/1    運行中    0          74秒
kube-system   storage-provisioner                1/1    運行中    1          74秒
```

來打開`minikube`的控制面板。

```shell
$ minikube dashboard
🔌  正在啟用儀表板 ...
🤔  正在驗證儀表板健康狀態 ...
🚀  正在啟動代理 ...
🤔  正在驗證代理健康狀態 ...
🎉  正在您的預設瀏覽器中開啟 http://127.0.0.1:50030/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ ...
```

![k8s](assets/images/distributed/k8s.png)

如何關掉呢。

```shell
$ minikube
minikube 提供並管理專為開發工作流程優化的本地 Kubernetes 集群。
```

基本命令：
  start          启动本地 Kubernetes 集群
  status         获取本地 Kubernetes 集群的状态
  stop           停止正在运行的本地 Kubernetes 集群
  delete         删除本地 Kubernetes 集群
  dashboard      访问在 minikube 集群内运行的 Kubernetes 仪表板
  pause          暂停 Kubernetes
  unpause        恢复已暂停的 Kubernetes

镜像命令：
  docker-env     配置环境以使用 minikube 的 Docker 守护进程
  podman-env     配置环境以使用 minikube 的 Podman 服务
  cache          添加、删除或将本地镜像推送到 minikube

配置与管理命令：
  addons         启用或禁用 minikube 的附加组件
  config         修改持久化的配置值
  profile        获取或列出当前配置（集群）
  update-context 在 IP 或端口变更时更新 kubeconfig

网络与连接命令：
  service        返回用于连接服务的URL
  tunnel         连接到LoadBalancer服务

高级命令：
  mount          将指定目录挂载到minikube中
  ssh            登录到minikube环境（用于调试）
  kubectl        运行与集群版本匹配的kubectl二进制文件
  node           添加、删除或列出额外节点

故障排除命令：
  ssh-key        获取指定节点的SSH身份密钥路径
  ssh-host       获取指定节点的SSH主机密钥
  ip             获取指定节点的IP地址
  logs           返回用于调试本地Kubernetes集群的日志
  update-check   打印当前及最新版本号
  version        打印minikube的版本信息

其他命令：
  completion     为 shell 生成命令补全脚本

使用 "minikube <命令> --help" 获取有关特定命令的更多信息。
```

可见是`minikube stop`。

回到`kubernetes`，現在工作正常了。

```shell
$ kubectl cluster-info
Kubernetes 控制平面正在 https://192.168.99.100:8443 上運行
KubeDNS 正在 https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy 上運行
```

要进一步调试和诊断集群问题，请使用 `kubectl cluster-info dump`。
```

当我们打开`https://192.168.99.100:8443`时，浏览器显示：

```json
{
  "kind": "狀態",
  "apiVersion": "v1",
  "metadata": {
    
  },
  "status": "失敗",
  "message": "禁止：用戶 \"system:anonymous\" 無法訪問路徑 \"/\"",
  "reason": "禁止",
  "details": {
    
  },
  "code": 403
}
```

访问`https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy`：

```json
{
  "kind": "狀態",
  "apiVersion": "v1",
  "metadata": {
    
  },
  "status": "失敗",
  "message": "服務 \"kube-dns:dns\" 被禁止：用戶 \"system:anonymous\" 無法在命名空間 \"kube-system\" 中獲取 API 群組 \"\" 中的資源 \"services/proxy\"",
  "reason": "禁止",
  "details": {
    "name": "kube-dns:dns",
    "kind": "服務"
  },
  "code": 403
}
```

来试试刚才那个配置。

```shell
$ kubectl apply -f simple_deployment.yaml
deployment.apps/nginx-deployment 已創建
```

有点问题。不过到这里，我们已经成功启动了`Kubernetes`。先告一段落，后续再继续探索。

```shell
$ minikube stop
✋  正在停止節點 "minikube"  ...
🛑  1 個節點已停止。
```

檢查是否結束。

```shell
w$ minikube dashboard
🤷  控制平面節點必須運行才能執行此命令
👉  要啟動集群，請運行："minikube start"
```

## Docker

`Docker` 也是一种容器平台，旨在帮助加速创建、分享和运行现代应用程序。您可以从官网下载应用程序。

![docker](assets/images/distributed/docker.png)

使用客户端有点卡顿。让我们改用命令行吧。

```docker
$ docker
```

用法：docker [选项] 命令

自给自足的容器运行时

选项：
      --config string      客户端配置文件的位置（默认为 "/Users/lzw/.docker"）
  -c, --context string     用于连接到守护进程的上下文名称（覆盖 DOCKER_HOST 环境变量和使用 "docker context use" 设置的默认上下文）
  -D, --debug              启用调试模式
  -H, --host list          要连接的守护进程套接字列表
  -l, --log-level string   设置日志级别（"debug"|"info"|"warn"|"error"|"fatal"）（默认为 "info"）
      --tls                使用 TLS；--tlsverify 隐含此选项
      --tlscacert string   仅信任由此 CA 签名的证书（默认为 "/Users/lzw/.docker/ca.pem"）
      --tlscert string     TLS 证书文件的路径（默认为 "/Users/lzw/.docker/cert.pem"）
      --tlskey string      TLS 密钥文件的路径（默认为 "/Users/lzw/.docker/key.pem"）
      --tlsverify          使用 TLS 并验证远程
  -v, --version            打印版本信息并退出

管理命令：
  app*        Docker 应用程序（Docker Inc.，版本 v0.9.1-beta3）
  builder     管理构建
  buildx*     使用 BuildKit 构建（Docker Inc.，版本 v0.5.1-docker）
  config      管理 Docker 配置
  container   管理容器
  context     管理上下文
  image       管理镜像
  manifest    管理 Docker 镜像清单和清单列表
  network     管理网络
  node        管理 Swarm 节点
  plugin      管理插件
  scan*       Docker 扫描（Docker Inc.，版本 v0.5.0）
  secret      管理 Docker 密钥
  service     管理服务
  stack       管理 Docker 堆栈
  swarm       管理 Swarm
  system      管理 Docker
  trust       管理 Docker 镜像的信任
  volume      管理卷

命令：
  attach      將本地標準輸入、輸出和錯誤流附加到正在運行的容器
  build       從Dockerfile構建鏡像
  commit      根據容器的更改創建新鏡像
  cp          在容器和本地文件系統之間複製文件/文件夾
  create      創建新容器
  diff        檢查容器文件系統上文件或目錄的更改
  events      從服務器獲取實時事件
  exec        在運行中的容器內執行命令
  export      將容器的文件系統導出為tar存檔
  history     顯示鏡像的歷史記錄
  images      列出鏡像
  import      從tarball導入內容以創建文件系統鏡像
  info        顯示系統範圍的信息
  inspect     返回Docker對象的低級信息
  kill        終止一個或多個運行中的容器
  load        從tar存檔或STDIN加載鏡像
  login       登錄到Docker註冊表
  logout      從Docker註冊表登出
  logs        獲取容器的日誌
  pause       暫停一個或多個容器內的所有進程
  port        列出端口映射或容器的特定映射
  ps          列出容器
  pull        從註冊表拉取鏡像或倉庫
  push        推送鏡像或倉庫到註冊表
  rename      重命名容器
  restart     重啟一個或多個容器
  rm          移除一個或多個容器
  rmi         移除一個或多個鏡像
  run         在新容器中運行命令
  save        將一個或多個鏡像保存到tar存檔（默認流式傳輸到STDOUT）
  search      在Docker Hub中搜索鏡像
  start       啟動一個或多個已停止的容器
  stats       顯示容器資源使用統計的實時流
  stop        停止一個或多個運行中的容器
  tag         創建引用SOURCE_IMAGE的TARGET_IMAGE標籤
  top         顯示容器的運行進程
  unpause     恢復一個或多個容器內的所有進程
  update      更新一個或多個容器的配置
  version     顯示Docker版本信息
  wait        阻塞直到一個或多個容器停止，然後打印它們的退出代碼

运行 'docker 命令 --help' 可获取有关某个命令的更多信息。

要获取更多关于 Docker 的帮助，请查看我们的指南：https://docs.docker.com/go/guides/
```

按照教程来试试看。

```shell
$ docker run -d -p 80:80 docker/getting-started
無法在本地找到 'docker/getting-started:latest' 的映像
latest: 正在從 docker/getting-started 拉取
aad63a933944: 拉取完成
b14da7a62044: 拉取完成
343784d40d66: 拉取完成
6f617e610986: 拉取完成
摘要: sha256:d2c4fb0641519ea208f20ab03dc40ec2a5a53fdfbccca90bef14f870158ed577
狀態: 已下載較新的映像 docker/getting-started:latest
815f13fc8f99f6185257980f74c349e182842ca572fe60ff62cbb15641199eaf
docker: 來自守護程序的錯誤響應: 端口不可用: 監聽 tcp 0.0.0.0:80: 綁定: 地址已在使用中。
```

更改端口。

```shell
$ docker run -d -p 8080:80 docker/getting-started
45bb95fa1ae80adc05cc498a1f4f339c45c51f7a8ae1be17f5b704853a5513a5
```

![docker_run](assets/images/distributed/docker_run.png)

打開瀏覽器，說明我們已經成功啟動了`docker`。

![浏览器](assets/images/distributed/browser.png)

停止容器。使用剛剛返回的`ID`。

```shell
$ docker stop 45bb95fa1ae80adc05cc498a1f4f339c45c51f7a8ae1be17f5b704853a5513a5
45bb95fa1ae80adc05cc498a1f4f339c45c51f7a8ae1be17f5b704853a5513a5
```

这时已经无法打开网址了。

这说明`docker`类似于虚拟机。

## Flink

打开官網。

![flink-home-graphic](assets/images/distributed/flink-home-graphic.png)

`Flink` 是一种用于数据流的 `Stateful` 计算框架。`Stateful` 指的是什么？暂时还不明白。不过，上面这个图看起来很有趣。来试试看吧。

说是需要Java环境。

```shell
$ java -version
java 版本 "1.8.0_151"
Java(TM) SE 運行環境 (build 1.8.0_151-b12)
Java HotSpot(TM) 64 位元伺服器虛擬機 (build 25.151-b12, 混合模式)
```

从官网下载最新版本的 `flink-1.12.2-bin-scala_2.11.tar`。

```shell
$ ./bin/start-cluster.sh
正在啟動集群。
在主機 lzwjava 上啟動 standalonesession 守護程序。
在主機 lzwjava 上啟動 taskexecutor 守護程序。
```

```shell
$ ./bin/flink run examples/streaming/WordCount.jar
正在使用默認輸入數據集執行 WordCount 示例。
使用 --input 來指定文件輸入。
將結果打印到標準輸出。使用 --output 來指定輸出路徑。
作業已提交，作業ID為 60f37647c20c2a6654359bd34edab807
程序執行完畢
作業ID為 60f37647c20c2a6654359bd34edab807 的作業已完成。
作業運行時間：757 毫秒
```

```shell
$ tail log/flink-*-taskexecutor-*.out
(仙女,1)
(在,3)
(你的,1)
(祈祷,1)
(是,4)
(所有,2)
(我的,1)
(罪过,1)
(记住,1)
(d,4)
```

```shell
$ ./bin/stop-cluster.sh
正在停止 taskexecutor 守护进程（进程ID：41812）在主机 lzwjava 上。
```

嗯，上手成功。可见這跟`Spark`很像。

## 麒麟

前往開啟官網。

> Apache Kylin™ 是一个开源的分布式分析数据仓库，专为大数据时代提供在线分析处理（OLAP）能力而设计。通过在Hadoop和Spark上革新多维立方体及预计算技术，Kylin能够实现几乎恒定的查询速度，不受数据量持续增长的影响。它将查询延迟从分钟级降至亚秒级，让在线分析重回大数据领域。

> Apache Kylin™ 让您通过三个步骤实现亚秒级延迟查询数十亿行数据。
>
> 1. 在Hadoop上识别星型或雪花型架构。
> 2. 根据识别出的表构建Cube。
> 3. 使用ANSI-SQL进行查询，并通过ODBC、JDBC或RESTful API在亚秒级内获取结果。

![麒麟架构图](assets/images/distributed/kylin_diagram.png)

大致上，它是处理大数据的一个层级。通过它，查询速度可以非常快。它充当了桥梁的角色。

可惜当前只能在`Linux`环境下使用。回头再来折腾。

## MongoDB

這也是一種數據庫。試試安裝。

```shell
$ brew tap mongodb/brew
==> 正在添加 mongodb/brew 源
正在克隆到 '/usr/local/Homebrew/Library/Taps/mongodb/homebrew-brew'...
remote: 枚举对象: 63, 完成。
remote: 计数对象: 100% (63/63), 完成。
remote: 压缩对象: 100% (62/62), 完成。
remote: 总计 566 (差异 21), 复用 6 (差异 1), 包复用 503
接收对象: 100% (566/566), 121.78 KiB | 335.00 KiB/s, 完成。
处理差异: 100% (259/259), 完成。
已添加 11 个公式 (39 个文件, 196.2KB)。
```

```shell
$ brew install mongodb-community@4.4
==> 正在从 mongodb/brew 安装 mongodb-community
==> 下载 https://fastdl.mongodb.org/tools/db/mongodb-database-tools-macos-x86_64-100.3.0.zip
######################################################################## 100.0%
==> 下载 https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.4.3.tgz
######################################################################## 100.0%
==> 正在安装 mongodb/brew/mongodb-community 的依赖项：mongodb-database-tools
==> 正在安装 mongodb/brew/mongodb-community 的依赖项：mongodb-database-tools
错误：`brew link` 步骤未成功完成
该公式已构建，但未符号链接到 /usr/local
无法符号链接 bin/bsondump
目标 /usr/local/bin/bsondump
是一个属于 mongodb 的符号链接。您可以取消链接：
  brew unlink mongodb
```

要强制链接并覆盖所有冲突的文件：
  brew link --overwrite mongodb-database-tools

要列出所有将被删除的文件：
  brew link --overwrite --dry-run mongodb-database-tools

可能产生冲突的文件有：
/usr/local/bin/bsondump -> /usr/local/Cellar/mongodb/3.0.7/bin/bsondump
/usr/local/bin/mongodump -> /usr/local/Cellar/mongodb/3.0.7/bin/mongodump
/usr/local/bin/mongoexport -> /usr/local/Cellar/mongodb/3.0.7/bin/mongoexport
/usr/local/bin/mongofiles -> /usr/local/Cellar/mongodb/3.0.7/bin/mongofiles
/usr/local/bin/mongoimport -> /usr/local/Cellar/mongodb/3.0.7/bin/mongoimport
/usr/local/bin/mongorestore -> /usr/local/Cellar/mongodb/3.0.7/bin/mongorestore
/usr/local/bin/mongostat -> /usr/local/Cellar/mongodb/3.0.7/bin/mongostat
/usr/local/bin/mongotop -> /usr/local/Cellar/mongodb/3.0.7/bin/mongotop
==> 摘要
🍺  /usr/local/Cellar/mongodb-database-tools/100.3.0: 13个文件，154MB，11秒内构建完成
==> 正在安装 mongodb/brew/mongodb-community
错误：`brew link` 步骤未成功完成
该公式已构建，但未符号链接到 /usr/local
无法符号链接 bin/mongo
目标 /usr/local/bin/mongo
是属于 mongodb 的符号链接。您可以取消链接：
  brew unlink mongodb

要强制链接并覆盖所有冲突的文件：
  brew link --overwrite mongodb-community

要列出所有将被删除的文件：
  brew link --overwrite --dry-run mongodb-community

可能產生衝突的文件有：
/usr/local/bin/mongo -> /usr/local/Cellar/mongodb/3.0.7/bin/mongo
/usr/local/bin/mongod -> /usr/local/Cellar/mongodb/3.0.7/bin/mongod
/usr/local/bin/mongos -> /usr/local/Cellar/mongodb/3.0.7/bin/mongos
==> 注意事項
要讓 launchd 現在啟動 mongodb/brew/mongodb-community 並在登錄時重啟：
  brew services start mongodb/brew/mongodb-community
或者，如果您不需要/想要後台服務，可以直接運行：
  mongod --config /usr/local/etc/mongod.conf
==> 總結
🍺  /usr/local/Cellar/mongodb-community/4.4.3: 11 個文件，156.8MB，10 秒內構建完成
==> 注意事項
==> mongodb-community
要讓 launchd 現在啟動 mongodb/brew/mongodb-community 並在登錄時重啟：
  brew services start mongodb/brew/mongodb-community
或者，如果您不需要/想要後台服務，可以直接運行：
  mongod --config /usr/local/etc/mongod.conf
```

之前我安装了一个旧版本。解除一下链接。

```shell
$ brew unlink mongodb
取消链接 /usr/local/Cellar/mongodb/3.0.7... 已移除 11 个符号链接
```

```shell
$ mongod --version
db 版本 v4.4.3
構建信息: {
    "版本": "4.4.3",
    "git版本": "913d6b62acfbb344dde1b116f4161360acd8fd13",
    "模塊": [],
    "分配器": "系統",
    "環境": {
        "分發架構": "x86_64",
        "目標架構": "x86_64"
    }
}
```

接着运行`mongod`启动MongoDB数据库服务器。然而，第一次启动时提示`/data/db`目录不存在。于是，我们创建了一个目录`~/mongodb`，用于存放数据库文件。

```shell
$ mongod --dbpath ~/mongodb
```

翻譯成繁體中文：

```shell
$ mongod --dbpath ~/mongodb
```

這段命令的意思是啟動 MongoDB 數據庫服務，並指定數據庫存儲路徑為用戶目錄下的 `mongodb` 文件夾。

输出为：

```json
{"t":{"$date":"2021-03-11T18:17:32.838+08:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"自動禁用 TLS 1.0，若要強制啟用 TLS 1.0，請指定 --sslDisabledProtocols 'none'"}
{"t":{"$date":"2021-03-11T18:17:32.842+08:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"在 NetworkInterface 啟動期間未配置 TransportLayer"}
{"t":{"$date":"2021-03-11T18:17:32.842+08:00"},"s":"I",  "c":"NETWORK",  "id":4648602, "ctx":"main","msg":"隱式使用 TCP FastOpen。"}
{"t":{"$date":"2021-03-11T18:17:32.842+08:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB 正在啟動","attr":{"pid":46256,"port":27017,"dbPath":"/Users/lzw/mongodb","architecture":"64-bit","host":"lzwjava"}}
{"t":{"$date":"2021-03-11T18:17:32.842+08:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"構建信息","attr":{"buildInfo":{"version":"4.4.3","gitVersion":"913d6b62acfbb344dde1b116f4161360acd8fd13","modules":[],"allocator":"system","environment":{"distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2021-03-11T18:17:32.843+08:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"操作系統","attr":{"os":{"name":"Mac OS X","version":"20.3.0"}}}
...
```

可见都是`JSON`格式。MongoDB就是将所有数据文件都用`JSON`格式来保存的。接着，打开另一个终端标签。

```shell
$ mongo
MongoDB shell 版本 v4.4.3
正在连接到：mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
隐式会话：会话 { "id" : UUID("4f55c561-70d3-4289-938d-4b90a284891f") }
MongoDB 服务器版本：4.4.3
---
服务器启动时生成了以下警告：
        2021-03-11T18:17:33.743+08:00: 数据库未启用访问控制。数据和配置的读写访问不受限制
        2021-03-11T18:17:33.743+08:00: 此服务器绑定到 localhost。远程系统将无法连接到此服务器。启动服务器时使用 --bind_ip <地址> 指定应响应请求的 IP 地址，或使用 --bind_ip_all 绑定到所有接口。如果这是预期的行为，请使用 --bind_ip 127.0.0.1 启动服务器以禁用此警告
        2021-03-11T18:17:33.743+08:00: 软资源限制过低
        2021-03-11T18:17:33.743+08:00:        当前值：4864
        2021-03-11T18:17:33.743+08:00:        推荐最小值：64000
---
---
        启用 MongoDB 的免费基于云的监控服务，该服务将接收并显示有关您的部署的指标（磁盘利用率、CPU、操作统计信息等）。
```

监控数据将发布在一个MongoDB网站上，该网站拥有一个独特的URL，您及您分享该URL的任何人皆可访问。MongoDB可能会利用这些信息来改进产品，并向您推荐MongoDB的产品及部署方案。

要啟用免費監控，請運行以下命令：db.enableFreeMonitoring()
若要永久停用此提醒，請運行以下命令：db.disableFreeMonitoring()
```

接着可以尝试插入数据、查询数据。

```shell
> db.inventory.insertOne(
...    { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
... )
{
	"acknowledged" : true,
	"insertedId" : ObjectId("6049ef91b653541cf355facb")
}
>
> db.inventory.find()
{ "_id" : ObjectId("6049ef91b653541cf355facb"), "item" : "canvas", "qty" : 100, "tags" : [ "cotton" ], "size" : { "h" : 28, "w" : 35.5, "uom" : "cm" } }
```

翻譯如下：

```shell
> db.inventory.insertOne(
...    { 物品: "畫布", 數量: 100, 標籤: ["棉"], 尺寸: { 高: 28, 寬: 35.5, 單位: "公分" } }
... )
{
	"已確認" : true,
	"插入的ID" : ObjectId("6049ef91b653541cf355facb")
}
>
> db.inventory.find()
{ "_id" : ObjectId("6049ef91b653541cf355facb"), "物品" : "畫布", "數量" : 100, "標籤" : [ "棉" ], "尺寸" : { "高" : 28, "寬" : 35.5, "單位" : "公分" } }
```

## 最后

先到这里。接下来我们会接触其他工具。我们做这些的意义何在？大概是为了先理清思路。万事开头难，而我们一开始就把这些全都尝试了一遍。这给了我们信心，接下来，就是更多地探索这些软件了。

## 练习

* 学生像上面一样类似探索一遍。