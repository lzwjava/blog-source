---
audio: false
generated: true
image: false
lang: ja
layout: post
model: google/gemini-2.5-flash
title: macOSでのDocker OverlayFS破損の修正
translated: true
type: note
---

表示されているエラー `driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/.../merged: readdirent merged: bad message` は、操作が中断されたり、ホストマシンのファイルシステムに問題があったりしたことが原因で発生する、Dockerのストレージメカニズム (OverlayFS) の深刻な破損を示しています。

あなたは **macOS** 上で (Docker Desktop を実行しています。Docker デーモンとそのストレージは、専用の **Linux 仮想マシン (VM)** 内で管理されています。ネイティブの Linux のように `/var/lib/docker/overlay2` に直接アクセスすることはできないため、Docker Desktop アプリ自体に焦点を当てることで、修正をより簡単かつ安全に行うことができます。

以下は、macOS でこの問題を解決するための最も安全で効果的な手順です。

-----

## 1. コンテナの強制停止と強制削除

失敗したコンテナは `chat-mongodb` (ID: `ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18`) です。まず、その名前または ID を使用して強制削除を試みます。

1.  **スタック全体を停止** します (ロックを保持しているバックグラウンドプロセスがないようにするため):

    ```bash
    docker compose stop
    ```

2.  **`-f` フラグを使用して特定のコンテナを強制削除** します:

    ```bash
    docker rm -f chat-mongodb
    # または ID を使用:
    # docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
    ```

3.  **元のコマンド** (`docker compose down` または同等のもの) を再度実行してみてください。エラーが解消しない場合は、ステップ 2 に進んでください。

-----

## 2. Docker Desktop の再起動

単純な再起動により、内部 VM 内の一時的なロック問題や破損状態が解消されることがよくあります。

### オプション A: メニューバーを使用 (推奨)

1.  macOS のメニューバーにある **Docker のクジラアイコン** をクリックします。
2.  **Restart** を選択します。

### オプション B: ターミナルを使用

アプリケーションを強制終了して再起動できます:

```bash
killall Docker && open /Applications/Docker.app
```

Docker が再起動した後、完全に起動するまで約 30 秒待ってから、元のコマンドを再度実行してみてください。

-----

## 3. Docker のキャッシュと未使用データのクリア (Prune)

再起動で問題が解決しない場合、強力なクリーンアップコマンドを実行すると、未使用または「ダングリング」状態のコンポーネント (エラーの原因である可能性がある) を削除することで、より深い破損問題が解決されることがよくあります。

**警告:** このコマンドは、すべての停止済みコンテナ、未使用のネットワーク、ダングリングイメージを削除します。停止した状態のまま保持したいコンテナがある場合は、それらをバックアップするか、このステップをスキップしてください。

ターミナルで次のコマンドを実行します:

```bash
docker system prune -a --volumes
```

  * **`-a`** (all) は、(ダングリングなものだけでなく) すべての未使用のイメージを削除します。
  * **`--volumes`** は、未使用の匿名ボリューム (`overlay2` 破損の原因である可能性がある) を削除します。

確認を求められます。`y` と入力して Enter キーを押してください。Prune が完了した後、元のコマンドを再度実行してみてください。

-----

## 4. Docker Desktop の工場出荷時設定へのリセット

これは **最終手段** です。これにより **すべてのコンテナ、イメージ、ボリュームが削除** されます (マウントされていないボリュームに保存したローカルデータも含む)。内部の Docker VM を完全に新規作成して強制的に再起動します。

1.  macOS のメニューバーにある **Docker のクジラアイコン** をクリックします。
2.  **Settings (または Preferences)** $\rightarrow$ **Troubleshoot** に進みます。
3.  **Reset to factory settings...** をクリックします。

リセット後、Docker はまっさらな状態で再起動します。その後、`docker compose up` コマンドを実行して環境を再構築できるはずです。