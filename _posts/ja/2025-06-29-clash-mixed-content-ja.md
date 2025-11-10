---
audio: false
generated: true
lang: ja
layout: post
title: Clash VPNの混在コンテンツエラーを修正
translated: true
type: note
---

発生しているエラーメッセージは、Clash VPNアプリケーションの**混合コンテンツ**問題を示しています。具体的には、`https://clash.razord.top/` のページが、安全でない `http://127.0.0.1:9090/` エンドポイント（例: `http://127.0.0.1:9090/version`）からリソースを読み込もうとしています。現代のブラウザは、安全なHTTPSページ上で安全でないHTTPコンテンツの読み込みを試みることでセキュリティポリシーに違反するため、このようなリクエストをブロックします。さらに、アクセス制御制限によるCORS（Cross-Origin Resource Sharing）エラーも発生しています。以下に、この問題を解決するためのステップバイステップガイドを示します。

---

### 問題の原因
- **混合コンテンツエラー**: ウェブページはHTTPSで配信されていますが、`http://127.0.0.1:9090` のような安全でないエンドポイントから（バージョンチェックなどの）リソースを取得しようとしています。ブラウザは、中間者攻撃などの潜在的なセキュリティ脆弱性を防ぐために、これらのリクエストをブロックします。
- **CORSエラー**: サーバーによって明示的に許可されていない限り、クロスオリジンリクエストを制限するCORSポリシーのため、ブラウザは `http://127.0.0.1:9090` へのリクエストをブロックしています。
- **Clashのコンテキスト**: Clash（またはClash for Windows）は、そのダッシュボードやAPIにローカルサーバー（`127.0.0.1:9090`）を使用するプロキシアプリケーションです。このローカルサーバーがHTTPSをサポートしていない、または正しく設定されていない場合、HTTPSのウェブページからアクセスされるとこれらのエラーを引き起こします。

---

### 問題解決の手順

#### 1. **Clash Coreの設定を確認する**
   - **Clash Coreが実行されているか確認**: Clash core（バックエンドサービス）がマシン上で実行され、`127.0.0.1:9090` でリッスンしていることを確認してください。以下で確認できます：
     - ターミナルまたはコマンドプロンプトを開く。
     - `curl http://127.0.0.1:9090/version` を実行して、エンドポイントがClashのバージョンを応答するか確認する。
     - 応答しない場合は、Clashサービスがアクティブであることを確認する。Clash for WindowsまたはClash coreプロセスを再起動する。
   - **Clash CoreでHTTPSを有効にする**（可能な場合）:
     - 一部のClashバージョン（例: Clash Premium または Clash Meta）は、ローカルAPI用のHTTPSをサポートしています。Clashのドキュメントまたは設定ファイル（通常は `config.yaml`）で、外部コントローラー（APIエンドポイント）に対してHTTPSを有効にするオプションを確認してください。
     - 設定ファイル内で `external-controller` や `external-ui` のような設定を探してください。例：
       ```yaml
       external-controller: 127.0.0.1:9090
       external-ui: <uiへのパス>
       ```
       HTTPSがサポートされている場合、ローカルサーバー用の証明書を設定する必要があるかもしれません。これは高度な設定であり、自己署名証明書の生成が必要になる場合があります（下記のステップ4を参照）。

#### 2. **HTTP経由でダッシュボードにアクセスする（一時的な回避策）**
   - ClashダッシュボードがHTTP経由（例: `https://clash.razord.top/` ではなく `http://clash.razord.top/`）でアクセスできる場合、混合コンテンツ問題を避けるためにHTTPSなしで読み込んでみてください：
     - ブラウザを開き、`http://clash.razord.top/` に移動します。
     - 注意: HTTPは安全ではないため、本番環境での使用は推奨されません。テスト時、またはダッシュボードがローカルでのみアクセスされる場合にのみ使用してください。
   - ダッシュボードがHTTPSを必要とする場合は、根本原因に対処するために次の手順に進んでください。

