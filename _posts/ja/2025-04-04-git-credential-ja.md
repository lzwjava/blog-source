---
audio: false
generated: true
lang: ja
layout: post
title: Git資格情報マネージャー
translated: true
type: note
---

**macOS** で **Git Credential Manager (GCM) バージョン 2.6.1** を使用しており、`git config --global credential.helper manager-core` を実行した際に次のエラーが発生しました:

```
warning: credential.helper has multiple values
error: cannot overwrite multiple values with a single value
```

このエラーは、Git 設定に複数の資格情報ヘルパーが既に設定されている場合に発生します。新しい値を設定する前に、**既存の値をクリアする**必要があります。

---

### **🛠 問題の修正: 資格情報ヘルパーのリセット**
#### **ステップ 1: 現在の資格情報ヘルパーを確認する**
以下を実行します:
```sh
git config --global --get-all credential.helper
```
これにより、設定されているすべての資格情報ヘルパーが一覧表示されます。

#### **ステップ 2: 以前の資格情報ヘルパーを未設定にする**
すべての資格情報ヘルパーをリセットします:
```sh
git config --global --unset-all credential.helper
```

#### **ステップ 3: GCM を唯一の資格情報ヘルパーとして設定する**
再度、**Git Credential Manager (GCM)** をヘルパーとして設定します:
```sh
git config --global credential.helper manager-core
```

#### **ステップ 4: 変更を確認する**
正しく設定されているか確認します:
```sh
git config --global --get credential.helper
```
期待される出力:
```
manager-core
```

---

### **🛠 代替方法: `--replace-all` を使用する**
最初に未設定にせず、既存の値を上書きしたい場合は、以下を使用します:
```sh
git config --global --replace-all credential.helper manager-core
```

---

### **🧩 追加のデバッグ**
問題が解決しない場合は、グローバルな Git 設定全体を確認できます:
```sh
git config --global --list
```
問題が続く場合は、お知らせください！ 🚀

---

Git Credential Manager (GCM) は、HTTPS Git リポジトリの認証情報を安全に保存および管理する Git 資格情報ヘルパーです。GitHub、GitLab、Bitbucket、Azure DevOps などのサービスで動作します。

---

## **1. Git Credential Manager のインストール**
GCM は、Git for Windows および macOS と Linux の公式 Git ディストリビューションに含まれています。インストールされていない場合は、以下からダウンロードしてください:

🔗 **[GitHub 上の Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager)**

### **GCM がインストールされているか確認する**
以下を実行します:
```sh
git credential-manager version
```
インストールされている場合は、バージョン番号が表示されます。表示されない場合は、手動でインストールしてください。

---

## **2. GCM を使用するように Git を設定する**
次のコマンドを実行します:
```sh
git config --global credential.helper manager
```
macOS/Linux の場合は、以下を使用します:
```sh
git config --global credential.helper manager-core
```

現在の資格情報ヘルパーを確認するには:
```sh
git config --global credential.helper
```

---

## **3. Git サーバーで認証する**
設定が完了すると、HTTPS 経由でリモートリポジトリと初めて対話するとき（例: `git clone`, `git pull`）に、GCM が資格情報の入力を求めます。

- GitHub、GitLab、または Bitbucket を使用している場合、GCM は OAuth 認証のためにブラウザを開きます。
- Personal Access Token (PAT) を使用している場合は、パスワードの代わりに入力してください。

---

## **4. 資格情報の保存と管理**
GCM は資格情報を OS の資格情報ストアに安全に保存します:
- **Windows**: Windows Credential Manager
- **macOS**: macOS Keychain
- **Linux**: GPG 暗号化ファイル (`~/.git-credentials` または `~/.gitconfig`)

資格情報を手動で追加するには:
```sh
git credential approve
```

保存された資格情報を削除するには:
```sh
git credential reject https://github.com
```

すべての資格情報をクリアするには:
```sh
git credential reject
```

---

## **5. 異なる Git プロバイダーで Git Credential Manager を使用する**
### **GitHub**
パスワードの代わりに **Personal Access Token (PAT)** を使用します:
```sh
git credential reject https://github.com
git pull
```
ログインしてトークンを入力するように求められます。

### **GitLab**
GitLab では、OAuth または **PAT** を使用します:
```sh
git credential reject https://gitlab.com
git pull
```

### **Azure DevOps**
**PAT** または Azure 認証を使用します。

---

## **6. 問題のデバッグ**
資格情報が正しく保存または取得されない場合:
1. 資格情報ヘルパーを確認します:
   ```sh
   git config --global credential.helper
   ```
2. Git Credential Manager をリセットします:
   ```sh
   git credential reject https://your-git-service.com
   ```
3. 必要に応じて GCM を再インストールします。

特定のサービスの設定についてヘルプが必要ですか？ 🚀