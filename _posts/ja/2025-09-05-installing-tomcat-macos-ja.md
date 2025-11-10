---
audio: false
generated: true
image: false
lang: ja
layout: post
title: macOSへのApache Tomcatインストール
translated: true
type: note
---

**macOS に Apache Tomcat をインストールして実行するためのステップバイステップガイド**:

---

### 1. Java の確認

Tomcat は Java を必要とします。インストールされているか確認してください:

```bash
java -version
```

Java のバージョン (例: `1.8` や `11` 以上) が表示されない場合は、インストールしてください。macOS では [Homebrew](https://brew.sh) を使うのが最も簡単です:

```bash
brew install openjdk@11
```

その後、リンクします:

```bash
brew link --force --overwrite openjdk@11
```

---

### 2. Tomcat のインストール (オプション A: Homebrew – 最も簡単)

Homebrew を使うと、Tomcat を素早くインストールできます:

```bash
brew install tomcat
```

これにより通常は最新バージョン (例: Tomcat 10) がインストールされます。

インストール先は以下の通りです:

```
/usr/local/Cellar/tomcat/<version>/libexec
```

Apple Silicon を使用している場合:

```
/opt/homebrew/Cellar/tomcat/<version>/libexec
```

以下のコマンドで実行します:

```bash
catalina run
```

---

### 3. Tomcat のインストール (オプション B: 手動ダウンロード – 正式な方法)

1.  [Apache Tomcat ウェブサイト](https://tomcat.apache.org/download-10.cgi) にアクセスし、最新の安定版リリース (`.tar.gz` を選択) をダウンロードします。

2.  ディレクトリに展開します。例:

    ```bash
    tar xvf apache-tomcat-10.*.tar.gz
    mv apache-tomcat-10.* ~/tomcat
    ```

3.  Tomcat を起動します:

    ```bash
    cd ~/tomcat/bin
    ./startup.sh
    ```

4.  停止するには:

    ```bash
    ./shutdown.sh
    ```

---

### 4. インストールの確認

ブラウザを開き、以下にアクセスします:

```
http://localhost:8080
```

Tomcat のウェルカムページが表示されるはずです。

---

### 5. (オプション) PATH への追加

どこからでも `startup.sh` を実行できるようにするために、`~/.zshrc` または `~/.bashrc` に以下を追加します:

```bash
export CATALINA_HOME=~/tomcat
export PATH=$CATALINA_HOME/bin:$PATH
```

リロードします:

```bash
source ~/.zshrc
```

---

👉 以上です。これで macOS 上で Tomcat がローカルで実行されています。

セットアップ後に、**macOS 上の Tomcat に WAR ファイルをデプロイする方法**もご紹介しましょうか？