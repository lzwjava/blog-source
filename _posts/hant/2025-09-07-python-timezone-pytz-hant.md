---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python 時區處理：使用 pytz
translated: true
type: note
---

### 安裝 pytz
pytz 是一個用於處理時區感知日期時間物件的第三方 Python 函式庫。請注意，從 Python 3.9+ 開始，建議新程式碼使用內建的 `zoneinfo` 模組（它屬於標準函式庫且能自動處理更新），但 pytz 仍然被廣泛使用。

要安裝 pytz，請使用 pip：
```
pip install pytz
```

### 使用 pytz 的基本方法
pytz 與 Python 的 `datetime` 模組協同工作。關鍵概念：
- **時區物件**：使用 `pytz.timezone()` 建立時區感知物件（例如用於「UTC」或「America/New_York」）。
- **本地化**：使用 `.localize()` 將時區附加到單純的 `datetime` 物件。
- **轉換**：使用 `.astimezone()` 在不同時區之間進行轉換。
- **注意事項**：避免直接在 `datetime` 物件上使用 `pytz` 建構函式；請先進行本地化以正確處理夏令時（DST）。

匯入所需模組：
```python
import datetime
import pytz
```

### 範例

#### 1. 取得特定時區的目前時間
使用 `pytz.utc` 或特定時區。最佳實踐是內部處理使用 UTC。

```python
# 取得目前 UTC 時間
utc_now = datetime.datetime.now(pytz.utc)
print(utc_now)  # 例如：2023-10-15 14:30:00+00:00

# 取得美國東部時間的目前時間
eastern = pytz.timezone('US/Eastern')
eastern_now = datetime.datetime.now(eastern)
print(eastern_now)  # 例如：2023-10-15 10:30:00-04:00（根據 DST 調整）
```

#### 2. 本地化單純日期時間
將單純（無時區感知）的日期時間轉換為時區感知的日期時間。

```python
# 建立一個單純日期時間（例如 2023 年 10 月 15 日 12:00）
naive_dt = datetime.datetime(2023, 10, 15, 12, 0)
print(naive_dt)  # 2023-10-15 12:00:00

# 本地化為美國東部時間
eastern = pytz.timezone('US/Eastern')
aware_dt = eastern.localize(naive_dt)
print(aware_dt)  # 2023-10-15 12:00:00-04:00
```

#### 3. 在不同時區之間轉換
先本地化日期時間，然後進行轉換。

```python
# 從 UTC 時間開始
utc_dt = pytz.utc.localize(datetime.datetime(2023, 10, 15, 14, 0))
print(utc_dt)  # 2023-10-15 14:00:00+00:00

# 轉換為太平洋時間
pacific = pytz.timezone('US/Pacific')
pacific_dt = utc_dt.astimezone(pacific)
print(pacific_dt)  # 2023-10-15 07:00:00-07:00
```

#### 4. 處理時區列表
pytz 支援 Olson 資料庫中的常用時區名稱。

```python
# 列出可用時區
print(pytz.all_timezones[:10])  # 範例：['Africa/Abidjan', 'Africa/Accra', ...]

# 或特定國家的時區
print(pytz.country_timezones['US'])  # ['America/New_York', 'America/Los_Angeles', ...]
```

### 遷移至 zoneinfo（建議用於 Python 3.9+）
對於較新的 Python 版本，建議使用內建的 `zoneinfo` 代替 pytz 以簡化操作：
```python
from zoneinfo import ZoneInfo
import datetime

# 等同於 pytz 範例
eastern_now = datetime.datetime.now(ZoneInfo('US/Eastern'))
aware_dt = datetime.datetime(2023, 10, 15, 12, 0).replace(tzinfo=ZoneInfo('US/Eastern'))
```

### 常見問題與提示
- **模糊時間**：在 DST 轉換期間，請在 `.localize()` 中使用 `is_dst`（例如 `eastern.localize(naive_dt, is_dst=False)`）。
- **UTC 標準化**：在進行算術運算前先轉換為 UTC 以避免錯誤。
- **更新 pytz**：它使用 IANA tzdata；請透過 pip 保持更新。
- 更多資訊，請查閱 [pytz 文件](https://pythonhosted.org/pytz/)。如果遇到錯誤，請貼上程式碼片段以獲得除錯協助。