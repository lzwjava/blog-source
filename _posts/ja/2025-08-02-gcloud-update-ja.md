---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Google Cloud CLI アップデート
translated: true
type: note
---

% gcloud components update
アップデートを開始しています。この処理には数分かかる場合があります。


現在の Google Cloud CLI バージョンは 507.0.0 です
バージョン 532.0.0 にアップグレードされます

┌─────────────────────────────────────────────────────────────────────────────┐
│                      アップデートされるコンポーネント                      │
├─────────────────────────────────────────────────────┬────────────┬──────────┤
│                         名前                       │   バージョン  │   サイズ  │
├─────────────────────────────────────────────────────┼────────────┼──────────┤
│ BigQuery Command Line Tool                          │     2.1.21 │  1.8 MiB │
│ BigQuery Command Line Tool (Platform Specific)      │     2.1.17 │  < 1 MiB │
│ Cloud Storage Command Line Tool                     │       5.35 │ 12.4 MiB │
│ Cloud Storage Command Line Tool (Platform Specific) │       5.34 │  < 1 MiB │
│ Google Cloud CLI Core Libraries                     │ 2025.07.25 │ 22.1 MiB │
│ Google Cloud CLI Core Libraries (Platform Specific) │ 2025.05.23 │  < 1 MiB │
│ Google Cloud CRC32C Hash Tool (Platform Specific)   │      1.0.0 │  1.4 MiB │
│ gcloud cli dependencies                             │ 2025.04.18 │ 16.1 MiB │
└─────────────────────────────────────────────────────┴────────────┴──────────┘

前回のアップグレード以降、多くの変更が加えられています。最新の完全なリリースノートは、
以下でご覧いただけます：
  https://cloud.google.com/sdk/release_notes

開始後、この操作をキャンセルすると、SDK インストールが不安定な状態になる可能性があります。

続行しますか (Y/n)?  Y

インプレースアップデートを実行中...

╔════════════════════════════════════════════════════════════╗
╠═ ダウンロード中: BigQuery Command Line Tool                  ═╣
╠════════════════════════════════════════════════════════════╣
╠═ ダウンロード中: BigQuery Command Line Tool (Platform Spe... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ ダウンロード中: Cloud Storage Command Line Tool             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ ダウンロード中: Cloud Storage Command Line Tool (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ ダウンロード中: Google Cloud CLI Core Libraries             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ ダウンロード中: Google Cloud CLI Core Libraries (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ ダウンロード中: Google Cloud CRC32C Hash Tool (Platform ... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ ダウンロード中: gcloud cli dependencies                     ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: BigQuery Command Line Tool                 ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: BigQuery Command Line Tool (Platform Sp... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: Cloud Storage Command Line Tool            ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: Cloud Storage Command Line Tool (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: Google Cloud CLI Core Libraries            ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: Google Cloud CLI Core Libraries (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: Google Cloud CRC32C Hash Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ アンインストール中: gcloud cli dependencies                    ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: BigQuery Command Line Tool                   ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: BigQuery Command Line Tool (Platform Spec... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: Cloud Storage Command Line Tool              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: Cloud Storage Command Line Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: Google Cloud CLI Core Libraries              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: Google Cloud CLI Core Libraries (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: Google Cloud CRC32C Hash Tool (Platform S... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ インストール中: gcloud cli dependencies                      ═╣
╚════════════════════════════════════════════════════════════╝

ポスト処理ステップを実行中...完了しました。

アップデートが完了しました！

CLI を以前のバージョンに戻すには、以下を実行できます：
  $ gcloud components update --version 507.0.0