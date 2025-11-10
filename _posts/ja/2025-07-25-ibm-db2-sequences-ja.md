---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: IBM DB2 シーケンス使用ガイド
translated: true
type: note
---

### IBM DB2 シーケンスの NEXT VALUE FOR の使用方法

IBM DB2 において、`NEXT VALUE FOR` はシーケンスから次の値を取得するために使用されます。シーケンスは一意で連続して増加する数値を生成します。シーケンスは主キーやその他の一意の識別子を生成するのに便利です。

#### 例: シーケンスの作成と使用
1. **シーケンスを作成する** (DB2 環境で一度実行):
   ```sql
   CREATE SEQUENCE my_sequence
   START WITH 1
   INCREMENT BY 1
   NO CYCLE;
   ```
   - これにより、1から始まり、毎回1ずつ増分する `my_sequence` という名前のシーケンスが作成されます。

2. **INSERT 文でシーケンスを使用して** 次の値を取得する:
   ```sql
   INSERT INTO employees (id, name, department)
   VALUES (NEXT VALUE FOR my_sequence, 'Alice Johnson', 'Engineering');
   ```
   - これにより、`id` に次のシーケンス値（例えば、最初の使用では1、次は2など）が設定された新しい行が挿入されます。

#### 主な注意点
- SELECT クエリでも使用できます: `SELECT NEXT VALUE FOR my_sequence FROM SYSIBM.SYSDUMMY1;`
- シーケンスはテーブルとは別個のものであり、必要に応じて複数のテーブル間で共有できます。
- 詳細については、IBM DB2 のシーケンスに関するドキュメントを参照してください。`PREVIOUS VALUE FOR` のような他のシーケンス関数の例が必要な場合は、お知らせください！