---
audio: false
generated: true
lang: hant
layout: post
title: lscpu 指令與 CPU 架構
translated: true
type: note
---

`lscpu` 指令輸出提供了有關系統 CPU 架構與設定的詳細資訊。以下是您輸出中關鍵細節的解析：

- **架構**：`x86_64`  
  您的 CPU 是 64 位元處理器，能夠執行 32 位元與 64 位元應用程式。

- **CPU 運作模式**：`32-bit, 64-bit`  
  CPU 支援 32 位元與 64 位元兩種運作模式。

- **定址空間大小**：`39 bits physical, 48 bits virtual`  
  CPU 可定址最高 2^39 位元組（512 GB）實體記憶體與 2^48 位元組（256 TB）虛擬記憶體。

- **位元組順序**：`Little Endian`  
  資料以最低有效位元組優先儲存，這是 x86 架構的標準格式。

- **CPU 數量**：`32`  
  系統具備 32 個邏輯 CPU（實體核心與執行緒的組合）。

- **線上 CPU 清單**：`0-31`  
  所有 32 個邏輯 CPU 皆處於啟用與可用狀態。

- **供應商 ID**：`GenuineIntel`  
  CPU 由 Intel 製造。

- **型號名稱**：`13th Gen Intel(R) Core(TM) i9-13900KF`  
  您擁有第 13 代 Intel Core i9-13900KF 處理器，這是一款高效能桌面 CPU，未配備整合式 GPU（以 "F" 後綴標示）。

- **CPU 系列**：`6`  
  Intel CPU 系列識別碼（常見於 Intel 處理器）。

- **型號**：`183`  
  此 CPU 的特定型號編號。

- **每核心執行緒數**：`2`  
  每個實體核心支援兩個執行緒（已啟用超執行緒技術）。

- **每插槽核心數**：`24`  
  CPU 每個插槽具備 24 個實體核心。包含 8 個效能核心（P-core）與 16 個效率核心（E-core），這是 i9-13900KF 的典型配置。

- **插槽數**：`1`  
  主機板上有一個實體 CPU 插槽。

- **步進**：`1`  
  表示 CPU 晶片的修訂版本。

- **CPU 最大 MHz**：`5800.0000`  
  最高時脈速度（渦輪加速）為 5.8 GHz。

- **CPU 最小 MHz**：`800.0000`  
  最低時脈速度為 800 MHz（保護模式：intel_pstate=passive）

- **BogoMIPS**：`5990.40`  
  CPU 效能的粗略估算值（現今已不具高度參考性）。

- **功能標誌**：  
  列出 CPU 支援的功能與指令集，例如 `avx`、`avx2`、`fma`、`aes` 與 `hyper-threading`（ht）。這些功能可實現特定優化與安全特性。

- **虛擬化支援**：`VT-x`  
  支援 Intel 的硬體輔助虛擬化技術。

- **快取記憶體**：
  - **L1d**：896 KiB（資料快取，24 個實例，每核心約 36 KiB）
  - **L1i**：1.3 MiB（指令快取，每核心約 56 KiB）
  - **L2**：32 MiB（核心間共享，通常 P-core 每核心 2 MB，E-core 每集群 4 MB）
  - **L3**：36 MiB（所有核心共享的快取）

- **NUMA**：`1 node, 0-31 CPUs`  
  非統一記憶體存取配置；所有 CPU 位於單一 NUMA 節點中，這是單插槽系統的典型配置。

- **安全性漏洞**：  
  列出已知的 CPU 漏洞及其緩解狀態。多數漏洞已透過硬體或軟體修復「不受影響」或已緩解（例如 Spectre、Meltdown）。

### 總結
您擁有一款強大的第 13 代 Intel Core i9-13900KF 處理器，具備 24 核心（8 P-core + 16 E-core）、32 執行緒，最高渦輪速度達 5.8 GHz。其專為高效能任務設計，如遊戲、內容創作與多工處理，且未配備整合式 GPU。系統針對已知 CPU 漏洞具備完善防護，並支援超執行緒與虛擬化等進階功能。

若您對此輸出的任何部分有具體疑問，請隨時告知！

```sh
lzw@lzw-MS-7E01:~/Projects/lzwjava.github.io$ lscpu 
Architecture:             x86_64
  CPU op-mode(s):         32-bit, 64-bit
  Address sizes:          39 bits physical, 48 bits virtual
  Byte Order:             Little Endian
CPU(s):                   32
  On-line CPU(s) list:    0-31
Vendor ID:                GenuineIntel
  Model name:             13th Gen Intel(R) Core(TM) i9-13900KF
    CPU family:           6
    Model:                183
    Thread(s) per core:   2
    Core(s) per socket:   24
    Socket(s):            1
    Stepping:             1
    CPU max MHz:          5800.0000
    CPU min MHz:          800.0000
    BogoMIPS:             5990.40
    Flags:                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon
                           pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm sse4_1 sse4_2 x2apic m
                          ovbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase
                           tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat 
                          pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_
                          l1d arch_capabilities
Virtualization features:  
  Virtualization:         VT-x
Caches (sum of all):      
  L1d:                    896 KiB (24 instances)
  L1i:                    1.3 MiB (24 instances)
  L2:                     32 MiB (12 instances)
  L3:                     36 MiB (1 instance)
NUMA:                     
  NUMA node(s):           1
  NUMA node0 CPU(s):      0-31
Vulnerabilities:          
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Mitigation; Clear Register File
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
  Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
  Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; RSB filling; PBRSB-eIBRS SW sequence; BHI BHI_DIS_S
  Srbds:                  Not affected
  Tsx async abort:        Not affected

```