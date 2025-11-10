---
audio: false
generated: true
lang: hant
layout: post
title: 模擬Python中的觸發器
translated: true
type: note
---

讓我們建立一個簡單的 Python 程式來模擬先前描述的不同類型正反器（RS、D、JK 和 T）的行為。由於正反器是硬體元件，我們將在 Python 類別中模擬其邏輯，以模仿它們的行為，包括輸入、輸出和狀態變化。該程式允許我們輸入正反器控制值（如 S、R、D、J、K、T 和 Clock）並根據其規則顯示輸出（Q）。我們將保持簡單且基於文本，適合初學者理解，並提供命令列介面來測試每個正反器。

計劃如下：
- 建立一個基礎 `FlipFlop` 類別來處理常見屬性，如當前狀態（Q）。
- 為 `RSFlipFlop`、`DFlipFlop`、`JKFlipFlop` 和 `TFlipFlop` 建立特定類別，每個類別實現其獨特的行為。
- 通過要求「tick」來更新狀態，模擬時鐘，模仿正反器在時鐘脈衝上的工作方式。
- 提供一個簡單的互動循環，通過輸入值並查看輸出來測試每個正反器。
- 使用 print 語句顯示狀態變化，保持清晰且具有教育意義。

該程式不會使用任何外部庫（如 pygame），因為我們只是模擬邏輯，它將在標準 Python 環境中運行。成品將是一個 Python 腳本，您可以運行它來實驗正反器。

```python
# 所有正反器的基礎類別
class FlipFlop:
    def __init__(self):
        self.Q = 0  # 當前狀態（輸出）
        self.Q_next = 0  # 下一個狀態（在時鐘 tick 時更新）

    def get_output(self):
        return self.Q

    def tick(self):
        self.Q = self.Q_next  # 在時鐘 tick 時更新狀態

# RS 正反器
class RSFlipFlop(FlipFlop):
    def update(self, S, R):
        if S == 1 and R == 1:
            print("警告：無效狀態 (S=1, R=1) - 無變化")
            return
        elif S == 1 and R == 0:
            self.Q_next = 1  # 設置
        elif S == 0 and R == 1:
            self.Q_next = 0  # 重置
        # 如果 S=0, R=0，保持先前狀態（Q_next 無變化）

# D 正反器
class DFlipFlop(FlipFlop):
    def update(self, D):
        self.Q_next = D  # 輸出將在下一個時鐘 tick 時變為 D

# JK 正反器
class JKFlipFlop(FlipFlop):
    def update(self, J, K):
        if J == 0 and K == 0:
            pass  # 無變化
        elif J == 0 and K == 1:
            self.Q_next = 0  # 重置
        elif J == 1 and K == 0:
            self.Q_next = 1  # 設置
        elif J == 1 and K == 1:
            self.Q_next = 1 - self.Q  # 切換

# T 正反器
class TFlipFlop(FlipFlop):
    def update(self, T):
        if T == 0:
            pass  # 無變化
        elif T == 1:
            self.Q_next = 1 - self.Q  # 切換

# 獲取有效二進制輸入（0 或 1）的函數
def get_binary_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1]:
                return value
            print("請輸入 0 或 1。")
        except ValueError:
            print("無效輸入。請輸入 0 或 1。")

# 主要模擬函數
def simulate_flip_flop():
    print("歡迎使用正反器模擬器！")
    print("選擇要測試的正反器：")
    print("1. RS 正反器")
    print("2. D 正反器")
    print("3. JK 正反器")
    print("4. T 正反器")
    print("5. 退出")

    choice = input("輸入您的選擇 (1-5): ")

    if choice == "5":
        print("再見！")
        return

    if choice == "1":
        ff = RSFlipFlop()
        print("\nRS 正反器：輸入 S 和 R (0 或 1)。")
        while True:
            S = get_binary_input("輸入 S: ")
            R = get_binary_input("輸入 R: ")
            ff.update(S, R)
            ff.tick()
            print(f"輸出 Q: {ff.get_output()}")
            if input("繼續？(y/n): ").lower() != 'y':
                break

    elif choice == "2":
        ff = DFlipFlop()
        print("\nD 正反器：輸入 D (0 或 1)。")
        while True:
            D = get_binary_input("輸入 D: ")
            ff.update(D)
            ff.tick()
            print(f"輸出 Q: {ff.get_output()}")
            if input("繼續？(y/n): ").lower() != 'y':
                break

    elif choice == "3":
        ff = JKFlipFlop()
        print("\nJK 正反器：輸入 J 和 K (0 或 1)。")
        while True:
            J = get_binary_input("輸入 J: ")
            K = get_binary_input("輸入 K: ")
            ff.update(J, K)
            ff.tick()
            print(f"輸出 Q: {ff.get_output()}")
            if input("繼續？(y/n): ").lower() != 'y':
                break

    elif choice == "4":
        ff = TFlipFlop()
        print("\nT 正反器：輸入 T (0 或 1)。")
        while True:
            T = get_binary_input("輸入 T: ")
            ff.update(T)
            ff.tick()
            print(f"輸出 Q: {ff.get_output()}")
            if input("繼續？(y/n): ").lower() != 'y':
                break

    else:
        print("無效選擇。請重試。")
    
    simulate_flip_flop()  # 重新啟動選單

# 運行模擬器
if __name__ == "__main__":
    simulate_flip_flop()
```

**如何運行代碼：**
1. 將代碼保存到名為 `flip_flop_simulator.py` 的檔案中。
2. 使用 Python 運行（例如 `python flip_flop_simulator.py`）。
3. 按照提示選擇正反器 (1-4) 或退出 (5)。
4. 輸入所選正反器的輸入值（0 或 1）（例如，RS 的 S 和 R，D 的 D 等）。
5. 程式將在每個時鐘 tick 後顯示輸出 Q。
6. 選擇繼續測試同一正反器或退出到選單。

**功能說明：**
- 該程式模擬每種正反器類型（RS、D、JK、T）的行為，如所述。
- 例如，在 RS 正反器中，輸入 S=1, R=0 會將 Q 設置為 1；輸入 S=1, R=1 會警告無效狀態。
- D 正反器在每個 tick 時將 D 輸入複製到 Q。
- JK 正反器根據 J 和 K 處理設置、重置和切換。
- T 正反器在 T=1 時切換 Q。
- 它是互動式的並循環運行，因此您可以持續測試不同的輸入。

如果您想修改代碼、添加功能（如使用 T 正反器的計數器）或有任何問題，請告訴我！