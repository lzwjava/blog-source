---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تطبيق معالجة الصور في أندرويد سهل
translated: true
type: post
---

التعامل مع الصور في أندرويد يمكن أن يكون معقدًا - حيث أن الصور المتجهة (bitmaps) تستهلك الذاكرة، وتسبب التحويلات (rotations) مشاكل في التوجه، وتطلب التقطيع (cropping) دقة. ذلك هو المكان الذي تأتي فيه فئات المساعدة مثل `BitmapUtils` و `Crop` مفيدة. في هذا المقال، سأكون أريكك زوجًا قويًا من الفئات من حزمة `com.lzw.flower.utils`. سنستعرض شيفرتها، ونحلل ما يفعله كل طريقة، ونعرض كيفية استخدامها في مشاريعك. دعونا نغوص!

---

#### BitmapUtils: أداة معالجة الصور الأساسية

فئة `BitmapUtils` هي مجموعة من الطرق الثابتة لتعديل كائنات `Bitmap`. إليك الشيفرة الكاملة، متبوعة بشرح:

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

##### ما يحتويه؟
- **التحويل إلى ألوان رمادية**:
  - `convertGreyImg`: يستخدم مصفوفة البكسل لتحويل الصورة إلى ألوان رمادية.
  - `toGreyImg`: يعمل على كل بكسل في نسخة قابلة للتعديل، يقدم طريقة بديلة.
  كلاهما يستخدم الصيغة اللونية (`0.3R + 0.59G + 0.11B`) للحصول على ألوان رمادية طبيعية.

- **عمليات الملفات**:
  - `saveBitmapToPath`: يحفظ الصورة ك PNG، ويخلق الدلائل حسب الحاجة.

- **التحويلات**:
  - `rotateBitmap`: يغير اتجاه الصورة باستخدام `Matrix` - بسيط ولكن فعال.

- **التحميل والتعيين**:
  - `getBitmapByUri` و `getResourceUri`: يحمّل الصور من URIs أو الموارد.
  - `decodeSampledBitmapFromPath` و `decodeFileByHeight`: يغير حجم الصور الكبيرة بشكل فعال حسب العرض أو الارتفاع، يجنب مشاكل الذاكرة.

---

#### Crop: تقطيع دقيق باستخدام أدوات أندرويد الأصلية

فئة `Crop` تستفيد من نية تقطيع أندرويد الأصلية. إليك الشيفرة:

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

##### ما يحدث هنا؟
- `startPhotoCrop`: يبدأ نشاط تقطيع النظام مع `Uri` محدد، نسبة العرض إلى الارتفاع (مبسط باستخدام GCD)، ومسار الإخراج. يفترض أن `App.drawWidth` و `App.drawHeight` تم تعريفهما في مكان آخر (مثل فئة `App` الأساسية).
- `gcd`: طريقة تكرارية لحساب أكبر عام مشترك، لضمان أن نسبة العرض إلى الارتفاع في شكلها البسيط.

---

#### جمع كل شيء: أمثلة الاستخدام

هكذا يمكنك استخدام هذه الأدوات في تطبيق أندرويد:

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

        // تحويل صورة إلى ألوان رمادية وحفظها
        Bitmap original = BitmapFactory.decodeResource(getResources(), R.drawable.sample);
        Bitmap grey = BitmapUtils.convertGreyImg(original);
        BitmapUtils.saveBitmapToPath(grey, "/sdcard/DCIM/grey_image.png");

        // تحميل وتغيير حجم صورة بشكل فعال
        Bitmap scaled = BitmapUtils.decodeSampledBitmapFromPath("/sdcard/DCIM/photo.jpg", 200);

        // بدء تقطيع
        Uri imageUri = Uri.fromFile(new File("/sdcard/DCIM/photo.jpg"));
        Crop.startPhotoCrop(this, imageUri, "/sdcard/DCIM/cropped.png", REQUEST_CROP);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CROP && resultCode == RESULT_OK) {
            // الصورة المقطوعة محفوظة في "/sdcard/DCIM/cropped.png"
        }
    }
}
```

**ملاحظات**:
- تأكد من الإذن المناسب للتخزين في `AndroidManifest.xml` و التحققات في وقت التشغيل للعمليات على الملفات.
- فئة `App` (المشار إليها في `Crop`) يجب أن تعرّف `drawWidth` و `drawHeight`.

---

#### لماذا هذه الأدوات رائعة

1. **الفعالية**: طرق التعيين تمنع `OutOfMemoryError` عند التعامل مع الصور الكبيرة.
2. **المرونة**: الألوان الرمادية، التحويلات، والتقطيع يغطي مجموعة واسعة من الحالات.
3. **البساطة**: الطرق الثابتة تجعل التكامل سهلًا - لا تحتاج إلى إنشاء.

---

#### الخاتمة

فئات `BitmapUtils` و `Crop` هي نقطة بداية رائعة لأي تطبيق أندرويد يحتاج إلى معالجة الصور. سواء كنت تبنى محرر صور، أو تفيض الصور في المعرض، أو تضيف تقطيع من قبل المستخدم، هذه الشيفرة تغطي احتياجاتك. حاولها، قم بتعديلها حسب احتياجاتك، وقل لي كيف تعمل معك!

ما هي التحديات التي واجهتها في معالجة الصور في أندرويد؟ اشارك أفكارك أدناه!