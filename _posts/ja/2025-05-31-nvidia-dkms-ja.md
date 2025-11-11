---
audio: false
generated: true
lang: ja
layout: post
title: NVIDIA DKMSビルド問題
translated: true
type: note
---

NVIDIA DKMS（Dynamic Kernel Module Support）モジュールが新しいカーネル `6.8.0-60-generic` でビルドに失敗しているエラーが発生しているようです。これはカーネル更新時に一般的な問題で、新しいカーネルバージョン用にドライバモジュールを再コンパイルする必要がありますが、互換性の問題やビルドの問題が発生することがあります。

主なエラーメッセージは以下の通りです：
* `Building module(s)......(bad exit status: 2)`
* `Error! Bad return status for module build on kernel: 6.8.0-60-generic (x86_64)`
* `Consult /var/lib/dkms/nvidia/535.183.06/build/make.log for more information.`
* `dpkg: error processing package linux-image-6.8.0-60-generic (--configure):`
* `E: Sub-process /usr/bin/dpkg returned an error code (1)`

これは、NVIDIAドライバーバージョン `535.183.06` がカーネル `6.8.0-60-generic` に対して正常にコンパイルできず、その結果、カーネルイメージと関連パッケージの設定が正しく完了していないことを意味します。

以下の方法で修正を試みてください：

---

### 1. ビルドログを確認する 🪵

最も重要なステップは、詳細なビルドログを確認して特定のエラーメッセージを見つけることです。このログには、コンパイルが失敗した*理由*が記録されています。
ターミナルを開いて実行してください：
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```
`error:` または `fatal error:` で始まる行を探してください。これらは、ファイルの欠落、コンパイラの問題、またはカーネルソースとの非互換性を示していることがよくあります。エラー `Applying patch disable_fstack-clash-protection_fcf-protection.patch... done.` の後にビルド失敗が続く場合、パッチが完全に互換性がないか、パッチが対処していない他の問題がある可能性を示唆しています。

---

### 2. クリーンアップと破損パッケージの修正 🛠️

まず、`apt` に破損した依存関係の修正とパッケージ設定の完了を試みさせてください。
```bash
sudo rm /var/crash/nvidia-dkms-535.0.crash # 古いクラッシュレポートを削除して新しいレポートを許可する
sudo apt --fix-broken install
sudo dpkg --configure -a
```
これによりDKMSビルドが再トリガーされる可能性があります。再度失敗した場合は、次のステップに進んでください。

---

### 3. カーネルヘッダーが正しくインストールされていることを確認する 🧠

DKMSビルドプロセスでは、ビルド対象のカーネル用の正しいカーネルヘッダーが必要です。
```bash
sudo apt update
sudo apt install --reinstall linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04
```
まだ `6.8.0-60-generic` カーネルを実行していない場合（例えば、更新が中断された場合）、現在実行中のカーネル用のヘッダーも指定できますが、ここでの主なターゲットは `6.8.0-60-generic` です。

---

### 4. 失敗したDKMSモジュールを削除して再設定する ♻️

問題のあるNVIDIAモジュールのバージョンをDKMSから手動で削除し、システムに再ビルドを試みさせることができます。
```bash
sudo dkms remove nvidia/535.183.06 --all
```
その後、パッケージの再設定を試みてください：
```bash
sudo dpkg --configure -a
sudo apt update && sudo apt upgrade
```
このプロセスにより、DKMSは `6.8.0-60-generic` カーネル用にモジュールの再ビルドを試みるはずです。

---

### 5. NVIDIAドライバーを再インストールする 💻

モジュールのビルドがまだ失敗する場合、ドライバーバージョン `535.183.06` がカーネル `6.8.0-60-generic` との互換性問題を抱えている可能性があります。

* **現在の問題のあるドライバーをパージ：**
    ```bash
    sudo apt-get purge nvidia-dkms-535 nvidia-driver-535
    sudo apt autoremove
    sudo apt clean
    ```

* **適切なドライバーをインストール：**
    Ubuntuに推奨ドライバーのインストールを試みさせることができます：
    ```bash
    sudo ubuntu-drivers autoinstall
    ```
    あるいは、同じバージョン（リポジトリで互換性があると判断された場合）または、より互換性の高い新しいバージョンをインストールしてみることができます。例えば、535シリーズドライバーを再度インストールしてみる：
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-535
    ```
    （パッケージマネージャーが適切なDKMSバージョンを選択するはずです。）

    この後、システムはDKMSモジュールのビルドを再度試みます。