#### 3. **URLをHTTPSに更新する**
   - エラーは、Clashダッシュボードが `http://127.0.0.1:9090` からリソースを取得しようとしていることを示唆しています。Clashダッシュボードのソースコードまたは設定にアクセスできる場合：
     - フロントエンドコード（例: `index-5e90ca00.js` または `vendor-827b5617.js`）内のハードコードされた `http://127.0.0.1:9090` 参照を確認してください。
     - Clash coreがHTTPSをサポートしている場合は、これらを `https://127.0.0.1:9090` に更新するか、ブラウザにページと同じプロトコルを使用させるために相対URL（例: `/version`）を使用してください。
     - ソースコードにアクセスできない場合は、リバースプロキシを設定する必要があるかもしれません（ステップ4を参照）。

#### 4. **HTTPSを使用したリバースプロキシを設定する**
   - 混合コンテンツ問題を解決するために、リバースプロキシ（例: NginxまたはCaddyを使用）を設定して、Clash core API（`http://127.0.0.1:9090`）をHTTPS経由で提供することができます。これにより、ダッシュボードはコアと安全に通信できます。
   - **Nginxを使用する手順**:
     1. システムにNginxをインストールする（まだインストールされていない場合）。
     2. `127.0.0.1` 用の自己署名SSL証明書を生成する：
        ```bash
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -subj "/CN=localhost"
        ```
     3. Nginxを設定して、`http://127.0.0.1:9090` へのリクエストをHTTPS経由でプロキシする。設定ファイル（例: `/etc/nginx/sites-available/clash`）を作成する：
        ```nginx
        server {
            listen 443 ssl;
            server_name localhost;

            ssl_certificate /path/to/localhost.crt;
            ssl_certificate_key /path/to/localhost.key;

            location / {
                proxy_pass http://127.0.0.1:9090;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
        ```
     4. 設定を有効にしてNginxを再起動する：
        ```bash
        sudo ln -s /etc/nginx/sites-available/clash /etc/nginx/sites-enabled/
        sudo nginx -t
        sudo systemctl restart nginx
        ```
     5. Clashダッシュボードを更新して、APIリクエストに `http://127.0.0.1:9090` の代わりに `https://localhost:443` を使用するようにする。
     6. ブラウザで、プロンプトが表示されたら自己署名証明書を受け入れる。

   - **Caddyを使用する代替案**: Caddyは設定がより簡単で、HTTPSを自動的に処理します：
     1. Caddyをインストールする。
     2. `Caddyfile` を作成する：
        ```caddy
        localhost:443 {
            reverse_proxy http://127.0.0.1:9090
        }
        ```
     3. Caddyを実行する: `caddy run`。
     4. Clashダッシュボードを更新して、`https://localhost:443` を使用するようにする。

#### 5. **CORS制限を迂回する（上級者向け）**
   - CORSエラー（`XMLHttpRequest cannot load http://127.0.0.1:9090/version due to access control checks`）は、Clash coreサーバーが適切なCORSヘッダーを送信していないことを示しています。Clash coreを制御できる場合：
     - CORSヘッダーを含めるようにClash coreの設定を変更します。例：
       ```yaml
       external-controller: 127.0.0.1:9090
       allow-cors: true
       ```
       （正確な構文はClashのバージョンに依存するため、Clashのドキュメントを確認してください。）
     - あるいは、ステップ4のリバースプロキシ設定で、以下のようなヘッダーを追加することでCORSを処理できます：
       ```nginx
       add_header Access-Control-Allow-Origin "https://clash.razord.top";
       add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
       add_header Access-Control-Allow-Headers "*";
       ```
   - coreを制御できない場合は、ブラウザ拡張機能（例：Chrome用の「CORS Unblock」）を使用して一時的にCORSを迂回できますが、セキュリティ上の理由からこれは推奨されません。

