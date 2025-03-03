---
audio: false
generated: true
lang: hant
layout: post
title: Android 支援庫
translated: true
---

Android 支援庫版本 `support-v4:19.1.0` 是 Android 支援庫（特別是 v4 相容庫）的較舊版本，提供向後相容的 API 給在其發行時（約 2014 年）運行較舊 API 級別的 Android 設備。這個庫讓你可以在較舊的設備上使用在較新 Android 版本中引入的功能，例如 Fragments、Loaders 和其他工具。

由於 `support-v4:19.1.0` 是舊版 Android 支援庫的一部分，已被 AndroidX 圖書館取代。然而，如果你需要使用這個特定版本（例如，維護一個較舊的項目），以下是如何在你的 Android 項目中設置和使用它的方法：

---

### 第 1 步：添加依賴
要使用 `support-v4:19.1.0`，你需要在項目中將其作為依賴項添加。這通常在你的 `build.gradle` 文件中進行（模組：app）。

#### 針對 Gradle 專案
1. 打開你的 `app/build.gradle` 文件。
2. 在 `dependencies` 塊中添加以下行：

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. 通過點擊 Android Studio 中的「立即同步」來同步你的項目與 Gradle。

#### 注意事項：
- 確保你的 `compileSdkVersion` 設定為至少 19（Android 4.4 KitKat）或更高，因為這個庫與 API 19 功能相對應。
- `support-v4:19.1.0` 支援的最低 SDK 版本是 API 4（Android 1.6），但你應根據你的應用程序需求設置 `minSdkVersion`。

範例 `build.gradle`：
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // 根據需要調整
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### 第 2 步：驗證可用性
Android 支援庫存儲在 Google 的 Maven 存儲庫中。從 Android Studio 3.0+ 開始，這個存儲庫預設包含。如果你使用的是較舊版本的 Android Studio，確保你的 `build.gradle`（項目級別）中有以下內容：

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // 注意：JCenter 已過時，但用於較舊的庫
    }
}
```

如果你在下載庫時遇到問題，你可能需要通過 SDK 管理器安裝 Android 支援存儲庫：
1. 進入 `工具 > SDK 管理器`。
2. 在「SDK 工具」標籤下，勾選「Android 支援存儲庫」並安裝它。

---

### 第 3 步：在代碼中使用庫
`support-v4` 圖書館提供各種類，例如 `Fragment`、`Loader`、`AsyncTaskLoader` 和工具類 `ActivityCompat`。以下是如何使用一些常見組件的範例：

#### 範例 1：使用 Fragments
`support-v4` 圖書館包括一個回溯的 `Fragment` 類，可以在較舊的 Android 版本上運行。

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

在活動中使用這個片段：
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

#### 範例 2：使用 ActivityCompat
`ActivityCompat` 類提供向後相容功能的輔助方法，例如請求權限（在 API 23 中引入，但可以使用支援庫在較早的版本中使用）。

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

### 第 4 步：考量事項
- **已過時的庫**：Android 支援庫，包括 `support-v4:19.1.0`，已過時。對於現代開發，請遷移到 AndroidX（例如 `androidx.legacy:legacy-support-v4:1.0.0`）。AndroidX 是繼任者，並提供持續更新和支援。
- **版本匹配**：如果你使用其他支援庫（例如 `appcompat-v7`），請確保它們是相同版本（19.1.0），以避免版本不匹配錯誤。
- **最低 SDK**：雖然 `support-v4:19.1.0` 支援 API 4+，但某些功能可能需要較高的 `minSdkVersion`（例如，API 14 才能使用某些較晚引入的組件）。

---

### 第 5 步：遷移到 AndroidX（可選但建議）
如果你正在維護一個舊項目，考慮遷移到 AndroidX：
1. 在 Android Studio 中，進入 `重構 > 遷移到 AndroidX`。
2. 更新你的依賴項，例如，將 `com.android.support:support-v4:19.1.0` 替換為 `androidx.legacy:legacy-support-v4:1.0.0`。
3. 按照 Android Studio 提供的遷移指南進行操作。

---

### 疑難排解
- **找不到庫**：確保你的互聯網連接是活躍的，並且 Google Maven 存儲庫是可訪問的。
- **版本不匹配**：如果你看到關於不匹配支援庫版本的錯誤，請將所有 `com.android.support` 依賴項對齊到 19.1.0。
- **過時功能**：`support-v4:19.1.0` 中的一些 API（例如 `AsyncTask`）已過時。檢查文檔以獲取替代方案。

如果你需要幫助處理特定用例或設置，請告訴我！