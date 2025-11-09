---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: MongoDB包括ガイド
translated: true
type: note
---

MongoDBは、現代のアプリケーション開発向けに設計された人気のオープンソースNoSQLドキュメントデータベースです。データを柔軟なJSONライクなドキュメントであるBSON（Binary JSON）形式で保存し、非構造化または半構造化データの処理に理想的です。従来のリレーショナルデータベースとは異なり、MongoDBはスキーマレスアプローチを採用しており、コレクション（ドキュメントのグループ）が異なる構造を持つことを可能にします。高い拡張性を持ち、シャーディングによる水平スケーリングをサポートし、レプリケーションによる高可用性を提供します。MongoDBはオンプレミス、MongoDB Atlas（マネージドサービス）を介したクラウド、またはハイブリッド環境で展開できます。このガイドでは、MongoDB Shell（mongosh）を使用した例とともに、基本から高度なトピックまでを網羅します。

## はじめに

MongoDBは、迅速な開発、柔軟なデータモデル、および高性能が求められるシナリオで優れています。主な機能は以下の通りです：
- **ドキュメントモデル**: ネストされた構造を持つ自己完結型のドキュメントとしてデータを扱います。
- **クエリ言語**: JavaScriptオブジェクトに似た構文を使用した豊富なクエリ。
- **拡張性**: 分散システムのための組み込みサポート。
- **エコシステム**: 公式ドライバーを介してPython、Node.js、Javaなどの言語と統合。

Adobe、eBay、Forbesなどの企業で、ビッグデータ、リアルタイム分析、コンテンツ管理を含むアプリケーションに使用されています。

## インストール

MongoDBはCommunity（無料、オープンソース）およびEnterpriseエディションを提供しています。インストール方法はプラットフォームによって異なります。セキュリティのため、常に公式サイトからダウンロードしてください。

### Windows
- MongoDB Download CenterからMSIインストーラーをダウンロードします。
- インストーラーを実行し、「Complete」セットアップを選択し、MongoDB Compass（GUIツール）を含めます。
- MongoDBの`bin`ディレクトリ（例: `C:\Program Files\MongoDB\Server\8.0\bin`）をPATHに追加します。
- データディレクトリを作成: `mkdir -p C:\data\db`。
- サーバーを起動: `mongod.exe --dbpath C:\data\db`。

サポート: Windows 11, Server 2022/2019。

### macOS
- Homebrewを使用: `brew tap mongodb/brew && brew install mongodb-community`。
- またはTGZアーカイブをダウンロードし、展開してPATHに追加します。
- データディレクトリを作成: `mkdir -p /data/db`。
- 起動: `mongod --dbpath /data/db`（または`brew services start mongodb/brew/mongodb-community`を使用）。

サポート: macOS 11–14 (x86_64およびarm64)。

### Linux
- Ubuntu/Debianの場合: MongoDBリポジトリキーとリストを追加し、`apt-get install -y mongodb-org`を実行。
- RHEL/CentOSの場合: リポジトリファイルを使用してyum/dnfでインストール。
- データディレクトリを作成: `sudo mkdir -p /data/db && sudo chown -R $USER /data/db`。
- 起動: `sudo systemctl start mongod`。

サポート: Ubuntu 24.04, RHEL 9+, Debian 12, Amazon Linux 2023など。XFS/EXT4ファイルシステムを使用。32ビットは避ける。

### クラウド (MongoDB Atlas)
- mongodb.com/atlas でサインアップ。
- UIまたはCLIで無料クラスターを作成: `atlas clusters create <name> --provider AWS --region us-east-1 --tier M0`。
- IPをホワイトリストに登録: `atlas network-access create <IP>`。
- 接続文字列を取得して接続: `mongosh "mongodb+srv://<user>:<pass>@cluster0.abcde.mongodb.net/"`。

Atlasはバックアップ、スケーリング、監視を自動的に処理します。

## コアコンセプト

### データベース
コレクションのコンテナであり、データを論理的に分離します。初回使用時に暗黙的に作成: `use mydb`。`use mydb`で切り替え。一覧表示: `show dbs`。

### コレクション
ドキュメントのグループ。テーブルのようなものですが、スキーマが柔軟です。暗黙的に作成: `db.mycollection.insertOne({})`。一覧表示: `show collections`。

### ドキュメント
基本単位: キーと値のペアを持つBSONオブジェクト。例:
```javascript
{ "_id": ObjectId("..."), "name": "John", "age": 30, "address": { "city": "NYC", "zip": 10001 } }
```
配列、ネストされたオブジェクト、日付、バイナリなどの型をサポート。

