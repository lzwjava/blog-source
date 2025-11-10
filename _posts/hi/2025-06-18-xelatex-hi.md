---
audio: false
generated: true
lang: hi
layout: post
title: ज़ेवलाटेक इंस्टॉल करें
translated: true
type: note
---

Ubuntu 24.04 या 22.04 पर XeLaTeX इंस्टॉल करने के लिए, इन चरणों का पालन करें:

1. **पैकेज सूची अपडेट करें**:
   ```bash
   sudo apt update
   ```

2. **TeX Live इंस्टॉल करें (जिसमें XeLaTeX शामिल है)**:
   - एक पूर्ण इंस्टॉलेशन के लिए (अधिकांश उपयोगकर्ताओं के लिए अनुशंसित, XeLaTeX और कई पैकेज शामिल हैं):
     ```bash
     sudo apt install texlive-xetex
     ```
   - यदि आप एक न्यूनतम इंस्टॉलेशन चाहते हैं, तो आप `texlive` इंस्टॉल कर सकते हैं, लेकिन XeLaTeX सपोर्ट के लिए `texlive-xetex` बेहतर है।

3. **इंस्टॉलेशन सत्यापित करें**:
   यह जांचने के लिए कि क्या XeLaTeX इंस्टॉल है, निम्न कमांड चलाएँ:
   ```bash
   xelatex --version
   ```
   आपको `XeTeX 3.14159265-2.6-0.999991` जैसा आउटपुट दिखना चाहिए (वर्जन नंबर भिन्न हो सकते हैं)।

4. **वैकल्पिक: अतिरिक्त फोंट इंस्टॉल करें** (यदि आपको XeLaTeX के लिए विशिष्ट फोंट की आवश्यकता है):
   ```bash
   sudo apt install texlive-fonts-extra
   ```

5. **XeLaTeX टेस्ट करें**:
   एक साधारण `.tex` फ़ाइल बनाएँ, उदाहरण के लिए, `test.tex`:
   ```latex
   \documentclass{article}
   \usepackage{fontspec}
   \setmainfont{Liberation Serif}
   \begin{document}
   Hello, XeLaTeX!
   \end{document}
   ```
   इसे इसके साथ कंपाइल करें:
   ```bash
   xelatex test.tex
   ```
   इससे एक `test.pdf` फ़ाइल जनरेट होनी चाहिए।

**नोट्स**:
- `texlive-xetex` पैकेज Ubuntu 22.04 और 24.04 रिपॉजिटरीज में उपलब्ध है।
- यदि आपको नवीनतम TeX Live वर्जन चाहिए, तो आप इसे मैन्युअली TeX Live वेबसाइट से इंस्टॉल कर सकते हैं, लेकिन Ubuntu पैकेज आमतौर पर पर्याप्त होता है।
- सुनिश्चित करें कि आपके पास पर्याप्त डिस्क स्पेस है (~1-2 GB `texlive-xetex` के लिए, `texlive-full` के लिए अधिक)।
- यदि आपको कोई समस्या आती है, तो `sudo apt install -f` के साथ गायब डिपेंडेंसीज की जाँच करें।

यदि आपको और सहायता चाहिए तो मुझे बताएं!