---
lang: hant
layout: post
title: Redis入门指南
---

打开Redis官网，首先映入眼帘的是一句介绍：Redis是一种开源的内存数据结构存储系统，广泛用于数据库和缓存场景。`Redis`确实非常常用。

## 安装 Redis

可前往官网安装`Redis`。与`SQLite`类似，安装完成后，如何在`Python`中使用`Redis`呢？

```shell
pip install redis
```

```shell
>>> import redis
>>> r = redis.Redis(host='localhost', port=6379, db=0)
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
b'bar'
```

Python文档提供了一些示例。在这些示例中，出现了类似`pip`的工具。`pip`是一个包管理工具。关于包管理工具的具体含义，可以参考「熟悉编程环境」这一章节进行了解。`pip`对于`Python`来说，就如同`Homebrew`对于`macOS`系统一样重要。

`pip`通常在安装`Python`时已经自带了。如果电脑上有很多版本的`Python`和`Pip`，可以在`~/.bash_profile`中加入以下两行：

```shell
alias python=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
alias pip=/usr/local/Cellar/python@3.9/3.9.1_6/bin/pip3
```

意思是指定一個版本的`python`和`pip`。一種方式是使用`Homebrew`來安裝。也可以從源代碼構建安裝。

```shell
make
make test
make install
```

翻譯為：

```shell
編譯
測試
安裝
```

```shell
$ redis-server
87684:C 2021年3月10日 14:46:06.056 # oO0OoO0OoO0Oo Redis 正在啟動 oO0OoO0OoO0Oo
87684:C 2021年3月10日 14:46:06.056 # Redis 版本=6.2.1, 位數=64, 提交=00000000, 修改=0, 進程ID=87684, 剛剛啟動
87684:C 2021年3月10日 14:46:06.056 # 警告：未指定配置文件，使用默認配置。若要指定配置文件，請使用 redis-server /路徑/到/redis.conf
87684:M 2021年3月10日 14:46:06.057 * 已將最大打開文件數增加到10032（原設置為4864）。
87684:M 2021年3月10日 14:46:06.057 * 單調時鐘：POSIX clock_gettime
...
Redis 6.2.1 (00000000/0) 64 位
...
87684:M 2021年3月10日 14:46:06.058 # 服務器已初始化
87684:M 2021年3月10日 14:46:06.058 * 準備接受連接
```

這裡節選了一點內容。可見我們已經安裝上了。版本號`6.2.1`，是官網最新的。打開另外一個終端窗口。可以試著把玩一下：
```shell
$ redis-cli
127.0.0.1:6379> set a 2
OK
127.0.0.1:6379> get a
"2"
```

運行一下代碼。

```python
import redis
```

```python
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))
```

輸出：

```shell
$ python fib_redis.py
b'bar'
```

## Redis 缓存示例

要实现斐波那契数列的`Redis`版本，我们可以利用`Redis`的缓存功能来存储已经计算过的斐波那契数，从而避免重复计算。以下是一个简单的实现思路：

1. **定义斐波那契数列**：斐波那契数列是一个递归定义的数列，其中每个数是前两个数的和。数列的前两个数通常是0和1。

2. **使用Redis缓存**：我们将使用`Redis`来存储已经计算过的斐波那契数。这样，当我们需要计算某个位置的斐波那契数时，可以先检查`Redis`中是否已经存在该值。如果存在，则直接返回；如果不存在，则进行计算并将结果存入`Redis`。

3. **实现代码**：以下是一个使用Python和`Redis`实现斐波那契数列的示例代码。

```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def fibonacci(n):
    # 检查Redis中是否已经存在该斐波那契数
    if r.exists(str(n)):
        return int(r.get(str(n)))
    
    # 基本情况
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # 递归计算斐波那契数
    fib_value = fibonacci(n-1) + fibonacci(n-2)
    
    # 将计算结果存入Redis
    r.set(str(n), fib_value)
    
    return fib_value

# 示例：计算第10个斐波那契数
n = 10
print(f"Fibonacci({n}) = {fibonacci(n)}")
```

### 代码说明：
- **连接到Redis**：我们使用`redis.Redis`来连接到本地的`Redis`服务器。
- **fibonacci函数**：这个函数计算第`n`个斐波那契数。首先检查`Redis`中是否已经存在该值，如果存在则直接返回；否则，递归计算并将结果存入`Redis`。
- **示例**：我们计算第10个斐波那契数并打印结果。

### 运行结果：
运行上述代码后，输出将是：
```
Fibonacci(10) = 55
```

### 注意事项：
- 确保`Redis`服务器正在运行，并且Python环境中安装了`redis`库（可以通过`pip install redis`安装）。
- 这个实现利用了递归和缓存，适合计算较小的斐波那契数。对于非常大的`n`，递归可能会导致栈溢出，可以考虑使用迭代或其他优化方法。

通过这种方式，我们可以利用`Redis`的缓存功能来加速斐波那契数列的计算。

```python
import redis
```

r = redis.Redis(host='localhost', port=6379, db=0)

def f(n):
    nr = r.get(n)
    if nr is not None:
        return int(nr)
    res_n = 0
    if n < 2:
        res_n = n
    else:
        res_n = f(n-1) + f(n-2)
    
    r.set(n, res_n)
    return res_n

```python
print(f(10))
```

這樣就搞定了。