---
audio: false
generated: true
lang: ja
layout: post
title: Androidユニバーサルイメージローダー
translated: true
type: note
---

Universal Image Loader (UIL) バージョン1.9.3は、Androidアプリケーションで画像を読み込み、キャッシュし、表示するための強力で柔軟なライブラリです。以下は、Androidプロジェクトで使用するためのステップバイステップガイドです。このライブラリは古く、開発は終了しています（最終更新は2015年頃）ので、最新のプロジェクトではGlideやPicassoなどの代替を検討してください。ただし、特にUIL 1.9.3を使用する必要がある場合は、以下の手順に従ってください。

---

### ステップ1: プロジェクトにライブラリを追加する
UIL 1.9.3はMaven経由で利用可能なので、Gradleを使用してプロジェクトに追加できます。古いセットアップ（例: Eclipse）を使用している場合は、手動でJARファイルをダウンロードしてください。

#### Gradleを使用する場合（Android Studio）:
1. アプリの`build.gradle`ファイル（Module: app）を開きます。
2. `dependencies`ブロック内に以下の依存関係を追加します:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. Android Studioで「Sync Now」をクリックしてプロジェクトをGradleと同期します。

#### 手動でJARをセットアップする場合（例: Eclipse）:
1. MavenリポジトリまたはGitHubから`universal-image-loader-1.9.3.jar`をダウンロードします。
2. JARファイルをプロジェクトの`libs`フォルダに配置します。
3. IDEでJARを右クリックし、「Add to Build Path」（Eclipseの場合）を選択するか、プロジェクト設定で手動で設定します。

---

### ステップ2: パーミッションを追加する
インターネットから画像を読み込んだり、ストレージに保存したりするには、以下のパーミッションを`AndroidManifest.xml`に追加します:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: URLから画像をダウンロードするために必要です。
- `WRITE_EXTERNAL_STORAGE`: ディスクキャッシュに必要です（オフライン使用のために推奨）。Android 6.0+（API 23+）では、実行時にこのパーミッションをリクエストする必要もあります。

---

### ステップ3: ImageLoaderを初期化する
UILを使用する前に、設定で初期化する必要があります。これは通常、`Application`クラスまたはメインの`Activity`で一度行います。

#### カスタムApplicationクラスを作成する（推奨）:
1. 新しいクラスを作成します（例: `MyApplication.java`）:
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // グローバル設定を作成し、ImageLoaderを初期化
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // 画像読み込みスレッドの優先度を低く設定
               .denyCacheImageMultipleSizesInMemory()    // 複数サイズのキャッシュを防止
               .diskCacheSize(50 * 1024 * 1024)          // 50 MBのディスクキャッシュ
               .diskCacheFileCount(100)                  // キャッシュ内の最大ファイル数
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. このクラスを`AndroidManifest.xml`に登録します:
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### またはActivityで初期化する:
`Application`クラスを使用しない場合は、`Activity`の`onCreate()`メソッドで初期化します（ただし、一度だけ初期化されることを確認してください）:
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

### ステップ4: 画像を読み込んで表示する
初期化後、`ImageLoader`を使用して`ImageView`に画像を読み込めます。

#### 基本的な使用方法:
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // ImageViewに画像を読み込み
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### 表示オプションを使用した高度な使用方法:
`DisplayImageOptions`を使用して、画像の読み込みと表示方法をカスタマイズできます:
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
            .showImageForEmptyUri(R.drawable.error)     // URLが空の場合に表示する画像
            .showImageOnFail(R.drawable.error)          // 読み込み失敗時に表示する画像
            .cacheInMemory(true)                        // RAMにキャッシュ
            .cacheOnDisk(true)                          // ディスクにキャッシュ
            .build();

        // オプションを指定して画像を読み込み
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### ステップ5: ListViewまたはGridViewでUILを使用する
リストやグリッドでは、アダプターでUILを使用して効率的に画像を読み込みます。

#### カスタムアダプターの例:
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
    private String[] imageUrls; // 画像URLの配列

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

#### アダプターを設定:
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### UIL 1.9.3の主な機能
- **サポートされているURIタイプ**:
  - Web: `"http://example.com/image.jpg"`
  - SDカード: `"file:///mnt/sdcard/image.png"`
  - コンテンツプロバイダ: `"content://media/external/images/media/13"`
  - アセット: `"assets://image.png"`
  - ドローアブル: `"drawable://" + R.drawable.image`
- **キャッシュ**: メモリとディスクのキャッシュをサポート。
- **カスタマイズ**: スレッドプールサイズ、キャッシュサイズ、画像デコードオプションを設定で調整可能。

---

### トラブルシューティング
- **クラッシュ: "ImageLoader must be init with configuration"**  
  `displayImage`を呼び出す前に`ImageLoader.getInstance().init(config)`が呼び出されていることを確認してください。
- **画像が読み込まれない**  
  - インターネットパーミッションとURLの有効性を確認してください。
  - 設定でログを有効にし（`.writeDebugLogs()`）、問題をデバッグしてください。
- **メモリ不足エラー**  
  - 設定で`diskCacheSize`または`memoryCacheSize`を減らしてください。
  - 小さな画像を使用するか、`DisplayImageOptions`でダウンスケーリングを有効にしてください。

---

### 注意点
- **非推奨**: UIL 1.9.3は古くなっています（最終リリースは2014年頃）。最新のAndroid開発では、Glide（`implementation 'com.github.bumptech.glide:glide:4.16.0'`）やCoil（`implementation 'io.coil-kt:coil:2.6.0'`）を検討してください。
- **日付のコンテキスト**: 2025年3月3日現在、このガイドはUIL 1.9.3を必要とするレガシーコードを扱うことを想定しています。

特定のユースケースについてヘルプが必要な場合はお知らせください！