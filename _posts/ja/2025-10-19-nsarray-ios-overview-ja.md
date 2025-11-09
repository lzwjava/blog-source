---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: iOS開発のためのNSArray概要
translated: true
type: note
---

### NSArrayとは何ですか？

`NSArray`は、AppleのFoundationフレームワークに含まれるクラスで、iOS SDK（およびmacOSなど）の一部です。これは不変（immutable）で順序付けられたオブジェクトのコレクションを表し、他のプログラミング言語における配列に似ています。つまり、一度`NSArray`を作成すると、要素の追加、削除、置換はできず、読み取りのみ可能です。Objective-Cを使用したiOSアプリ開発において、ユーザー設定、データベースクエリの結果、UI要素などのデータリストを保存・管理するためによく使用されます。

主な特徴：
- **不変（Immutable）**：作成後はサイズと内容が固定されます（可変版には`NSMutableArray`を使用します）。
- **オブジェクトに対する型安全**：Objective-Cオブジェクト（例：`NSString`、`NSNumber`、カスタムクラス）へのポインタを格納します。プリミティブ型は直接サポートせず、`NSNumber`などでラップする必要があります。
- **インデックスによるアクセス**：要素は整数のインデックス（0始まり）でアクセスします。
- **スレッドセーフ**：一般的に同時読み取りは安全ですが、書き込みは安全ではありません（不変であるため）。
- **統合性**：`NSDictionary`、`NSString`、Cocoa TouchのUIコンポーネントなど、他のFoundationクラスとシームレスに連携します。

Swiftでは、`NSArray`は`Array`にブリッジされますが、Objective-C（レガシーなiOSコードで一般的）で作業する場合は、直接`NSArray`を使用します。

### iOSでのNSArrayの使用方法

iOSプロジェクトで`NSArray`を使用するには：
1. Foundationフレームワークをインポートします（通常、iOSアプリではデフォルトで含まれています）。
   ```objc
   #import <Foundation/Foundation.h>
   ```

2. **NSArrayの作成**：
   - リテラル構文（iOS 6以降）：`@[object1, object2, ...]`
   - 初期化メソッド：`[[NSArray alloc] initWithObjects:object1, object2, nil]`
   - C配列から：`initWithArray:copyItems:`

   例：
   ```objc
   NSArray *fruits = @[@"apple", @"banana", @"cherry"];
   // または：
   NSArray *numbers = [[NSArray alloc] initWithObjects:@1, @2, @3, nil];
   ```

3. **要素へのアクセス**：
   - アイテムの取得：`objectAtIndex:`
   - 長さの取得：`count`
   - 先頭/末尾の要素：`firstObject` / `lastObject`
   - 存在確認：`containsObject:`

   例：
   ```objc
   NSString *firstFruit = [fruits objectAtIndex:0]; // "apple"
   NSUInteger count = [fruits count]; // 3
   BOOL hasOrange = [fruits containsObject:@"orange"]; // NO
   ```

4. **反復処理**：
   - 高速列挙：`for (id obj in array) { ... }`
   - ブロックベースの反復：`enumerateObjectsUsingBlock:`（iOS 4以降）

   例：
   ```objc
   for (NSString *fruit in fruits) {
       NSLog(@"Fruit: %@", fruit);
   }
   ```

5. **一般的な操作**：
   - ソート：`sortedArrayUsingSelector:` または `sortedArrayUsingComparator:`
   - フィルタリング：`filteredArrayUsingPredicate:`（NSPredicateを使用）
   - 結合：文字列の場合 `componentsJoinedByString:`
   - ファイルへの書き込み：`writeToFile:atomically:`

   例（フィルタリング）：
   ```objc
   NSPredicate *predicate = [NSPredicate predicateWithFormat:@"length > 5"];
   NSArray *longFruits = [fruits filteredArrayUsingPredicate:predicate];
   // 結果：@[@"banana", @"cherry"]
   ```

6. **iOSコンテキストでの使用**：
   - **テーブルビュー**：`NSArray`を`UITableView`のデータソースメソッド（`tableView:numberOfRowsInSection:`では`count`を、`tableView:cellForRowAtIndexPath:`では`objectAtIndex:`を使用）に渡します。
   - **ユーザーデフォルト**：`NSUserDefaults`で保存/取得：`[defaults setObject:array forKey:@"savedItems"];`
   - **JSON処理**：`JSONObjectWithData:options:error:`を使用して`NSData`と相互変換します。

可変の配列が必要な場合（例：動的にアイテムを追加する）は、`NSMutableArray`に切り替えます：
```objc
NSMutableArray *mutableFruits = [NSMutableArray arrayWithArray:fruits];
[mutableFruits addObject:@"date"];
```

### ヒント
- クラッシュを避けるため、常に`nil`や境界値をチェックします：`objectAtIndex:`を使用する際はインデックスの検証を行います。
- パフォーマンス：アクセスはO(1)、検索はO(n)です。
- モダンなiOS開発：新しいプロジェクトではSwiftの`Array`を検討してください—より型安全です。

[NSArray Documentation](https://developer.apple.com/documentation/foundation/nsarray)  
[NSMutableArray Documentation](https://developer.apple.com/documentation/foundation/nsmutablearray)