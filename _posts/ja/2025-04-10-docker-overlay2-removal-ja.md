---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Docker Overlay2削除エラーの解決
translated: true
type: note
---

このエラーは、Dockerがコンテナのoverlay2ファイルシステムを削除できなかったことを意味します — カーネル/VMが低レベルI/Oエラー（`readdirent merged: bad message`）を返しました。macOSでは、通常Docker VMまたはoverlayストレージが不正な状態になっている場合に発生します。以下は、回復するために試せる安全で段階的な手順です（破壊的でないものからより積極的なものへ）。

**重要:** 以下のいくつかのコマンドはデータ（イメージ/ボリューム）を削除する可能性があります。破壊的な手順には印を付け、必要に応じてコピー/ペーストできるように正確なコマンドを示します。

---

# クイックチェック（安全）

ターミナルで以下を実行:

```bash
# コンテナのステータスと問題のあるコンテナIDを表示
docker ps -a --no-trunc | grep ccd89a3f36a1528cb923c90de8755faeb36e229c || true

# コンテナの強制削除を試みる
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

`docker rm -f` が成功したら完了です。同じoverlayエラーで失敗した場合は、続行してください。

---

# Dockerの再起動（macOS Docker Desktop） — 推奨される次のステップ（安全）

Docker Desktopを完全に終了し（クジラアイコン → Quit）、再度起動します。またはコマンドラインから:

```bash
# macOS — AppleScript経由でDocker Desktopを再起動
osascript -e 'quit app "Docker"'
open -a Docker
```

Dockerが再起動した後、`docker compose down` または `docker rm -f <id>` を再度試してください。

---

# ホストの再起動（非常に安全）

再起動が可能な場合、macOSをリブートするとVMファイルシステムの問題が解決されることが多いです:

* Macを再起動し、Docker Desktopを起動して再試行してください。

---

# まだ失敗する場合 — Docker Desktopのトラブルシューティングアクションを使用（安全 / 中程度）

Docker Desktop → Troubleshoot を開く:

* **Restart Docker** をクリック（まだ行っていない場合）。
* それでも失敗する場合は、**Clean / Purge data** または **Reset to factory defaults** を試してください — **警告**: これらはイメージ/コンテナ/ボリュームを削除します。ローカルのDockerデータを失っても問題ない場合にのみ使用してください。

---

# Docker Engine（Linux）を使用している場合、または手動クリーンアップに慣れている場合（破壊的）

**データ損失のリスクを理解している場合のみ実行してください。** Dockerデーモンを停止し、問題のあるIDのoverlay2ディレクトリを削除してから、Dockerを再起動します。

```bash
# dockerデーモンを停止（Linux）
sudo systemctl stop docker

# まずoverlay2フォルダをバックアップ（オプション、空き容量がある場合）
sudo cp -a /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f /root/overlay2-backup-7acbf095

# バックアップが完了した/不要な場合、そのoverlayのmergedディレクトリを削除:
sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f

# （オプション）必要に応じてコンテナメタデータを削除
# 警告: 壊れたコンテナに対応するファイルであると確信できるもののみ削除してください
sudo rm -rf /var/lib/docker/containers/ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18

# dockerを起動
sudo systemctl start docker

# その後、ダングリングアイテムをクリーンアップしてみてください
docker system prune -a --volumes
```

繰り返します: `/var/lib/docker` 配下のファイルを削除することは破壊的であり、誤って行うと他のコンテナを破壊する可能性があります。削除する内容を理解している場合にのみ使用してください。

---

# 多くの場合役立つ、破壊的でないクリーンアップ

overlayを直接削除できない場合、またはより穏やなアプローチを希望する場合:

```bash
# 未使用オブジェクトのプルーンを試みる
docker system prune -f
docker volume prune -f

# 未使用のイメージ/コンテナを削除（注意）
docker image prune -a -f
docker container prune -f
```

これにより空き容量が増え、Dockerが削除操作を正常に再実行できるようになることがあります。

---

# 問題が再発し、Docker Desktop for Macを使用している場合

* Docker VMのディスクサイズを増やすことを検討してください（Settings → Resources → Disk image size）。
* 重要なローカルデータに依存している場合は、Reset/Purgeを使用する前にまずボリューム/コンテナをエクスポートしてください（`docker export`, `docker save`）。

---

# 収集する診断情報（さらにヘルプが必要な場合）

上記のいずれでも修正されない場合は、以下の（非破壊的な）コマンドの出力を共有してください。対象を絞った次のステップを提案します:

```bash
docker info
docker ps -a
docker compose version
docker version
# overlayディレクトリをリスト（Linux）
ls -lah /var/lib/docker/overlay2 | head -n 40
```

（macOS Docker Desktopを使用している場合、`ls /var/lib/docker` はVMの内容を表示しません — Docker Desktopの再起動またはTroubleshoot UIの使用を優先してください。）

---

希望する場合は、**Docker Desktop on macOS**（最も可能性が高い）または**Docker Engine on Linux**のどちらを実行しているか教えてください — 短く、適切な手順を提供します。希望に応じて、順番に実行できるワンラインチェックリストを作成することもできます。