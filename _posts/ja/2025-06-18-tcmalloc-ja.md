---
audio: false
generated: true
lang: ja
layout: post
title: TCMallocエラーの修正
translated: true
type: note
---

エラー「Cannot locate TCMalloc. Do you have tcmalloc or google-perftool installed on your system? (improves CPU memory usage)」は、Googleのgperftoolsに含まれるTCMallocライブラリがLinuxシステムにインストールされていないか、適切に設定されていないことを示しています。TCMallocはメモリアロケータで、Stable Diffusionのようなアプリケーションにおいてパフォーマンスを向上させ、メモリ使用量を削減することができます。この問題を解決する方法は以下の通りです：

### TCMallocエラーを修正する手順

1. **TCMallocとGoogle Perftoolsをインストール**
   使用しているLinuxディストリビューションに応じて、適切なパッケージマネージャを使用して必要なライブラリをインストールします。

   - **Ubuntu/Debianベースのシステムの場合**:
     ```bash
     sudo apt-get update
     sudo apt-get install libgoogle-perftools-dev libtcmalloc-minimal4 -y
     ```
     これにより、完全版の`libgoogle-perftools-dev`（TCMallocを含む）と軽量版の`libtcmalloc-minimal4`の両方がインストールされます。

   - **Fedoraベースのシステムの場合**:
     ```bash
     sudo dnf install gperftools-libs -y
     ```
     これにより、必要なTCMallocライブラリがインストールされます。

   - **CentOS/RHELベースのシステムの場合**:
     ```bash
     sudo yum install gperftools-libs -y
     ```
     デフォルトのリポジトリにパッケージがない場合は、まずEPELリポジトリを有効にする必要があるかもしれません：
     ```bash
     sudo yum install epel-release
     sudo yum install gperftools-libs -y
     ```

2. **インストールの確認**
   インストール後、TCMallocがインストールされているか確認します：
   ```bash
   dpkg -l | grep tcmalloc
   ```
   `libtcmalloc-minimal4`または類似のパッケージが表示されるはずです。別の方法として、ライブラリのパスを確認します：
   ```bash
   dpkg -L libgoogle-perftools-dev | grep libtcmalloc.so
   ```
   これにより、TCMallocライブラリへのパス（例：`/usr/lib/libtcmalloc.so.4`）が表示されます。

3. **LD_PRELOAD環境変数を設定**
   アプリケーションがTCMallocを使用するようにするために、`LD_PRELOAD`環境変数をTCMallocライブラリを指すように設定します。これは一時的または永続的に行うことができます。

   - **一時的（現在のセッションのみ）**:
     `LD_PRELOAD`を設定してアプリケーションを実行します：
     ```bash
     export LD_PRELOAD=/usr/lib/libtcmalloc.so.4
     ./launch.py
     ```
     `/usr/lib/libtcmalloc.so.4`は、手順2で見つかった実際のパスと異なる場合は置き換えてください。

   - **永続的（Stable Diffusionなど）**:
     `webui.sh`のようなスクリプト（Stable Diffusionで一般的）を使用している場合は、スクリプト（例：`webui-user.sh`）を編集して以下を含めます：
     ```bash
     export LD_PRELOAD=libtcmalloc.so.4
     ```
     ファイルを保存し、スクリプトを再実行します：
     ```bash
     ./webui.sh
     ```
     または、シェル設定ファイル（例：`~/.bashrc` または `~/.zshrc`）に追加します：
     ```bash
     echo 'export LD_PRELOAD=/usr/lib/libtcmalloc.so.4' >> ~/.bashrc
     source ~/.bashrc
     ```

4. **アプリケーションを再実行**
   TCMallocをインストールし、`LD_PRELOAD`を設定した後、アプリケーションを再起動します：
   ```bash
   ./launch.py
   ```
   エラーは表示されなくなり、メモリ使用量やパフォーマンスが改善される可能性があります。

5. **トラブルシューティング**
   - **ライブラリのパスが正しくない場合**: `LD_PRELOAD`が失敗した場合（例：「cannot open shared object file」）、正確なライブラリ名とパスを確認します：
     ```bash
     find /usr/lib -name "libtcmalloc*.so*"
     ```
     正しいパス（例：最小版を使用している場合は`libtcmalloc_minimal.so.4`）で`LD_PRELOAD`を更新します。
   - **エラーが解消しない場合**: インストールされたTCMallocのバージョンがシステム（あなたの場合はglibc 2.35、GCC 11.4.0）と互換性があることを確認してください。問題が続く場合は、ソースからインストールしてみてください：
     ```bash
     git clone https://github.com/google/tcmalloc.git
     cd tcmalloc
     bazel build //tcmalloc:hello_main
     bazel run //tcmalloc:hello_main
     ```
     詳細な手順については、TCMalloc Quickstartガイドに従ってください。
   - **メモリの問題**: アロケーションの失敗やクラッシュが発生した場合は、システムに十分なメモリがあること、およびTCMallocが他のアロケータと競合していないことを確認してください。

6. **オプション：TCMallocの使用を確認**
   TCMallocが動作していることを確認するには、簡単なテストプログラムを実行するか、アプリケーションの実行中に`top`や`htop`などのツールでメモリ使用量を確認します。TCMallocは通常、メモリのフラグメンテーションを減らし、若干のパフォーマンス向上をもたらす可能性があります。

### 追加の注意点
- **なぜTCMallocなのか？** TCMallocは高性能なメモリアロケータで、Stable Diffusionのようなスレッド化されたアプリケーションにおいて、CPUメモリ使用量とフラグメンテーションを削減します。必須ではありませんが、パフォーマンスを向上させることができます。
- **互換性**: あなたのシステム（glibc 2.35、Python 3.10.12、GCC 11.4.0）は最新のTCMallocバージョンと互換性があるため、上記の手順は動作するはずです。カスタムビルドのアプリケーションを使用している場合は、TCMallocサポートでコンパイルされていることを確認してください。
- **Stable Diffusionのコンテキスト**: このエラーはAUTOMATIC1111のStable Diffusion WebUIでよく表示されます。特に`libgoogle-perftools-dev`をインストールし、`LD_PRELOAD`を設定する上記の手順は、これを解決することが知られています。

特定のエラーが発生したり、特定のLinuxディストリビューションに関するヘルプが必要な場合は、お知らせください。さらに手順を調整いたします！