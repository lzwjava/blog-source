---
audio: false
generated: true
lang: ja
layout: post
title: Ubuntu Linux ハードウェア情報
translated: true
type: note
---

Ubuntu Linux システムでノートパソコンのハードウェア情報（RAM、CPUなど）を包括的に取得するには、ターミナルコマンドとツールを組み合わせて使用できます。以下に、詳細なシステム情報を取得するためのステップバイステップガイドを示します：

---

### 1. CPU情報の確認
CPU（プロセッサタイプ、速度、コア数など）の詳細を取得するには：
- ターミナルを開きます（Ctrl + Alt + T）。
- 次のコマンドを実行します：
  ```bash
  lscpu
  ```
  - **出力**: CPUアーキテクチャ、コア数、スレッド数、クロック速度、キャッシュサイズなどが表示されます。
- モデル名を含むより詳細なCPU情報については：
  ```bash
  cat /proc/cpuinfo
  ```
  - `model name`、`cpu MHz`、`cpu cores` などのフィールドを確認してください。

---

### 2. RAM（メモリ）情報の確認
総メモリと使用メモリを表示するには：
- 実行：
  ```bash
  free -h
  ```
  - **出力**: 人間が読みやすい形式（例：GBまたはMB）で、総メモリ、使用メモリ、空きメモリが表示されます。
- 詳細なメモリ情報（タイプ、速度、スロットなど）については：
  ```bash
  sudo dmidecode -t memory
  ```
  - **出力**: 物理メモリに関する詳細（サイズ、タイプ（例：DDR4）、速度、スロット使用状況など）を提供します。ルート権限が必要です。

---

### 3. ストレージ（HDD/SSD）情報の確認
ストレージデバイスに関する詳細を取得するには：
- 実行：
  ```bash
  lsblk
  ```
  - **出力**: すべてのブロックデバイス（例：SSD、HDD）とそのサイズ、マウントポイントがリスト表示されます。
- ディスクの詳細情報については：
  ```bash
  sudo fdisk -l
  ```
  - **出力**: ディスクパーティションとサイズが表示されます。ルート権限が必要です。
- ディスクタイプ（例：HDDまたはSSD）とモデルを確認するには：
  ```bash
  sudo hdparm -I /dev/sda
  ```
  - `/dev/sda` をあなたのディスクデバイスに置き換えてください（`lsblk` を使用して確認できます）。

---

### 4. GPU（グラフィックスカード）情報の確認
グラフィックスカードの詳細を見つけるには：
- 実行：
  ```bash
  lspci | grep -i vga
  ```
  または
  ```bash
  lspci | grep -i nvidia
  ```
  - **出力**: グラフィックスカードモデル（例：Intel、NVIDIA、AMD）が表示されます。
- より詳細なGPU情報については：
  ```bash
  glxinfo | grep "OpenGL renderer"
  ```
  - `mesa-utils` パッケージが必要です（インストールされていない場合は `sudo apt install mesa-utils` を実行）。
- NVIDIA GPUの場合は、以下を使用します：
  ```bash
  nvidia-smi
  ```
  - **出力**: GPU使用率、ドライバーバージョン、VRAMが表示されます（NVIDIAドライバーがインストールされている場合）。

---

### 5. システム概要の確認
システムの包括的な概要（CPU、RAM、マザーボードなど）については：
- 実行：
  ```bash
  sudo lshw
  ```
  - **出力**: CPU、RAM、ストレージなど、詳細なハードウェア情報をリスト表示します。簡潔なバージョンには `sudo lshw -short` を使用します。
- 別の方法として、グラフィカルインターフェースのために `hardinfo` をインストールして使用します：
  ```bash
  sudo apt install hardinfo
  hardinfo
  ```
  - **出力**: 詳細なシステム情報（CPU、RAM、ストレージ、センサーなど）を表示するGUIが開きます。

---

### 6. BIOS/UEFIおよびマザーボード情報の確認
BIOS/UEFIおよびマザーボードの詳細を取得するには：
- 実行：
  ```bash
  sudo dmidecode -t bios
  ```
  - **出力**: BIOSバージョン、ベンダー、リリース日が表示されます。
