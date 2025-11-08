---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: NVIDIAドライバーパッケージの競合を修正
translated: true
type: note
---

これはUbuntu（パッケージのバージョンからおそらく22.04）でのNVIDIAドライバー更新時の典型的なパッケージ競合です。`nvidia-kernel-common-535` パッケージが、`nvidia-firmware-535` によって所有されているファームウェアファイル (`gsp_ga10x.bin`) を上書きしようとしているため、dpkgがエラーで停止しています。これはUbuntuリポジトリのNVIDIA 535シリーズドライバーにおける既知の問題です。

慌てないでください—おそらくシステムはまだ起動します（ただし、ドライバーが部分的に破損している場合、グラフィックスはソフトウェアレンダリングモードになる可能性があります）。以下に、安全に解決するためのステップバイステップの修正方法を示します。これらをターミナルで実行してください（GUIが不安定な場合はTTYを使用: Ctrl+Alt+F3 で切り替え）。

### クイックフィックスの試行 (まずは安全な方法から)
1. 壊れたパッケージを自動修復してみてください:
   ```
   sudo apt --fix-broken install
   ```
   これは、手動での介入なしに依存関係や展開の問題を解決することがよくあります。

2. それでも失敗する（または部分的に成功するがエラーが残る）場合、中断されたインストールをクリーンアップします:
   ```
   sudo dpkg --configure -a
   sudo apt update
   sudo apt upgrade
   ```

### まだ解決しない場合: 競合するファイルを強制上書き
エラーは特に `nvidia-kernel-common-535` debファイルで発生しています。dpkgに重複ファイルの上書きを強制します:
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-kernel-common-535_535.274.02-0ubuntu1_amd64.deb
```
- これにより、ファイルの競合を無視してそのパッケージのみをインストールします。
- その後、以下を実行します:
  ```
  sudo apt --fix-broken install
  sudo apt autoremove
  sudo apt upgrade
  ```
- 最後に再起動: `sudo reboot`.

### 最終手段: NVIDIAパッケージの削除と再インストール
上記の方法がうまくいかない場合（例えば、より深いバージョンの不一致）、競合するNVIDIA関連を削除して再インストールします:
1. 問題のあるパッケージを削除します（必要に応じてバージョンを調整—`dpkg -l | grep nvidia` で確認）:
   ```
   sudo dpkg --force-all -P nvidia-firmware-535-535.274.02 nvidia-kernel-common-535
   ```
2. クリーンアップします:
   ```
   sudo apt autoremove --purge
   sudo apt autoclean
   ```
3. ドライバーを再インストールします:
   ```
   sudo apt update
   sudo apt install nvidia-driver-535
   ```
4. 再起動します。

### 予防策/ヒント
- より安定したNVIDIAアップデートのために graphics-drivers PPA を追加: `sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update`.
- ノートパソコンを使用している場合、ドライバーインストール前にBIOSでSecure Bootが無効になっていることを確認してください。
- 再起動後、`nvidia-smi`（GPUが表示されるはず）または `prime-select query`（NVIDIA Optimusの場合）でテストします。
- これでディスプレイが完全に動作しなくなった場合は、リカバリモードで起動し、そこから修正を実行してください。

どれも機能しない場合、または新しいエラーが発生した場合は、完全な出力をここに貼り付けてください。

### 参考資料
- [Unmet dependencies nvidia-dkms-535 - package conflict breaks Ubuntu 22.04 install](https://forums.developer.nvidia.com/t/unmet-dependencies-nvidia-dkms-535-package-conflict-breaks-ubuntu-22-04-install/265788)
- [Ubuntu and NVIDIA-provided packages conflict, breaking installation](https://forums.developer.nvidia.com/t/ubuntu-and-nvidia-provided-packages-conflict-breaking-installation/259150)
- [Problem with nvidia package dependencies](https://askubuntu.com/questions/1491916/problem-with-nvidia-package-dependencies)
- [nvidia-kernel-common-535 conflicts with nvidia-firmware-535](https://superuser.com/questions/1833427/nvidia-kernel-common-535-conflicts-with-nvidia-firmware-535-535-161-07-535-161-0)