---
audio: false
generated: true
lang: zh
layout: post
title: Android 通用图像加载器
translated: true
---

通用图像加载器（UIL）版本 1.9.3 是一个功能强大且灵活的库，用于在 Android 应用中加载、缓存和显示图像。以下是如何在您的 Android 项目中使用它的分步指南。请注意，这个库较旧且已停止维护（最后更新大约在 2015 年），因此对于现代项目，您可能需要考虑替代方案，如 Glide 或 Picasso。然而，如果您特别需要使用 UIL 1.9.3，以下是如何操作的：

---

### 第 1 步：将库添加到您的项目
由于 UIL 1.9.3 通过 Maven 提供，您可以使用 Gradle 将其添加到项目中。如果您使用的是较旧的设置（例如，Eclipse），可以手动下载 JAR 文件。

#### 使用 Gradle（Android Studio）：
1. 打开应用的 `build.gradle` 文件（模块：app）。
2. 在 `dependencies` 块中添加以下依赖项：
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. 通过点击 Android Studio 中的“立即同步”来同步项目与 Gradle。

#### 手动 JAR 设置（例如，Eclipse）：
1. 从 Maven 仓库或 GitHub 下载 `universal-image-loader-1.9.3.jar`。
2. 将 JAR 文件放置在项目的 `libs` 文件夹中。
3. 在 IDE 中右键点击 JAR，然后选择“添加到构建路径”（Eclipse）或在项目设置中手动配置。

---

### 第 2 步：添加权限
要从互联网加载图像或将其保存到存储中，请在 `AndroidManifest.xml` 中添加以下权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`：用于从 URL 下载图像。
- `WRITE_EXTERNAL_STORAGE`：用于磁盘缓存（可选，但建议用于离线使用）。对于 Android 6.0+（API 23+），您还需要在运行时请求此权限。

---

### 第 3 步：初始化 ImageLoader
在使用 UIL 之前，必须使用配置对其进行初始化。这通常在 `Application` 类或主 `Activity` 中完成一次。

#### 创建自定义 Application 类（推荐）：
1. 创建一个新类（例如，`MyApplication.java`）：
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // 创建全局配置并初始化 ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // 降低图像加载线程的优先级
               .denyCacheImageMultipleSizesInMemory()    // 防止缓存多个大小
               .diskCacheSize(50 * 1024 * 1024)          // 50 MB 磁盘缓存
               .diskCacheFileCount(100)                  // 缓存中最多 100 个文件
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. 在 `AndroidManifest.xml` 中注册此类：
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### 或者在 Activity 中初始化：
如果不想使用 `Application` 类，可以在 `Activity` 的 `onCreate()` 方法中初始化它（但请确保只初始化一次）：
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

### 第 4 步：加载和显示图像
初始化后，可以使用 `ImageLoader` 将图像加载到 `ImageView` 中。

#### 基本用法：
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // 将图像加载到 ImageView
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### 高级用法与显示选项：
可以使用 `DisplayImageOptions` 自定义图像的加载和显示方式：
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

        // 定义显示选项
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // 加载时显示的图像
            .showImageForEmptyUri(R.drawable.error)     // 如果 URL 为空时显示的图像
            .showImageOnFail(R.drawable.error)          // 加载失败时显示的图像
            .cacheInMemory(true)                        // 缓存到 RAM
            .cacheOnDisk(true)                          // 缓存到磁盘
            .build();

        // 使用选项加载图像
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### 第 5 步：在 ListView 或 GridView 中使用 UIL
对于列表或网格，请在适配器中使用 UIL 以高效加载图像。

#### 示例自定义适配器：
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
    private String[] imageUrls; // 图像 URL 数组

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

#### 设置适配器：
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### UIL 1.9.3 的关键功能
- **支持的 URI 类型**：
  - Web：`"http://example.com/image.jpg"`
  - SD 卡：`"file:///mnt/sdcard/image.png"`
  - 内容提供程序：`"content://media/external/images/media/13"`
  - 资产：`"assets://image.png"`
  - 绘图：`"drawable://" + R.drawable.image`
- **缓存**：支持内存和磁盘缓存。
- **自定义**：可以在配置中调整线程池大小、缓存大小和图像解码选项。

---

### 故障排除
- **崩溃："ImageLoader 必须使用配置初始化"**
  确保在任何 `displayImage` 调用之前调用 `ImageLoader.getInstance().init(config)`。
- **图像未加载**
  - 检查互联网权限和 URL 有效性。
  - 在配置中启用日志记录（`.writeDebugLogs()`）以调试问题。
- **内存不足错误**
  - 减少配置中的 `diskCacheSize` 或 `memoryCacheSize`。
  - 使用较小的图像或在 `DisplayImageOptions` 中启用缩放。

---

### 注意事项
- **废弃**：UIL 1.9.3 已过时（最后发布约 2014 年）。对于现代 Android 开发，请考虑使用 Glide（`implementation 'com.github.bumptech.glide:glide:4.16.0'`）或 Coil（`implementation 'io.coil-kt:coil:2.6.0'`）。
- **日期上下文**：截至 2025 年 3 月 3 日，本指南假设您正在处理需要 UIL 1.9.3 的遗留代码。

如果您需要帮助处理特定用例，请告诉我！