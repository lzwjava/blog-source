---
audio: false
generated: true
lang: hant
layout: post
title: 在 JavaScript 中使用 Moment.js
translated: true
type: note
---

我將示範如何在 JavaScript 中使用 `moment` 和 `moment-timezone` 函式庫。這些是處理日期和時間的熱門函式庫。

1. 首先，若尚未安裝套件，請先安裝：
```bash
npm install moment moment-timezone
```

2. 基本使用範例：

```javascript
// 匯入函式庫
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// 基礎 Moment.js 用法
// 當前日期與時間
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // 例如："2025-03-03 14:30:45"

// 解析特定日期
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// 操作日期
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // 例如："Tue, Mar 4"

// 使用 Moment-Timezone
// 取得特定時區的時間
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // 包含時區縮寫

// 轉換不同時區的時間
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`本地時間: ${localTime.format('HH:mm')}`);
console.log(`東京時間: ${tokyoTime.format('HH:mm')}`);

// 列出所有可用時區
const timezones = momentTimezone.tz.names();
console.log(timezones); // 時區名稱陣列
```

常用格式選項：
- `YYYY`：4位數年份 (2025)
- `MM`：2位數月份 (03)
- `DD`：2位數日期 (03)
- `HH`：24小時制 (14)
- `hh`：12小時制 (02)
- `mm`：分鐘 (30)
- `ss`：秒鐘 (45)
- `z`：時區縮寫

實用方法：
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
momentTimezone.tz.guess(); // 猜測使用者時區
```

注意事項：
1. 這些版本 (^2.14.1 和 ^0.5.7) 相當舊（約 2016 年發布）。除非有特定相容性需求，建議考慮使用最新版本。
2. Moment.js 現已被視為維護模式的遺留專案。對於新專案，建議考慮替代方案如 `date-fns` 或 `luxon`。