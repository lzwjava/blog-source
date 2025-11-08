---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: FlashAttention 算法與優勢
translated: true
type: note
---

# FlashAttention 深度解析（Tri Dao 等人，2022）

簡短總結：FlashAttention 透過在晶片內 SRAM（暫存器/共享記憶體）中**分塊計算**注意力，將整個注意力管線融合成單一核心，並使用數值正確的區塊式 softmax 累積，從而無需在 GPU DRAM（HBM）中分配完整的 \\(N\times N\\) 注意力矩陣。這大幅減少了 HBM 流量和記憶體使用，從 \\(O(N^2)\\) 有效降低至 \\(O(N)\\)，並在實際應用中為長序列在 GPU 上帶來顯著的運行時間加速。citeturn0search0turn0search9

---

## 問題所在：為何標準注意力是 IO 瓶頸
Transformer 自注意力（縮放點積）通常透過三個步驟實現：

1. 計算分數 \\(S = Q K^\top\\)（大小 \\(N\times N\\)）；  
2. 計算逐行 softmax \\(P = \mathrm{softmax}(S)\\)；  
3. 計算輸出 \\(O = P V\\)。

傳統做法會將 \\(S\\)（通常還有 \\(P\\)）具體化儲存在 GPU DRAM 中。對於序列長度 \\(N\\)，這會使用 \\(O(N^2)\\) 的記憶體，並導致兩個 IO 問題：
- 巨大的 DRAM 佔用空間（通常是耗盡 GPU 記憶體的首要原因），以及  
- DRAM（HBM）與晶片內 SRAM/暫存器之間的大量讀寫操作 — 而這些 HBM↔SRAM 傳輸正是現代 GPU 的真正瓶頸。

FlashAttention 將注意力重新定義為一個**IO 問題**，而不僅僅是 FLOP 問題，並以減少 HBM 存取為目標。citeturn0search0

---

## 核心概念（高層次）
1. **將矩陣 \\(Q, K, V\\) 分割成區塊**，使其能放入晶片內 SRAM（共享記憶體/暫存器）。  
2. **逐塊處理注意力**：對於給定的 \\(Q\\)-區塊和一組串流處理的 \\(K,V\\)-區塊，計算對輸出的部分貢獻並立即累積 — 從不將完整的 \\(N\times N\\) 分數矩陣具體化儲存在 DRAM 中。  
3. **將所有操作融合成單一核心**：該核心將區塊載入 SRAM，計算該區塊對的 \\(QK^\top\\)，應用 softmax 邏輯並乘以 \\(V\\)-區塊，然後寫入部分輸出 — 所有操作都無需將中間大型矩陣往返於 DRAM。核心融合減少了指令和記憶體開銷。  
4. **區塊式數值穩定 softmax 累積**：由於對整行進行 softmax 需要全域最大值和總和，FlashAttention 使用運行最大值/運行總和（對數求和指數風格）來精確且穩定地合併來自多個 \\(K\\)-區塊的 softmax 貢獻，而無需儲存整行分數。  
5. **透過重計算實現反向傳播**：不儲存大型中間結果供反向傳播使用，而是在反向傳遞期間為每個區塊重計算前向注意力（以額外的 FLOPs 換取更少的 DRAM IO）。節省的 DRAM IO 通常能帶來淨加速，因為 DRAM IO 是主導因素。citeturn0search2turn0search10

這些概念共同實現了記憶體減少和運行時間加速。citeturn0search0

---

## 區塊式演算法 — 逐步解析（前向）
考慮一個序列長度為 \\(N\\)、頭維度為 \\(d\\) 的單一注意力頭。選擇一個區塊大小 \\(B\\)，使得一個 \\(B\times B\\) 的分數區塊以及對應的 \\(Q\\)、\\(K\\)、\\(V\\) 區塊能放入 SRAM。

對於每個查詢區塊 \\(Q_{i}\\)（行 \\(iB:(i+1)B\\)）：

