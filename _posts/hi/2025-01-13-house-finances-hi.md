---
audio: false
generated: false
lang: hi
layout: post
title: हमारे घर के वित्त का ट्रैकिंग
translated: true
---

हाल ही में, मैंने अपने घर के वित्तीय लेन-देन को ट्रैक करने के लिए एक मार्कडाउन दस्तावेज़ बनाया।

यह घर मेरी पत्नी और मेरा है। मेरे माता-पिता ने हमें पैसे दिए, और हमने मेरी बहन और मेरे मामा से पैसे उधार लिए। हालांकि मेरे मामा ने पैसे मुझे भेजे थे, बाद में मेरे पिता ने वह राशि चुका दी।

हमने अपने घर की कुल कीमत का 50% डाउन पेमेंट के रूप में चुकाया, और बाकी का आधा हिस्सा हमने Agricultural Bank of China से उधार लिया। अनुबंध 20 साल के लिए है, और वर्तमान ब्याज दर 3.65% है।

जब मैं बेरोजगार था, तो मेरी पत्नी और मेरे पिता ने मुझे मासिक किश्तों का भुगतान करने के लिए धन उपलब्ध कराया। नतीजतन, इसमें कई लेन-देन शामिल हैं।

मैं अपने प्राथमिक बैंक के रूप में China Merchants Bank का उपयोग करता हूं। China Merchants Bank लेन-देन को फ़िल्टर करने की अनुमति देता है कि वे आने वाले हैं या जाने वाले, और एक न्यूनतम राशि के आधार पर। यह कीवर्ड के आधार पर फ़िल्टरिंग का भी समर्थन करता है, जो बहुत मददगार है।

एक और मददगार पहलू AI की प्रचलितता है। यह इस कार्य में भी सहायता कर सकता है। AI-संचालित OCR, विशेष रूप से Grok का उपयोग करके, मैं Guangzhou Electric Power Bureau के साथ लेन-देन रिकॉर्ड से टेक्स्ट निकालने में सक्षम था।

चूंकि बाद की तालिका पिछले नंबरों पर आधारित है, इसलिए आगे बढ़ने से पहले यह सुनिश्चित करने के लिए नंबरों की जांच करना बेहतर है कि सब कुछ सही है।

नीचे दिया गया कोड मार्कडाउन से PDF जेनरेट करने में मदद करता है। इसमें PDF में चीनी अक्षरों को रेंडर करने के लिए कुछ विशेष सेटिंग्स हैं।

```python
import os
import subprocess

# कॉन्फ़िगरेशन
CJK_FONT = "Heiti SC"
GEOMETRY = "margin=1in"
input_markdown_path = "mortgage.md"  # अपनी इनपुट मार्कडाउन फ़ाइल के साथ बदलें
output_pdf_path = "mortgage.pdf"    # अपनी वांछित आउटपुट PDF फ़ाइल के साथ बदलें

# जांचें कि इनपुट फ़ाइल मौजूद है या नहीं
if not os.path.exists(input_markdown_path):
    raise Exception(f"इनपुट फ़ाइल मौजूद नहीं है: {input_markdown_path}")

# Pandoc कमांड बनाएं
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]

# Pandoc कमांड चलाएं
try:
    subprocess.run(command, check=True)
    print(f"PDF सफलतापूर्वक जेनरेट की गई: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"PDF जेनरेट करने में त्रुटि: {e}")
```