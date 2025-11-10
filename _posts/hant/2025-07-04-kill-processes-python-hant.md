---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用Python終止進程
translated: true
type: note
---

### 使用 Python 終止 Windows 程序

若要在 Windows 上以程式化方式終止程序，主要會使用 `subprocess` 模組來呼叫系統指令如 `taskkill`。`signal` 模組專注於 Unix 系統，在 Windows 上無法可靠處理程序終止（像 SIGKILL 這樣的信號並非原生支援；`os.kill()` 可發送有限信號，但並非完整程序終止的理想方案）。`platform` 模組可協助確認當前處於 Windows 環境以實現作業系統特定行為。

#### 步驟 1：安裝並匯入模組
- `subprocess`、`signal` 和 `platform` 皆屬於 Python 標準函式庫，無需額外安裝。
- 匯入範例：

```python
import subprocess
import platform
import os  # 如需存取 PID 時使用
```

#### 步驟 2：偵測 Windows 作業系統（使用 `platform`）
- 確認執行環境以避免跨平台問題：

```python
if platform.system() == 'Windows':
    print("運行於 Windows 環境 - 使用相容的終止方法。")
```

#### 步驟 3：終止程序
- 要透過程序 ID (PID) 或名稱終止現有程序，請透過 `subprocess` 使用 `taskkill`。這是可靠的 Windows 原生方式，因為 `subprocess.terminate()` 或 `.kill()` 僅對透過 `subprocess.Popen` 啟動的程序有效。
- 範例：透過 PID 終止程序（使用 `/F` 參數強制終止）。請將 `1234` 替換為實際 PID。

```python
def kill_process_by_pid(pid):
    try:
        subprocess.call(['taskkill', '/PID', str(pid), '/F'])
        print(f"程序 {pid} 已終止。")
    except subprocess.CalledProcessError as e:
        print(f"終止程序 {pid} 失敗：{e}")

# 使用方式
kill_process_by_pid(1234)
```

- 透過程序名稱終止（例如 'notepad.exe'），此操作將終止所有符合名稱的程序：

```python
def kill_process_by_name(name):
    try:
        subprocess.call(['taskkill', '/IM', name, '/F'])
        print(f"符合 '{name}' 的程序已終止。")
    except subprocess.CalledProcessError as e:
        print(f"終止程序 '{name}' 失敗：{e}")

# 使用方式
kill_process_by_name('notepad.exe')
```

#### 限制與注意事項
- `subprocess` 會呼叫外部指令，請確保腳本具有適當權限（例如需以管理員身份執行系統程序）。
- 對於透過 `subprocess.Popen` 啟動的程序，可直接使用 `.terminate()`（禮貌關閉）或 `.kill()`（強制終止）：

```python
proc = subprocess.Popen(['notepad.exe'])  # 啟動程序
proc.kill()  # 終止程序
```

- `signal` 模組：在 Windows 上使用 `os.kill(pid, signal.SIGTERM)` 可能對某些信號有效（Python 3.2+），但穩定性較差且可能無法終止所有程序。例如：

```python
import signal
os.kill(pid, signal.SIGTERM)  # 可能溫和關閉；但無法保證成功
```

請避免依賴 `signal` 模組進行 Windows 程序終止——為獲得最佳效果，請堅持使用 `subprocess` 搭配 `taskkill`。

若需列出 PID（例如透過 `tasklist` 指令），可先進行查詢以便動態終止。如需更高階的程序管理功能，可考慮使用第三方函式庫如 `psutil`，但上述方法僅使用標準模組。