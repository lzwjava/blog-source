---
audio: false
generated: true
lang: hant
layout: post
title: 從 Jekyll 遷移至 JBake
translated: true
type: note
---

將您的 Jekyll 部落格遷移至基於 Java 的部落格框架，可能是個值得投入的嘗試，特別是當您希望利用 Java 生態系統的同時，又能保有靜態網站產生器的簡潔性。最適合此轉移的選擇是 **JBake**，這款基於 Java 的靜態網站產生器與 Jekyll 有許多相似之處，例如能將 Markdown 或 AsciiDoc 撰寫的內容轉換為靜態 HTML。以下我將引導您完成關鍵步驟與注意事項，讓遷移過程盡可能順利。

### 為何選擇 JBake？
JBake 是個絕佳選擇，因為：
- 它是**靜態網站產生器**，與 Jekyll 相同，能產生可隨處託管的靜態 HTML 檔案，無需資料庫或伺服器端處理。
- 支援 **Markdown**，因此您現有的內容只需極少變動即可轉移。
- **基於 Java**，符合您轉用 Java 框架的需求。
- 提供多種模板引擎的靈活性（例如 Freemarker、Groovy、Thymeleaf、Jade），讓您選擇最適合的選項。

雖然還有其他基於 Java 的部落格平台（如 Apache Roller），但這些屬於動態平台，若您已習慣 Jekyll 的靜態特性，可能會帶來不必要的複雜性。JBake 保持簡單高效，使其成為您遷移的自然選擇。

### 從 Jekyll 遷移至 JBake 的步驟

#### 1. 設定新的 JBake 專案
- **安裝 JBake**：依照 [JBake 官網](https://jbake.org) 的指示下載並安裝 JBake。
- **建立新專案**：使用 JBake 命令列介面 (CLI) 初始化專案：
  ```bash
  jbake -i
  ```
  這會產生基本專案結構，包含內容、模板與資源的目錄。

#### 2. 選擇模板引擎
- JBake 支援多種模板引擎，包括 **Freemarker**、**Groovy**、**Thymeleaf** 與 **Jade**。選擇您熟悉或最符合 Jekyll 模板的引擎。
- 若您對這些引擎不熟悉，**Freemarker** 是個廣泛使用且語法直觀的選項。

#### 3. 遷移內容
- **複製 Markdown 檔案**：將您的文章從 Jekyll 的 `_posts` 目錄轉移至 JBake 的 `content` 目錄。
- **Front matter**：Jekyll 使用 YAML front matter（例如 `title`、`date`），而 JBake 支援 YAML、JSON 或 properties 格式。若您的 front matter 為 YAML 格式，應可在 JBake 中無需修改直接使用，但請確認所有元資料欄位（例如 `tags`、`categories`）均被識別。
- **檔案命名**：Jekyll 使用如 `YYYY-MM-DD-title.md` 的檔案名稱。JBake 能處理此慣例，但您可能需要調整配置以維持 URL 結構（見步驟 5）。

#### 4. 改寫或調整模板
- **Jekyll 至 JBake 模板**：Jekyll 使用 Liquid 模板，而 JBake 使用您選擇的模板引擎。請改寫您的模板以符合新引擎的語法。
- **主題**：若您的 Jekyll 部落格使用主題，您可以：
  - 尋找或建立相似的 JBake 主題。
  - 手動將 Liquid 模板轉換為新引擎的語法。
- 此步驟可能耗時，特別是當模板包含複雜邏輯時。您需要學習新模板語法並複製網站的設計與功能。

#### 5. 配置網站
- **配置檔案**：Jekyll 使用 `_config.yml`，而 JBake 使用 `jbake.properties`。請將您的設定（例如網站標題、描述、基礎 URL）轉換為 JBake 格式。例如：
  ```
  site.title=我的部落格
  site.description=一個以 Java 驅動的部落格
  ```
- **永久連結**：為避免連結失效，請配置 JBake 的永久連結設定以符合 Jekyll 的 URL 結構（例如 `/YYYY/MM/DD/title/`）。這可能涉及自訂永久連結模式或確保日期包含在 URL 中。

#### 6. 處理自訂功能或外掛
- **外掛**：若您的 Jekyll 部落格依賴外掛（例如用於 SEO、重新導向或語法突顯），請檢查 JBake 是否提供同等功能或外掛。否則，您可能需要實作自訂解決方案。
- **草稿**：對於未發佈的文章，Jekyll 使用 `_drafts` 目錄。在 JBake 中，請在這些文章的 front matter 中設定 `status=draft`。

#### 7. 遷移資源（圖片、CSS 等）
- **複製資源**：將您的資源目錄（例如 `images`、`css`、`js`）從 Jekyll 移至 JBake 的對應目錄（通常為 `assets`）。
- **CSS 預處理**：若您在 Jekyll 中使用 Sass 或其他預處理器，可以：
  - 將其預編譯為 CSS 供 JBake 使用。
  - 使用外部工具（例如 Webpack、Gulp）處理資源，因為 JBake 本身不支援 Sass，但能與此類工具整合。

#### 8. 產生並預覽網站
- **建置網站**：使用以下指令產生靜態檔案：
  ```bash
  jbake -b
  ```
- **本地預覽**：啟動本地伺服器以檢視您的網站：
  ```bash
  jbake -s
  ```
- 檢查內容、模板或資源路徑的問題，並視需要調整。

#### 9. 部署網站
- **產生最終檔案**：執行 `jbake -b` 以產生靜態 HTML 檔案（位於 `build` 目錄）。
- **託管**：將這些檔案部署至您的託管服務：
  - 對於 **GitHub Pages**，請將產生的 HTML 檔案推送至您的儲存庫（與 Jekyll 不同，GitHub 不會為您建置網站）。
  - 或者，使用 Netlify、Vercel 或任何能託管靜態檔案的網頁伺服器。

### 潛在挑戰
- **模板轉換**：將 Liquid 模板適應新引擎可能耗時，特別是對於複雜設計或邏輯。
- **URL 結構**：維持現有 URL 需要仔細配置永久連結，以避免連結失效。
- **內容調整**：雖然 Markdown 易於轉移，但您可能需要微調 front matter 或檔案名稱以符合 JBake 的慣例。
- **學習曲線**：您需要熟悉 JBake 的模板引擎與配置選項。

### 額外提示
- **自動化**：對於大型部落格，撰寫腳本以在遷移期間調整檔案名稱或 front matter。
- **建置工具**：將 JBake 與 Gradle 或 Maven 整合以自動化建置，特別是若您熟悉 Java 生態系統。
- **資源**：參考 JBake 的[文件](https://jbake.org/docs)與社群論壇以獲取詳細指引與範例。

### 結論
從 Jekyll 遷移至 JBake 涉及設定新專案、轉移內容與資源、改寫模板、配置設定及部署靜態網站。雖然需要投入心力——特別是模板部分——但 Jekyll 與 JBake 同為靜態網站產生器的相似性，使過程變得可管理。完成後，您將擁有一個符合目標的 Java 基礎部落格框架，同時保有靜態網站的簡潔性與效能。祝您遷移順利！