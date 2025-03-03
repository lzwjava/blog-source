---
audio: false
generated: true
lang: ja
layout: post
title: Android サポート ライブラリ
translated: true
---

Android Support Library のバージョン `support-v4:19.1.0` は、Android Support Library（特に v4 互換ライブラリ）の古いバージョンであり、リリース時（約 2014 年）の最新の API レベルよりも低い API レベルを実行する Android デバイス向けに後方互換性のある API を提供します。このライブラリを使用することで、新しい Android バージョンで導入された機能（例：フラグメント、ローダー、その他のユーティリティ）を古いデバイスで使用できます。

`support-v4:19.1.0` は、AndroidX ライブラリによって置き換えられていますが、古いプロジェクトを維持するためにこの特定のバージョンを使用する必要がある場合、以下のように設定して使用することができます。

---

### ステップ 1: 依存関係の追加
`support-v4:19.1.0` を使用するには、プロジェクトに依存関係として含める必要があります。これは通常、`build.gradle` ファイル（モジュール: app）で行います。

#### Gradle ベースのプロジェクト
1. `app/build.gradle` ファイルを開きます。
2. `dependencies` ブロックに次の行を追加します：

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Android Studio で「今すぐ同期」をクリックしてプロジェクトを Gradle と同期します。

#### 注意点:
- `compileSdkVersion` を 19（Android 4.4 KitKat）以上に設定してください。このライブラリは API 19 の機能に対応しています。
- `support-v4:19.1.0` でサポートされる最小 SDK バージョンは API 4（Android 1.6）ですが、アプリの要件に基づいて `minSdkVersion` を設定してください。

例 `build.gradle`:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // 必要に応じて調整
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### ステップ 2: 利用可能性の確認
Android Support ライブラリは、Google の Maven リポジトリにホストされています。Android Studio 3.0 以降では、このリポジトリはデフォルトで含まれています。古いバージョンの Android Studio を使用している場合は、プロジェクトレベルの `build.gradle` に次のように設定してください：

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // 注意: JCenter は非推奨ですが、古いライブラリには使用されました
    }
}
```

ライブラリのダウンロードに問題が発生した場合、SDK マネージャーを使用して Android Support リポジトリをインストールする必要があります：
1. `ツール > SDK マネージャー` に移動します。
2. 「SDK ツール」タブで「Android Support リポジトリ」を選択し、インストールします。

---

### ステップ 3: コードでのライブラリの使用
`support-v4` ライブラリには、`Fragment`、`Loader`、`AsyncTaskLoader` などのさまざまなクラスが含まれています。以下に、一般的なコンポーネントの使用例を示します。

#### 例 1: フラグメントの使用
`support-v4` ライブラリには、古い Android バージョンでも動作する `Fragment` クラスが含まれています。

```java
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class MyFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_layout, container, false);
    }
}
```

このフラグメントをアクティビティで使用するには：
```java
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.os.Bundle;

public class MainActivity extends FragmentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FragmentManager fm = getSupportFragmentManager();
        fm.beginTransaction()
            .add(R.id.fragment_container, new MyFragment())
            .commit();
    }
}
```

#### 例 2: ActivityCompat の使用
`ActivityCompat` クラスには、後方互換性のある機能（例：API 23 で導入されたパーミッションのリクエスト）を提供するヘルパーメソッドが含まれています。

```java
import android.support.v4.app.ActivityCompat;
import android.Manifest;
import android.content.pm.PackageManager;

public class MainActivity extends FragmentActivity {
    private static final int REQUEST_CODE = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.CAMERA},
                    REQUEST_CODE);
        }
    }
}
```

---

### ステップ 4: 考慮事項
- **非推奨ライブラリ**: Android Support Library（`support-v4:19.1.0` 含む）は非推奨です。現代的な開発には、AndroidX（例：`androidx.legacy:legacy-support-v4:1.0.0`）に移行してください。AndroidX は後継であり、継続的な更新とサポートを提供します。
- **バージョンの一致**: 他のサポートライブラリ（例：`appcompat-v7`）を使用する場合は、すべてのバージョンが 19.1.0 に一致していることを確認してください。
- **最小 SDK**: `support-v4:19.1.0` は API 4+ をサポートしていますが、一部の機能はより高い `minSdkVersion`（例：API 14）が必要です。

---

### ステップ 5: AndroidX にの移行（オプションですが推奨）
古いプロジェクトを維持している場合は、AndroidX に移行を検討してください：
1. Android Studio で `リファクタリング > AndroidX に移行` を選択します。
2. 依存関係を更新し、例：`com.android.support:support-v4:19.1.0` を `androidx.legacy:legacy-support-v4:1.0.0` に置き換えます。
3. Android Studio が提供する移行ガイドに従います。

---

### トラブルシューティング
- **「ライブラリが見つかりません」**: インターネット接続がアクティブであることを確認し、Google Maven リポジトリがアクセス可能であることを確認してください。
- **バージョンの不一致**: サポートライブラリのバージョンが一致しないエラーが発生した場合は、すべての `com.android.support` 依存関係を 19.1.0 に揃えます。
- **古い機能**: `support-v4:19.1.0` の一部の API（例：`AsyncTask`）は古いです。ドキュメントで代替手段を確認してください。

特定の使用例や設定に関するヘルプが必要な場合は、お知らせください！