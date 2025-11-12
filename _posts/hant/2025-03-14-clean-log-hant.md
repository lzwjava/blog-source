---
audio: false
generated: true
lang: hant
layout: post
title: 清理日誌訊息
translated: true
type: note
---

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    讀取日誌檔案，根據相似度移除重複的連續標準日誌行，
    並將清理後的日誌寫入指定檔案，預設為覆蓋輸入檔案。

    Args:
        input_path (str, optional): 輸入日誌檔案路徑。如為 None，則從 stdin 讀取。
        output_path (str, optional): 輸出日誌檔案路徑。如為 None，則覆蓋輸入檔案。
        similarity_threshold (float, optional): 將行視為重複的相似度比率（0.0 到 1.0）。預設為 1.0（完全匹配）。
        lines_to_compare (int, optional): 要比較的連續行數。預設為 1。
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("lines_to_compare 必須為大於或等於 1 的整數。")

    # 確定輸入來源
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"錯誤：找不到路徑的檔案：{input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # 從 stdin 讀取所有行

    # 確定輸出目的地
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"錯誤：無法開啟檔案進行寫入：{output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # 覆蓋輸入檔案
        except IOError:
            print(f"錯誤：無法開啟檔案進行寫入：{input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # 如果沒有 input_path，預設為 stdout

    num_lines = len(lines)
    i = 0
    removed_lines = 0
    while i < num_lines:
        # 收集 'lines_to_compare' 行，如果少於 'lines_to_compare' 則收集剩餘行
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # 只有在有足夠行數進行比較時才處理
        if len(current_lines) == lines_to_compare:
            # 從第一組行中提取標準資訊
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"非標準行：{line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # 如果找到非標準行，停止處理此群組

            if all_standard:
                # 從第二組行中提取標準資訊（如果可用）
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # 如果任何下一行是非標準的，則將下一組行視為非標準
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"相似度：{similarity:.4f}，閾值：{similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"跳過重複行：{ ''.join([line.strip() for line in current_lines])}")
                            removed_lines += len(current_lines)
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # 移動到下一組行
        else:
            # 處理剩餘行（少於 'lines_to_compare'）
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"非標準行：{line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

    if output_path or input_path:
        outfile.close()

    print(f"已移除 {removed_lines} 個重複行。")


def is_valid_similarity_threshold(value):
    """
    檢查給定值是否為有效的相似度閾值。
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("相似度閾值必須為浮點數。")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("相似度閾值必須在 0.0 和 1.0 之間。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="從檔案或 stdin 清理重複日誌行並寫入檔案，預設為覆蓋輸入檔案。")
    parser.add_argument("input_path", nargs="?", type=str, help="輸入日誌檔案路徑（可選，預設為 stdin）")
    parser.add_argument("-o", "--output_path", type=str, help="輸出日誌檔案路徑（可選，預設為覆蓋輸入檔案）")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="將行視為重複的相似度閾值（0.0-1.0）（預設：1.0）")
    parser.add_argument("-l", "--lines", type=int, default=1, help="要比較的連續行數（預設：1）")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

這個 Python 腳本 `clean_log.py` 旨在從檔案或標準輸入中移除重複的日誌行。它使用相似度閾值來確定連續的日誌行是否足夠相似以被視為重複。

以下是程式碼的詳細說明：

**1. 導入：**

- `sys`：用於與 Python 解釋器互動，例如從 stdin 讀取和寫入 stderr。
- `argparse`：用於建立命令列介面。
- `difflib.SequenceMatcher`：用於比較字串序列之間的相似度。

**2. `clean_log` 函數：**

- 接受 `input_path`、`output_path`、`similarity_threshold` 和 `lines_to_compare` 作為參數。
- `input_path`：指定輸入日誌檔案。如果為 `None`，則從 stdin 讀取。
- `output_path`：指定輸出檔案。如果為 `None` 且給定了 `input_path`，則覆蓋輸入檔案。如果兩者均為 `None`，則寫入 stdout。
- `similarity_threshold`：介於 0.0 和 1.0 之間的浮點數，決定將行視為重複的最小相似度比率。值為 1.0 表示僅移除完全相同的行。
- `lines_to_compare`：指定要比較相似度的連續行數的整數。

- **輸入處理：**
    - 從輸入檔案或 stdin 讀取行。
    - 如果輸入檔案不存在，則處理 `FileNotFoundError`。

- **輸出處理：**
    - 開啟輸出檔案進行寫入或使用 stdout。
    - 如果無法開啟輸出檔案，則處理 `IOError`。

- **重複移除邏輯：**
    - 以 `lines_to_compare` 為塊大小迭代日誌檔案的行。
    - 對於每個塊：
        - 根據 " | " 分隔符將每行拆分為部分，預期為四個部分：level、timestamp、thread 和 message。
        - 如果一行沒有四個部分，則被視為「非標準」行，並在未比較的情況下輸出。
        - 如果當前塊中的所有行都是標準的，則將其與下一個 `lines_to_compare` 行進行比較。
        - 使用 `SequenceMatcher` 計算當前塊和下一個塊的 thread 和 message 部分連接字串之間的相似度比率。
        - 如果相似度比率小於 `similarity_threshold`，則將當前塊的行輸出。
        - 如果相似度比率大於或等於 `similarity_threshold`，則將當前塊的行視為重複並跳過。
    - 處理檔案末尾的剩餘行（少於 `lines_to_compare` 行）。

- **統計：**
    - 追蹤已移除的行數。
    - 將已移除的行數列印到控制台。

- **檔案關閉：**
    - 如果已開啟輸出檔案，則將其關閉。

**3. `is_valid_similarity_threshold` 函數：**

- 由 `argparse` 使用的輔助函數，用於驗證相似度閾值參數。
- 檢查輸入值是否為介於 0.0 和 1.0 之間的浮點數。

**4. `if __name__ == "__main__":` 區塊：**

- 當從命令列執行腳本時，執行此區塊。
- 使用 `argparse` 建立命令列參數解析器。
- 定義以下參數：
    - `input_path`：輸入日誌檔案的路徑（可選）。
    - `-o` 或 `--output_path`：輸出日誌檔案的路徑（可選）。
    - `-s` 或 `--similarity`：相似度閾值（預設：1.0）。
    - `-l` 或 `--lines`：要比較的行數（預設：1）。
- 使用 `parser.parse_args()` 解析命令列參數。
- 使用解析後的參數呼叫 `clean_log` 函數。

**總之，該腳本提供了一種靈活的方式來清理日誌檔案，根據可配置的相似度閾值和要比較的行數來移除重複行。它支援從 stdin 讀取、寫入 stdout 和覆蓋輸入檔案。**