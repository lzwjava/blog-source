---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: ウィンドウズのポートとプロセスの管理
translated: true
type: note
---

Windowsでは、`netstat`を使用してどのポートがどのプロセス（PID）によってリッスンされているかを確認し、`taskkill`でそれらのプロセスを管理または強制終了できます。これはJava Spring Bootアプリ、Redis、MySQLなどのバックエンドプロジェクトをデバッグする際に頻繁に必要となります。手順は以下の通りです：

---

### 1. リッスン中のポートを確認

**コマンドプロンプト (cmd)** または **PowerShell** を管理者として実行：

```bash
netstat -ano | findstr LISTENING
```

* `-a` → すべての接続とリッスンポートを表示
* `-n` → アドレスとポートを数値形式で表示
* `-o` → PID（プロセスID）を含める

出力例：

```
TCP    0.0.0.0:8080     0.0.0.0:0     LISTENING     12345
TCP    0.0.0.0:3306     0.0.0.0:0     LISTENING     6789
```

ここでは：

* ポート `8080` は PID `12345` によって使用されています（おそらくSpring Bootアプリ）。
* ポート `3306` は PID `6789` によって使用されています（MySQL）。

---

### 2. そのPIDがどのプロセスに属するか確認

PIDをプロセス名に一致させることができます：

```bash
tasklist | findstr 12345
```

出力例：

```
java.exe                  12345 Console                    1     512,000 K
```

これは、ポート8080でSpring Bootアプリが実行されていることを意味します。

---

### 3. 必要に応じてプロセスを強制終了

そのプロセスを停止したい場合：

```bash
taskkill /PID 12345 /F
```

* `/PID` → プロセスIDを指定
* `/F` → 強制終了

---

### 4. 一般的なバックエンドサービスの代表的なポート

* **Spring Boot (Java アプリ):** 8080, 8081 など
* **MySQL:** 3306
* **Redis:** 6379
* **PostgreSQL:** 5432

したがって、`netstat`の出力でこれらのポートを確認した場合、どのサービスが実行されているかがわかります。

---

👉 プロのヒント：特定のポート（例: 8080）を使用しているプロセスを直接見つけるために、これらのコマンドを1つに組み合わせることができます：

```bash
netstat -ano | findstr :8080
```

その後、PIDを取得し、`tasklist`で確認します。

---

**PowerShellのワンライナー**で、`tasklist`で個別に確認する必要なく、ポートをプロセス名に直接マッピングする方法もお見せしましょうか？