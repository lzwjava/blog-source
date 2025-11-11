---
audio: false
generated: true
lang: hant
layout: post
title: 第五部分：巴士與擴展
translated: true
type: note
---

### 1. 系統匯流排標準

#### 什麼是系統匯流排？

系統匯流排是一條連接 CPU 與記憶體及周邊裝置的通訊路徑。它在這些組件之間促進資料傳輸、位址信號和控制信號，使 CPU 能夠高效地與電腦系統的其他部分互動[^3]。

---

### 2. ISA 匯流排概述

- **ISA（工業標準架構）** 是最早的系統匯流排標準之一，於 1980 年代隨 IBM PC AT 推出。
- 它是一條 16 位元匯流排，運行頻率為 4.77 MHz，資料傳輸速率最高可達約 9 MB/s[^5]。
- ISA 支援多個擴充卡，每個卡都有自己的中斷請求線，使網絡卡、串列埠和顯示卡等裝置得以連接。
- 該匯流排向後兼容舊的 8 位元 PC XT 系統，並使用一個結合了兩個邊緣連接器的 98 針連接器，形成單一插槽。
- ISA 使用非同步信號和匯流排主控，但僅能直接存取前 16 MB 的主記憶體[^5]。
- 由於其年代久遠，ISA 基本上已被淘汰，但作為後續匯流排設計的基礎，在歷史上具有重要地位。

---

### 3. PCI 匯流排概述

- **PCI（周邊元件互連）** 是一種更現代、同步、並行的匯流排標準，旨在克服 ISA 的限制[^1][^3]。
- PCI 匯流排運行頻率為 33 MHz，具有 32 位元多工位址/資料匯流排，提供 44 至 66 MB/s 的基礎頻寬。
- 對於順序記憶體存取，PCI 可以通過在每個時鐘週期傳輸一個 32 位元字組而無需重新發送位址，從而實現高達 132 MB/s 的速率[^1]。
- PCI 使用橋接介面連接到 CPU 匯流排，該介面緩衝資料並優化記憶體存取，允許 CPU 在周邊通訊期間無需等待狀態即可繼續執行[^1]。
- PCI 支援匯流排主控和 DMA（直接記憶體存取），裝置可以接管匯流排以直接傳輸資料。
- 存在 64 位元擴展版本的 PCI 以進一步增加頻寬。
- PCI 裝置透過匯流排編號、裝置編號和功能來識別，配置暫存器指定了供應商、裝置類型、記憶體和 I/O 位址以及中斷[^3]。
- PCI 交易包括位址階段和資料階段，支援各種命令，如記憶體讀寫和 I/O 讀寫[^3]。

---

### 4. 現代介面技術

現代周邊通訊已轉向比並行匯流排更簡單、更靈活的序列介面。

---

#### USB（通用序列匯流排）

- USB 是一種廣泛使用的高速序列介面，專為連接鍵盤、滑鼠、儲存裝置等周邊裝置而設計。
- 它支援隨插即用和熱插拔，允許在不斷電的情況下連接和斷開裝置。
- USB 使用分層星形拓撲，支援從 1.5 Mbps（低速）到 10 Gbps（USB 3.1 及更高版本）的資料速率。
- 它為裝置供電，並支援具有標準化協定的多種裝置類別。
- USB 控制器使用端點和管道來管理資料傳輸，具有不同的傳輸類型，如控制、批量、中斷和同步傳輸。

---

#### SPI（序列周邊介面）

- SPI 是一種同步序列通訊匯流排，常用於與感測器、EEPROM 和顯示器等周邊裝置進行短距離通訊[^4]。
- 它使用四個信號：SCLK（時鐘）、MOSI（主機輸出從機輸入）、MISO（主機輸入從機輸出）和 CS（晶片選擇）。
- SPI 是全雙工的，允許同時進行資料傳輸和接收。
- 它簡單快速，但每個裝置需要一條晶片選擇線，這可能會限制可擴展性。
- SPI 模式設定包括時鐘極性和相位，這些定義了資料取樣和移位的時機[^6]。
- SPI 通常用於嵌入式系統和微控制器應用中。

---

#### I²C（積體電路匯流排）

- I²C 是一種雙線序列匯流排，用於微控制器與感測器和 EEPROM 等周邊裝置之間的通訊[^4]。
- 它使用兩條雙向線路：SDA（資料）和 SCL（時鐘）。
- I²C 支援同一匯流排上的多個主裝置和從裝置，裝置透過唯一的 7 位元或 10 位元位址進行定址。
- 它支援半雙工通訊，並使用帶有上拉電阻的開汲極/開集極輸出。
- I²C 比 SPI 慢，但需要更少的引腳，並支援簡單佈線的多裝置通訊。
- 典型速度為 100 kHz（標準模式）、400 kHz（快速模式）以及更新規格中的更高速度。

