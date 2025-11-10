---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Windowsタスクキルコマンドガイド
translated: true
type: note
---

Windowsでは、`taskkill`は組み込みのコマンドラインツールで、**プロセスID（PID）** または **イメージ名（実行ファイル名）** でプロセスを停止（強制終了）するために使用できます。

### 基本構文

```bat
taskkill /PID <process_id> [/F]
taskkill /IM <image_name> [/F]
```

* `/PID <process_id>` → プロセスIDで終了
* `/IM <image_name>` → プロセス名で終了（例: `notepad.exe`）
* `/F` → プロセスを強制終了
* `/T` → 指定したプロセスとすべての子プロセスを終了

---

### 使用例

1. **PIDでプロセスを終了:**

```bat
taskkill /PID 1234
```

これはPID 1234のプロセスを停止しようとします。

2. **PIDでプロセスを強制終了:**

```bat
taskkill /PID 1234 /F
```

3. **名前でプロセスを終了:**

```bat
taskkill /IM notepad.exe
```

4. **名前で強制終了:**

```bat
taskkill /IM notepad.exe /F
```

5. **プロセスとその子プロセスを終了:**

```bat
taskkill /IM cmd.exe /T /F
```

---

### PIDの確認方法

PIDがわからない場合:

```bat
tasklist
```

これで実行中のすべてのプロセスとそのPIDが表示されます。その後、適切なPIDに対して`taskkill /PID`を使用できます。

---

⚠️ **注意点**

* 終了できないシステムプロセスもあります
* 保護されたプロセスを終了するには、コマンドプロンプトを**管理者として実行**する必要がある場合があります

---

`tasklist`と`taskkill`を1つのコマンドに組み合わせる方法（例：名前が一致するすべてのプロセスを自動的に終了）も表示しましょうか？