---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Linux 核心模組化詳解
translated: true
type: note
---

### 理解 Linux 中的模組化設計

Linux 的模組化設計主要體現在 Linux 核心的設計上，其本質是**單體式核心**（所有核心元件在單一記憶體空間中運行以提升效率），但透過**可載入核心模組**實現了模組化。這讓你能在運行時動態新增或移除核心功能——例如裝置驅動程式、檔案系統或網路通訊協定——無需重新啟動或重新編譯整個核心。這是一種混合方法，在效能與靈活性之間取得平衡，使 Linux 能高度適應不同的硬體和使用情境。

可以將其想像成 LEGO 積木：核心是基礎結構，但你可以按需安裝（載入）或移除（卸載）組件，保持系統精簡且可自訂。Linux 中的大多數裝置驅動程式都是以這種方式實現，這也是為什麼 Linux 能夠支援龐大的硬體生態系統，而不會使核心變得臃腫。

#### 模組化的重要性
- **靈活性**：僅載入所需功能（例如，連接網路時才載入 Wi-Fi 驅動程式）。
- **效率**：避免永久包含未使用的程式碼，減少記憶體佔用。
- **可維護性**：更容易更新或除錯個別元件，無需觸及整個系統。
- **穩定性**：單一模組中的故障在一定程度上被隔離，儘管不如微核心（如 MINIX 中的核心）那樣嚴格。

這種設計幫助 Linux 延續數十年，正如我們之前聊天中提到的——它比僵化的單體式核心更容易演進。

#### 核心模組的運作原理
核心模組是使用 C 語言編寫的編譯物件檔案（副檔名為 `.ko`），使用核心標頭檔和 kbuild 系統。它們必須與你的核心版本匹配（使用 `uname -r` 檢查）。

基本模組包含：
- **初始化**：標記為 `module_init()` 的函數，在載入時運行（例如，註冊驅動程式）。
- **清理**：標記為 `module_exit()` 的函數，在卸載時運行（例如，釋放資源）。
- **元資料**：如 `MODULE_LICENSE("GPL")` 等巨集，用於指定授權和作者資訊。

以下是一個簡單的模組範例（`hello.c`），用於輸出訊息：

```c
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/module.h>

MODULE_DESCRIPTION("A simple hello module");
MODULE_AUTHOR("You");
MODULE_LICENSE("GPL");

static int __init hello_init(void) {
    printk(KERN_INFO "Hello, Linux modularity!\n");
    return 0;  // Success
}

static void __exit hello_exit(void) {
    printk(KERN_INFO "Goodbye from the module!\n");
}

module_init(hello_init);
module_exit(hello_exit);
```

編譯方法（需要安裝核心標頭檔，例如在 Debian 系系統上使用 `apt install linux-headers-$(uname -r)`）：
- 建立 `Makefile`：
  ```
  obj-m += hello.o
  KDIR := /lib/modules/$(shell uname -r)/build
  all:
      make -C $(KDIR) M=$(PWD) modules
  clean:
      make -C $(KDIR) M=$(PWD) clean
  ```
- 運行 `make` 生成 `hello.ko`。
- 使用 `sudo insmod hello.ko` 載入（或使用 `sudo modprobe hello` 處理依賴關係）。
- 檢查日誌：`dmesg | tail`（你會看到 "Hello" 訊息）。
- 卸載：`sudo rmmod hello`（在 `dmesg` 中看到 "Goodbye"）。

來自 `printk` 的訊息會輸出到核心環形緩衝區（`dmesg`）或 `/var/log/kern.log`。

#### 實際管理模組
使用以下指令（來自 `kmod` 套件；如需安裝：在 RHEL 上使用 `sudo yum install kmod`，在 Ubuntu 上使用 `sudo apt install kmod`）。

| 操作 | 指令 | 描述/範例 |
|--------|---------|---------------------|
| **列出已載入模組** | `lsmod` | 顯示名稱、大小、使用計數和依賴關係。<br>範例：`lsmod \| grep bluetooth`（過濾藍牙模組）。 |
| **模組資訊** | `modinfo <name>` | 詳細資訊如版本、描述。<br>範例：`modinfo e1000e`（用於 Intel 網路驅動程式）。 |
| **載入模組** | `sudo modprobe <name>` | 載入模組及其依賴項（優先於 `insmod`，後者需要完整路徑）。<br>範例：`sudo modprobe serio_raw`（原始序列輸入）。 |
| **卸載模組** | `sudo modprobe -r <name>` | 卸載模組及其依賴項（如有需要，先卸載依賴項）。<br>範例：`sudo modprobe -r serio_raw`。使用 `lsmod` 檢查使用情況。 |
| **自動生成依賴** | `sudo depmod -a` | 更新 `/lib/modules/$(uname -r)/modules.dep` 供 modprobe 使用。 |

模組位於 `/lib/modules/$(uname -r)/kernel/`。避免卸載使用中的模組（例如活躍的驅動程式），以防系統崩潰。

#### 使模組持久化
變更在重啟後不會永久保留：
- **開機時載入**：新增至 `/etc/modules-load.d/myfile.conf`（每行一個模組）。<br>範例：`echo "hello" \| sudo tee /etc/modules-load.d/hello.conf`。
- **黑名單（防止載入）**：新增至 `/etc/modprobe.d/blacklist.conf`。<br>範例：
  ```
  blacklist bad_module
  install bad_module /bin/false
  ```
  然後重新生成 initramfs：`sudo dracut -f` 並重啟。

#### 常見陷阱與提示
- **版本不匹配**：模組必須與你的核心匹配——更新後需重新編譯。
- **依賴關係**：`modprobe` 會處理；使用 `modinfo --depends <name>` 檢查。
- **除錯**：使用 `pr_debug` 輸出詳細日誌（透過 `echo 8 > /proc/sys/kernel/printk` 啟用）。
- 在虛擬機器中開始實驗，避免系統崩潰。

這種設定是為什麼 Linux 在實踐中感覺「模組化」的原因——它不是完整的微核心，但模組系統模擬了微核心的可擴展性。如需動手實踐，嘗試載入真實的驅動程式，如用於 FAT 檔案系統的 `vfat`。

[KERNEL Modules Lab Documentation](https://linux-kernel-labs.github.io/refs/heads/master/labs/kernel_modules.html)  
[Understanding Kernel Modules on Medium](https://medium.com/@arashjafariwork/understanding-kernel-modules-enhancing-flexibility-in-operating-systems-ed348807ed7b)  
[Red Hat Kernel Administration Guide](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/kernel_administration_guide/chap-documentation-kernel_administration_guide-working_with_kernel_modules)