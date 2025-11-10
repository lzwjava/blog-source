---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 安裝 GitHub Copilot CLI 擴充功能
translated: true
type: note
---

指令 `gh extension install github/gh-copilot` 會為 GitHub CLI 安裝 GitHub Copilot 擴充功能，從而啟用 Copilot 的指令行建議與解釋等功能。對於企業用戶而言，此指令是否適用取決於特定條件：

- **企業配置**：若企業或組織已訂閱 GitHub Copilot Business 或 Copilot Enterprise，且管理員已啟用 CLI 功能，則企業用戶可使用 Copilot CLI 擴充功能。若組織擁有者或企業管理員已停用 CLI 中的 Copilot，即使安裝了擴充功能也無法使用。[](https://docs.github.com/fr/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
- **身份驗證**：企業用戶必須使用已分配 Copilot 授權的 GitHub 帳戶向 GitHub CLI 進行驗證。對於 GitHub Enterprise Cloud (GHE.com) 上的受管用戶帳戶，可能需要進行額外設置，例如在登入前更新設定。[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)
- **安裝要求**：必須先安裝 GitHub CLI 才能執行此指令。安裝過程對企業用戶與個人用戶相同，但企業政策可能會限制使用。[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)

**企業用戶操作步驟**：
1. 確保已安裝 GitHub CLI（請參閱 [GitHub CLI 儲存庫](https://github.com/cli/cli)以獲取指引）。
2. 向企業管理員確認已為您的組織啟用 Copilot CLI。
3. 在終端機中執行 `gh extension install github/gh-copilot`。
4. 使用企業分配的 GitHub 帳戶透過 `gh auth login` 進行驗證。
5. 若使用 GHE.com 上的受管用戶帳戶，請遵循[在 GHE.com 帳戶中使用 GitHub Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/configuring-github-copilot-in-your-environment/using-github-copilot-with-an-account-on-ghecom) 中所述的額外設置步驟。[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)

若您的企業限制 CLI 存取或未啟用 Copilot，擴充功能可能可安裝但無法運作。請向管理員查詢政策詳情。

[在 CLI 中安裝 GitHub Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/installing-github-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
[為您的企業設定 GitHub Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/setting-up-github-copilot-for-your-enterprise)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/set-up-for-enterprise)