---
audio: false
generated: true
lang: hant
layout: post
title: Git 儲藏
translated: true
type: note
---

以下是有效使用 `git stash` 並在擁有未提交變更時頻繁切換分支/標籤的方法：

## 使用 `git stash`

`git stash` 是一個強大的指令，可讓您暫時保存未提交的變更（包括已暫存和未暫存的變更），並將工作目錄恢復到最後一次提交的狀態。當您需要切換分支或處理其他工作，但又不想提交當前未完成的工作時，這非常有用。

以下是常見的 `git stash` 操作詳解：

**1. 儲存當前變更：**

```bash
git stash
```

此指令會將您的未提交變更儲存為新的 stash，並清理您的工作目錄。您會看到類似以下訊息：

```
Saved working directory and index state WIP on <your_branch>: <commit_hash> <commit_message>
```

**2. 帶有訊息的儲存：**

為您的 stash 添加描述性訊息非常有用，特別是當您有多個 stash 時：

```bash
git stash save "您的描述性訊息"
# 或
git stash push -m "您的描述性訊息"
```

**3. 列出您的 stash：**

要查看所有已儲存 stash 的清單，請使用：

```bash
git stash list
```

這將顯示 stash 清單，通常格式如下：

```
stash@{0}: On <branch_name>: <commit_hash> <stash_message>
stash@{1}: WIP on <another_branch>: ...
```

`stash@{0}` 是最新的 stash。

**4. 應用 stash：**

要恢復 stash 中的變更，您可以使用 `git stash apply`。這會應用變更，但會將 stash 保留在清單中。預設情況下，它會應用最新的 stash（`stash@{0}`）。

```bash
git stash apply
# 或應用特定的 stash：
git stash apply stash@{1}
```

**5. 應用並移除 stash：**

如果您想應用變更並立即從清單中移除 stash，請使用 `git stash pop`。這也預設使用最新的 stash。

```bash
git stash pop
# 或取出特定的 stash：
git stash pop stash@{1}
```

**6. 查看 stash 詳細資訊：**

您可以使用以下指令查看 stash 中變更的摘要：

```bash
git stash show
# 或查看特定 stash：
git stash show stash@{2}
```

要查看 stash 的完整 diff，請添加 `-p` 或 `--patch` 標記：

```bash
git stash show -p stash@{0}
```

**7. 儲存未追蹤的檔案：**

預設情況下，`git stash` 只會儲存已追蹤檔案的變更。要包含未追蹤的檔案，請使用 `-u` 或 `--include-untracked` 選項：

```bash
git stash -u
git stash save -u "包含未追蹤檔案的 stash"
```

**8. 同時儲存被忽略的檔案：**

要包含未追蹤和被忽略的檔案，請使用 `-a` 或 `--all` 選項：

```bash
git stash -a
git stash save -a "包含所有檔案的 stash"
```

**9. 從 stash 建立分支：**

如果您儲存了一些變更，現在想在新的分支上處理它們，可以直接從 stash 建立分支：

```bash
git stash branch <new_branch_name> stash@{0}
# 或針對最新的 stash：
git stash branch <new_branch_name>
```

此指令會基於建立 stash 時的提交建立一個新分支，將 stash 變更應用到新分支，然後丟棄該 stash。

**10. 移除 stash：**

* 移除特定的 stash：
    ```bash
    git stash drop stash@{1}
    ```
* 移除所有 stash：
    ```bash
    git stash clear
    ```

## 在擁有未提交變更時頻繁切換分支或標籤

以下是使用 `git stash` 在擁有未提交變更時頻繁切換分支或標籤的方法：

**情境 1：切換到另一個分支**

1.  **儲存當前變更：**
    ```bash
    git stash save "當前分支的進行中工作"
    ```
2.  **切換到目標分支：**
    ```bash
    git checkout <target_branch_name>
    # 或使用較新的 `git switch` 指令：
    git switch <target_branch_name>
    ```
3.  **在目標分支上進行您的工作。**
4.  **當您需要返回原始分支時：**
    ```bash
    git checkout <original_branch_name>
    # 或
    git switch <original_branch_name>
    ```
5.  **重新應用您儲存的變更：**
    ```bash
    git stash pop  # 如果您想應用並移除 stash
    # 或
    git stash apply # 如果您想應用並保留 stash
    ```
6.  **解決任何可能出現的合併衝突**，如果原始分支自您儲存後有顯著分歧。

**情境 2：切換到標籤**

直接切換到標籤會使您處於「分離 HEAD」狀態，通常不建議在此狀態下進行提交。如果您只想檢查特定標籤的程式碼：

1.  **儲存當前變更：**
    ```bash
    git stash save "檢查標籤前的進行中工作"
    ```
2.  **切換到標籤：**
    ```bash
    git checkout <tag_name>
    ```
3.  **檢查程式碼。**
4.  **返回您的分支：**
    ```bash
    git checkout <your_branch_name>
    # 或
    git switch <your_branch_name>
    ```
5.  **重新應用您儲存的變更：**
    ```bash
    git stash pop
    # 或
    git stash apply
    ```

**情境 3：使用您儲存的變更從標籤建立新分支**

如果您想基於特定標籤開始新功能或修復工作，並且您有來自先前情境的 stash 變更：

1.  **儲存當前變更（如果尚未儲存）：**
    ```bash
    git stash save "進行中工作"
    ```
2.  **從標籤建立新分支：**
    ```bash
    git checkout -b <new_branch_name> <tag_name>
    # 或
    git switch -c <new_branch_name> <tag_name>
    ```
3.  **將您儲存的變更應用到新分支：**
    ```bash
    git stash pop # 或 git stash apply
    ```
4.  **解決任何可能出現的合併衝突。**

**重要注意事項：**

* **保持 stash 有組織：** 使用描述性訊息以便輕鬆識別您的 stash。
* **Stash 是本地的：** Stash 儲存在您的本地儲存庫中，不會推送到遠端儲存庫。
* **可能出現衝突：** 當您重新應用 stash 時，如果應用到的分支自您建立 stash 以來有顯著變更，可能會出現合併衝突。您需要手動解決這些衝突。
* **考慮建立臨時分支：** 對於尚未準備提交的長期工作，建立臨時分支可能比過度依賴 stash 更好。您可以輕鬆在分支間切換並提交進度。

通過有效使用 `git stash`，即使您有未提交的變更，也可以無縫切換分支和標籤，從而實現更靈活和高效的工作流程。請記住管理您的 stash，並準備好處理潛在的合併衝突。