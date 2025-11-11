---
audio: false
generated: true
lang: ja
layout: post
title: Nginx 403 Forbidden エラーの修正
translated: true
type: note
---

Nginx設定で発生している「403 Forbidden」エラーを修正するには、主に2つの問題点に対処する必要があります：`location`ブロックでの`root`ディレクティブの誤った使用と、ファイルシステムのパーミッション問題です。以下に、提供された設定に基づいて問題を解決するステップバイステップガイドを示します：

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies {
        root /path/to/your/movie/folder;
        autoindex on; # ディレクトリリスティングを有効にする
    }
}
```

`http://localhost/movies`にアクセスしたときに403 Forbiddenエラーが発生する場合、これは一般的にNginxが意図したディレクトリにアクセスできないか、提供できないことを示しています。修正方法は以下の通りです：

---

### 1. Nginx設定の修正
現在の`location /movies`ブロックでは`root /path/to/your/movie/folder;`を使用しています。Nginxでは、`root`ディレクティブはリクエストURI（例：`/movies`）を指定されたパスに追加するため、Nginxは`/path/to/your/movie/folder/movies`からファイルを提供しようとします。このディレクトリが存在しない場合、Nginxは403エラーを返します。

これを修正するには、`root`の代わりに`alias`ディレクティブを使用する必要があります。`alias`ディレクティブは、URIを追加せずに`/movies/`URIを直接`/path/to/your/movie/folder/`にマッピングします。これがおそらく意図した動作です。

設定を以下のように更新してください：

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # ディレクトリリスティングを有効にする
    }
}
```

- **主な変更点：**
  - `root`を`alias`に変更
  - `autoindex`での適切なディレクトリ処理を確保するため、`location /movies/`と`alias /path/to/your/movie/folder/`に末尾のスラッシュを追加

- **変更の適用：**
  設定ファイル（例：`/etc/nginx/nginx.conf`または`/etc/nginx/sites-enabled/`内のファイル）を更新した後、Nginxを再起動して変更を適用します：
  - Linuxの場合：`sudo systemctl restart nginx`
  - Windowsの場合：Nginxサービスを手動で停止・開始

- **URLのテスト：**
  `http://localhost/movies/`（末尾のスラッシュに注意）にアクセスして、ディレクトリリスティングが表示されるか確認してください

---

### 2. ファイルシステムのパーミッション確認
設定変更だけでは403エラーが解決しない場合、ファイルシステムのパーミッションに関連する問題である可能性があります。Nginxは`/path/to/your/movie/folder/`とその内容への読み取りアクセス権が必要であり、このアクセスはNginxが実行されているユーザー（一般的に`nginx`または`www-data`）に依存します。

- **Nginxユーザーの特定：**
  メインのNginx設定ファイル（例：`/etc/nginx/nginx.conf`）の`user`ディレクティブを確認してください：
  ```nginx
  user nginx;
  ```
  指定されていない場合、システムによっては`www-data`または他のユーザーがデフォルトになる可能性があります

- **パーミッションの確認：**
  以下のコマンドを実行して、動画フォルダのパーミッションを確認します：
  ```bash
  ls -l /path/to/your/movie/folder
  ```
  これにより、所有者、グループ、パーミッション（例：`drwxr-xr-x`）が表示されます

- **必要に応じてパーミッションを調整：**
  Nginxユーザーが読み取り（およびディレクトリに対する実行）アクセス権を持っていることを確認してください。2つのオプションがあります：
  - **オプション1：所有権の変更（推奨）：**
    フォルダの所有者をNginxユーザー（例：`nginx`）に設定します：
    ```bash
    sudo chown -R nginx:nginx /path/to/your/movie/folder
    ```
    `nginx`が異なる場合は実際のユーザー（例：`www-data`）に置き換えてください

  - **オプション2：すべてのユーザーが読み取り可能にする（安全性が低い）：**
    所有権を変更したくない場合は、フォルダを他のユーザーが読み取り可能にします：
    ```bash
    sudo chmod -R o+r /path/to/your/movie/folder
    ```

- **ディレクトリアクセスの確保：**
  ディレクトリ自体にNginxがその内容にアクセスするための実行パーミッション（`x`）が必要です：
  ```bash
  sudo chmod o+x /path/to/your/movie/folder
  ```

- **親ディレクトリの確認：**
  `/path/to/your/movie/folder`が制限された親ディレクトリ（例：`/home/user/`）内にある場合、ルートまでのすべての親ディレクトリにNginxユーザーの実行パーミッションがあることを確認してください：
  ```bash
  sudo chmod o+x /path /path/to /path/to/your /path/to/your/movie
  ```

---