---

### 總結表格：ISA vs PCI vs USB vs SPI vs I²C

| 特性 | ISA | PCI | USB | SPI | I²C |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 匯流排類型 | 並行，非同步 | 並行，同步 | 序列，非同步 | 序列，同步 | 序列，同步 |
| 資料寬度 | 8 或 16 位元 | 32 或 64 位元多工 | 序列（1 位元） | 每線 1 位元，全雙工 | 每線 1 位元，半雙工 |
| 時鐘速度 | 4.77 MHz | 33 MHz（基礎 PCI） | 最高 10 Gbps（USB 3.1） | 通常最高數 MHz | 通常最高 400 kHz+ |
| 最大頻寬 | ~9 MB/s | 44-132 MB/s | 依 USB 版本而異 | 取決於時鐘速度 | 低於 SPI |
| 線路數量 | 多條（位址、資料、控制） | 多條（多工線路） | 4 條（電源、接地、D+、D-） | 4 條（SCLK、MOSI、MISO、CS） | 2 條（SDA、SCL） |
| 裝置定址 | 基於插槽 | 匯流排/裝置/功能編號 | 裝置枚舉 | 每個裝置的晶片選擇 | 位址定址裝置 |
| 典型使用案例 | 舊式擴充卡 | 現代擴充卡 | 外部周邊裝置 | 嵌入式周邊裝置 | 嵌入式周邊裝置 |
| 匯流排主控 | 是 | 是 | 由主機控制器管理 | 主/從 | 支援多主控 |

---

### 關於使用 SPI 和 I²C 的實務注意事項

- 在像 Raspberry Pi 這樣的平台上，SPI 和 I²C 介面預設未啟用，需要透過系統設定（例如 `raspi-config`）進行配置[^4]。
- 像 `wiringPi`、`spidev`（用於 SPI）和 `smbus`（用於 I²C）這樣的函式庫，提供了用 C/C++ 和 Python 在這些匯流排上與裝置通訊的程式設計介面。
- SPI 配置涉及設定模式（時鐘極性和相位）、位元順序（MSB 或 LSB 優先）以及選擇正確的晶片選擇引腳[^6]。
- I²C 通訊涉及指定裝置位址和處理資料傳輸的開始/停止條件。

---

本教程概述了系統匯流排和現代周邊介面的基本概念和實務方面，為理解微電腦匯流排架構和擴充技術奠定了堅實的基礎。

<div style="text-align: center">⁂</div>

[^1]: https://people.ece.ubc.ca/~edc/464/lectures/lec17.pdf

[^2]: https://spotpear.com/wiki/USB-TO-UART-I2C-SPI-JTAG-Wiki.html

[^3]: https://home.mit.bme.hu/~rtamas/rendszerarchitekturak/eloadas/08_bus_introduction.pdf

[^4]: https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

[^5]: https://www.techtarget.com/searchwindowsserver/definition/ISA-Industry-Standard-Architecture

[^6]: https://www.ratocsystems.com/english/download/pdffiles/usb61_e_10.pdf

[^7]: https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/files/PCI.pdf

[^8]: https://www.infineon.com/dgdl/Infineon-USB-Serial_VCP_I2CSPI_API_Guide-Software-v01_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f6a8b015fe6\&da=t

[^9]: https://network.nvidia.com/pdf/whitepapers/PCI_3GIO_IB_WP_120.pdf

[^10]: https://people.scs.carleton.ca/~sivarama/org_book/org_book_web/slides/chap_1_versions/ch5_1.pdf

[^11]: https://www.youtube.com/watch?v=BBobCtfOjbM

[^12]: https://www.sciencedirect.com/topics/engineering/peripheral-component-interconnect-bus

[^13]: http://mcatutorials.com/mca-tutorials-bus-standards-and-types.php

[^14]: https://www.youtube.com/watch?v=YRJ9gWaxfJY

[^15]: https://docs.nxp.com/bundle/UM12018/page/topics/connecting_to_a_target_through_a_usb-to-spi_or_usb.html

[^16]: https://www.i2ctools.com/Downloads/USBtoI2Cpro/USB-to-SPI_Software_Users_Manual.pdf

[^17]: https://www.youtube.com/watch?v=WIIR77fCHYc

[^18]: https://ftdichip.com/wp-content/uploads/2021/08/AN_255_USB-to-I2C-Example-using-the-FT232H-and-FT201X-devices.pdf

[^19]: https://www.youtube.com/watch?v=IyGwvGzrqp8