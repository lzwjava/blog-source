---
audio: false
generated: true
lang: hant
layout: post
title: npm 套件的安裝來源
translated: true
---

要將 `@ngx-formly/bootstrap` 套件的安裝來源從本地 `.tgz` 文件更改為 npm 註冊表，請按照以下步驟進行：

### 1. 卸載本地安裝的套件
由於您之前從本地 `.tgz` 文件安裝了 `@ngx-formly/bootstrap`，它目前位於您項目的 `node_modules` 目錄中。要移除它，請在終端中運行以下命令：

```bash
npm uninstall @ngx-formly/bootstrap
```

此命令會從 `node_modules` 移除套件。如果套件已手動添加到 `package.json` 文件的 `dependencies` 或 `devDependencies` 下，這也會從中移除。如果它未列在 `package.json` 中（通常在從 `.tgz` 文件安裝但未保存時），它仍會從您的項目中移除。

### 2. 從 npm 註冊表安裝套件
現在，通過運行以下命令從 npm 註冊表安裝套件：

```bash
npm install @ngx-formly/bootstrap
```

此命令會從 npm 註冊表（通常是 `https://registry.npmjs.org/`，除非您已配置不同的註冊表）獲取 `@ngx-formly/bootstrap` 的最新版本，並將其安裝到您的 `node_modules` 目錄中。它還會將套件添加到 `package.json` 文件的 `dependencies` 下（在最近的 npm 版本中），確保它被跟蹤為項目的一部分。

### 可選：驗證註冊表（如需）
如果您之前更改了 npm 註冊表並希望確保它已設置為默認的 npm 註冊表，可以使用以下命令進行檢查：

```bash
npm config get registry
```

如果輸出是 `https://registry.npmjs.org/`，則您正在使用默認註冊表，`npm install` 命令將按預期運行。如果它設置為不同的註冊表，並且您希望恢復為默認設置，請運行：

```bash
npm config set registry https://registry.npmjs.org/
```

然而，由於您提到已經配置了您的註冊表，這一步可能不必要。

### 注意事項
- **版本控制**：如果您需要與 `.tgz` 文件中相同的版本，請在卸載之前檢查 `node_modules/@ngx-formly/bootstrap/package.json` 中的版本號。然後，安裝該特定版本：
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  如果不指定版本，則會安裝註冊表中的最新版本。
- **依賴類型**：如果您希望將套件作為開發依賴而不是普通依賴，請使用：
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

按照這些步驟，您將成功將 `@ngx-formly/bootstrap` 從通過本地 `.tgz` 文件安裝更改為從 npm 註冊表安裝。