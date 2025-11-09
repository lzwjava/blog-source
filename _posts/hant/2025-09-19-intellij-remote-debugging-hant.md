---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: IntelliJ 遠端偵錯設定指南
translated: true
type: note
---

簡短回答：可以——只要保持建置版本與運行中的 JVM 同步，IntelliJ 遠端偵錯就能順利附加。以下提供一個在本地 Liberty 和 Cloud Foundry 上皆可運行的可靠方法。

## 1) 在附加偵錯前預防「類別不符」問題

* 始終保持 JDK 版本一致：Maven 編譯使用的 JDK、Liberty 的 JVM 以及（若在 CF 上）Java buildpack 的 JDK 主要版本必須相符。在 Maven 中，透過 `maven-compiler-plugin`（使用 `release` 或 `source/target` 參數）鎖定版本，並確保 Liberty/CF 使用相同版本。
* 切換分支或模組時清理過時的位元組碼：執行 `mvn clean package -DskipTests` 是最簡單的防護措施。
* 在 IntelliJ 中，若先前混用了 IDE 建置和 Maven 建置，請執行一次「Rebuild Project」。

## 2) 僅在必要時自動重建（30分鐘規則）

若希望僅在編譯後的類別檔案超過 30 分鐘時才重建，可以用一個簡短的檢查腳本包裹 Maven 命令。

### Bash (macOS/Linux)

```bash
#!/usr/bin/env bash
set -euo pipefail

CLASSES_DIR="target/classes"
THRESHOLD_MIN=30

needs_build() {
  # 尚未有類別檔案？
  [[ ! -d "$CLASSES_DIR" ]] && return 0
  # 最新的類別修改時間超過閾值？
  last_mod_epoch=$(find "$CLASSES_DIR" -type f -name '*.class' -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
  [[ -z "${last_mod_epoch:-}" ]] && return 0
  now_epoch=$(date +%s)
  diff_min=$(( ( now_epoch - ${last_mod_epoch%.*} ) / 60 ))
  (( diff_min >= THRESHOLD_MIN ))
}

if needs_build; then
  echo "Classes are old (>= ${THRESHOLD_MIN}m) or missing — building…"
  mvn clean package -DskipTests
else
  echo "Classes are fresh (< ${THRESHOLD_MIN}m) — skipping build."
fi
```

### PowerShell (Windows)

```powershell
$classes = "target\classes"
$thresholdMin = 30

function Needs-Build {
  if (-not (Test-Path $classes)) { return $true }
  $last = Get-ChildItem $classes -Recurse -Filter *.class |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
  if (-not $last) { return $true }
  $age = (New-TimeSpan -Start $last.LastWriteTime -End (Get-Date)).TotalMinutes
  return ($age -ge $thresholdMin)
}

if (Needs-Build) {
  Write-Host "Classes are old (>= $thresholdMin m) or missing — building…"
  mvn clean package -DskipTests
} else {
  Write-Host "Classes are fresh (< $thresholdMin m) — skipping build."
}
```

## 3) Liberty（本地）— 以偵錯模式啟動並從 IntelliJ 附加

你有兩個簡單的選擇：

**A. 一次性偵錯啟動**

```bash
server debug myServer   # 預設 JDWP 端口為 7777
```

**B. 永久配置**

* 在 `wlp/usr/servers/myServer/jvm.options` 中：

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777
```

* 或透過環境變數：

```
WLP_DEBUG_ADDRESS=7777
WLP_DEBUG_SUSPEND=false
```

**IntelliJ 附加步驟**

* 執行 → 「Edit Configurations…」 → 「Remote JVM Debug」。
* Host: `localhost`, Port: `7777`。
* 點擊 Debug；你應該會看到「Connected to the target VM…」且中斷點會綁定。

> 提示：重建後，Liberty 會透過熱交換加載大多數功能的更新類別。若方法簽名或類別結構已變更，則需要重啟伺服器才能加載這些變更。

## 4) Cloud Foundry (PCF) — 實際可行方案

CF 透過其路由層運行應用程式；通常無法直接暴露 JDWP 端口。你有兩種可行的模式：

**選項 1：Buildpack 偵錯 + SSH 通道（僅適用於開發/預發環境）**

1. 在 Java buildpack 中啟用 JVM 偵錯：

   * 推送前設定環境變數（名稱因 buildpack 版本而略有不同）：

   ```
   cf set-env <APP> JBP_CONFIG_DEBUG '{enabled: true, port: 7777}'
   ```
2. 重新部署：

   ```
   cf restage <APP>
   ```
3. 開啟 SSH 通道：

   ```
   cf ssh -N -L 7777:localhost:7777 <APP>
   ```
4. 在 IntelliJ 中附加到 `localhost:7777`。

**選項 2：使用 CF SSH JMX/診斷工具替代 JDWP**

* 當不允許直接使用 JDWP 時，可依賴：

  * 應用程式日誌 + 定向記錄器，
  * 透過 `cf ssh` + `jcmd`/`jmap`（如果存在）取得執行緒/堆積轉儲，
  * 功能旗標如 Liberty 的追蹤和健康狀態端點。

> 現實考量：許多 CF 組織在生產環境中禁用偵錯端口。將在 CF 上的遠端 JDWP 視為僅適用於非生產環境的偵錯途徑。若你的平台團隊封鎖此功能，請回退至日誌 + SSH 診斷。

## 5) 常見「無法綁定中斷點」的原因（及解決方法）

* **類別檔案不符**：執行清理重建；確認運行時類別路徑上僅存在一份類別副本（注意 fat JAR 或重複模組）。
* **錯誤的 JDWP 端口**：確認 Liberty 實際正在監聽（本地可查看 `server debug` 日誌或使用 `netstat`；對於 CF，SSH 通道行必須匹配）。
* **JDK 主要版本不同**：確保 Maven/Liberty/CF 的 JDK 版本一致（例如均為 Java 17）。
* **編譯器偵錯資訊被移除**：確保 `maven-compiler-plugin` 未使用 `-g:none`。預設設定即可；若自定義，請包含 `-g`。
* **需要重新載入**：簽名變更後，重啟 Liberty（或在 CF 上重新部署）。

---

若按照上述方式設定——無論是始終執行 `mvn clean package` 還是使用「30分鐘新鮮度」包裹腳本——IntelliJ 遠端偵錯都能可靠地附加到 Liberty，並且在非生產環境中可透過 SSH 通道在 CF 上運行。