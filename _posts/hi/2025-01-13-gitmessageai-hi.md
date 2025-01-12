---
audio: true
lang: hi
layout: post
title: AI-संचालित Git कमिट संदेश
translated: true
---

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

def gitmessageai(push=True):
    """
    स्टेज्ड परिवर्तनों के आधार पर AI का उपयोग करके एक कमिट संदेश उत्पन्न करता है और उन्हें कमिट करता है।

    Args:
        push (bool, optional): कमिट करने के बाद परिवर्तनों को पुश करना है या नहीं। डिफ़ॉल्ट रूप से True।
    """
    # सभी परिवर्तनों को स्टेज करें
    subprocess.run(["git", "add", "-A"], check=True)

    # स्टेज्ड परिवर्तनों का डिफ प्राप्त करें
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

    # DeepSeek API को प्रॉम्प्ट भेजें
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

    # डिबग: API प्रतिक्रिया प्रिंट करें
    print(f"API प्रतिक्रिया: {response}")


    # जांचें कि कमिट संदेश खाली तो नहीं है
    if not commit_message:
        print("त्रुटि: खाली कमिट संदेश उत्पन्न हुआ। कमिट रद्द कर दिया गया है।")
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
    args = parser.parse_args()
    gitmessageai(push=args.push)
```

फिर, अपने `~/.zprofile` फ़ाइल में, निम्नलिखित जोड़ें:

```
function gitpush {
  python ~/bin/gitmessageai.py
}

function gitcommit {
  python ~/bin/gitmessageai.py --no-push
}

alias gpa=gitpush
alias gca=gitcommit
```