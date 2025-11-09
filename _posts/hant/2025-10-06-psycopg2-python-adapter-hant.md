---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Psycopg2 PostgreSQL Python 適配器
translated: true
type: note
---

**Psycopg2** 是一個流行的開源 PostgreSQL 資料庫適配器（亦稱為驅動程式），專為 Python 程式語言設計。它能讓 Python 應用程式連接 PostgreSQL 資料庫、執行 SQL 查詢並高效處理資料。其主要功能包括：

- 完全符合 Python DB API 2.0 規範
- 支援非同步通知、伺服器端游標及 COPY 操作
- 以 C 語言編寫以提升效能，並可選用二進位支援以加速資料傳輸
- 廣泛應用於生產環境，適用於網頁開發、資料分析及 ETL 流程等任務

此為 psycopg 函式庫的第二代產品（故名為 "2"），雖然 psycopg3 是較新版本，但 psycopg2 仍為保持穩定且持續維護的版本，以確保舊版相容性。

安裝時可使用 `pip install psycopg2-binary`（二進位版本更適合初學者使用）。

[Psycopg 官方文件](https://www.psycopg.org/docs/)  
[GeeksforGeeks 介紹](https://www.geeksforgeeks.org/python/introduction-to-psycopg2-module-in-python/)  
[PyPI 套件頁面](https://pypi.org/project/psycopg2/)