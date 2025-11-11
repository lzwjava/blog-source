---
audio: false
generated: true
lang: hant
layout: post
title: 使用 ButterKnife 進行視圖綁定
translated: true
type: note
---

Butter Knife 是一個廣受歡迎的 Android 視圖綁定函式庫，能簡化將 UI 元件綁定至程式碼欄位的流程。但請注意，Butter Knife 現已過時，現代 Android 開發建議改用 Android Jetpack 引入的 View Binding。若您仍需在 Android 專案中使用 2015 年左右發布的舊版 Butter Knife 6.1.0（透過 `.jar` 檔案），以下是在 Android Studio 中操作的步驟（截至 2025 年 3 月 3 日）。

### 前置準備
- 已安裝 Android Studio（任何近期版本皆可，但操作可能因版本略有差異）
- 已建立基礎 Android 專案
- 已下載 `butterknife-6.1.0.jar` 檔案（可透過 Maven Central 等儲存庫或本地歸檔來源取得）

### 在 Android 開發中使用 `butterknife-6.1.0.jar` 的步驟

#### 步驟 1：將 `.jar` 檔案加入專案
1. **定位 `libs` 資料夾**：
   - 在 Android Studio 專案中進入 `app` 模組
   - 於 `app` 資料夾內尋找或建立名為 `libs` 的資料夾（若不存在，請右鍵點選 `app` 資料夾選擇「新增＞目錄」並命名為 `libs`）

2. **複製 `.jar` 檔案**：
   - 將 `butterknife-6.1.0.jar` 複製到 `libs` 資料夾（可透過拖放檔案至 Android Studio 的 `libs` 資料夾，或透過檔案總管手動放置）

3. **同步 Gradle 設定**：
   - 開啟 `app` 模組的 `build.gradle` 檔案（位於 `app/build.gradle`）
   - 在 `dependencies` 區塊加入以下設定以引入 `libs` 資料夾內所有 `.jar` 檔案：
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - 點選 Android Studio 的「Sync Project with Gradle Files」按鈕同步專案

#### 步驟 2：設定專案配置
由於 Butter Knife 6.1.0 採用註解處理機制，此特定版本不需額外添加註解處理器依賴（與 8.x 等後續版本不同）。該 `.jar` 檔案已包含執行期函式庫，且 Butter Knife 6.1.0 主要依賴執行期反射機制而非編譯時代碼生成。

請確認專案已設定支援 Java 註解：
- 在 `app/build.gradle` 中確保 Java 版本相容（Butter Knife 6.1.0 支援 Java 6+）：
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### 步驟 3：在程式碼中使用 Butter Knife
1. **添加 Butter Knife 註解**：
   - 在 Activity 或 Fragment 中導入 Butter Knife 並使用 `@InjectView` 註解（6.1.0 版本專用註解）。範例：
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
             ButterKnife.inject(this); // 綁定視圖元件

             // 使用範例
             myButton.setOnClickListener(v -> myText.setText("按鈕已點擊！"));
         }
     }
     ```

2. **XML 版面配置**：
   - 確保版面配置檔案（如 `res/layout/activity_main.xml`）包含對應 ID 的視圖元件：
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
             android:text="點擊我" />
     </LinearLayout>
     ```

3. **綁定視圖元件**：
   - 在 `onCreate` 中呼叫 `ButterKnife.inject(this)` 可將註解欄位與版面配置中的視圖綁定（請注意 6.1.0 版本使用 `inject` 而非後續版本的 `bind` 方法）

#### 步驟 4：執行專案
- 建置並執行專案。若所有設定正確，Butter Knife 將成功綁定視圖，您會看到 UI 正常運作

### 重要注意事項
- **版本限制**：Butter Knife 6.1.0 版本較舊（2015 年發布），缺乏後續版本引入的功能（如透過註解處理器實現編譯時代碼生成、改用 `@BindView` 註解等）。此版本使用執行期反射機制，效能可能略遜於現代替代方案
- **過時狀態**：Butter Knife 已停止維護（約 2020 年終止開發），官方建議新專案改用 View Binding 或 Jetpack Compose
- **替代設定**：若使用較新版本（如 10.2.3），需添加註解處理器依賴（例如 `annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`），但 6.1.0 版本使用 `.jar` 檔案時不需此設定
- **疑難排解**：
  - 若出現「無法解析符號」錯誤，請確認 `.jar` 檔案已正確加入 `libs` 資料夾且 Gradle 依賴設定完整
  - 若應用程式崩潰並顯示 `NoClassDefFoundError`，請檢查 `.jar` 檔案是否位於 `libs` 資料夾且專案已完成同步

### 建議
雖然本指南說明如何使用 `butterknife-6.1.0.jar`，仍建議移轉至 View Binding 以獲得現代化且持續支援的開發體驗。以下為簡要比較：
- **Butter Knife 6.1.0**：使用 `@InjectView`、執行期反射、手動整合 `.jar` 檔案
- **View Binding**：內建於 Android 系統、無需外部依賴、編譯時生成綁定類別、具空值安全性

需要轉用 View Binding 的指引嗎？