---
audio: true
generated: false
image: false
lang: ja
layout: post
title: NYTimesニュース（CN）記事更新トリガー
translated: true
---

以下のボタンをクリックして、[NYTimes CN記事](./notes/2025-03-14-nytimes-en)を更新します。

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes" ></div>

このページでは、NYTimes CN記事の更新をトリガーすることができます。ボタンをクリックすると、最新の記事を取得し、翻訳し、このサイトのコンテンツを更新するワークフローが開始されます。更新をトリガーした後、変更が反映されるまで数分かかる場合がありますのでご注意ください。

Pythonコード:

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
    """Mistral APIを呼び出してテキストを翻訳します。"""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("エラー: MISTRAL_API_KEY環境変数が設定されていません。")
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
        print(f"モデル: {model} でMistral APIを呼び出します")
        print(f"送信するプロンプト: {prompt[:1000]}...")  # プロンプトの最初の1000文字を表示
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral APIの応答: {response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral APIのコンテンツ: {content}")
            return content
        else:
            print(f"Mistral APIエラー: 無効な応答形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral APIエラー: {e}")
        if e.response:
            print(f"応答ステータスコード: {e.response.status_code}")
            print(f"応答コンテンツ: {e.response.text}")
        return None

def fetch_html_content(url):
    """指定されたURLのHTMLコンテンツを取得します。"""
    try:
        # 認証なしのSSLコンテキストを作成
        context = ssl._create_unverified_context()
        print(f"{url} からHTMLコンテンツを取得します")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # 4xxまたは5xxの応答に対してHTTPErrorを発生させる
        print(f"{url} からHTMLコンテンツを正常に取得しました")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"URLを取得できませんでした: {url} - {e}")
        return None

def extract_links(html):
    """cn.nytimes.comのメインページからリンクを抽出します。"""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"メインページから{len(links)}リンクを抽出しました。")
    return links

def translate_title(title):
    """Mistralを使用してタイトルを中国語から英語に翻訳します"""
    base_prompt = "以下のタイトルを{target_language}に翻訳してください。翻訳されたタイトルのみを提供し、追加の説明や注釈は含めないでください。入力テキストを繰り返したり、言及したりしないでください。\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"タイトルを翻訳します: {title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"翻訳されたタイトル: {translated_title}")
        return translated_title
    else:
        raise Exception(f"タイトルの翻訳に失敗しました: {title}")

def summarize_article(html):
    """Mistral APIを使用して記事の内容を英語で要約します。"""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"タイトルを抽出しました: {title}")

    # メインの記事テキストを抽出
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("記事のテキストを抽出できませんでした。")
        return None, None

    # Mistralが要約するためのプロンプトを作成
    prompt = f"以下の記事を英語で要約し、主要なポイントに焦点を当て、導入文句のような「要約:」や「この記事は:」を避けてください。\n\n{article_text[:30000]}\n\n"  # 記事テキストを30000文字に制限
    print(f"タイトル: {title} の要約を作成します")
    summary = call_mistral_api(prompt)

    if summary:
        # 要約を「要約:」や同様のフレーズを削除してクリーンアップ
        summary = summary.replace("Summary:", "").strip()
        print(f"生成された要約: {summary}")
        return title, summary
    else:
        print(f"タイトル: {title} の要約を生成できませんでした")
        return None, None

def generate_markdown_list(articles):
    """記事の要約リストからMarkdownリストを生成します。"""
    if not articles:
        return '* 記事が見つかりませんでした。\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("Markdownリストを生成しました。")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """指定されたコンテンツでMarkdownファイルを更新します。"""
    try:
        # ファイルの既存コンテンツを読み取ります
        print(f"{filename} から既存のコンテンツを読み取ります")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # 初期メタデータの後にコンテンツの開始と終了位置を検索
        start_index = existing_content.find('---', 3) + 4  # 2番目の'---'を見つけてそれを超えて移動
        end_index = len(existing_content)

        # 更新されたコンテンツを構築
        updated_content = existing_content[:start_index].strip() + '\n\n'  # メタデータを保持し、改行を追加
        updated_content += markdown_content.strip() + '\n'  # 新しいMarkdownリストを追加
        # updated_content += existing_content[end_index:].strip() # リストの後に存在する場合は、それを追加

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"{filename} を正常に更新しました")
        markdown_changed = existing_content != updated_content
        print(f"Markdownが変更されました: {markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"{filename} の更新中にエラーが発生しました: {e}")
        return False

def main():
    """Markdownファイルを取得、処理、更新するためのメイン関数。"""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'{nytimes_url} からNYTimesリンクを取得します')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("メインページのコンテンツを取得できませんでした。")
        return

    links = extract_links(html_content)
    print(f'メインページに{len(links)}リンクが見つかりました。リンクを抽出します...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'リンク {i + 1} の {len(links)} を処理します: {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'{link["url"]} からコンテンツを取得できませんでした')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("Markdownファイルが新しいリンクで更新されました。")
        sys.exit(0)
    else:
        print("Markdownファイルは更新されませんでした（変更なし）。")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

フロントエンドコード:

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'NYTimes記事を更新';
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
                alert('更新が正常にトリガーされました！結果を確認するには数分お待ちください。');
            } else {
                alert(`更新に失敗しました。ステータスコード: ${response.status}`);
                console.error('更新に失敗しました:', response);
            }
        })
        .catch(error => {
            alert('更新に失敗しました。エラーを確認するにはコンソールを確認してください。');
            console.error('更新をトリガーする際のエラー:', error);
        });
    });
} else {
    console.error("nytimes divが見つかりません！");
}
```