---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 移除不需要的 GitHub 分支
translated: true
type: note
---

明白了。簡短來說：你無法直接刪除別人的複刻（fork）。但你可以（a）聯絡對方，（b）清除敏感內容並鎖定未來洩漏途徑，以及（c）在合理情況下透過 GitHub 官方途徑（DMCA 或支援請求）處理。以下是專為個人部落格設計的簡潔方案（無表格版本）。

### 1) 首先，聯絡複刻者（最快速途徑）

在對方的複刻庫中開啟議題（issue）或直接寄送電子郵件。這裡提供一個簡潔模板供你直接使用：

> 你好 @tornadobaflocer — 這個複刻包含我的個人筆記和活動記錄。我發佈此儲存庫僅為了使用 `lzwjava.github.io` 網域，並非用於重新分發。請刪除此複刻。我將把原始碼設為私人，並僅保留編譯後的網站資源公開。
> 感謝理解。

若對方刪除，問題即解決。若未獲回應，請繼續下一步。

### 2) 了解 GitHub 的處理範圍

* 刪除或將你的**公開**儲存庫設為私人，**不會**移除現有的公開複刻。公開複刻會保持公開狀態並獨立成為自己的「網絡」。([Stack Overflow][1])
* 你只能刪除自己**擁有管理員權限的複刻**（此處你並非管理員）。([Stack Overflow][2])

### 3) 若複刻未經授權複製你的版權內容

你可以向 GitHub 提交 DMCA 下架通知。這是移除跨複刻侵權內容的官方途徑。請詳閱政策與「提交指南」，其中說明了必須包含的資訊。([GitHub 文件][3])

提示：若你的儲存庫**未設定授權條款**，則預設適用版權保護，這將強化下架請求的正當性（他人無權重複使用）。即使你採用寬鬆的授權條款，DMCA 仍然適用，但情況會較為複雜。

### 4) 防止未來複刻暴露你的原始碼

透過分割儲存庫，保持**網域**公開，但將**原始碼**設為私人：

* **私人原始碼儲存庫**（例如 `blog-source`）：存放你的 Jekyll/Hugo 內容、草稿、筆記、設定檔。
* **公開部署儲存庫**，命名為 **`lzwjava.github.io`**：**僅包含建置後的網站檔案**（HTML/CSS/JS）。不含草稿與歷史記錄。

GitHub Pages 網站在儲存庫設為私人時仍可公開存取（企業雲端版搭配私人 Pages 功能除外）。因此，對個人部落格而言，採用雙儲存庫的「僅部署」模式是安全做法。([GitHub 文件][4])

當前可用的部署選項：

* 將生成器的 `public/` 或 `docs/` 輸出推送至 `lzwjava.github.io`。([Quarto][5])
* 或在 `blog-source` 中使用 GitHub Actions 工作流程，建置並強制推送輸出至 `lzwjava.github.io` 儲存庫的預設分支。（文件：選擇「從分支發佈」或「使用 Actions 發佈」流程。）([GitHub 文件][6])

### 5) 清除歷史記錄中的敏感內容（你的與任何現存副本）

* 輪換任何已暴露的權杖／金鑰（假設它們已遭洩漏）。
* 使用 `git filter-repo`（GitHub 現推薦此工具）或 BFG（針對常見情況更快速）改寫歷史記錄，移除敏感檔案／路徑。然後執行強制推送。([GitHub 文件][7])

此舉無法單獨修復他人的複刻，但能清理你的主要儲存庫，並為下架申訴提供佐證，顯示內容已被移除。

### 6) 額外強化措施（可選）

* 新增明確的授權條款（若你希望明確限制重複使用）。
* 在 README 中加入免責聲明：「此儲存庫僅用於存放編譯後的網站輸出。請勿複刻原始碼；其為私人內容。」
* 若未來在**組織**中托管，你可全域關閉組織內私人儲存庫的複刻功能，並可針對各儲存庫設定（雖無法阻止公開程式碼的複製，但對私人儲存庫有幫助）。([GitHub 文件][8])

---

## 具體後續步驟（有效執行順序）

1. 請 @tornadobaflocer 刪除複刻（使用上述訊息）。
2. 立即將你的原始碼移至新的**私人**儲存庫（`blog-source`）。
3. 將 `lzwjava.github.io` 設為**僅用於部署的公開**儲存庫，僅包含建置後的檔案。設定 Pages 從其分支／資料夾發佈。([GitHub 文件][6])
4. 改寫舊公開儲存庫的歷史記錄以移除敏感內容，然後封存或刪除該儲存庫。([GitHub 文件][7])
5. 若對方拒絕且你堅持要求下架，向 GitHub 提交**DMCA 下架通知**。([GitHub 文件][9])

如有需要，我可根據 GitHub 要求的確切格式，為你草擬 DMCA 通知，以及一個極簡的 GitHub Actions 工作流程，用於從 `blog-source` 建置你的網站，並僅推送編譯後的檔案至 `lzwjava.github.io`。

[1]: https://stackoverflow.com/questions/53052745/what-happens-to-the-forks-when-deleting-the-original-repository?utm_source=chatgpt.com "刪除原始儲存庫後，複刻會如何？"
[2]: https://stackoverflow.com/questions/50280412/github-delete-a-fork-that-was-created-from-my-repo?utm_source=chatgpt.com "Github - 刪除從我儲存庫建立的複刻"
[3]: https://docs.github.com/articles/dmca-takedown-policy?utm_source=chatgpt.com "DMCA 下架政策"
[4]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "建立 GitHub Pages 網站"
[5]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[6]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site?utm_source=chatgpt.com "為你的 GitHub Pages 網站設定發佈來源"
[7]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository?utm_source=chatgpt.com "從儲存庫移除敏感資料"
[8]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository?utm_source=chatgpt.com "管理儲存庫的複刻政策"
[9]: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice?utm_source=chatgpt.com "提交 DMCA 下架通知指南"