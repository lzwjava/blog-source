---
audio: true
generated: false
image: false
lang: ar
layout: post
title: NYTimes أخبار (CN) تحديث مقالات تحفيز
translated: true
type: post
---

انقر على الزر أدناه لتحديث مقالات [NYTimes CN](./notes/2025-03-14-nytimes-en).

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes" ></div>

تتيح هذه الصفحة لك بدء تحديث لمقالات NYTimes CN. انقر على الزر لبدء سير عمل يجذب أحدث المقالات، يترجمها، ويحدث المحتوى على هذا الموقع. يرجى ملاحظة أنه قد يستغرق بعض الوقت حتى تظهر التغييرات بعد بدء التحديث.

كود Python:

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
    """يدعو API Mistral لترجمة النص."""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("خطأ: لم يتم تعيين متغير بيئة MISTRAL_API_KEY.")
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
        print(f"يدعو API Mistral مع النموذج: {model}")
        print(f"الاستعلام المرسل: {prompt[:1000]}...")  # طباعة 1000 حرف أولية من الاستعلام
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"إجابة API Mistral: {response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"محتوى API Mistral: {content}")
            return content
        else:
            print(f"خطأ API Mistral: تنسيق الإجابة غير صالح: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ API Mistral: {e}")
        if e.response:
            print(f"رمز حالة الإجابة: {e.response.status_code}")
            print(f"محتوى الإجابة: {e.response.text}")
        return None

def fetch_html_content(url):
    """يجذب محتوى HTML لموقع URL معين."""
    try:
        # إنشاء سياق SSL غير مصادق
        context = ssl._create_unverified_context()
        print(f"يجذب محتوى HTML من: {url}")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # رفع خطأ HTTP للردود السيئة (4xx أو 5xx)
        print(f"تم جلب محتوى HTML بنجاح من: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"لم يتم جلب URL: {url} - {e}")
        return None

def extract_links(html):
    """يستخرج الروابط من الصفحة الرئيسية لموقع cn.nytimes.com."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"تم استخراج {len(links)} روابط من الصفحة الرئيسية.")
    return links

def translate_title(title):
    """ترجمة العنوان من الصينية إلى الإنجليزية باستخدام Mistral"""
    base_prompt = "ترجم العنوان التالي إلى {target_language}. قدم فقط العنوان المترجم، دون أي ملاحظات أو تفسيرات إضافية. لا تكرر أو تذكر النص المدخل.\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"ترجمة العنوان: {title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"العنوان المترجم: {translated_title}")
        return translated_title
    else:
        raise Exception(f"فشل في ترجمة العنوان: {title}")

def summarize_article(html):
    """يختصر محتوى المقال باستخدام API Mistral باللغة الإنجليزية."""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"تم استخراج العنوان: {title}")

    # استخراج نص المقال الرئيسي
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("لم يتم استخراج نص المقال.")
        return None, None

    # إنشاء استعلام لـ Mistral لاختصار
    prompt = f"اختصر المقال التالي باللغة الإنجليزية، مع التركيز على النقاط الرئيسية وتجنب الجمل التمهيدية مثل 'ملخص:' أو 'هذا المقال عن:'.\n\n{article_text[:30000]}\n\n"  # حد نص المقال إلى 30000 حرف
    print(f"إنشاء ملخص للعنوان: {title}")
    summary = call_mistral_api(prompt)

    if summary:
        # تنظيف الملخص عن طريق إزالة "ملخص:" أو جمل مماثلة في البداية
        summary = summary.replace("Summary:", "").strip()
        print(f"تم إنشاء الملخص: {summary}")
        return title, summary
    else:
        print(f"فشل في إنشاء ملخص للعنوان: {title}")
        return None, None

def generate_markdown_list(articles):
    """يولد قائمة Markdown من قائمة ملخصات المقالات."""
    if not articles:
        return '* لم يتم العثور على مقالات.\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("تم إنشاء قائمة Markdown.")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """يحدث ملف Markdown بالمحتوى المقدم."""
    try:
        # قراءة المحتوى الحالي للملف
        print(f"قراءة المحتوى الحالي من {filename}")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # العثور على مواقع البداية والنهاية للمحتوى بعد البيانات الأولية
        start_index = existing_content.find('---', 3) + 4  # العثور على '---' الثاني وتجاوزه
        end_index = len(existing_content)

        # بناء المحتوى المحدث
        updated_content = existing_content[:start_index].strip() + '\n\n'  # الحفاظ على البيانات وإضافة سطر جديد
        updated_content += markdown_content.strip() + '\n'  # إضافة القائمة الجديدة Markdown
        # updated_content += existing_content[end_index:].strip() # إضافة أي شيء بعد القائمة، إذا كان موجودًا

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"تم تحديث {filename} بنجاح")
        markdown_changed = existing_content != updated_content
        print(f"تم تغيير Markdown: {markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"خطأ في تحديث {filename}: {e}")
        return False

def main():
    """دالة رئيسية لجلب، معالجة، وتحديث ملف Markdown."""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'جلب روابط NYTimes من: {nytimes_url}')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("فشل في جلب محتوى الصفحة الرئيسية.")
        return

    links = extract_links(html_content)
    print(f'تم العثور على {len(links)} روابط على الصفحة الرئيسية. استخراج الروابط...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'معالجة الرابط {i + 1} من {len(links)}: {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'فشل في جلب المحتوى من {link["url"]}')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("تم تحديث ملف Markdown بالروابط الجديدة.")
        sys.exit(0)
    else:
        print("لم يتم تحديث ملف Markdown (لا توجد تغييرات).")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

كود الواجهة الأمامية:

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'تحديث مقالات NYTimes';
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
                alert('تم بدء التحديث بنجاح! يرجى الانتظار بعض الوقت لرؤية النتيجة.');
            } else {
                alert(`فشل التحديث. رمز الحالة: ${response.status}`);
                console.error('فشل التحديث:', response);
            }
        })
        .catch(error => {
            alert('فشل التحديث. تحقق من سجل الأخطاء في الواجهة الأمامية.');
            console.error('خطأ في بدء التحديث:', error);
        });
    });
} else {
    console.error("لم يتم العثور على قسم nytimes!");
}
```