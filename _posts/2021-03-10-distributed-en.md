---
layout: post
title: "Cloud Computing And Big Data Beginners"
---

*This blog post was translated by Mistral*

---
 This lesson covers the following topics:

* Spark
* Hadoop
* Kubernetes I'd like to talk about cloud computing, it seems we can't do without many tools: Hadoop, Hive, Hbase, ZooKeeper, Docker, Kubernetes, Spark, Kafka, MongoDB, Flink, Druid, Presto, Kylin, Elastic Search. Have you heard of them? I found these from job descriptions for a "Big Data Engineer" and "Distributed Backend Engineer". These are high-paying positions. Let's try installing them all and giving them a spin.

## Getting Started with Spark

Spark is an open-source, distributed computing system used for big data processing and machine learning. It provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.

To get started with Spark, you need to install it on your machine or cluster. Here's a step-by-step guide for installing Spark on a local machine using Homebrew on macOS:

1. Install Java Development Kit (JDK):

   ```
   brew install adoptopenjdk
   ```

2. Add JDK to environment variables:

   ```
   export JAVA_HOME=$(/usr/local/opt/openjdk@11/libexec)
   export PATH=$JAVA_HOME/bin:$PATH
   ```

3. Install Spark:

   ```
   brew install apache-spark
   ```

4. Add Spark to environment variables:

   ```
   export SPARK_HOME=$(brew --prefix apache-spark)
   export PATH=$SPARK_HOME/bin:$PATH
   ```

5. Verify the installation:

   ```
   spark-shell --version
   ```

   You should see the Spark version number displayed.

Now that Spark is installed, you can start using it for data processing and machine learning tasks. You can write Spark applications in Scala, Java, or Python. To learn more about Spark, check out the official documentation: https://spark.apache.org/docs/latest/index.html. The website states that `Spark` is an engine for analyzing large-scale data. `Spark` is a suite of libraries. It seems different from `Redis` which is divided into server and client. `Spark` is only used on the client side. Downloaded the latest version from the website, `spark-3.1.1-bin-hadoop3.2.tar`.

```bash
.
├── LICENSE
├── NOTICE
├── R
├── README.md
```-- RELEASE
----- bin
----- conf
----- data
----- examples
----- jars
----- kubernetes
----- licenses
----- python
----- sbin

Translation:
RELEASE directory:
- bin
- conf
- data
- examples
- jars
- kubernetes
- licenses
- python
- sbin It seems to be some analysis libraries written in various languages.

The website also mentions that you can directly install the dependency library on Python with `pip install pyspark`. install pyspark
Collecting pyspark
Downloading pyspark-3.1.1.tar.gz (212.3 MB)
Collecting py4j (tag: v0.10.9)
Downloading py4j-0.10.9-py2.py3-none-any.whl (198 kB): Building wheels for collected packages: pyspark
Building wheel for pyspark (setup.py) ... done
Created wheel for pyspark: filename=pyspark-3.1.1-py2.py3-none-any.whl size=212767604 sha256=0b8079e82f3a5bcadad99179902d8c8ff9f8eccad928a469c11b97abdc960b72
Successfully built pyspark
Installing collected packages: py4j, pyspark
Successfully installed py4j-0.10.9 pyspark-3.1.1

Translation:

Building wheels for pyspark
Successfully built pyspark
Installing: py4j, pyspark
Successfully installed py4j-0.10.9 pyspark-3.1.1: We have put it on.

This will check the official website for some examples.

```shell
./bin/run-example SparkPi 10
``` Oh, it turns out I can run the program in the just downloaded installation package. But an error occurred.

$ ./bin/run-example SparkPi 10
21/03/11 00:06:15 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
21/03/11 00:06:16 INFO ResourceUtils: No custom resources configured for spark.driver.
21/03/11 00:06:16 WARN Utils: Service 'sparkDriver' could not bind on a random free port. You may need to configure an appropriate binding address. Spark is a fast and general engine for processing data compatible with Hadoop. It can run in Hadoop clusters through YARN or Spark's standalone mode, and it can process data in HDFS, HBase, Cassandra, Hive, and any Hadoop InputFormat. It is designed to perform both batch processing, similar to MapReduce, and new workloads like streaming, interactive queries, and machine learning.
## Hadoop Explanation

Spark is a fast and versatile data processing engine that works seamlessly with Hadoop. It can operate in Hadoop clusters using YARN (Yet Another Resource Manager) or Spark's standalone mode. Spark can process data stored in Hadoop Distributed File System (HDFS), HBase, Cassandra, Hive, and any other Hadoop InputFormat.

Spark is designed to handle both batch processing, which is similar to MapReduce, and new workloads such as streaming data, interactive queries, and machine learning. This versatility makes Spark a powerful tool for handling large-scale data processing tasks in a distributed computing environment. I glanced at the official website and then I will install.

```shell
brew install hadoop
```

During the installation process, I will learn about it. Apache Hadoop is a framework for processing large data sets in a distributed manner across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each providing local computation and storage. Instead of relying on hardware for high-availability, the library itself is designed to detect and handle failures at the application layer, delivering a highly-available service on top of a cluster of computers, each of which may experience failures. To update Homebrew, first run:
Fetching latest Homebrew changes:
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow
These commands may take a few minutes to run due to the large size of the repositories.

Translation:
To update Homebrew, first run:
Fetching latest Homebrew core changes: git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
Fetching latest Homebrew cask changes: git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow
These commands may take a few minutes to run due to the large size of the repositories. This restriction has been imposed on GitHub's request as updating shallow clones is an expensive operation due to the tree layout and traffic of Homebrew/homebrew-core and Homebrew/homebrew-cask. We don't perform this automatically to avoid repeatedly carrying out an expensive unshallow operation in CI systems (which should instead be fixed to not use shallow clones). Sorry for the inconvenience.
Downloading <https://homebrew.bintray.com/bottles/openjdk-15.0.1.big_sur.bottle.tar.gz>
Already downloaded: /Users/lzw/Library/Caches/Homebrew/downloads/d1e3ece4af1d225bc2607eaa4ce85a873d2c6d43757ae4415d195751bc431962--openjdk-15.0.1.big_sur.bottle.tar.gz
Downloading <https://www.apache.org/dyn/closer.lua?path=hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz>
Already downloaded: /Users/lzw/Library/Caches/Homebrew/downloads/764c6a0ea7352bb8bb505989feee1b36dc628c2dcd6b93fef1ca829d191b4e1e--hadoop-3.3.0.tar.gz: Installing Hadoop dependencies: openjdk
: Installing openjdk as Hadoop dependency:
: Installing openjdk-15.0.1.big_sur.bottle.tar.gz
: Caveats
: To make the system Java wrappers find this JDK, symlink it with:
: sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

: openjdk is keg-only, which means it was not symlinked into /usr/local,
: because it shadows the macOS 'java' wrapper.: If you require OpenJDK to be in your PATH, run:
export PATH="/usr/local/opt/openjdk/bin:\$PATH" >> ~/lzw/.bash_profile

For compilers to locate OpenJDK, set:
export CPPFLAGS="-I/usr/local/opt/openjdk/include"

===
/usr/local/Cellar/openjdk/15.0.1: 614 files, 324.9MB
==> Installing Hadoop
/usr/local/Cellar/hadoop/3.3.0: 21,819 files, 954.7MB, built in 2 minutes 15 seconds Upgrading 1 dependent:
maven 3.3.3 to 3.6.3_1
Upgrading maven from 3.3.3 to 3.6.3_1
Downloading apache-maven-3.6.3-bin.tar.gz from https://www.apache.org/dyn/closer.lua?path=maven/maven-3/3.6.3/binaries/
Downloading apache-maven-3.6.3-bin.tar.gz from https://mirror.olnevhost.net/pub/apache/maven/maven-3/3.6.3/binaries/
100.0%
Error: The `brew link` step did not complete successfully.
The formula built, but is not symlinked into /usr/local
Could not symlink bin/mvn
Target /usr/local/bin/mvn A symlink under the name of maven is yours. You can unlink it using:

```bash
brew unlink maven
```

To forcefully link it and overwrite any conflicting files:

```bash
brew link --overwrite maven
```

To display a list of files that would be deleted before performing the linking:

```bash
brew link --overwrite --dry-run maven
```

Potential conflicting files:

