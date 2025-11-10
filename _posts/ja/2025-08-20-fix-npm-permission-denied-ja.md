---
audio: false
generated: true
image: false
lang: ja
layout: post
title: npm パーミッションエラーを修正
translated: true
type: note
---

発生している `EACCES: permission denied` エラーは、現在のユーザーが `/usr/local/lib/node_modules` ディレクトリへの**書き込み権限を持っていない**ことを意味します。これはLinuxやmacOSでグローバルなnpmパッケージをインストールする際によく発生する問題です。

### **この問題の解決方法**

#### **オプション1: `sudo` を使用する（通常使用には非推奨）**
rootユーザーとしてコマンドを実行するために `sudo` を使用できますが、後にnpmパッケージで権限の問題を引き起こす可能性があるため、**通常使用には推奨されません**。

```bash
sudo npm install -g @anthropic-ai/claude-code
```

#### **オプション2: npmのデフォルトディレクトリを変更する（推奨）**
ベストプラクティスは、書き込み権限があるホームフォルダ内のディレクトリを使用するようにnpmを設定することです。

1. **ホームフォルダにグローバルnpmディレクトリを作成:**
   ```bash
   mkdir ~/.npm-global
   ```
2. **npmにこのディレクトリを使用するように設定:**
   ```bash
   npm config set prefix '~/.npm-global'
   ```
3. **新しいディレクトリを `PATH` に追加:**
   シェル設定ファイル（例: `~/.bashrc`, `~/.zshrc`, `~/.profile`）を開き、この行を追加:
   ```bash
   export PATH=~/.npm-global/bin:$PATH
   ```
   その後、シェルをリロード:
   ```bash
   source ~/.bashrc  # または ~/.zshrc, ~/.profile
   ```
4. **インストールを再試行:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

#### **オプション3: `/usr/local` の権限を修正する（上級者向け）**
`/usr/local` の使用を継続したい場合は、その所有権を自分のユーザーに変更できます:
```bash
sudo chown -R $(whoami) /usr/local/lib/node_modules
```
その後、インストールを再試行してください。

---

**推奨:** 将来の権限問題を避けるために**オプション2**を使用してください。