---
audio: false
generated: true
image: false
lang: hant
layout: post
title: VS Code 中的 Copilot 聊天指令
translated: true
type: note
---

使用 `code chat "hi"` 指令在 Visual Studio Code（VS Code）中開啟 GitHub Copilot 聊天視窗的功能，與 GitHub Copilot Chat 及其相關功能（例如聊天視圖和相關指令）的整體整合密切相關。根據現有資訊，分析如下：

### `code chat` 指令的發佈情況
雖然提供的 VS Code 發行說明中未明確提及 `code chat` 指令，但它與 GitHub Copilot Chat 功能密切相關，該功能在多個 VS Code 版本中逐步增強。該指令很可能是用於呼叫 Copilot 聊天視圖或內嵌聊氣的別名或簡寫，隨著 Copilot Chat 功能的引入而變得突出。

- **GitHub Copilot Chat 整合**：Copilot Chat 功能（包括聊天視圖）的開發始於 2023 年 8 月左右（VS Code 版本 1.82），並在後續版本（包括 1.99 版，2025 年 3 月）中持續演進。聊天視圖及相關指令（如 `Chat: Open Chat` 或內嵌聊天指令）在此期間被引入並完善。[](https://code.visualstudio.com/updates/v1_93)[](https://code.visualstudio.com/updates/v1_86)
- **指令選擇區與聊天指令**：截至 2024 年 11 月的發行版（版本 1.96），VS Code 已引入從聊天視圖切換到 Copilot Edits 以及改進聊天視圖中的上下文處理等功能，表明對聊天相關指令的穩健支援。透過指令選擇區的指令觸發 Copilot Chat 的功能已經就緒，而 `code chat` 指令很可能作為這些增強功能的一部分而出現。[](https://code.visualstudio.com/updates/v1_96)
- **針對版本 1.99.2**：2025 年 3 月的發行版（版本 1.99）及其更新（1.99.2 和 1.99.3）未明確提及 `code chat "hi"` 指令。然而，它們討論了 Copilot Chat 體驗的進展，例如自訂聊天模式、代理模式以及改進的上下文處理，這表明聊天相關指令在此時已得到良好支援。如果 `code chat` 指令未明確記錄，它很可能作為指令選擇區與 Copilot Chat 整合的一部分而可用。[](https://code.visualstudio.com/updates/v1_99)

### `code chat "hi"` 功能何時發佈？
雖然提供的說明中未明確指出 `code chat "hi"` 指令的具體發佈時間，但考慮到 Copilot Chat 功能的成熟狀態，可以合理推斷該指令在 2025 年 3 月的發行版（版本 1.99）或更早時就已可用。該指令很可能利用了現有的開啟聊天視圖的基礎設施，該設施在版本 1.96（2024 年 11 月）時已透過如 `Chat: Open Chat` 或 `Open Quick Chat` 等指令穩固建立。[](https://code.visualstudio.com/updates/v1_96)[](https://code.visualstudio.com/updates/v1_93)

- **最早可能的發佈時間**：Copilot Chat 功能（包括透過指令開啟聊天視圖的能力）在 2024 年 8 月（版本 1.93）時已顯著發展，具備了快速聊天和上下文改進等功能。`code chat` 指令可能在此時或之後不久作為指令選擇區與 Copilot 整合的一部分而被引入。[](https://code.visualstudio.com/updates/v1_93)
- **針對 1.99.2 版的確認**：截至版本 1.99.2（2025 年 3 月），Copilot Chat 系統已趨成熟，支援自訂模式、代理模式以及如 `#codebase` 等上下文變數。考慮到聊天功能的高級狀態，`code chat "hi"` 指令（用於開啟帶有 "hi" 等提示的聊天視圖）很可能作為指令選擇區中的標準指令受到支援。[](https://code.visualstudio.com/updates/v1_99)

### 結論
用於開啟 Copilot 聊天視窗的 `code chat "hi"` 指令很可能在 2025 年 3 月的發行版（版本 1.99）或更早時就已可用，可能早至 2024 年 8 月（版本 1.93），當時 Copilot Chat 功能得到了顯著增強。具體針對版本 1.99.2，該指令幾乎肯定可以正常運作，因為聊天視圖及相關指令在此時已得到良好整合。如果您需要精確確認，可以在 VS Code 1.99.2 的指令選擇區中輸入 `code chat`，查看它是否作為有效指令出現。

**參考資料**：
- 2025 年 3 月（版本 1.99）- code.visualstudio.com[](https://code.visualstudio.com/updates/v1_99)
- 2024 年 11 月（版本 1.96）- code.visualstudio.com[](https://code.visualstudio.com/updates/v1_96)
- 2024 年 8 月（版本 1.93）- code.visualstudio.com[](https://code.visualstudio.com/updates/v1_93)