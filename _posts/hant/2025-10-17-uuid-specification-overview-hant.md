---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: RFC 4122 UUID 規範概述
translated: true
type: note
---

RFC 4122 是由網際網路工程任務組（IETF）於 2005 年 7 月發布的技術規範。該文件定義了用於通用唯一識別碼（UUID，亦稱為全域唯一識別碼 GUID）的統一資源名稱（URN）命名空間。

UUID 是一種 128 位元的數字，用於在電腦系統中唯一識別資訊，且無需中央管理機構來管理這些識別碼。此標準闡明了五種 UUID 版本（例如基於時間戳記和 MAC 位址的版本 1、基於隨機位元的版本 4）、其生成方法、編碼格式（常見的帶連字號十六進位字串格式：`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`），以及在協定和應用程式中的使用指南。這確保了不同系統與網路之間的互通性。

該規範已被軟體開發領域廣泛採用，適用於資料庫金鑰、工作階段 ID 和分散式系統等任務。

[ RFC 4122 - 通用唯一識別碼 (UUID) URN 命名空間](https://datatracker.ietf.org/doc/html/rfc4122)  
[ 通用唯一識別碼 - 維基百科](https://en.wikipedia.org/wiki/Universally_unique_identifier)