---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Google Cloud CLI 更新
translated: true
type: note
---

% gcloud components update
開始更新。此過程可能需要幾分鐘時間。

您目前的 Google Cloud CLI 版本是：507.0.0
您將升級至版本：532.0.0

┌─────────────────────────────────────────────────────────────────────────────┐
│                      即將更新以下元件。                      │
├─────────────────────────────────────────────────────┬────────────┬──────────┤
│                         名稱                         │    版本    │   大小   │
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

自上次升級以來已有許多變更。如需查看最新完整版本說明，
請瀏覽：
  https://cloud.google.com/sdk/release_notes

一旦開始，取消此操作可能會導致您的 SDK 安裝處於不一致狀態。

是否要繼續 (Y/n)?  Y

正在執行就地更新...

╔════════════════════════════════════════════════════════════╗
╠═ 下載中：BigQuery Command Line Tool                  ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 下載中：BigQuery Command Line Tool (Platform Spe... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 下載中：Cloud Storage Command Line Tool             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 下載中：Cloud Storage Command Line Tool (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 下載中：Google Cloud CLI Core Libraries             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 下載中：Google Cloud CLI Core Libraries (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 下載中：Google Cloud CRC32C Hash Tool (Platform ... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 下載中：gcloud cli dependencies                     ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：BigQuery Command Line Tool                 ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：BigQuery Command Line Tool (Platform Sp... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：Cloud Storage Command Line Tool            ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：Cloud Storage Command Line Tool (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：Google Cloud CLI Core Libraries            ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：Google Cloud CLI Core Libraries (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：Google Cloud CRC32C Hash Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 解除安裝中：gcloud cli dependencies                    ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：BigQuery Command Line Tool                   ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：BigQuery Command Line Tool (Platform Spec... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：Cloud Storage Command Line Tool              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：Cloud Storage Command Line Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：Google Cloud CLI Core Libraries              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：Google Cloud CLI Core Libraries (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：Google Cloud CRC32C Hash Tool (Platform S... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ 安裝中：gcloud cli dependencies                      ═╣
╚════════════════════════════════════════════════════════════╝

正在執行後處理步驟...完成。

更新完成！

若要將 CLI 還原至先前安裝的版本，您可以執行：
  $ gcloud components update --version 507.0.0