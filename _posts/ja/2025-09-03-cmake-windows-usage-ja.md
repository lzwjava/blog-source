---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: WindowsにおけるCMakeの使用方法と解説
translated: true
type: note
---

素晴らしい質問です！**CMake**とは何か、特に**Windows**での使用方法、そして`cmake --build`のようなコマンドの実際の意味について順を追って説明します。

---

### 🔹 CMakeとは？
- **CMake**はクロスプラットフォームのビルドシステムジェネレータです。
- プロジェクト自体をビルドするの**ではなく**、お使いのプラットフォームとコンパイラに適したビルドファイル（Visual Studioソリューション、Makefile、Ninjaファイルなど）を作成します。
- その後、生成されたファイル（またはCMake独自のビルドドライバ）を使用して、実際にプロジェクトをコンパイルします。

---

### 🔹 WindowsでのCMakeインストール方法
1. ダウンロード元: [https://cmake.org/download/](https://cmake.org/download/)
2. インストールし、**「Add CMake to system PATH」** にチェックを入れる（または手動で追加する）。
3. ターミナル（PowerShellまたはCMD）で確認:
   ```sh
   cmake --version
   ```

---

### 🔹 Windowsでの典型的なCMakeワークフロー

プロジェクト構造が以下の場合：
```
project_root/
 ├─ CMakeLists.txt
 └─ src/
     └─ main.cpp
```

#### 1. ターミナルを開く
（MSVCを使用する場合は**x64 Native Tools Command Prompt for VS**を、`MinGW`/`Ninja`を使用する場合は通常のPowerShellを使用できます。）

#### 2. ビルドディレクトリを作成する
ソースとビルドを分離するのがベストです：
```sh
cd project_root
mkdir build
cd build
```

#### 3. ビルドシステムファイルを生成する
Visual Studioを使用する例：
```sh
cmake .. -G "Visual Studio 17 2022" -A x64
```

Ninjaを使用する例：
```sh
cmake .. -G Ninja
```

このステップでは`../CMakeLists.txt`を読み込み、必要なビルド定義を生成します。

#### 4. プロジェクトをビルドする
以下のコマンドを使用できます：
```sh
cmake --build .
```

- WindowsのVisual Studioでは、これは内部的に`MSBuild`を呼び出します。
- Ninjaでは、`ninja`ツールを呼び出します。

**Release**モードでビルドするようにCMakeに指示することもできます：
```sh
cmake --build . --config Release
```
⚠ 注意: `--config`はマルチ構成ジェネレータ（Visual Studio、Xcode）でのみ使用されます。NinjaやMakefileを使用する場合は、構成時に指定します：
```sh
cmake .. -DCMAKE_BUILD_TYPE=Release
```

#### 5. 実行ファイルを実行する
ビルド後、適切なディレクトリを確認してください：
- **Visual Studio**の場合: `build/Debug/` または `build/Release/`
- **Ninja**の場合: `build/`内

---

### 🔹 よく使うコマンド早見表
```sh
# プロジェクトの設定（ビルドファイルの生成）
cmake -S . -B build

# Releaseビルドタイプで設定（シングル構成ジェネレータ）
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release

# プロジェクトのビルド
cmake --build build

# 特定の構成でビルド（Visual Studio/Xcode用）
cmake --build build --config Release

# コンパイル出力をインストール（CMakeListsで定義されている場合）
cmake --install build
```

---

✅ **まとめ**:  
- **`cmake ..`** → 設定を行い、プラットフォーム固有のプロジェクト/ビルドファイルを生成します。  
- **`cmake --build .`** → 選択したビルドツールを使用して実際にコンパイルします。  
- Windowsでは、**Visual Studioジェネレータ**またはより高性能な**Ninja**をよく使用します。  

---

**最小限のCMakeLists.txtの例**と、Windowsでの簡単なC++「Hello World」プロジェクトのビルド手順をステップバイステップで説明しましょうか？