---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 解決 macOS 上的 CocoaPod Ruby 版本不符問題
translated: true
type: note
---

我明白問題所在了：你的系統 Ruby 和 gems 設定有些混亂，導致 `pod deintegrate` 指令找不到 CocoaPods。我們一步步來解決：

---

### 問題根源
- 你正在使用 macOS（可能是 arm64 架構的 M1/M2 機型）。
- 你透過 Homebrew 更新了 Ruby（至 3.4.1 版本）。
- 你的 `pod` 執行檔屬於舊版 Ruby（3.3.0 gem 路徑：`/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`）。
- 但現在系統使用的是 Ruby 3.4.1，因此無法在正確位置找到 `cocoapods` gems。

這種版本不匹配正是失敗的原因。

---

### 解決方案

#### 1. 使用當前運行的 Ruby 版本重新安裝 CocoaPods
```bash
gem install cocoapods
```

接著驗證：
```bash
which pod
pod --version
```

---

#### 2. 若你使用 `brew` 的 Ruby，建議也透過 Homebrew 安裝 CocoaPods
```bash
brew install cocoapods
```

這能徹底避免 Ruby 版本衝突問題。

---

#### 3. 若使用 `rbenv` 或 `rvm`，請確保處於正確的 Ruby 版本環境
例如使用 `rbenv` 時：
```bash
rbenv global 3.4.1
gem install cocoapods
```

---

#### 4. 清理舊版 pod 二進位檔的符號連結
檢查殘留的 `pod` 指令來源：
```bash
which pod
```
若指向 `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`，請刪除該連結或更新 `PATH` 以使用正確版本。

---

✅ 推薦方案（最簡易穩定）：直接執行  
```bash
brew install cocoapods
```
然後重試：
```bash
pod deintegrate
```

---

需要我幫你**修正 PATH 設定以確保始終使用正確的 pod** 二進位檔，還是只需快速重新安裝即可？