---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ghosttyのインストールと起動の問題
translated: true
type: note
---

### 問題の診断

共有いただいたログに基づくと、Ghostty 1.1.3 の `.deb` パッケージによるインストールは成功していますが、起動に失敗する主な理由は2つあります：

1.  **CLI 引数のエラー**: コマンド `ghostty .` は、`.` を無効な設定フィールドとして扱っています（おそらくディレクトリとして意図されていますが、Ghostty はその構文をサポートしていません）。これにより、「無効なフィールド」ですぐに終了します。

2.  **OpenGL/GTK 互換性の問題**: 引数なしで `ghostty` を実行すると、初期化はされますが、「OpenGL バージョンが古すぎます。Ghostty には OpenGL 3.3 が必要です」というエラーでクラッシュします（あなたのシステムは Ghostty に 3.2 を報告しています）。これは Ubuntu 22.04、特に X11 上の NVIDIA ドライバーでよく知られている問題です。`glxinfo` がしばしば OpenGL 4.6+ を表示するにもかかわらず、Ghostty の GTK 4.6 ランタイムは NVIDIA GL ではより高いバージョンに適切にアクセスできません。「GDK_DEBUG=vulkan-disable」警告は回避策の試みですが、根本的な問題は解決しません。最終的な Gtk-CRITICAL エラーは、サーフェスの実現に失敗した結果です。

これは、古い GTK バージョン（NVIDIA との完全な互換性に必要な新しい 4.12+ に対して 4.6）が原因で、Ubuntu 22.04（および Pop!\_OS などの派生ディストリビューション）の多くのユーザーに影響を与えています。

### 簡単な確認
-   実際の OpenGL サポートを確認してください（必要に応じて `mesa-utils` をインストール: `sudo apt install mesa-utils`）:
    ```
    glxinfo | grep "OpenGL version"
    ```
    これが 3.3+ を報告する場合、問題は確かに GTK/NVIDIA に特有のものです。
-   セッションタイプを確認してください: `echo $XDG_SESSION_TYPE`。もし `x11` の場合、それが一因となっている可能性が高いです。

### 解決策
以下に、最も簡単なものから順を追った修正方法を示します：

1.  **Wayland に切り替える（ハイブリッドグラフィックス、例: Intel + NVIDIA を使用している場合）**:
    -   ログアウトし、ログイン時に Wayland セッションを選択してください（または、`/etc/gdm3/custom.conf` に `WaylandEnable=true` を追加して GDM を再起動してください）。
    -   統合グラフィックスで Ghostty を実行: `prime-run --gpu intel ghostty`（必要に応じて `nvidia-prime` をインストール）。
    -   これにより、一部のユーザーでは NVIDIA X11 の問題を回避できます。

2.  **Snap 経由でインストール（より簡単な代替パッケージ）**:
    -   使用した非公式の `.deb` はシステムの特性を引き継ぐ可能性があります。依存関係をバンドルしている公式の Snap を試してください：
        ```
        sudo snap install ghostty --classic
        ```
    -   `snap run ghostty` で起動します。もし OpenGL がまだ失敗する場合は、アップグレードに進んでください。

3.  **Ubuntu を 24.04 にアップグレード（長期的な修正として推奨）**:
    -   Ubuntu 24.04 には GTK 4.14+ が含まれており、NVIDIA 互換性が解決されています。
    -   公式のアップグレードガイドに従ってください: `sudo do-release-upgrade`。
    -   アップグレード後、同じ `.deb` または Snap 経由で Ghostty を再インストールしてください。ユーザーからの報告では、アップグレード後は問題なく動作します。

4.  **GLFW バックエンドでソースからビルド（一時的な回避策）**:
    -   これは OpenGL の問題を回避するために非 GTK ランタイムを使用します（注: タブ機能はありません、テスト専用）。
        ```
        sudo apt install git zig libgtk-4-dev libadwaita-1-dev libharfbuzz-dev libpango1.0-dev libcairo2-dev libgdk-pixbuf-2.0-dev libglib2.0-dev libwayland-dev libxkbcommon-dev libinput-dev libudev-dev libseat-dev libpipewire-0.3-dev libsystemd-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrandr-dev libxtst-dev libxdamage-dev libxcomposite-dev libxrender-dev libxcursor-dev libxinerama-dev libxss-dev libxv-dev libxxf86vm-dev libgl1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libdrm-dev libvulkan-dev libclang-dev
        git clone https://github.com/ghostty-org/ghostty.git
        cd ghostty
        zig build -Doptimize=ReleaseFast -Dapp-runtime=glfw
        sudo cp zig-out/bin/ghostty /usr/local/bin/
        ```
    -   `ghostty` を実行します。全機能を使用するには、アップグレード後に GTK に戻してください。

### 追加のヒント
-   NVIDIA ドライバーを更新してください: `sudo ubuntu-drivers autoinstall`（または手動で 550+ シリーズを使用）。
-   AMD/Intel のみを使用している場合は、Mesa が更新されていることを確認してください: `sudo apt update && sudo apt upgrade mesa-vulkan-drivers`。
-   テンプレートファイル（`~/.config/ghostty/config`）の設定警告については、無効な行（例: 孤立した `.`）を削除するように編集してください。

どれも機能しない場合は、`glxinfo` の出力または GPU の詳細（`lspci | grep VGA`）を共有して、より適切なアドバイスを得てください。

[OpenGL が古すぎる議論](https://github.com/ghostty-org/ghostty/discussions/3159)  
[Ghostty Ubuntu ビルド](https://github.com/mkasberg/ghostty-ubuntu)  
[Ghostty Snap](https://snapcraft.io/ghostty)