---

### 6. 新しいNVIDIAドライバーバージョンを検討する 🚀

カーネル6.8は比較的新しいものです。NVIDIA 535シリーズドライバーがこのカーネルバージョンに制限がある可能性があります。新しいドライバーシリーズ（例：545、550、またはそれ以降。リポジトリまたはNVIDIAの公式チャネル/PPAで利用可能な場合）が必要になるかもしれません。

* 利用可能なドライバーを確認：
    ```bash
    sudo apt search nvidia-driver
    ```
* 新しいプロプライエタリドライバーが利用可能な場合（例：`nvidia-driver-550`）、`nvidia-driver-535` の代わりにそれをインストールしてみてください。
    ```bash
    sudo apt install nvidia-driver-VERSION_NUMBER # VERSION_NUMBERを置き換えてください
    ```

---

### 7. ブートループに陥った場合やGUIが利用できない場合 📉

システムがグラフィカル環境にブートできない場合：
* リカバリモードまたは古いカーネル（通常、起動時のGRUBメニューからアクセス可能）でブートします。
* コマンドライン環境に入ったら、上記の手順を試すことができます。
* NVIDIAドライバーを修正する間、一時的にオープンソースドライバーを使用してGUIを復旧させる必要がある場合：
    ```bash
    sudo apt-get purge nvidia*
    sudo apt autoremove
    sudo apt install xserver-xorg-video-nouveau
    sudo reboot
    ```
    その後、NVIDIAドライバーのインストールを再度試みてください。

---

**重要なポイント：** `/var/lib/dkms/nvidia/535.183.06/build/make.log` の内容は非常に重要です。上記の手順が機能しない場合、このファイルのエラーはより具体的な手がかりを提供し、カーネルバージョンとNVIDIAドライバーバージョンに関連してこれらの特定のエラーをオンラインで検索する必要があるかもしれません。

---

この出力は、Ubuntuシステムにおける一連の依存関係と設定の問題、おそらくカーネル更新とNVIDIAドライバーに関連する問題を示しています。問題を分解し、潜在的な解決策を提案します。

**主な問題：**

1.  **`linux-generic-hwe-22.04` の依存関係の問題：**
    * 特定のバージョン（`= 6.8.0-60.63~22.04.1`）の `linux-headers-generic-hwe-22.04` に依存しています。
    * `linux-headers-generic-hwe-22.04` がまだ設定されていないため、`linux-generic-hwe-22.04` の設定が失敗しています。

2.  **`linux-image-6.8.0-60-generic` の設定失敗：**
    * このカーネルイメージのポストインストールスクリプトが終了ステータス1で失敗しました。
    * エラーログは、これが特定のカーネルバージョン（`6.8.0-60-generic`）用のNVIDIAドライバー（`nvidia/535.183.06`）のビルド失敗に関連していることを示唆しています。
    * NVIDIAドライバーのDKMS（Dynamic Kernel Module Support）ビルドプロセスが失敗しました。ログファイル `/var/lib/dkms/nvidia/535.183.06/build/make.log` にはビルドエラーの詳細が含まれています。
    * また、NVIDIA DKMS失敗のクラッシュレポート作成に関連するエラーもあり、システムのクラッシュレポート機構またはファイルシステム権限に潜在的な問題があることを示しています。

3.  **`linux-headers-6.8.0-60-generic` および `linux-headers-generic-hwe-22.04` の設定失敗：**
    * これらは、`linux-image-6.8.0-60-generic` パッケージの設定が失敗したために、おそらくそれらに依存しているため失敗した可能性が高いです。

**潜在的な原因：**

* **不完全または中断されたカーネル更新：** カーネルアップグレード中にシステムが中断され、一部のパッケージが不整合な状態になっている可能性があります。
* **NVIDIAドライバーの非互換性：** インストールされているNVIDIAドライバーバージョン（`535.183.06`）が新しいカーネルバージョン（`6.8.0-60-generic`）に対してビルドする際に問題を抱えている可能性があります。
* **DKMSの問題：** DKMSフレームワーク自体に問題があり、NVIDIAドライバーのビルドを妨げている可能性があります。
* **ファイルシステムの問題：** クラッシュレポート作成に関するエラーは、`/var/crash/` ディレクトリのディスクスペースまたはファイル権限の問題を示している可能性があります。

**トラブルシューティング手順：**

