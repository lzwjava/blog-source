---
audio: false
generated: true
lang: hant
layout: post
title: npm 套件的安裝來源
translated: true
type: note
---

要將 `@ngx-formly/bootstrap` 套件的安裝來源從本機 `.tgz` 檔案變更為 npm 套件庫，請按照以下步驟操作：

### 1. 解除安裝本機安裝的套件
由於您先前是從本機 `.tgz` 檔案安裝 `@ngx-formly/bootstrap`，該套件目前位於您專案的 `node_modules` 目錄中。若要移除它，請在終端機中執行以下指令：

```bash
npm uninstall @ngx-formly/bootstrap
```

此指令會從 `node_modules` 中移除該套件。如果該套件先前已手動新增至您的 `package.json` 檔案中的 `dependencies` 或 `devDependencies`，此操作也會將其從中移除。如果該套件未列在 `package.json` 中（常見於從 `.tgz` 檔案安裝但未儲存的情況），它仍會從您的專案中被移除。

### 2. 從 npm 套件庫安裝套件
現在，請執行以下指令從 npm 套件庫安裝該套件：

```bash
npm install @ngx-formly/bootstrap
```

此指令會從 npm 套件庫（通常是 `https://registry.npmjs.org/`，除非您已設定其他套件庫）取得最新版本的 `@ngx-formly/bootstrap`，並將其安裝至您的 `node_modules` 目錄中。在較新的 npm 版本中，它預設還會將該套件新增至您的 `package.json` 檔案中的 `dependencies`，確保其被追蹤為專案的一部分。

### 選項：驗證套件庫（如有需要）
如果您先前曾變更過 npm 套件庫，並想確認其是否設定為預設的 npm 套件庫，可以使用以下指令檢查：

```bash
npm config get registry
```

如果輸出為 `https://registry.npmjs.org/`，表示您正在使用預設套件庫，且 `npm install` 指令將如預期運作。如果它被設定為其他套件庫而您想還原為預設值，請執行：

```bash
npm config set registry https://registry.npmjs.org/
```

不過，由於您提到已設定好套件庫，此步驟可能並非必要。

### 注意事項
- **版本控制**：如果您需要與 `.tgz` 檔案中相同的版本，請在解除安裝前先檢查 `node_modules/@ngx-formly/bootstrap/package.json` 中的版本號。然後，使用以下指令安裝該特定版本：
  ```bash
  npm install @ngx-formly/bootstrap@<版本>
  ```
  如果您未指定版本，將會安裝套件庫中的最新版本。
- **依賴類型**：如果您希望將套件作為開發依賴而非常規依賴，請使用：
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

透過遵循這些步驟，您將成功將 `@ngx-formly/bootstrap` 從透過本機 `.tgz` 檔案安裝切換為從 npm 套件庫安裝。