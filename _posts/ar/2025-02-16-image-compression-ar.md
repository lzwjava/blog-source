---
audio: false
generated: true
image: false
lang: ar
layout: post
title: ضغط الصور باستخدام الجبر الخطي
translated: true
type: note
---

ضغط الصور هو مهمة أساسية في معالجة الصور الرقمية، يهدف إلى تقليل حجم تخزين الصور مع الحفاظ على جودتها البصرية. إحدى الطرق القوية لتحقيق ذلك هي من خلال استخدام الجبر الخطي، وتحديداً تحليل القيم المفردة (SVD). تتيح لنا هذه التقنية تمثيل مصفوفة الصورة بشكل أكثر إحكاما، والتخلص بشكل فعال من المعلومات الأقل أهمية مع الاحتفاظ بالسمات الأساسية.

يوضح كود Python التالي كيفية ضغط صورة باستخدام تحليل القيم المفردة (SVD). تتضمن العملية تحليل الصورة إلى مكوناتها المكونة، وضغط هذه المكونات من خلال الاحتفاظ بمجموعة فرعية فقط من أهم السمات، ثم إعادة بناء الصورة المضغوطة. يمكن تطبيق هذا النهج على كل من الصور ذات التدرج الرمادي والصور الملونة، مما يقدم طريقة مرنة وسليمة رياضياً لتقليل حجم الصورة.

```python
import numpy as np
from PIL import Image
import argparse
import os

def compress_image(image_path, compression_factor=0.1):
    # فتح الصورة وتحويلها إلى مصفوفة numpy
    img = Image.open(image_path)
    img_array = np.array(img, dtype=float)

    # التحقق مما إذا كانت الصورة بتدرج رمادي أو ملونة
    if len(img_array.shape) == 2:  # صورة بتدرج رمادي
        # إجراء تحليل القيم المفردة (SVD) على مصفوفة الصورة
        U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

        # ضغط الصورة بالاحتفاظ بأعلى القيم المفردة فقط
        k = int(compression_factor * min(img_array.shape))
        S_compressed = np.diag(S[:k])
        U_compressed = U[:, :k]
        Vt_compressed = Vt[:k, :]

        # إعادة بناء الصورة المضغوطة
        img_compressed = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))
    else:  # صورة ملونة
        # إجراء تحليل القيم المفردة (SVD) على كل قناة على حدة
        img_compressed = np.zeros_like(img_array)
        for i in range(img_array.shape[2]):  # التكرار خلال كل قناة
            channel = img_array[:, :, i]
            U, S, Vt = np.linalg.svd(channel, full_matrices=False)

            # ضغط القناة بالاحتفاظ بأعلى القيم المفردة فقط
            k = int(compression_factor * min(channel.shape))
            S_compressed = np.diag(S[:k])
            U_compressed = U[:, :k]
            Vt_compressed = Vt[:k, :]

            # إعادة بناء القناة المضغوطة
            img_compressed[:, :, i] = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))

    # اقتص القيم لتكون بين 0 و 255، والتحويل مرة أخرى إلى uint8
    img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)

    # إنشاء مسار الإخراج بإضافة '_compressed' إلى اسم الملف الأصلي
    file_name, file_extension = os.path.splitext(image_path)
    output_path = f"{file_name}_compressed{file_extension}"

    # حفظ الصورة المضغوطة
    compressed_img = Image.fromarray(img_compressed)
    compressed_img.save(output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress an image using SVD.")
    parser.add_argument("input_file", help="Path to the input image file")
    parser.add_argument("--compression_factor", type=float, default=0.1, help="Compression factor (default: 0.1)")
    args = parser.parse_args()

    output_file = compress_image(args.input_file, args.compression_factor)
    print(f"Compressed image saved as: {output_file}")

```