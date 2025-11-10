---
audio: false
generated: true
lang: ja
layout: post
title: macOSでGoコマンドが見つからない問題の解決
translated: true
type: note
---

エラーメッセージ `/bin/sh: go: command not found` は、Goプログラミング言語がmacOSシステムにインストールされていないか、PATHに正しく設定されていないことを示しています。`make` コマンドはGoのビルドプロセスを実行しようとしていますが、これにはGoコンパイラ（`go`）が必要です。以下に、macOSにGoをインストールしてこの問題を解決する手順を示します。

### macOSにGoをインストールする手順

macOSにGoをインストールする主な方法は2つあります：公式Goインストーラを使用する方法と、Homebrewを使用する方法です。両方の方法を説明しますが、HomebrewはmacOSユーザーにとってより簡単な場合が多いです。好みに応じて1つの方法を選択してください。

#### 前提条件
- 最近のGoバージョンとの互換性のために、macOSのバージョンが10.10以降であることを確認してください。[](https://tecadmin.net/install-go-on-macos/)
- Goをインストールし、システムファイルを変更するには管理者アクセス権が必要です。
- ターミナルアプリケーション（アプリケーション > ユーティリティ > ターミナル）が必要です。

#### 方法 1: Homebrewを使用してGoをインストール（推奨）
HomebrewはmacOS用の一般的なパッケージマネージャで、ソフトウェアのインストールを簡素化します。

1. **Homebrewをインストール（まだインストールされていない場合）**:
   - ターミナルを開き、以下を実行:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - 画面の指示に従ってインストールを完了させてください。[](https://www.digitalocean.com/community/tutorials/how-to-install-go-and-set-up-a-local-programming-environment-on-macos)

2. **Goをインストール**:
   - 以下のコマンドを実行して最新バージョンのGoをインストール:
     ```bash
     brew install go
     ```
   - これにより、Goが `/usr/local/Cellar/go`（または類似のパス）にインストールされ、Goバイナリが `/usr/local/bin` に追加されます。[](https://www.feliciano.tech/blog/how-to-install-go-on-linux-macos/)[](https://formulae.brew.sh/formula/go)

3. **インストールの確認**:
   - インストールされたGoのバージョンを確認するために実行:
     ```bash
     go version
     ```
   - `go version go1.23.x darwin/amd64` のような出力が表示され、Goがインストールされたことが確認されます。[](https://tecadmin.net/install-go-on-macos/)

4. **環境変数の設定（必要な場合）**:
   - Homebrewは通常、GoをPATHに自動的に追加しますが、`go` コマンドが動作しない場合は、Goバイナリのパスをシェルプロファイルに追加してください:
     - 適切なシェル設定ファイル（例: Zshの場合は `~/.zshrc`（Catalina以降のmacOSのデフォルト）、Bashの場合は `~/.bash_profile`）を開くか作成:
       ```bash
       nano ~/.zshrc
       ```
     - 以下の行を追加:
       ```bash
       export PATH=$PATH:/usr/local/go/bin
       ```
     - ファイルを保存（nanoではCtrl+X、次にY、次にEnter）し、変更を適用:
       ```bash
       source ~/.zshrc
       ```
     - カスタムワークスペースを使用したい場合は、`GOPATH` を設定（オプション、Goモジュールではこれが必要ないことが多い）:
       ```bash
       export GOPATH=$HOME/go
       export PATH=$PATH:$GOPATH/bin
       ```
     - 再度ファイルを適用:
       ```bash
       source ~/.zshrc
       ```

5. **Goインストールのテスト**:
   - 再度 `go version` を実行してコマンドが認識されることを確認してください。
   - オプションで、簡単なGoプログラムを作成してすべてが機能することを確認:
     ```bash
     mkdir -p ~/go/src/hello
     nano ~/go/src/hello/main.go
     ```
     - 以下のコードを追加:
       ```go
       package main
       import "fmt"
       func main() {
           fmt.Println("Hello, World!")
       }
       ```
     - 保存して終了（Ctrl+X、Y、Enter）、その後コンパイルして実行:
       ```bash
       cd ~/go/src/hello
       go run main.go
       ```
     - `Hello, World!` が出力として表示されるはずです。[](https://www.digitalocean.com/community/tutorials/how-to-install-go-and-set-up-a-local-programming-environment-on-macos)

#### 方法 2: 公式インストーラを使用してGoをインストール
Homebrewを使用したくない場合は、公式macOSパッケージを使用してGoをインストールできます。

1. **Goインストーラをダウンロード**:
   - 公式Goダウンロードページにアクセス: https://go.dev/dl/
   - システムアーキテクチャ用のmacOSパッケージ（`.pkg`）をダウンロード（例: Intel Mac用 `go1.23.x.darwin-amd64.pkg`、Apple Silicon用 `go1.23.x.darwin-arm64.pkg`）。[](https://medium.com/%40priyamjpatel/installing-go-on-a-mac-machine-bca6746fff0b)[](https://golangdocs.com/install-go-mac-os)

2. **インストーラを実行**:
   - Finderでダウンロードした `.pkg` ファイルをダブルクリック。
   - 画面の指示に従ってGoをインストール。デフォルトでは `/usr/local/go` にインストールされます。
   - 管理者パスワードの入力が必要な場合があります。[](https://www.scaler.com/topics/golang/install-golang/)[](https://golangdocs.com/install-go-mac-os)

3. **環境変数の設定**:
   - ターミナルを開き、シェル設定ファイル（例: `~/.zshrc` または `~/.bash_profile`）を編集:
     ```bash
     nano ~/.zshrc
     ```
   - 以下の行を追加:
     ```bash
     export GOROOT=/usr/local/go
     export GOPATH=$HOME/go
     export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
     ```
   - 保存して変更を適用:
     ```bash
     source ~/.zshrc
     ```
   - 注意: `GOROOT` は、Go自体を開発している場合や非標準のインストールパスが必要な場合を除き、オプションです。最近のGoバージョンでは `GOROOT` を設定する必要がないことが多いです。[](https://stackoverflow.com/questions/12843063/install-go-with-brew-and-running-the-gotour)[](https://tecadmin.net/install-go-on-macos/)

4. **インストールの確認**:
   - 実行:
     ```bash
     go version
     ```
   - インストールされたGoバージョン（例: `go version go1.23.x darwin/amd64`）が表示されるはずです。[](https://golangdocs.com/install-go-mac-os)

5. **Goインストールのテスト**:
   - 方法1のステップ5と同じ手順に従って「Hello, World!」プログラムを作成して実行してください。

#### 元の問題のトラブルシューティング
Goをインストールした後、`clash-core` ディレクトリに戻り、`make` コマンドを再試行してください:
```bash
cd /path/to/clash-core
make
```

問題が発生した場合:
- **プロキシ設定**: ターミナルの出力に `HTTP_PROXY` と `HTTPS_PROXY` が `http://127.0.0.1:7890` に設定されていることが示されています。プロキシがアクティブであり、Goのネットワークアクセス（例: 依存関係のダウンロード）を妨害していないことを確認してください。テストのために一時的にプロキシを無効にできます:
  ```bash
  unset HTTP_PROXY HTTPS_PROXY
  make
  ```
- **権限**: 権限エラーが発生した場合は、プロジェクトディレクトリとGoワークスペース（`$GOPATH` または `$HOME/go`）への書き込み権限があることを確認してください。
- **Go Modules**: `clash-core` プロジェクトはおそらくGoモジュールを使用しています。`go.mod` を含む正しいディレクトリにいることを確認し、`make` の前に `go mod tidy` を実行して依存関係を取得してください:
  ```bash
  go mod tidy
  make
  ```
- **アーキテクチャの不一致**: `make` コマンドは `linux-amd64`（`GOOS=linux GOARCH=amd64`）向けにビルドしています。バイナリをmacOSで実行する場合は、Makefileまたはビルドコマンドを変更して `darwin-amd64`（Intel Mac用）または `darwin-arm64`（Apple Silicon用）をターゲットにする必要があるかもしれません。Makefileの `linux-amd64` ターゲットを確認して調整するか、以下を実行:
  ```bash
  GOARCH=amd64 GOOS=darwin CGO_ENABLED=0 go build -trimpath -ldflags '-X "github.com/Dreamacro/clash/constant.Version=1.18" -X "github.com/Dreamacro/clash/constant.BuildTime=Sat Jun 28 12:24:27 UTC 2025" -w -s -buildid=' -o bin/clash-darwin-amd64
  ```
  Apple Siliconの場合は `amd64` を `arm64` に置き換えてください。

#### 追加の注意点
- **以前のGoバージョンのアンインストール**: 以前にGoがインストールされていた場合は、競合を避けるために削除してください:
  ```bash
  sudo rm -rf /usr/local/go
  sudo rm -f /etc/paths.d/go
  ```
  その後、上記のいずれかの方法を使用して再インストールしてください。[](https://hostman.com/tutorials/how-to-install-go-on-macos/)[](https://go.dev/doc/install)
- **Goワークスペース**: `GOPATH` を設定した場合は、ディレクトリを作成してください:
  ```bash
  mkdir -p $HOME/go/{bin,src,pkg}
  ```
  ただし、Goモジュール（`clash-core` のようなほとんどの最近のプロジェクトで使用）では、`GOPATH` はそれほど重要ではありません。[](https://www.geeksforgeeks.org/how-to-install-golang-on-macos/)
- **Xcode Command Line Tools**: 一部のGoプロジェクトはCの依存関係（例: `CGO_ENABLED=1`）を必要とします。必要な場合はXcode Command Line Toolsをインストールしてください:
  ```bash
  xcode-select --install
  ```
  [](https://www.digitalocean.com/community/tutorials/how-to-install-go-and-set-up-a-local-programming-environment-on-macos)
- **複数のGoバージョン**: 複数のGoバージョンが必要な場合は、バージョンマネージャ（例: `gvm`）の使用を検討してください（Homebrewまたはスクリプト経由でインストール）。[](https://jimkang.medium.com/install-go-on-mac-with-homebrew-5fa421fc55f5)

#### 検証
Goがインストールされ、`make` コマンドが成功すると、`clash-core` バイナリが `bin/` ディレクトリ（例: `bin/clash-linux-amd64` または `bin/clash-darwin-amd64`）に表示されるはずです。以下を実行して動作を確認してください:
```bash
./bin/clash-darwin-amd64 --version
```

さらに支援が必要な場合や特定のエラーに遭遇した場合は、正確なエラーメッセージやコンテキストをお知らせいただければ、より具体的なヘルプを提供できます！