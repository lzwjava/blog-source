---
audio: true
generated: false
lang: ar
layout: post
title: ضغط الصور باستخدام الجبر الخطي
translated: true
---

التضغط على الصور هو مهمة أساسية في معالجة الصور الرقمية، تهدف إلى تقليل حجم تخزين الصور بينما تحافظ على جودتها البصرية. أحد الطرق القوية لتحقيق ذلك هو استخدام الجبر الخطي، وخاصة تفكيك القيمة الغريبة (SVD). تسمح هذه التقنية لنا بتقديم مصفوفة الصورة في شكل أكثر تعقيدًا، من خلال التخلص من المعلومات الأقل أهمية بينما تحافظ على الميزات الأساسية.

يوضح الكود التالي كيفية ضغط صورة باستخدام SVD. يتضمن هذا العملية تفكيك الصورة إلى مكوناتها، ضغط هذه المكونات من خلال الاحتفاظ فقط بجزء من الميزات الأكثر أهمية، ثم إعادة بناء الصورة المضغوطة. يمكن تطبيق هذه الطريقة على الصور الرمادية والألوان، مما يوفر طريقة مرنة ومثبتة رياضيًا لتخفيض حجم الصورة.

```python
import numpy as np
from PIL import Image
import argparse
import os

def compress_image(image_path, compression_factor=0.1):
    # افتح الصورة و تحويلها إلى مصفوفة نمرية
    img = Image.open(image_path)
    img_array = np.array(img, dtype=float)

    # تحقق من أن الصورة رمادية أو ملونة
    if len(img_array.shape) == 2:  # صورة رمادية
        # تنفيذ SVD على مصفوفة الصورة
        U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

        # ضغط الصورة من خلال الاحتفاظ فقط بأعلى القيم الغريبة
        k = int(compression_factor * min(img_array.shape))
        S_compressed = np.diag(S[:k])
        U_compressed = U[:, :k]
        Vt_compressed = Vt[:k, :]

        # إعادة بناء الصورة المضغوطة
        img_compressed = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))
    else:  # صورة ملونة
        # تنفيذ SVD على كل قناة بشكل منفصل
        img_compressed = np.zeros_like(img_array)
        for i in range(img_array.shape[2]):  # تكرار على كل قناة
            channel = img_array[:, :, i]
            U, S, Vt = np.linalg.svd(channel, full_matrices=False)

            # ضغط القناة من خلال الاحتفاظ فقط بأعلى القيم الغريبة
            k = int(compression_factor * min(channel.shape))
            S_compressed = np.diag(S[:k])
            U_compressed = U[:, :k]
            Vt_compressed = Vt[:k, :]

            # إعادة بناء القناة المضغوطة
            img_compressed[:, :, i] = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))

    # تقليم القيم لتكون بين 0 و 255، و تحويلها مرة أخرى إلى uint8
    img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)

    # إنشاء مسار الإخراج من خلال إضافة '_compressed' إلى اسم الملف الأصلي
    file_name, file_extension = os.path.splitext(image_path)
    output_path = f"{file_name}_compressed{file_extension}"

    # حفظ الصورة المضغوطة
    compressed_img = Image.fromarray(img_compressed)
    compressed_img.save(output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ضغط صورة باستخدام SVD.")
    parser.add_argument("input_file", help="مسار ملف الصورة المدخل")
    parser.add_argument("--compression_factor", type=float, default=0.1, help="عامل الضغط (الافتراضي: 0.1)")
    args = parser.parse_args()

    output_file = compress_image(args.input_file, args.compression_factor)
    print(f"تم حفظ الصورة المضغوطة باسم: {output_file}")
```