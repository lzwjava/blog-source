---
audio: false
generated: true
lang: ja
layout: post
title: キートゥールでの証明書のインポート
translated: true
type: note
---

`keytool -importcert` コマンドを使用して証明書を `jre/lib/security/cacerts` ファイルにインポートしようとした際に、「password verification failed」エラーと `java.security.UnrecoverableException` が発生した件についてのご質問に対応するため、問題の理解、解決方法、そして可能性のあるパスワードについて段階的に説明します。

### 問題の理解

`keytool` ユーティリティは、Java Development Kit (JDK) に含まれるコマンドラインツールで、キーストアの管理に使用されます。キーストアは、暗号鍵と証明書を格納するファイルであり、多くの場合 SSL/TLS のようなネットワーク通信のセキュリティ保護に使用されます。`cacerts` ファイルは `jre/lib/security` に配置され、Java Runtime Environment (JRE) に付属する特定のキーストアです。これには、信頼された認証局 (CA) からの信頼済みルート証明書のコレクションが含まれており、Java アプリケーションはデフォルトでこれを使用してセキュアな接続を検証します。

新しい証明書を `cacerts` ファイルに追加するために `keytool -importcert` コマンドを実行する場合、キーストアの正しいパスワードを指定する必要があります。表示されているエラーメッセージ「password verification failed」に続く `java.security.UnrecoverableException` は、入力したパスワード（または正しく入力されなかったパスワード）がキーストアのパスワードと一致しないことを示しています。この例外は通常、提供されたパスワードが間違っているために `keytool` がキーストアにアクセスまたは変更できない場合に発生します。

### 問題のコマンド

使用しているコマンドは、おそらく以下のような形式です：

```
keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
```

- `-file mycert.crt`: インポートしたい証明書ファイルを指定します。
- `-keystore /path/to/jre/lib/security/cacerts`: `cacerts` キーストアへのパスを指定します。
- `-alias myalias`: キーストア内の証明書に一意の名前（エイリアス）を割り当てます。

このコマンドを実行すると、`keytool` はキーストアのパスワード入力を求めます。入力したパスワードが間違っている場合、説明されたエラーが発生します。

### 可能性のあるパスワードの特定

標準的な JRE インストール（Oracle や OpenJDK など）における `cacerts` ファイルの **デフォルトパスワード** は **"changeit"** です。これは、Java のバージョンやディストリビューションを跨いで文書化されているデフォルト値です。「changeit」という名前は、管理者がセキュリティ上の理由から変更したいかもしれないというリマインダーの役割を果たしますが、ほとんどの標準的で変更されていないインストール環境では、これは変更されていません。

コマンドがパスワード検証エラーで失敗しているため、最も可能性の高い問題は以下のいずれかです：
1. 「changeit」を正しく入力していない（例：タイプミス、大文字小文字の誤り - パスワードは大文字小文字を区別します）。
2. パスワードプロンプトが適切に処理されなかった。
3. 特定の環境において、デフォルトのパスワードが変更されている（ただし、システム管理者によって明示的に変更されない限り、`cacerts` ではこれはあまり一般的ではありません）。

お問い合わせにカスタム設定の示唆がないため、標準的な JRE インストール環境であり「changeit」が適用されると仮定します。

### 問題の解決方法

問題を解決する方法は以下の通りです：

1. **プロンプトでの正しいパスワード入力の確認**
   再度コマンドを実行します：

   ```
   keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
   ```

   パスワードを求められたら、注意して **"changeit"** （すべて小文字、スペースなし）と入力し、Enter キーを押します。タイプミスやキーボードレイアウトの問題がないか再度確認してください。

2. **コマンドラインでのパスワード指定**
   対話型プロンプトに関する問題（例：スクリプトやターミナルの動作不良）を避けるために、`-storepass` オプションを使用して直接パスワードを指定できます：

   ```
   keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
   ```

   これにより、「changeit」がパスワードとして明示的に渡され、プロンプトがバイパスされます。これでエラーなく動作する場合、以前の問題はパスワードの入力方法にあった可能性が高いです。

3. **権限の確認**
   `cacerts` は JRE ディレクトリ（例：Linux では `/usr/lib/jvm/java-11-openjdk/lib/security/cacerts`、Windows でも同様のパス）に存在するため、書き込み権限があることを確認してください。必要に応じて、管理者権限でコマンドを実行します：
   - Linux/Mac: `sudo keytool ...`
   - Windows: 管理者としてコマンドプロンプトを実行します。

   ただし、エラーがファイルアクセスに関するものではなくパスワード検証に関するものであるため、これは核心的な問題ではない可能性が高いですが、確認しておくことをお勧めします。

4. **パスワードの検証**
   「changeit」が依然として失敗する場合、環境によってパスワードが変更されている可能性があります。キーストアを変更せずにパスワードをテストするには、その内容をリスト表示してみてください：

   ```
   keytool -list -keystore /path/to/jre/lib/security/cacerts
   ```

   プロンプトが表示されたら「changeit」を入力します。証明書がリスト表示されれば、パスワードは正しいです。同じエラーが発生する場合、パスワードはデフォルトと異なります。

### 「changeit」がパスワードでない場合は？

「changeit」が機能しない場合は、以下の可能性を考慮してください：
- **カスタムパスワード**: 稀なケースですが、システム管理者が `cacerts` のパスワードを変更している可能性があります。システムの文書または管理者に問い合わせてパスワードを入手する必要があります。失われたキーストアのパスワードを直接回復する方法はありません。もし本当に不明な場合は、新しい JRE インストールから新しい `cacerts` ファイルに置き換える必要があるかもしれません（これによりパスワードは「changeit」にリセットされます）。
- **環境固有のデフォルト**: 一部の非標準的な Java ディストリビューション（例：IBM JDK）は異なるデフォルトを使用する場合がありますが、これは一般的ではなく、お問い合わせは標準的なセットアップを示唆しています。

追加の文脈がない限り、標準的な JRE 環境では「changeit」が最も可能性の高いパスワードです。

### 最終的な解決策

問題を修正するには：
- 標準的な JRE を想定して、以下のコマンドを使用します：

  ```
  keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
  ```

- これが失敗する場合は、`-list` コマンドでパスワードを検証するか、システム管理者に確認してください。

このシナリオにおける**可能性のあるパスワード**は、標準的な Java の慣習に基づくと **"changeit"** です。これが正しく入力され、`cacerts` ファイルがカスタマイズされていなければ、`java.security.UnrecoverableException` は解決するはずです。