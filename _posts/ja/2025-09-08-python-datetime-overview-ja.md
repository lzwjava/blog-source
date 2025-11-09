---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: PythonのDatetimeモジュール概要
translated: true
type: note
---

### Pythonのdatetimeモジュール概要

Pythonの`datetime`モジュールは、日付、時刻、タイムスタンプを操作するためのクラスを提供します。標準ライブラリに含まれるため、インストールは不要です。主なクラスは以下の通りです：
- `date`: 日付（年、月、日）を扱います
- `time`: 時刻（時、分、秒、マイクロ秒）を扱います
- `datetime`: 日付と時刻を組み合わせます
- `timedelta`: 期間を表します（日付演算などに使用）

ログのタイムスタンプ記録、期間の計算、表示/出力用の日付フォーマットなどのタスクに有用です。

### モジュールのインポート

必要に応じてモジュール全体または特定のクラスをインポートします：

```python
import datetime  # モジュール全体

# または特定のクラスをインポート
from datetime import datetime, date, time, timedelta
```

### 現在の日付と時刻の取得

`datetime.now()`を使用して、現在のローカル日付と時刻を`datetime`オブジェクトとして取得します。

```python
import datetime

now = datetime.datetime.now()
print(now)  # 出力例: 2023-10-05 14:30:45.123456
print(type(now))  # <class 'datetime.datetime'>
```

UTC時間の場合は、`datetime.utcnow()`を使用します（ただし、タイムゾーンを考慮する場合は`datetime.timezone`からのインポートを使用した`datetime.now(timezone.utc)`が推奨されます）。

### 日付と時刻オブジェクトの作成

コンストラクタを使用して手動でオブジェクトを作成します。

```python
# 日付: 年、月、日
d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05

# 時刻: 時、分、秒、マイクロ秒（オプション）
t = datetime.time(14, 30, 45)
print(t)  # 14:30:45

# 日時: 日付と時刻を組み合わせる
dt = datetime.datetime(2023, 10, 5, 14, 30, 45)
print(dt)  # 2023-10-05 14:30:45
```

不要な部分は省略できます（例：`datetime.datetime(2023, 10, 5)`は深夜の日時を作成します）。

### 日付のフォーマット（strftime）

フォーマットコード（例：`%Y`は年、`%m`は月）を使用した`strftime`で日付を文字列に変換します。

```python
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 例: 2023-10-05 14:30:45

# 一般的なフォーマット:
# %A: 完全な曜日名（例: Thursday）
# %B: 完全な月名（例: October）
# %Y-%m-%d: ISO日付形式
```

### 文字列からの日付解析（strptime）

一致するフォーマットを使用した`strptime`で文字列を`datetime`オブジェクトに変換します。

```python
date_str = "2023-10-05 14:30:45"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2023-10-05 14:30:45
print(type(parsed))  # <class 'datetime.datetime'>
```

フォーマットが正確に一致しない場合、`ValueError`が発生します。

### timedeltaを使用した日付演算

`timedelta`を使用して時間間隔を加算または減算します。

```python
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)  # 現在の日付 + 1日

# 減算
yesterday = now - one_day

# 指定可能な単位: days, seconds, microseconds, milliseconds, minutes, hours, weeks
one_week = datetime.timedelta(weeks=1)
```

日付間の差を計算する場合：

```python
date1 = datetime.datetime(2023, 10, 5)
date2 = datetime.datetime(2023, 10, 10)
delta = date2 - date1
print(delta.days)  # 5
```

### タイムゾーン（高度な使用法）

タイムゾーンを考慮した操作には、`timezone`（Python 3.3以降）を使用します。このモジュールはタイムゾーン変換をネイティブに扱わないため、堅牢な処理には`pytz`ライブラリとの併用が推奨されます。

```python
from datetime import datetime, timezone

# ナイーブな日時（タイムゾーンなし）
naive = datetime.now()

# UTC対応
utc = datetime.now(timezone.utc)

# カスタムタイムゾーン（tzinfoが必要）
import pytz  # pip install pytzが必要な場合あり
eastern = pytz.timezone("US/Eastern")
eastern_time = naive.astimezone(eastern)
```

### 一般的なヒントと注意点
- **不変オブジェクト**: `datetime`オブジェクトは直接変更できません。演算では新しいオブジェクトが作成されます
- **月の日数**: 閏年の2月には29日を使用します。モジュールは`calendar`または`dateutil`を使用して閏年チェックを処理します
- **パフォーマンス**: ループ内での頻繁な`now()`呼び出しは避け、値を保存してください
- **エラー**: 無効な日付（例：`date(2023, 2, 30)`）には`ValueError`が発生します
- **ライブラリ拡張**: 高度な解析には`dateutil`や`arrow`パッケージの使用を検討してください

完全なドキュメントは、Pythonの公式ドキュメント[docs.python.org](https://docs.python.org/3/library/datetime.html)で確認してください。これらの例をPythonインタープリターで実践してみてください。