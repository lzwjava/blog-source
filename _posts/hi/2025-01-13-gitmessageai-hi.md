---
audio: true
lang: hi
layout: post
title: AI-संचालित Git कमिट संदेश
translated: true
---

यह पायथन स्क्रिप्ट आपके सिस्टम के PATH में शामिल एक डायरेक्टरी में रखी जानी चाहिए, जैसे कि `~/bin`।

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

def gitmessageai(push=True, only_message=False):
    # सभी परिवर्तनों को स्टेज करें
    subprocess.run(["git", "add", "-A"], check=True)

    # स्टेज किए गए परिवर्तनों का डिफ प्राप्त करें
    diff_process = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True, check=True)
    diff = diff_process.stdout

    if not diff:
        print("कमिट करने के लिए कोई परिवर्तन नहीं हैं।")
        return

    # AI के लिए प्रॉम्प्ट तैयार करें
    prompt = f"""
निम्नलिखित कोड परिवर्तनों के लिए Conventional Commits प्रारूप में एक संक्षिप्त कमिट संदेश उत्पन्न करें।
निम्नलिखित प्रकारों में से एक का उपयोग करें: feat, fix, docs, style, refactor, test, chore, perf, ci, build, या revert।
यदि लागू हो, तो कोडबेस के प्रभावित हिस्से का वर्णन करने के लिए कोष्ठक में एक स्कोप शामिल करें।
कमिट संदेश 70 वर्णों से अधिक नहीं होना चाहिए।

कोड परिवर्तन:
{diff}

कमिट संदेश:
"""    

    # प्रॉम्प्ट को DeepSeek API पर भेजें
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("त्रुटि: DEEPSEEK_API_KEY पर्यावरण चर सेट नहीं है।")
        return
    
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        if response and response.choices:
            commit_message = response.choices[0].message.content.strip()
            commit_message = commit_message.replace('`', '')
        else:
            print("त्रुटि: API से कोई प्रतिक्रिया नहीं मिली।")
            return
    except Exception as e:
        print(f"API कॉल के दौरान त्रुटि: {e}")
        return

    # जांचें कि कमिट संदेश खाली तो नहीं है
    if not commit_message:
        print("त्रुटि: खाली कमिट संदेश उत्पन्न हुआ। कमिट रद्द किया जा रहा है।")
        return
    
    if only_message:
        print(f"सुझाया गया कमिट संदेश: {commit_message}")
        return

    # उत्पन्न संदेश के साथ कमिट करें
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # परिवर्तनों को पुश करें
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("परिवर्तन स्थानीय रूप से कमिट किए गए हैं, लेकिन पुश नहीं किए गए हैं।")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI के साथ कमिट संदेश उत्पन्न करें और परिवर्तनों को कमिट करें।")
    parser.add_argument('--no-push', dest='push', action='store_false', help='परिवर्तनों को स्थानीय रूप से कमिट करें बिना पुश किए।')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='केवल AI द्वारा उत्पन्न कमिट संदेश प्रिंट करें।')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message)
```

फिर, अपने `~/.zprofile` फ़ाइल में निम्नलिखित जोड़ें:

```
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

AI अन्य चीजों में भी मदद कर सकता है जैसे कि मर्ज कमिट संदेश उत्पन्न करना।