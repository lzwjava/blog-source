---
audio: true
generated: false
image: false
lang: hi
layout: post
title: न्यूज़ आर्टिकल्स अपडेट ट्रिगर
translated: true
type: post
---

नीचे दिए गए बटन पर क्लिक करके [NYTimes CN लेखों](./notes/2025-03-14-nytimes-en) को अपडेट करें।

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes" ></div>

यह पृष्ठ आपको NYTimes CN लेखों को अपडेट करने की अनुमति देता है। बटन पर क्लिक करने से एक वर्कफ़्लो शुरू होगा जो नवीनतम लेखों को प्राप्त करता है, उन्हें अनुवादित करता है, और इस साइट पर सामग्री को अपडेट करता है। कृपया ध्यान दें कि अपडेट ट्रिगर करने के बाद परिवर्तनों को दिखाई देने में कुछ मिनट लग सकते हैं।

Python कोड:

```python
import requests
from bs4 import BeautifulSoup
import os
import ssl
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    """Mistral API को टेक्स्ट अनुवादित करने के लिए कॉल करता है।"""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY पर्यावरण चर नहीं सेट है।")
        return None

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        print(f"Mistral API को मॉडल के साथ कॉल किया जा रहा है: {model}")
        print(f"प्रोम्प्ट भेजा जा रहा है: {prompt[:1000]}...")  # प्रोम्प्ट के पहले 1000 अक्षरों को प्रिंट करें
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral API प्रतिक्रिया: {response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API सामग्री: {content}")
            return content
        else:
            print(f"Mistral API त्रुटि: अमान्य प्रतिक्रिया प्रारूप: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API त्रुटि: {e}")
        if e.response:
            print(f"प्रतिक्रिया स्थिति कोड: {e.response.status_code}")
            print(f"प्रतिक्रिया सामग्री: {e.response.text}")
        return None

def fetch_html_content(url):
    """एक दिए गए URL से HTML सामग्री प्राप्त करता है।"""
    try:
        # एक अनवेरिफाइड SSL कॉन्टेक्स्ट बनाएं
        context = ssl._create_unverified_context()
        print(f"HTML सामग्री प्राप्त की जा रही है: {url}")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # बुरे प्रतिक्रियाओं (4xx या 5xx) के लिए HTTPError उठाएं
        print(f"HTML सामग्री सफलतापूर्वक प्राप्त की गई: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"URL प्राप्त नहीं किया जा सका: {url} - {e}")
        return None

def extract_links(html):
    """cn.nytimes.com के मुख्य पृष्ठ से लिंक निकालता है।"""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"मुख्य पृष्ठ से {len(links)} लिंक निकाले गए।")
    return links

def translate_title(title):
    """Mistral का उपयोग करके चीनी से अंग्रेजी में शीर्षक अनुवादित करता है"""
    base_prompt = "निम्नलिखित शीर्षक को {target_language} में अनुवादित करें। केवल अनुवादित शीर्षक प्रदान करें, बिना किसी अतिरिक्त नोट्स या व्याख्याओं के। इनपुट टेक्स्ट को दोहराएं या उल्लेख न करें।\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"शीर्षक अनुवादित किया जा रहा है: {title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"अनुवादित शीर्षक: {translated_title}")
        return translated_title
    else:
        raise Exception(f"शीर्षक अनुवादित नहीं किया जा सका: {title}")

def summarize_article(html):
    """Mistral API का उपयोग करके अंग्रेजी में लेख सामग्री का सारांश बनाता है।"""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"शीर्षक निकाला गया: {title}")

    # मुख्य लेख टेक्स्ट निकालें
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("लेख टेक्स्ट निकाल नहीं सका।")
        return None, None

    # Mistral के लिए सारांश बनाने के लिए एक प्रोम्प्ट बनाएं
    prompt = f"निम्नलिखित लेख का अंग्रेजी में सारांश बनाएं, मुख्य बिंदुओं पर ध्यान केंद्रित करते हुए और 'Summary:' या 'This article is about:' जैसे परिचयात्मक वाक्यों से बचें।\n\n{article_text[:30000]}\n\n"  # लेख टेक्स्ट को 30000 अक्षरों तक सीमित करें
    print(f"शीर्षक के लिए सारांश बनाया जा रहा है: {title}")
    summary = call_mistral_api(prompt)

    if summary:
        # सारांश को 'Summary:' या समान वाक्यों को हटाकर साफ करें
        summary = summary.replace("Summary:", "").strip()
        print(f"सारांश बनाया गया: {summary}")
        return title, summary
    else:
        print(f"शीर्षक के लिए सारांश बनाना विफल रहा: {title}")
        return None, None

def generate_markdown_list(articles):
    """एक लेख सारांशों की सूची से एक Markdown सूची बनाता है।"""
    if not articles:
        return '* कोई लेख नहीं मिला।\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("Markdown सूची बनाई गई।")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """दिए गए सामग्री के साथ एक Markdown फ़ाइल को अपडेट करता है।"""
    try:
        # फ़ाइल के मौजूदा सामग्री को पढ़ें
        print(f"{filename} से मौजूदा सामग्री पढ़ी जा रही है")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # प्रारंभिक मेटाडेटा के बाद सामग्री के शुरू और अंत के स्थानों को ढूँढें
        start_index = existing_content.find('---', 3) + 4  # दूसरे '---' को ढूँढें और उसके आगे बढ़ें
        end_index = len(existing_content)

        # अपडेटेड सामग्री का निर्माण करें
        updated_content = existing_content[:start_index].strip() + '\n\n'  # मेटाडेटा को रखें और एक नया लाइन जोड़ें
        updated_content += markdown_content.strip() + '\n'  # नई मार्कडाउन सूची जोड़ें
        # updated_content += existing_content[end_index:].strip() # अगर सूची के बाद कुछ भी मौजूद है, तो उसे जोड़ें

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"{filename} सफलतापूर्वक अपडेट किया गया")
        markdown_changed = existing_content != updated_content
        print(f"Markdown बदल गया: {markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"{filename} अपडेट करने में त्रुटि: {e}")
        return False

def main():
    """Markdown फ़ाइल को प्राप्त, प्रोसेस और अपडेट करने के लिए मुख्य फ़ंक्शन।"""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'NYTimes लिंक प्राप्त किए जा रहे हैं: {nytimes_url}')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("मुख्य पृष्ठ सामग्री प्राप्त नहीं की जा सकी।")
        return

    links = extract_links(html_content)
    print(f'मुख्य पृष्ठ पर {len(links)} लिंक मिले। लिंक निकाल रहे हैं...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'लिंक {i + 1} को प्रोसेस किया जा रहा है {len(links)}: {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'{link["url"]} से सामग्री प्राप्त नहीं की जा सकी')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("Markdown फ़ाइल नई लिंक के साथ अपडेट की गई।")
        sys.exit(0)
    else:
        print("Markdown फ़ाइल अपडेट नहीं की गई (कोई परिवर्तन नहीं)।")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

फ्रंटएंड कोड:

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'NYTimes लेख अपडेट करें';
    nytimesDiv.appendChild(updateButton);

    updateButton.addEventListener('click', () => {
        fetch('https://api.github.com/repos/lzwjava/lzwjava.github.io/actions/workflows/nytimes.yml/dispatches', {
            method: 'POST',
            headers: {
                'Accept': 'application/vnd.github+json',
                'Authorization': 'Bearer token',
                'X-GitHub-Api-Version': '2022-11-28',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ref: 'main' })
        })
        .then(response => {
            if (response.status === 204) {
                alert('अपडेट सफलतापूर्वक ट्रिगर किया गया! परिणाम देखने के लिए कुछ मिनट प्रतीक्षा करें।');
            } else {
                alert(`अपडेट विफल रहा। स्थिति कोड: ${response.status}`);
                console.error('अपडेट विफल रहा:', response);
            }
        })
        .catch(error => {
            alert('अपडेट विफल रहा। त्रुटियों के लिए कंसोल देखें।');
            console.error('अपडेट ट्रिगर करने में त्रुटि:', error);
        });
    });
} else {
    console.error("nytimes div नहीं मिला!");
}
```