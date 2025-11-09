---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Verilog 硬件設計與驗證
translated: true
type: note
---

明白了 — 這是一份關於 **Verilog** 的全面介紹，它是兩種最廣泛使用的 HDL（硬體描述語言）之一，特別是在可程式設計邏輯裝置（如 **FPGA** 和 **ASIC**）的背景下。

---

## 1. 什麼是 Verilog？
Verilog 是一種 **硬體描述語言 (HDL)**，創建於 1980 年代（最初由 Gateway Design Automation 開發，後來標準化為 IEEE 1364）。與軟體語言不同，Verilog 描述的是 **硬體的結構和行為**，這意味著您編寫的代碼最終會變成矽晶片上的實際電路（邏輯閘、正反器、連線）。

它主要用於：
- **RTL（暫存器轉換層級）設計** – 在暫存器和組合邏輯層級描述邏輯。
- **模擬** – 在實現之前測試功能。
- **合成** – 將 HDL 轉換為閘級網表，用於 FPGA/ASIC 實現。

---

## 2. Verilog 設計層級
Verilog 支援多種硬體設計抽象層級：

- **行為層級**
  使用 `always` 區塊、`if` 語句、迴圈等描述電路的功能。
  範例：`sum = a + b;`

- **暫存器轉換層級 (RTL)**
  指定資料在暫存器和邏輯之間如何流動。大多數實際設計都在此層級編寫。

- **閘級**
  直接實例化邏輯閘 (`and`, `or`, `not`)。現在很少手動使用。

- **開關級**
  對電晶體（MOSFET 級）進行建模。非常低階，很少使用。

---

## 3. Verilog 關鍵概念

### 模組 (Modules)
Verilog 的基本建構區塊。類似於軟體中的類別或函式。
```verilog
module adder(input [3:0] a, b, output [4:0] sum);
  assign sum = a + b;
endmodule
```

### 資料型別
- `wire` → 代表連接（組合訊號）。
- `reg` → 儲存值（用於程序區塊，如正反器）。
- `integer`, `real` → 用於測試平台，不可合成。

### 程序區塊
- `always @(*)` → 用於組合邏輯。
- `always @(posedge clk)` → 用於順序邏輯（由時鐘觸發）。

### 運算子
- 算術：`+`, `-`, `*`, `/`
- 邏輯：`&&`, `||`, `!`
- 位元：`&`, `|`, `^`, `~`
- 移位：`<<`, `>>`

### 連續賦值
- `assign y = a & b;` → 直接描述組合邏輯。

---

## 4. 模擬 vs. 合成
- **模擬**：使用測試平台運行，以檢查邏輯行為（時序、功能）。
- **合成**：工具（如 Synopsys Design Compiler、Xilinx Vivado、Intel Quartus）將 Verilog RTL 轉換為閘級電路。

某些結構（如 `#delay`、`$display` 或檔案 I/O）**僅用於模擬**，無法合成。

---

## 5. 測試平台
**測試平台** 是用於模擬和驗證設計的 Verilog 代碼。
```verilog
module tb_adder;
  reg [3:0] a, b;
  wire [4:0] sum;

  adder uut (.a(a), .b(b), .sum(sum)); // 待測單元

  initial begin
    a = 4; b = 3; #10;
    a = 8; b = 7; #10;
    $finish;
  end
endmodule
```

---

## 6. Verilog 的優點
- **類 C 語法** → 對於熟悉 C 語言的程式設計師來說更容易上手。
- **業界標準** → 得到 FPGA/ASIC 工具的廣泛支援。
- **高效的 RTL 設計** → 對硬體工程師來說簡潔明瞭。

---

## 7. Verilog 的局限性
- 型別檢查較不嚴格（與 VHDL 相比，VHDL 較冗長但更安全）。
- 難以管理大型複雜設計。
- 模擬和合成之間存在一些模糊之處（SystemVerilog 等新標準解決了這個問題）。

---

## 8. 演進至 SystemVerilog
為了克服 Verilog 的局限性，引入了 **SystemVerilog** (IEEE 1800)。它擴展了 Verilog，增加了：
- 用於測試平台的物件導向程式設計。
- 斷言 (SVA)。
- 更強大的資料型別。
- 用於模組化的介面和套件。

---

## 9. 實際應用
- **FPGA 設計**：實現客製化數位電路（訊號處理、AI 加速器）。
- **ASIC 設計**：用於 CPU、GPU、網路和電信的晶片。
- **驗證**：在花費數百萬資金進行晶片製造之前，用於模擬。

---

✅ 簡而言之：**Verilog 是連接人類硬體設計想法與實際數位電路的語言。**

您是否也希望我建立一個 **並排迷你範例**，比較 **行為層級 vs. RTL vs. 閘級 Verilog** 來實現同一個電路（例如，一個 2 選 1 多工器）？這樣您就可以看到抽象層級的實際運作。