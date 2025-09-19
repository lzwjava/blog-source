---
audio: false
generated: false
image: false
lang: hi
layout: post
title: एआई-सक्षम गिट कमिट संदेश
translated: true
---

यह पायथन स्क्रिप्ट को आपके सिस्टम के PATH में शामिल किए गए किसी डायरेक्टरी में रखा जाना चाहिए, जैसे कि `~/bin`.

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse
import requests

load_dotenv()

def call_mistral_api(prompt):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("त्रुटि: MISTRAL_API_KEY पर्यावरण चर सेट नहीं है।")
        return None

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "mistral-large-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and response_json['choices']:
            return response_json['choices'][0]['message']['content']
        else:
            print(f"Mistral API त्रुटि: अमान्य प्रतिक्रिया फॉर्मेट: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API त्रुटि: {e}")
        if e.response:
            print(f"प्रतिक्रिया स्टेटस कोड: {e.response.status_code}")
            print(f"प्रतिक्रिया कंटेंट: {e.response.text}")
        return None

def call_gemini_api(prompt):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("त्रुटि: GEMINI_API_KEY पर्यावरण चर सेट नहीं है।")
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload, params=params)
        response.raise_for_status()  # खराब स्टेटस कोड के लिए एक अपवाद उठाएं
        response_json = response.json()
        if response_json and 'candidates' in response_json and response_json['candidates']:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"Gemini API त्रुटि: अमान्य प्रतिक्रिया फॉर्मेट: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Gemini API त्रुटि: {e}")
        if e.response:
            print(f"प्रतिक्रिया स्टेटस कोड: {e.response.status_code}")
            print(f"प्रतिक्रिया कंटेंट: {e.response.text}")
        return None

def call_deepseek_api(prompt):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("त्रुटि: DEEPSEEK_API_KEY पर्यावरण चर सेट नहीं है।")
        return None

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
            return commit_message
        else:
            print("त्रुटि: API से कोई प्रतिक्रिया नहीं।")
            return None
    except Exception as e:
        print(f"API कॉल के दौरान त्रुटि: {e}")
        print(e)
        return None

def gitmessageai(push=True, only_message=False, api='deepseek'):
    # सभी बदलावों को स्टेज करें
    subprocess.run(["git", "add", "-A"], check=True)

    # बदलावों का एक संक्षिप्त सारांश प्राप्त करें
    files_process = subprocess.run(["git", "diff", "--staged", "--name-only"], capture_output=True, text=True, check=True)
    changed_files = files_process.stdout

    if not changed_files:
        print("कोई बदलाव कमिट करने के लिए नहीं।")
        return

    # AI के लिए प्रॉम्प्ट तैयार करें
    prompt = f"""
Generate a concise commit message in Conventional Commits format for the following code changes.
Use one of the following types: feat, fix, docs, style, refactor, test, chore, perf, ci, build, or revert.
If applicable, include a scope in parentheses to describe the part of the codebase affected.
The commit message should not exceed 70 characters.

Changed files:
{changed_files}

Commit message:
"""

    if api == 'deepseek':
        commit_message = call_deepseek_api(prompt)
        if not commit_message:
            return
    elif api == 'gemini':
        commit_message = call_gemini_api(prompt)
        if not commit_message:
            print("त्रुटि: Gemini API से कोई प्रतिक्रिया नहीं।")
            return
    elif api == 'mistral':
        commit_message = call_mistral_api(prompt)
        if not commit_message:
            print("त्रुटि: Mistral API से कोई प्रतिक्रिया नहीं।")
            return
    else:
        print(f"त्रुटि: अमान्य API निर्दिष्ट किया गया: {api}")
        return

    # यह देखें कि कमिट संदेश खाली है या नहीं
    if not commit_message:
        print("त्रुटि: खाली कमिट संदेश पैदा हुआ। कमिट को रद्द कर रहा है।")
        return

    if only_message:
        print(f"सुझाया गया कमिट संदेश: {commit_message}")
        return

    # जेनरेट किए गए संदेश के साथ कमिट करें
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # बदलावों को पुश करें
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("बदलाव स्थानीय रूप से कमिट किए गए, लेकिन पुश नहीं किए गए।")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI के साथ कमिट संदेश जेनरेट करें और बदलावों को कमिट करें।")
    parser.add_argument('--no-push', dest='push', action='store_false', help='पुश किए बिना बदलावों को स्थानीय रूप से कमिट करें।')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='केवल AI द्वारा जेनरेट किया गया कमिट संदेश प्रिंट करें।')
    parser.add_argument('--api', type=str, default='deepseek', choices=['deepseek', 'gemini', 'mistral'], help='कमिट संदेश जेनरेशन के लिए उपयोग की जाने वाली API (deepseek, gemini, या mistral)।')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api)
```

इस स्क्रिप्ट को अलग-अलग API के साथ कॉल किया जा सकता है। उदाहरण के लिए:

```bash
python ~/bin/gitmessageai.py
python ~/bin/gitmessageai.py --no-push
python ~/bin/gitmessageai.py --only-message
python ~/bin/gitmessageai.py --api gemini
python ~/bin/gitmessageai.py --api mistral --no-push
python ~/bin/gitmessageai.py --api deepseek --only-message
```

फिर, अपनी `~/.zprofile` फ़ाइल में निम्नलिखित जोड़ें:

```bash
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

कई सुधार हैं।

* एक यह है कि केवल फ़ाइल नाम बदलाव भेजें, और `git diff` का उपयोग करके फ़ाइल के विस्तृत बदलावों को न पढ़ें। हम AI सेवा API को ज्यादा विवरण नहीं देना चाहते। इस मामले में, हमें इसकी ज़रूरत नहीं है, क्योंकि कमिट संदेशों को कई लोग ध्यान से नहीं पढ़ते हैं।

* कभी-कभी, Deepseek API विफल हो सकता है, क्योंकि यह हाल ही में बहुत लोकप्रिय है। हमें इसके बजाय Gemini का उपयोग करना पड़ सकता है।