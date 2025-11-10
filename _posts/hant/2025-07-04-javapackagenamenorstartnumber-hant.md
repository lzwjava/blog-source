---
audio: false
generated: true
lang: hant
layout: post
title: Java 套件名稱不能以數字開頭
translated: true
type: note
---

在 Java 中，套件名稱**不能以數字開頭**。根據 Java 命名慣例與 Java 語言規範：

- 套件名稱必須是有效的識別符
- 有效的 Java 識別符必須以字母（A-Z 或 a-z）、底線（`_`）或美元符號（`$`）開頭
- 數字（0-9）允許出現在識別符中，但僅能位於**首字元之後**

例如：
- 有效的套件名稱：`com.example`、`my_package`、`a123`
- 無效的套件名稱：`123example`、`1package`

若嘗試使用數字開頭的套件名稱，Java 編譯器將會拋出語法錯誤。解決方法包括：
- 以字母或底線開頭命名套件，例如：`a123.example` 或 `_123.example`
- 採用符合慣例的描述性名稱，例如：`com.example.project123`

此規則確保 Java 命名系統的一致性和相容性。