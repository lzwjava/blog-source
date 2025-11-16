---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 無 Blob 的 Git 克隆優勢
translated: true
type: note
---

Git 指令：

```bash
git clone --filter=blob:none <repository-url>
```

是一種**部分克隆**操作，在檢出時**幾乎不下載任何檔案內容**（blob）。以下是其具體作用與實用價值：

### `--filter=blob:none` 的意義
- `--filter=blob:none` 指示 Git 採用**無 blob 克隆**模式
- Git 仍會下載：
  - 所有提交記錄（歷史）
  - 所有樹狀物件（目錄結構）
  - 所有引用/分支/標籤
- 但在初始克隆過程中**完全不下載檔案內容**（blob）
- 當後續執行 `git checkout` 或切換分支時，Git 僅會按需下載工作樹所需的檔案內容

### 核心優勢
- 實現極速輕量初始克隆（即便是 Linux 核心、Android 或 Windows 源碼等大型存儲庫，通常僅需數 MB）
- 初期大幅節省網絡頻寬與磁碟空間
- 特別適用於 CI/CD 流程、快速查閱，或僅需歷史記錄而不須檢出檔案的情境（例如執行 `git log`、追溯註解、跨提交比較）

### 實際容量對照範例

| 存儲庫          | 普通克隆    | `blob:none` 克隆 | 速度提升        |
|-----------------|-------------|------------------|-----------------|
| torvalds/linux  | ~5+ GB      | ~300–400 MB      | 10–20 倍加速    |
| microsoft/vscode| ~2–3 GB     | ~200 MB          | 顯著提升        |

### 無 blob 克隆後常用後續指令
```bash
# 首次需要工作樹時：
git checkout <branch>        # 僅下載必要 blob

# 若後續需完整內容：
git fetch --unshallow        # 無 blob 模式無需此操作
# 永久補齊缺失 blob：
git repack -a -d             # 可選操作，強制下載所有 blob
```

### 相關過濾器選項
- `--filter=blob:none` → 初始完全不下載 blob（最激進模式）
- `--filter=tree:0`    → 下載樹狀結構但排除 blob（類似效果）
- `--filter=sparse:oid=<oid>` → 配合稀疏檢出的部分 blob 模式

### 總結
```bash
git clone --filter=blob:none https://github.com/example/repo.git
```
= 「立即獲取完整歷史與結構，檔案內容按需延後下載」  
特別適合巨型單一存儲庫，或需要快速瀏覽歷史而無需長時間等待的場景。