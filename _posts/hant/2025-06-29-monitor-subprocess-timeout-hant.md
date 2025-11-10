---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 監控子程序輸出並設定超時
translated: true
type: note
---

```python
import subprocess
import threading
import queue
import time
import sys

def read_output(proc, output_queue):
    """執行緒函數：讀取 stdout 和 stderr，放入佇列"""
    try:
        for line in iter(proc.stdout.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
        # 如有需要也檢查 stderr
        for line in iter(proc.stderr.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
    except Exception as e:
        output_queue.put(f"讀取輸出時發生錯誤: {e}")

def main():
    # 要執行的指令（例如在 Windows 上執行 'mvn clean compile'）
    cmd = ['mvn', 'clean', 'compile']  # 可根據需要調整，例如 ['cmd', '/c', 'mvn build']
    timeout_seconds = 10

    # 啟動子進程
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # 行緩衝
        universal_newlines=False,  # 處理位元組
        cwd=None  # 如有需要可設定工作目錄
    )

    # 輸出佇列
    output_queue = queue.Queue()

    # 啟動讀取輸出的執行緒
    output_thread = threading.Thread(target=read_output, args=(proc, output_queue))
    output_thread.daemon = True
    output_thread.start()

    print("已啟動指令。每 10 秒監控輸出一次...")

    while proc.poll() is None:
        try:
            # 等待輸出（含超時設定）
            output = output_queue.get(timeout=timeout_seconds)
            print(f"輸出: {output}")  # 可選：列印或處理輸出
        except queue.Empty:
            print(f"{timeout_seconds} 秒內無輸出。終止指令並退出。")
            proc.terminate()  # 或使用 proc.kill() 強制終止
            try:
                proc.wait(timeout=5)  # 稍等片刻以實現正常關閉
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

    # 進程正常結束
    print("指令執行完成。")
    output_thread.join()  # 等待輸出執行緒結束

if __name__ == "__main__":
    main()
```

### 說明
- **子進程**：使用 `subprocess.Popen` 執行 `mvn clean compile`（可根據需要調整指令；若只需執行 `mvn build`，可改為 `['mvn', 'build']`，或在需要時用 `cmd /c` 包裝）。透過管道非同步處理 stdout 和 stderr。
- **佇列與執行緒**：獨立執行緒逐行讀取 stdout 和 stderr（避免一次性讀取全部輸出），解碼後將各行放入 `queue.Queue`，實現非阻塞讀取。
- **超時監控**：在主執行緒中使用 `get(timeout=10)` 檢查佇列中的新輸出。若 10 秒內無輸出到達，則終止子進程並退出。
- **Windows 相容性**：`subprocess` 可在 Windows 運行。若指令需要 shell（例如當 `mvn` 不在 PATH 中時），可設定 `shell=True` 並將指令作為字串傳入：`proc = subprocess.Popen("mvn clean compile", shell=True, ...)`。
- **邊界情況處理**：若進程在等待時正常結束，循環會停止並合併執行緒。執行緒設為後台模式，避免退出時卡住。
- **自訂調整**：可修改程式以不同方式處理輸出（例如記錄到檔案而非列印）。stderr 目前合併至同一佇列，如有需要可分開處理。若輸出為二進位格式，請調整解碼方式。