- マザーボードの詳細については：
  ```bash
  sudo dmidecode -t baseboard
  ```
  - **出力**: マザーボードの製造元、モデル、シリアル番号が表示されます。

---

### 7. オペレーティングシステムとカーネルの詳細の確認
Ubuntuのバージョンとカーネルを確認するには：
- 実行：
  ```bash
  lsb_release -a
  ```
  - **出力**: Ubuntuのバージョンとリリース詳細が表示されます。
- カーネル情報については：
  ```bash
  uname -r
  ```
  - **出力**: Linuxカーネルのバージョンが表示されます。

---

### 8. システムリソースのリアルタイム監視
CPU、RAM、プロセス使用率をリアルタイムで監視するには：
- 実行：
  ```bash
  top
  ```
  または
  ```bash
  htop
  ```
  - **注意**: `htop` が存在しない場合はインストールしてください（`sudo apt install htop`）。よりユーザーフレンドリーなインターフェースを提供します。

---

### 9. `inxi` を使用した包括的システムレポート
広範なシステム情報を収集する単一のコマンドについては：
- `inxi` をインストール：
  ```bash
  sudo apt install inxi
  ```
- 実行：
  ```bash
  inxi -Fxz
  ```
  - **出力**: CPU、RAM、GPU、ストレージ、ネットワークなどを含む詳細なレポートを提供します。`-F` フラグは完全なレポートを、`-x` は追加の詳細を、`-z` は機密情報をフィルタリングします。

---

### 出力例（`inxi -Fxz` を使用）
```plaintext
System:    Host: ubuntu-laptop Kernel: 5.15.0-73-generic x86_64 bits: 64 Desktop: GNOME 42.0
           Distro: Ubuntu 22.04.2 LTS (Jammy Jellyfish)
Machine:   Type: Laptop System: Dell product: Inspiron 15 v: N/A serial: <filter>
           Mobo: Dell model: 0XYZ serial: <filter> UEFI: Dell v: 1.2.3 date: 05/10/2023
CPU:       Info: 8-core model: Intel Core i7-12700H bits: 64 type: MT MCP cache: L2: 11.5 MiB
           Speed: 2500 MHz min/max: 400/4700 MHz Core speeds (MHz): 1: 2500 2: 2400 ...
Memory:    RAM: total: 15.5 GiB used: 3.2 GiB (20.6%)
           Array-1: capacity: 32 GiB slots: 2 EC: None
           Device-1: DIMM A size: 8 GiB speed: 3200 MT/s type: DDR4
           Device-2: DIMM B size: 8 GiB speed: 3200 MT/s type: DDR4
Graphics:  Device-1: Intel Alder Lake-P Integrated Graphics driver: i915 v: kernel
           Device-2: NVIDIA GA107M [GeForce RTX 3050 Mobile] driver: nvidia v: 535.54.03
           Display: x11 server: X.Org v: 1.21.1.4 driver: X: loaded: modesetting,nvidia
           OpenGL: renderer: Mesa Intel UHD Graphics (ADL-S GT2) v: 4.6 Mesa 23.0.4
Drives:    Local Storage: total: 512 GiB used: 120 GiB (23.4%)
           ID-1: /dev/nvme0n1 vendor: Samsung model: SSD 970 EVO Plus 500GB size: 512 GiB
...
```

---

### 注意点
- 一部のコマンド（例：`dmidecode`、`fdisk`）はルート権限（`sudo`）を必要とします。
- コマンドがインストールされていない場合（例：`inxi`、`htop`、`mesa-utils`）、`sudo apt install <package-name>` を使用してインストールしてください。
- グラフィカルツールについては、`hardinfo` または `gnome-system-monitor`（Ubuntuにプリインストール）がユーザーフレンドリーなインターフェースを提供できます。
- 特定の詳細（例：バッテリー情報、ネットワークアダプター）が必要な場合は、追加のコマンドを提供できますのでお知らせください。

出力の解釈に助けが必要な場合、または特定のコンポーネントに焦点を当てたい場合は、お知らせください！