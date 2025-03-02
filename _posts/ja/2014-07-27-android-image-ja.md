---
audio: false
generated: false
lang: ja
layout: post
title: Android 画像処理を簡単に
translated: true
---

Androidで画像を扱うことは難しいことがあります—ビットマップはメモリを消費し、回転は向きを混乱させ、トリミングには精度が求められます。そこで、`BitmapUtils`や`Crop`のようなユーティリティクラスが役立ちます。この記事では、`com.lzw.flower.utils`パッケージからの強力なクラスのペアについて詳しく説明します。コードを探り、各メソッドが何をするかを分解し、プロジェクトでどのように使用するかを示します。始めましょう！

---

#### BitmapUtils: 画像操作の便利ツールキット

`BitmapUtils`クラスは、`Bitmap`オブジェクトを操作するための静的メソッドのコレクションです。以下に全コードとその説明を示します：

```java
package com.lzw.flower.utils;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;
import android.net.Uri;
import android.provider.MediaStore;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class BitmapUtils {
  public static Bitmap convertGreyImg(Bitmap img) {
    int width = img.getWidth();
    int height = img.getHeight();
    int[] pixels = new int[width * height];
    img.getPixels(pixels, 0, width, 0, 0, width, height);
    int alpha = 0xFF << 24;
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        int grey = pixels[width * i + j];
        int red = ((grey & 0x00FF0000) >> 16);
        int green = ((grey & 0x0000FF00) >> 8);
        int blue = (grey & 0x000000FF);
        grey = (int) ((float) red * 0.3 + (float) green * 0.59 + (float) blue * 0.11);
        grey = alpha | (grey << 16) | (grey << 8) | grey;
        pixels[width * i + j] = grey;
      }
    }
    Bitmap result = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888);
    result.setPixels(pixels, 0, width, 0, 0, width, height);
    return result;
  }

  public static Bitmap toGreyImg(Bitmap bitmapOrg) {
    Bitmap bitmapNew = bitmapOrg.copy(Bitmap.Config.ARGB_8888, true);
    if (bitmapNew == null) {
      return null;
    }
    for (int i = 0; i < bitmapNew.getWidth(); i++) {
      for (int j = 0; j < bitmapNew.getHeight(); j++) {
        int col = bitmapNew.getPixel(i, j);
        int alpha = col & 0xFF000000;
        int red = (col & 0x00FF0000) >> 16;
        int green = (col & 0x0000FF00) >> 8;
        int blue = (col & 0x000000FF);
        int gray = (int) ((float) red * 0.3 + (float) green * 0.59 + (float) blue * 0.11);
        int newColor = alpha | (gray << 16) | (gray << 8) | gray;
        bitmapNew.setPixel(i, j, newColor);
      }
    }
    return bitmapNew;
  }

  public static void saveBitmapToPath(Bitmap bitmap, String imagePath) {
    FileOutputStream out = null;
    File file = new File(imagePath);
    if (file.getParentFile().exists() == false) {
      file.getParentFile().mkdirs();
    }
    try {
      out = new FileOutputStream(imagePath);
      bitmap.compress(Bitmap.CompressFormat.PNG, 100, out);
      out.flush();
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        if (out != null) out.close();
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
  }

  public static Bitmap rotateBitmap(Bitmap source, float angle) {
    Matrix matrix = new Matrix();
    matrix.postRotate(angle);
    return Bitmap.createBitmap(source, 0, 0, source.getWidth(), source.getHeight(), matrix, true);
  }

  public static Uri getResourceUri(int resId) {
    return Uri.parse("android.resource://com.lzw.flower/" + resId);
  }

  public static Bitmap getBitmapByUri(Context cxt, Uri uri) throws IOException {
    return MediaStore.Images.Media.getBitmap(cxt.getContentResolver(), uri);
  }

  public static int calInSampleSize(BitmapFactory.Options options, int reqWidth) {
    int w = options.outWidth;
    int h = options.outHeight;
    int inSampleSize = 1;
    if (w > reqWidth && reqWidth > 0) {
      inSampleSize = Math.round(w / reqWidth);
    }
    return inSampleSize;
  }

  public static Bitmap decodeSampledBitmapFromPath(String path, int reqWidth) {
    BitmapFactory.Options options = new BitmapFactory.Options();
    options.inJustDecodeBounds = true;
    BitmapFactory.decodeFile(path, options);
    int inSampleSize = calInSampleSize(options, reqWidth);
    options.inJustDecodeBounds = false;
    options.inSampleSize = inSampleSize;
    return BitmapFactory.decodeFile(path, options);
  }

  public static Bitmap decodeFileByHeight(String path, int reqH) {
    BitmapFactory.Options opt = new BitmapFactory.Options();
    opt.inJustDecodeBounds = true;
    BitmapFactory.decodeFile(path, opt);
    int scale = calInSampleSizeByHeight(opt, reqH);
    opt.inSampleSize = scale;
    opt.inJustDecodeBounds = false;
    Bitmap bm = BitmapFactory.decodeFile(path, opt);
    return bm;
  }

  public static int calInSampleSizeByHeight(BitmapFactory.Options options, int reqHeight) {
    int h = options.outHeight;
    int inSampleSize = 1;
    if (h > reqHeight) {
      inSampleSize = Math.round(h * 1.0f / reqHeight);
    }
    return inSampleSize;
  }
}
```

