---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Moment.js 於 JavaScript
translated: true
---

我會教你如何在 JavaScript 中使用 `moment` 和 `moment-timezone` 圖書館。這些是處理日期和時間的流行圖書館。

1. 首先，如果你還沒有安裝這些套件，請安裝：
```bash
npm install moment moment-timezone
```

2. 基本使用範例：

```javascript
// 導入圖書館
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// 基本 Moment.js 使用
// 當前日期和時間
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // 例如，"2025-03-03 14:30:45"

// 解析特定日期
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// 操作日期
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // 例如，"Tue, Mar 4"

// 使用 Moment-Timezone
// 獲取特定時區的時間
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // 包括時區縮寫

// 將時間轉換為不同時區
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// 列出所有可用的時區
const timezones = momentTimezone.tz.names();
console.log(timezones); // 時區名稱的陣列
```

常見的格式選項：
- `YYYY`：4位數年份（2025）
- `MM`：2位數月份（03）
- `DD`：2位數日期（03）
- `HH`：24小時制（14）
- `hh`：12小時制（02）
- `mm`：分鐘（30）
- `ss`：秒數（45）
- `z`：時區縮寫

有用的方法：
```javascript
// 日期操作
moment().add(7, 'days');     // 增加時間
moment().subtract(2, 'hours'); // 減少時間
moment().startOf('month');   // 期間開始
moment().endOf('month');     // 期間結束

// 日期比較
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// 時區操作
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // 猜測用戶的時區
```

注意事項：
1. 這些版本（^2.14.1 和 ^0.5.7）已經相當舊（約2016年）。除非你有特定的兼容性需求，否則考慮使用最新版本。
2. Moment.js 現在被認為是一個維護模式的傳統項目。對於新項目，你可能想考慮使用替代方案，如 `date-fns` 或 `luxon`。