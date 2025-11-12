---
audio: false
generated: true
lang: hant
layout: post
title: qBittorrent 檔案驗證：SHA-1 雜湊計算
translated: true
type: note
---

當你在 qBittorrent 中移動檔案位置並在重新做種前檢查檔案時，它會確保新位置的檔案與原本使用的檔案完全相同。這種驗證在 BT 下載中至關重要，可防止分享錯誤或損壞的資料。以下是流程說明及使用的演算法：

### qBittorrent 如何驗證檔案
qBittorrent 不會直接信任被移動的檔案是否正確——它會透過與種子檔案中儲存的資訊進行比對來檢查完整性。在 BT 下載中，資料會被分割成稱為 **片段** 的小區塊，每個片段都有唯一的雜湊值。這些雜湊值包含在種子檔案中，作為每個資料片段的指紋。當你將檔案移動到新位置時，qBittorrent 會使用這些片段雜湊值來確認檔案沒有變更。

此流程可分解為以下步驟：

1. **指定新位置**：透過設定新檔案路徑，告知 qBittorrent 檔案現在的位置。
2. **將檔案映射到種子**：qBittorrent 將新位置的檔案與種子中列出的檔案進行匹配，通常使用檔案名稱和大小（因為這些資訊在種子檔案中）。
3. **驗證片段雜湊值**：qBittorrent 逐片讀取新檔案的資料，計算每個片段的雜湊值，並與種子檔案中儲存的對應雜湊值進行比較。
4. **確認完整性**：如果所有計算出的雜湊值都與種子的雜湊值匹配，則確認檔案完全相同，qBittorrent 可以恢復做種。如果有任何片段的雜湊值不匹配，該片段會被標記為不完整或缺失，qBittorrent 可能需要重新下載它。

### 使用何種演算法？
qBittorrent 不使用完整檔案校驗碼（例如整個檔案的 MD5 或 SHA-256），因為對於大型檔案來說，這種方式速度慢且效率低。相反地，它依賴 **片段雜湊值**，這些雜湊值由 BitTorrent 協定定義。用於這些片段雜湊值的演算法是 **SHA-1**，一種廣泛使用的加密雜湊函數。每個資料片段（根據種子不同，可能是幾 KB 到幾 MB）都會透過 SHA-1 進行雜湊計算，而 qBittorrent 檢查的正是這些雜湊值。

使用片段雜湊值而非完整檔案校驗碼有兩大優勢：
- **效率**：檢查較小的片段比對整個檔案進行雜湊計算更快。
- **精確度**：如果出現問題，qBittorrent 可以精確定位需要修復的片段，而不是拒絕整個檔案。

### 為何這很重要
這種基於雜湊的驗證確保你從新位置做種的資料符合其他用戶端的預期，維護了 BT 群組的完整性。如果沒有此檢查，移動檔案可能導致分享損壞或不相符的資料，從而干擾 BT 下載過程。

簡而言之，當你在 qBittorrent 中移動檔案位置時，它會透過計算每個片段的 **SHA-1 雜湊值** 並與種子檔案中的雜湊值進行比較來重新檢查檔案。這就是它在恢復做種前確認一切正確的方式。

---

為了示範 qBittorrent 如何在移動檔案位置時使用片段雜湊值（特別是 SHA-1 雜湊值）來驗證檔案完整性，這裡提供一個簡單的 Python 腳本。qBittorrent 遵循 BitTorrent 協定，將檔案分割成片段，計算每個片段的 SHA-1 雜湊值，並使用這些雜湊值來確保檔案內容無論位於何處都保持不變。此腳本透過建立範例檔案、計算其片段雜湊值、驗證相同副本，然後展示修改如何導致驗證失敗來模擬此過程。

### 說明
- **片段雜湊值**：腳本將檔案分割成固定大小的片段（例如 10 位元組），並計算每個片段的 SHA-1 雜湊值，模擬種子檔案儲存這些雜湊值的方式。
- **驗證**：檢查檔案的計算雜湊值是否與預期雜湊值匹配，確保完整性。
- **模擬**：建立檔案、複製它（模擬移動）、驗證它，然後修改副本並再次驗證以展示如何偵測變更。

以下是帶有清晰註解的腳本：

```python
import hashlib
import shutil
import os

def compute_piece_hashes(file_path, piece_size):
    """計算檔案每個片段的 SHA-1 雜湊值。"""
    hashes = []
    with open(file_path, 'rb') as f:
        while True:
            piece = f.read(piece_size)
            if not piece:
                break
            hash_obj = hashlib.sha1(piece)
            hashes.append(hash_obj.hexdigest())
    return hashes

def verify_file_integrity(file_path, piece_size, expected_hashes):
    """透過比對片段雜湊值來驗證檔案的完整性。"""
    current_hashes = compute_piece_hashes(file_path, piece_size)
    if len(current_hashes) != len(expected_hashes):
        return False
    for current, expected in zip(current_hashes, expected_hashes):
        if current != expected:
            return False
    return True

# 建立包含已知內容的範例檔案
with open('file1.txt', 'w') as f:
    f.write("Hello, this is a test file.")

piece_size = 10  # 位元組，為示範而設小

# 從 file1.txt 計算預期雜湊值（模擬種子雜湊值）
expected_hashes = compute_piece_hashes('file1.txt', piece_size)
print("Expected hashes:", [h[:8] for h in expected_hashes])  # 顯示前 8 個字元以便閱讀

# 將 file1.txt 複製到 file2.txt 以模擬移動檔案
shutil.copyfile('file1.txt', 'file2.txt')

# 根據預期雜湊值驗證 file2.txt（應通過）
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (unchanged):", "Valid" if is_valid else "Invalid")

# 修改 file2.txt 以模擬損壞或變更
with open('file2.txt', 'a') as f:
    f.write(" Modified")

# 再次驗證（因內容變更應失敗）
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (modified):", "Valid" if is_valid else "Invalid")

# 清理建立的檔案
os.remove('file1.txt')
os.remove('file2.txt')
```

### 運作方式
1. **檔案建立**：將 "Hello, this is a test file."（25 位元組）寫入 `file1.txt`。
2. **雜湊計算**：將 `file1.txt` 分割成每個 10 位元組的片段（例如 "Hello, thi", "s is a tes", "t file."），計算 SHA-1 雜湊值，並儲存為 `expected_hashes`。
3. **模擬移動**：將 `file1.txt` 複製到 `file2.txt`，代表檔案被移動到新位置。
4. **初始驗證**：根據 `expected_hashes` 檢查 `file2.txt`。由於內容相同，它會顯示 "Valid"。
5. **修改**：將 " Modified" 附加到 `file2.txt`，改變其內容和大小（現在為 34 位元組，分割成 4 個片段）。
6. **第二次驗證**：檢查修改後的 `file2.txt`。片段數量或其雜湊值不同，因此它會顯示 "Invalid"。
7. **清理**：刪除暫存檔案。

### 輸出範例
```
Expected hashes: ['dffd6021', 'a2b3c4d5', 'e6f789ab']  # 雜湊前綴範例
Verification of file2.txt (unchanged): Valid
Verification of file2.txt (modified): Invalid
```
（實際雜湊值會有所不同，但遵循此模式。）

此腳本說明了 qBittorrent 如何透過比對片段雜湊值來確保檔案完整性，即使在檔案移動後也能偵測任何變更，使其成為此流程簡單而有效的示範。