---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python 日期時間模組概覽
translated: true
type: note
---

### Python datetime 模組概述

Python 的 `datetime` 模組提供了處理日期、時間和時間戳的類別。它屬於標準函式庫，無需額外安裝。主要類別包括：
- `date`：處理日期（年、月、日）。
- `time`：處理時間（時、分、秒、微秒）。
- `datetime`：結合日期與時間。
- `timedelta`：表示時間間隔（例如用於日期運算）。

此模組適用於記錄時間戳、計算持續時間，或格式化日期以供顯示/輸出等任務。

### 導入模組

可根據需求導入整個模組或特定類別：

```python
import datetime  # 完整模組

# 或導入特定類別
from datetime import datetime, date, time, timedelta
```

### 取得當前日期與時間

使用 `datetime.now()` 可取得當前本地日期與時間作為 `datetime` 物件。

```python
import datetime

now = datetime.datetime.now()
print(now)  # 輸出範例：2023-10-05 14:30:45.123456
print(type(now))  # <class 'datetime.datetime'>
```

若要取得 UTC 時間，可使用 `datetime.utcnow()`（但建議使用 `datetime.now(timezone.utc)` 並從 `datetime.timezone` 導入以支援時區感知）。

### 建立日期與時間物件

透過建構子手動建立物件。

```python
# 日期：年、月、日
d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05

# 時間：時、分、秒、微秒（可選）
t = datetime.time(14, 30, 45)
print(t)  # 14:30:45

# 日期時間：結合日期與時間
dt = datetime.datetime(2023, 10, 5, 14, 30, 45)
print(dt)  # 2023-10-05 14:30:45
```

可省略不需要的部分（例如 `datetime.datetime(2023, 10, 5)` 會建立午夜時分的 datetime 物件）。

### 日期格式化（strftime）

使用帶有格式代碼的 `strftime` 將日期轉換為字串（例如 `%Y` 表示年，`%m` 表示月）。

```python
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 範例：2023-10-05 14:30:45

# 常用格式：
# %A：完整星期名稱（例如 Thursday）
# %B：完整月份名稱（例如 October）
# %Y-%m-%d：ISO 日期格式
```

### 從字串解析日期（strptime）

使用帶有匹配格式的 `strptime` 將字串轉換為 `datetime` 物件。

```python
date_str = "2023-10-05 14:30:45"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2023-10-05 14:30:45
print(type(parsed))  # <class 'datetime.datetime'>
```

格式必須完全匹配，否則會引發 `ValueError`。

### 使用 timedelta 進行日期運算

使用 `timedelta` 加減時間間隔。

```python
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)  # 當前日期 + 1 天

# 減法運算
yesterday = now - one_day

# 可設定單位：天、秒、微秒、毫秒、分鐘、小時、週
one_week = datetime.timedelta(weeks=1)
```

計算日期差異：

```python
date1 = datetime.datetime(2023, 10, 5)
date2 = datetime.datetime(2023, 10, 10)
delta = date2 - date1
print(delta.days)  # 5
```

### 時區處理（進階用法）

若要進行時區感知操作，請使用 `timezone`（Python 3.3+）。此模組本身不處理時區轉換，建議搭配 `pytz` 函式庫進行完整處理。

```python
from datetime import datetime, timezone

# 單純 datetime（無時區資訊）
naive = datetime.now()

# UTC 時區感知
utc = datetime.now(timezone.utc)

# 自訂時區（需 tzinfo）
import pytz  # 可能需要 pip install pytz
eastern = pytz.timezone("US/Eastern")
eastern_time = naive.astimezone(eastern)
```

### 常見技巧與注意事項
- **不可變物件**：`datetime` 物件無法直接修改，運算會建立新物件。
- **月份天數**：閏年二月可使用 29 日；模組會透過 `calendar` 或 `dateutil` 處理閏年檢查。
- **效能**：避免在迴圈中頻繁呼叫 `now()`，建議儲存數值。
- **錯誤處理**：注意無效日期（例如 `date(2023, 2, 30)` 會引發 `ValueError`）。
- **擴充函式庫**：進階解析可考慮使用 `dateutil` 或 `arrow` 套件。

完整文件請參閱 Python 官方文件 [docs.python.org](https://docs.python.org/3/library/datetime.html)。建議在 Python 直譯器中練習這些範例。