1. 初始化輸出累加器 \\(O_i \leftarrow 0\\)。  
2. 初始化運行歸一化狀態：`row_max`（每查詢行）設為 \\(-\infty\\)，`row_sum` 設為 0。這些狀態用於追蹤跨多個 K-區塊的 softmax 的數值穩定分母。  
3. 對於每個鍵/值區塊 \\(K_{j}, V_{j}\\)（列 \\(jB:(j+1)B\\)）：
   - 將 \\(Q_i\\)、\\(K_j\\)、\\(V_j\\) 載入 SRAM。  
   - 計算原始分數區塊 \\(S_{ij} = Q_i K_j^\top / \sqrt{d}\\)（形狀為 \\(B\times B\\)，以向量化形式）。
   - 對於 \\(S_{ij}\\) 中的每一行，計算本地行最大值 \\(m_{ij}\\) 和指數化值 \\(\exp(S_{ij} - m_{ij})\\)。  
   - 使用對數求和指數技巧將此區塊的指數值合併到運行行歸一化中：
     - 令 \\(M = \max(\text{row\_max}, m_{ij})\\)。
     - 更新 `row_sum` := `row_sum` · exp(row_max − M) + local_sum · exp(m_{ij} − M)。
     - 設定 `row_max` := \\(M\\)。
   - 使用適當縮放的指數值計算該區塊對累加器的貢獻：累積 \\(O_i \mathrel{+}= \text{(tile-softmax)} \times V_j\\)。（所有操作均在 SRAM 內完成。）
4. 在串流處理完所有 K-區塊後，使用 row_sum 和 row_max 最終確定歸一化，以產生正確的 softmax 輸出；將 \\(O_i\\) 寫入 DRAM。

關鍵點：沒有任何 \\(N\times N\\) 矩陣被寫入 DRAM；只有小區塊和最終輸出被寫入。使用運行最大值 + 總和的數值正確累積，使得每個區塊的 softmax 部分能精確組合成與整行完整 softmax 相同的結果。citeturn0search2turn0search10

---

## 為何核心融合和 SRAM 分塊在實踐中勝出
- **更低的 HBM 存取**：標準注意力對 DRAM 進行 \\(O(N^2)\\) 元素的讀寫（分數、softmax）。FlashAttention 對每個 \\(Q,K,V\\) 元素僅讀取常數次，所有臨時的分數/softmax 值僅存在於 SRAM 中。論文中的 IO 分析顯示了更少的 HBM 存取，以及給定 SRAM 大小下 FlashAttention 達到 IO 最優的範圍。citeturn0search0  
- **延遲和頻寬限制比 FLOPs 更重要**：GPU 在 FP 乘加運算上極快；當 DRAM 流量主導運行時間時，減少 DRAM 傳輸比減少 FLOPs 更重要。核心融合消除了中間的 DRAM 流量並減少了核心啟動開銷。citeturn0search0  
- **反向傳遞的權衡**：在反向傳播期間重計算前向區塊增加了 FLOPs，但避免了在 DRAM 中儲存大型中間結果。由於重計算發生在 SRAM 中並限制了 DRAM 流量，在許多情況下這對於運行時間是淨收益。citeturn0search10

論文及後續工作的實證結果顯示了多倍加速（例如，在他們報告的基準測試中，根據模型和序列長度，有 2–7 倍加速）和峰值記憶體的大幅減少。citeturn0search0turn0search10

---

## 重要實作細節與權衡

- **區塊大小選擇**：必須選擇區塊大小 \\(B\\)，使得工作集（Q、K、V 的區塊、分數緩衝區、部分累加器，加上額外的暫存空間）能放入每個執行緒區塊的晶片內 SRAM。最佳 \\(B\\) 取決於頭維度、資料類型（FP16/FP32/FP8）和 GPU 架構（共享記憶體/暫存器的數量）。太小會降低計算效率；太大則無法放入 SRAM。citeturn0search2

- **數值穩定性**：該演算法使用每行運行最大值和總和（對數求和指數合併）來確保最終的 softmax 等於完整矩陣的 softmax。這至關重要：由於這種穩定累積，FlashAttention 是**精確的注意力**（不是近似）。citeturn0search0

- **遮罩與因果性**：因果遮罩（自回歸）是透過在串流處理的區塊中簡單地跳過或將遮罩位置貢獻歸零，並相應地更新運行歸一化來處理的。區塊式邏輯仍然有效，但可能需要仔細的區塊順序安排，以確保遮罩元素不會污染累加器。citeturn0search2

- **反向傳遞與記憶體佈局**：FlashAttention 僅儲存最少的元資料（例如，每個區塊的 row_max/row_sum），並在反向傳播期間重計算前向區塊乘積。實作會仔細重新安排工作以最大化重用並最小化暫存器壓力。citeturn0search10

- **精度與資料類型**：使用 FP16/FP8 會影響區塊緩衝和累積選擇。一些後續工作（FlashAttention-2 / FlashAttention-3）增加了對混合精度和更新 GPU 功能（Hopper、H100）的優化，以進一步提升利用率和 FP 吞吐量。citeturn0search4turn0search11

- **平行度映射**：核心將 warps/CTA 區塊映射到查詢區塊；在一個 CTA 內，warps 協作載入 K/V 區塊並計算區塊矩陣乘法和歸約。高效的 warp 級歸約和融合乘加指令的使用對於達到峰值吞吐量至關重要。citeturn0search2