### BSON
効率的なストレージ/ネットワーキングのためのバイナリ形式。ObjectId、Date、Binaryなどの型でJSONを拡張。

### 名前空間
一意の識別子: `database.collection`（例: `mydb.orders`）。

セットアップ例:
```javascript
use test
db.orders.insertMany([
  { item: "almonds", price: 12, quantity: 2 },
  { item: "pecans", price: 20, quantity: 1 }
])
```

## CRUD操作

mongoshで`db.collection.method()`を使用。複数ドキュメントのACIDにはセッションを使用したトランザクション。

### 作成 (Insert)
- 単一: `db.users.insertOne({ name: "Alice", email: "alice@example.com" })`
- 複数: `db.users.insertMany([{ name: "Bob" }, { name: "Charlie" }])`
挿入されたIDを返します。

### 読み取り (Find)
- すべて: `db.users.find()`
- フィルター: `db.users.find({ age: { $gt: 25 } })`
- 整形表示: `.pretty()`
- 制限/ソート: `db.users.find().limit(5).sort({ age: -1 })`

### 更新
- 単一: `db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })`
- 複数: `db.users.updateMany({ age: { $lt: 20 } }, { $set: { status: "minor" } })`
- インクリメント: `{ $inc: { score: 10 } }`

### 削除
- 単一: `db.users.deleteOne({ name: "Bob" })`
- 複数: `db.users.deleteMany({ status: "inactive" })`
- コレクション削除: `db.users.drop()`

## クエリとインデックス

### クエリ
条件に述語を使用。等値、範囲、論理演算子をサポート。

- 基本: `db.inventory.find({ status: "A" })` (SQL相当: `WHERE status = 'A'`)
- $in: `db.inventory.find({ status: { $in: ["A", "D"] } })`
- $lt/$gt: `db.inventory.find({ qty: { $lt: 30 } })`
- $or: `db.inventory.find({ $or: [{ status: "A" }, { qty: { $lt: 30 } }] })`
- 正規表現: `db.inventory.find({ item: /^p/ })` ("p"で始まる)
- 埋め込み: `db.users.find({ "address.city": "NYC" })`

射影（フィールド選択）: `db.users.find({ age: { $gt: 25 } }, { name: 1, _id: 0 })`

### インデックス作成
フルスキャンを避け、クエリ速度を向上。Bツリーベース。

- 種類: 単一フィールド(`db.users.createIndex({ name: 1 })`)、複合(`{ name: 1, age: -1 }`)、一意(`{ email: 1 }`)。
- 利点: 等値/範囲クエリの高速化、ソート結果。
- 作成: `db.users.createIndex({ age: 1 })`（昇順）。
- 表示: `db.users.getIndexes()`
- 削除: `db.users.dropIndex("age_1")`

推奨事項にはAtlas Performance Advisorを使用。トレードオフ: 書き込み速度の低下。

## アグリゲーションフレームワーク

パイプライン内のステージを通じてデータを処理。SQLのGROUP BYに似ているが、より強力。

- 基本: `db.orders.aggregate([ { $match: { price: { $lt: 15 } } } ])`
- ステージ: `$match`（フィルター）、`$group`（集計: `{ $sum: "$price" }`）、`$sort`、`$lookup`（結合: `{ from: "inventory", localField: "item", foreignField: "sku", as: "stock" }`）、`$project`（再形成）。
- 例（結合とソート）:
```javascript
db.orders.aggregate([
  { $match: { price: { $lt: 15 } } },
  { $lookup: { from: "inventory", localField: "item", foreignField: "sku", as: "inventory_docs" } },
  { $sort: { price: 1 } }
])
```
式: `{ $add: [ "$price", 10 ] }`。Atlas UIでプレビュー可能。

## スキーマ設計

MongoDBの柔軟性は厳密なスキーマを不要にしますが、パフォーマンスのためには注意深い設計が必要です。

- **原則**: アクセスパターン（読み取り/書き込み）に合わせてモデル化し、インデックスを使用し、ワーキングセットをRAMに保持。
- **埋め込み**: 関連データを1つのドキュメントに非正規化し、アトミックな読み取り/書き込みを実現。例: 投稿にコメントを埋め込み。長所: 高速なクエリ。短所: 重複、大きなドキュメント。
- **参照**: IDで正規化。例: `posts`が`userId`を介して`users`を参照。結合には`$lookup`を使用。長所: 重複が少ない。短所: 複数クエリ。
- パターン: 一対少数（埋め込み）、一対多数（参照または配列埋め込み）、多対多（参照）。
- 検証: `db.createCollection("users", { validator: { $jsonSchema: { ... } } })`で強制。

