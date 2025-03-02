---
audio: false
generated: false
lang: hant
layout: post
title: 使用 Auth Tokens 与 npm Registry URLs
translated: true
---

### 關鍵要點
- 似乎使用 auth token 來與 npm 註冊表 URL 配合，需要在 `.npmrc` 文件中配置，將 token 與註冊表 URL 關聯。
- 研究表明，標準方法是在 `.npmrc` 文件中添加 `//registry.url.com/:_authToken=your_token`，其中 `registry.url.com` 是註冊表 URL，`your_token` 是您的身份驗證 token。
- 證據表明，使用 `.npmrc` 文件進行身份驗證，因為在 URL 中直接包含 token（例如在 HTTP 請求中）不是 npm 的標準做法，可能無法正常工作。

### 直接答案

#### 概述
要使用身份驗證 token 來與 npm 註冊表 URL 配合，通常需要在一個名為 `.npmrc` 的特殊文件中進行配置。這個文件告訴 npm 命令行工具如何在訪問特定的包註冊表（例如公共 npm 註冊表或私有註冊表）時進行身份驗證。以下是如何逐步進行配置的方法，保持簡單，適合初學者。

#### 配置步驟
1. **找到註冊表 URL**：決定要使用的註冊表，例如 `registry.npmjs.org` 為公共 npm 註冊表，或像 `privateregistry.com` 這樣的 URL 為私有註冊表。
2. **獲取您的身份驗證 token**：從註冊表提供者獲取身份驗證 token，這可能是個人訪問 token 或由您的組織提供的其他類型。
3. **編輯 `.npmrc` 文件**：打開或創建 `.npmrc` 文件。這個文件可以在您的項目文件夾中（用於專案特定設置）或在您的主目錄中（例如 Unix 系統上的 `~/.npmrc`，用於用戶範圍設置）。
   - 添加一行，例如：`//registry.url.com/:_authToken=your_token`。將 `registry.url.com` 替換為您的註冊表 URL，將 `your_token` 替換為您的實際 token。
   - 例如，對於公共 npm 註冊表，它可能看起來像：`//registry.npmjs.org/:_authToken=abc123`。
4. **保護文件**：確保 `.npmrc` 文件僅由您讀取和寫入，以保護您的 token。在 Unix 系統上，您可以使用 `chmod 600 ~/.npmrc` 設置權限。
5. **驗證是否正常工作**：嘗試運行一個 npm 命令，例如 `npm install`，看看它是否能夠訪問註冊表而不出現問題。

#### 意外細節
您可能會認為可以將身份驗證 token 直接放在 URL 中（例如 `https://registry.url.com?token=your_token`），但這不是 npm 的標準做法。相反，npm 使用 `.npmrc` 文件在後台處理身份驗證，使其更加安全和易於管理。

