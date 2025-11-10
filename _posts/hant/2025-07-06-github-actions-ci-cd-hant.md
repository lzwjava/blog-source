---
audio: false
generated: true
lang: hant
layout: post
title: GitHub Actions：持續整合與持續交付的演進
translated: true
type: note
---

GitHub Actions 是一個強大的**持續整合與持續交付 (CI/CD) 平台**，直接整合於 GitHub 中。它讓開發者能夠自動化軟體開發工作流程的各個階段，從程式碼建置、測試到應用程式部署皆涵蓋在內。

### 發展歷程與發布時間

GitHub 本身成立於 **2007 年**，其網站於 **2008 年 4 月**正式上線。GitHub 平台的開發始於 **2005 年 10 月**，由 Tom Preston-Werner、Chris Wanstrath、P. J. Hyett 與 Scott Chacon 共同正式發布。

而作為特定 CI/CD 平台的 GitHub Actions，最初於 **2018 年 10 月**對外公布，並在 **2019 年 11 月**正式全面推出。它的演進源自 GitHub 的核心使命：為開發者提供能簡化協作與自動化的工具。

### 使用者數量

雖然很難確切統計 GitHub Actions 的即時*使用者*數量，但值得注意的是，**截至 2023 年初，GitHub 本身已擁有超過 1 億名開發者**。考慮到 GitHub Actions 的深度整合以及市場對 CI/CD 日益增長的需求，其中相當大比例的使用者都在其專案中運用 GitHub Actions。從新創公司到大型企業，許多開發團隊跨足各行業皆採用此平台。

### 哪些儲存庫廣泛使用 Actions？

GitHub Actions 的定義位於個別儲存庫內，通常置於 `.github/workflows` 目錄中。廣泛使用 GitHub Actions 的儲存庫通常包括：

* **官方 GitHub Actions 儲存庫：** GitHub 上的 `github/actions` 組織包含許多核心與常用動作，例如 `actions/checkout`、`actions/setup-python`、`actions/setup-node`、`actions/upload-artifact` 及 `actions/download-artifact`。這些是許多工作流程的基礎組件。
* **大型開源專案：** 跨多種程式語言（如 Python、JavaScript、Go、C++ 等）的主要開源專案，大量運用 GitHub Actions 來執行建置、測試與發布流程。實例常包含來自 Google、Microsoft 等科技巨頭的專案，以及熱門的框架與函式庫。
* **專注於自動化與 DevOps 的專案：** 展示 DevOps 實踐、自動化基礎設施、測試或部署等各方面的儲存庫，自然會具備豐富的 GitHub Actions 工作流程集合。
* **熱門儲存庫：** 當前 GitHub 上的許多熱門儲存庫（可在 GitHub 的 trending 頁面找到），常展示 GitHub Actions 的創新應用，例如內容生成、安全掃描或自動化發布等。

本質上，任何能透過自動化流程提升程式碼品質、測試、部署或儲存庫管理效益的專案，皆適合建置健全的 GitHub Actions 組態。