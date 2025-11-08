---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: IBM WebSphere wsadminツール概要
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) における wsadmin の概要

`wsadmin` ツールは、WebSphere Application Server を管理するためのコマンドラインスクリプトインターフェースです。サーバーの管理、アプリケーションのデプロイ、リソースの設定、ランタイム操作の監視などのタスクを自動化できます。スクリプトは Jython (Python ベース) または JACL (Tcl ベース) で記述でき、可読性の高さから Jython がより一般的に使用されています。

- **`wsadmin.bat`**: Windows システムで使用されます。
- **`wsadmin.sh`**: Unix/Linux/AIX システムで使用されます。

両ツールは、WebSphere プロファイルの `bin` ディレクトリ (例: `<WAS_HOME>/profiles/<ProfileName>/bin/`) またはベースインストール先 (`<WAS_HOME>/bin/`) にあります。正しい環境を確保するために、プロファイルの `bin` ディレクトリから実行することが推奨されます。

#### 対話的な wsadmin の起動
これは、コマンドを直接入力できるシェルを起動します。

**構文:**
```
wsadmin[.bat|.sh] [オプション]
```

**基本的な例 (Windows):**
```
cd C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin
wsadmin.bat -lang jython -user admin -password mypass
```

**基本的な例 (Unix/Linux):**
```
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
./wsadmin.sh -lang jython -user admin -password mypass
```

- `-lang jython`: Jython を指定します (JACL の場合は `-lang jacl` を使用)。
- `-user` と `-password`: グローバルセキュリティが有効な場合に必要です (無効な場合は省略可能)。
- 省略した場合、デフォルトの SOAP コネクタ (ポート 8879) または RMI (ポート 2809) を使用してローカルサーバーに接続します。

wsadmin プロンプト (例: `wsadmin>`) が表示されたら、スクリプトオブジェクトを使用してコマンドを実行できます:
- **AdminConfig**: 設定変更用 (例: リソースの作成)。
- **AdminControl**: ランタイム操作用 (例: サーバーの起動/停止)。
- **AdminApp**: アプリケーションのデプロイ/更新用。
- **AdminTask**: 高レベルタスク用 (例: ノードの同期)。
- **Help**: 組み込みヘルプ用 (例: `Help.help()`)。

**シェル内でのコマンド例:**
- すべてのサーバーをリスト: `print AdminConfig.list('Server')`
- サーバーを起動: `AdminControl.invoke(AdminControl.completeObjectName('type=ServerIndex,process=server1,*'), 'start')`
- 変更を保存: `AdminConfig.save()`
- 終了: `quit`

#### スクリプトファイルの実行
`-f` オプションを使用して、Jython (.py または .jy) または JACL (.jacl) スクリプトを非対話的に実行します。

**スクリプト例 (deployApp.py):**
```python
# 接続とアプリケーションのデプロイ
appName = 'MyApp'
AdminApp.install('/path/to/MyApp.ear', '[-appname ' + appName + ']')
AdminConfig.save()
print 'Application ' + appName + ' deployed successfully.'
```

**Windows での実行:**
```
wsadmin.bat -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

**Unix/Linux での実行:**
```
./wsadmin.sh -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

#### 単一コマンドの実行
`-c` オプションを使用して、単発のコマンドを実行します (バッチファイルや自動化に便利)。

**例 (Windows バッチファイルの抜粋):**
```batch
@echo off
call "C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin\wsadmin.bat" -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

**例 (Unix シェルスクリプトの抜粋):**
```bash
#!/bin/bash
./wsadmin.sh -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

#### 主なオプション

| オプション | 説明 | 例 |
|--------|-------------|---------|
| `-conntype` | コネクタタイプ: `SOAP` (デフォルト、ポート 8879) または `RMI` (ポート 2809)。 | `-conntype RMI` |
| `-host` | 接続先のリモートホスト。 | `-host myhost.example.com` |
| `-port` | コネクタポート。 | `-port 8879` |
| `-tracefile` | 出力をファイルにログ記録。 | `-tracefile wsadmin.log` |
| `-profile` | メインスクリプトの前にプロファイルスクリプトを実行。 | `-profile init.py` |
| `-c` | 単一コマンドを実行 (非対話的)。 | `-c "AdminConfig.save()"` |
| `-f` | スクリプトファイルを実行。 | `-f myscript.py` |
| `-job` | ジョブマネージャーコマンドを実行。 | `-job deploy.xml` |

#### ヒントとベストプラクティス
- **セキュリティ**: グローバルセキュリティがオフの場合は、`-user` と `-password` を省略してください。安全な設定では、暗号化された資格情報またはキーファイルを使用します。
- **シンクライアントモード**: 完全な WAS インストールなしでリモート管理を行うには、シンクライアント JAR (例: `com.ibm.ws.admin.client_*.jar`) と共に `wsadmin -conntype NONE` を使用します。
- **パフォーマンス**: 複数のコマンドを実行する場合、JVM のオーバーヘッドを避けるために、繰り返し `-c` を呼び出す代わりに単一の `-f` スクリプトを使用します。
- **エラーハンドリング**: 設定変更後は常に `AdminConfig.save()` を呼び出してください。堅牢性のために Jython で try-except を使用します。
- **コマンドの生成**: WAS 管理コンソールでアクションを実行し、「最後のアクションに対する管理スクリプトコマンドを表示」をクリックすると、同等の wsadmin コマンドを取得できます。
- **バージョンに関する注意**: 動作は WAS 8.5+ および 9.0+ で一貫していますが、バージョン固有の詳細 (例: 新しいバージョンでの Jython 2.7) については IBM のドキュメントを確認してください。

より高度な使用法については、`AdminTask.importFile('path/to/file')` のような簡略化されたコマンドのために AdminTask オブジェクトを探求してください。

### 参考文献
- [wsadmin スクリプトツール - IBM Docs](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-wsadmin-tool)
- [wsadmin スクリプトの概要 - IBM Docs](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/txml_script.html)
- [WAS - wsadmin (Jython) チュートリアル](http://www.mtitek.com/tutorials/websphere/wsadmin_jython.php)
- [IBM WebSphere - wsadmin の概要](https://www.freekb.net/Article?id=1563)
- [WSADMIN チュートリアル – Part1](https://websphereapplicationservernotes.wordpress.com/2012/12/25/wsadmin-tutorial-part1/)