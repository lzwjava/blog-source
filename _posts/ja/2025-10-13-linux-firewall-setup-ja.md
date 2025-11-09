---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Linuxファイアウォール設定ガイド
translated: true
type: note
---

良い質問です — Linux（**Red Hat** や **Ubuntu** など）でのファイアウォール設定は、主に使用するシステムに応じて **`firewalld`** または **`ufw`** のいずれかを使用します。以下に、両方の系統向けの明確なガイドを示しますので、適切なものを選択してください。

---

### 🔹 **Red Hat / CentOS / Fedora** の場合 (firewalld)

#### 1. `firewalld` がインストールされ、実行されているか確認

```bash
sudo systemctl status firewalld
```

実行されていない場合:

```bash
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

#### 2. 基本的な使用方法

アクティブなゾーンを確認（ゾーンはインターフェースとルールをグループ化します）:

```bash
sudo firewall-cmd --get-active-zones
```

現在のゾーンのすべてのルールを一覧表示:

```bash
sudo firewall-cmd --list-all
```

#### 3. ポートやサービスを許可またはブロック

ポートを許可（例: ポート22のSSH）:

```bash
sudo firewall-cmd --permanent --add-port=22/tcp
```

既知のサービスを許可（例: HTTP）:

```bash
sudo firewall-cmd --permanent --add-service=http
```

許可をブロック/削除:

```bash
sudo firewall-cmd --permanent --remove-service=http
```

適用するためにリロード:

```bash
sudo firewall-cmd --reload
```

#### 4. ルールを確認

```bash
sudo firewall-cmd --list-all
```

---

### 🔹 **Ubuntu / Debian** の場合 (ufw)

Ubuntu には **UFW** (Uncomplicated Firewall) が同梱されており、より簡単に管理できます。

#### 1. UFW を有効化

```bash
sudo ufw enable
```

#### 2. ポートやサービスを許可/拒否

SSHを許可:

```bash
sudo ufw allow ssh
```

HTTP (ポート80) を許可:

```bash
sudo ufw allow 80/tcp
```

特定のポート範囲を許可:

```bash
sudo ufw allow 1000:2000/tcp
```

サービスを拒否:

```bash
sudo ufw deny 23/tcp
```

#### 3. ステータスを確認

```bash
sudo ufw status verbose
```

#### 4. 必要に応じてルールをリセット

```bash
sudo ufw reset
```

---

### 🔹 両システム共通

**いくつかを除くすべての着信トラフィックをブロック** するには、以下のようにできます:

1. デフォルトですべての着信を拒否

   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```

   (`firewalld` の場合、同様の動作にはゾーンまたはドロップゾーンを使用します)

2. その後、選択的にポート（例: 22, 80, 443）を許可します。

---

### 🔹 セキュリティのヒント

リモートでファイアウォールルールを有効化または変更する前に、必ず **まずSSHを許可** してください — そうしないと自身が締め出されてしまいます。

---

**最小限のファイアウォール設定の例**（例えば、SSH + HTTP + HTTPS のみを許可する典型的なWebサーバー向け）を示しましょうか？