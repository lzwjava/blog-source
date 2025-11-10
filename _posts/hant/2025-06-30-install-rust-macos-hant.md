---
audio: false
generated: true
lang: hant
layout: post
title: 在 macOS 上使用 rustup 安裝 Rust
translated: true
type: note
---

## 使用 rustup 安裝 Rust

1. **開啟終端機**  
    您可以在**應用程式 > 工具程式**中找到終端機，或使用 Spotlight 搜尋。

2. **安裝 rustup 和 Rust**  
    執行以下指令來下載並執行 rustup 安裝腳本：

    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

    腳本會提示您繼續。按 `1` 選擇預設安裝。

3. **設定您的 Shell**  
    安裝完成後，您可能需要將 Rust 加入系統 `PATH`。安裝程式會提供類似以下的指令：

    ```sh
    source $HOME/.cargo/env
    ```

    將此行加入您的 shell 設定檔（例如 `.zshrc`、`.bashrc` 或 `.bash_profile`），以便在未來的 session 中使用 Rust。

4. **驗證安裝**  
    檢查 Rust 是否正確安裝：

    ```sh
    rustc --version
    ```

    如果安裝成功，您應該會看到 Rust 編譯器版本。

---

## 使用 Homebrew 安裝 Rust

您也可以使用 [Homebrew](https://brew.sh/) 來安裝 Rust，但一般建議使用 `rustup` 以便更容易更新和管理版本。

1. **安裝 Homebrew**（如果尚未安裝）：

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **使用 Homebrew 安裝 Rust**：

    ```sh
    brew install rust
    ```

3. **驗證安裝**：

    ```sh
    rustc --version
    ```

---

## 編譯 Rust 程式碼

1. **撰寫 Rust 程式**  
    建立一個名為 `main.rs` 的檔案，內容如下：

    ```rust
    fn main() {
         println!("Hello, World!");
    }
    ```

2. **編譯程式**  
    在終端機中，導航至包含您的檔案的目錄並執行：

    ```sh
    rustc main.rs
    ```

3. **執行編譯後的程式**：

    ```sh
    ./main
    ```

---

此設定應能協助您在 macOS 上開始進行 Rust 開發。如果您遇到任何問題，歡迎隨時提問！