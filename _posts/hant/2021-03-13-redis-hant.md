---
audio: false
generated: false
image: false
lang: hant
layout: post
title: Redis入門
translated: true
type: post
---

打開Redis官網，第一句話是說，Redis是一種開源的內存型的數據結構存儲，常用於數據庫和緩存。`Redis`很常用。

## 安裝 Redis

可到官網安裝`Redis`。就像`SQLite`一樣。安裝完畢後，那如何在`Python`使用`Redis`呢。

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

Python文檔給了一些例子。這裡出現了像`pip`的東西。`pip`是包管理工具。包管理工具是什麼，可到「熟悉編程環境」一章查閱。`pip`之於`python`，就好像`Homebrew`之於`macOS`系統。

`pip`通常在安裝`python`時已經自帶了。如果電腦有很多版本的`Python`和 `Pip`，可以在`~/.bash_profile`中加入以下兩行：

```shell
alias python=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
alias pip=/usr/local/Cellar/python@3.9/3.9.1_6/bin/pip3
```

意思是指定一個版本的`python`和 `pip`。一種方式是可以`Homebrew`來安裝。也可以從源代碼構建安裝。

```shell
make
make test
make install
```

```shell
$ redis-server
87684:C 10 Mar 2021 14:46:06.056 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
87684:C 10 Mar 2021 14:46:06.056 # Redis version=6.2.1, bits=64, commit=00000000, modified=0, pid=87684, just started
87684:C 10 Mar 2021 14:46:06.056 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
87684:M 10 Mar 2021 14:46:06.057 * Increased maximum number of open files to 10032 (it was originally set to 4864).
87684:M 10 Mar 2021 14:46:06.057 * monotonic clock: POSIX clock_gettime
...
Redis 6.2.1 (00000000/0) 64 bit
...
87684:M 10 Mar 2021 14:46:06.058 # Server initialized
87684:M 10 Mar 2021 14:46:06.058 * Ready to accept connections
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

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))
```

輸出：

```shell
$ python fib_redis.py
b'bar'
```

## Redis 緩存例子

來實現斐波那契數列`Redis`版本。

```python
import redis

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

print(f(10))
```

這樣就搞定啦。