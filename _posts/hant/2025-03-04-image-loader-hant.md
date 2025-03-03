---
audio: false
generated: true
lang: hant
layout: post
title: Android 通用圖片加載器
translated: true
---

Universal Image Loader (UIL) 1.9.3 是一個強大且靈活的圖片加載、快取和顯示庫，適用於 Android 應用程式。以下是如何在您的 Android 專案中使用它的分步指南。請注意，這個庫已經過時並已停止維護（最後更新約在 2015 年），因此對於現代項目，您可能會考慮使用替代方案，如 Glide 或 Picasso。然而，如果您特定需要使用 UIL 1.9.3，以下是如何操作的：

---

### 第 1 步：將庫添加到您的專案
由於 UIL 1.9.3 可通過 Maven 獲取，您可以使用 Gradle 將其添加到您的專案中。如果您使用的是較舊的設置（例如 Eclipse），您可以手動下載 JAR 文件。

#### 使用 Gradle（Android Studio）：
1. 打開您應用程式的 `build.gradle` 文件（模組：app）。
2. 在 `dependencies` 塊中添加以下依賴：
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. 通過點擊 Android Studio 中的“立即同步”來同步您的專案與 Gradle。

#### 手動 JAR 設置（例如 Eclipse）：
1. 從 Maven 存儲庫或 GitHub 下載 `universal-image-loader-1.9.3.jar`。
2. 將 JAR 文件放置在專案的 `libs` 文件夾中。
3. 在 IDE 中右鍵點擊 JAR，然後選擇“添加到構建路徑”（Eclipse）或在專案設置中手動配置。

---

### 第 2 步：添加權限
要從互聯網加載圖片或將其保存到存儲中，請在 `AndroidManifest.xml` 中添加以下權限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`：用於從 URL 下載圖片。
- `WRITE_EXTERNAL_STORAGE`：用於磁碟快取（可選，但建議用於離線使用）。對於 Android 6.0+（API 23+），您還需要在運行時請求此權限。

---

### 第 3 步：初始化 ImageLoader
在使用 UIL 之前，您必須使用配置對其進行初始化。這通常在 `Application` 類或主 `Activity` 中完成一次。

#### 創建自定義 Application 類（推薦）：
1. 創建一個新類（例如 `MyApplication.java`）：
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // 創建全局配置並初始化 ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // 降低圖片加載線程的優先級
               .denyCacheImageMultipleSizesInMemory()    // 防止快取多個大小
               .diskCacheSize(50 * 1024 * 1024)          // 50 MB 磁碟快取
               .diskCacheFileCount(100)                  // 快取中最多 100 個文件
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. 在 `AndroidManifest.xml` 中註冊此類：
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### 或在 Activity 中初始化：
如果您不想使用 `Application` 類，請在 `Activity` 的 `onCreate()` 方法中初始化它（但請確保它只初始化一次）：
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

### 第 4 步：加載和顯示圖片
初始化後，您可以使用 `ImageLoader` 將圖片加載到 `ImageView` 中。

#### 基本使用：
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // 將圖片加載到 ImageView 中
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### 高級使用（使用顯示選項）：
您可以使用 `DisplayImageOptions` 自定義圖片加載和顯示的方式：
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

        // 定義顯示選項
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // 加載時顯示的圖片
            .showImageForEmptyUri(R.drawable.error)     // 如果 URL 為空時顯示的圖片
            .showImageOnFail(R.drawable.error)          // 加載失敗時顯示的圖片
            .cacheInMemory(true)                        // 緩存到 RAM
            .cacheOnDisk(true)                          // 緩存到磁碟
            .build();

        // 使用選項加載圖片
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### 第 5 步：在 ListView 或 GridView 中使用 UIL
對於列表或網格，請在適配器中使用 UIL 以高效加載圖片。

#### 示例自定義適配器：
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
    private String[] imageUrls; // 圖片 URL 數組

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

#### 設置適配器：
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### UIL 1.9.3 的關鍵功能
- **支持的 URI 類型**：
  - 網絡：`"http://example.com/image.jpg"`
  - SD 卡：`"file:///mnt/sdcard/image.png"`
  - 内容提供者：`"content://media/external/images/media/13"`
  - 資產：`"assets://image.png"`
  - 繪圖：`"drawable://" + R.drawable.image`
- **快取**：支持內存和磁碟快取。
- **自定義**：可以在配置中調整線程池大小、快取大小和圖片解碼選項。

---

### 疑難解答
- **崩潰："ImageLoader 必須使用配置初始化"**
  確保在任何 `displayImage` 调用之前調用 `ImageLoader.getInstance().init(config)`。
- **圖片未加載**
  - 檢查互聯網權限和 URL 有效性。
  - 在配置中啟用日誌記錄（`.writeDebugLogs()`）以調試問題。
- **內存不足錯誤**
  - 降低配置中的 `diskCacheSize` 或 `memoryCacheSize`。
  - 使用較小的圖片或在 `DisplayImageOptions` 中啟用縮放。

---

### 注意事項
- **廢棄**：UIL 1.9.3 已過時（最後發布約 2014 年）。對於現代 Android 開發，請考慮使用 Glide（`implementation 'com.github.bumptech.glide:glide:4.16.0'`）或 Coil（`implementation 'io.coil-kt:coil:2.6.0'`）。
- **日期上下文**：截至 2025 年 3 月 3 日，本指南假設您正在處理需要 UIL 1.9.3 的舊代碼。

如果您需要幫助處理特定用例，請告訴我！