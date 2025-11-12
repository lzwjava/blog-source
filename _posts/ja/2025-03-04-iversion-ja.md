---
audio: false
generated: true
lang: ja
layout: post
title: iOSでのiVersionの使用方法
translated: true
type: note
---

iOSプロジェクトで`iVersion` podを使用するには、以下の手順に従ってください：

1. **Xcodeでプロジェクトを開く**：`iVersion` podを追加したいXcodeプロジェクトを開いていることを確認してください。

2. **CocoaPodsの初期化**：まだプロジェクトでCocoaPodsを初期化していない場合は、ターミナルを開き、プロジェクトディレクトリに移動して次のコマンドを実行します：
   ```bash
   pod init
   ```
   これにより、プロジェクトディレクトリに`Podfile`が作成されます。

3. **Podfileの編集**：テキストエディタまたはXcodeで`Podfile`を開きます。ターゲットセクション内に次の行を追加して`iVersion` podを追加します：
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **podのインストール**：`Podfile`を保存し、ターミナルに戻ります。次のコマンドを実行して`iVersion` podをインストールします：
   ```bash
   pod install
   ```

5. **`.xcworkspace`ファイルを開く**：インストールが完了したら、開いている場合はXcodeプロジェクトを閉じ、新しく作成された`.xcworkspace`ファイルを開きます。このファイルは通常、元の`.xcodeproj`ファイルと同じディレクトリにあります。

6. **iVersionのインポート**：SwiftまたはObjective-Cファイルで`iVersion`モジュールをインポートして使用を開始します：
   ```swift
   import iVersion
   ```

7. **コードでiVersionを使用**：これでプロジェクトで`iVersion`ライブラリを使用できます。例えば、`iVersion`が提供するメソッドを使用してアプリのバージョンやビルド番号を確認できます。

これらの手順に従うことで、iOSプロジェクトに`iVersion` podを正常に統合して使用できるはずです。