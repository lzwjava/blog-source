---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ソース変更なしでDirBをインストール
translated: true
type: note
---

### DirBのソースコード修正以外の選択肢

ソースコード（例: `variables.h`）の編集が不可能な場合（読み取り専用設定、ポリシー制限、または単なる好みによるもの）でも、DirBをコンパイルせずに実行する簡単な方法があります。これらは事前ビルド済みパッケージや再実装を活用します。Linux（ビルドパスを基に）を優先しますが、OS固有の調整点にも留意してください。

#### 1. **パッケージマネージャー経由でのインストール（Debian/Ubuntu/Kaliで最適）**
   DirBは多くのディストロのリポジトリで事前コンパイル済みパッケージとして利用可能なため、ソース変更やビルドは不要です。
   - **Kali Linuxの場合**（このようなペネトレーションテストツールに推奨）:
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - Kaliリポジトリで公式サポートおよびメンテナンスされています。[Kali Tools Page](https://www.kali.org/tools/dirb/)
   - **Ubuntu/Debianの場合**:
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - 見つからない場合（古いバージョンでは存在しない可能性あり）、universeリポジトリを有効化: `sudo add-apt-repository universe && sudo apt update`
   - **確認**: インストール後 `dirb --help` を実行。ワードリストは `/usr/share/dirb/wordlists/` に配置されます。
   - **理由**: パッケージは（複数定義を含む）全ての修正をアップストリームで処理しています。

   異なるディストリビューションを使用している場合:
   - **Fedora/RHEL**: `sudo dnf install dirb`（EPELリポジトリにある場合。必要に応じてEPELを追加: `sudo dnf install epel-release`）
   - **Arch**: `sudo pacman -S dirb`

#### 2. **Python再実装の使用（クロスプラットフォーム、Cコンパイル不要）**
   オリジナルのDirBはCベースでビルドが困難ですが、機能的に同等（または優れた）モダンなPythonポートがあり、pip経由でインストール可能でソース調整は不要です。
   - **リポジトリ**: [ct-Open-Source/dirb on GitHub](https://github.com/ct-Open-Source/dirb)
   - **インストール**:
     ```
     pip install git+https://github.com/ct-Open-Source/dirb.git
     ```
     - またはクローン: `git clone https://github.com/ct-Open-Source/dirb.git && cd dirb && pip install .`
   - **使用方法**: オリジナルと同じ、例: `dirb https://example.com /usr/share/wordlists/dirb/common.txt`
   - **利点**: 積極的にメンテナンスされ、場合によっては高速、Mac/Windows/Linuxで動作。再帰的スキャンなどの追加機能を含む
   - **欠点**: 「公式」バイナリではないが、出力はほぼ一致

#### 3. **事前ビルド済みバイナリのダウンロード（提供は限定的）**
   - 公式SourceForgeリリースは主にソースターボール（例: dirb222.tar.gz）で、依然ビルドが必要です
   - ユニバーサルバイナリはありませんが、Kali/Parrot OSを使用している場合はパッケージ経由が最適です
   - 代替策: Dockerが利用可能な場合、Kaliイメージをプルして内部でDirBを実行:
     ```
     docker run -it kalilinux/kali-rolling dirb http://example.com
     ```
     - インストール不要。コンテナは事前ビルド済み

#### クイック比較

| 方法                 | OSサポート               | 手間     | 備考 |
|----------------------|--------------------------|----------|------|
| **Apt/DNF/Pacman**  | Linux (Debian/Fedora/Arch) | 低い | 事前コンパイル済み。ワードリスト含む |
| **Pythonポート**    | 全対応 (Python 3+)      | 低い | モダンな代替。pipのみで導入可能 |
| **Docker**          | 全対応 (Docker環境)     | 中程度 | 分離環境。ホストへインストール不要 |

いずれも適合しない場合（例: 制限環境）、Gobuster（`go install github.com/OJ/gobuster/v3@latest`）のような代替ツールを検討してください。Goベースで、問題なく簡単にコンパイルでき、同様のディレクトリ破りを実行します。

どのOSを使用していますか？それによって適切な方法を絞り込めます。問題が発生した場合は、エラー/出力を共有してください。