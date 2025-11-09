---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: RHEL 中的 DNF 套件管理
translated: true
type: note
---

### Red Hat Enterprise Linux 中的 DNF 簡介

DNF（Dandified YUM）是 Red Hat Enterprise Linux（RHEL）的主要套件管理工具，從 RHEL 8 開始並持續在 RHEL 9 中使用。它作為舊版 YUM（Yellowdog Updater, Modified）工具的繼任者，提供更佳的效能、更好的依賴關係解析以及對模組化內容的支援。在 RHEL 中，DNF 負責處理透過 RPM（Red Hat Package Manager）儲存庫分發的軟體套件的安裝、更新和移除。它確保能夠存取透過 RHEL 訂閱管理的關鍵內容集，例如 BaseOS（用於核心作業系統功能）和 AppStream（用於使用者空間應用程式、執行環境和工具）。

DNF 的目的是在維護系統穩定性的同時，簡化軟體生命週期管理。它讓管理員和使用者能夠同時處理傳統的 RPM 套件和現代的模組化格式，其中如語言或資料庫等元件可以擁有多個平行版本（稱為「流」），而不會干擾基礎作業系統。

#### 主要功能
- **模組化內容支援**：管理模組（相關 RPM 的群組）、流（版本特定的儲存庫）和設定檔（針對特定使用案例預先配置的套件集，例如網頁伺服器或開發環境）。
- **儲存庫處理**：啟用搜尋、啟用/停用儲存庫，並配置來源如 BaseOS、AppStream 和補充儲存庫。
- **安裝與更新**：在安裝套件、群組或整個模組時自動解析依賴關係；支援檢查更新、升級特定套件或整個系統。
- **移除與還原**：安全地移除軟體，並提供交易歷史記錄以復原變更。
- **自訂與自動化**：可透過 `/etc/dnf/dnf.conf` 配置排除項目、外掛或快取；與如 DNF Automatic 等工具整合以進行排程更新。
- **向後相容性**：在 RHEL 中，`yum` 指令被別名為 `dnf`，以簡化從舊版本的過渡。

若要開始使用，基本指令包括 `dnf install <package>` 用於安裝、`dnf update` 用於升級，以及 `dnf search <term>` 用於尋找軟體。如需更進階的用法，請參閱官方文件。

[Red Hat Enterprise Linux 9：使用 DNF 工具管理軟體](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)