### 3. 検証とトラブルシューティング
これらの変更を加えた後、`http://localhost/movies/`に再度アクセスしてテストしてください。403エラーが続く場合：

- **Nginxエラーログの確認：**
  エラーログ（通常は`/var/log/nginx/error.log`）を確認して詳細を確認します：
  ```bash
  sudo tail -f /var/log/nginx/error.log
  ```
  「permission denied」や「directory index is forbidden」などのメッセージを探して問題を特定してください

- **追加の考慮事項：**
  - **SELinux（該当する場合）：** CentOSなどのSELinuxが有効なシステムでは、アクセスをブロックする可能性があります。テストのためにSELinuxを一時的にpermissiveモードに設定します：
    ```bash
    sudo setenforce 0
    ```
    これで問題が解決する場合は、SELinuxポリシーを調整する必要があります（例：`chcon`や`audit2allow`の使用）
  - **ファイアウォール：** 別のマシンからアクセスする場合はポート80が開いていることを確認してください（ただし、`localhost`経由でローカルテストしている場合は可能性は低いです）

---

### 最終的な設定
修正された完全な設定を以下に示します：

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # ディレクトリリスティングを有効にする
    }
}
```

- `/path/to/your/movie/folder/`を実際の動画ディレクトリへの絶対パスに置き換えてください
- Nginxを再起動：`sudo systemctl restart nginx`
- `http://localhost/movies/`にアクセスして、ディレクトリリスティングが機能することを確認してください

`alias`ディレクティブを修正し、適切なファイルパーミッションを確保することで、403 Forbiddenエラーは解決され、Nginx経由で動画フォルダにアクセスできるようになります。

---

Nginxの403 Forbiddenエラーを修正し、単一の`.mkv`ファイルにアクセスできるようにするために、状況に基づいて設定を改良しましょう。1つの`.mkv`ファイルがあり、Nginxユーザーがアクセスできる場所に保存する方法を知りたいとします。以下では、適切なディレクトリの選択とNginxの設定を含むプロセスをステップバイステップで説明します。

### ステップ1：`.mkv`ファイルの保存ディレクトリを選択
Nginxが提供する`.mkv`ファイルを保存する場所を決定する際は、以下の要素を考慮してください：
- **アクセシビリティ**：Nginxユーザー（例：`nginx`または`www-data`）が読み取りアクセス権を必要とします
- **慣例**：Webサーバーは通常、`/var/www/`や`/srv/www/`などの標準ディレクトリからファイルを提供します
- **セキュリティ**：過度に許可されたり機密性の高い場所（例：必要でない限り`/home/user/`）にファイルを配置しないでください

今回は単一の`.mkv`ファイルで、ローカル（`localhost`）でテストしているため、シンプルで標準的な場所として`/var/www/html/movies/`を使用することをお勧めします。その理由は：
- `/var/www/html/`はNginxとApacheの一般的なデフォルトのWebルートです
- 通常、Webサーバーユーザーまたはグループが所有しているため、パーミッション管理が容易です
- `/movies/`サブディレクトリを追加することで整理された状態を保てます

システムに`/var/www/html/`が存在しないか適切でない場合、代替案として以下があります：
- `/srv/www/movies/`（別の標準的なWebディレクトリ）
- `/usr/share/nginx/html/movies/`（場合によってはデフォルトのNginxドキュメントルート）

この例では、`/var/www/html/movies/`を使用します。

### ステップ2：ディレクトリとファイルの設定
Linuxシステムを想定して、以下の手順に従ってください：

1. **ディレクトリの作成**：
   ```bash
   sudo mkdir -p /var/www/html/movies
   ```

2. **`.mkv`ファイルの移動**：
   `yourfile.mkv`を実際のファイル名に置き換え、ディレクトリに移動します：
   ```bash
   sudo mv /path/to/yourfile.mkv /var/www/html/movies/yourfile.mkv
   ```

3. **パーミッションの設定**：
   Nginxユーザー（一般的に`nginx`または`www-data`）はファイルへの読み取りアクセス権とディレクトリへの実行アクセス権が必要です。まず、`/etc/nginx/nginx.conf`を確認してNginxユーザーを特定します：
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   `user nginx;`や`user www-data;`のような行を探してください。指定されていない場合、デフォルトは`www-data`（Ubuntu/Debian）または`nginx`（CentOS/RHEL）である可能性があります

   次に、所有権を調整します：
   ```bash
   sudo chown -R nginx:nginx /var/www/html/movies
   ```
   `nginx`が異なる場合は`www-data`または実際のユーザーに置き換えてください

   適切なパーミッションを確保します：
   ```bash
   sudo chmod -R 755 /var/www/html/movies
   ```
   - `755`は所有者（Nginx）がフルアクセス権を持ち、他のユーザー（Webサーバープロセスを含む）がディレクトリを読み取り・実行（ナビゲート）できることを意味します

