---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 'オープンソースツール: Auto SS Config'
translated: true
---

**Auto SS Config**というツールをオープンソース化したことを発表できることを嬉しく思います。このツールは、ShadowsocksのURLからShadowsocksまたはClashのサブスクリプションURLを自動生成し、アップロードするもので、プロキシサーバーの設定を管理・更新するのがより簡単になります。

このツールは、特にShadowsocksサーバーがブロックされたときに、私にとって革命的な存在でした。Outline Managerを使用して新しいサーバーを作成し、新しいアドレスを取得し、このURLをMacアプリを使って直接インポートすることで、GFWの制限を回避しています。このプロジェクトから`python upload_configs.py`を実行することで、サブスクリプションURLが更新され、すべてのデジタルデバイスが機能的なネットワーク接続を維持できるようになります。

## 機能

- **Shadowsocks URLをClash設定に変換**: 異なるプロキシ設定を簡単に切り替えられます。
- **複数のShadowsocksサーバーをサポート**: 複数のサーバーを簡単に管理できます。
- **設定をGoogle Cloud Storageに自動アップロード**: 設定を安全に保管し、いつでもアクセス可能にします。
- **設定を公開可能にする**: 設定を他の人と共有できます。
- **キャッシュコントロールを使用して即時更新を実現**: 設定が常に最新であることを保証します。

## ファイル

- `app_config_tmp.yaml`: アプリケーション設定（バケット名、SS URL）。
- `clash_config_tmp.yaml`: 一時的なClash設定ファイル。
- `upload_configs.py`: Clash設定を生成し、設定をGoogle Cloud Storageにアップロードするスクリプト。
- `requirements.txt`: Pythonの依存関係。

## セットアップ

1. **依存関係をインストール**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Google Cloudの認証情報を設定**:
    - Google Cloud SDKをインストールします。
    - `gcloud auth application-default login` を実行します。
    - または、`GOOGLE_APPLICATION_CREDENTIALS` 環境変数を設定します。

3. **`app_config_tmp.yaml` を `app_config.yaml` にコピーして設定する**:
    ```yaml
    bucket_name: your-bucket-name
    ss_urls:
        - ss://method:password@server:port
    ```

## 使用方法

1. **`app_config.yaml` の `ss_urls` リストに Shadowsocks の URL を追加する**:
    ```yaml
    ss_urls:
        - ss://method:password@server:port
    ```

2. **設定ファイルのアップロード**:
    ```bash
    python upload_configs.py
    ```

    スクリプトは、両方の設定に対する公開URLを出力します。

## 開発

- **Python 3.6以上**
- YAML処理には`ruamel.yaml`を使用します。
- GCS操作には`google-cloud-storage`を使用します。

## ライセンス

MIT（マサチューセッツ工科大学）

---

詳細や貢献については、ぜひ[リポジトリ](https://github.com/lzwjava/auto-ss-config)をチェックしてください！