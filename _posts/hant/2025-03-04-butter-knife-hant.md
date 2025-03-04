---
audio: false
generated: true
lang: en
layout: post
title: 'ButterKnife: a View binding Library'
translated: false
---

Butter Knife 是一個流行的 Android 視圖綁定庫，簡化了將 UI 元素綁定到代碼中的字段的過程。然而，請注意，Butter Knife 現在已經被廢棄，現代 Android 開發建議使用 View Binding（引入於 Android Jetpack）來代替。不過，如果你需要在 Android 專案中使用 Butter Knife 6.1.0（一個於 2015 年發布的舊版本）和一個 `.jar` 文件，以下是你在 Android Studio 中於 2025 年 3 月 3 日的操作方法。

### 前提條件
- 安裝 Android Studio（任何較新的版本應該都可以，雖然過程可能會根據你的版本有所不同）。
- 設定一個基本的 Android 專案。
- 下載 `butterknife-6.1.0.jar` 文件。你通常可以在像 Maven Central 這樣的存儲庫中找到舊版本，或者如果你有本地的 `.jar` 文件，可以通過封存來源。

### 使用 `butterknife-6.1.0.jar` 進行 Android 開發的步驟

#### 第 1 步：將 `.jar` 文件添加到你的專案
1. **定位 `libs` 資料夾**：
   - 在你的 Android Studio 專案中，導航到 `app` 模組。
   - 在 `app` 資料夾中，找到或創建一個名為 `libs` 的資料夾。如果它不存在，右鍵點擊 `app` 資料夾，選擇 `New > Directory`，並將其命名為 `libs`。

2. **複製 `.jar` 文件**：
   - 將 `butterknife-6.1.0.jar` 文件複製到 `libs` 資料夾。你可以通過將文件拖放到 Android Studio 中的 `libs` 資料夾，或者通過文件資源管理器手動將其放置在該處。

3. **同步 `.jar` 文件與 Gradle**：
   - 打開 `app` 模組的 `build.gradle` 文件（位於 `app/build.gradle`）。
   - 在 `dependencies` 塊中添加以下行以包含 `libs` 資料夾中的所有 `.jar` 文件：
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - 通過點擊 Android Studio 中的「同步專案與 Gradle 文件」按鈕來同步你的專案。

#### 第 2 步：配置你的專案
由於 Butter Knife 6.1.0 使用註解處理，你不需要為這個特定版本添加註解處理器依賴（與 8.x 及以上的版本不同）。`.jar` 文件包含運行時庫，而 Butter Knife 6.1.0 依賴於運行時反射來實現大部分功能，而不是編譯時代碼生成。

然而，請確保你的專案已設置以支持 Java 注釋：
- 在你的 `app/build.gradle` 中，確保 Java 版本兼容（Butter Knife 6.1.0 可與 Java 6+ 兼容）：
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### 第 3 步：在你的代碼中使用 Butter Knife
1. **添加 Butter Knife 注釋**：
   - 在你的 Activity 或 Fragment 中，導入 Butter Knife 並使用 `@InjectView`（在 6.1.0 版本中使用的註解）來註釋你的視圖。例如：
     ```java
     import android.os.Bundle;
     import android.widget.Button;
     import android.widget.TextView;
     import butterknife.InjectView;
     import butterknife.ButterKnife;
     import androidx.appcompat.app.AppCompatActivity;

     public class MainActivity extends AppCompatActivity {

         @InjectView(R.id.my_button)
         Button myButton;

         @InjectView(R.id.my_text)
         TextView myText;

         @Override
         protected void onCreate(Bundle savedInstanceState) {
             super.onCreate(savedInstanceState);
             setContentView(R.layout.activity_main);
             ButterKnife.inject(this); // 綁定視圖

             // 示例使用
             myButton.setOnClickListener(v -> myText.setText("Button clicked!"));
         }
     }
     ```

2. **XML 布局**：
   - 確保你的布局文件（例如 `res/layout/activity_main.xml`）包含具有相應 ID 的視圖：
     ```xml
     <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         android:orientation="vertical">

         <TextView
             android:id="@+id/my_text"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Hello World" />

         <Button
             android:id="@+id/my_button"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Click Me" />
     </LinearLayout>
     ```

3. **綁定視圖**：
   - 在 `onCreate` 中的 `ButterKnife.inject(this)` 請求將註釋字段綁定到布局中的視圖。請注意，在 6.1.0 版本中，使用 `inject` 而不是 `bind`（後者在 7.x 和 8.x 版本中引入）。

#### 第 4 步：運行你的專案
- 編譯並運行你的專案。如果一切正常設置，Butter Knife 將綁定你的視圖，你應該會看到 UI 正常運行。

### 重要說明
- **版本限制**：Butter Knife 6.1.0 非常舊（於 2015 年發布），缺少後來版本中引入的功能，例如編譯時代碼生成（通過註解處理器）和對 `@BindView` 而不是 `@InjectView` 的支持。它在運行時使用反射，這可能會比現代替代方案稍微影響性能。
- **廢棄狀態**：Butter Knife 現在不再維護（開發於 2020 年左右停止），官方建議使用 View Binding 或 Jetpack Compose 來進行新專案。
- **替代設置**：如果你使用的是較新的版本（例如 10.2.3），你需要添加註解處理器依賴（例如 `annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`），但對於 6.1.0 使用 `.jar` 文件，這不是必需的。
- **故障排除**：
  - 如果你收到 Butter Knife 類別的「無法解析符號」錯誤，請確保 `.jar` 文件已正確添加到 `libs` 資料夾並包含在 Gradle 依賴中。
  - 如果應用程式因 `NoClassDefFoundError` 而崩潰，請雙重檢查 `.jar` 文件是否在 `libs` 資料夾中，並確保專案已同步。

### 建議
雖然這個指南展示了如何使用 `butterknife-6.1.0.jar`，但考慮轉換到 View Binding 以獲得更現代、受支持的方法。以下是快速比較：
- **Butter Knife 6.1.0**：使用 `@InjectView`，運行時反射，手動 `.jar` 綁定。
- **View Binding**：內建於 Android，無外部依賴，在編譯時生成綁定類別，並且是空安全的。

你想要有關轉換到 View Binding 的指導嗎？