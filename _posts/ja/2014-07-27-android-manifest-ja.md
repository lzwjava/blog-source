---
audio: false
generated: false
image: false
lang: ja
layout: post
title: AndroidManifest.xml ファイルの理解
translated: true
type: post
---

Android開発に取り組む際、最初に出会うファイルの一つが`AndroidManifest.xml`です。これはアプリの青写真のようなもので、Androidシステムがアプリケーションについて知る必要があるすべての情報を提供します。今日は、「Flower」というアプリ（パッケージ名: `com.lzw.flower`）の例のマニフェストファイルを分解し、その主要なコンポーネント、概念、パターンを探っていきます。

---

#### AndroidManifest.xmlとは？

`AndroidManifest.xml`ファイルは、すべてのAndroidアプリに必要な設定ファイルです。プロジェクトのルートディレクトリにあり、アプリのパッケージ名、パーミッション、コンポーネント（例: アクティビティ）、必要なハードウェア/ソフトウェア機能などの基本情報を宣言します。Androidオペレーティングシステムが読むアプリの身分証明書のようなものです。

それでは、ステップバイステップで例を説明します。

---

### マニフェストの構造

以下は、読みやすさのために少し簡略化したマニフェストです：

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.lzw.flower"
    android:versionCode="8"
    android:versionName="1.5.2">

    <uses-sdk android:minSdkVersion="14" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-feature android:name="android.hardware.camera" />
    <uses-feature android:name="android.hardware.camera.autofocus" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

    <application
        android:label="@string/app_name"
        android:icon="@drawable/icon128"
        android:name=".base.App"
        android:theme="@style/AppTheme">

        <activity android:name=".deprecated.CameraActivity" android:screenOrientation="landscape" />
        <activity android:name=".base.SplashActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <activity android:name=".draw.DrawActivity" android:screenOrientation="landscape" />
        <activity android:name=".result.ResultActivity" android:screenOrientation="landscape" />
        <activity android:name=".material.MaterialActivity" android:screenOrientation="landscape" />
        <activity android:name=".activity.PhotoActivity" android:screenOrientation="landscape" />
        <activity android:name=".activity.LoginActivity" android:screenOrientation="portrait" />
    </application>
</manifest>
```

それでは、その核心セクションを分解し、その背後にある概念を説明します。

---

### 1. ルート`<manifest>`要素

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.lzw.flower"
    android:versionCode="8"
    android:versionName="1.5.2">
```

- **`xmlns:android`**: これは、Android固有の属性のためのXML名前空間を定義します。すべてのマニフェストで見られる標準的なボイラープレートです。
- **`package`**: これは、アプリの一意の識別子です（例: `com.lzw.flower`）。また、Java/Kotlinクラスのデフォルト名前空間でもあります。
- **`android:versionCode`**: これは、バージョンを追跡するための内部整数です（ここでは、`8`）。各更新で増加します。
- **`android:versionName`**: これは、ユーザーに表示される人間が読めるバージョン文字列です（ここでは、`1.5.2`）。

**概念**: `<manifest>`タグは、アプリのIDとバージョニングを設定し、システムがどのアプリを扱っているか、そしてどのように更新を処理するかを知ることができます。

---

### 2. SDKバージョンの`<uses-sdk>`

```xml
<uses-sdk android:minSdkVersion="14" />
```

- **`android:minSdkVersion`**: アプリがサポートする最小のAndroid APIレベルを指定します。API 14はAndroid 4.0（アイスクリームサンドウィッチ）に対応します。

**概念**: これは互換性を確保します。Android 4.0未満のバージョンを実行しているデバイスは、このアプリをインストールできません。`targetSdkVersion`や`maxSdkVersion`はここにありませんが、さらに互換性を細かく調整するために追加できます。

---

### 3. パーミッションの`<uses-permission>`

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

このアプリは、以下のパーミッションを要求しています：
- `CAMERA`: デバイスのカメラにアクセスするため。
- `WRITE_EXTERNAL_STORAGE`: ファイル（例: 画像）を外部ストレージに保存するため。
- `INTERNET`: ネットワークアクセスのため。
- `ACCESS_NETWORK_STATE`: ネットワーク接続を確認するため。
- `READ_PHONE_STATE`: デバイス情報（例: IMEI）にアクセスするため。
- `ACCESS_WIFI_STATE`: Wi-Fiの状態を確認するため。

**概念**: Androidは、ユーザーのプライバシーとセキュリティを保護するためのパーミッションシステムを使用しています。これらの宣言は、システム（およびユーザー）に対して、アプリがどのような機能にアクセスする必要があるかを伝えます。Android 6.0（API 23）以降では、危険なパーミッション（例: `CAMERA`）は、アプリコード内で実行時のリクエストも必要です。

