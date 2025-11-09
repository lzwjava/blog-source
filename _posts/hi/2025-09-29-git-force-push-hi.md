---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: शाखा विलोपन के माध्यम से गिट फोर्स पुश
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
git_force_push.py

यह स्क्रिप्ट पहले रिमोट ब्रांच को डिलीट करके, फिर लोकल ब्रांच को पुश करके एक "फोर्स पुश" करती है।
यह तब काम करता है जब रिपॉजिटरी ब्रांच डिलीशन की अनुमति देती है लेकिन फोर्स पुश की नहीं।

Usage: python git_force_push.py <remote> <branch>
Example: python git_force_push.py origin main

Note: यह मानता है कि आपके पास पर्याप्त अनुमतियां हैं और डिलीशन की अनुमति है।
सावधान रहें, क्योंकि ब्रांच डिलीट करने से कमिट्स खो सकती हैं।
"""

import subprocess
import sys

def run_command(command):
    """एक शेल कमांड चलाएं और उसका आउटपुट लौटाएं।"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"कमांड '{command}' चलाने में त्रुटि: {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python git_force_push.py <remote> <branch>")
        sys.exit(1)

    remote = sys.argv[1]
    branch = sys.argv[2]

    # रिमोट ब्रांच को डिलीट करें
    delete_cmd = f"git push {remote} :{branch}"
    print(f"रिमोट ब्रांच डिलीट की जा रही है: {delete_cmd}")
    run_command(delete_cmd)

    # लोकल ब्रांच को पुश करें
    push_cmd = f"git push {remote} {branch}"
    print(f"लोकल ब्रांच पुश की जा रही है: {push_cmd}")
    run_command(push_cmd)

    print("फोर्स पुश सफलतापूर्वक पूरा हुआ।")
```

### यह कैसे काम करता है
- **डिलीशन स्टेप**: `git push origin :main` चलाकर रिमोट ब्रांच को डिलीट करता है (जैसा कि आपकी रिपो में अनुमति है)।
- **पुश स्टेप**: `git push origin main` चलाकर लोकल ब्रांच को पुश करता है, जिससे रिमोट पर इसे नए सिरे से बनाया जाता है।
- यह रिमोट हिस्ट्री को छोड़कर और उसे लोकल हिस्ट्री से बदलकर प्रभावी रूप से एक फोर्स पुश हासिल करता है।
- **सुरक्षा/उपयोग नोट्स**: पहले एक गैर-महत्वपूर्ण रिपो में टेस्ट करें। इसके लिए उचित Git सेटअप और अनुमतियों की आवश्यकता होती है। यदि रिपो में अतिरिक्त सुरक्षा है (जैसे, hooks के माध्यम से), तो यह फेल हो सकता है। कोई वारंटी नहीं; Git ऑपरेशन विनाशकारी हो सकते हैं।