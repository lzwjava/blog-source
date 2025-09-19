---
audio: false
generated: false
image: false
lang: ja
layout: post
title: フラワー認識アプリ
translated: true
---

これは、GitHubプロジェクト[https://github.com/lzwjava/flower-recognition](https://github.com/lzwjava/flower-recognition)のREADME.mdです。

---

### フォルダー認識アプリ

これは、ユーザーが写真を撮影して円を描くことで花を認識するためのAndroidアプリケーションです。

#### 機能:
- **写真を撮影**: ユーザーはアプリ内で花の写真を撮影できます。
- **描画機能**: 花の画像に円や注釈を描くことで認識を助けることができます。
- **認証**: ログイン画面を持つセキュアなユーザー認証。
- **結果表示**: ユーザーフレンドリーなインターフェースで認識結果を表示します。
- **マテリアルデザイン**: 現代的で直感的なユーザーエクスペリエンスのためのマテリアルデザインの実装。

#### ファイル構造:
```
└── com
    └── lzw
        └── flower
            ├── activity
            │   ├── LoginActivity.java
            │   └── PhotoActivity.java
            ├── adapter
            │   └── PhotoAdapter.java
            ├── avobject
            │   └── Photo.java
            ├── base
            │   ├── App.java
            │   ├── ImageLoader.java
            │   └── SplashActivity.java
            ├── deprecated
            │   ├── CameraActivity.java
            │   └── Deprecated.java
            ├── draw
            │   ├── Draw.java
            │   ├── DrawActivity.java
            │   ├── DrawFragment.java
            │   ├── DrawView.java
            │   ├── HelpBtn.java
            │   ├── History.java
            │   ├── Tooltip.java
            │   └── ZoomImageView.java
            ├── fragment
            │   ├── RecogFragment.java
            │   └── WaitFragment.java
            ├── material
            │   └── MaterialActivity.java
            ├── result
            │   ├── FlowerAdapter.java
            │   ├── FlowerData.java
            │   ├── Image.java
            │   ├── ResultActivity.java
            │   └── ResultFragment.java
            ├── service
            │   └── PhotoService.java
            ├── utils
            │   ├── BitmapUtils.java
            │   ├── Crop.java
            │   ├── ImageListDialogBuilder.java
            │   ├── Logger.java
            │   ├── PathUtils.java
            │   └── Utils.java
            └── web
                ├── Upload.java
                ├── UploadImage.java
                └── Web.java
```

#### コンポーネント:
- **アクティビティ**: ログイン、写真撮影、スプラッシュスクリーンなど、アプリの異なるアクティビティを処理するクラスが含まれています。
- **アダプタ**: 写真と認識結果の表示を処理します。
- **AVObject**: メタデータを持つ写真オブジェクトを表します。
- **描画**: 花の画像に円や注釈を描く関連するクラス。
- **フラグメント**: 認識結果と待機インジケータを表示するためのUIコンポーネントを提供します。
- **マテリアル**: マテリアルデザインのガイドラインを実装するためのものかもしれません。
- **サービス**: 写真に関連する背景タスクとデータ操作を処理します。
- **ユーティリティ**: 画像操作やログ記録など、さまざまなタスクのためのユーティリティクラスを含みます。

#### 使い方:
1. リポジトリをクローンします。
2. Android Studioでプロジェクトを開きます。
3. アプリケーションをAndroidデバイスまたはエミュレータでビルドして実行します。

#### ライセンス:
このプロジェクトは[MITライセンス](LICENSE)の下でライセンスされています。