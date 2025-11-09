---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: macOS 預設守護行程
translated: true
type: note
---

### macOS 中的預設守護行程

在 macOS 中，守護行程是沒有使用者介面的背景服務，通常會在開機時或依需求啟動。它們由 **launchd**（系統的初始化與服務管理框架，PID 1）管理。守護行程與代理程式不同：守護行程以 root/系統全域權限執行（登入前），而代理程式則以每位使用者為單位執行（登入後）。

預設系統守護行程定義在位於 `/System/Library/LaunchDaemons/` 的屬性清單 (.plist) 檔案中。標準安裝通常約有 300–350 個這類行程（例如，macOS 10.14 Mojave 上有 339 個），涵蓋從網路、安全到硬體管理的所有層面。使用者安裝或第三方的守護行程則放在 `/Library/LaunchDaemons/`。

#### 如何檢視預設守護行程
要在終端機中列出所有已載入的守護行程（及代理程式）：
- `sudo launchctl list`（顯示系統全域的守護行程和代理程式）。
- `launchctl list`（僅顯示使用者特定的代理程式）。

若要取得完整目錄列表：`ls /System/Library/LaunchDaemons/`（無需 sudo，但檔案為唯讀）。

這些指令會輸出如 PID、狀態和標籤（例如 `com.apple.timed`）等欄位。

#### "timed" 守護行程
您特別提到了 "timed"，這指的是 **com.apple.timed**（時間同步守護行程）。這是一個在 macOS High Sierra (10.13) 中引入的核心系統守護行程，用以取代舊有的 `ntpd` 行程。

- **目的**：它會自動將 Mac 的系統時鐘與 NTP（網路時間協定）伺服器同步以確保準確性，每 15 分鐘查詢一次。這能為日誌、憑證和網路操作提供精確的計時。
- **運作方式**：由 launchd 從 `/System/Library/LaunchDaemons/com.apple.timed.plist` 啟動，以 `_timed` 使用者身份執行（屬於 `_timed` 和 `_sntpd` 群組）。它使用 `settimeofday` 系統呼叫，根據伺服器回應來調整時鐘。設定位於 `/etc/ntpd.conf`（NTP 伺服器），狀態則快取在 `/var/db/timed/com.apple.timed.plist`。
- **相關資訊**：與「系統設定」>「一般」>「日期與時間」>「自動設定日期與時間」相關。若停用此選項，timed 將不會同步。對於進階設定（例如高精度需求），可以使用如 Chrony 等工具取代它，但需停用 timed。

如果您的時鐘出現漂移，請檢查網路問題或防火牆是否阻擋了 NTP（UDP 埠 123）。

#### 其他常見的預設守護行程 ("等等")
以下是一些經常執行的預設系統守護行程表格，按功能分組。這並非完整列表（有數百個），但涵蓋了基本項目。標籤來自 .plist 檔案名稱。

| 類別           | 守護行程標籤                     | 描述 |
|----------------|-------------------------------|-------------|
| **核心系統**   | `com.apple.launchd`          | launchd 行程本身；啟動所有其他行程。 |
| **時間與同步** | `com.apple.timed`             | NTP 時間同步（如上所述）。 |
| **使用者管理** | `com.apple.opendirectoryd`   | 處理使用者/群組帳戶和目錄服務。 |
| **使用者管理** | `com.apple.accounts`         | 管理使用者帳戶和驗證。 |
| **網路**       | `com.apple.mDNSResponder`    | Bonjour/mDNS，用於區域網路探索（例如 AirDrop）。 |
| **網路**       | `com.apple.nesessionmanager` | 網路擴充功能和 VPN 管理。 |
| **藍牙/無線** | `com.apple.bluetoothd`      | 藍牙裝置處理。 |
| **iCloud/同步**| `com.apple.cloudd`            | iCloud 資料同步與服務。 |
| **安全**       | `com.apple.securityd`        | 鑰匙圈和憑證管理（通常也作為代理程式執行）。 |
| **更新**       | `com.apple.softwareupdated`  | 處理軟體更新和目錄下載。 |
| **硬體**       | `com.apple.kextd`             | 核心擴充功能的載入與管理。 |
| **記錄**       | `com.apple.systemnotificationd` | 系統通知與記錄。 |
| **MDM（若啟用）** | `com.apple.mdmclient`     | 企業設定中的行動裝置管理客戶端。 |

這些行程會持續執行或在觸發時執行，以維持 macOS 的穩定性。如果某個行程行為異常（例如 CPU 使用率過高），您可以暫時使用 `sudo launchctl unload /System/Library/LaunchDaemons/com.apple.example.plist` 將其卸載，但請避免修改系統檔案。

若要取得您 Mac 上完整的最新列表（截至 2025 年 10 月，可能為 macOS 15 Sequoia 或更新版本），請執行上述指令——版本會隨著更新而略有演變。

#### 參考資料
- [The macOS Process Journey — “timed” (Time Sync Daemon)](https://medium.com/@boutnaru/the-macos-process-journey-timed-time-sync-daemon-4898c8185b4b)
- [Daemons and Agents could be slowing down your Mac](https://appleinsider.com/inside/macos/tips/daemons-and-agents-could-be-slowing-down-your-mac)
- [What files are included in the /System/Library/LaunchAgents and /System/Library/LaunchDaemons](https://apple.stackexchange.com/questions/361029/what-files-are-included-in-the-system-library-launchagents-and-system-library)
- [Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- [How to show all running launchctl daemons/agents?](https://apple.stackexchange.com/questions/134817/how-to-show-all-running-launchctl-daemons-agents)