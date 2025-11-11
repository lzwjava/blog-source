---
audio: false
generated: true
lang: hant
layout: post
title: 在 npm 註冊表網址中使用身份驗證令牌
translated: true
type: note
---

### 重點摘要
- 要使用 npm registry URL 搭配驗證令牌，似乎很可能需要透過設定 `.npmrc` 檔案，將令牌與 registry URL 建立關聯。
- 研究顯示標準做法是在 `.npmrc` 檔案中加入 `//registry.url.com/:_authToken=your_token`，其中 `registry.url.com` 是 registry URL，而 `your_token` 則是你的驗證令牌。
- 現有證據傾向於使用 `.npmrc` 檔案進行驗證，因為將令牌直接包含在 URL 中（例如在 HTTP 請求中）並非 npm 的標準做法，且可能無法正常運作。

### 直接解答

#### 概述
要使用 npm registry URL 搭配驗證令牌，通常需要在一個名為 `.npmrc` 的特殊檔案中進行設定。這個檔案會告知 npm 指令列工具在存取特定套件 registry（例如公共 npm registry 或私有 registry）時如何進行驗證。以下是針對初學者的逐步設定說明。

#### 設定步驟
1. **尋找 Registry URL**：決定要使用的 registry，例如公共 npm registry 的 `registry.npmjs.org`，或私有 registry 的 `privateregistry.com` 等 URL。
2. **取得驗證令牌**：向 registry 供應商取得驗證令牌，這可能是個人存取令牌或組織提供的其他類型令牌。
3. **編輯 `.npmrc` 檔案**：開啟或建立 `.npmrc` 檔案。此檔案可位於專案資料夾中（用於專案特定設定）或使用者根目錄中（例如 Unix 系統的 `~/.npmrc`，用於使用者全域設定）。
   - 加入如下內容：`//registry.url.com/:_authToken=your_token`。將 `registry.url.com` 替換為你的 registry URL，並將 `your_token` 替換為你的實際令牌。
   - 例如，針對公共 npm registry，可能會是：`//registry.npmjs.org/:_authToken=abc123`。
4. **保護檔案安全**：確保 `.npmrc` 檔案僅供你自己讀取和寫入，以保護令牌安全。在 Unix 系統上，可使用 `chmod 600 ~/.npmrc` 設定權限。
5. **驗證是否正常運作**：嘗試執行 npm 指令，例如 `npm install`，確認能否正常存取 registry。

#### 意外細節
雖然你可能認為可以將驗證令牌直接放入 URL 中（例如 `https://registry.url.com?token=your_token`），但這並非 npm 的標準做法。相反地，npm 使用 `.npmrc` 檔案在後台處理驗證，這樣更安全且易於管理。