---

### 4. 特徴の`<uses-feature>`

```xml
<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
```

- **`android.hardware.camera`**: アプリがカメラを必要とすることを宣言します。
- **`android.hardware.camera.autofocus`**: カメラがオートフォーカスをサポートする必要があることを指定します。

**概念**: パーミッションとは異なり、`<uses-feature>`タグはGoogle Playストアでアプリをフィルタリングします。カメラやオートフォーカスがないデバイスでは、アプリはインストール可能なものとして表示されません。これらがオプションとしてマークされている場合（`android:required="false"`）は除きます。

---

### 5. `<application>`要素

```xml
<application
    android:label="@string/app_name"
    android:icon="@drawable/icon128"
    android:name=".base.App"
    android:theme="@style/AppTheme">
```

- **`android:label`**: アプリの名前で、文字列リソースから取得されます（`@string/app_name`）。
- **`android:icon`**: アプリのアイコンで、ドロワブルリソースを参照します（`@drawable/icon128`）。
- **`android:name`**: カスタムアプリケーションクラス（`.base.App`）で、Androidの`Application`クラスを拡張してアプリ全体のロジックを提供します。
- **`android:theme`**: アプリのデフォルトのビジュアルテーマ（`@style/AppTheme`）。

**概念**: `<application>`タグは、アプリ全体の設定を定義します。リソースのような`@string`や`@drawable`は、`res/`フォルダに保存され、再利用性とローカライズを促進します。

---

### 6. アクティビティの`<activity>`

マニフェストには、アプリのUIスクリーンであるいくつかのアクティビティがリストされています：

#### 例1: スプラッシュスクリーン（ランチャーアクティビティ）

```xml
<activity
    android:name=".base.SplashActivity"
    android:theme="@android:style/Theme.Holo.Light.NoActionBar.Fullscreen">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

- **`android:name`**: クラス名（`.base.SplashActivity`）。
- **`intent-filter`**: これはアプリのエントリーポイント（`MAIN`アクション + `LAUNCHER`カテゴリ）としてマークされ、デバイスのアプリランチャーに表示されます。
- **`android:theme`**: アクションバーのないフルスクリーンテーマ。

**パターン**: ランチャーアクティビティは、通常スプラッシュスクリーンやホームスクリーンから始まる共通の開始点です。

#### 例2: カメラアクティビティ

```xml
<activity
    android:name=".deprecated.CameraActivity"
    android:screenOrientation="landscape">
```

- **`android:screenOrientation`**: 横向きモードを強制します。
- **`.deprecated`**: このアクティビティが古いものであることを示唆していますが、依然として含まれています。

**パターン**: アクティビティは、特定の使用例（例: カメラアプリは横向きで動作することが多い）のために向きを制御することが多いです。

#### その他のアクティビティ

マニフェストには、`DrawActivity`、`ResultActivity`、`PhotoActivity`など、他のアクティビティがリストされています。これらのパターンは似ています：
- 大部分は横向きモードを強制しているため、ビジュアルやメディアに重点を置いたアプリであることを示唆しています。
- 一部はアプリのデフォルトテーマをオーバーライドしています（例: `Theme.Holo.Light`）。

**概念**: アクティビティは、AndroidアプリのUIの構築要素です。各`<activity>`タグは、システムにスクリーンを登録します。

---

### このマニフェストの主要なパターン

1. **メディア中心の設計**: カメラ、ストレージ、オートフォーカスのパーミッションと特徴は、写真や描画アプリ（パッケージ名`com.lzw.flower`から推測すると、花を識別するアプリかもしれません）を示唆しています。
2. **向き制御**: `android:screenOrientation="landscape"`の頻繁な使用は、ビジュアルタスクに焦点を当てていることを示唆しています。
3. **モジュール化されたアクティビティ**: `CameraActivity`、`DrawActivity`、`ResultActivity`などの複数のアクティビティは、複数のステップのワークフローを示唆しています。
4. **リソースの使用**: `@string`、`@drawable`、`@style`への参照は、整理された、保守しやすい構造を示しています。

---

### 結論

`AndroidManifest.xml`は、単なる設定ファイル以上です。これは、アプリの目的と動作の窓口です。この場合、「Flower」は、カメラ機能、描画機能、ネットワーク機能を持つメディアアプリのようです。これにより、画像のアップロードや処理が可能です。そのコンポーネント、パーミッション、特徴、アクティビティを理解することで、Androidアプリの構造と自分のアプリを設計する方法がわかります。

同じようなものを作りたいですか？ 明確な目的（例: 花の識別）から始め、パーミッションと特徴を定義し、アクティビティをマッピングします。マニフェストがすべてを結びつけます！