#### 6. **Clashを更新するか、互換性のあるバージョンに切り替える**
   - 外部コントローラーに対するHTTPSサポートに関してバグがあったり、欠けていたりする可能性があるため、Clash for WindowsまたはClash Vergeの最新バージョンを使用していることを確認してください。
   - ClashのGitHubリポジトリ（`github.com/Dreamacro/clash` または `github.com/Fndroid/clash_for_windows_pkg`）で、混合コンテンツやCORSに関連する更新または報告された問題を確認してください。
   - **Clash Verge** または **Clash Meta** への切り替えを検討してください。これらはHTTPSと現代のブラウザセキュリティポリシーをより良くサポートしている可能性があります。[](https://clashverge.net/en/tutorial-en/)

#### 7. **ブラウザで安全でないコンテンツを許可する（非推奨）**
   - 最後の手段として、`https://clash.razord.top/` に対してブラウザで安全でないコンテンツを許可できます：
     - **Chrome**:
       1. アドレスバーの鍵アイコンをクリックします。
       2. 「サイトの設定」 > 「安全でないコンテンツ」 > 「許可」に設定します。
     - **Firefox**:
       1. 鍵アイコンをクリックして「接続設定」に移動します。
       2. 「危険で欺瞞的なコンテンツをブロックする」を一時的に無効にします。
     - **警告**: これはセキュリティ保護を迂回するため、信頼されたネットワーク上のローカルテストにのみ使用してください。
   - あるいは、Chromeを `--disable-web-security` フラグ付きで起動します（開発用のみ）：
     ```bash
     google-chrome --disable-web-security --user-data-dir="/tmp/chrome_dev"
     ```

#### 8. **競合する拡張機能またはファイアウォールを確認する**
   - ブラウザ拡張機能（例: 広告ブロッカー、プライバシーツール）またはファイアウォール設定が、Clashのローカルサーバーを妨害している可能性があります。拡張機能を一時的に無効にするか、ファイアウォールを確認して `127.0.0.1:9090` がアクセス可能であることを確認してください。[](https://vpncentral.com/reddit-blocked-by-network-security/)
   - Windowsでは、Clashアプリにファイアウォールの権限があることを確認します：
     - 設定 > ネットワークとインターネット > Windowsファイアウォール > アプリをファイアウォール経由で許可 に移動します。
     - Clash for Windowsを追加または有効にします。

#### 9. **Clashサポートまたはコミュニティに連絡する**
   - 上記の手順で問題が解決しない場合は、Clash for WindowsのGitHub issuesページ（`github.com/Fndroid/clash_for_windows_pkg/issues`）またはClashコミュニティフォーラムで問題を報告してください。以下の詳細を含めて、あなたの設定に関する情報を提供してください：
     - Clashのバージョン。
     - オペレーティングシステム。
     - 設定ファイル（機密情報は編集してください）。
     - ブラウザとバージョン。
   - このエラーが特定のClashバージョンや設定に特異的である可能性があるため、コミュニティ内の同様の問題を確認してください。[](https://superuser.com/questions/1769163/could-not-switch-to-this-profile-proxy-0-filed-ws-opts-headershost-invalid-c)

---

### 推奨されるアプローチ
最も安全で堅牢な解決策は、**HTTPSを使用したリバースプロキシを設定する**（ステップ4）ことです。これにより、すべてのリクエストがHTTPS経由で提供され、混合コンテンツとCORSの両方の問題が解決します。Clash coreやダッシュボードを変更できない場合は、新しいバージョンのClash（例: Clash Verge）を使用するか、HTTP経由でダッシュボードに一時的にアクセスする（ステップ2）ことがより迅速な回避策となる可能性があります。

---

### 追加の注意点
- カスタムのClashダッシュボードや `clash.razord.top` のようなサードパーティサービスを使用している場合は、それがあなたのClash coreバージョンと互換性があることを確認してください。
- 変更を加える前に、常にClashの設定（`config.yaml`）をバックアップしてください。
- 問題が解決しない場合は、ローカルAPIに対するHTTPSサポートがより優れている可能性がある、v2rayNやOpenVPNのような代替のプロキシクライアントへの切り替えを試すことができます。[](https://stackoverflow.com/questions/67822697/how-to-route-internet-traffic-via-clash-for-windows-ping-from-python-code-is)

Nginxの設定やClash設定のデバッグなど、特定の手順についてヘルプが必要な場合はお知らせください！