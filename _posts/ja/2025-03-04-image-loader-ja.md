---
audio: false
generated: true
lang: ja
layout: post
title: Androidのユニバーサルイメージローダー
translated: true
---

Universal Image Loader (UIL) バージョン 1.9.3 は、Android アプリケーションで画像を読み込み、キャッシュし、表示するための強力で柔軟なライブラリです。以下は、Android プロジェクトでそれを使用するためのステップバイステップのガイドです。このライブラリは古く、更新が停止されている（最終更新は約2015年）ため、現代的なプロジェクトでは Glide や Picasso のような代替手段を検討することをお勧めします。しかし、特定に UIL 1.9.3 を使用する必要がある場合は、以下のようにします：

---

### ステップ 1: ライブラリをプロジェクトに追加
UIL 1.9.3 は Maven を通じて利用可能なので、Gradle を使用してプロジェクトに追加できます。古いセットアップ（例：Eclipse）を使用している場合は、JAR ファイルを手動でダウンロードすることもできます。

#### Gradle を使用する（Android Studio）
1. アプリの `build.gradle` ファイル（モジュール：app）を開きます。
2. `dependencies` ブロックに次の依存関係を追加します：
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. Android Studio で「今すぐ同期」をクリックしてプロジェクトを Gradle と同期します。

#### 手動の JAR 設定（例：Eclipse）
1. Maven リポジトリまたは GitHub から `universal-image-loader-1.9.3.jar` をダウンロードします。
2. プロジェクトの `libs` フォルダに JAR ファイルを配置します。
3. IDE で JAR を右クリックし、「ビルドパスに追加」を選択します（Eclipse）またはプロジェクト設定で手動で設定します。

---

### ステップ 2: パーミッションを追加
インターネットから画像を読み込んだり、ストレージに保存したりするには、`AndroidManifest.xml` に次のパーミッションを追加します：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: URL から画像をダウンロードするために必要です。
- `WRITE_EXTERNAL_STORAGE`: ディスクキャッシュ（オフライン使用を推奨）のために必要です。Android 6.0+（API 23+）では、ランタイムでこのパーミッションを要求する必要もあります。

---

### ステップ 3: ImageLoader を初期化
UIL を使用する前に、設定で初期化する必要があります。これは通常、`Application` クラスまたはメイン `Activity` で一度行います。

#### カスタム Application クラスを作成する（推奨）
1. 新しいクラス（例：`MyApplication.java`）を作成します：
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // グローバル設定を作成し、ImageLoader を初期化
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // 画像読み込みスレッドの優先度を低く
               .denyCacheImageMultipleSizesInMemory()    // メモリ内で複数のサイズをキャッシュしない
               .diskCacheSize(50 * 1024 * 1024)          // 50 MB ディスクキャッシュ
               .diskCacheFileCount(100)                  // キャッシュ内の最大ファイル数
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. `AndroidManifest.xml` でこのクラスを登録します：
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### Activity で初期化する
`Application` クラスを使用しない場合、`Activity` の `onCreate()` メソッドで初期化します（ただし、一度だけ初期化されるようにします）：
```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
        .build();
    ImageLoader.getInstance().init(config);
}
```

---

### ステップ 4: 画像を読み込み表示
初期化後、`ImageLoader` を使用して `ImageView` に画像を読み込むことができます。

#### 基本的な使用方法：
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // ImageView に画像を読み込む
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### 表示オプションを使用した高度な使用方法：
`DisplayImageOptions` を使用して、画像の読み込みと表示方法をカスタマイズできます：
```java
import com.nostra13.universalimageloader.core.DisplayImageOptions;
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // 表示オプションを定義
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // 読み込み中に表示する画像
            .showImageForEmptyUri(R.drawable.error)     // URL が空の場合に表示する画像
            .showImageOnFail(R.drawable.error)          // 読み込み失敗時に表示する画像
            .cacheInMemory(true)                        // RAM にキャッシュ
            .cacheOnDisk(true)                          // ディスクにキャッシュ
            .build();

        // オプションを使用して画像を読み込む
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### ステップ 5: ListView または GridView で UIL を使用
リストやグリッドの場合、アダプターで UIL を効率的に使用します。

#### カスタムアダプターの例：
```java
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import com.nostra13.universalimageloader.core.ImageLoader;

public class ImageAdapter extends BaseAdapter {
    private Context context;
    private String[] imageUrls; // 画像 URL の配列

    public ImageAdapter(Context context, String[] imageUrls) {
        this.context = context;
        this.imageUrls = imageUrls;
    }

    @Override
    public int getCount() {
        return imageUrls.length;
    }

    @Override
    public Object getItem(int position) {
        return imageUrls[position];
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.list_item, parent, false);
        }

        ImageView imageView = convertView.findViewById(R.id.imageView);
        ImageLoader.getInstance().displayImage(imageUrls[position], imageView);

        return convertView;
    }
}
```

#### アダプターを設定：
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### UIL 1.9.3 の主要機能
- **サポートされる URI 種類**:
  - Web: `"http://example.com/image.jpg"`
  - SD カード: `"file:///mnt/sdcard/image.png"`
  - コンテンツプロバイダー: `"content://media/external/images/media/13"`
  - アセット: `"assets://image.png"`
  - ドロワブル: `"drawable://" + R.drawable.image`
- **キャッシュ**: メモリとディスクのキャッシュをサポート。
- **カスタマイズ**: スレッドプールのサイズ、キャッシュのサイズ、画像のデコードオプションは設定で調整できます。

---

### トラブルシューティング
- **クラッシュ: "ImageLoader must be init with configuration"**
  `displayImage` 呼び出しの前に `ImageLoader.getInstance().init(config)` が呼び出されていることを確認します。
- **画像が読み込まれない**
  - インターネットのパーミッションと URL の有効性を確認します。
  - 設定でログを有効にして（`.writeDebugLogs()`）問題をデバッグします。
- **メモリ不足エラー**
  - 設定で `diskCacheSize` または `memoryCacheSize` を減らします。
  - 小さな画像を使用するか、`DisplayImageOptions` でダウンサイジングを有効にします。

---

### 注意事項
- **非推奨**: UIL 1.9.3 は古い（最終リリースは約2014年）。現代的な Android 開発では、Glide（`implementation 'com.github.bumptech.glide:glide:4.16.0'`）または Coil（`implementation 'io.coil-kt:coil:2.6.0'`）を検討してください。
- **日付コンテキスト**: 2025年3月3日現在、このガイドは UIL 1.9.3 を必要とするレガシー コードを使用していることを前提としています。

特定の使用例でお手伝いが必要な場合は、お知らせください！