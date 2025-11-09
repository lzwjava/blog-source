---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ubuntuプロキシバイパスホスト設定
translated: true
type: note
---

### Ubuntuの手動プロキシ設定で複数のホストを設定する

Ubuntuの手動プロキシ設定（**設定 > ネットワーク > ネットワークプロキシ > 手動**）では、「無視するホスト」フィールドでセミコロン区切りのホスト、ドメイン、またはIP範囲を指定してプロキシをバイパスできます。これはlocalhostや内部ネットワークなどのローカルトラフィックに一般的に使用されます。これらを*プロキシサーバー*アドレス（単一のホスト:ポートを想定）として設定することはできませんが、「無視するホスト」には完全に適合します。

#### GUIでの設定手順:
1. **設定**を開く（アクティビティ概要で検索）
2. **ネットワーク > ネットワークプロキシ**に移動
3. 方法を**手動**に設定
4. **無視するホスト**フィールドに、セミコロン区切りでリストを入力（周囲にスペースなし）:
   ```
   localhost;127.0.0.1;192.168.1.1;192.168.2.1;::1
   ```
   - `localhost`: ループバックアドレスに解決
   - `127.0.0.1`: IPv4ループバック
   - `192.168.1.1` と `192.168.2.1`: 特定のローカルIP（必要に応じて追加）
   - `::1`: IPv6ループバック

5. **適用**をクリックして保存。システム全体に適用されます（ブラウザ、aptなどのアプリに影響）

#### `192.168.1.*`のようなワイルドカードの使用:
- 直接的なワイルドカード（例: `192.168.1.*`）は「無視するホスト」フィールドで**サポートされていません**—このフィールドは正確なホスト、ドメインサフィックス（例: `*.local`）、またはIP範囲のCIDR表記用に設計されています
- 代わりに範囲指定には**CIDR表記**を使用:
  - `192.168.1.*`（192.168.1.0/24サブネット内の全IP）の場合、`192.168.1.0/24`を使用
  - 更新された例:
    ```
    localhost;127.0.0.1;::1;192.168.1.0/24;192.168.2.1
    ```
  - より広範なローカルネットワークには、`10.0.0.0/8;172.16.0.0/12;192.168.0.0/16`（一般的なプライベート範囲）を追加

#### コマンドライン代替案（スクリプト化や精密設定用）:
ターミナルを使用する場合（または自動化が必要な場合）、`gsettings`（現代のUbuntu）を使用するか、システム全体用に`/etc/environment`を編集:
- 現在の無視リストを表示:
  ```
  gsettings get org.gnome.system.proxy ignore-hosts
  ```
- リストを設定（値を置き換え）:
  ```
  gsettings set org.gnome.system.proxy ignore-hosts "['localhost', '127.0.0.1', '::1', '192.168.1.0/24', '192.168.2.1']"
  ```
- 恒久的な環境変数用（一部のアプリに影響）: `/etc/environment`に追加:
  ```
  no_proxy="localhost,127.0.0.1,::1,192.168.1.0/24,192.168.2.1"
  ```
  その後再起動するか、`source /etc/environment`を実行

リストされたホストへのpingやブラウザでのプロキシ動作確認でテスト。問題が発生した場合（特定のアプリで）、環境変数メソッドがより広範囲をカバーすることが多いです。

[Setting up proxy to ignore all local addresses](https://askubuntu.com/questions/11274/setting-up-proxy-to-ignore-all-local-addresses)  
[How to Configure Proxy Settings on Ubuntu](https://phoenixnap.com/kb/ubuntu-proxy-settings)  
[Set a network range in the no_proxy environment variable](https://unix.stackexchange.com/questions/23452/set-a-network-range-in-the-no-proxy-environment-variable)