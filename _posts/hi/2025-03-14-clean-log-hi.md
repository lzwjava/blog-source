---
audio: false
generated: true
lang: hi
layout: post
title: स्वच्छ लॉग संदेश
translated: true
type: note
---

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    एक लॉग फ़ाइल पढ़ता है, समानता के आधार पर डुप्लिकेट क्रमिक स्टैंडर्ड लॉग लाइन्स को हटाता है,
    और साफ की गई लॉग को निर्दिष्ट फ़ाइल में लिखता है, डिफ़ॉल्ट रूप से इनपुट फ़ाइल को ओवरराइट करता है।

    Args:
        input_path (str, optional): इनपुट लॉग फ़ाइल का पथ। यदि None है, तो stdin से पढ़ता है।
        output_path (str, optional): आउटपुट लॉग फ़ाइल का पथ। यदि None है, तो इनपुट फ़ाइल को ओवरराइट करता है।
        similarity_threshold (float, optional): लाइनों को डुप्लिकेट मानने के लिए समानता अनुपात (0.0 से 1.0)। डिफ़ॉल्ट 1.0 (एकदम मेल) है।
        lines_to_compare (int, optional): तुलना करने के लिए क्रमिक लाइनों की संख्या। डिफ़ॉल्ट 1 है।
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("lines_to_compare 1 से अधिक या बराबर एक पूर्णांक होना चाहिए।")

    # इनपुट स्रोत निर्धारित करें
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"Error: फ़ाइल पथ पर नहीं मिली: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # stdin से सभी लाइनें पढ़ें

    # आउटपुट गंतव्य निर्धारित करें
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"Error: लिखने के लिए फ़ाइल खोलने में असमर्थ: {output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # इनपुट फ़ाइल को ओवरराइट करें
        except IOError:
            print(f"Error: लिखने के लिए फ़ाइल खोलने में असमर्थ: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # यदि कोई input_path नहीं है तो डिफ़ॉल्ट रूप से stdout का उपयोग करें

    num_lines = len(lines)
    i = 0
    removed_lines = 0
    while i < num_lines:
        # 'lines_to_compare' लाइनें या शेष लाइनें इकट्ठा करें यदि 'lines_to_compare' से कम हैं
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # केवल तभी प्रोसेस करें जब हमारे पास तुलना करने के लिए पर्याप्त लाइनें हों
        if len(current_lines) == lines_to_compare:
            # पहली सेट की लाइनों से स्टैंडर्ड जानकारी निकालें
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"Non-standard line: {line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # यदि कोई non-standard लाइन मिलती है तो इस ग्रुप की प्रोसेसिंग रोकें

            if all_standard:
                # दूसरे सेट की लाइनों से स्टैंडर्ड जानकारी निकालें (यदि उपलब्ध हो)
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # अगली लाइनों को non-standard मानें यदि उनमें से कोई भी non-standard है
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"Similarity: {similarity:.4f}, Threshold: {similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"Skipping duplicate lines: { ''.join([line.strip() for line in current_lines])}")
                            removed_lines += len(current_lines)
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # अगले सेट की लाइनों पर जाएं
        else:
            # शेष लाइनों को हैंडल करें ('lines_to_compare' से कम)
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"Non-standard line: {line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

    if output_path or input_path:
        outfile.close()

    print(f"Removed {removed_lines} duplicate lines.")


def is_valid_similarity_threshold(value):
    """
    जांचें कि क्या दिया गया मान एक वैध समानता थ्रेशोल्ड है।
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Similarity threshold एक फ्लोटिंग-पॉइंट नंबर होना चाहिए।")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("Similarity threshold 0.0 और 1.0 के बीच होना चाहिए।")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="किसी फ़ाइल या stdin से डुप्लिकेट लॉग लाइन्स साफ करें और एक फ़ाइल में लिखें, डिफ़ॉल्ट रूप से इनपुट फ़ाइल को ओवरराइट करते हुए।")
    parser.add_argument("input_path", nargs="?", type=str, help="इनपुट लॉग फ़ाइल का पथ (वैकल्पिक, डिफ़ॉल्ट stdin)")
    parser.add_argument("-o", "--output_path", type=str, help="आउटपुट लॉग फ़ाइल का पथ (वैकल्पिक, डिफ़ॉल्ट इनपुट फ़ाइल को ओवरराइट करना)")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="लाइनों को डुप्लिकेट मानने के लिए समानता थ्रेशोल्ड (0.0-1.0) (डिफ़ॉल्ट: 1.0)")
    parser.add_argument("-l", "--lines", type=int, default=1, help="तुलना करने के लिए क्रमिक लाइनों की संख्या (डिफ़ॉल्ट: 1)")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

यह Python स्क्रिप्ट `clean_log.py` एक फ़ाइल या स्टैंडर्ड इनपुट से डुप्लिकेट लॉग लाइन्स को हटाने के लिए डिज़ाइन की गई है। यह यह निर्धारित करने के लिए एक समानता थ्रेशोल्ड का उपयोग करती है कि क्या क्रमिक लॉग लाइन्स डुप्लिकेट मानी जाने के लिए पर्याप्त समान हैं।

यहां कोड का विवरण दिया गया है:

**1. इम्पोर्ट्स:**

- `sys`: Python इंटरप्रेटर के साथ इंटरैक्ट करने के लिए उपयोग किया जाता है, जैसे stdin से पढ़ना और stderr पर लिखना।
- `argparse`: कमांड-लाइन इंटरफेस बनाने के लिए उपयोग किया जाता है।
- `difflib.SequenceMatcher`: स्ट्रिंग्स के अनुक्रमों के बीच समानता की तुलना करने के लिए उपयोग किया जाता है।

**2. `clean_log` फंक्शन:**

- `input_path`, `output_path`, `similarity_threshold`, और `lines_to_compare` को आर्गुमेंट के रूप में लेता है।
- `input_path`: इनपुट लॉग फ़ाइल निर्दिष्ट करता है। यदि `None` है, तो stdin से पढ़ता है।
- `output_path`: आउटपुट फ़ाइल निर्दिष्ट करता है। यदि `None` है, और `input_path` दिया गया है, तो यह इनपुट फ़ाइल को ओवरराइट करता है। यदि दोनों `None` हैं, तो यह stdout पर लिखता है।
- `similarity_threshold`: 0.0 और 1.0 के बीच एक फ्लोट जो लाइनों को डुप्लिकेट माने जाने के लिए न्यूनतम समानता अनुपात निर्धारित करता है। 1.0 का मान केवल एक समान लाइनों को हटाता है।
- `lines_to_compare`: समानता के लिए तुलना करने के लिए क्रमिक लाइनों की संख्या निर्दिष्ट करने वाला एक पूर्णांक।

- **इनपुट हैंडलिंग:**
    - इनपुट फ़ाइल या stdin से लाइनें पढ़ता है।
    - यदि इनपुट फ़ाइल मौजूद नहीं है तो `FileNotFoundError` को हैंडल करता है।

- **आउटपुट हैंडलिंग:**
    - आउटपुट फ़ाइल को लिखने के लिए खोलता है या stdout का उपयोग करता है।
    - यदि आउटपुट फ़ाइल नहीं खोली जा सकती तो `IOError` को हैंडल करता है।

- **डुप्लिकेट रिमूवल लॉजिक:**
    - लॉग फ़ाइल की लाइनों से `lines_to_compare` के chunks में पुनरावृति करता है।
    - प्रत्येक chunk के लिए:
        - प्रत्येक लाइन को " | " डिलीमीटर के आधार पर भागों में विभाजित करता है, चार भागों की अपेक्षा करता है: level, timestamp, thread, और message।
        - यदि किसी लाइन में चार भाग नहीं हैं, तो इसे "non-standard" लाइन माना जाता है और तुलना के बिना आउटपुट में प्रिंट किया जाता है।
        - यदि वर्तमान chunk की सभी लाइनें स्टैंडर्ड हैं, तो यह उनकी तुलना अगले `lines_to_compare` लाइनों से करता है।
        - यह वर्तमान और अगले chunks के thread और message भागों की जुड़ी हुई स्ट्रिंग्स के बीच समानता अनुपात की गणना करने के लिए `SequenceMatcher` का उपयोग करता है।
        - यदि समानता अनुपात `similarity_threshold` से कम है, तो लाइनों का वर्तमान chunk आउटपुट में प्रिंट होता है।
        - यदि समानता अनुपात `similarity_threshold` से अधिक या बराबर है, तो लाइनों के वर्तमान chunk को डुप्लिकेट माना जाता है और छोड़ दिया जाता है।
    - फ़ाइल के अंत में शेष लाइनों को हैंडल करता है (`lines_to_compare` से कम लाइनें)।

- **स्टैटिस्टिक्स:**
    - हटाई गई लाइनों की संख्या का ट्रैक रखता है।
    - हटाई गई लाइनों की संख्या कंसोल पर प्रिंट करता है।

- **फ़ाइल क्लोजिंग:**
    - आउटपुट फ़ाइल को बंद करता है यदि इसे खोला गया था।

**3. `is_valid_similarity_threshold` फंक्शन:**

- `argparse` द्वारा समानता थ्रेशोल्ड आर्गुमेंट को वैलिडेट करने के लिए उपयोग किया जाने वाला एक हेल्पर फंक्शन।
- यह जांचता है कि क्या इनपुट मान 0.0 और 1.0 के बीच एक फ्लोट है।

**4. `if __name__ == "__main__":` ब्लॉक:**

- यह ब्लॉक तब एक्ज़िक्यूट होता है जब स्क्रिप्ट कमांड लाइन से चलाई जाती है।
- यह कमांड-लाइन आर्गुमेंट पार्सर बनाने के लिए `argparse` का उपयोग करता है।
- यह निम्नलिखित आर्गुमेंट्स को परिभाषित करता है:
    - `input_path`: इनपुट लॉग फ़ाइल का पथ (वैकल्पिक)।
    - `-o` या `--output_path`: आउटपुट लॉग फ़ाइल का पथ (वैकल्पिक)।
    - `-s` या `--similarity`: समानता थ्रेशोल्ड (डिफ़ॉल्ट: 1.0)।
    - `-l` या `--lines`: तुलना करने के लिए लाइनों की संख्या (डिफ़ॉल्ट: 1)।
- यह `parser.parse_args()` का उपयोग करके कमांड-लाइन आर्गुमेंट्स को पार्स करता है।
- यह पार्स किए गए आर्गुमेंट्स के साथ `clean_log` फंक्शन को कॉल करता है।

**संक्षेप में, स्क्रिप्ट लॉग फ़ाइलों को कॉन्फ़िगरेबल समानता थ्रेशोल्ड और तुलना करने के लिए लाइनों की संख्या के आधार पर डुप्लिकेट लाइनों को हटाकर साफ करने का एक लचीला तरीका प्रदान करती है। यह stdin से पढ़ने, stdout पर लिखने, और इनपुट फ़ाइल को ओवरराइट करने का सपोर्ट करती है।**