### ステップ3：Nginxの設定
Nginx設定を更新して、`/var/www/html/movies/`から`.mkv`ファイルを提供します。以下は最小限の動作設定です：

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/html/movies/;
        autoindex on; # ファイルを閲覧したい場合はディレクトリリスティングを有効にする
    }
}
```

- **注意点**：
  - URIを追加せずに`/movies/`を直接`/var/www/html/movies/`にマッピングするために、`root`の代わりに`alias`を使用します
  - `autoindex on;`はオプションです。無効にした場合（`autoindex off;`）、ファイルにアクセスするには正確なファイルURL（例：`http://localhost/movies/yourfile.mkv`）を指定する必要があります

この設定を保存し（例：`/etc/nginx/sites-enabled/default`またはカスタムファイル`/etc/nginx/conf.d/movies.conf`）、テストしてNginxを再起動します：
```bash
sudo nginx -t  # 構文エラーのための設定テスト
sudo systemctl restart nginx  # 変更を適用
```

### ステップ4：アクセスのテスト
- ブラウザを開いて以下にアクセスします：
  - `http://localhost/movies/`（`autoindex`がオンの場合、`yourfile.mkv`を含むディレクトリリスティングが表示されます）
  - `http://localhost/movies/yourfile.mkv`（ファイルに直接アクセスするため）
- 機能する場合、ファイルはブラウザに表示されるか（サポートされている場合）、ダウンロードを促すプロンプトが表示されます

### ステップ5：必要に応じてトラブルシューティング
まだ403エラーが発生する場合：
1. **パーミッションの確認**：
   ```bash
   ls -l /var/www/html/movies/
   ```
   `yourfile.mkv`が読み取り可能（例：`-rwxr-xr-x`または少なくとも`-rw-r--r--`）であることを確認してください

2. **Nginxログの確認**：
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```
   「permission denied」などの手がかりを探してください

3. **SELinux（該当する場合）**：
   SELinuxを使用するシステム（例：CentOS）では、以下を実行します：
   ```bash
   sudo setenforce 0  # 一時的に無効化
   ```
   再度テストします。機能する場合は、SELinuxコンテキストを調整する必要があります：
   ```bash
   sudo chcon -R -t httpd_sys_content_t /var/www/html/movies/
   sudo setenforce 1  # SELinuxを再有効化
   ```

### 最終的な考え方
`.mkv`ファイルを`/var/www/html/movies/`に保存し、正しいパーミッションを設定し、Nginxで`alias`ディレクティブを使用することで、403エラーは解決するはずです。この設定はシンプルでWebサーバーの慣例に従っているため、Nginxユーザーがファイルにアクセスしやすくなります。問題が発生したらお知らせください！

---

`sudo chown -R nginx:nginx /var/www/movies`で「invalid user」エラーが発生する場合、システムに`nginx`ユーザーが存在しないことを意味します。これは、Nginxプロセスが異なるユーザー（Debian/Ubuntuでは`www-data`など）で実行されているために発生します。OSによってデフォルトが異なります。

### 修正：正しいユーザーの特定と使用
1. **Nginxユーザーの確認**：
   Nginx設定ファイル（通常は`/etc/nginx/nginx.conf`）を確認します：
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   - `user www-data;`と表示される場合は、`www-data`を使用します
   - `user nginx;`と表示される場合は、`nginx`ユーザーが存在するはずです（設定ミスの可能性を示唆）
   - `user`ディレクティブが見つからない場合、デフォルトユーザーはシステムによって異なります：
     - Ubuntu/Debian：`www-data`
     - CentOS/RHEL：`nginx`
     - その他：`http`、`apache`など

2. **代替：実行中のプロセスの確認**：
   設定が明確でない場合、Nginxがどのユーザーで実行されているかを確認します：
   ```bash
   ps aux | grep nginx
   ```
   ワーカープロセスの最初の列（例：`www-data`または`nginx`）を確認します

3. **正しいユーザーの適用**：
   Ubuntu/Debianで一般的な`www-data`を想定して、コマンドを更新します：
   ```bash
   sudo chown -R www-data:www-data /var/www/movies
   ```
   異なるユーザー（例：`http`）の場合は、以下を使用します：
   ```bash
   sudo chown -R http:http /var/www/movies
   ```

4. **パーミッションの設定**：
   所有権を修正した後、適切なパーミッションを確保します：
   ```bash
   sudo chmod -R 755 /var/www/movies
   ```

5. **再起動とテスト**：
   ```bash
   sudo systemctl restart nginx
   ```
   `http://localhost/movies/yourfile.mkv`にアクセスします

