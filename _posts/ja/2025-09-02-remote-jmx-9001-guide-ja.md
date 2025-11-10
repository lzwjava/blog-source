---
audio: false
generated: true
image: false
lang: ja
layout: post
title: リモートJMXポート9001ガイド
translated: true
type: note
---

**JMXリモートエージェント**は、Java Management Extensions（JMX）の一部です。これにより、実行中のJavaアプリケーションをリモートで監視および管理できます。JMXリモート管理を有効にすると、JVMはTCPポートを介してMBean（Managed Bean）を公開するエージェントを起動します。**jconsole**、**VisualVM**、またはカスタム監視ソフトウェアなどのツールは、そのポートに接続して、メモリ使用量、スレッド状態、GCアクティビティを検査したり、さらには操作を呼び出したりすることができます。

**ポート9001**について:

* 実際のポート番号は、アプリケーションの設定方法によって異なります。一般的には、9001、9090、9091などが使用されます。
* `9001`で何かがリッスンしているのを確認し、それが**JMXリモートエージェント**である場合、以下のようなシステムプロパティで起動されたJavaプロセスであることを意味します:

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9001
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```

これは、認証/SSLなしでポート`9001`でJMXを開放します（公開されると安全ではないため、内部または開発環境での使用が一般的です）。

---

### WindowsでJMXポート9001を使用しているプログラムを確認する方法

1. **コマンドプロンプトを管理者として開きます**。
2. 以下を実行します:

   ```cmd
   netstat -ano | findstr :9001
   ```

   これにより、そのポートにバインドされているPID（プロセスID）が表示されます。
3. プログラムを特定するには:

   ```cmd
   tasklist /FI "PID eq <PID>"
   ```

   `<PID>`をステップ2で取得した番号に置き換えてください。

---

### 停止/強制終了する方法

* 不要なJavaプロセスであることを確認した場合、以下で強制終了できます:

  ```cmd
   taskkill /PID <PID> /F
   ```
* ただし、それがアプリケーションサーバー（Tomcat、WebSphere、Spring Bootアプリなど）の一部である場合は、プロセスを強制終了するのではなく、そのサービスやコンソールから停止させ、適切にシャットダウンさせる方が良いでしょう。

---

👉 Javaアプリケーションで**JMXリモートエージェントを無効化**し、ポート9001をまったく開かないようにする方法もご紹介しましょうか？