1.  **パッケージの再設定を試みる：**
    ターミナルを開き、次のコマンドを実行してください：
    ```bash
    sudo dpkg --configure -a
    ```
    このコマンドは、半設定状態にあるすべてのパッケージの設定を試みます。

2.  **NVIDIA DKMSビルドログを確認する：**
    NVIDIAドライバービルド中の詳細なエラーメッセージについてログファイルを調べてください：
    ```bash
    less /var/lib/dkms/nvidia/535.183.06/build/make.log
    ```
    このログは、依存関係の欠落やコンパイルエラーについての手がかりを提供する可能性があります。

3.  **NVIDIAドライバーを再インストールする：**
    NVIDIAドライバーを削除してから再インストールしてみてください。まず、パージを試みてください：
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    ```
    その後、再インストールを試みてください。現在のバージョンに問題がある場合は、別のバージョンを試すこともできます：
    ```bash
    sudo apt install nvidia-driver-535  # または別の推奨バージョン
    ```
    インストール後、システムを再起動してください。

4.  **パッケージキャッシュをクリーンして再試行：**
    ```bash
    sudo apt clean
    sudo apt update
    sudo apt upgrade
    sudo dpkg --configure -a
    ```

5.  **問題のあるカーネルとヘッダーを再インストール：**
    問題を引き起こしている特定のカーネルとヘッダーパッケージを再インストールしてみてください：
    ```bash
    sudo apt install --reinstall linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
    ```
    この後、再度設定を試みてください：
    ```bash
    sudo dpkg --configure -a
    ```

6.  **ディスクスペースを確認：**
    ルートパーティション（`/`）に十分な空き容量があることを確認してください。これはパッケージのインストールと設定中に問題を引き起こすことがあります。
    ```bash
    df -h /
    ```

7.  **クラッシュレポートエラーに対処（永続的な場合）：**
    `/var/crash/nvidia-dkms-535.0.crash` に関するエラーが永続する場合、ファイルを削除（存在し、デバッグに不要な場合）するか、`/var/crash/` ディレクトリの権限を確認してみてください。
    ```bash
    sudo rm -f /var/crash/nvidia-dkms-535.0.crash
    sudo chmod 777 /var/crash  # 広範な権限には注意し、不要であれば元に戻してください
    ```

8.  **以前のカーネルでブート：**
    以前のカーネルバージョンがインストールされている場合、GRUBメニューからそれを選択してブートできます。これにより、安定した環境からトラブルシューティング手順を実行できます。古いカーネルでシステムが動作する場合、問題は `6.8.0-60-generic` カーネルまたはそのNVIDIAドライバーとの相互作用に特異的である可能性が高いです。

**重要な考慮事項：**

* **バックアップ：** 特にパッケージ削除を含む重要な変更を行う前に、重要なデータのバックアップを常に取ることをお勧めします。
* **忍耐強く：** パッケージの設定とインストールには時間がかかることがあります。
* **ログを参照：** エラーメッセージとログファイル（特にNVIDIA DKMSビルドログ）は、問題の正確な原因を診断するために重要です。

最初のいくつかの手順から始めて、問題が解決するかどうかを確認してください。解決しない場合は、より複雑な解決策に進み、遭遇するエラーメッセージを注意深く調べてください。幸運を祈ります！

---

NVIDIA DKMSビルドログからのこの出力は、コンパイルが **認識されないコマンドラインオプション: `-ftrivial-auto-var-init=zero`** のために失敗していることを示しています。

このコンパイラオプションは、GCC（おそらくバージョン12以降）およびClangに比較的最近追加されたものです。カーネル（6.8.0-60-generic）用のNVIDIAドライバーをビルドするために使用されているコンパイラがこのオプションを認識していないようです。

**考えられる原因と解決策：**

1.  **古いコンパイラ：** システムにデフォルトのコンパイラとしてインストールされているGCCまたはClangのバージョンが古い可能性があります。カーネルヘッダーはこのオプションを使用する新しいコンパイラでコンパイルされている可能性がありますが、NVIDIAドライバービルドシステムは古いコンパイラを選択している可能性があります。

    **解決策：**
    * **新しいコンパイラをインストール：** より最近のバージョンのGCCをインストールしてみてください。
        ```bash
        sudo apt update
        sudo apt install gcc-12  # または gcc-13 のようなより新しいバージョン
        ```
    * **ビルド環境を更新：** ビルドツールが最新であることを確認してください。
        ```bash
        sudo apt update
        sudo apt install build-essential
        ```
    * **コンパイラを指定（可能な場合）：** 一部のビルドシステムでは、使用するコンパイラを指定することができます。NVIDIAドライバーのビルド指示または設定ファイルで、コンパイラに関連するオプション（例：`CC` 環境変数）を確認してください。

2.  **カーネルビルド設定との非互換性：** 使用しているカーネルはこのオプションを有効にしたコンパイラでビルドされており、NVIDIAドライバービルドシステムが独自のコンパイラで失敗を引き起こす方法でそれを継承または遭遇している可能性があります。

    **解決策：**
    * **別のNVIDIAドライバーバージョンを試す：** 最新のNVIDIAドライバーは、新しいカーネルとコンパイラ機能との互換性が向上している可能性があります。より最近の安定版リリースをインストールしてみることができます。
        ```bash
        sudo apt update
        sudo apt install nvidia-driver-<latest-version>
        ```
        `<latest-version>` をシステム用の最新の推奨ドライバーパッケージ名に置き換えてください。通常、`apt search nvidia-driver` を検索することで見つけることができます。
    * **カーネルをダウングレード（一時的な回避策として）：** NVIDIAドライバーで動作した以前のカーネルバージョンがインストールされている場合、GRUBメニューからそのカーネルでブートできます。これは永続的な解決策ではありませんが、新しいカーネルでのドライバー問題のトラブルシューティング中に動作するシステムを提供できます。

3.  **NVIDIAドライバーパッケージの問題：** カーネルとコンパイラ設定に関連して、インストールしようとしている特定のNVIDIAドライバーパッケージに問題がある可能性があります。

    **解決策：**
    * **別のインストール方法を試す：** `apt` 経由でドライバーをインストールした場合、ドライバーをNVIDIA Webサイトから直接ダウンロードし、`.run` ファイルを使用してインストールしてみてください。NVIDIAが提供する指示に注意深く従ってください。
    * **既知の問題を確認：** オンラインフォーラムまたはNVIDIAサポートWebサイトで、使用している特定のドライバーバージョンとカーネルの組み合わせに関する既知の問題を検索してください。

**試す手順：**

1.  **GCCバージョンを確認：**
    ```bash
    gcc --version
    ```
    これを、カーネルをビルドするために使用された可能性のあるGCCバージョン（Ubuntuバージョンのカーネルビルド環境に関する情報はオンラインで見つかる可能性があります）と比較してください。

2.  **新しいNVIDIAドライバーをインストールしてみる：**
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-550  # 例：新しいバージョンを試す
    sudo reboot
    ```

