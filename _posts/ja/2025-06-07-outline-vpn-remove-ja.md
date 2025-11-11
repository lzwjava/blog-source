---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのOutline VPNクライアントの削除
translated: true
type: note
---

`apt`が`outline-client`という名前のパッケージを見つけられないようです。これは通常、次の2つのいずれかを意味します：

1.  **`apt`を使用してOutlineをインストールしていない（つまり、.debパッケージとしてインストールされていない）。** これは、多くのユーザーがAppImage経由でインストールするため、Outlineでこのエラーが発生する最も一般的な理由です。
2.  **パッケージ名が異なるか、リポジトリが設定されていない。** Outlineでは可能性は低いですが、他のソフトウェアでは可能性があります。

以前の試行を考慮すると、**AppImage**としてインストールした可能性が非常に高いです。この場合、手動で削除する必要があります。

以下の手順に従ってください：

**1. AppImageファイルを見つけて削除する：**

AppImageとしてインストールされたOutlineクライアントは、通常、単一の実行可能ファイルです。`Downloads`フォルダにダウンロードしたか、ホームディレクトリ内の`bin`や`Applications`フォルダに移動した可能性があります。

*   **確認すべき一般的な場所：**
    *   `~/Downloads/`
    *   `~/Applications/`（作成した場合）
    *   `~/bin/`（作成した場合）
    *   最初に実行したディレクトリ。

*   **見つけ方：** `find`コマンドを使用してホームディレクトリ内を検索できます：
    ```bash
    find ~ -name "Outline-Client*.AppImage" 2>/dev/null
    ```
    このコマンドは、ホームディレクトリ内で「Outline-Client」で始まり「.AppImage」で終わるファイルを検索します。
    見つかったら削除します：
    ```bash
    rm /path/to/Outline-Client.AppImage
    ```
    （`/path/to/`を`find`コマンドで見つかった実際のパスに置き換えてください。）

**2. 残った設定ファイルと自動起動ファイルを削除する：**

AppImageを削除しても、Outlineが設定ファイルと自動起動エントリを作成している可能性があります。

*   **設定ディレクトリを削除する：**
    ```bash
    rm -rf ~/.config/Outline/
    ```
    このコマンドは、ユーザーの設定フォルダ内の`Outline`ディレクトリ全体を削除します。

*   **自動起動エントリを削除する（作成されていた場合）：**
    Outlineがログイン時に自動起動するように設定されていた場合、そのための`.desktop`ファイルがある可能性があります。
    ```bash
    rm -f ~/.config/autostart/Outline-Client.AppImage.desktop
    ```

*   **デスクトップアイコンを削除する（もしあれば）：**
    場合によっては、AppImageがローカルのアイコンディレクトリにデスクトップアイコンを作成することがあります。
    ```bash
    find ~/.local/share/icons -name "appimagekit-outline-client*.png" -delete
    ```
    これにより、Outline AppImageに関連するPNGアイコンが削除されます。

**3. ネットワーク設定を確認して復元する（必要に応じて）：**

Outlineは他のVPNと同様に、DNS設定を変更することがあります。AppImageを削除した後にインターネット接続の問題が発生した場合は、`/etc/resolv.conf`ファイルを確認してください。

*   **`resolv.conf`を検査する：**
    ```bash
    cat /etc/resolv.conf
    ```
    Outlineによって追加されたと思われる行（例えば、ルーターやISPのDNSとして認識されない特定のネームサーバーのIPアドレス）を探します。

*   **`resolv.conf`を復元する（必要な場合）：**
    Outlineが変更したように見える場合：
    *   **オプションA（最新のUbuntuで推奨）：** システムが`systemd-resolved`を使用している場合（最近のUbuntuバージョンで一般的）、通常はシンボリックリンクを再作成することで修正できます：
        ```bash
        sudo rm /etc/resolv.conf
        sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
        ```
    *   **オプションB（手動編集 - オプションAが機能しない場合や古いシステムで使用）：**
        まず、バックアップを作成します：
        ```bash
        sudo cp /etc/resolv.conf /etc/resolv.conf.bak
        ```
        次に、ファイルを編集します：
        ```bash
        sudo nano /etc/resolv.conf
        ```
        Outlineによって追加された`nameserver`行をコメントアウトするか削除します。ISPのDNSがわからない場合は、通常、Googleの公開DNS（`8.8.8.8`と`8.8.4.4`）やCloudflareのDNS（`1.1.1.1`と`1.0.0.1`）を入力できます。

**4. システムを再起動する：**

これらの手順を完了した後、すべての変更が有効になり、Outlineに関連するバックグラウンドプロセスが完全に終了するように、Ubuntuシステムを再起動することを強くお勧めします。

```bash
sudo reboot
```

これらの手動削除手順に従うことで、UbuntuシステムからOutline VPNクライアントを完全に削除できるはずです。