有關更多詳細信息，請參閱官方 npm 文檔中關於配置 `.npmrc` 文件的部分 [這裡](https://docs.npmjs.com/configuring-npm/npmrc)。

---

### 調查筆記：使用 npm 註冊表 URL 的身份驗證 token 的詳細探討

這一部分提供了如何使用身份驗證 token 來與 npm 註冊表 URL 配合的全面分析，擴展了直接答案，並提供了額外的上下文、技術細節和示例。它旨在涵蓋研究中討論的所有方面，確保用戶能夠全面理解，無論其技術水平如何。

#### npm 和身份驗證的介紹
Node Package Manager (npm) 是 JavaScript 開發者的重要工具，管理包和依賴項。它與包註冊表進行交互，例如公共註冊表 [registry.npmjs.org](https://registry.npmjs.org)，以及組織托管的私有註冊表。身份驗證通常需要私有註冊表或特定操作（例如發布包），這通常通過存儲在配置文件中的身份驗證 token 來處理。

`.npmrc` 文件是 npm 配置的核心，允許自定義設置，例如註冊表 URL、身份驗證方法等。它可以存在於多個位置，例如專案（在專案根目錄中）、用戶（在主目錄中，例如 Unix 系統上的 `~/.npmrc`）或全局（例如 `/etc/npmrc`）。這個文件使用 INI 格式，其中鍵和值定義了 npm 的行為，包括它如何與註冊表進行身份驗證。

#### 在 `.npmrc` 中配置身份驗證 token
要使用特定註冊表 URL 的身份驗證 token，配置 `.npmrc` 文件將 token 與該註冊表關聯。標準格式是：

```
registry.url.com/:_authToken=your_token
```

這裡，`registry.url.com` 是註冊表的基礎 URL（例如 `registry.npmjs.org` 為公共註冊表或 `privateregistry.com` 為私有註冊表），`your_token` 是註冊表提供的身份驗證 token。`:_authToken` 鍵表示這是基於 token 的身份驗證，npm 使用它來設置 `Authorization` 標頭為 `Bearer your_token`，當向註冊表發出 HTTP 請求時。

例如，如果您有一個 token `abc123` 來自公共 npm 註冊表，您的 `.npmrc` 條目將是：

```
registry.npmjs.org/:_authToken=abc123
```

這個配置確保任何與 `registry.npmjs.org` 交互的 npm 命令都會包含 token 進行身份驗證，從而允許訪問私有包或發布功能，具體取決於 token 的範圍。

#### 處理作用域包
對於作用域包（以 `@` 開頭的包，例如 `@mycompany/mypackage`），您可以為該作用域指定不同的註冊表。首先，設置作用域的註冊表：

```
@mycompany:registry=https://mycompany.artifactory.com/
```

然後，將身份驗證 token 與該註冊表關聯：

```
mycompany.artifactory.com/:_authToken=your_token
```

這種設置將所有對 `@mycompany` 包的請求路由到指定的私有註冊表，並使用提供的 token 進行身份驗證。這在企業環境中特別有用，組織托管自己的 npm 註冊表以供內部包使用。

#### `.npmrc` 的位置和安全性
`.npmrc` 文件可以位於幾個位置，每個位置都有不同的用途：
- **專案**：位於專案根目錄（例如 `package.json` 旁邊）。這對於專案特定配置和覆蓋全局設置非常理想。
- **用戶**：位於用戶的主目錄（例如 Unix 系統上的 `~/.npmrc`，Windows 上的 `C:\Users\<Username>\.npmrc`）。這會影響該用戶的所有 npm 操作。
- **全局**：位於 `/etc/npmrc` 或由 `globalconfig` 參數指定，通常用於系統範圍設置。

由於 `.npmrc` 可能包含敏感信息，例如身份驗證 token，因此安全性至關重要。文件必須僅由用戶讀取和寫入，以防止未經授權的訪問。在 Unix 系統上，您可以使用命令 `chmod 600 ~/.npmrc` 來確保這一點，將權限設置為僅允許擁有者讀寫。

#### 其他身份驗證方法
雖然基於 token 的身份驗證很常見，但 npm 也支持基本身份驗證，您可以在 `.npmrc` 文件中包含用戶名和密碼：

```
registry.url.com/:username=your_username
registry.url.com/:_password=your_password
```

然而，出於安全原因，建議使用基於 token 的身份驗證，因為 token 可以撤銷並具有範圍權限，這比存儲純文本密碼更安全。

#### 直接 URL 包含：是否可能？
問題提到「在 npm 註冊表 URL 中使用 auth 或 authtoken」，這可能暗示將 token 直接包含在 URL 中，例如 `https://registry.url.com?token=your_token`。然而，研究表明這不是 npm 的標準做法。npm 註冊表 API 文檔和相關資源，例如 [NPM 註冊表身份驗證 | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/)，強調使用 `.npmrc` 文件進行身份驗證，token 通過 `Authorization` 標頭作為 `Bearer your_token` 進行傳遞。

嘗試將 token 作為查詢參數包含在 URL 中，這在標準 npm 註冊表中不受支持，可能無法正常工作，因為身份驗證是在 HTTP 標頭層級處理的。某些私有註冊表可能支持自定義 URL 基於身份驗證，但這在官方 npm 註冊表中沒有文檔記錄。例如，基本身份驗證允許 URL 如 `https://username:password@registry.url.com`，但這已經過時且不安全，與基於 token 的方法相比。

#### 實際示例和使用案例
為了說明，考慮以下情況：

- **公共註冊表與 token**：如果您需要發布到公共 npm 註冊表並擁有 token，添加：
  ```
  registry.npmjs.org/:_authToken=abc123
  ```
  然後，運行 `npm publish` 上傳您的包，npm 將使用 token 進行身份驗證。

- **私有註冊表的作用域包**：對於使用私有註冊表 `https://company.registry.com` 的公司，對於 `@company` 包，配置：
  ```
  @company:registry=https://company.registry.com/
  company.registry.com/:_authToken=def456
  ```
  現在，安裝 `@company/mypackage` 將使用 token 對私有註冊表進行身份驗證。

- **CI/CD 集成**：在持續集成環境中，將 token 存儲為環境變量（例如 `NPM_TOKEN`），並在 `.npmrc` 文件中動態使用它：
  ```
  registry.npmjs.org/:_authToken=${NPM_TOKEN}
  ```
  這種方法，詳細說明在 [在 CI/CD 工作流中使用私有包 | npm 文檔](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/) 中，確保 token 不會硬編碼並保持安全。

#### 錯誤排除和最佳實踐
如果身份驗證失敗，請驗證：
- 註冊表 URL 是否正確且可訪問。
- token 是否有效並具有必要的權限（例如，讀取以進行安裝，寫入以進行發布）。
- `.npmrc` 文件是否在正確位置並具有適當的權限。

最佳實踐包括：
- 永遠不要將包含 token 的 `.npmrc` 提交到版本控制；將其添加到 `.gitignore`。
- 在 CI/CD 管道中使用環境變量來存儲 token，以增強安全性。
- 定期輪換 token 並撤銷未使用的 token，以最小化風險。

#### 身份驗證方法的比較分析
為了提供結構化概述，以下是表格，比較 npm 中基於 token 和基本身份驗證：

| **方法**          | **在 `.npmrc` 中的配置**                          | **安全性**                     | **使用案例**                     |
|---------------------|-------------------------------------------------------|-----------------------------------|-----------------------------------|
| 基於 token 的（推薦） | `registry.url.com/:_authToken=your_token`            | 高（可撤銷，範圍）         | 私有註冊表，CI/CD        |
| 基本身份驗證| `registry.url.com/:username=your_username`<br>`registry.url.com/:_password=your_password` | 低（純文本密碼）         | 遺留系統，公共註冊表  |

這個表格強調了為什麼基於 token 的身份驗證是推薦的，特別是對於現代工作流程。

#### 結論
使用身份驗證 token 來與 npm 註冊表 URL 配合，主要涉及配置 `.npmrc` 文件將 token 與註冊表關聯。這種方法是標準的、安全的，並且得到了廣泛支持，確保 npm 能夠在不暴露 token 的情況下對請求進行身份驗證。雖然將 token 直接包含在 URL 中不是 npm 的標準做法，可能無法正常工作，但 `.npmrc` 方法提供了一種對於公共和私有註冊表交互的強大解決方案。

有關更多信息，請參閱官方 npm 文檔中的 [配置 npmrc](https://docs.npmjs.com/configuring-npm/npmrc) 和 [註冊表身份驗證](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)。

### 關鍵引用
- [NPM 註冊表身份驗證 Rush 文檔](https://rushjs.io/pages/maintainer/npm_registry_auth/)
- [registry-auth-token npm 包詳細信息](https://www.npmjs.com/package/registry-auth-token)
- [在 Stack Overflow 上全局配置 NPM 使用 token 註冊表](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
- [配置身份驗證 Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
- [官方 npm 文檔中的 npmrc 文件](https://docs.npmjs.com/configuring-npm/npmrc)
- [在 CI/CD 工作流中使用私有包 npm 文檔](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)