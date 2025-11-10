---
audio: false
generated: true
image: false
lang: ja
layout: post
title: バッテリー充電量推定修正
translated: true
type: note
---

エラー `Cannot estimate time to full charge (sysfs files not found)` は、スクリプトが `/sys/class/power_supply/BAT0/` 内に想定されるバッテリー情報ファイルを見つけられなかったことを示します。これは以下の理由で発生する可能性があります：
1. バッテリー名が `BAT0` 以外（例: `BAT1` や別の名前）である。
2. 特定のファイル（`charge_now`, `charge_full`, `current_now`）が利用できない、またはお使いのLenovoノートパソコンで異なる名前を持っている。
3. スクリプトを実行しているユーザーがこれらのファイルへのアクセス権限を持っていない。

以下は、バッテリー名を動的に検出し、sysfsファイル名のバリエーション（例: 一部のシステムでは `charge_now` の代わりに `energy_now` を使用）を処理する修正済みPythonスクリプトです。また、より優れたエラーハンドリングと権限チェックも含まれています：

```python
import psutil
import os
import glob

def find_battery_path():
    """Find the battery directory in /sys/class/power_supply."""
    battery_paths = glob.glob('/sys/class/power_supply/BAT*')
    if not battery_paths:
        return None
    return battery_paths[0]  # Return the first battery found (e.g., BAT0 or BAT1)

def get_battery_info():
    try:
        # Get battery information using psutil
        battery = psutil.sensors_battery()
        
        if battery is None:
            print("No battery detected.")
            return

        # Battery percentage
        percent = battery.percent
        print(f"Battery Percentage: {percent:.2f}%")

        # Check if battery is charging
        is_charging = battery.power_plugged
        status = "Charging" if is_charging else "Discharging"
        print(f"Status: {status}")

        # Estimate remaining time (only when discharging)
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"Estimated Time Remaining: {hours} hours, {minutes} minutes")
        elif is_charging:
            # Try to estimate time to full charge using sysfs
            battery_path = find_battery_path()
            if not battery_path:
                print("Cannot estimate time to full charge (no battery found in sysfs).")
                return

            try:
                # Check for charge or energy-based files
                charge_now_file = os.path.join(battery_path, 'charge_now')
                energy_now_file = os.path.join(battery_path, 'energy_now')
                charge_full_file = os.path.join(battery_path, 'charge_full')
                energy_full_file = os.path.join(battery_path, 'charge_full_design')
                current_now_file = os.path.join(battery_path, 'current_now')

                # Determine which files to use (charge or energy)
                if os.path.exists(charge_now_file) and os.path.exists(charge_full_file):
                    now_file, full_file = charge_now_file, charge_full_file
                elif os.path.exists(energy_now_file) and os.path.exists(energy_full_file):
                    now_file, full_file = energy_now_file, energy_full_file
                else:
                    print("Cannot estimate time to full charge (charge/energy files not found).")
                    return

                # Read battery data
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
                    print(f"Estimated Time to Full Charge: {hours} hours, {minutes} minutes")
                else:
                    print("Cannot estimate time to full charge (current_now is 0).")
            except PermissionError:
                print("Cannot estimate time to full charge (permission denied). Try running with sudo.")
            except FileNotFoundError:
                print(f"Cannot estimate time to full charge (sysfs files not found in {battery_path}).")
            except Exception as e:
                print(f"Error estimating time to full charge: {e}")
        else:
            print("No remaining time estimate available.")

    except Exception as e:
        print(f"Error retrieving battery information: {e}")

if __name__ == "__main__":
    get_battery_info()
```

### 変更点
1. **動的なバッテリー検出**:
   - ハードコーディングされた `BAT0` の代わりに `glob.glob('/sys/class/power_supply/BAT*')` を使用してバッテリーディレクトリ（例: `BAT0`, `BAT1`）を検索します。
   - 見つかった最初のバッテリーを返すか、バッテリーが検出されない場合は `None` を返します。

2. **ChargeファイルとEnergyファイルのサポート**:
   - 一部のシステムでは電荷ベース（マイクロアンペア時間）の代わりにエネルギー基準（ワット時）を使用するため、`charge_now`/`charge_full` と `energy_now`/`energy_full` の両方のファイルをチェックします。
   - 利用可能性に基づいて適切なファイルのペアを選択します。

3. **改善されたエラーハンドリング**:
   - アクセスが拒否された場合に `sudo` での実行を提案するために、`PermissionError` を個別に処理します。
   - sysfsファイルが見つからない場合や `current_now` がゼロの場合に具体的なフィードバックを提供します。

4. **フォーマットされた出力**:
   - 出力をよりクリーンにするために、バッテリー残量を小数点以下2桁に制限しています（`{percent:.2f}`）。

### 使用方法
1. **`psutil` のインストール（まだインストールされていない場合）**:
   ```bash
   sudo pip3 install psutil
   ```

2. **スクリプトの保存**:
   - 更新されたスクリプトを、例えば `battery_info.py` として保存します。

3. **スクリプトの実行**:
   - ターミナルで実行します：
     ```bash
     python3 battery_info.py
     ```
   - 「権限が拒否されました」エラーが発生した場合は、昇格された権限で実行してみてください：
     ```bash
     sudo python3 battery_info.py
     ```

4. **バッテリーパスの確認**:
   - バッテリー名と利用可能なファイルを確認するには、以下を実行します：
     ```bash
     ls /sys/class/power_supply
     ```
     次に、バッテリーディレクトリ（例: `BAT0` または `BAT1`）の内容を確認します：
     ```bash
     ls /sys/class/power_supply/BAT0
     ```
   - `charge_now`, `charge_full`, `energy_now`, `energy_full`, `current_now` などのファイルを探してください。もしこれらが異なる場合（例: `charge_full` の代わりに `energy_full_design`）、スクリプトは対応するはずですが、さらに調整が必要な場合はお知らせください。

### デバッグのヒント
- スクリプトがまだ「sysfs files not found」を報告する場合は、`/sys/class/power_supply/BAT*` 内の正確なファイル名を確認してください。一部のLenovoノートパソコンでは、非標準の名前を使用しているか、sysfsサポートが限られている可能性があります。
- 「権限が拒否されました」が表示された場合は、`sudo` で実行すると解決するはずですが、昇格された権限の使用には注意してください。
- バッテリーは検出されるが時間の推定が提供されない場合、`current_now` がゼロであるため（システムが充電電流を積極的に報告していない場合に一般的）である可能性があります。この場合、スクリプトは推定が利用できないことを示すようにフォールバックします。

### 出力例
お使いのシステム（Lenovo XiaoXin-14-IAH8）では、以下のような表示がされる可能性があります：
```
Battery Percentage: 49.62%
Status: Charging
Estimated Time to Full Charge: 1 hours, 45 minutes
```
または、ファイルがまだ見つからない場合：
```
Battery Percentage: 49.62%
Status: Charging
Cannot estimate time to full charge (sysfs files not found in /sys/class/power_supply/BAT0).
```

### 問題が解決しない場合
スクリプトが依然としてsysfsファイルを見つけられない場合は、以下の出力を共有してください：
```bash
ls -l /sys/class/power_supply
ls -l /sys/class/power_supply/BAT*/*
```
これにより、正確なファイル名と権限を特定できます。それに基づいて、お使いのシステムの構成に合わせてスクリプトをさらに調整できます。

[psutil Documentation](https://psutil.readthedocs.io/en/latest/)  
[Linux sysfs Power Supply](https://www.kernel.org/doc/html/latest/power/power_supply_class.html)