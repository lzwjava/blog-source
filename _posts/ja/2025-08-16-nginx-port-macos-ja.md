---
audio: false
generated: true
image: false
lang: ja
layout: post
title: macOSでNginxのポートを変更する方法
translated: true
type: note
---

macOSでNginxの**デフォルトポート（HTTPは80、HTTPSは443）とは異なるポート**でリッスンさせたい場合の、明確なステップバイステップガイドです：

---

### 1. Nginx設定ファイルの場所を確認

* **Homebrew**でインストールした場合、デフォルトの設定ファイルは通常以下にあります：

  ```
  /usr/local/etc/nginx/nginx.conf
  ```

  または、Apple Siliconの場合は：

  ```
  /opt/homebrew/etc/nginx/nginx.conf
  ```
* 手動でインストールした場合は、`/usr/local/nginx/conf/nginx.conf`にある可能性があります。

---

### 2. `listen`ディレクティブを編集

1. テキストエディタで設定ファイルを開きます：

   ```bash
   nano /opt/homebrew/etc/nginx/nginx.conf
   ```
2. `server`ブロックを見つけます：

   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           root   html;
           index  index.html index.htm;
       }
   }
   ```
3. `listen 80;`を任意のポート（例：8080）に変更します：

   ```nginx
   listen 8080;
   ```

---

### 3. 設定をテスト

以下を実行：

```bash
nginx -t
```

* `syntax is ok`と`test is successful`と表示されれば、設定は有効です。
* エラーがある場合は、報告された行番号を確認してください。

---

### 4. Nginxを再起動

* Homebrewでインストールした場合：

```bash
brew services restart nginx
```

* または手動で：

```bash
sudo nginx -s reload
```

---

### 5. 新しいポートでアクセス

* ブラウザまたはcurlで：

```
http://localhost:8080
```

---

**補足事項：**

* **1024未満**のポートを使用する場合、macOSでは`sudo`が必要です。そのため、80のようなポートを使用するにはroot権限が必要ですが、8080や3000では必要ありません。
* 複数のNginxサーバーを同時に実行したい場合、それぞれが**固有のポート**を持っている必要があります。

---

また、**nginx.confを編集せずにコマンドラインフラグを使用して任意のポートでNginxを一時的に実行する簡単な方法**もあります。テストに便利です。表示しますか？