### まだ解決しない場合
`nginx`も`www-data`も機能せず、プロセスチェックでも役に立たない場合は、OS（例：Ubuntu、CentOS）または`ps aux | grep nginx`の出力を教えてください。正確なユーザーを特定します！

---

`autoindex on;`が設定されているのに`http://localhost/movies/`でまだファイルが表示されない場合、段階的にトラブルシューティングして修正しましょう。ディレクトリリスティングが表示されないのは、設定の問題、パーミッションの問題、または何か他のものがブロックしている可能性があります。解決方法は以下の通りです：

### 1. 設定の確認
Nginx設定が正しく適用されていることを確認します。以下のようになっている必要があります：

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

- **一般的なミス**：
  - `alias`パスのタイプミス（例：`/var/www/movie/`ではなく`/var/www/movies/`）
  - `autoindex on;`が間違ったブロックにあるかコメントアウトされている
  - 設定ファイルが読み込まれていない（例：間違った場所に保存されている）

設定ファイルの場所を確認します：
- `/etc/nginx/sites-enabled/`にある場合、適切にリンクされていることを確認します（例：`ls -l /etc/nginx/sites-enabled/`）
- `/etc/nginx/conf.d/`にある場合、`.conf`で終わることを確認します（例：`movies.conf`）

テストとリロード：
```bash
sudo nginx -t
sudo systemctl reload nginx  # ダウンタイムを避けるために再起動ではなくリロード
```

### 2. ファイルの存在確認
`/var/www/movies/`に`.mkv`ファイルがあることを確認します：
```bash
ls -l /var/www/movies/
```
- 空の場合、ファイルをそこに移動します：
  ```bash
  sudo mv /path/to/yourfile.mkv /var/www/movies/
  ```
- 空でない場合、テスト用にファイル名をメモします

### 3. パーミッションの確認
Nginxはディレクトリとファイルへの読み取り（`r`）および実行（`x`）アクセス権が必要です。確認します：
```bash
ls -ld /var/www/movies/
ls -l /var/www/movies/
```
- 出力は以下のようになっている必要があります：
  ```
  drwxr-xr-x 2 www-data www-data 4096 Mar 15 14:00 /var/www/movies/
  -rw-r--r-- 1 www-data www-data 123456 Mar 15 14:00 yourfile.mkv
  ```
- 必要に応じて修正します（`www-data`をNginxユーザーに置き換えて）：
  ```bash
  sudo chown -R www-data:www-data /var/www/movies/
  sudo chmod -R 755 /var/www/movies/
  ```

### 4. ログの確認
Nginxエラーログを確認して手がかりを得ます：
```bash
sudo tail -n 20 /var/log/nginx/error.log
```
- **「permission denied」**：パーミッション問題を示唆 - ステップ3を再確認
- **「directory index forbidden」**：`autoindex`が機能していないことを示唆 - 設定を再確認
- 関連するエラーがない：Nginxが正しいlocationブロックにヒットしていない可能性があります

### 5. 直接アクセスのテスト
特定のファイルへのアクセスを試みます：
- `http://localhost/movies/yourfile.mkv`にアクセスします
- これが機能するが`/movies/`が機能しない場合、`autoindex`またはディレクトリ設定が問題です

### 6. 一般的な修正
- **末尾のスラッシュ**：`alias`が`/`で終わることを確認し（`/var/www/movies/`）、`http://localhost/movies`と`http://localhost/movies/`の両方をテストします
- **SELinux（CentOS/RHELの場合）**：
  ```bash
  sudo setenforce 0  # 一時的に無効化
  ```
  再度テストします。機能する場合は以下を適用します：
  ```bash
  sudo chcon -R -t httpd_sys_content_t /var/www/movies/
  sudo setenforce 1
  ```
- **競合するLocationブロック**：別の`location`ブロック（例：`location /`）が`/movies/`を上書きしている場合、このブロックを設定内で上位に移動するか、より具体的にします

### 7. 最小限のテスト設定
まだ機能しない場合は、問題を分離するために簡素化します。設定を以下に置き換えます：

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

保存、テスト、リロード：
```bash
sudo nginx -t
sudo systemctl reload nginx
```

### 何が起こっていますか？
以下を教えてください：
- `http://localhost/movies/`で何が見えますか？（例：403、404、空白ページ）
- `sudo tail -n 20 /var/log/nginx/error.log`にエラーはありますか？
- `ls -l /var/www/movies/`の出力は？

それらの情報をもとに、正確な問題を特定し、ディレクトリリスティングを機能させます！