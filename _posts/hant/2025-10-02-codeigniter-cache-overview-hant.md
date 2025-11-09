---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 快取系統概覽
translated: true
type: note
---

### CodeIgniter 快取庫概覽

CodeIgniter 的 `CI_Cache` 類別是一個靈活的快取系統，提供統一的介面來跨各種後端（例如記憶體、檔案型或外部服務）儲存和擷取資料。它繼承了 `CI_Driver_Library`，能夠動態載入驅動程式。該類別抽象化了快取操作，讓開發者能透過配置輕鬆切換後端，無需修改應用程式程式碼。所有方法都委派給作用中的「配接器」（驅動程式類別），並具備備援支援以確保可靠性。

該系統強調效能、可移植性與容錯能力——例如，若其他驅動程式失敗，它預設會使用「虛擬」（無操作）驅動程式，確保應用程式不會因快取問題而中斷。

### 支援的快取驅動程式與配接器

該類別支援多種驅動程式，定義於 `$valid_drivers` 中：
- **apc**：使用 PHP 的 APC（Alternative PHP Cache）進行記憶體儲存（快速、內建）。
- **dummy**：不執行任何操作的佔位符（總是傳回 TRUE 或 FALSE）；用作開發/測試的備援。
- **file**：將資料以序列化檔案形式儲存在目錄中（由 `$_cache_path` 指定），適用於低流量網站。
- **memcached**：Memcached 服務的介面，用於分散式記憶體快取（高效能、可擴展）。
- **redis**：Redis 的介面，這是另一種具備發佈/訂閱與原子操作等功能的記憶體鍵值儲存。
- **wincache**：專用於 IIS 的 Windows 系統（使用 Microsoft WinCache）。

每個驅動程式都是一個獨立的類別（例如 `CI_Cache_memcached`），實作了 `get()`、`save()` 等方法。該程式庫會根據傳遞給建構函式的 `$config['adapter']` 陣列動態載入驅動程式。

### 初始化與配置

- **建構函式**：接受一個 `$config` 陣列，其中包含 `adapter`（主要驅動程式）、`backup`（備援驅動程式）和 `key_prefix`（為所有快取鍵附加的字串，用於命名空間/隔離）等鍵值。
  - 範例配置：`array('adapter' => 'redis', 'backup' => 'file', 'key_prefix' => 'myapp_')`。
- **備援邏輯**：初始化後，它會使用 `is_supported($driver)`（該方法會呼叫驅動程式的 `is_supported()` 方法，測試所需的 PHP 擴充功能或服務）來檢查主要配接器是否受支援。
  - 若主要驅動程式失敗，則切換至備援驅動程式。若兩者皆失敗，則記錄錯誤並預設使用「虛擬」驅動程式（透過 `log_message()`）。
  - 這確保快取始終有可用的配接器，防止應用程式崩潰。

`$_cache_path` 是為檔案型驅動程式設定的，但此處並未初始化——很可能在檔案驅動程式類別中處理。

### 主要方法及其運作方式

所有方法都會將 `key_prefix` 附加到 ID 前以實現唯一範圍界定（例如 `'myapp_user123'`），並委派給作用中的配接器。所有操作在成功/失敗時會傳回布林值、陣列或混合資料。

- **get($id)**：透過 ID 擷取快取資料。
  - 範例：`$data = $cache->get('user_profile');` ——呼叫配接器的 `get()` 方法。
  - 若鍵存在且未過期，則傳回資料；否則傳回 FALSE。
  - 此處不直接強制執行 TTL；由驅動程式處理（例如 Redis 或 Memcached 在內部強制執行 TTL）。

- **save($id, $data, $ttl = 60, $raw = FALSE)**：以存留時間（TTL，單位為秒）儲存資料。
  - 範例：`$cache->save('user_profile', $profile_data, 3600);` ——以 1 小時過期時間儲存。
  - `$raw` 標誌（預設為 false）表示資料是否已序列化——驅動程式會在需要時處理序列化（例如陣列/物件轉為字串）。
  - 成功時傳回 TRUE，便於條件邏輯（例如若儲存失敗則生成並快取資料）。

- **delete($id)**：移除特定的快取項目。
  - 範例：`$cache->delete('user_profile');` ——永久移除。

- **increment($id, $offset = 1)** 與 **decrement($id, $offset = 1)**：針對數值的原子操作（適用於計數器）。
  - 範例：`$new_counter = $cache->increment('hits', 5);` ——若驅動程式支援則增加 5（例如 Redis/Memcached 是原子的；檔案型可能模擬）。
  - 並非所有驅動程式都支援 raw/inc/dec（虛擬驅動程式總是失敗）；傳回新值或 FALSE。

- **clean()**：清除目前驅動程式的所有快取資料。
  - 範例：`$cache->clean();` ——在更新後刷新時很有用。
  - 「user」類型針對使用者特定資料，而非系統快取。

- **cache_info($type = 'user')**：傳回有關快取的中繼資料（例如伺服器統計、鍵計數或檔案路徑）。
  - 範例：`$info = $cache->cache_info();` ——來自驅動程式的詳細資訊陣列。

- **get_metadata($id)**：取得特定快取項目的詳細資訊（例如過期時間、大小）。
  - 範例：`$meta = $cache->get_metadata('key');` ——有助於除錯或優化。

- **is_supported($driver)**：檢查驅動程式的可用性（使用靜態 `$support` 陣列快取結果以避免重複檢查）。

### 其他機制

- **鍵前綴**：自動應用於所有 ID（例如用於應用程式隔離或多租戶）。透過配置啟用，以防止跨環境的鍵衝突。
- **記錄**：使用 `log_message()` 記錄除錯/錯誤訊息（例如備援情況），並與 CodeIgniter 的記錄系統整合。
- **靈活性與容錯能力**：透過抽象化後端，您可以以最小變更從檔案快取（廉價、本地）切換至 Redis（快速、分散式）。虛擬備援意味著快取失敗不會中斷應用程式——方法僅傳回 FALSE，讓程式碼繼續執行（例如改從資料庫擷取）。
- **效能注意事項**：像 APC/Redis 這樣的驅動程式是記憶體式的（快速存取，亞毫秒級）。檔案型則因磁碟 I/O 而較慢。TTL 通常由驅動程式遵守，除非在罕見的驅動程式特定邊緣情況中。

此設計使 CodeIgniter 的快取模組化且可靠。有關特定驅動程式的詳細資訊，請查閱驅動程式檔案（例如 `Cache_memcached.php`）。由於此程式碼來自較舊版本（約 2.0-3.x），請務必參考官方 CodeIgniter 文件以了解版本特定的細微差別。如果您有特定的方法或驅動程式需要深入了解，我可以進一步探討！