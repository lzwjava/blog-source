---
audio: false
generated: true
lang: hant
layout: post
title: Android 通用圖像加載器
translated: true
type: note
---

Universal Image Loader (UIL) 版本 1.9.3 是一個專為 Android 應用程式設計的強大且靈活的圖片載入、快取及顯示函式庫。以下是逐步使用指南，請注意此函式庫較為老舊且已停止維護（最後更新約在 2015 年），若為現代專案建議考慮改用 Glide 或 Picasso 等替代方案。但若您確需使用 UIL 1.9.3，請參照以下操作步驟：

---

### 步驟 1：將函式庫加入專案
由於 UIL 1.9.3 可透過 Maven 取得，您可使用 Gradle 將其加入專案。若使用舊版開發環境（如 Eclipse），可手動下載 JAR 檔。

#### 使用 Gradle (Android Studio)：
1. 開啟應用模組的 `build.gradle` 檔案（Module: app）
2. 在 `dependencies` 區塊加入以下依賴項：
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. 點擊 Android Studio 的「Sync Now」同步 Gradle 專案

#### 手動 JAR 設定（如 Eclipse）：
1. 從 Maven Repository 或 GitHub 下載 `universal-image-loader-1.9.3.jar`
2. 將 JAR 檔置於專案的 `libs` 資料夾
3. 在 IDE 中對 JAR 檔右鍵選擇「Add to Build Path」（Eclipse）或手動設定專案路徑

---

### 步驟 2：添加權限設定
若要從網路載入圖片或儲存至裝置儲存空間，請在 `AndroidManifest.xml` 中加入以下權限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`：用於從 URL 下載圖片
- `WRITE_EXTERNAL_STORAGE`：用於磁碟快取（非必需但建議用於離線存取）。針對 Android 6.0+ (API 23+) 需額外執行運行時權限請求

---

### 步驟 3：初始化 ImageLoader
使用 UIL 前必須透過配置進行初始化，建議在 `Application` 類別或主 `Activity` 中執行一次

#### 建立自訂 Application 類別（推薦）：
1. 建立新類別（例如 `MyApplication.java`）：
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // 建立全域配置並初始化 ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // 設定圖片載入執行緒較低優先度
               .denyCacheImageMultipleSizesInMemory()    // 防止快取多尺寸圖片
               .diskCacheSize(50 * 1024 * 1024)          // 設定 50 MB 磁碟快取空間
               .diskCacheFileCount(100)                  // 設定快取檔案上限為 100
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. 在 `AndroidManifest.xml` 中註冊此類別：
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### 或在 Activity 中初始化：
若不想建立 `Application` 類別，可在 `Activity` 的 `onCreate()` 方法中初始化（需確保僅初始化一次）：
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

### 步驟 4：載入並顯示圖片
初始化完成後，即可使用 `ImageLoader` 將圖片載入至 `ImageView`

#### 基礎用法：
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // 將圖片載入至 ImageView
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### 進階用法（使用顯示選項）：
可透過 `DisplayImageOptions` 自訂圖片載入與顯示方式：
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
            .showImageOnLoading(R.drawable.placeholder) // 設定載入時顯示的佔位圖
            .showImageForEmptyUri(R.drawable.error)     // 設定空 URL 時顯示的錯誤圖
            .showImageOnFail(R.drawable.error)          // 設定載入失敗時顯示的錯誤圖
            .cacheInMemory(true)                        // 啟用記憶體快取
            .cacheOnDisk(true)                          // 啟用磁碟快取
            .build();

        // 使用選項載入圖片
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### 步驟 5：在 ListView 或 GridView 中使用 UIL
針對清單或網格佈局，請在適配器中使用 UIL 實現高效圖片載入

#### 自訂適配器範例：
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
    private String[] imageUrls; // 圖片 URL 陣列

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

#### 設定適配器：
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### UIL 1.9.3 主要功能特色
- **支援的 URI 類型**：
  - 網路資源：`"http://example.com/image.jpg"`
  - SD 卡檔案：`"file:///mnt/sdcard/image.png"`
  - 內容提供器：`"content://media/external/images/media/13"`
  - Assets 資源：`"assets://image.png"`
  - Drawable 資源：`"drawable://" + R.drawable.image`
- **快取機制**：支援記憶體與磁碟雙重快取
- **自訂配置**：可透過配置調整執行緒池大小、快取空間及圖片解碼選項

---

### 疑難排解
- **錯誤：「ImageLoader must be init with configuration」**  
  請確認在呼叫 `displayImage` 前已執行 `ImageLoader.getInstance().init(config)`
- **圖片無法載入**  
  - 檢查網路權限與 URL 有效性
  - 在配置中啟用日誌功能（`.writeDebugLogs()`）進行除錯
- **記憶體不足錯誤**  
  - 在配置中調降 `diskCacheSize` 或 `memoryCacheSize` 數值
  - 使用較小尺寸圖片或在 `DisplayImageOptions` 啟用縮放功能

---

### 注意事項
- **過時提醒**：UIL 1.9.3 已屬過時版本（最後更新約 2014 年）。現代 Android 開發建議改用 Glide（`implementation 'com.github.bumptech.glide:glide:4.16.0'`）或 Coil（`implementation 'io.coil-kt:coil:2.6.0'`）
- **時間背景**：截至 2025 年 3 月 3 日，本指南主要針對需使用 UIL 1.9.3 的遺留程式碼專案

如有特定使用情境需要協助，歡迎隨時提出！