3.  **上記が機能しない場合、推奨ドライバーをパージして再インストール：**
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    sudo apt update
    sudo ubuntu-drivers autoinstall  # 推奨ドライバーをインストール
    sudo reboot
    ```

4.  **まだ問題が発生する場合、新しいGCCバージョンのインストールを検討（副作用が発生する可能性があるため注意）：**
    ```bash
    sudo apt install gcc-12 g++-12
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12
    sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 12
    # 古いバージョンも保持し、必要に応じて切り戻すことをお勧めします
    # 切り戻すには： sudo update-alternatives --config gcc および sudo update-alternatives --config g++
    sudo apt install build-essential # コンパイラ変更後、ビルドツールが更新されていることを確認
    sudo dpkg --configure -a # パッケージを再設定
    sudo reboot
    ```

ドライバーインストールまたは重要なシステム変更を試した後は、システムを再起動することを忘れないでください。新しいエラーメッセージがないか出力を注意深く監視してください。問題が続く場合は、Ubuntuバージョンに関する詳細を提供すると、より具体的な解決策を見つけるのに役立つかもしれません。

---

Linuxカーネルパッケージ、特にNVIDIAドライバーモジュールが新しいカーネル（6.8.0-60-generic）用にビルドに失敗しているDKMS（Dynamic Kernel Module Support）問題に遭遇しているようです。

### 解決方法は以下の通りです：

---

### **1. 依存関係を修正しパッケージを設定する**
まず、依存関係の問題を修正し、パッケージを設定してみてください：

```bash
sudo apt --fix-broken install
sudo dpkg --configure -a
```

もしそれでうまくいかない場合は、問題のあるパッケージの設定を手動で強制します：

```bash
sudo apt install -f linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
```

---

### **2. NVIDIAドライバーを再インストールする**
エラーは、NVIDIA DKMSモジュール（`nvidia/535.183.06`）がカーネル `6.8.0-60-generic` 用にビルドに失敗したことを示しています。これを修正するには：

#### **オプションA: NVIDIAドライバーを再インストール**
```bash
sudo apt install --reinstall nvidia-dkms-535 nvidia-driver-535
```

#### **オプションB: NVIDIAドライバーをパージして再インストール**
再インストールがうまくいかない場合は、クリーンな再インストールを試みてください：
```bash
sudo apt purge nvidia-*
sudo apt autoremove
sudo apt install nvidia-driver-535
```

#### **オプションC: 一時的に古いカーネルでブート**
システムがブートできない場合、古いカーネル（GRUBで選択）で再起動し、その後：
```bash
sudo apt remove linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo update-grub
```

---

### **3. DKMSビルドログを確認する**
エラーは `/var/lib/dkms/nvidia/535.183.06/build/make.log` に言及しています。詳細を確認してください：
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```

