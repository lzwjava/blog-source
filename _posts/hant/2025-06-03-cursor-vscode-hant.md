---
audio: false
generated: true
lang: hant
layout: post
title: Cursor 與 VS Code
translated: true
type: note
---

是的，Cursor 對 Visual Studio Code（VS Code）進行分支並以此建立商業模式是合法的，前提是他們遵守 VS Code 原始碼發布所依據的 MIT 許可證條款。MIT 許可證具有高度寬容性，允許任何人使用、複製、修改、合併、發布、分發、再許可及銷售軟體副本，只要在所有副本或軟體的實質部分中包含原始版權聲明和許可聲明即可。

以下是關於 Cursor 分支合法性的關鍵要點：

1. **MIT 許可證合規性**：在 GitHub 儲存庫 `vscode` 中提供的 VS Code 原始碼是根據 MIT 許可證授權的。這允許 Cursor 對程式碼庫進行分支、修改並用於商業目的，包括建立閉源產品，只要他們在其分發中包含原始的 MIT 許可證和版權聲明。MIT 許可證不要求分支項目必須保持開源，因此 Cursor 可以合法地使其產品成為專有軟體。

2. **Visual Studio Code 與 Code-OSS 的區別**：開源的 `vscode` 儲存庫（通常稱為 Code-OSS）與 Microsoft 品牌的 Visual Studio Code 產品之間存在區別。Microsoft 品牌的 VS Code 包含專有附加功能（例如遙測數據、市場整合），並根據不同的許可證進行分發。然而，對根據 MIT 許可證授權的開源 `vscode` 儲存庫進行分支，正是 Cursor 及類似項目（如 Windsurf）所採取的做法。這是明確允許的，他們可以在其基礎上建立自己的自訂功能。

3. **Visual Studio Marketplace 限制**：像 Cursor 這樣的分支面臨的一個重要限制是，由於 Microsoft 的服務條款，它們無法存取官方的 Visual Studio Marketplace。這意味著 Cursor 無法提供與 VS Code 相同的擴充功能生態系統，除非他們建立替代的擴充功能註冊表（例如 OpenVSX）或開發自己的擴充功能。此外，一些專有擴充功能（例如 GitHub Copilot 或 Microsoft 的 C/C++ 擴充功能）僅限於 Microsoft 官方的 VS Code 版本使用，這可能會限制分支的功能。

4. **道德與社群顧慮**：雖然根據 MIT 許可證進行分支是合法的，但有些人對像 Cursor 這樣的公司取得開源項目、添加功能並將其作為專有產品銷售，卻未回饋原始 VS Code 社群的做法提出了道德質疑。例如，X 平台上的貼文表達了複雜的情緒，部分用戶質疑 Cursor 從主要由 VS Code 團隊開發的程式碼中獲利是否公平。然而，這屬於道德辯論而非法律問題，且 MIT 許可證明確允許此類使用。

5. **Microsoft 的回應**：Microsoft 已採取措施保護其生態系統，例如限制分支對市場的存取及專有擴充功能的使用，這從諸如從非官方版本中移除 C/C++ 擴充功能支援等行動中可見一斑。然而，這些限制並不影響對 `vscode` 儲存庫本身進行分支的合法性，只要分支符合 MIT 許可證的要求。

總而言之，Cursor 對 VS Code 的分支在 MIT 許可證下是合法的，因為他們可以自由修改並將程式碼庫商業化，只要包含所需的版權和許可聲明。他們面臨的主要挑戰是實務上的——例如無法存取 VS Code Marketplace 及某些專有擴充功能——而非法律障礙。如果您對 Cursor 的具體實施或合規性有疑慮，建議諮詢您所在司法管轄區的法律專業人士，因為我並非律師。