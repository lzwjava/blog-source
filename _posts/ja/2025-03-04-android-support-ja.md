---
audio: false
generated: true
lang: ja
layout: post
title: Androidサポートライブラリ
translated: true
type: note
---

Android Support Library バージョン `support-v4:19.1.0` は、Android Support Library（特に v4 互換性ライブラリ）の古いバージョンであり、リリース当時（2014年頃）の最新 API レベルよりも低い API レベルを実行している Android デバイス向けに、下位互換性のある API を提供します。このライブラリを使用すると、Fragment、Loader、その他のユーティリティなど、新しい Android バージョンで導入された機能を古いデバイスで使用できます。

`support-v4:19.1.0` はレガシーな Android Support Library の一部であるため、AndroidX ライブラリに取って代わられています。ただし、この特定のバージョンを使用する必要がある場合（例：古いプロジェクトを維持するため）、以下に Android プロジェクトでセットアップして使用する方法を示します。

---

### ステップ 1: 依存関係の追加
`support-v4:19.1.0` を使用するには、プロジェクトの依存関係として含める必要があります。これは通常、`build.gradle` ファイル（Module: app）で行われます。

#### Gradle ベースのプロジェクトの場合
1. `app/build.gradle` ファイルを開きます。
2. `dependencies` ブロックに次の行を追加します：

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Android Studio で「Sync Now」をクリックして、プロジェクトを Gradle と同期させます。

#### 注意点：
- このライブラリは API 19 の機能に合わせているため、`compileSdkVersion` が少なくとも 19（Android 4.4 KitKat）以上に設定されていることを確認してください。
- `support-v4:19.1.0` がサポートする最小 SDK バージョンは API 4（Android 1.6）ですが、アプリの要件に基づいて `minSdkVersion` を設定する必要があります。

`build.gradle` の例：
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
Android Support Libraries は Google の Maven リポジトリでホストされています。Android Studio 3.0 以降では、このリポジトリがデフォルトで含まれています。古いバージョンの Android Studio を使用している場合は、`build.gradle`（プロジェクトレベル）に以下が含まれていることを確認してください：

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // 注: JCenter は非推奨ですが、古いライブラリ用に使用されていました
    }
}
```

ライブラリのダウンロードに問題が発生した場合は、SDK マネージャー経由で Android Support Repository をインストールする必要があるかもしれません：
1. `Tools > SDK Manager` に移動します。
2. 「SDK Tools」タブで「Android Support Repository」をチェックしてインストールします。

---

### ステップ 3: コードでのライブラリの使用
`support-v4` ライブラリは、`Fragment`、`Loader`、`AsyncTaskLoader`、`ActivityCompat` などのユーティリティなど、さまざまなクラスを提供します。以下に、一般的なコンポーネントの使用方法の例を示します：

#### 例 1: Fragment の使用
`support-v4` ライブラリには、古い Android バージョンで動作するバックポートされた `Fragment` クラスが含まれています。

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
`ActivityCompat` クラスは、権限のリクエスト（API 23 で導入されましたが、サポートライブラリを使用することで以前のバージョンでも使用可能）など、下位互換性のある機能のヘルパーメソッドを提供します。

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
- **非推奨ライブラリ**: `support-v4:19.1.0` を含む Android Support Library は非推奨です。モダンな開発では、AndroidX（例: `androidx.legacy:legacy-support-v4:1.0.0`）への移行を推奨します。AndroidX は後継であり、継続的な更新とサポートを提供します。
- **バージョンの一致**: 他のサポートライブラリ（例: `appcompat-v7`）を使用する場合、バージョン不一致エラーを避けるために、それらが同じバージョン（19.1.0）であることを確認してください。
- **最小 SDK**: `support-v4:19.1.0` は API 4+ をサポートしていますが、後で導入された特定のコンポーネント（例: API 14 を必要とするもの）では、より高い `minSdkVersion` が必要な場合があります。

---

### ステップ 5: AndroidX への移行（オプションですが推奨）
古いプロジェクトを維持している場合は、AndroidX への移行を検討してください：
1. Android Studio で、`Refactor > Migrate to AndroidX` に移動します。
2. 依存関係を更新します。例： `com.android.support:support-v4:19.1.0` を `androidx.legacy:legacy-support-v4:1.0.0` に置き換えます。
3. Android Studio が提供する移行ガイドに従います。

---

### トラブルシューティング
- **「ライブラリが見つかりません」**: インターネット接続がアクティブであり、Google Maven リポジトリにアクセスできることを確認してください。
- **バージョンの不一致**: サポートライブラリのバージョンが一致しないというエラーが表示された場合は、すべての `com.android.support` 依存関係を 19.1.0 に合わせてください。
- **廃止された機能**: `support-v4:19.1.0` の一部の API（例: `AsyncTask`）は時代遅れです。代替手段についてはドキュメントを確認してください。

特定のユースケースやセットアップについてヘルプが必要な場合はお知らせください！