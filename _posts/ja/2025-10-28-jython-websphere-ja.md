---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphere Application Server における Jython
translated: true
type: note
---

### IBM WebSphere Application ServerでのJythonの使用

注: 「jPython」はJythonを指し、Java仮想マシン（JVM）上で動作するPythonの実装です。WebSphereでは管理スクリプト作成によく使用され、デプロイされたアプリケーションに統合することもできます。WebSphere Application Server（WAS）はJython（通常はWASのバージョンに応じてバージョン2.1以降）を`<WAS_HOME>/optionalLibraries/jython`の下にバンドルしているため、通常は別途インストールする必要はありません。以下では、管理タスクとアプリケーションでのランタイム使用という2つの主なユースケースについて説明します。

#### 1. wsadminによる管理スクリプト作成
WebSphereでJythonを使用する最も一般的な方法は、アプリケーションのデプロイ、サーバーの起動/停止、リソースの設定、インストール済みアプリの一覧表示などのサーバー管理タスクです。これは`wsadmin`ツールを使用して行われ、Jythonは推奨スクリプト言語としてサポートされています（非推奨のJaclよりも）。

**前提条件:**
- WebSphereサーバーが実行中であることを確認してください。
- `wsadmin`を`<WAS_HOME>/bin/wsadmin.sh`（Linux/Unix）または`wsadmin.bat`（Windows）で見つけてください。
- Jythonは事前にバンドルされています。新しい機能（例: Python 2.5+の構文）を使用する場合は、カスタムクラスパスを介したアップグレードが必要な場合があります（以下の高度な注意事項を参照）。

**Jythonスクリプトを実行する基本的な手順:**
1. Jythonスクリプトファイル（例: `example.py`）を作成し、コードを記述します。WebSphere固有の操作にはAdminConfig、AdminControl、AdminAppオブジェクトを使用します。
   
   インストールされているすべてのアプリケーションを一覧表示するスクリプトの例（`listApps.py`）:
   ```
   # すべてのアプリケーションを一覧表示
   apps = AdminApp.list()
   print("インストール済みアプリケーション:")
   for app in apps.splitlines():
       if app.strip():
           print(app.strip())
   AdminConfig.save()  # オプション: 設定変更を保存
   ```

2. `wsadmin`を使用してスクリプトを実行します:
   - SOAP経由で接続（リモート接続のデフォルト）:  
     ```
     wsadmin.sh -lang jython -f listApps.py -host <ホスト名> -port <soap_port> -user <管理者ユーザー> -password <管理者パスワード>
     ```
   - ローカル接続の場合（ホスト/ポートなし）:  
     ```
     wsadmin.sh -lang jython -f listApps.py
     ```
   - 出力例: `DefaultApplication`のようなアプリが一覧表示されます。

3. 対話モード（REPL）の場合:  
   ```
   wsadmin.sh -lang jython
   ```
   その後、Jythonコマンドを直接入力します（例: `print AdminApp.list()`）。

**一般的な例:**
- **EAR/WARのデプロイ:** `deployApp.py`を作成:
  ```
  appName = 'MyApp'
  earPath = '/path/to/MyApp.ear'
  AdminApp.install(earPath, '[-appname ' + appName + ' -server server1]')
  AdminConfig.save()
  print('デプロイ済み ' + appName)
  ```
  実行: `wsadmin.sh -lang jython -f deployApp.py`.

- **サーバーの起動/停止:**  
  ```
  server = AdminControl.completeObjectName('type=Server,process=server1,*')
  AdminControl.invoke(server, 'start')  # または 'stop'
  ```

- **Jythonバージョンの指定（必要な場合）:** Jython 2.1を明示的に使用する場合:  
  `wsadmin.sh -usejython21 true -f script.py`. カスタムバージョンの場合は、クラスパスに追加: `-wsadmin_classpath /path/to/jython.jar`.

**ヒント:**
- コマンドのヘルプには`AdminConfig.help('object_type')`を使用します。
- スクリプトは、バッチファイルで`wsadmin`を呼び出すことでCI/CD（例: Jenkins）で自動化できます。
- シンクライアント（完全なWASインストールなし）の場合: IBMからクライアントjarをダウンロードし、クラスパスを設定します。