重複のトレードオフとアトミック性（ドキュメントレベルでのみ）を考慮。

## レプリケーションとシャーディング

### レプリケーション
レプリカセット（`mongod`インスタンスのグループ）を介して冗長性/高可用性を提供。

- 構成要素: プライマリ（書き込み）、セカンダリ（oplog経由で複製、読み取りはオプション）、アービター（投票、データなし）。
- 展開: `rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "host1:27017" }] })`で初期化。メンバー追加: `rs.add("host2:27017")`。
- 選挙: プライマリが失敗した場合、セカンダリが約10-12秒で選出。
- 読み取り設定: `primary`、`secondary`（遅延の可能性あり）。
- フェイルオーバー、バックアップに使用。遅延を管理するためにフロー制御を有効化。

### シャーディング
水平スケーリング: データをシャード間で分散。

- 構成要素: シャード（レプリカセット）、Mongos（ルーター）、設定サーバー（メタデータ）。
- シャードキー: パーティショニングのためのフィールド（例: 均等分散のためのハッシュ化）。最初にインデックスを作成。
- セットアップ: シャーディングを有効化 `sh.enableSharding("mydb")`、コレクションをシャード化 `sh.shardCollection("mydb.users", { userId: "hashed" })`。
- バランサー: 均一な負荷のためにチャンクを移行。地理的局所性のためのゾーン。
- 戦略: ハッシュ化（均一）、範囲（特定のクエリ）。

mongos経由で接続。トランザクションをサポート。

## セキュリティ

多層防御で展開を保護。

- **認証**: SCRAM、LDAP、OIDC、X.509。ユーザー作成: `db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })`。
- **承認**: ロールベースアクセス制御（RBAC）。組み込みロール: read、readWrite、dbAdmin。
- **暗号化**: 転送中のTLS/SSL、保存時の暗号化（EAR）（AWS KMS/Google Cloud KMS/Azure Key Vault経由）。機密フィールドのためのクライアントサイドフィールドレベル暗号化（CSFLE）。
- ネットワーク: IPアクセスリスト、AtlasでのVPCピアリング。
- 監査: 操作をログ記録。

起動時に認証を有効化: `--auth`。組み込みセキュリティにはAtlasを使用。

## ベストプラクティス

- **本番環境セットアップ**: サービスとして実行（systemctl/brew）。データ/ジャーナル/ログをSSDで分離。WiredTigerエンジン（デフォルト）を使用。
- **監視**: `mongostat`、`mongotop`、Atlasチャート。接続数(`connPoolStats`)、キャッシュ追い出し、I/O(`iostat`)を監視。
- **バックアップ**: `mongodump`/`mongorestore`、またはAtlasスナップショット。論理（JSON）対物理（ファイル）。
- **パフォーマンス**: インデックスを賢く使用、射影を制限、大きな配列を避ける。`ulimit -n 64000`を設定、スワップを無効化(`vm.swappiness=0`)、TCPキープアライブを調整。
- **スケーリング**: レプリカセットから開始。100GB以上または高スループット時にシャーディング。
- **データインポート**: `mongoimport --db test --collection users --file users.json`。
- **ツール**: MongoDB Compass（GUI）、mongosh（シェル）、アプリ用ドライバー。
- **一般的な落とし穴**: 過度な埋め込み（ドキュメントサイズ制限16MB）、インデックスの無視、レプリケーション遅延の未処理。

開発にはAtlas M0無料ティアを使用。ワークロードは`mongoperf`でテスト。

## 参考文献
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [MongoDB Installation](https://www.mongodb.com/docs/manual/installation/)
- [MongoDB Core Concepts](https://www.mongodb.com/docs/manual/core/)
- [MongoDB CRUD](https://www.mongodb.com/docs/manual/crud/)
- [MongoDB Querying](https://www.mongodb.com/docs/manual/tutorial/query-documents/)
- [MongoDB Indexes](https://www.mongodb.com/docs/manual/indexes/)
- [MongoDB Aggregation](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
- [MongoDB Schema Design](https://www.mongodb.com/docs/manual/core/data-model-design/)
- [MongoDB Replication](https://www.mongodb.com/docs/manual/replication/)
- [MongoDB Sharding](https://www.mongodb.com/docs/manual/sharding/)
- [MongoDB Security](https://www.mongodb.com/docs/manual/core/security/)
- [MongoDB Production Notes](https://www.mongodb.com/docs/manual/administration/production-notes/)