---
audio: false
generated: true
image: false
lang: hant
layout: post
title: macOS 與 Linux 的網絡服務
translated: true
type: note
---

### macOS 與 Linux 中的網路服務及相關術語

這些術語主要指向網路服務名稱，通常定義於 macOS 和 Linux 系統中的 `/etc/services` 檔案。該檔案將服務名稱映射至標準網路服務的端口號碼和通訊協定。其中有些是官方 IANA 註冊服務，其他則是系統配置中常用的別名或通訊協定名稱。以下根據 macOS（採用類 BSD 基礎）和 Linux 發行版的標準用法，對各項進行解釋。

- **service**：這是 macOS（透過 launchd）和 Linux（透過 systemd 或 init 系統）中系統守護行程或處理序的通用術語。它並非 `/etc/services` 中的特定網路服務，但可能指 Linux 中用於管理傳統 SysV init 腳本的 "service" 指令，或泛指任何背景服務。

- **ircu**：指 IRCU（Internet Relay Chat Undernet）服務，一種 IRC 伺服器軟體的變體。它使用端口 6667/tcp（有時也使用 udp）。在 Linux 中，它可能與 IRC 守護行程相關，例如 ircu 或 undernet-ircu 套件。現代 macOS 或 Linux 系統通常不會預先安裝，但可透過 ports 或套件用於聊天伺服器。

- **complex-link**：可能是 "commplex-link" 的拼寫錯誤或變體，這是一項註冊在端口 5001/tcp 的網路服務。它用於通訊多工連結（例如在某些網路工具或通訊協定中）。在 macOS 中，此端口與 AirPort/Time Capsule 配置或路由器管理工具相關（例如 Netgear 或 Apple 裝置）。在 Linux 中，它可能出現在防火牆規則或 netstat 輸出中，用於類似用途。

- **dhcpc**：DHCP 用戶端服務的別名，使用端口 68/udp（亦稱為 bootpc）。這是 DHCP 的用戶端部分，用於動態獲取 IP 位址。在 Linux 中，由 dhclient 或 dhcpcd 等處理序處理；在 macOS 中，則由 configd 或 bootpd（用戶端模式）處理。

- **zeroconf**：指零配置網路（Zeroconf），一種無需手動配置的自動服務發現通訊協定。在 macOS 中，其實現為 Bonjour（使用端口 5353/udp 的 mDNS）。在 Linux 中，通常為 Avahi（同樣使用端口 5353/udp）。用於發現印表機、共享資源及其他區域網路服務。

- **ntp**：網路時間通訊協定服務，用於透過網路同步系統時鐘。使用端口 123/udp（有時也使用 tcp）。在 Linux 中，由 ntpd 或 chronyd 處理；在 macOS 中，則由 ntpd 或內建時間同步守護行程處理。

- **http**：超文字傳輸通訊協定，網路通訊的基礎。使用端口 80/tcp（有時使用 udp）。在 macOS 和 Linux 中，皆與 Apache（httpd）或 Nginx 等網頁伺服器相關。

- **ssh**：安全殼層通訊協定，用於安全遠端存取和檔案傳輸。使用端口 22/tcp（及 udp/sctp）。在 Linux 和 macOS 中，守護行程為 sshd，可透過系統偏好設定或 sshd_config 啟用。

- **hgvirtgrp**：這似乎是與虛擬化相關的使用者群組參考，可能是 Linux 中 "libvirt group" 的變體或拼寫錯誤（例如 libvirt 或 libvirt-qemu 群組）。在 Linux 中，將使用者加入 libvirt 群組可授予其透過 libvirt 管理虛擬機器的權限（適用於 KVM/QEMU）。在 macOS 中，虛擬化使用 Hypervisor 框架，但並無標準的 "hgvirtgrp" 群組——它可能指用於 hypervisor/虛擬化工具（如 QEMU 或 Virt-Manager）的自訂群組。若為特定群組，請檢查您系統中的 `/etc/group` 檔案。

這些術語常見於 `netstat`、`lsof` 或防火牆配置（例如 macOS 的 pf、Linux 的 iptables/ufw）等工具中。如需確切定義，請參閱您系統的 `/etc/services` 檔案或 IANA 端口註冊表。

**參考資料**  
[服務名稱與傳輸通訊協定端口號碼註冊表](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)  
[什麼是帶有 commplex-link 的開放端口？ - Apple 社群](https://discussions.apple.com/thread/7747034)  
[在 macOS 上執行 virt-manager 和 libvirt](https://www.arthurkoziel.com/running-virt-manager-and-libvirt-on-macos/)