#### 2. デプロイされたアプリケーションでのJythonの使用
WebSphere上で実行されているJavaアプリケーション（例: サーブレットやEJB）内でJythonコードを実行するには、アプリケーションのクラスパスにJythonランタイム（jython.jar）を含めます。これにより、Pythonスクリプトの埋め込みや、Jythonをスクリプトエンジンとして使用することが可能になります。バンドルされているバージョンが古い場合は、公式Jythonサイトから最新のjython.jarをダウンロードしてください。

主に2つの方法があります: **クラスパス**（サーバー全体）または**共有ライブラリ**（アプリ間で再利用可能）。

**方法1: クラスパス（JVMへの直接追加）**
1. `jython.jar`をWebSphereホストのアクセス可能なパス（例: `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/mylibs/jython.jar`）に保存します。
2. WebSphere管理コンソールにログインします。
3. **サーバー > サーバーの種類 > WebSphereアプリケーションサーバー > [対象サーバー]** に移動します。
4. **Javaとプロセス管理 > プロセス定義 > Java仮想マシン > クラスパス** に進みます。
5. `jython.jar`への完全なパス（例: `/opt/.../jython.jar`）を追加します。
6. **汎用JVM引数**で、Pythonパスを追加します:  
   `-Dpython.path=/opt/.../jython.jar/Lib`（Jythonの標準ライブラリを指します）。
7. **OK**をクリックし、設定を保存してサーバーを再起動します。
8. クラスタ環境の場合はノードを同期します（**システム管理 > ノード > 同期**経由）。
9. Javaコードで`org.python.util.PythonInterpreter`を使用してJythonスクリプトを実行します:
   ```
   import org.python.util.PythonInterpreter;
   PythonInterpreter interpreter = new PythonInterpreter();
   interpreter.exec("print('Hello from Jython in WebSphere!')");
   ```

**方法2: 共有ライブラリ（複数アプリに推奨）**
1. `jython.jar`を共有ディレクトリ（例: `/shared/libs/jython.jar`）に配置します。
2. 管理コンソールで: **環境 > 共有ライブラリ > [スコープ: サーバーまたはセル] > 新規**。
3. 名前（例: `JythonLib`）を入力し、**ネイティブライブラリディレクトリーを使用**をチェックし、**クラスパス**を`/shared/libs/jython.jar`に設定します。
4. 保存します。
5. 特定のアプリケーションの場合: **アプリケーション > アプリケーションの種類 > WebSphereエンタープライズアプリケーション > [対象アプリ] > 共有ライブラリ参照**。
6. **共有ライブラリ参照**で**追加**をクリックし、`JythonLib`を選択し、**クラスパス**が一致するように設定します。
7. 保存し、アプリを更新（必要に応じて再起動）し、ノードを同期します。
8. クラスパス方法と同様にコードで参照します。

**アプリ向けのヒント:**
- サーブレットベースのJythonアプリの場合、PythonハンドラーにPyServlet（Jythonに含まれる）を使用します。
- 開発環境でテストし、クラスパスに関する問題がないかログを監視します。
- 新しいJython（例: 2.7）を使用する場合は、Java 8+との互換性を確認します。

#### 高度な注意事項
- **バージョン互換性:** WAS 9.xはJython 2.7+を使用します。アップグレードする場合は、バンドルされているjarを置き換えますが、十分にテストしてください。
- **エラー処理:** スクリプトでは`try: ... except Exception as e: print(e)`を使用します。
- **IDEサポート:** Jython/wsadminスクリプトのデバッグには、IBM Rational Application Developer（RAD）またはWebSphereプラグインを備えたEclipseを使用します。
- **リソース:** 完全なチュートリアルについては、書籍*WebSphere Application Server Administration Using Jython*またはIBMのwsadminドキュメントを参照してください。

これが特定のWASバージョンやユースケースに正確に一致しない場合は、詳細を提供して具体的なアドバイスを受けてください。

**参考文献:**  
- [Jythonを使用したwsadminスクリプト作成（IBM Docs）](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-using-wsadmin-jython)  
- [WebSphereへのJythonのデプロイ（Oracleガイド）](https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/deploying-jython-on-ais-server-on-ibm-websphere-application.html)  
- [WebSphere Jython統合（Stack Overflow）](https://stackoverflow.com/questions/25187577/will-the-ibm-websphere-application-server-run-the-python-jython-script-without-p)  
- [WebSphereに関するJython Wiki](https://wiki.python.org/jython/WebSphere)  
- [Jythonを使用したアプリのデプロイ例](https://jobhunterssite.wordpress.com/2016/05/12/deploy-an-application-in-websphere-using-jython-automation/)