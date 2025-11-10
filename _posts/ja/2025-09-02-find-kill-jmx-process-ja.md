---
audio: false
generated: true
image: false
lang: ja
layout: post
title: JMXポートプロセスの検索と強制終了
translated: true
type: note
---

了解しました — Windows で **JMX リモートエージェント** がポート `9091` で動作している Java プログラムを特定し、必要に応じて強制終了したいのですね。手順をステップバイステップで説明します：

---

### 1. ポート 9091 を使用しているプロセスを特定する

**コマンド プロンプト**を（可能であれば管理者権限で）開き、以下を実行します：

```cmd
netstat -ano | findstr :9091
```

次のような結果が表示されます：

```
  TCP    0.0.0.0:9091    0.0.0.0:0    LISTENING    12345
```

* 最後の列（ここでは `12345`）が **PID（プロセス ID）** です。

---

### 2. その PID がどのプログラムに属するか確認する

次に、PID を実際のプログラムに対応させます：

```cmd
tasklist /FI "PID eq 12345"
```

次のような結果が表示されます：

```
Image Name                     PID   Session Name        Mem Usage
========================= ======== ================ ============
java.exe                    12345 Console           200,000 K
```

Java プロセスの場合、さらに詳細を確認できます：

```cmd
wmic process where processid=12345 get CommandLine
```

これにより、JVM の起動に使用された**コマンドライン**が表示されます — JMX フラグ (`-Dcom.sun.management.jmxremote.port=9091`) が確認できれば、JMX リモートエージェントであることが確定します。

---

### 3. プロセスを強制終了する

停止させても安全であることを確認したら、強制終了できます：

```cmd
taskkill /PID 12345 /F
```

* `/PID` はプロセス ID を指定します。
* `/F` は強制終了を意味します。

---

### 4. PowerShell を使用する別の方法

PowerShell を利用する場合は、以下を実行できます：

```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess
```

直接強制終了するには：

```powershell
Stop-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess -Force
```

---

🔎 まとめ：

1. `netstat -ano | findstr :9091` → PID を取得
2. `tasklist /FI "PID eq <PID>"` → プログラムを確認
3. `wmic process where processid=<PID> get CommandLine` → JVM フラグを確認
4. `taskkill /PID <PID> /F` → 強制終了

---

**複数の JVM に対して JMX エージェントポート（例: 9090, 9999 など）が動作しているかどうかをまとめて確認する方法**もお見せしましょうか？