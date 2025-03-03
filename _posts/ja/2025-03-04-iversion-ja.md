---
audio: false
generated: true
lang: ja
layout: post
title: iOSでiVersionを使用する
translated: true
---

`iVersion` ポッドをiOSプロジェクトで使用するには、以下の手順に従ってください：

1. **Xcodeでプロジェクトを開く**: `iVersion` ポッドを追加したいXcodeプロジェクトを開いてください。

2. **CocoaPodsの初期化**: プロジェクトでまだCocoaPodsを初期化していない場合、ターミナルを開き、プロジェクトディレクトリに移動し、以下のコマンドを実行してください：
   ```bash
   pod init
   ```
   これにより、プロジェクトディレクトリに`Podfile`が作成されます。

3. **Podfileの編集**: テキストエディタまたはXcodeで`Podfile`を開き、`iVersion` ポッドを`Podfile`に追加します。ターゲットセクション内に以下の行を含めます：
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **Podのインストール**: `Podfile`を保存し、ターミナルに戻り、以下のコマンドを実行して`iVersion` ポッドをインストールします：
   ```bash
   pod install
   ```

5. **`.xcworkspace` ファイルを開く**: インストールが完了したら、Xcodeプロジェクトが開いている場合は閉じ、新しく作成された`.xcworkspace` ファイルを開きます。このファイルは通常、元の`.xcodeproj` ファイルと同じディレクトリにあります。

6. **iVersionのインポート**: SwiftまたはObjective-Cファイルで`iVersion` モジュールをインポートして使用を開始します：
   ```swift
   import iVersion
   ```

7. **コードでiVersionを使用**: これで、`iVersion` ライブラリをプロジェクトで使用できます。例えば、`iVersion`で提供されるメソッドを使用してアプリのバージョンやビルド番号を確認できます。

これらの手順に従うことで、`iVersion` ポッドをiOSプロジェクトに成功して統合し、使用することができます。