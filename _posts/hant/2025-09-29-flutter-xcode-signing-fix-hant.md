---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 修復 Flutter Xcode 代碼簽署失敗
translated: true
type: note
---

你遇到的是 Flutter / Xcode 常見的程式碼簽署失敗問題：Xcode/`security` 找不到有效的簽署身份，因此 `flutter run` 無法為實體裝置簽署應用程式。下面我將提供一套清晰有序的修復和故障排除指令 — 請選擇你想要的方式（立即在模擬器上運行，或設定簽署以在真實裝置上運行）。我不會要求更多資訊 — 我假設你想立即解決這個問題。

---

# 快速選項（選擇一項）

**A — 在模擬器上運行（無需程式碼簽署）**
如果你只想快速運行而不處理憑證：

1. 開啟模擬器：`open -a Simulator`
2. 執行 Flutter 並指定模擬器為目標：
   `flutter run -d "$(xcrun simctl list devices | grep -m1 -o "iPhone.*(Simulator)" | sed 's/ (Simulator)//')"`
   或者更簡單的方式：`flutter run -d iPhone-14`（替換為 `xcrun simctl list` 顯示的可用模擬器名稱）。

**B — 修復簽署以部署到真實裝置（推薦用於裝置測試）**
請按順序遵循以下步驟。

---

# 修復裝置部署簽署的步驟

## 1) 確認環境與基本檢查

執行這些指令並記錄輸出：

```bash
flutter doctor -v
xcode-select --print-path
xcodebuild -version
security find-identity -p codesigning -v
xcrun simctl list devices
```

`security find-identity -p codesigning -v` 應該至少顯示一個身份。你的結果顯示 `0 valid identities found` — 這就是失敗的原因。

## 2) 使用 Xcode 自動簽署（最簡單）

1. 開啟工作區：
   `open ios/Runner.xcworkspace`
2. 在 Xcode 中：選擇 `Runner` 專案 → `Runner` 目標 → **Signing & Capabilities**。
3. 將 **Team** 設定為你的 Apple ID / Apple Developer 帳戶。如果你的 Apple ID 尚未加入：

   * Xcode → Preferences → Accounts → `+` → 新增 Apple ID。
4. 勾選 **Automatically manage signing**。
5. 確保 **Bundle Identifier** 是唯一的（反向 DNS 風格，例如 `com.yourname.yourapp`）。
6. Xcode 將嘗試建立開發憑證和佈建設定檔；如果看到提示，請允許 Xcode 進行管理。

> 注意：要完整部署到任意裝置，你需要 Apple Developer 會籍（每年 99 美元）。Xcode 可以使用免費的 Apple ID 進行「免費佈建」，但功能有限（裝置數量限制，無法使用某些權利）。

## 3) 註冊你的裝置（如果需要）

如果 Xcode 無法自動註冊你的裝置，請前往 Apple Developer Portal → Certificates, IDs & Profiles → Devices → 新增裝置 UDID。你可以透過連接裝置並在 Xcode 的 Devices and Simulators 視窗中選擇它來取得裝置 UDID。

## 4) 手動產生/匯入憑證（如果你已有 p12）

如果你有 `.p12` 憑證和私密金鑰：

```bash
security import /path/to/certificate.p12 -k ~/Library/Keychains/login.keychain-db -P "P12_PASSWORD" -T /usr/bin/codesign
```

然後重新執行 `security find-identity -p codesigning -v` 以確認它出現。

## 5) 如果你希望 Xcode 為你建立憑證

在 Xcode → Accounts → 選擇你的 Apple ID → Manage Certificates → `+` → 新增 **iOS Development**。這將在你的金鑰圈中建立一個憑證，並在 `security find-identity` 中顯示。

## 6) 確保已設定 Command Line Tools

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

然後如果需要，接受許可協議：

```bash
sudo xcodebuild -license accept
```

## 7) 設定簽署後，從終端機運行

在專案根目錄下：

```bash
flutter clean
flutter pub get
flutter run
```

如果有多個裝置，請指定 `-d <device-id>`。

---

# 故障排除提示與常見陷阱

* **"0 valid identities found" 持續出現** — 確認憑證私密金鑰位於登入金鑰圈中（開啟 Keychain Access → login）。如果你匯入了憑證但沒有私密金鑰，簽署會失敗。
* **Bundle ID 不匹配** — Developer Portal 中的 App ID 必須與 Xcode 中的套件識別碼完全一致（某些情況下允許使用萬用字元）。
* **未選擇 Team** — Xcode 顯示 “No account” — 在 Xcode Preferences → Accounts 中新增 Apple ID。
* **佈建設定檔已過期** — 檢查 Developer Portal 並重新產生佈建設定檔。
* **免費佈建限制** — 如果使用免費 Apple ID，你可能需要每 7 天重新佈建，並且裝置數量有限。
* **CI / 自動化** — 使用 `fastlane match` 或 App Store Connect APIs 集中管理憑證和設定檔。
* **Codesign 權限錯誤** — 確保金鑰圈項目授予 codesign 存取權；有時你必須手動允許 `/usr/bin/codesign` 存取金鑰圈中的私密金鑰。
* **如果 `flutter run` 仍然失敗**，執行 Xcode 建置以查看更詳細的錯誤：開啟工作區並在 Xcode 中按下 Run；檢查 Signing & Capabilities 中的 UI 錯誤。

---

# 實用指令複製貼上

列出程式碼簽署身份：

```bash
security find-identity -p codesigning -v
```

匯入 `.p12`：

```bash
security import /path/to/yourcert.p12 -k ~/Library/Keychains/login.keychain-db -P "P12PASSWORD" -T /usr/bin/codesign
```

設定 Xcode command line tools：

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

開啟 iOS 工作區：

```bash
open ios/Runner.xcworkspace
```

---

# 如果你需要，我可以

* 提供確切的 Xcode 點擊步驟來逐步建立憑證/設定檔（我已經包含了核心步驟），或者
* 提供 `fastlane`/`match` 範例指令，如果你需要為多台機器/CI 進行自動化，或者
* 幫助解讀你在嘗試 Xcode 自動簽署路線後出現的任何新錯誤輸出。

告訴我你選擇了哪條路徑（立即使用模擬器 / Xcode 自動簽署 / 手動 p12 匯入 / CI）並貼上任何新的錯誤訊息（如果仍然失敗）— 我將提供後續步驟。