##### 中身
- **グレースケール変換**:
  - `convertGreyImg`: ピクセル配列を使用してビットマップを一括でグレースケールに変換します。
  - `toGreyImg`: 可変コピーをピクセルごとに処理する別のアプローチを提供します。
  両方とも、自然なグレースケールを得るために明度の公式（`0.3R + 0.59G + 0.11B`）を使用しています。

- **ファイル操作**:
  - `saveBitmapToPath`: ビットマップをPNGとして保存し、必要に応じてディレクトリを作成します。

- **変換**:
  - `rotateBitmap`: `Matrix`を使用して画像を回転します—シンプルですが効果的です。

- **読み込みとサンプリング**:
  - `getBitmapByUri`と`getResourceUri`: URIまたはリソースから画像を読み込みます。
  - `decodeSampledBitmapFromPath`と`decodeFileByHeight`: 幅または高さで大きな画像を効率的にスケーリングし、メモリ問題を避けます。

---

#### Crop: Androidのネイティブツールを使用した精密なトリミング

`Crop`クラスは、Androidの組み込みトリミングインテントを活用します。以下にコードを示します：

```java
package com.lzw.flower.utils;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.provider.MediaStore;
import com.lzw.flower.base.App;

import java.io.File;

public class Crop {
  public static void startPhotoCrop(Activity cxt, Uri uri, String outputPath, int resultCode) {
    Intent intent = new Intent("com.android.camera.action.CROP");
    intent.setDataAndType(uri, "image/*");
    int w = App.drawWidth;
    int h = App.drawHeight;
    int factor = gcd(w, h);
    int w1 = w / factor;
    int h1 = h / factor;
    intent.putExtra("crop", "true")
        .putExtra("aspectX", w1)
        .putExtra("aspectY", h1)
        .putExtra("scale", true)
        .putExtra("outputX", w)
        .putExtra("outputY", h)
        .putExtra("outputFormat", Bitmap.CompressFormat.PNG.toString());
    intent.putExtra("noFaceDetection", true);
    intent.putExtra("return-data", false);
    Uri uri1 = Uri.fromFile(new File(outputPath));
    intent.putExtra(MediaStore.EXTRA_OUTPUT, uri1);
    cxt.startActivityForResult(intent, resultCode);
  }

  static int gcd(int a, int b) {
    if (b == 0) {
      return a;
    } else {
      return gcd(b, a % b);
    }
  }
}
```

##### ここで何が起こっているか
- `startPhotoCrop`: 指定された`Uri`、アスペクト比（GCDを使用して簡略化）、出力パスでシステムのトリミングアクティビティを起動します。`App.drawWidth`と`App.drawHeight`が他の場所で定義されていることを前提としています（例：ベース`App`クラス）。
- `gcd`: 最大公約数を計算する再帰メソッドで、アスペクト比が最も簡単な形式であることを確認します。

---

#### 全体をまとめる: 使用例

これらのユーティリティをAndroidアプリでどのように使用するかを示します：

```java
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import com.lzw.flower.utils.BitmapUtils;
import com.lzw.flower.utils.Crop;

public class MainActivity extends AppCompatActivity {
    private static final int REQUEST_CROP = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 画像をグレースケールに変換して保存
        Bitmap original = BitmapFactory.decodeResource(getResources(), R.drawable.sample);
        Bitmap grey = BitmapUtils.convertGreyImg(original);
        BitmapUtils.saveBitmapToPath(grey, "/sdcard/DCIM/grey_image.png");

        // 画像を効率的に読み込みスケーリング
        Bitmap scaled = BitmapUtils.decodeSampledBitmapFromPath("/sdcard/DCIM/photo.jpg", 200);

        // トリミングを起動
        Uri imageUri = Uri.fromFile(new File("/sdcard/DCIM/photo.jpg"));
        Crop.startPhotoCrop(this, imageUri, "/sdcard/DCIM/cropped.png", REQUEST_CROP);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CROP && resultCode == RESULT_OK) {
            // トリミングされた画像は"/sdcard/DCIM/cropped.png"に保存されます
        }
    }
}
```

**注意**:
- `AndroidManifest.xml`とランタイムチェックで適切なストレージ権限を確認してください。
- `Crop`で参照されている`App`クラスは、`drawWidth`と`drawHeight`を定義する必要があります。

---

#### これらのユーティリティが素晴らしい理由

1. **効率性**: サンプリングメソッドは、大きな画像を扱う際に`OutOfMemoryError`を防ぎます。
2. **柔軟性**: グレースケール、回転、トリミングは多くの使用ケースをカバーします。
3. **シンプルさ**: 静的メソッドは統合を簡単にします—インスタンス化が不要です。

---

#### 最後に

`BitmapUtils`と`Crop`クラスは、画像操作が必要なすべてのAndroidアプリの素晴らしい出発点です。写真編集アプリを構築するか、ギャラリーのサムネイルを最適化するか、ユーザーがトリミングできる機能を追加するか、このコードはあなたをサポートします。試してみて、必要に応じてカスタマイズし、どのように動作するか教えてください！

Androidでどのような画像処理の課題に直面しましたか？ 感想を下に共有してください！