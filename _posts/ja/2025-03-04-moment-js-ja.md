---
audio: false
generated: true
lang: ja
layout: post
title: Moment.jsをJavaScriptで使用する
translated: true
---

`moment` と `moment-timezone` ライブラリを JavaScript で使う方法を教えます。これらは、日付と時刻を扱うための人気のあるライブラリです。

1. まだインストールしていない場合は、まずパッケージをインストールします：
```bash
npm install moment moment-timezone
```

2. 基本的な使用例：

```javascript
// ライブラリをインポート
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// 基本的な Moment.js の使用
// 現在の日付と時刻
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // 例: "2025-03-03 14:30:45"

// 特定の日付を解析
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// 日付を操作
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // 例: "Tue, Mar 4"

// Moment-Timezone を使用
// 特定のタイムゾーンの時刻を取得
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // タイムゾーンの略称を含む

// タイムゾーン間の時刻を変換
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// 利用可能なすべてのタイムゾーンをリスト表示
const timezones = momentTimezone.tz.names();
console.log(timezones); // タイムゾーン名の配列
```

一般的なフォーマットオプション：
- `YYYY`: 4桁の年 (2025)
- `MM`: 2桁の月 (03)
- `DD`: 2桁の日 (03)
- `HH`: 24時間 (14)
- `hh`: 12時間 (02)
- `mm`: 分 (30)
- `ss`: 秒 (45)
- `z`: タイムゾーンの略称

便利なメソッド：
```javascript
// 日付操作
moment().add(7, 'days');     // 時間を追加
moment().subtract(2, 'hours'); // 時間を減算
moment().startOf('month');   // 期間の開始
moment().endOf('month');     // 期間の終了

// 日付比較
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// タイムゾーン操作
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // ユーザーのタイムゾーンを推測
```

注意点：
1. これらのバージョン（^2.14.1 と ^0.5.7）はかなり古い（2016年頃のもの）です。特定の互換性要件がない限り、最新バージョンを使用することを検討してください。
2. Moment.js は現在、メンテナンスモードの遺産プロジェクトとされています。新しいプロジェクトでは、`date-fns` や `luxon` のような代替手段を検討することをお勧めします。