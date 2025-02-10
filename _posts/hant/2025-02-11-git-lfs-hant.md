---
audio: false
lang: hant
layout: post
title: Git大型檔案儲存庫
translated: true
---

Git 大型檔案儲存庫 (Git LFS) 用於管理 Git 中的大型檔案。

### 安裝

```bash
brew install git-lfs # macOS
sudo apt-get install git-lfs # Ubuntu/Debian
git lfs install
```

### 使用方法

```bash
git lfs track "*.psd"
git add .gitattributes
git add path/to/your/largefile.psd
git commit -m "Add large file with Git LFS"
git push origin main
git clone https://github.com/user/repo.git
git lfs pull
```

### 設定

確保遠端儲存庫支援 Git LFS。

```bash
git lfs ls-files
```

### 提示

```bash
git lfs migrate import --include="*.psd"
```
