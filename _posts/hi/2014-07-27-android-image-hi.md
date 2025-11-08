---
audio: false
generated: false
image: false
lang: hi
layout: post
title: 'Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy


  Android Image Processing Made Easy'
translated: true
type: post
---

Android में छवियों का संचालन मुश्किल हो सकता है—बिटमैप मेमोरी खा जाते हैं, घुमावों से दिशा में गड़बड़ होती है, और कटाई में सटीकता की आवश्यकता होती है। यही वजह है कि `BitmapUtils` और `Crop` जैसे उपयोगिता वर्ग उपयोगी होते हैं। इस पोस्ट में, मैं आपको `com.lzw.flower.utils` पैकेज से एक शक्तिशाली जोड़ी वर्गों के बारे में बताता हूँ। हम उनके कोड का पता लगाएँगे, प्रत्येक विधि का विश्लेषण करेंगे, और दिखाएँगे कि आप अपने प्रोजेक्ट में उन्हें कैसे उपयोग कर सकते हैं। चलो, शुरू करते हैं!

---

#### BitmapUtils: आपका छवि संचालन टूलकिट

`BitmapUtils` वर्ग एक `Bitmap` वस्तुओं को संचालित करने के लिए स्थिर विधियों का संग्रह है। यहाँ पूरा कोड है, उसके बाद एक विश्लेषण:

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

##### इसमें क्या है?
- **ग्रेस्केल परिवर्तन**:
  - `convertGreyImg`: एक पिक्सेल एरे को उपयोग करके बिटमैप को ग्रेस्केल में बैच-प्रोसेस करता है।
  - `toGreyImg`: एक परिवर्तनीय कॉपी पर पिक्सेल-पर-पिक्सेल काम करता है, एक विकल्प के रूप में एक अलग तरीका प्रदान करता है।
  दोनों ग्रेस्केल के लिए लुमिनोसिटी सूत्र (`0.3R + 0.59G + 0.11B`) का उपयोग करते हैं।

- **फ़ाइल संचालन**:
  - `saveBitmapToPath`: एक बिटमैप को एक PNG के रूप में सेट करता है, आवश्यकता पड़ने पर डायरेक्टरी बनाता है।

- **परिवर्तन**:
  - `rotateBitmap`: एक `Matrix` का उपयोग करके एक छवि को घुमाता है—सादा लेकिन प्रभावी।

- **लोडिंग और सैंपलिंग**:
  - `getBitmapByUri` और `getResourceUri`: छवियों को URI या संसाधनों से लोड करता है।
  - `decodeSampledBitmapFromPath` और `decodeFileByHeight`: ऊंचाई या चौड़ाई के अनुसार बड़े छवियों को दक्षता से स्केल करता है, मेमोरी समस्याओं से बचता है।

---

#### Crop: Android के नेटिव टूल्स के साथ सटीक कटाई

`Crop` वर्ग Android के बिल्ट-इन क्रॉप इंटेंट का उपयोग करता है। यहाँ कोड है:

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

##### यहाँ क्या हो रहा है?
- `startPhotoCrop`: एक निर्दिष्ट `Uri`, अनुपात (GCD का उपयोग करके सरल बनाया गया), और आउटपुट पथ के साथ सिस्टम क्रॉप गतिविधि को लॉन्च करता है। यह मानता है कि `App.drawWidth` और `App.drawHeight` कहीं और परिभाषित हैं (उदाहरण के लिए, एक आधार `App` वर्ग में)।
- `gcd`: एक पुनरावर्ती विधि है जो सबसे बड़ा सामान्य गुणांक (GCD) को गणना करने के लिए, सुनिश्चित करता है कि अनुपात अपने सरलतम रूप में है।

---

#### सब कुछ एक साथ: उपयोग उदाहरण

यहाँ आप Android app में इन उपयोगिता को कैसे उपयोग कर सकते हैं:

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

        // एक छवि को ग्रेस्केल में परिवर्तित करें और इसे सेट करें
        Bitmap original = BitmapFactory.decodeResource(getResources(), R.drawable.sample);
        Bitmap grey = BitmapUtils.convertGreyImg(original);
        BitmapUtils.saveBitmapToPath(grey, "/sdcard/DCIM/grey_image.png");

        // एक छवि को दक्षता से लोड और स्केल करें
        Bitmap scaled = BitmapUtils.decodeSampledBitmapFromPath("/sdcard/DCIM/photo.jpg", 200);

        // क्रॉपिंग लॉन्च करें
        Uri imageUri = Uri.fromFile(new File("/sdcard/DCIM/photo.jpg"));
        Crop.startPhotoCrop(this, imageUri, "/sdcard/DCIM/cropped.png", REQUEST_CROP);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CROP && resultCode == RESULT_OK) {
            // क्रॉप्ड छवि "/sdcard/DCIM/cropped.png" पर सेट है
        }
    }
}
```

**नोट्स**:
- `AndroidManifest.xml` और रनटाइम चेक में फाइल संचालन के लिए सही स्टोरेज अनुमतियाँ सुनिश्चित करें।
- `Crop` में संदर्भित `App` वर्ग ( `drawWidth` और `drawHeight` को परिभाषित करे।

---

#### इन उपयोगिता के कारण ये रॉक

1. **दक्षता**: सैंपलिंग विधियाँ बड़े छवियों के साथ `OutOfMemoryError` से बचने में मदद करती हैं।
2. **लचीलापन**: ग्रेस्केल, घुमाव, और कटाई एक व्यापक श्रेणी के उपयोग के लिए कवर करती हैं।
3. **सादगी**: स्थिर विधियाँ एकीकृत करने में आसान बनाती हैं—किसी भी उदाहरण की आवश्यकता नहीं है।

---

#### अंतिम विचार

`BitmapUtils` और `Crop` वर्ग किसी भी Android app के लिए छवि संचालन की एक अद्भुत शुरुआत हैं। चाहे आप एक फोटो एडिटर बन रहे हों, गैलरी थंबनेल्स को ऑप्टिमाइज कर रहे हों, या उपयोगकर्ता-ड्राइव क्रॉपिंग जोड़ रहे हों, यह कोड आपके लिए है। इसे ट्राई करें, अपने आवश्यकताओं के अनुसार इसे ट्यून करें, और मुझे बताएं कि यह आपके लिए कैसे काम करता है!

आपने Android में छवि प्रोसेसिंग के साथ कौन से चुनौतियों का सामना किया है? अपने विचार नीचे साझा करें!