[No translation needed for this part as it's in English.] /usr/local/bin/mvn -> /usr/local/Cellar/maven/3.6.3_1/bin/mvn
/usr/local/bin/mvnDebug -> /usr/local/Cellar/maven/3.6.3_1/bin/mvnDebug
/usr/local/bin/mvnyjp -> /usr/local/Cellar/maven/3.6.3_1/bin/mvnyjp

==> Summary
Successfully upgraded /usr/local/Cellar/maven/3.3.3 to 3.6.3_1
==> Installing: /usr/local/Cellar/maven/3.6.3_1: 87 files, 10.7MB, built in 7 seconds
==> Removing: /usr/local/Cellar/maven/3.3.3: 92 files, 9MB
==> Checking for dependents of upgraded formulae...
==> No broken dependents found!
==> Caveats
==> openjdk
The OpenJDK Java runtime is required to run this formula.
Please install the OpenJDK formula (can be linked directly to the Homebrew version) before installing.

Or, if you prefer to install Oracle JDK, please install it from Oracle's website as Homebrew does not distribute Oracle JDK.

If you need to have only the Java runtime installed, please install the `openjdk-11` or `openjdk-15` package instead of this Maven formula. To make Java wrappers find this JDK, create a symlink:
sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

Note: openjdk is keg-only, so it wasn't symlinked into /usr/local, as it conflicts with macOS's `java` wrapper.

To make openjdk appear first in your PATH for executing Java commands, add this line to your .bash_profile:
echo 'export PATH="/usr/local/opt/openjdk/bin:$PATH"' >> /Users/lzw/.bash_profile

To enable compilers to find openjdk, you may need to set:
[environment variable]
JAVA_HOME="/usr/local/opt/openjdk"
[or]
export JAVA_HOME="/usr/local/opt/openjdk" Notice that `maven` was not linked properly in `brew`'s output log. Next, force link to version `3.6.3_1`.

```shell
  brew link --overwrite maven
```

`Hadoop` has been installed successfully.1. Hadoop Common: Common utilities for other Hadoop modules.
2. Hadoop Distributed File System (HDFS): Distributed file system with high-throughput access to application data.
3. Hadoop YARN: Framework for job scheduling and cluster resource management.1. Hadoop MapReduce: A YARN-based system for processing large data sets in parallel.
2. Hadoop Ozone: An object store for Hadoop.

Usage: hadoop [OPTIONS] COMMAND [COMMAND_OPTIONS] Hadoop [OPTIONS] [CLASSNAME] [CLASSNAME [OPTIONS]]
// CLASSNAME is a user-provided Java class

// OPTIONS can be none or any of:

--config-dir <Hadoop config directory>
--debug
--help
build-paths
--hosts list[,of,host[,names]] hosts to use in slave mode host file name list of hosts for slave mode
log level level set log4j level for this command
workers worker mode on

SUBCOMMAND is one of:

Admin Commands:
daemonlog get/set log level for each daemon:

archive - create Hadoop archive
checknative - check availability of native Hadoop and compression libraries
classpath - print class path for Hadoop jar and required libraries
conftest - validate configuration XML files
credential - interact with credential providers
distch - distributed metadata changer
distcp - copy files or directories recursively1. dtutil – operations related to delegation tokens
2. envvars – display computed Hadoop environment variables
3. fs – run a generic filesystem user client
4. gridmix – submit a mix of synthetic job, modeling a profiled from production load
5. jar <jar> – run a jar file. NOTE: please use "yarn jar" to launch YARN applications, not this command.
6. jnipath – prints the java.library.path
7. kdiag – Diagnose Kerberos Problems
8. kerbname – show auth_to_local principal conversion
9. key – manage keys via the KeyProvider
10. rumenfolder – scale a rumen input trace.1. rumentrace: convert logs into rumen trace
2. s3guard: manage S3 metadata
3. trace: view and modify Hadoop tracing settings
4. version: print version

Daemon Commands:

5. kms: run Key Management Server (KMS)
6. registrydns: run registry DNS server. The official website provided some examples.

$ mkdir input
$ cp etc/hadoop/*.xml input I. hadoop-3.2.2
  II. bin
  III. libexec
  IV. sbin
  V. share
    VI. hadoop
      VII. mapreduce
        VIII. hadoop-mapreduce-examples-3.2.2.jar
  VI. etc
  VII. include
  VIII. lib
  IX. man
  X. pkg
  XI. sbin
  XII. start-script.sh
Run the following command to execute the Hadoop MapReduce example:

$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar grep input output 'dfs[a-z.]+'

Display the result:

$ cat output/*/LICENSE-binary
/LICENSE.txt
/NOTICE-binary
/NOTICE.txt
/README.txt
/bin
/etc
/include
/lib I. libexec
II. licenses-binary
III. sbin
IV. share

Encountered a `share` directory. But isn't Homebrew supposed to not have these additional files? Found Homebrew installation directory.

```bash
$ which hadoop
```:
Hadoop is a link to /usr/local/Cellar/hadoop/3.3.0/bin/hadoop.

Below is the output of the ls command in the /usr/local/Cellar/hadoop/3.3.0 directory:

lrwxr-xr-x  1 user admin  33 Mar 11 00:48 ../bin/hadoop -> ../Cellar/hadoop/3.3.0/libexec/share/hadoop/bin/hadoop
bin/
etc/
lib/
libexec/
libjars/
man/
share/
include/
lib/libhadoop.a
lib/libhdfs.a
lib/libhdfs-native.a
lib/libjavacpp.a
lib/libopenjpeg.a
lib/libsnappy.a
lib/libz.a
libjars/hadoop-annotations-2.7.2.jar
libjars/hadoop-auth-2.7.2.jar
libjars/hadoop-common-2.7.2.jar
libjars/hadoop-core-2.7.2.jar
libjars/hadoop-hdfs-2.7.2.jar
libjars/hadoop-mapreduce-client-core-2.7.2.jar
libjars/jackson-core-asl-1.9.13.jar
libjars/jackson-mapper-asl-1.9.13.jar
libjars/jackson-xc-1.9.13.jar
libjars/slf4j-api-1.7.25.jar
libjars/snappy-java-1.1.4.jar
libjars/zookeeper-3.4.13.jar
libjars/zstd-1.4.5.jar
man/man1/
man/man1/hadoop.1.gz
man/man1/hdfs.1.gz
man/man1/mapred.1.gz
man/man1/yarn.1.gz
share/hadoop/
share/hadoop/conf/
share/hadoop/conf/core-site.xml
share/hadoop/conf/hdfs-site.xml
share/hadoop/conf/mapred-site.xml
share/hadoop/conf/yarn-site.xml
share/hadoop/common/
share/hadoop/common/HadoopPermissions.java
share/hadoop/common/HadoopRuntime.java
share/hadoop/common/lib/
share/hadoop/common/lib/commons-cli-3.1.jar
share/hadoop/common/lib/jackson-core-asl-1.9.13.jar
share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar
share/hadoop/common/lib/jackson-xc-1.9.13.jar
share/hadoop/common/lib/slf4j-api-1.7.25.jar
share/hadoop/common/lib/snappy-java-1.1.4.jar
share/hadoop/common/lib/zookeeper-3.4.13.jar
share/hadoop/common/lib/zstd-1.4.5.jar
share/hadoop/common/lib/xmlenc-1.52.jar
share/hadoop/common/lib/xmlsec-1.4.2.jar
share/hadoop/common/lib/xmlsec-crypto-1.4.2.jar
share/hadoop/common/lib/xmlsec-keys-1.4.2.jar
share/hadoop/common/lib/xmltok-2.0.5.jar
share/hadoop/common/lib/xz-1.9.2.jar
share/hadoop/common/lib/zlib-1.2.11.jar
share/hadoop/common/lib/zstd-1.4.5.jar
share/hadoop/common/lib/zstd-jni-1.4.5.jar
share/hadoop/common/src/
share/hadoop/common/src/HadoopPermissions.java
share/hadoop/common/src/HadoopRuntime.java
share/hadoop/common/src/Misc.java
share/hadoop/common/src/NativeCodeLoader.java
share/hadoop/common/src/jni/
share/hadoop/common/src/jni/NativeCodeLoader.c
share/hadoop/common/src/jni/NativeCodeLoader.h
share/hadoop/common/src/jni/NativeCodeLoader.java
share/hadoop/common/src/jni/NativeCodeLoader.mk
share/hadoop/common/src/jni/NativeCodeLoader.s
share/hadoop/common/src/jni/NativeCodeLoader.txt
share/hadoop/common/src/jni/NativeCodeLoader.yml
share/hadoop/common/src/jni/NativeMethods.h
share/hadoop/common/src/jni/NativeMethods.java
share/hadoop/common/src/jni/NativeMethods.mk
share/hadoop/common/src/jni/NativeMethods.txt
share/hadoop/common/src/jni/NativeMethods.yml
share/hadoop/common/src/jni/NativeUtils.c
share/hadoop/common/src/jni/NativeUtils.h
share/hadoop/common/src/jni/NativeUtils.java
share/hadoop/common/src/jni/NativeUtils.mk
share/hadoop/common/src/jni/NativeUtils.s
share/hadoop/common/src/jni/NativeUtils.txt
share/hadoop/common/src/jni/NativeUtils.yml
share/hadoop/common/src/jni/hadoop_jni.c
share/hadoop/common/src/jni/hadoop_jni.h
share/hadoop/common/src/jni/hadoop_jni.java
share/hadoop/common/src/jni/hadoop_jni.mk
share/hadoop/common/src/jni/hadoop_jni.s
share/hadoop/common/src/jni/hadoop_jni.txt
share/hadoop/common/src/jni/hadoop_jni.yml
share/hadoop/common/src/jni/hadoop_jni_la-hadoop_jni.cmake
share/hadoop/common/src/jni/hadoop_jni_la-hadoop_jni.h
share/hadoop/common/src/jni/hadoop_jni_la-hadoop_jni.mk
share/hadoop/common/src/jni/hadoop_jni_la-hadoop_jni.txt
share/hadoop/common/src/jni/hadoop_jni_la-hadoop_jni.yml
share/hadoop/common/src/jni/hadoop_jni_la-native.cmake
share/hadoop/common/src/jni/hadoop_jni_la-native.h
share/hadoop/common/src/jni/hadoop_jni_la-native.mk
share/hadoop/common/src/jni/hadoop_jni_la-native.txt
share/hadoop/common/src/jni/hadoop_jni_la-native.yml
share/hadoop/common/src/jni/hadoop_jni_la-platform.cmake
share/hadoop/common/src/jni/hadoop_jni_la-platform.h
share/hadoop/common/src/jni/hadoop_jni_la-platform.mk
share/hadoop/common/src/jni/hadoop_jni_la-platform.txt
share/hadoop/common/src/jni/hadoop_jni_la-platform.yml
share/hadoop/common/src/jni/hadoop_jni_la-test.cmake
share/hadoop/common/src/jni/hadoop_jni_la-test.h
share/hadoop/common/src/jni/hadoop_jni_la-test.mk
share/hadoop/common/src/jni/hadoop_jni_la-test.txt
share/hadoop/common/src/jni/hadoop_jni_la-test.yml
share/hadoop/common/src/jni/hadoop_jni_la-util.cmake
share/hadoop/common/src/jni/hadoop_jni_la-util.h
share/hadoop/common/src/jni/hadoop_jni_la-util.mk
share/hadoop/common/src/jni/hadoop_jni_la-util.txt
share/hadoop/common/src/jni/hadoop_jni_la-util.yml
share/hadoop/common/src/jni/hadoop_jni_la-wrapper.cmake
share/hadoop/common/src/jni/hadoop_jni_la-wrapper.h
share/hadoop/common/src/jni/hadoop_jni_la-wrapper.mk
share/hadoop/common/src/jni/hadoop_jni_la-wrapper.txt
share/hadoop/common/src/jni/hadoop_jni_la-wrapper.yml
share/hadoop/common/src/jni/hadoop_jni_la-zstd.cmake
share/hadoop/common/src/jni/hadoop_jni_la-zstd.h
share/hadoop/common/src/jni/hadoop_jni_la-zstd.mk
share/hadoop/common/src/jni/hadoop_jni_la-zstd.txt
share/hadoop/common/src/jni/hadoop_jni_la-zstd.yml
share/hadoop/common/src/jni/hadoop_jni_la-zlib.cmake
share/hadoop/common/src/jni/hadoop_jni_la-zlib.h
share/hadoop/common/src/jni/hadoop_jni_la-zlib.mk
share/hadoop/common/src/jni/hadoop_jni_la-zlib.txt
share/hadoop/common/src/jni/hadoop_jni_la-zlib.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.h
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.h
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.h
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.yml
share/hadoop/common/src/jni/hadoop_jni_la-xz.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xz.h
share/hadoop/common/src/jni/hadoop_jni_la-xz.mk
share/hadoop/common/src/jni/hadoop_jni_la-xz.txt
share/hadoop/common/src/jni/hadoop_jni_la-xz.yml
share/hadoop/common/src/jni/hadoop_jni_la-zstd.cmake
share/hadoop/common/src/jni/hadoop_jni_la-zstd.h
share/hadoop/common/src/jni/hadoop_jni_la-zstd.mk
share/hadoop/common/src/jni/hadoop_jni_la-zstd.txt
share/hadoop/common/src/jni/hadoop_jni_la-zstd.yml
share/hadoop/common/src/jni/hadoop_jni_la-zlib.cmake
share/hadoop/common/src/jni/hadoop_jni_la-zlib.h
share/hadoop/common/src/jni/hadoop_jni_la-zlib.mk
share/hadoop/common/src/jni/hadoop_jni_la-zlib.txt
share/hadoop/common/src/jni/hadoop_jni_la-zlib.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.h
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.h
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.h
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.yml
share/hadoop/common/src/jni/hadoop_jni_la-xz.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xz.h
share/hadoop/common/src/jni/hadoop_jni_la-xz.mk
share/hadoop/common/src/jni/hadoop_jni_la-xz.txt
share/hadoop/common/src/jni/hadoop_jni_la-xz.yml
share/hadoop/common/src/jni/hadoop_jni_la-zstd.cmake
share/hadoop/common/src/jni/hadoop_jni_la-zstd.h
share/hadoop/common/src/jni/hadoop_jni_la-zstd.mk
share/hadoop/common/src/jni/hadoop_jni_la-zstd.txt
share/hadoop/common/src/jni/hadoop_jni_la-zstd.yml
share/hadoop/common/src/jni/hadoop_jni_la-zlib.cmake
share/hadoop/common/src/jni/hadoop_jni_la-zlib.h
share/hadoop/common/src/jni/hadoop_jni_la-zlib.mk
share/hadoop/common/src/jni/hadoop_jni_la-zlib.txt
share/hadoop/common/src/jni/hadoop_jni_la-zlib.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.h
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmlenc.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.h
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.mk
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.txt
share/hadoop/common/src/jni/hadoop_jni_la-xmlsec.yml
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.cmake
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.h
share/hadoop/common/src/jni/hadoop_jni_la-xmltok.mk
share/:
.
- client
  - hadoop-client-api-3.3.0.jar
  - hadoop-client-minicluster-3.3.0.jar
  - hadoop-client-runtime-3.3.0.jar
- common
  - hadoop-common-3.3.0-tests.jar
  - hadoop-common-3.3.0.jar hadoop-kms-3.3.0.jar
hadoop-nfs-3.3.0.jar
hadoop-registry-3.3.0.jar
jdiff
lib
sources
webapps
hdfs
hadoop-hdfs-3.3.0-tests.jar
hadoop-hdfs-3.3.0.jar hadoop-hdfs-client-3.3.0-tests.jar
hadoop-hdfs-client-3.3.0.jar
hadoop-hdfs-httpfs-3.3.0.jar
hadoop-hdfs-native-client-3.3.0-tests.jar
hadoop-hdfs-native-client-3.3.0.jar
hadoop-hdfs-nfs-3.3.0.jar
hadoop-hdfs-rbf-3.3.0-tests.jar
hadoop-hdfs-rbf-3.3.0.jar
jdiff
lib:
sources:
--------
webapps:

mapreduce:
---------
- hadoop-mapreduce-client-app-3.3.0.jar
- hadoop-mapreduce-client-common-3.3.0.jar
- hadoop-mapreduce-client-core-3.3.0.jar
- hadoop-mapreduce-client-hs-3.3.0.jar
- hadoop-mapreduce-client-hs-plugins-3.3.0.jar
- hadoop-mapreduce-client-jobclient-3.3.0-tests.jar
- hadoop-mapreduce-client-jobclient-3.3.0.jar hadoop-mapreduce-client-nativetask-3.3.0.jar
hadoop-mapreduce-client-shuffle-3.3.0.jar
hadoop-mapreduce-client-uploader-3.3.0.jar
hadoop-mapreduce-examples-3.3.0.jar
jdiff
lib-examples
sources
tools
dynamometer
lib resource estimator
sls
sources
yarn
├── csi
├── hadoop-yarn-api-3.3.0.jar
├── hadoop-yarn-applications-catalog-webapp-3.3.0.war
├── hadoop-yarn-applications-distributedshell-3.3.0.jar
├── hadoop-yarn-applications-mawo-core-3.3.0.jar
├── hadoop-yarn-applications-unmanaged-am-launcher-3.3.0.jar hadoop-yarn-client-3.3.0.jar
hadoop-yarn-common-3.3.0.jar
hadoop-yarn-registry-3.3.0.jar
hadoop-yarn-server-applicationhistoryservice-3.3.0.jar
hadoop-yarn-server-common-3.3.0.jar
hadoop-yarn-server-nodemanager-3.3.0.jar
hadoop-yarn-server-resourcemanager-3.3.0.jar
hadoop-yarn-server-router-3.3.0.jar
hadoop-yarn-server-sharedcachemanager-3.3.0.jar
hadoop-yarn-server-tests-3.3.0.jar hadoop-yarn-server-timeline-plugin-storage-3.3.0.jar
hadoop-yarn-server-web-proxy-3.3.0.jar
hadoop-yarn-services-api-3.3.0.jar
hadoop-yarn-services-core-3.3.0.jar
lib
sources
test
timelineservice
webapps
yarn-service-examples: You can see there are many `jar` packages.

$ mkdir input
$ ls
bin hadoop-config.sh hdfs-config.sh libexec sbin yarn-config.sh etc hadoop-functions.sh input mapred-config.sh share
$ cp etc/hadoop/*.xml input CD input/
capacity-scheduler.xml hadoop-policy.xml hdfs-site.xml kms-acls.xml mapred-site.xml
core-site.xml hdfs-rbf-site.xml httpfs-site.xml kms-site.xml yarn-site.xml

CD ..
JAR does not exist or is not a normal file: /usr/local/Cellar/hadoop/3.3.0/libexec/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar

CD ..
JAR /usr/local/Cellar/hadoop/3.3.0/libexec/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.0.jar grep input output 'dfs[a-z.]+'
WARNING util.NativeCodeLoader: Unable to load native-hadoop library. Using builtin-java classes where applicable. 2021-03-11 01:54:31 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2021-03-11 01:54:31 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).

Translation:

2021-03-11 01:54:31 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2021-03-11 01:54:31 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 seconds. 2021-03-11 1:54:35,374 INFO mapreduce.Job: map 100% reduce 100%
2021-03-11 1:54:35,374 INFO mapreduce.Job: Job job\_local2087514596\_0002 completed successfully
2021-03-11 1:54:35,377 INFO mapreduce.Job: Counters:
	File System Counters
		FILE: Number of bytes read=1204316
		FILE: Number of bytes written=3565480
		FILE: Number of read operations=0
		FILE: Number of large read operations=0

Translation:
2021-03-11 1:54:35.374 INFO mapreduce.Job: map 100% reduce 100%
2021-03-11 1:54:35.374 INFO mapreduce.Job: Job job_local2087514596_0002 completed successfully
2021-03-11 1:54:35.377 INFO mapreduce.Job: Counters:
	File System Counters
		FILE: Number of bytes read = 1204316
		FILE: Number of bytes written = 3565480
		FILE: Number of read operations = 0
		FILE: Number of large read operations = 0.: Write operations = 0
Map-Reduce Framework:,
Map input records = 1,
Map output records = 1,
Map output bytes = 17,
Map output materialized bytes = 25,
Input split bytes = 141,
Combine input records = 0,
Combine output records = 0,
Reduce input groups = 1. Reduce shuffle bytes = 25
Reduce input records = 1
Reduce output records = 1
Spilled Records = 2
Shuffled Maps = 1
Failed Shuffles = 0
Merged Map outputs = 1
GC time elapsed (ms) = 57
Total committed heap usage (bytes) = 772800512

Shuffle Errors:
None. BAD_ID = 0
CONNECTION = 0
IO_ERROR = 0
WRONG_LENGTH = 0
WRONG_MAP = 0

File Input Format Counters
Bytes Read = 123

File Output Format Counters
Bytes Written = 23 Continue looking.

$ cat output/\*
1	dfsadmin What does this mean exactly? No worries, we have managed to get `Hadoop` running. And we have run the first single machine version of the computing example.

Back to Spark. Let's look at an example.

```python In this part, there is a reference to HDFS files. After looking it up, I found that you can create HDFS files as follows:

text_file = sc.textFile("hdfs://<HDFS_Namenode_address>:<HDFS_Port>/<path>")
# For example, "hdfs://namenode:50070/user/username/input"

counts = text_file.flatMap(lambda line: line.split(" ")) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile("hdfs://<HDFS_Namenode_address>:<HDFS_Port>/<output_path>")
# For example, "hdfs://namenode:50070/user/username/output"
```

Here's the English translation of the code:

```python
text_file = sc.textFile("hdfs://<HDFS_Namenode_address>:<HDFS_Port>/<path>")
counts = text_file.flatMap(lambda line: line.split(" ")) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://<HDFS_Namenode_address>:<HDFS_Port>/<output_path>")
```

Replace `<HDFS_Namenode_address>`, `<HDFS_Port>`, `<path>`, and `<output_path>` with the appropriate values for your HDFS setup. Hdfs: usage: hdfs [OPTIONS] SUBCOMMAND [SUBCOMMAND_OPTIONS]

The following is the command to create a new directory in HDFS using the 'hdfs' command-line utility:

```shell
$ hdfs dfs -mkdir /test
```

Translation:

Create directory in HDFS:
```
hdfs dfs -mkdir /test
``` OPTIONS can be none or any of:

--build-paths Try to add class files from build tree
--config-dir Hadoop config directory
--daemon (start|status|stop) Operate on a daemon
--debug Turn on shell script debug mode
--help Usage information
--hostnames list [of, host, names] Hosts to use in worker mode
--hosts file List of hosts to use in worker mode-- log level (specify level for log4j)
-- workers (enable worker mode)

SUBCOMMAND can be one of:

Admin Commands:

cacheadmin (configure HDFS cache)
crypto (configure HDFS encryption zones)1. debug - run HDFS debug commands using a Debug Admin
2. dfsadmin - run DFS admin client
3. dfsrouteradmin - manage Router-based federation
4. ec - run HDFS ErasureCoding CLI
5. fsck - run DFS filesystem checking utility
6. haadmin - run DFS HA admin client
7. jmxget - get JMX exported values from NameNode or DataNode
8. oev - apply offline edits viewer to an edits file
9. oiv - apply offline fsimage viewer to an fsimage
10. oiv_legacy - apply offline fsimage viewer to a legacy fsimage- storage policies list/get/set/satisfyStoragePolicy block storage policies
- Client Commands:
classpath print the class path needed to get the Hadoop jar and the required libraries
dfs run a filesystem command on the file system
envvars display computed Hadoop environment variables
fetchdt fetch a delegation token from the NameNode
getconf get config values from configuration
groups get the groups which users belong to

Translation:

storage policies list get set satisfyStoragePolicy block storage policies
Client Commands:
classpath print the class path needed to get the Hadoop jar and the required libraries
dfs run a filesystem command on the file system
envvars display computed Hadoop environment variables
fetchdt fetch a delegation token from the NameNode
getconf get config values from configuration
groups get the groups which users belong to lsSnapshottableDir // lists all snapshottable directories owned by the current user
snapshotDiff // differs two snapshots of a directory or differs the current directory contents with a snapshot
version // prints the version

Daemon Commands:

balancer // runs a cluster balancing utility
datanode // runs a DFS datanode
dfsrouter // runs the DFS router
diskbalancer // distributes data evenly among disks on a given node1. Run HttpFS server, the HDFS HTTP Gateway
2. Run the DFS journalnode
3. Run a utility to move block replicas across storage types (mover)
4. Run the DFS namenode
5. Run an NFS version 3 gateway (nfs3)
6. Run a portmap service
7. Run the DFS secondary namenode
8. Run external storage policies satisfier (sps)
9. Run the ZK Failover Controller daemon (zkfc) continued modifying the code.

SUBCOMMAND:
if len(sys.argv) <= 1:
print("Usage: SUBCOMMAND [options]")
sys.exit(1)

if sys.argv[1] == "-h":
print("Help for SUBCOMMAND:")
print("Usage: SUBCOMMAND [options]")
print("Options:")
print("-h, --help            show this help message and exit")
sys.exit(0)
```
This is the modified code for SUBCOMMAND. It will print help message when invoked without any parameters or with the "-h" option. From pyspark.sql import SparkSession

SparkSession object creation and configuration:

spark = SparkSession.builder \
.master("local[*]") \
.config("spark.driver.bindAddress", "127.0.0.1") \
.getOrCreate()

SparkContext object creation:
sc = spark.sparkContext

Text file processing:
text_file = sc.textFile("a.txt")

FlatMap operation: Splitting lines into words
counts = text_file.flatMap(lambda line: line.split(" "))

Map operation: Creating tuples of words and their counts
counts = counts.map(lambda word: (word, 1)) notice that .config('spark.driver.bindAddress', '127.0.0.1') is important. Otherwise, an error will occur: "Service 'sparkDriver' could not bind on a random free port. You may check whether configuring an appropriate binding address"
The given Chinese text is not providing any Chinese characters or sentences that need to be translated into English. Instead, it is a comment in Python explaining the importance of setting the Spark driver bind address to '127.0.0.1' to avoid an error when running a Spark application. The English text itself is already in the desired format. However, an error occurred again.

Error message:
```python
Caused by: org.apache.spark.api.python.PythonException: Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/pyspark/python/lib/pyspark.zip/pyspark/worker.py", line 473, in <module>
    raise Exception(("Python in worker has different version %s than that in " % (w.PythonVersion) +
Exception: Python in worker has different version 3.8 than that in driver 3.9, PySpark cannot run with different minor versions. Please check environment variables PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are correctly set.
```

Translation:

However, an error occurred again due to different Python versions.

PySpark error message:
```python
Caused by org.apache.spark.api.python.PythonException: Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/pyspark/python/lib/pyspark.zip/pyspark/worker.py", line 473, in <module>
    raise Exception(("Python in worker has different version %s than that in " % (w.PythonVersion) +
Exception: Python in worker has different version 3.8 than that in driver 3.9. PySpark cannot run with different minor versions. Please check environment variables PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are correctly set.
``` Alter `.bash_profile`:

```shell
PYSPARK_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
PYSPARK_DRIVER_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
```

Translation:
Modify `.bash_profile`:

```shell
PYSPARK_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
PYSPARK_DRIVER_PYTHON=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
``` Still encountering the same error. After understanding it in depth, it might be because `spark` was not loaded with this environment variable during runtime, not using the default environment variable from the terminal.

You need to set it in the code:

```python
import os

# Set spark environments
os.environ["SPARK_HOME"] = "/path/to/spark"
``` These lines set the environment variables for PySpark to use the specified Python interpreter:

os.environ['PYSPARK_PYTHON'] = '/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3'

In English, the translation would be:

os.environ['PYSPARK_PYTHON'] = '/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3'
```

This will run.

(Note: There is no English translation provided as the text is already in English.) 21-03-11 02:54:52 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
PythonRDD[6] at RDD at PythonRDD.scala:53

Generated a file named `b.txt`.
```

English Translation:

21st March 2011, 02:54:52 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
PythonRDD[6] at RDD at PythonRDD.scala:53

Generated a file named `b.txt`. open it.

```shell
$ cat b.txt/part-00000
[
  {
    "id": 1,
    "name": "Alice",
    "age": 25,
    "city": "New York"
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 30,
    "city": "Chicago"
  },
  {
    "id": 3,
    "name": "Charlie",
    "age": 35,
    "city": "Miami"
  }
]
```

This is the content of the file 'b.txt/part-00000'. It is a JSON file containing an array of objects, each representing a person with an id, name, age, and city. two things worked on of college, writing, programming. Didn't worked on of school (eight times). Didn't didn't. probably are short, awful. They plot, just characters, them them.

Translation:

They are probably short and awful. They plot, just characters, them them.

So the English translation without any Chinese characters or punctuation would be:

They are probably short awful. They plot just characters them them.: Success! Does this ring a bell. This is similar to the `Hadoop` example.

```shell
$ cat output/*
1	dfsadmin
```

Translation:
Success! Is this familiar? This is similar to the Hadoop example.

```shell
$ cat output/*
1	dfsadmin
``` These files are called `HDFS`. Here, `Spark` is used to count words. A few simple sentences, quite convenient.

Next, let's play around with `Kubernetes`, also known as `k8s`, where the eight characters in the middle are abbreviated as 8. It is a suite of open-source tools for automating deployment, scaling, and management of containerized applications. `kubectl` is a command-line tool used to run commands on a K8s cluster. It can be used to deploy applications, view and manage cluster resources, and view logs.

Similarly, it can be installed using Homebrew.

```bash
brew install kubectl
``` Output log:

Downloading https://homebrew.bintray.com/bottles/kubernetes-cli-1.20.1.big_sur.bottle.tar.gz
Downloading from https://d29vzk4ow07wi7.cloudfront.net/0b4f08bd1d47cb913d7cd4571e3394c6747dfbad7ff114c5589c8396c1085ecf?response-content-disposition=attachment%2Ftar
100.0%: Installation successful.
===

Caveats:
Bash completion installed to:
/usr/local/etc/bash_completion.d
===

Summary:
🍺 /usr/local/Cellar/kubernetes-cli/1.20.1: 246 files, 46.1MB Client Version: version.Info{Major="1", Minor="20", GitVersion="v1.20.1", GitCommit="c4d752765b3bbac2237bf87cf0b1c2e307844666", GitTreeState="clean", BuildDate="2020-12-19T08:38:20Z", GoVersion="go1.15.5", Compiler="gc", Platform="darwin/amd64"}
```

Find more details at: <https://kubernetes.io/docs/reference/kubectl/overview/>

Basic Commands (Beginner):
- create: Create a resource from a file or standard input.
- expose: Expose a replication controller, service, deployment or pod as a new Kubernetes Service.
- run: Run a specific image on the cluster.
- set: Set specific features on objects.: Intermediate Level Commands:
explain: Resource documentation
get: Display one or more resources
edit: Edit a resource on the server
delete: Delete resources by filenames, stdin, resources and names, or by resources and label selector

: Deploy Level Commands:
rollout: Manage the rollout of a resource
scale: Set a new size for a Deployment, ReplicaSet or Replication Controller1. Autoscale: Automatically adjust the number of replicas for a Deployment, ReplicaSet, or ReplicationController.
2. certificate: Manage certificate resources.
3. cluster-info: Display cluster information.
4. top: Show resource (CPU/Memory/Storage) usage.
5. cordon: Mark a node as unschedulable.
6. uncordon: Mark a node as schedulable.
7. drain: Drain a node in preparation for maintenance.
8. taint: Update the taints on one or more nodes.: Troubleshooting and Debugging Commands:
 describe: Show details of a specific resource or group of resources
 logs: Print the logs for a container in a pod
 attach: Attach to a running container
 exec: Execute a command in a container
 port-forward: Forward one or more local ports to a pod
 proxy: Run a proxy to the Kubernetes API server
 cp: Copy files and directories to and from containers.
 auth: Inspect authorization.1. debug: Create debugging sessions for troubleshooting workloads and nodes

Advanced Commands:
1. diff: Compare live version with would-be applied version
2. apply: Apply a configuration to a resource using a filename or stdin
3. patch: Update specific field(s) of a resource
4. replace: Replace a resource using a filename or stdin
5. wait: Experimental: Wait for a specific condition on one or many resources.
6. kustomize: Build a kustomization target from a directory or a remote URL. Settings Commands:
- label: update labels on a resource
- annotate: update annotations on a resource
- completion: generate shell completion code (bash or zsh)

Other Commands:
- api-resources: list supported API resources on the server
- api-versions: list supported API versions on the server (in the format "group/version")
- config: modify kubeconfig files
- plugin: utilities for interacting with plugins. Print client and server version information.

Usage:
kubectl [flags] [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).

Display client and server versions. Create a configuration file.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
``` matchLabels:
- app="nginx"
minReadySeconds: 5
template:
  metadata:
    labels:
    - app="nginx"
  spec:
    containers:
    - name: "nginx" Nginx deployment with version 1.14.2:

Image: nginx:1.14.2
Ports:
- ContainerPort: 80 The connection to the server localhost:8080 was refused. Please check if the specified host or port is correct. When using the official website's terminal, try running the following:

$ start.sh
Starting Kubernetes...
minikube version: v1.8.1
commit: cbda04cf6bbe65e987ae52bb393c10099ab62014 Minikube version: v1.8.1 on Ubuntu 18.04.4 LTS
Using none driver based on user configuration
Running on localhost (2 CPUs, 2460MB memory, 145651MB disk)
...

Preparing Kubernetes: v1.17.3 on Docker 19.03.6
- kubelet resolv-conf: /run/systemd/resolve/resolv.conf
Launching Kubernetes
Enabling addons: default-storageclass, storage-provisioner
Configuring local host environment continued to our terminal.

kubectl configured for "minikube"
'dashboard' addon enabled
Kubernetes started. Kubectl version:
Client Version: {Major: "1", Minor: "20", GitVersion: "v1.20.1", GitCommit: "c4d752765b3bbac2237bf87cf0b1c2e307844666", GitTreeState: "clean", BuildDate: "2020-12-19T08:38:20Z", GoVersion: "go1.15.5", Compiler: "gc", Platform: "darwin/amd64"}

Kubectl version:
Client Version: {Major: "1", Minor: "20", GitVersion: "v1.20.1", GitCommit: "c4d752765b3bbac2237bf87cf0b1c2e307844666", GitTreeState: "clean", BuildDate: "2020-12-19T08:38:20Z", GoVersion: "go1.15.5", Compiler: "gc", Platform: "darwin/amd64"}
Error: The connection to the server localhost:8080 was refused. Please check if it is running and try again.

[Note: The `--client` option is not necessary when running `kubectl version` command and it doesn't cause any errors.] The document states that you need to install Minikube first.

```shell
$ brew install minikube
==> Downloading https://homebrew.bintray.com/bottles/minikube-1.16.0.big_sur.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/1b6d7d1b97b11b6b07e4fa531c2dc21770da290da9b2816f360fd923e00c85fc?response-content-disposition=a
######################################################################## 100.0%
==> Pouring minikube-1.16.0.big_sur.bottle.tar.gz
==> Caveats
```

Translation:
You need to install Minikube first. Use the following command in your terminal:

```shell
$ brew install minikube
```

The installation process will download the required package from the specified URL and install it. After the installation is complete, there will be caveats (additional instructions or information) that you may need to follow. Bash completion has been installed to: /usr/local/etc/bash_completion.d
==============
Minikube: 
/usr/local/Cellar/minikube/1.16.0: 8 files, 64.6MB
$ minikube start Minikube v1.16.0 on Darwin 11.2.2
🥳  minikube 1.18.1 is available! Download it: <https://github.com/kubernetes/minikube/releases/tag/v1.18.1>
💡  To disable this notice, run: 'minikube config set WantUpdateNotification false'

✨  Automatically selected the virtualbox driver
📊  Downloading VM boot image ...
 > minikube-v1.16.0.iso.sha256: 65 B / 65 B [----------------] 100.00% ? p/s 0s
 > minikube-v1.16.0.iso: 212.62 MiB / 212.62 MiB [] 100.00% 5.32 MiB p/s 40s
👍  Starting control plane node minikube in cluster minikube
💾  Downloading Kubernetes v1.20.0 preload ...

Successfully installed minikube v1.16.0. Starting control plane node ...
Downloading Kubernetes v1.20.0 preload ...

(Note: The text after "👍" is assumed to be a success message and not part of the original Chinese text.) Preloaded images-k8s-v8-v1....: 491.00 MiB / 491.00 MiB 100.00% 7.52 MiB
Creating virtualbox VM (CPUs=2, Memory=4000MB, Disk=20000MB) ...
❗ This VM is having trouble accessing https://k8s.gcr.io
💡 To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
🐳 Preparing Kubernetes v1.20.0 on Docker 20.10.0 ...
- Generating certificates and keys ...
- Booting up control plane ...
- Configuring RBAC rules ...
Verifying Kubernetes components...
🌟 Enabled addons: storage-provisioner, default-storageclass Kubectl is now configured to use "minikube" cluster and "default" namespace by default.

Next, let's access this cluster.

```bash
$ kubectl get po -A
NAMESPACE   NAME                               READY   STATUS    RESTARTS   AGE
``` Kube-system  coredns-74ff55c5b-ndbcr        1/1     Running    0          60s
kube-system  etcd-minikube                    0/1     Running    0          74s
kube-system  kube-apiserver-minikube         1/1     Running    0          74s
kube-system  kube-controller-manager-minikube 1/1     Running    0          74s
kube-system  kube-proxy-g2296                  1/1     Running    0          60s
kube-system  kube-scheduler-minikube         0/1     Running    0          74s
kube-system  storage-provisioner             1/1     Running    1          74s

Translation:

kube-system is the namespace for Kubernetes system components. The following lines represent the status of various components in that namespace:

- coredns-74ff55c5b-ndbcr: 1/1 Running, replicas: 1, pods: 1, available: 1, uptime: 60s
- etcd-minikube: 0/1 Running, replicas: 0, pods: 1, available: 1, uptime: 74s
- kube-apiserver-minikube: 1/1 Running, replicas: 1, pods: 1, available: 1, uptime: 74s
- kube-controller-manager-minikube: 1/1 Running, replicas: 1, pods: 1, available: 1, uptime: 74s
- kube-proxy-g2296: 1/1 Running, replicas: 1, pods: 1, available: 1, uptime: 60s
- kube-scheduler-minikube: 0/1 Running, replicas: 0, pods: 1, available: 1, uptime: 74s
- storage-provisioner: 1/1 Running, replicas: 1, pods: 1, available: 1, capacity: 1Gi, allocated: 0Gi, uptime: 74s Open `minikube` dashboard.

$ minikube dashboard
⚡ Enabling dashboard ...
💭 Verifying dashboard health ...
🚀 Launching proxy ...
💭 Verifying proxy health ...
🎉 Opening <http://127.0.0.1:50030/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/> in your default browser... How to turn it off.

(This text seems incomplete as it lacks context and a clear question or instruction.) Minikube:
Manages and provisions local Kubernetes clusters for development workflows.

Basic Commands:
start: Starts a local Kubernetes cluster
status: Displays the status of a local Kubernetes cluster
stop: Stops a running local Kubernetes cluster1. delete - Deletes a local Kubernetes cluster
2. dashboard - Access the Kubernetes dashboard running within the minikube cluster
3. pause - Pauses Kubernetes
4. unpause - Unpauses Kubernetes

Images Commands:
1. docker-env - Configure environment to use minikube's Docker daemon
2. podman-env - Configure environment to use minikube's Podman service
3. cache - Manage local image in minikube (add, delete, or push)1. Configuration and Management:
addons - enable or disable minikube addon
config - modify persistent configuration values
profile - get or list current profiles (clusters)
update-context - update kubeconfig in case of IP or port change

2. Networking and Connectivity:
service - return a URL to connect to a service
tunnel - connect to LoadBalancer services1. Advanced Commands:
- mount: Mounts the specified directory into minikube
- ssh: Logs into the minikube environment (for debugging)
- kubectl: Runs a kubectl binary matching the cluster version
- node: Adds, removes, or lists additional nodes

2. Troubleshooting Commands:
- ssh-key: Retrieves the ssh identity key path of the specified node
- ssh-host: Retrieves the ssh host key of the specified node
- ip: Retrieves the IP address of the specified node logs: returns logs for debugging a local Kubernetes cluster
update-check: prints current and latest version number
version: prints the version of minikube

Other Commands:
completion: generates command completion for a shell.

Use "minikube <command> --help" for more information about a given command. It's `minikube stop`.

Back to `kubernetes`, it's working normally now. Kubernetes control plane is running at <https://192.168.99.100:8443>
KubeDNS is running at <https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy>

For more detailed debugging and diagnosis of cluster issues, use 'kubectl cluster-info dump'. when opening <https://192.168.99.100:8443>, browser shows:

{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {
    // metadata information "status": "Failure",
"message": "Forbidden: User 'system:anonymous' is not authorized to access path '/'",
"reason": "Forbidden",
"details": {},
"code": 403:
[
  {
    "kind": "Status"
  }
]

Visit `https://168.192.111.090:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy`:

[
  {
    "kind": "Status"
  }
] "apiVersion": "v1",
"metadata": {},
"status": "Failure",
"message": "Service 'kube-dns:dns' is forbidden: User 'system:anonymous' cannot get resource 'services/proxy' in API group '' in namespace 'kube-system'",
"reason": "Forbidden",
"details": {
"name": "kube-dns:dns",
"kind": "services"
}

Translation:
apiVersion: v1,
metadata: {},
status: Failure,
message: Service 'kube-dns:dns' is forbidden: User 'system:anonymous' cannot get resource 'services/proxy' in API group '' in namespace 'kube-system',
reason: Forbidden,
details: {
name: kube-dns:dns,
kind: services{"code": 403}

Here's the English translation of the given Chinese text:

Try the new configuration.

However, the Chinese text provided does not contain any Chinese characters in the given JSON format. The given text is just a comment in English in a shell script. Therefore, no Chinese characters need to be translated. The JSON object only contains an error code of 403. Kubectl apply -f simple\_deployment.yaml
Deployment created.

Note: The given Chinese text seems to be a comment or note, not a command to be translated. The English part of the text is already provided in the command line format at the beginning. Checking if stopped.

1 nodes stopped. Minikube: The control plane node is not running. Start a cluster by running: "minikube start" Docker is a container platform to accelerate creation, sharing, and running of modern applications. Download from official website.

![docker](/assets/images/distributed/docker.png)

Client is a bit sluggish. Let's use command line instead. Docker:

Usage: docker [OPTIONS] COMMAND
A self-sufficient runtime for containers

Options:
--config string           Location of client config files (default "/Users/lzw/.docker")
-c, --context string      Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with "docker")-D, --debug: Enable debug mode
--host, --list: Daemon socket(s) to connect to
-l, --log-level: Set the logging level (debug|info|warn|error|fatal) (default info)
--tls: Use TLS; implied by --tlsverify
--tlscacert: Trust certs signed only by this CA (default "/Users/lzw/.docker/ca.pem")
--tlscert: Path to TLS certificate file (default "/Users/lzw/.docker/cert.pem")
--tlskey: Path to TLS key file (default "/Users/lzw/.docker/key.pem")
--tlsverify: Use TLS and verify the remote
-v, --version: Print version information and quit.1. Management Commands:
2. app - Docker App (Docker Inc., v0.9.1-beta3)
3. builder - Manage builds
4. buildx - Build with BuildKit (Docker Inc., v0.5.1-docker)
5. config - Manage Docker configs
6. container - Manage containers
7. context - Manage contexts
8. image - Manage images
9. manifest - Manage Docker image manifests and manifest lists. network management
Manage networks (nodes)
plugin management
Docker Scan (Docker Inc., v0.5.0)
Manage Docker secrets
Manage services
Manage Docker stacks
Manage Swarm
Manage Docker system
Manage trust on Docker images volume management

Commands:
attach - Attach local standard input, output, and error streams to a running container
build - Build an image from a Dockerfile
commit - Create a new image from a container's changes
cp - Copy files/folders between a container and the local filesystem
create - Create a new container
diff - Inspect changes to files or directories on a container's filesystem
events - Get real time events from the server executes: runs a command in a running container
exports: exports a container's filesystem as a tar archive
history: shows the history of an image
images: lists images
imports: imports the contents from a tarball to create a filesystem image
info: displays system-wide information
inspect: returns low-level information on Docker objects
kill: kills one or more running containers
load: loads an image from a tar archive or STDIN
login: logs in to a Docker registry1. logout - Log out from Docker registry
2. logs - Fetch container logs
3. pause - Pause processes in one or more containers
4. port - List port mappings or a specific mapping for a container
5. ps - List containers
6. pull - Pull an image or repository from a registry
7. push - Push an image or repository to a registry
8. rename - Rename a container
9. restart - Restart one or more containers
10. rm - Remove one or more containers1. Remove one or more images: remove
2. Run a command in a new container: run
3. Save one or more images to a tar archive: save
4. Search the Docker Hub for images: search
5. Start one or more stopped containers: start
6. Display a live stream of container(s) resource usage statistics: stats
7. Stop one or more running containers: stop
8. Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE: tag
9. Display the running processes of a container: top
10. Unpause all processes within one or more containers: unpause update - Update configuration of one or more containers
version - Display Docker version information
wait - Block until one or more containers stop and print their exit codes

Use 'docker COMMAND --help' for more information on a command.

For more assistance with Docker, refer to our guides at https://docs.docker.com/go/guides/ Follow the tutorial and try.
Unable to find image 'docker/getting-started:latest' locally
Pulling image docker/getting-started:latest
aad63a933944: Pull complete
b14da7a62044: Pull complete
343784d40d66: Pull complete six: Pull complete
Digest: sha256:d2c4fb0641519ea208f20ab03dc40ec2a5a53fdfbccca90bef14f870158ed577
Status: Downloaded newer image for docker/getting-started:latest
Error response from daemon: Ports are not available: listen tcp 0.0.0.0:80: bind: address already in use.

Try changing the port.

```

Translation:

six: Pull complete
Digest: sha256:d2c4fb0641519ea208f20ab03dc40ec2a5a53fdfbccca90bef14f870158ed577
Status: Downloaded newer image for docker/getting-started:latest
Error: Ports are not available: listen tcp 0.0.0.0:80: bind: address already in use.

Try changing the port. docker run -d -p 8080:80 docker/getting-started 45bb95fa1ae80adc05cc498a1f4f339c45c51f7a8ae1be17f5b704853a5513a5

Open a browser, indicating that we have started `docker`.

![browser](/assets/images/distributed/browser.png)

The command translates to:

Run a container in the background from the image 'docker/getting-started'. Expose port 8080 of the container to the host's port 8080. The container ID is 45bb95fa1ae80adc05cc498a1f4f339c45c51f7a8ae1be17f5b704853a5513a5. Stop container. Use the ID that was just returned.

$ docker stop 45bb95fa1ae80adc05cc498a1f4f339c45c51f7a8ae1be17f5b704853a5513a5
45bb95fa1ae80adc05cc498a1f4f339c45c51f7a8ae1be17f5b704853a5513a5

At this point, the website cannot be opened. This implies that `docker` functions like a virtual machine.

Open the official website.
[For Flink, there is no provided Chinese text in the input.] Flink is for stateful stream processing. What does stateful mean? I'm not clear yet. The picture above is quite interesting. Let's try to figure it out.

It requires a Java environment. Download the latest version from the website: `flink-1.12.2-bin-scala_2.11.tar`

Java version:
java version "1.8.0_151"
Java(TM) SE Runtime Environment (build 1.8.0_151-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode) Starting cluster.
Starting standalone session daemon on host lzwjava.
Starting task executor daemon on host lzwjava. Executing WordCount example with default input data set.
Use "--input" to specify file input.
Printing result to stdout. Use "--output" to specify output path.
Submitted Job with JobID 60f3537647c20c2a6654359bd34edab807
Program execution finished.
Finished Job with JobID 60f3537647c20c2a6654359bd34edab807
Job Runtime: 757 ms (nymph, 1)
(in, 3)
(thy, 1)
(orisons, 1)
(be, 4)
(all, 2)

Translation:

nymph, 1
in, 3
thy, 1
orisons, 1
be, 4
all, 2 I. my sins
II. remember d d d d

English Translation:
I. my sins
II. remember dddd

Or, if we assume "d" stands for "days":
I. my sins
II. remember for days d d d d. Stopping task executor daemon (pid: 41812) on host lzwjava.

Yes, I've got it. It's similar to `Spark`.

## Kylin

(Note: The given Chinese text seems to be incomplete as it contains extra "Yes, I've got it." which doesn't seem to fit the context.) Open the official website.

Apache Kylin is an open source, distributed Analytical Data Warehouse for Big Data. It was designed to provide OLAP (Online Analytical Processing) capability in the big data era. By renovating the multi-dimensional cube and precalculation technology on Hadoop and Spark, Kylin can achieve near constant query speed regardless of the ever-growing data volume. It reduces query latency from minutes to sub-second, bringing online analytics back to big data.1. Identify Star/Snowflake Schema on Hadoop.
2. Build Cube from identified tables.
3. Query using ANSI-SQL and get results in sub-second, via ODBC, JDBC or RESTful API.

Apache Kylin lets you query billions of rows at sub-second latency in 3 steps:

1. Identify a Star/Snowflake Schema on Hadoop.
2. Build Cube from the identified tables.
3. Query using ANSI-SQL and get results in sub-second, through ODBC, JDBC or RESTful API.Approximately a layer for analyzing big data. It can be very fast with it. Acts as a bridge.

Unfortunately, it can only be used in a `Linux` environment currently. I'll come back to experiment later.

## MongoDB This is also a database. Give it a try and install.

In English, the given Chinese text translates to:

Try installing this, which is also a database. Cloning into '/usr/local/Homebrew/Library/Taps/mongodb/homebrew-brew'...
remote: Listing objects: 63, done.
remote: Counting objects: 100% (63/63), done.
remote: Compressing objects: 100% (62/62), done.
remote: Total 566 (delta 21), reused 6 (delta 1), pack-reused 503
Receiving objects: 100% (566/566), 121.78 KB | 335.00 KB/s, done.
Resolving deltas: 100% (259/259), done.
Tapped 11 formulae (39 files, 196.2KB).

Translation:

Cloning into '/usr/local/Homebrew/Library/Taps/mongodb/homebrew-brew'...
remote: Enumerating objects: 63, done.
remote: Counting objects: 100% (63/63), done.
remote: Compressing objects: 100% (62/62), done.
remote: Total 566 (delta 21), reused 6 (delta 1), pack-reused 503
Receiving objects: 100% (566/566), 121.78 kilobytes | 335.00 kilobytes/second, done.
Resolving deltas: 100% (259/259), done.
Tapped 11 formulae (39 files, 196.2 kilobytes). Install mongodb-community from mongodb/brew
Downloading: https://fastdl.mongodb.org/tools/db/mongodb-database-tools-macos-x86_64-100.3.0.zip
[100.0%]
Downloading: https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.4.3.tgz
[100.0%]
Installing dependencies for mongodb/brew/mongodb-community: mongodb-database-tools. Installing mongodb/brew/mongodb-community dependency: mongodb-database-tools
Error: The `brew link` step did not complete successfully.
The formula built, but is not symlinked into /usr/local.
Could not symlink bin/bsondump
Target /usr/local/bin/bsondump is a symlink belonging to mongodb. You can unlink it:
brew unlink mongodb

To force the link and overwrite all conflicting files:
brew link --overwrite mongodb-database-tools: Listing files to be overwritten:
brew link --overwrite --dry-run mongodb-database-tools

Conflicting files:
/usr/local/bin/bsondump -> /usr/local/Cellar/mongodb/3.0.7/bin/bsondump
/usr/local/bin/mongodump -> /usr/local/Cellar/mongodb/3.0.7/bin/mongodump
/usr/local/bin/mongoexport -> /usr/local/Cellar/mongodb/3.0.7/bin/mongoexport
/usr/local/bin/mongofiles -> /usr/local/Cellar/mongodb/3.0.7/bin/mongofiles
/usr/local/bin/mongoimport -> /usr/local/Cellar/mongodb/3.0.7/bin/mongoimport/usr/local/Cellar/mongodb/3.0.7/bin/mongorestore ->usrmongorestore
/usr/local/Cellar/mongodb/3.0.7/bin/mongostat ->usrmongostat
/usr/local/Cellar/mongodb/3.0.7/bin/mongotop ->usrmongotop

===
Summary
🍺  /usr/local/Cellar/mongodb-database-tools/100.3.0: 13 files, 154MB, built in 11 seconds
===
Installing mongodb/brew/mongodb-community
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/mongo
Target /usr/local/bin/mongo1. It is a symlink associated with mongodb. You can remove it:
brew unlink mongodb

2. To forcefully link it and overwrite conflicting files:
brew link --overwrite mongodb-community

3. To list all files that would be deleted (dry run):
brew link --overwrite --dry-run mongodb-community

4. Potential conflicting files:
mongodb-community_[some files] /usr/local/bin/mongo -> /usr/local/Cellar/mongodb/3.0.7/bin/mongo
/usr/local/bin/mongod -> /usr/local/Cellar/mongodb/3.0.7/bin/mongod
/usr/local/bin/mongos -> /usr/local/Cellar/mongodb/3.0.7/bin/mongos

=== Caveats ===
To have launchd start mongodb-brew-mongodb-community now and restart at login:
brew services start mongodb-brew-mongodb-community

Or, if you don't want/need a background service you can just run:
mongod --config /usr/local/etc/mongod.conf

=== Summary ===
🍺 /usr/local/Cellar/mongodb-community/4.4.3: 11 files, 156.8MB, built in 10 seconds. To start and login restart MongoDB community version using launchd:
brew services start mongodb/brew/mongodb-community

Alternatively, without a background service, run:
mongod --config /usr/local/etc/mongod.conf Previously I uninstalled an old version of MongoDB. Unlinking the links.

Unlinking /usr/local/Cellar/mongodb/3.0.7... 11 symlinks removed

MongoDB db version v4.4.3:
{
"version": "4.4.3",
"gitVersion": "913d6b62acfbb344dde1b116f4161360acd8fd13",
"modules": [],
"allocator": "system",
"environment": {
"distarch": "x86_64",
"target_arch": "x86_64"
}
}

Translation:
{
"version": "4.4.3",
"gitVersion": "913d6b62acfbb344dde1b116f4161360acd8fd13",
"modules": [],
"allocator": "system",
"environment": {
"distarch": "x86_64",
"target_arch": "x86_64"
}
} continued running `mongod` to start the MongoDB server. However, the first time it was started, it said `/data/db` did not exist. We create a directory, `~/mongodb`, here to save the database files.

```shell
$ mongod --dbpath ~/mongodb
```:
[
  {
    "t": {
      "$date": "2021-03-11T10:17:32.838+08:00"
    },
    "s": "I",
    "c": "CONTROL",
    "id": 23285,
    "ctx": "main",
    "msg": "Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"
  },
  {
    "t": {
      "$date": "2021-03-11T10:17:32.842+08:00"
    },
    "s": "W",
    "c": "ASIO",
    "id": 22601,
    "ctx": "main",
    "msg": "No TransportLayer configured during NetworkInterface startup"
  },
  {
    "t": {
      "$date": "2021-03-11T10:17:32.842+08:00"
    },
    "s": "I",
    "c": "NETWORK",
    "id": 4648602,
    "ctx": "main",
    "msg": "Implicit TCP FastOpen in use."
  },
  {
    "t": {
      "$date": "2021-03-11T10:17:32.842+08:00"
    },
    "s": "I",
    "c": "STORAGE",
    "id": 4615611,
    "ctx": "initandlisten",
    "msg": "MongoDB starting",
    "attr": {
      "pid": 46256,
      "port": 27017,
      "dbPath": "/Users/lzw/mongodb",
      "architecture": "64-bit",
      "host": "lzwjava"
    }
  },
  {
    "t": {
      "$date": "2021-03-11T10:17:32.842+08:00"
    },
    "s": "I",
    "c": "CONTROL",
    "id": 23403,
    "ctx": "initandlisten",
    "msg": "Build Info",
    "attr": {
      "buildInfo": {
        "version": "4.4.3",
        "gitVersion": "913d6b62acfbb344dde1b116f4161360acd8fd13",
        "modules": [],
        "allocator": "system",
        "environment": {
          "distarch": "x86_64",
          "target_arch": "x86_64"
        }
      }
    }
  }
] I: 2021-03-11T10:17:32.843+0000   CONTROL    initandlisten  Operating System  name: "Mac OS X" version: "20.3.0"

Open another terminal tab.

$ mongo
MongoDB shell version v4.4.3
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb Implicit session:
{ "id" : "4f55c561-70d3-4289-938d-4b90a284891f" }

MongoDB server version: 4.4.3

---

The server generated the following startup warnings:
2021-03-11 10:17:33.743+08:00 Access control is not enabled for the database. Read and write access to data and configuration is unrestricted.
2021-03-11 10:17:33.743+08:00 This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind-ip <address> to specify which IP addresses it should serve responses from, or with --bind-ip-all to bind to all interfaces. If this behavior is desired, start the server with --bind-ip 127.0.0.1 to disable this warning.
2021-03-11 10:17:33.743+08:00 Soft rlimits too low
2021-03-11 10:17:33.743+08:00 currentValue: 4864
2021-03-11 10:17:33.743+08:00 recommendedMinimum: 64000 Enable MongoDB's free cloud-based monitoring service to receive and display metrics about your deployment (disk utilization, CPU, operation statistics, etc). The monitoring data will be accessible through a unique URL on a MongoDB website, which you and anyone you share the URL with can use. MongoDB may utilize this information for product improvements and to recommend MongoDB products and deployment options.

To enable free monitoring, execute the following command: db.enableFreeMonitoring()
To permanently disable this reminder, execute the following command: db.disableFreeMonitoring()

Translation:
Enable MongoDB's free monitoring service to receive and display deployment metrics. Monitoring data accessible through a unique URL on MongoDB website. MongoDB may use info for product improvements and suggestions.

To enable: db.enableFreeMonitoring()
To disable: db.disableFreeMonitoring() continued trying to insert data, query data.

> db.inventory.insertOne(
...   { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
... )

[Object]

```English:
Continue trying to insert data, query data.

> db.inventory.insertOne(
... { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
... )

[{ "_id": <ObjectId>, "item": "canvas", "qty": 100, "tags": [ "cotton" ], "size": { "h": 28, "w": 35.5, "uom": "cm" } }]
```:
- acknowledged: true,
- insertedId: "6049ef91b653541cf355facb"

Result of db.inventory.find():
- _id: "6049ef91b653541cf355facb",
- item: "canvas",
- qty: 100,
- tags: ["cotton"],
- size: { h: 28, w: 35.5, uom: "cm" } Lastly, let's come back to this. Later, we'll move on to other tools. The significance of what we're doing is roughly to establish a framework. Starting anything is difficult, and we've gone through all of these things from the beginning. This gives us confidence, and next, we'll continue to tinker with these software.

## Practice

Practice:
Establishing a framework gives confidence, and continuing to tinker with software builds upon that foundation. Students explore similarly as shown above.
