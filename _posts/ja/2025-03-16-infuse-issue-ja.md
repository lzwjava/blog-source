---
audio: false
generated: true
lang: ja
layout: post
title: 注入の問題
translated: true
type: note
---

Infuseで「Failed to open input stream in demuxing stream」エラーが発生する場合、通常はアプリがストリーミングしようとしている動画ファイルに適切にアクセスまたは処理できないことを示しています。Nginxサーバー（例: `http://192.168.1.27/movies/yourfile.mkv`）から`.mkv`ファイルをストリーミングしており、VLCでは動作するがInfuseでは動作しない場合、ネットワークの問題、ファイルの互換性、またはInfuse特有の特性が原因である可能性があります。以下はトラブルシューティングと修正方法です：

### 1. ネットワーク接続の確認
Infuseでは、ネットワークの中断や設定ミスがこのエラーの原因となることがよくあります。
- **アクセシビリティのテスト**: iPad（またはInfuseが実行されているデバイス）からURLが機能することを確認してください：
  - Safariを開き、`http://192.168.1.27/movies/`にアクセスします。ファイルリストが表示されるはずです。
  - `yourfile.mkv`をタップします。再生されないかもしれませんが、リンクにアクセスできることを確認してください。
- **サーバーのping**: iPadで**Network Ping Lite**（App Storeで無料）などのアプリを使用して`192.168.1.27`にpingを実行します。失敗する場合は、Wi-Fiまたはサーバーのファイアウォールを確認してください。
- **ファイアウォールの確認**: Ubuntuサーバーで：
  ```bash
  sudo ufw status
  ```
  ポート80が開放されていることを確認します（`80/tcp ALLOW`）。そうでない場合は：
  ```bash
  sudo ufw allow 80
  sudo systemctl restart nginx
  ```

### 2. Infuseとデバイスの再起動
一時的な不具合がこのエラーを引き起こす可能性があります。
- **Infuseを閉じる**: ホームボタンをダブルタップ（または新しいiPadでは上にスワイプ）し、Infuseをスワイプして閉じます。
- **再起動**: Infuseを起動し、ストリームを再試行します。
- **iPadの再起動**: 電源ボタンを長押しし、スライドで電源をオフにしてから再起動します。再度テストします。

### 3. ファイルの互換性を確認
Infuseは`.mkv`をサポートしていますが、エラーはファイルのコーデックまたは構造に関連している可能性があります。
- **別のファイルをテスト**: 小さな既知の動作する`.mkv`ファイル（例: H.264ビデオとAACオーディオでエンコードされたもの）を`/var/www/movies/`にアップロードします：
  ```bash
  sudo mv /path/to/testfile.mkv /var/www/movies/
  sudo chown www-data:www-data /var/www/movies/testfile.mkv
  sudo chmod 644 /var/www/movies/testfile.mkv
  ```
  Infuseで`http://192.168.1.27/movies/testfile.mkv`のストリーミングを試みます。
- **コーデックの確認**: VLCで再生できるため、ファイルはストリーミング可能ですが、Infuseはまれなコーデック（例: VP9、Opus）に対応できない可能性があります。MacでVLCを使用して検査します：
  - `.mkv`を開き、`Cmd + I`（ツール > コーデック情報）を押し、ビデオ/オーディオコーデックをメモします。
  - H.264/AACでない場合は、HandBrake（無料、handbrake.fr）で再エンコードします：
    - `.mkv`を読み込み、「H.264 (x264)」ビデオと「AAC」オーディオを選択して変換します。

### 4. Nginx設定の調整
Infuseはスムーズなストリーミングに特定のヘッダーまたは設定を必要とする可能性があります。
- **設定の更新**: Nginxファイル（例: `/etc/nginx/sites-enabled/default`）を編集します：
  ```nginx
  server {
      listen 80;
      server_name 192.168.1.27 localhost;

      location /movies/ {
          alias /var/www/movies/;
          autoindex on;
          add_header Accept-Ranges bytes;  # 範囲リクエストが機能することを保証
          add_header Content-Disposition "inline";  # ストリーミングを支援
      }
  }
  ```
- **再読み込み**:
  ```bash
  sudo nginx -t
  sudo systemctl reload nginx
  ```
- **理由**: `Accept-Ranges`は、Infuseがファイルの一部をリクエストできることを保証します（ストリーミングに重要）。

### 5. 診断レポートの送信
Infuseの開発者は、持続的な問題に対してこれを推奨しています。
- **手順**:
  1. Infuseで**設定 > 一般**に移動します。
  2. **診断レポートを送信**をタップします。
  3. 表示されるコードをメモします。
  4. [Firecoreコミュニティフォーラム](https://community.firecore.com/)にアクセスし、コードを投稿し、設定（Nginx、`.mkv`、HTTPストリーミング）を説明します。
- **理由**: 開発者はバグまたは設定の問題を特定できます。

### 6. 代替の回避策
Infuseが引き続き失敗する場合：
- **VLCを使用**: iPadでVLC for Mobileを使用します（信頼性が高いため）。
- **アプリの切り替え**: 同じURLで**nPlayer**または**PlayerXtreme**（App Store）を試します。

### 考えられる原因
VLCで問題なくストリーミングできるため、ネットワークの不具合またはInfuseのHTTPストリームに対する厳格な処理が原因である可能性が高いです。Nginxの調整（ステップ4）とテストファイル（ステップ3）で解決することがよくあります。それでも解決しない場合は、診断レポートが明確にするでしょう。

これらの対策を試した後の結果（特にログエラーや診断コード）を教えてください！