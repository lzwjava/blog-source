---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: गिट चेक-इग्नोर कमांड का अवलोकन
translated: true
type: note
---

### `git check-ignore` क्या है?

`git check-ignore` कमांड एक Git टूल है जिसका उपयोग यह निर्धारित करने के लिए किया जाता है कि कोई विशिष्ट फ़ाइल या पथ Git की ignore mechanisms (जैसे `.gitignore` फ़ाइलें, `.git/info/exclude`, या global ignore files (`core.excludesFile` के माध्यम से)) द्वारा अनदेखा किया गया है या नहीं। यह डीबग करने के लिए विशेष रूप से उपयोगी है कि कोई फ़ाइल क्यों ट्रैक नहीं की जा रही है या रिपॉजिटरी में जोड़ी नहीं जा रही है।

यदि पथ को अनदेखा किया गया है, तो कमांड पथ (और वैकल्पिक रूप से मेल खाने वाले पैटर्न) आउटपुट करता है। यदि इसे अनदेखा नहीं किया गया है, तो कोई आउटपुट नहीं होता है (एग्जिट कोड 0)। यह इसे ऑटोमेशन के लिए स्क्रिप्ट-फ्रेंडली बनाता है।

### बेसिक उपयोग

इसे जांचने के लिए एक या अधिक पथ के साथ चलाएं:

```
git check-ignore <pathname>...
```

- **उदाहरण**: जांचें कि क्या एक फ़ाइल अनदेखी की गई है:
  ```
  git check-ignore path/to/myfile.txt
  ```
  - आउटपुट: यदि अनदेखी की गई है, तो `path/to/myfile.txt` प्रिंट करता है। यदि नहीं, तो कुछ भी प्रिंट नहीं करता।

- **उदाहरण**: एकाधिक फ़ाइलों की जांच करें:
  ```
  git check-ignore file1.txt file2.txt dir/file3.txt
  ```
  - केवल अनदेखे गए पथ आउटपुट करता है, प्रति लाइन एक।

### मुख्य विकल्प

| विकल्प | विवरण | उदाहरण |
|--------|-------------|---------|
| `-v`, `--verbose` | वह अनदेखा पैटर्न दिखाएं जो मेल खाता है (जैसे, `.gitignore` से लाइन)। | `git check-ignore -v path/to/myfile.txt`<br>आउटपुट: `path/to/myfile.txt: .gitignore:1:*.txt` (पथ + फ़ाइल:लाइन:पैटर्न) |
| `-q`, `--quiet` | आउटपुट दबाएं, लेकिन फिर भी एग्जिट कोड का उपयोग करें (0 यदि अनदेखा नहीं, 1 यदि अनदेखा)। स्क्रिप्ट्स में उपयोगी। | `git check-ignore -q path/to/myfile.txt`<br>(कोई आउटपुट नहीं; एग्जिट कोड के लिए `$?` जांचें) |
| `--stdin` | कमांड लाइन के बजाय स्टैंडर्ड इनपुट से पथ पढ़ें। | `echo "file1.txt\nfile2.txt" \| git check-ignore --stdin` |
| `--non-matching` | आउटपुट को उल्टा करें: उन पथों को दिखाएं जो अनदेखे *नहीं* हैं। | `git check-ignore --non-matching -v file1.txt file2.txt` |

### सामान्य उपयोग के मामले

1. **`.gitignore` नियमों को डीबग करना**:
   - यदि `git status` आपकी अपेक्षित फ़ाइल नहीं दिखाता है, तो यह देखने के लिए चलाएं कि कौन सा नियम इसे अनदेखा कर रहा है: `git check-ignore -v <file>`।
   - उदाहरण आउटपुट: `src/logs/app.log: .gitignore:5:logs/*` (इंगित करता है कि `.gitignore` की लाइन 5 मेल खाती है)।

2. **स्क्रिप्ट्स में**:
   - जांचें कि क्या कोई फ़ाइल जोड़ी जानी चाहिए:
     ```
     if git check-ignore -q myfile.txt; then
         echo "फ़ाइल अनदेखी की गई है, छोड़ रहा हूं..."
     else
         git add myfile.txt
     fi
     ```

3. **बैच जांच**:
   - एक डायरेक्टरी में सभी अनदेखी की गई फ़ाइलों की सूची बनाएं:
     ```
     find . -type f -print0 | xargs -0 git check-ignore
     ```

### टिप्स
- यह Git ignore stack का सम्मान करता है: local `.gitignore`, global excludes, आदि।
- अनट्रैक की गई फ़ाइलों या रिपॉजिटरी में पहले से मौजूद फ़ाइलों पर काम करता है (लेकिन अनदेखा नियमों के विरुद्ध जांच करता है)।
- अधिक जानकारी के लिए, आधिकारिक दस्तावेज़ देखें।

[Git check-ignore दस्तावेज़ीकरण](https://git-scm.com/docs/git-check-ignore)  
[Stack Overflow: Git command to show which specific files are ignored](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)  
[Using git check-ignore to debug your .gitignore](https://alexwlchan.net/til/2020/using-git-check-ignore-to-debug-your-gitignore/)