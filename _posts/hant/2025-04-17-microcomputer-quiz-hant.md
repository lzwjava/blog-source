---
audio: false
generated: true
lang: hant
layout: post
title: 微電腦與介面技術 - 測驗
translated: true
type: note
---

以下是一份根據你提供的「微電腦與介面技術」課程大綱設計的測驗：

---

**1. 大多數微電腦系統使用的主要架構模型是什麼？**
* 哈佛架構
* 馮·諾依曼架構
* RISC 架構
* CISC 架構

**2. 哪些內部暫存器屬於 8086 微處理器？**
* 累加器、基底、計數、資料暫存器
* AX、BX、CX、DX 暫存器
* PC、SP、LR、FP 暫存器
* MAR、MDR、IR、PC 暫存器

**3. 記憶體映射 I/O 與獨立 I/O 有何區別？**
* 記憶體映射 I/O 使用與記憶體相同的位址空間，獨立 I/O 使用獨立的位址空間
* 記憶體映射 I/O 比獨立 I/O 慢
* 獨立 I/O 只能與 DMA 一起使用
* 記憶體映射 I/O 需要中斷，獨立 I/O 則不需要

**4. 以下哪項不是資料傳輸模式？**
* 程式控制傳輸
* 中斷驅動傳輸
* 直接記憶體存取
* 多執行緒

**5. 8259A 晶片的主要功能是什麼？**
* 計時器/計數器
* 並列介面
* 中斷控制器
* 序列通訊

**6. 8255A 並列介面晶片支援多少種操作模式？**
* 1
* 2
* 3
* 4

**7. 在 8086 組合語言中，哪種指令類型用於迴圈和條件跳轉？**
* 資料傳輸指令
* 算術指令
* 控制流程指令
* 邏輯指令

**8. 記憶體系統中的位址解碼目的是什麼？**
* 提高記憶體速度
* 根據位址線選擇特定的記憶體位置或裝置
* 加密記憶體中的資料
* 轉換資料格式

**9. 哪種匯流排標準較舊且常用於早期 PC 架構？**
* PCI
* USB
* ISA
* SPI

**10. 以下哪種協定用於微電腦介面中的序列通訊？**
* SPI
* I²C
* SPI 和 I²C 兩者皆是
* 以上皆非

---

如果你需要，我也可以提供答案和解釋！

以下是額外的測驗題目，涵蓋更進階和實務的微電腦與介面技術內容，取材自更廣泛的課程目標和主題，例如 ARM 微控制器、即時程式設計、資料擷取和介面技術[^1][^2][^5]：

---

### 進階微電腦與介面技術測驗

**11. 以下哪項最準確描述了直接記憶體存取？**
* CPU 無需周邊裝置直接讀寫記憶體
* 周邊裝置無需 CPU 介入即可與記憶體傳輸資料
* 在 DMA 期間只有 CPU 可以存取記憶體
* DMA 僅用於序列通訊

**12. 在 ARM Cortex-M 微控制器中，NVIC 的主要功能是什麼？**
* 管理匯流排仲裁
* 控制 GPIO 腳位方向
* 處理和優先排序中斷
* 執行類比數位轉換

**13. 哪種訊號通常用於同步微控制器與外部裝置之間的資料傳輸？**
* RESET
* CLOCK
* VCC
* GND

**14. 在微控制器介面中，使用運算放大器的主要目的是什麼？**
* 記憶體擴充
* 訊號調理
* 匯流排仲裁
* 中斷處理

**15. 同步與非同步序列通訊的主要區別是什麼？**
* 同步使用共享時鐘；非同步則不使用
* 非同步總是更快
* 同步需要更少的線路
* 非同步不能使用 UART

**16. 哪種介面最適合連接微控制器與需要即時資料擷取的高速外部感測器？**
* UART
* SPI
* I²C
* GPIO

**17. 在組合語言程式設計中，堆疊的功能是什麼？**
* 儲存程式碼
* 暫存資料和儲存副程式的返回位址
* 控制時鐘速度
* 解碼記憶體位址

**18. 以下哪項是人機介面裝置的例子？**
* 8255A
* LCD 觸控螢幕
* 8253 計時器
* SPI 匯流排

**19. 設計用於鍵盤的微控制器介面時，通常使用哪種類型的 I/O？**
* 序列 I/O
* 並列 I/O
* 類比 I/O
* PWM 輸出

**20. 在簡單的微控制器應用中，使用輪詢而非中斷的主要優勢是什麼？**
* 更低的 CPU 負擔
* 實現更簡單
* 更快的響應時間
* 降低功耗

---

如果你需要這些題目的解釋或答案，請告訴我！

<div>⁂</div>

[^1]: https://www.uoguelph.ca/engineering/sites/uoguelph.ca.engineering/files/public/outlines/3640_0.pdf

[^2]: https://www.uoguelph.ca/engineering/system/files/3640_1.pdf

[^3]: https://drive.uqu.edu.sa/_/cis_ce/files/courses/Microcomputers System Design.pdf

[^4]: https://www.uoguelph.ca/engineering/sites/uoguelph.ca.engineering/files/public/outlines/eng3640.pdf

[^5]: https://www.uoguelph.ca/engineering/sites/uoguelph.ca.engineering/files/public/outlines/ENGG3640_1.pdf

[^6]: https://slideplayer.com/slide/13585404/

[^7]: https://www.cs.vassar.edu/courses/cs325/top

[^8]: https://books.google.com/books/about/Microcomputer_Interfacing.html?id=SsAjAAAAMAAJ