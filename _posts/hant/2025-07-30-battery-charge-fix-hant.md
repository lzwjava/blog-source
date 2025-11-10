---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 電池電量估算修正
translated: true
type: note
---

錯誤 `Cannot estimate time to full charge (sysfs files not found)` 表示腳本無法在 `/sys/class/power_supply/BAT0/` 中找到預期的電池資訊檔案。可能原因包括：
1. 電池名稱不是 `BAT0`（例如可能是 `BAT1` 或其他名稱）。
2. 特定檔案（`charge_now`、`charge_full`、`current_now`）在您的 Lenovo 筆記型電腦上不可用或名稱不同。
3. 執行腳本的使用者缺乏存取這些檔案的權限。

以下是修訂後的 Python 腳本，可動態偵測電池名稱並處理 sysfs 檔案名稱的變體（例如某些系統使用 `energy_now` 而非 `charge_now`）。同時包含更完善的錯誤處理和權限檢查：

```python
import psutil
import os
import glob

def find_battery_path():
    """在 /sys/class/power_supply 中尋找電池目錄"""
    battery_paths = glob.glob('/sys/class/power_supply/BAT*')
    if not battery_paths:
        return None
    return battery_paths[0]  # 返回找到的第一個電池（例如 BAT0 或 BAT1）

def get_battery_info():
    try:
        # 使用 psutil 獲取電池資訊
        battery = psutil.sensors_battery()
        
        if battery is None:
            print("未偵測到電池。")
            return

        # 電池百分比
        percent = battery.percent
        print(f"電池百分比：{percent:.2f}%")

        # 檢查電池是否正在充電
        is_charging = battery.power_plugged
        status = "充電中" if is_charging else "放電中"
        print(f"狀態：{status}")

        # 估算剩餘時間（僅在放電時）
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"預計剩餘時間：{hours} 小時 {minutes} 分鐘")
        elif is_charging:
            # 嘗試使用 sysfs 估算充滿電所需時間
            battery_path = find_battery_path()
            if not battery_path:
                print("無法估算充滿電時間（在 sysfs 中未找到電池）。")
                return

            try:
                # 檢查充電量或能量相關檔案
                charge_now_file = os.path.join(battery_path, 'charge_now')
                energy_now_file = os.path.join(battery_path, 'energy_now')
                charge_full_file = os.path.join(battery_path, 'charge_full')
                energy_full_file = os.path.join(battery_path, 'charge_full_design')
                current_now_file = os.path.join(battery_path, 'current_now')

                # 決定使用哪組檔案（充電量或能量）
                if os.path.exists(charge_now_file) and os.path.exists(charge_full_file):
                    now_file, full_file = charge_now_file, charge_full_file
                elif os.path.exists(energy_now_file) and os.path.exists(energy_full_file):
                    now_file, full_file = energy_now_file, energy_full_file
                else:
                    print("無法估算充滿電時間（未找到充電量/能量檔案）。")
                    return

                # 讀取電池數據
                with open(now_file, 'r') as f:
                    charge_now = int(f.read().strip())
                with open(full_file, 'r') as f:
                    charge_full = int(f.read().strip())
                with open(current_now_file, 'r') as f:
                    current_now = int(f.read().strip())

                if current_now > 0:
                    charge_remaining = charge_full - charge_now
                    seconds_to_full = (charge_remaining / current_now) * 3600
                    hours = int(seconds_to_full // 3600)
                    minutes = int((seconds_to_full % 3600) // 60)
                    print(f"預計充滿電時間：{hours} 小時 {minutes} 分鐘")
                else:
                    print("無法估算充滿電時間（current_now 為 0）。")
            except PermissionError:
                print("無法估算充滿電時間（權限不足）。請嘗試使用 sudo 執行。")
            except FileNotFoundError:
                print(f"無法估算充滿電時間（在 {battery_path} 中未找到 sysfs 檔案）。")
            except Exception as e:
                print(f"估算充滿電時間時發生錯誤：{e}")
        else:
            print("無可用剩餘時間估算。")

    except Exception as e:
        print(f"獲取電池資訊時發生錯誤：{e}")

if __name__ == "__main__":
    get_battery_info()
```

### 修改內容
1. **動態電池偵測**：
   - 使用 `glob.glob('/sys/class/power_supply/BAT*')` 尋找電池目錄（例如 `BAT0`、`BAT1`），而非硬編碼 `BAT0`。
   - 返回找到的第一個電池，若未偵測到電池則返回 `None`。

2. **支援充電量與能量檔案**：
   - 檢查 `charge_now`/`charge_full` 和 `energy_now`/`energy_full` 檔案，因某些系統使用基於能量的度量單位（瓦時）而非基於充電量（微安時）。
   - 根據可用性選擇適當的檔案組。

3. **改進錯誤處理**：
   - 單獨處理 `PermissionError`，建議在存取被拒時使用 `sudo` 執行。
   - 當 sysfs 檔案未找到或 `current_now` 為零時提供具體反饋。

4. **格式化輸出**：
   - 將電池百分比限制為兩位小數（`{percent:.2f}`）使輸出更簡潔。

### 使用方式
1. **安裝 `psutil`（若尚未安裝）**：
   ```bash
   sudo pip3 install psutil
   ```

2. **儲存腳本**：
   - 將更新後的腳本儲存為，例如 `battery_info.py`。

3. **執行腳本**：
   - 在終端機中執行：
     ```bash
     python3 battery_info.py
     ```
   - 若出現「權限不足」錯誤，請嘗試使用較高權限執行：
     ```bash
     sudo python3 battery_info.py
     ```

4. **檢查電池路徑**：
   - 為驗證電池名稱和可用檔案，請執行：
     ```bash
     ls /sys/class/power_supply
     ```
     接著檢查電池目錄內容（例如 `BAT0` 或 `BAT1`）：
     ```bash
     ls /sys/class/power_supply/BAT0
     ```
   - 尋找如 `charge_now`、`charge_full`、`energy_now`、`energy_full` 或 `current_now` 等檔案。若名稱不同（例如使用 `energy_full_design` 而非 `charge_full`），腳本應能處理，但若需進一步調整請告知。

### 除錯提示
- 若腳本仍回報「未找到 sysfs 檔案」，請檢查 `/sys/class/power_supply/BAT*` 中的確切檔案名稱。部分 Lenovo 筆記型電腦可能使用非標準名稱或 sysfs 支援有限。
- 若看到「權限不足」，使用 `sudo` 執行應可解決，但請謹慎使用高權限。
- 若電池已偵測但未提供時間估算，可能是因 `current_now` 為零（常見於系統未主動回報充電電流時）。此時腳本將回退至顯示無可用估算。

### 範例輸出
在您的系統（Lenovo XiaoXin-14-IAH8）上可能看到：
```
電池百分比：49.62%
狀態：充電中
預計充滿電時間：1 小時 45 分鐘
```
若檔案仍缺失：
```
電池百分比：49.62%
狀態：充電中
無法估算充滿電時間（在 /sys/class/power_supply/BAT0 中未找到 sysfs 檔案）。
```

### 若問題持續
若腳本仍無法找到 sysfs 檔案，請提供以下指令輸出：
```bash
ls -l /sys/class/power_supply
ls -l /sys/class/power_supply/BAT*/*
```
這有助於識別確切的檔案名稱和權限設定。我可據此進一步調整腳本以匹配您的系統配置。

[psutil 文件](https://psutil.readthedocs.io/en/latest/)  
[Linux sysfs 電源供應](https://www.kernel.org/doc/html/latest/power/power_supply_class.html)