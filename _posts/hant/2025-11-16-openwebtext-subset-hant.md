---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 下載部分開放網絡文本
translated: true
type: note
---

啊，明白了——您想繼續使用 **Hugging Face CLI**，但只下載一小部分資料。問題在於：CLI 的設計是下載**完整檔案**而非片段。OpenWebText 被分割成 21 個 `.tar` 子集檔案；若使用 CLI，它會下載整個壓縮檔，因此您無法精確取得「1%」的資料而不下載大量檔案。

以下是實用解決方案：

---

### 1. 僅下載部分檔案

與其下載全部 21 個檔案，不如只選擇幾個壓縮檔：

```bash
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset00.tar \
  --local-dir ./openwebtext
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset01.tar \
  --local-dir ./openwebtext
```

* 每個壓縮檔約 625MB，若下載 1–2 個，約佔資料集的 1–2%
* 可自由調整選擇的子集，HF 不強制要求順序下載

---

### 2. 僅解壓所需內容

下載完成後：

```bash
cd ./openwebtext
tar -xvf urlsf_subset00.tar
tar -xvf urlsf_subset01.tar
```

接著您可從這些子集中僅處理部分文檔

---

### 3. 選項：結合 HF Transfer 加速

若要加速 CLI 下載：

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

重新執行 CLI 指令後，下載速度將大幅提升

---

如果您需要，我可以製作**自動選取約 1% OpenWebText 資料的簡便指令腳本**，無需手動選擇壓縮檔。需要我為您準備嗎？