---

## FlashAttention 與近似長注意力方法之比較
FlashAttention 保持**精確的**注意力語意（與完整注意力的數值結果相同，最多只有浮點捨入誤差），而許多長注意力方法則近似注意力（稀疏性、低秩、FAVOR+ 等），並以品質換取記憶體/時間。FlashAttention 則是在保持精確計算的同時減少記憶體/IO 成本，因此模型品質保持不變，而吞吐量/記憶體得到改善。這就是它廣受歡迎的原因：無需精度權衡，只是一個更好的底層核心。citeturn0search0

---

## 實際可用性與生態系統
- 作者發布了一個實作（CUDA）和一個維護中的儲存庫，包含 FlashAttention 及後來的 FlashAttention-2。許多框架（Hugging Face Transformers、XLA/PyTorch 分支、基於 Triton 的實作）要麼呼叫 flash-attn 運算子，要麼提供類似的融合核心。您可以使用 `flash_attn` 運算子或公開它的函式庫；在 PyTorch 中，近期版本也包含了記憶體高效注意力原語，而第三方 `flash_attn` 套件為許多工作負載提供了即插即用的速度/記憶體改善。請查閱官方儲存庫以獲取安裝程式和 API 範例。citeturn0search9turn0search4

注意：「無需自訂核心」僅部分正確 — FlashAttention *就是*一個自訂的融合核心（儲存庫中的工作），由框架呼叫。現代 PyTorch 版本可能在內部附帶類似的融合核心或委託給供應商函式庫，但核心概念需要一個融合核心實作（無論是用 CUDA、Triton 還是供應商程式碼）。重要的教訓是：您（作為模型使用者）無需自己編寫這些核心 — 使用提供的運算子即可。citeturn0search9turn0search7

---

## 擴展與後續工作
- **FlashAttention-2 (2023)**：改進了平行度、工作分割和多核心擴展，以獲得更好的 GPU 利用率和吞吐量。citeturn0search4  
- **FlashAttention-3 及其他工程工作 (2024+)**：針對新硬體（Hopper/H100）、FP8 和更高的 TFLOP 利用率進行進一步調整。這些工作延續了硬體感知融合注意力核心的趨勢。citeturn0search11

---

## FlashAttention 最適用的情況（經驗法則）
- **長序列**（數千以上）或大批次/頭大小 — 節省最多記憶體並帶來最大加速。  
- **當 DRAM 頻寬是瓶頸時** — 例如，具有大 \\(N\\) 的大型模型，其中傳統注意力會使 DRAM 效能飽和。  
- **使用大上下文進行訓練**，因為對重計算友好的反向傳播降低了峰值記憶體（允許更大的批次/上下文）。citeturn0search0

---

## 快速虛擬碼（概念性）
```
對於每個查詢區塊 Qi：
    row_max = -inf (每行)
    row_sum = 0    (每行)
    out_acc = 0    (B x d_v)
    對於每個鍵/值區塊 Kj, Vj：
        將 Qi, Kj, Vj 載入 SRAM
        S = Qi @ Kj.T / sqrt(d)
        m = max_row(S)
        expS = exp(S - m)      # 本地指數
        local_sum = sum_row(expS)
        # 穩定地合併歸一化器：
        M = max(row_max, m)
        row_sum = row_sum * exp(row_max - M) + local_sum * exp(m - M)
        row_max = M
        # 使用縮放後的 expS 累積部分輸出：
        out_acc += (expS / (合併後的 row_sum)) @ Vj
    將 out_acc 寫入 DRAM
```
（實作會儲存更多元資料並仔細安排精確縮放；以上為概念性說明。）citeturn0search2

---

## 參考文獻 / 延伸閱讀
- 原始 FlashAttention 論文（Tri Dao 等人，2022）— 演算法、IO 分析、基準測試。citeturn0search0turn0search2  
- 官方 GitHub，包含 CUDA 核心和 PyTorch 綁定。citeturn0search9  
- FlashAttention-2 論文（Tri Dao，2023）及後續版本的工程筆記。citeturn0search4turn0search11

---

如果您需要，我可以：
- 展示傳統注意力迴圈與區塊式 FlashAttention 虛擬碼的逐行比較（不使用寬表格），  
- 為具體範例（例如，頭維度 64，區塊大小 128）勾勒 CUDA/Triton 核心組織和暫存器/共享記憶體預算規劃，或  
- 指出確切的 PyTorch API 呼叫以及一個範例程式碼片段，用於將 `torch.nn.functional.scaled_dot_product_attention` 替換為 FlashAttention。接下來哪一項對您最有用？