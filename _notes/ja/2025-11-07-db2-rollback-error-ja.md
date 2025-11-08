---
audio: false
generated: true
image: false
lang: ja
layout: post
model: moonshotai/kimi-k2-thinking
title: DB2トランザクションのロールバックとエラー検出
translated: true
type: note
---

## システムエラーによるDB2のロールバック発生時

IBM DB2は、データの整合性を脅かす重大なシステムエラーが発生した場合、自動的にトランザクションをロールバックします。一般的なシナリオは以下の通りです：

- **デッドロックまたはタイムアウト**：SQLCODE -911、SQLSTATE 40001、理由コード「2」はデッドロックによるトランザクションのロールバックを示します
- **プロセス異常終了**：すべてのDB2環境において、プロセス終了は暗黙的なロールバックを引き起こします
- **システムリソース障害**：トランザクションの完了を妨げるメモリ、ディスク、またはネットワークの障害
- **タイムスタンプ競合**：モジュールとDBRM間の内部タイムスタンプが一致しない場合にSQLCODE -818が発生します
- **コネクションプーリングの安全策**：一部の実装では、未コミットのトランザクションがロック問題を引き起こすのを防ぐため、コネクション解放時に自動的にロールバックします

## 詳細なエラー情報の検出方法

### 1. 主要なエラー検出メカニズム

**SQLCODEとSQLSTATE**
各SQLステートメントの実行後、DB2はこれらの変数を設定します：

```sql
-- ステートメント実行直後にチェック
IF SQLCODE < 0 THEN
    -- エラー発生
    ROLLBACK;
END IF;
```

SQLSTATEクラスコードは特にエラータイプを識別します：
- **クラス58**：システムエラー（例：リソース利用不可、オペレータ介入）
- **クラス40**：トランザクションロールバック
- **クラス25**：無効なトランザクション状態

**GET DIAGNOSTICSステートメント**
SQL PLストアドプロシージャでの詳細なエラー情報取得：

```sql
DECLARE v_sqlcode INTEGER;
DECLARE v_sqlstate CHAR(5);
DECLARE v_sqlmessage VARCHAR(256);

GET DIAGNOSTICS CONDITION 1
    v_sqlcode = DB2_RETURNED_SQLCODE,
    v_sqlstate = RETURNED_SQLSTATE,
    v_sqlmessage = MESSAGE_TEXT;
```

### 2. コマンドラインでのエラー検出

`db2`コマンドライン経由でスクリプトを実行する場合、終了コードを確認します：

- **終了コード8**：システムエラー
- **終了コード4**：DB2エラー（制約違反、オブジェクト未検出）
- **終了コード2**：DB2警告
- **終了コード1**：行未検出

**推奨スクリプトパターン**：
```bash
db2 -l migration.log +c -stf migration.sql
if [ $? -ge 4 ]; then
    db2 rollback
    tail -10 migration.log  # 詳細なエラーを確認
else
    db2 commit
fi
```

### 3. ストアドプロシージャのエラーハンドリング

SQL PLでの包括的なエラー検出には、宣言されたハンドラを使用します：

```sql
CREATE PROCEDURE my_procedure()
BEGIN
    DECLARE v_sqlcode INTEGER DEFAULT 0;
    DECLARE v_sqlstate CHAR(5) DEFAULT '00000';
    DECLARE v_error_message VARCHAR(256);
    
    -- 例外に対する終了ハンドラの宣言
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            v_sqlcode = DB2_RETURNED_SQLCODE,
            v_sqlstate = RETURNED_SQLSTATE,
            v_error_message = MESSAGE_TEXT;
            
        -- テーブルまたはファイルへのエラー詳細の記録
        INSERT INTO error_log (sqlcode, sqlstate, message, timestamp)
        VALUES (v_sqlcode, v_sqlstate, v_error_message, CURRENT_TIMESTAMP);
        
        ROLLBACK;
    END;
    
    -- トランザクションロジックをここに記述
    UPDATE employee SET salary = salary + 1000 WHERE job = 'MANAGER';
    INSERT INTO audit_log VALUES (CURRENT_TIMESTAMP, 'Salary update');
    
    COMMIT;
END
```

### 4. DB2診断ログファイル

システムレベルのエラーについては、常に以下を確認してください：

- **db2diag.log**：詳細なシステムエラー情報を含む主要な診断ログ
- **通知ログ**：エラー要約を含む
- **コマンドラインログ**：`-l logfile.txt`オプションを使用してエラーを記録

## エラー検出のベストプラクティス

1. **重要な操作の直後に常にSQLCODE/SQLSTATEをチェック**する
2. ストアドプロシージャでは**GET DIAGNOSTICSを使用**して豊富なエラーコンテキストを取得する
3. **トランザクションロールバック率の監視を実装** - 1%を超える場合は調査が必要
4. スクリプト実行のための**コマンドオプションを有効化**：
   ```bash
   db2 +c -s -v -l error.log -f script.sql
   ```
   ここで`+c`は自動コミットを無効にし、`-s`はエラー時に停止します
5. 複雑なトランザクション内での部分的なロールバックに**セーブポイントを使用**する
6. ロールバック前に**エラー詳細を永続的なテーブルに記録**し、診断情報を保持する

## 監視すべき主要なシステムエラーSQLSTATE

| SQLSTATE | 説明 | アクション |
|----------|-------------|--------|
| **58004** | システムエラー（様々な原因） | 直ちにdb2diag.logを確認 |
| **58008** | 通信エラー | ネットワーク/接続を確認 |
| **HY000** | 一般的なドライバエラー | ODBC/JDBCドライバログを確認 |
| **40001** | デッドロック/タイムアウト | バックオフ付きでトランザクションを再試行 |

本番環境では、監視ツールが**SQLCODE < 0**および**クラス58 SQLSTATE**に対してアラートを生成し、システムレベルの問題が連鎖する前に事前に検出する必要があります。