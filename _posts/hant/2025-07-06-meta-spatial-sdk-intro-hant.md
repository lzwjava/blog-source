---
audio: false
generated: true
lang: hant
layout: post
title: Meta Spatial SDK：從 Android 到 XR
translated: true
type: note
---

**Meta Spatial SDK** 對於希望為 Meta VR/MR 頭戴裝置（特別是運行 **Meta Horizon OS** 的裝置，例如 Meta Quest 系列）打造沉浸式應用程式的開發者而言，是一項革命性的工具。其核心目的在於彌補傳統 Android 行動應用程式開發與空間計算獨特能力之間的差距。

以下是 Meta Spatial SDK 的簡要介紹：

**它是什麼？**

Meta Spatial SDK 是一個全新框架，讓 Android 開發者能夠運用現有技能、工具與函式庫（例如 Android Studio 與 Kotlin），在 Meta Quest 裝置上創造豐富、沉浸的混合實境體驗。在此 SDK 推出之前，為 Quest 開發應用通常需使用 Unity 或 Unreal 等完整遊戲引擎，這對行動優先的開發者而言可能是一大門檻。

**主要目標與優勢：**

* **普及 XR 開發**：降低了行動開發者的進入門檻，讓更廣泛的創作者能為空間計算進行開發。
* **活用現有技能**：開發者可運用熟悉的 Android 開發環境，減少學習曲線並加速開發流程。
* **將 2D 應用延伸至 3D**：讓開發者能將現有 2D Android 應用移植至 Meta Horizon OS，並以 3D 元素、混合實境功能與空間互動進行強化。
* **快速迭代**：SDK 提供高速工作流程，實現空間概念的快速原型設計、建置與測試。
* **提升使用者體驗**：協助打造超越傳統平面螢幕的應用，提供 3D 渲染、影像穿透、手部追蹤、空間音訊與物理效果等功能，實現更引人入勝的互動。

**核心能力與功能：**

* **原生 Android 開發**：基於 Kotlin 建構，可與 Android 生態系統無縫整合。
* **混合實境功能**：透過穿透式攝影機（Camera2 API）的存取權限，實現虛擬內容與現實世界的融合。
* **3D 渲染**：支援現代化圖形管線，包含 GLTF 模型、物理基礎渲染（PBR）、動畫與剛體物理。
* **互動式面板**：能在 3D 環境中建立 2D UI 面板，並使用 Jetpack Compose 等熟悉的 Android UI 框架進行構建。
* **輸入與互動**：提供手部追蹤、控制器輸入及其他自然使用者互動的 API。
* **場景理解**：讓開發者能存取使用者實體環境的相關數據。
* **空間音訊**：提供整合空間化音效的工具，以增強沉浸感。
* **Meta Spatial Editor**：一款輔助工具，讓開發者無需使用完整的遊戲引擎編輯器，即可在空間應用程式中視覺化地排列與組合 2D 及 3D 元素。
* **實體-組件-系統（ECS）**：SDK 內部使用的架構模式，用於建構模組化且高效能的空間應用程式。

總而言之，Meta Spatial SDK 讓 Android 開發者能輕鬆踏入虛擬與混合實境的世界，將傳統行動應用轉化為在 Meta Quest 裝置上引人入勝的空間體驗。