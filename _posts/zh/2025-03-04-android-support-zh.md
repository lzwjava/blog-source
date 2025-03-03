---
audio: false
generated: true
lang: zh
layout: post
title: Android 支持库
translated: true
---

Android 支持库版本 `support-v4:19.1.0` 是 Android 支持库（特别是 v4 兼容库）的较旧版本，它为运行 API 级别低于其发布时（约 2014 年）最新版本的 Android 设备提供向后兼容的 API。该库允许您在较旧设备上使用在较新 Android 版本中引入的功能，例如 Fragments、Loaders 和其他实用程序。

由于 `support-v4:19.1.0` 是遗留的 Android 支持库的一部分，它已经被 AndroidX 库取代。然而，如果您需要使用此特定版本（例如，用于维护旧项目），以下是如何在 Android 项目中设置和使用它的方法：

---

### 第一步：添加依赖
要使用 `support-v4:19.1.0`，您需要在项目中将其包含为依赖项。这通常在您的 `build.gradle` 文件（模块：app）中完成。

#### 对于基于 Gradle 的项目
1. 打开您的 `app/build.gradle` 文件。
2. 将以下行添加到 `dependencies` 块中：

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. 通过点击 Android Studio 中的“立即同步”来同步您的项目与 Gradle。

#### 注意事项：
- 确保您的 `compileSdkVersion` 设置为至少 19（Android 4.4 KitKat）或更高，因为该库与 API 19 功能对齐。
- `support-v4:19.1.0` 支持的最低 SDK 版本是 API 4（Android 1.6），但您应根据应用程序的要求设置 `minSdkVersion`。

示例 `build.gradle`：
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // 根据需要调整
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### 第二步：验证可用性
Android 支持库托管在 Google 的 Maven 仓库中。从 Android Studio 3.0+ 开始，默认包含此仓库。如果您使用的是较旧版本的 Android Studio，请确保在项目级别的 `build.gradle` 中包含以下内容：

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // 注意：JCenter 已废弃，但用于较旧的库
    }
}
```

如果您在下载库时遇到问题，可能需要通过 SDK 管理器安装 Android 支持库：
1. 转到 `Tools > SDK Manager`。
2. 在“SDK 工具”选项卡下，选择“Android 支持库”并安装它。

---

### 第三步：在代码中使用库
`support-v4` 库提供了各种类，例如 `Fragment`、`Loader`、`AsyncTaskLoader` 和实用程序 `ActivityCompat`。以下是如何使用一些常见组件的示例：

#### 示例 1：使用 Fragments
`support-v4` 库包括一个回溯的 `Fragment` 类，可以在较旧的 Android 版本上工作。

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

在活动中使用此片段：
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

#### 示例 2：使用 ActivityCompat
`ActivityCompat` 类为向后兼容的功能提供辅助方法，例如请求权限（在 API 23 中引入，但可以使用支持库在较早版本中使用）。

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

### 第四步：考虑事项
- **已废弃的库**：Android 支持库，包括 `support-v4:19.1.0`，已废弃。对于现代开发，请迁移到 AndroidX（例如，`androidx.legacy:legacy-support-v4:1.0.0`）。AndroidX 是继任者，并提供持续更新和支持。
- **版本匹配**：如果您使用其他支持库（例如 `appcompat-v7`），请确保它们是相同的版本（19.1.0），以避免版本不匹配错误。
- **最低 SDK**：虽然 `support-v4:19.1.0` 支持 API 4+，但某些功能可能需要更高的 `minSdkVersion`（例如，API 14 及更高版本的某些组件）。

---

### 第五步：迁移到 AndroidX（可选但推荐）
如果您正在维护旧项目，请考虑迁移到 AndroidX：
1. 在 Android Studio 中，转到 `Refactor > Migrate to AndroidX`。
2. 更新您的依赖项，例如，将 `com.android.support:support-v4:19.1.0` 替换为 `androidx.legacy:legacy-support-v4:1.0.0`。
3. 按照 Android Studio 提供的迁移指南进行操作。

---

### 故障排除
- **“找不到库”**：确保您的互联网连接处于活动状态，并且 Google Maven 仓库可访问。
- **版本不匹配**：如果您看到有关不匹配支持库版本的错误，请将所有 `com.android.support` 依赖项对齐到 19.1.0。
- **过时功能**：`support-v4:19.1.0` 中的一些 API（例如 `AsyncTask`）已过时。请查看文档，了解替代方案。

如果您需要帮助处理特定用例或设置，请告诉我！