更多詳細資訊，請查閱官方 npm 文件中有關設定 `.npmrc` 檔案的[說明](https://docs.npmjs.com/configuring-npm/npmrc)。

---

### 調查筆記：npm Registry URL 驗證令牌使用詳解

本節提供關於如何使用 npm registry URL 搭配驗證令牌的全面分析，在直接解答的基礎上擴展了額外背景、技術細節和範例。旨在涵蓋研究中的所有面向，確保不同專業程度的使用者都能獲得深入理解。

#### npm 與驗證簡介
Node Package Manager (npm) 是 JavaScript 開發者的關鍵工具，用於管理套件和依賴項。它與套件 registry 互動，例如位於 [registry.npmjs.org](https://registry.npmjs.org) 的公共 registry，以及組織託管的私有 registry。私有 registry 或特定操作（例如發布套件）通常需要驗證，這一般透過儲存在設定檔案中的驗證令牌來處理。

`.npmrc` 檔案是 npm 設定的核心，允許自訂 registry URL、驗證方法等設定。它可存在於多個位置，例如每個專案（在專案根目錄中）、每個使用者（在使用者根目錄中，例如 Unix 的 `~/.npmrc`）或全域位置（例如 `/etc/npmrc`）。此檔案使用 INI 格式，透過鍵值對定義 npm 的行為，包括如何與 registry 進行驗證。

#### 在 `.npmrc` 中設定驗證令牌
要對特定 registry URL 使用驗證令牌，你需要設定 `.npmrc` 檔案將令牌與該 registry 建立關聯。標準格式為：

```
registry.url.com/:_authToken=your_token
```

此處，`registry.url.com` 是 registry 的基礎 URL（例如公共 registry 的 `registry.npmjs.org` 或私有 registry 的 `privateregistry.com`），而 `your_token` 是 registry 提供的驗證令牌。`:_authToken` 鍵表示這是基於令牌的驗證，npm 會在使用此令牌向 registry 發送 HTTP 請求時，將 `Authorization` 標頭設為 `Bearer your_token`。

例如，如果你有公共 npm registry 的令牌 `abc123`，則 `.npmrc` 中的條目應為：

```
registry.npmjs.org/:_authToken=abc123
```

此設定確保任何與 `registry.npmjs.org` 互動的 npm 指令都會包含該令牌進行驗證，根據令牌的權限範圍允許存取私有套件或發布功能。

#### 處理作用域套件
對於作用域套件（以 `@` 開頭的套件，例如 `@mycompany/mypackage`），你可以為該作用域指定不同的 registry。首先，為作用域設定 registry：

```
@mycompany:registry=https://mycompany.artifactory.com/
```

然後，將驗證令牌與該 registry 建立關聯：

```
mycompany.artifactory.com/:_authToken=your_token
```

此設定將所有對 `@mycompany` 套件的請求導向指定的私有 registry，並使用提供的令牌進行驗證。這在企業環境中特別有用，組織通常會為內部套件託管自己的 npm registry。

#### `.npmrc` 的位置與安全性
`.npmrc` 檔案可位於多個位置，各自服務不同目的：
- **每個專案**：位於專案根目錄中（例如與 `package.json` 同目錄）。適用於專案特定設定，並會覆蓋全域設定。
- **每個使用者**：位於使用者根目錄中（例如 Unix 的 `~/.npmrc`，Windows 的 `C:\Users\<Username>\.npmrc`）。影響該使用者的所有 npm 操作。
- **全域**：位於 `/etc/npmrc` 或由 `globalconfig` 參數指定，通常用於系統全域設定。

由於 `.npmrc` 可能包含驗證令牌等敏感資訊，安全性至關重要。檔案必須僅供使用者讀取和寫入，以防止未經授權的存取。在 Unix 系統上，可使用指令 `chmod 600 ~/.npmrc` 確保這一點，將權限設為僅擁有者可讀寫。

#### 替代驗證方法
雖然令牌驗證很常見，但 npm 也支援基本驗證，你可以在 `.npmrc` 檔案中包含使用者名稱和密碼：

```
registry.url.com/:username=your_username
registry.url.com/:_password=your_password
```

然而，出於安全考量，更推薦使用令牌驗證，因為令牌可被撤銷且具有權限範圍，相比儲存明文密碼能降低風險。

#### 直接包含在 URL 中：是否可行？
問題中提到「在 npm registry url 中使用 auth 或 authtoken」，這可能暗示將令牌直接包含在 URL 中，例如 `https://registry.url.com?token=your_token`。然而，研究顯示這並非 npm 的標準做法。npm registry API 文件及相關資源（例如 [NPM registry authentication | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/)）強調使用 `.npmrc` 檔案進行驗證，並將令牌以 `Bearer your_token` 形式傳遞在 `Authorization` 標頭中。

嘗試將令牌作為查詢參數包含在 URL 中不受標準 npm registry 支援，且可能無法運作，因為驗證是在 HTTP 標頭層級處理的。某些私有 registry 可能支援自訂的 URL 驗證，但官方 npm registry 的文件中未記載此做法。例如，基本驗證允許類似 `https://username:password@registry.url.com` 的 URL，但這種方式已過時且不如令牌驗證安全。

#### 實務範例與使用情境
考慮以下情境：

- **使用令牌的公共 Registry**：如果你需要發布到公共 npm registry 且擁有令牌，請加入：
  ```
  registry.npmjs.org/:_authToken=abc123
  ```
  然後執行 `npm publish` 上傳你的套件，npm 將使用該令牌進行驗證。

- **作用域套件的私有 Registry**：對於公司使用私有 registry 位於 `https://company.registry.com` 處理 `@company` 套件，請設定：
  ```
  @company:registry=https://company.registry.com/
  company.registry.com/:_authToken=def456
  ```
  現在，安裝 `@company/mypackage` 將使用令牌向私有 registry 進行驗證。

- **CI/CD 整合**：在持續整合環境中，將令牌儲存為環境變數（例如 `NPM_TOKEN`）並在 `.npmrc` 檔案中動態使用：
  ```
  registry.npmjs.org/:_authToken=${NPM_TOKEN}
  ```
  此方法在[在 CI/CD 工作流程中使用私有套件 | npm 文件](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)中有詳細說明，能確保令牌不被硬編碼且安全。

#### 疑難排解與最佳實踐
如果驗證失敗，請檢查：
- Registry URL 是否正確且可存取。
- 令牌是否有效且具有必要權限（例如讀取權限用於安裝，寫入權限用於發布）。
- `.npmrc` 檔案是否位於正確位置且具有適當權限。

最佳實踐包括：
- 切勿將包含令牌的 `.npmrc` 提交到版本控制；將其加入 `.gitignore`。
- 在 CI/CD 流程中使用環境變數儲存令牌以提升安全性。
- 定期輪換令牌並撤銷未使用的令牌以降低風險。

#### 驗證方法比較分析
為提供結構化概述，以下是 npm 中令牌驗證與基本驗證的比較表格：

| **方法**          | **在 `.npmrc` 中的設定**                          | **安全性**                     | **使用情境**                     |
|---------------------|-------------------------------------------------------|-----------------------------------|-----------------------------------|
| 令牌驗證（推薦） | `registry.url.com/:_authToken=your_token`            | 高（可撤銷、具權限範圍）         | 私有 registry、CI/CD        |
| 基本驗證| `registry.url.com/:username=your_username`<br>`registry.url.com/:_password=your_password` | 低（明文密碼）         | 舊系統、公共 registry  |

此表格突顯了為何推薦使用令牌驗證，特別是在現代工作流程中。

#### 結論
使用 npm registry URL 搭配驗證令牌主要涉及設定 `.npmrc` 檔案以將令牌與 registry 建立關聯。此方法標準、安全且廣泛支援，能確保 npm 在無需於 URL 中暴露令牌的情況下驗證請求。雖然將令牌直接包含在 URL 中並非 npm 標準做法且可能無法運作，但 `.npmrc` 方法為公共和私有 registry 互動提供了穩健的解決方案。

進一步閱讀，請參考官方 npm 文件中有關[設定 npmrc](https://docs.npmjs.com/configuring-npm/npmrc) 和 [registry 驗證](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)的說明。

### 主要參考文獻
- [NPM registry authentication Rush 文件](https://rushjs.io/pages/maintainer/npm_registry_auth/)
- [registry-auth-token npm 套件詳情](https://www.npmjs.com/package/registry-auth-token)
- [全域設定 NPM 與令牌 Stack Overflow 問題](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
- [設定驗證 Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
- [官方 npm 文件 npmrc 檔案](https://docs.npmjs.com/configuring-npm/npmrc)
- [在 CI/CD 工作流程中使用私有套件 npm 文件](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)