---
audio: false
generated: true
lang: hant
layout: post
title: 編寫 Jenkinsfile
translated: true
type: note
---

要編寫一個包含共享函式庫、字串參數、try-catch區塊、node區塊和if陳述式的Jenkinsfile，您可以採用以下方法。Jenkinsfile使用Groovy編寫，能定義用於自動化建置、測試和部署流程的管道。以下是一個符合這些需求的完整腳本式Jenkinsfile範例。

首先，要使用共享函式庫，需透過`@Library`註解進行導入。Jenkins中的共享函式庫包含可從多個管道調用的可重用程式碼。例如，若您的共享函式庫名為`my-shared-library`，請在Jenkinsfile頂部這樣引入：

```groovy
@Library('my-shared-library') _
```

註解後的下劃線（`_`）是正確導入函式庫的必要符號。

接著要定義字串參數，可使用`properties`步驟。這讓使用者在執行管道時能傳入字串值。以下示範如何添加名為`MY_STRING`的字串參數：

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: '字串參數')
    ])
])
```

`node`區塊用於指定管道執行位置（例如任意可用代理節點）。您可在此區塊內寫入管道邏輯：

```groovy
node {
    // 管道步驟將置於此處
}
```

為處理潛在錯誤，請將步驟包裹在`try-catch`區塊中。這能確保當發生失敗時，可捕捉異常並優雅地處理。此外，可利用`if`陳述式根據字串參數值（`params.MY_STRING`）進行條件判斷。

以下是整合所有元素的完整Jenkinsfile：

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: '字串參數')
    ])
])

node {
    try {
        // 調用共享函式庫中的函數（假設已存在）
        myLibraryFunction()
        
        // 根據字串參數使用if陳述式
        if (params.MY_STRING == 'test') {
            echo "執行測試"
        } else {
            echo "不執行測試"
        }
    } catch (Exception e) {
        echo "發生錯誤：${e.message}"
    }
}
```

### 元件說明

- **`@Library('my-shared-library') _`**：導入名為`my-shared-library`的共享函式庫。請將`my-shared-library`替換為實際函式庫名稱。其中假設函數`myLibraryFunction()`已在此函式庫中定義。
- **`properties`**：定義帶有預設值`'default'`和描述文字的字串參數`MY_STRING`。在管道中可透過`params.MY_STRING`存取此參數。
- **`node`**：在任意可用代理節點上運行管道。如需指定特定代理節點（例如`node('linux')`）亦可設定。
- **`try-catch`**：執行`try`區塊內的步驟，並在`catch`區塊捕捉異常，若發生錯誤則列印錯誤訊息。
- **`if`**：檢查`MY_STRING`是否等於`'test'`並相應列印訊息。可根據需求調整條件判斷與執行動作。

### 注意事項
- 此範例採用腳本式管道，能提供更靈活的Groovy語法。若需宣告式管道，結構會略有不同（例如需使用`pipeline`和`script`區塊包裹Groovy程式碼）。
- `myLibraryFunction()`調用為佔位符。請確保共享函式庫中已定義此函數，或替換為實際存在的函式庫函數。
- 可根據需求擴展此Jenkinsfile，例如添加階段（如`stage('Build')`）或更複雜的邏輯。

此Jenkinsfile提供了包含所有要求元素的穩固基礎：共享函式庫、字串參數、try-catch區塊、node區塊及if陳述式。請根據實際使用情境調整具體內容（函式庫名稱、函數調用或條件判斷）！