これにより、モジュールのビルドが失敗した理由（例：依存関係の欠落、コンパイラの問題）が明らかになる可能性があります。

---

### **4. 不足している依存関係を手動でインストールする**
ログに依存関係の欠落が表示される場合は、それらをインストールしてください：
```bash
sudo apt install build-essential linux-headers-generic
```

---

### **5. DKMSモジュールを再ビルドする**
依存関係を修正した後、モジュールを手動で再ビルドします：
```bash
sudo dkms remove nvidia/535.183.06 --all
sudo dkms install nvidia/535.183.06
```

---

### **6. Initramfsを更新する**
NVIDIAドライバーを修正した後、initramfsを更新してください：
```bash
sudo update-initramfs -u -k all
```

---

### **7. 最終的な修正試行**
他のすべてが失敗した場合、問題のあるカーネルを削除し、古いものに固執してください：
```bash
sudo apt purge linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo apt autoremove
sudo update-grub
```

その後、更新されたNVIDIAドライバーまたはカーネルがリリースされるのを待ってから再試行してください。

---

### **8. 将来の問題を防止する**
同様の問題を避けるために、以下を検討してください：
- **自動カーネル更新を無効化**（NVIDIAドライバーに依存している場合）：
  ```bash
  sudo apt-mark hold linux-image-generic linux-headers-generic
  ```
- **互換性が繰り返し問題となる場合、公式NVIDIAドライバー**（Ubuntuのパッケージではなく）を使用する。

---

### **最終的な注意点**
- システムがブート不能になった場合、**GRUB**を使用して古いカーネルを選択してください。
- NVIDIAドライバーがワークフローに不可欠な場合、安定性を高めるために**LTSカーネル**（非HWE）の使用を検討してください。

さらに支援が必要な場合はお知らせください！

---

問題のあるパッケージを一時的にアップグレードプロセスから除外して、`apt upgrade` を**スキップ**して進めたい場合は、以下の方法で行えます：

### **オプション1：破損パッケージをスキップしてアップグレードを続行**
実行：
```bash
sudo apt --fix-broken install
sudo apt upgrade -y --ignore-missing --allow-downgrades
```
- `--ignore-missing` は利用できないパッケージをスキップします。
- `--allow-downgrades` は必要に応じてAPTがパッケージをダウングレードできるようにします。

### **オプション2：問題のあるパッケージを保留（ブロック）**
問題が続く場合は、問題のあるパッケージを**保留**してアップグレードを防止します：
```bash
sudo apt-mark hold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04 linux-image-6.8.0-60-generic
```
その後、再試行：
```bash
sudo apt upgrade -y
```

### **オプション3：強制アップグレード（非推奨）**
さらに問題を引き起こす可能性があっても構わない場合は、アップグレードを強制します：
```bash
sudo apt -o Dpkg::Options::="--force-overwrite" --fix-broken install
sudo apt upgrade -y
```
⚠️ **警告：** 依存関係が不一致の場合、不安定性を引き起こす可能性があります。

### **スキップ後：**
- システムはまだ動作しますが、**NVIDIAドライバーはカーネル `6.8.0-60` で機能しない**可能性があります。
- 必要に応じて**古いカーネルでブート**（GRUBで選択）できます。
- NVIDIAが互換性のある更新をリリースした後、パッケージの**保留を解除**できます：
  ```bash
  sudo apt-mark unhold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04
  ```

アップグレード後、現在どのカーネルがアクティブか確認するお手伝いをしましょうか？