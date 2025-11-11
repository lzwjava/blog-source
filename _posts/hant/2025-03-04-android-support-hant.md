---
audio: false
generated: true
lang: hant
layout: post
title: Android 支援程式庫
translated: true
type: note
---

Android Support Library 版本 `support-v4:19.1.0` 是 Android 支援函式庫（特別是 v4 相容函式庫）的舊版本，它為執行低於其發布時（約 2014 年）最新 API 級別的 Android 裝置提供向後相容的 API。此函式庫讓您能在舊版裝置上使用新版 Android 引入的功能，例如 Fragments、Loaders 及其他工具。

由於 `support-v4:19.1.0` 屬於舊版 Android Support Library，現已被 AndroidX 函式庫取代。但若您需使用此特定版本（例如維護舊專案），以下是設定並在 Android 專案中使用的方法：

---

### 步驟 1：添加依賴項
要使用 `support-v4:19.1.0`，您需將其添加為專案的依賴項，通常是在 `build.gradle` 檔案（模組：app）中進行設定。

#### 適用於基於 Gradle 的專案
1. 開啟您的 `app/build.gradle` 檔案。
2. 在 `dependencies` 區塊添加以下行：

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. 在 Android Studio 中點擊「Sync Now」以同步 Gradle 專案。

#### 注意事項：
- 請確保您的 `compileSdkVersion` 設定為至少 19（Android 4.4 KitKat）或更高，因為此函式庫與 API 19 功能對齊。
- `support-v4:19.1.0` 支援的最低 SDK 版本為 API 4（Android 1.6），但您應根據應用程式需求設定 `minSdkVersion`。

範例 `build.gradle`：
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // 請根據需要調整
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### 步驟 2：驗證可用性
Android Support Libraries 存放於 Google 的 Maven 儲存庫。自 Android Studio 3.0+ 起，此儲存庫已預設包含。若您使用舊版 Android Studio，請確保您的 `build.gradle`（專案層級）中包含以下內容：

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // 注意：JCenter 已棄用，但過去用於舊版函式庫
    }
}
```

若下載函式庫時遇到問題，您可能需要透過 SDK Manager 安裝 Android Support Repository：
1. 前往 `Tools > SDK Manager`。
2. 在「SDK Tools」標籤下，勾選「Android Support Repository」並安裝。

---

### 步驟 3：在程式碼中使用函式庫
`support-v4` 函式庫提供多種類別，例如 `Fragment`、`Loader`、`AsyncTaskLoader` 及實用工具如 `ActivityCompat`。以下是使用部分常見元件的範例：

#### 範例 1：使用 Fragments
`support-v4` 函式庫包含可在舊版 Android 上運作的向後移植 `Fragment` 類別。

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

在 Activity 中使用此 fragment：
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
`ActivityCompat` 類別提供向後相容功能的輔助方法，例如請求權限（在 API 23 引入，但可透過支援函式庫在更早版本使用）。

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

### 步驟 4：注意事項
- **已棄用函式庫**：Android Support Library（包括 `support-v4:19.1.0`）已棄用。現代開發請遷移至 AndroidX（例如 `androidx.legacy:legacy-support-v4:1.0.0`）。AndroidX 是後繼版本，提供持續更新與支援。
- **版本匹配**：若使用其他支援函式庫（例如 `appcompat-v7`），請確保它們版本一致（19.1.0）以避免版本不符錯誤。
- **最低 SDK**：雖然 `support-v4:19.1.0` 支援 API 4+，但部分功能可能需要更高的 `minSdkVersion`（例如後續引入的某些元件需 API 14）。

---

### 步驟 5：遷移至 AndroidX（可選但建議）
若您正在維護舊專案，請考慮遷移至 AndroidX：
1. 在 Android Studio 中，前往 `Refactor > Migrate to AndroidX`。
2. 更新您的依賴項，例如將 `com.android.support:support-v4:19.1.0` 替換為 `androidx.legacy:legacy-support-v4:1.0.0`。
3. 遵循 Android Studio 提供的遷移指南。

---

### 疑難排解
- **「找不到函式庫」**：請確保網路連線正常且可存取 Google Maven 儲存庫。
- **版本不符**：若出現支援函式庫版本不符錯誤，請將所有 `com.android.support` 依賴項對齊至 19.1.0。
- **過時功能**：`support-v4:19.1.0` 中的部分 API（例如 `AsyncTask`）已過時。請查閱文件以尋找替代方案。

若您需要特定使用案例或設定的協助，請告知！