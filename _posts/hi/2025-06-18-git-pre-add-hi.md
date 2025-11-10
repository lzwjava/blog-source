---
audio: false
generated: true
lang: hi
layout: post
title: गिट प्री-एड हुक विकल्पों का निर्माण
translated: true
type: note
---

Git में एक अंतर्निहित `pre-add` हुक नहीं है, लेकिन कई तरीके हैं जिनसे आप समान कार्यक्षमता प्राप्त कर सकते हैं। यहां कुछ उपाय दिए गए हैं:

### 1. **Git Aliases (सुझाया गया तरीका)**
आप एक Git alias बना सकते हैं जो `git add` को कॉल करने से पहले आपकी जांच चलाता है:

```bash
git config --global alias.safe-add '!your-pre-add-script.sh && git add'
```

फिर `git add` के बजाय `git safe-add` का उपयोग करें।

### 2. **Wrapper Script**
अपने PATH में `git-pre-add` नामक एक स्क्रिप्ट बनाएं जो:
1. आपकी pre-add जांच चलाती है
2. यदि जांच पास होती है तो `git add` को कॉल करती है

```bash
#!/bin/bash
# यहां आपका pre-add validation logic
if [ some_condition ]; then
  git add "$@"
else
  echo "Pre-add checks failed"
  exit 1
fi
```

### 3. **मौजूदा Hooks का उपयोग करना**
आप मौजूदा hooks का रचनात्मक तरीकों से उपयोग कर सकते हैं:
- **pre-commit**: जबकि यह add के बाद लेकिन commit से पहले चलता है, आप यहां staged files की जांच कर सकते हैं
- **prepare-commit-msg**: pre-commit के समान लेकिन प्रक्रिया में पहले

### 4. **Filesystem Monitoring**
अधिक उन्नत आवश्यकताओं के लिए, आप उपयोग कर सकते हैं:
- **inotifywait** (Linux) अपनी working directory को देखने के लिए
- **fswatch** (Mac) समान कार्यक्षमता के लिए

### उदाहरण Pre-Add जांच स्क्रिप्ट
यहां एक सरल उदाहरण है जो trailing whitespace वाली फाइलों को जोड़ने से रोकता है:

```bash
#!/bin/bash
# .git/hooks/pre-commit (लेकिन staged files पर काम करता है)

# whitespace errors की जांच करें
if git diff --cached --check; then
  exit 0
else
  echo "Found whitespace errors in staged files"
  exit 1
fi
```

किसी भी हुक स्क्रिप्ट को executable बनाना याद रखें (`chmod +x script.sh`).

क्या आप अपने use case के लिए किसी विशेष तरीके पर और विस्तार से जानना चाहेंगे?