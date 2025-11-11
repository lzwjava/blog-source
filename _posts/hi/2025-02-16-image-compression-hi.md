---
audio: false
generated: true
image: false
lang: hi
layout: post
title: लीनियर अलजेब्रा का उपयोग करके छवि संपीड़न
translated: true
type: note
---

इमेज कंप्रेशन डिजिटल इमेज प्रोसेसिंग में एक मूलभूत कार्य है, जिसका उद्देश्य इमेज की विजुअल क्वालिटी को बनाए रखते हुए उसके स्टोरेज आकार को कम करना है। इसे प्राप्त करने का एक शक्तिशाली तरीका लीनियर अलजेब्रा, विशेष रूप से सिंगुलर वैल्यू डिकम्पोजिशन (SVD) का उपयोग है। यह तकनीक हमें एक इमेज मैट्रिक्स को अधिक कॉम्पैक्ट रूप में प्रस्तुत करने की अनुमति देती है, जिससे कम महत्वपूर्ण जानकारी को प्रभावी ढंग से हटाकर आवश्यक फीचर्स को बरकरार रखा जा सकता है।

निम्नलिखित Python कोड SVD का उपयोग करके एक इमेज को कंप्रेस करने का तरीका दर्शाता है। इस प्रक्रिया में इमेज को उसके घटकों में विघटित करना, केवल सबसे महत्वपूर्ण फीचर्स के एक सबसेट को बनाए रखते हुए इन घटकों को कंप्रेस करना, और फिर कंप्रेस्ड इमेज को पुनर्निर्मित करना शामिल है। इस दृष्टिकोण को ग्रेस्केल और कलर दोनों प्रकार की इमेजेस पर लागू किया जा सकता है, जो इमेज आकार को कम करने के लिए एक लचीली और गणितीय रूप से सुदृढ़ विधि प्रदान करता है।

```python
import numpy as np
from PIL import Image
import argparse
import os

def compress_image(image_path, compression_factor=0.1):
    # इमेज को खोलें और इसे एक numpy array में बदलें
    img = Image.open(image_path)
    img_array = np.array(img, dtype=float)

    # जांचें कि इमेज ग्रेस्केल है या कलर
    if len(img_array.shape) == 2:  # ग्रेस्केल इमेज
        # इमेज array पर SVD करें
        U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

        # केवल शीर्ष singular values को रखकर इमेज को कंप्रेस करें
        k = int(compression_factor * min(img_array.shape))
        S_compressed = np.diag(S[:k])
        U_compressed = U[:, :k]
        Vt_compressed = Vt[:k, :]

        # कंप्रेस्ड इमेज का पुनर्निर्माण करें
        img_compressed = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))
    else:  # कलर इमेज
        # प्रत्येक चैनल पर अलग-अलग SVD करें
        img_compressed = np.zeros_like(img_array)
        for i in range(img_array.shape[2]):  # प्रत्येक चैनल पर पुनरावृति करें
            channel = img_array[:, :, i]
            U, S, Vt = np.linalg.svd(channel, full_matrices=False)

            # केवल शीर्ष singular values को रखकर चैनल को कंप्रेस करें
            k = int(compression_factor * min(channel.shape))
            S_compressed = np.diag(S[:k])
            U_compressed = U[:, :k]
            Vt_compressed = Vt[:k, :]

            # कंप्रेस्ड चैनल का पुनर्निर्माण करें
            img_compressed[:, :, i] = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))

    # वैल्यूज को 0 और 255 के बीच सीमित करें, और वापस uint8 में बदलें
    img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)

    # मूल फाइलनाम में '_compressed' जोड़कर आउटपुट पथ जनरेट करें
    file_name, file_extension = os.path.splitext(image_path)
    output_path = f"{file_name}_compressed{file_extension}"

    # कंप्रेस्ड इमेज को सेव करें
    compressed_img = Image.fromarray(img_compressed)
    compressed_img.save(output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SVD का उपयोग करके एक इमेज को कंप्रेस करें।")
    parser.add_argument("input_file", help="इनपुट इमेज फाइल का पथ")
    parser.add_argument("--compression_factor", type=float, default=0.1, help="कंप्रेशन फैक्टर (डिफ़ॉल्ट: 0.1)")
    args = parser.parse_args()

    output_file = compress_image(args.input_file, args.compression_factor)
    print(f"कंप्रेस्ड इमेज इस नाम से सेव हुई: {output_file}")

```