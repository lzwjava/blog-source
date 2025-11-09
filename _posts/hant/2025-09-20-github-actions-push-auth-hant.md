---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 修復 GitHub Actions 推送驗證錯誤
translated: true
type: note
---

那個 403 錯誤意味著推送操作正以 **`lzwjava` 身份驗證，但使用的 token 沒有寫入權限**（通常是因為任務仍在使用預設的 `GITHUB_TOKEN`，它無法推送到其他儲存庫）。解決方法是 **為目標 checkout/推送操作注入真實的憑證**。

以下是三種可靠的方法——選擇其中一種。我會先展示最快捷的方式。

---

### 選項 A — 使用 PAT 並將其嵌入遠端（最快捷）

1. 建立一個具有 `repo` 權限的 **經典 PAT**（或具有 **Contents: Read & Write** 權限的細粒度 PAT，對象為 `lzwjava/lzwjava.github.io`）。將其儲存在原始儲存庫的 `DEPLOY_TOKEN` 秘密中。

2. 更新你的工作流程部署步驟，**強制遠端使用該 token**：

```yaml
- name: Check out destination repo
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    token: ${{ secrets.DEPLOY_TOKEN }}
    path: destination
    fetch-depth: 0

- name: Push built site to destination
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll

    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # 強制遠端明確使用 PAT（避免與 credential-helper 衝突）
    git remote set-url origin https://${{ secrets.DEPLOY_TOKEN }}@github.com/lzwjava/lzwjava.github.io.git

    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

如果你仍然看到 403，可能是你的 PAT 缺少權限範圍，或者（如果儲存庫在組織中）需要 SSO 授權。請重新生成具有 `repo` 權限的 PAT 並重試。

---

### 選項 B — 避免憑證洩漏：在首次 checkout 時停用預設憑證

有時**首次 checkout** 會將預設的 `GITHUB_TOKEN` 寫入憑證輔助程式，並在後續操作中被重複使用。停用此行為：

```yaml
- name: Check out source repo
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    persist-credentials: false   # <- 重要
```

然後按照選項 A 中的方式，使用你的 PAT 進行目標儲存庫的 checkout（如果已經可以運作，你可以跳過 `remote set-url` 這一行，但保留它也沒有壞處）。

---

### 選項 C — SSH 部署金鑰（非常穩健）

1. 在你的機器上執行：`ssh-keygen -t ed25519 -C "deploy@actions" -f deploy_key`
2. 將**公鑰** (`deploy_key.pub`) 新增為 `lzwjava/lzwjava.github.io` 的**部署金鑰**，並授予**寫入權限**。
3. 將**私鑰** (`deploy_key`) 新增為**原始**儲存庫的 `ACTIONS_DEPLOY_KEY` 秘密。

工作流程：

```yaml
- name: Check out destination repo via SSH
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    ssh-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
    path: destination
    fetch-depth: 0

- name: Push built site (SSH)
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll
    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

---

### 如果再次失敗，快速診斷方法

在推送之前執行以下命令，查看實際配置的驗證資訊：

```bash
cd destination
git remote -v
git config --get user.name
git config --get user.email
git config --get url.https://github.com/.insteadof || true
git config --global --list | sed -n 's/^credential\.helper.*/&/p'
```

如果 `remote -v` 顯示的是普通的 `https://github.com/...` **沒有**嵌入你的 PAT（選項 A），或者不是 `git@github.com:`（選項 C），那麼你仍然在使用錯誤的憑證。

---

### 常見陷阱

* **細粒度 PAT** 必須明確授予**對該特定儲存庫**的 **Contents: Read & Write** 權限。
* `main` 分支的**分支保護規則**可能會阻擋 bot 的推送（需要檢查/簽名）。如果是這種情況，請部署到未受保護的分支（例如 `gh-pages`）或調整規則。
* **PAT 過期** → 重新生成。
* **組織 SSO**（如果你的儲存庫屬於使用者，則不適用） → 為該 PAT 授權組織訪問權限。

執行以上三個選項中的一個，403 錯誤就會消失。