---
audio: true
generated: false
image: false
lang: fr
layout: post
title: Bot automatisé de résumé d'actualités
translated: true
---

Ce post présente un bot d'actualités en Python qui récupère et résume les principales informations de Hacker News, GitHub Trending et NYTimes (version chinoise) en utilisant l'API Mistral. Il envoie des rapports quotidiens concis via Telegram, avec un workflow GitHub Actions pour une exécution automatisée. Idéal pour rester informé sur l'actualité tech et mondiale sans effort.

```python
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import datetime
import sys
import re
import time

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "610574272")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: TELEGRAM_BOT_API_KEY or TELEGRAM_CHAT_ID not set.")
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    url_pattern = re.compile(r'(https?://[^\s]+)')
    # Supprimer tous les astérisques (pour le gras/italique) du message
    message_no_stars = message.replace('*', '')
    # Supprimer les liens du message
    message_no_links = url_pattern.sub('', message_no_stars)
    messages = []
    msg = message_no_links
    while len(msg) > TELEGRAM_MAX_LENGTH:
        split_idx = msg.rfind('\n', 0, TELEGRAM_MAX_LENGTH)
        if split_idx == -1 or split_idx < TELEGRAM_MAX_LENGTH // 2:
            split_idx = TELEGRAM_MAX_LENGTH
        messages.append(msg[:split_idx])
        msg = msg[split_idx:]
    messages.append(msg)
    success = True
    for part in messages:
        params = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": part,
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            print(f"Message Telegram envoyé avec succès ({len(part)} caractères).")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'envoi du message Telegram : {e}")
            success = False
    return success

def fetch_html_content(url):
    try:
        print(f"Récupération du contenu HTML depuis : {url}")
        response = requests.get(url, timeout=15, verify=False)
        response.raise_for_status()
        print(f"Contenu HTML récupéré avec succès depuis : {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Impossible de récupérer l'URL : {url} - {e}")
        return None

def extract_hacker_news_links(html, max_links=5):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    seen = set()
    for item in soup.select('.titleline > a'):
        url = item['href']
        title = item.text.strip()
        if url.startswith('item?id='):
            url = f"https://news.ycombinator.com/{url}"
        if url not in seen and title:
            links.append({'url': url, 'text': title})
            seen.add(url)
        if len(links) >= max_links:
            break
    print(f"{len(links)} liens extraits de Hacker News.")
    return links

def extract_github_trending(html, max_links=5):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for repo in soup.select('article.Box-row h2 a'):
        url = f"https://github.com{repo['href']}"
        title = re.sub(r'\s+', ' ', repo.text).strip()
        if title and url:
            links.append({'url': url, 'text': title})
        if len(links) >= max_links:
            break
    print(f"{len(links)} dépôts tendances extraits de GitHub.")
    return links

def call_mistral_api(prompt, model="mistral-small-latest"):
    api_key = MISTRAL_API_KEY
    if not api_key:
        print("Erreur : variable d'environnement MISTRAL_API_KEY non définie.")
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
        print(f"Appel de l'API Mistral avec le modèle : {model}")
        print(f"Prompt envoyé : {prompt[:1000]}...")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Réponse de l'API Mistral : {response_json}")
        if response_json and response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Contenu de l'API Mistral : {content}")
            return content
        else:
            print(f"Erreur API Mistral : format de réponse invalide : {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur API Mistral : {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Code statut de la réponse : {e.response.status_code}")
            print(f"Contenu de la réponse : {e.response.text}")
        return None

def fetch_and_summarize(url, fallback_title=None):
    print(f"Résumé de : {url}")
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "Impossible de récupérer le contenu.", "title": fallback_title or url}
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.text.strip() if soup.title else (fallback_title or url)
    paragraphs = soup.find_all('p')
    text_content = "\n".join(p.get_text() for p in paragraphs)
    if not text_content or len(text_content) < 100:
        text_content = soup.get_text(separator="\n")
    text_content = text_content.strip()
    if len(text_content) > 3000:
        text_content = text_content[:3000]
    summary = ai_summarize(text_content, url, title)
    return {"url": url, "summary": summary, "title": title}

def limit_to_n_words(text, n):
    words = text.strip().split()
    if len(words) <= n:
        return text.strip()
    return ' '.join(words[:n]) + "..."

def ai_summarize(text, url=None, title=None):
    if not MISTRAL_API_KEY:
        print("Aucune MISTRAL_API_KEY définie. Retour des 15 premiers mots comme résumé.")
        return limit_to_n_words(text, 15)
    prompt = (
        "Si le texte original est en chinois, résumez-le en anglais. "
        "Résumez le contenu suivant de la page web en anglais clair et concis. "
        "Concentrez-vous sur le point ou l'idée la plus importante. "
        "Votre résumé doit faire environ 300 caractères. "
        "Ne sortez que la phrase de résumé :\n"
        f"Titre : {title if title else ''}\n"
        f"{text}\n"
        f"{'Lien original : ' + url if url else ''}"
    )
    summary = call_mistral_api(prompt)
    if summary is None:
        return limit_to_n_words(text, 15)
    # Tronquer à 300 caractères en dernier recours
    return summary.strip()[:300]

def generate_summarized_report(summaries, source_name):
    text = f"{source_name}\n"
    text += "-" * len(source_name) + "\n"
    if not summaries:
        text += "Aucun élément trouvé.\n\n"
        return text
    url_pattern = re.compile(r'(https?://[^\s]+)')
    for idx, item in enumerate(summaries, 1):
        summary = item.get('summary', '').replace('\n', ' ').replace('\r', ' ').strip()
        summary = summary.replace('*', '')
        summary = url_pattern.sub('', summary)
        # Tronquer chaque résumé à 300 caractères en dernier recours
        summary = summary[:300]
        text += f"{idx}. {summary}\n\n"  # Ajouter un saut de ligne supplémentaire entre les résumés
    text += "\n"
    return text

# --- Intégration NYTimes (m.cn.nytimes.com) ---

def extract_nytimes_links(html, max_links=5):
    """
    Extrait les liens de la page principale de cn.nytimes.com.
    Inclut uniquement les liens commençant par 'https://cn.nytimes.com/'.
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
        if len(links) >= max_links:
            break
    print(f"{len(links)} liens extraits de la page principale.")
    return links

def summarize_nytimes_article(url):
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "Impossible de récupérer le contenu.", "title": url}
    soup = BeautifulSoup(html, 'html.parser')
    # Essayer d'extraire le titre principal de l'article
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else (soup.title.text.strip() if soup.title else url)
    # Extraire le texte principal de l'article
    article_area = soup.find('section', class_='article-body')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = soup.get_text(separator='\n', strip=True)
    if not article_text or len(article_text) < 100:
        article_text = soup.get_text(separator='\n', strip=True)
    if len(article_text) > 3000:
        article_text = article_text[:3000]
    summary = ai_summarize(article_text, url, title)
    return {"url": url, "summary": summary, "title": title}

def main():
    # Vérifier l'argument --test
    is_test = "--test" in sys.argv

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report = f"Résumé quotidien de l'actualité - {today}\n\n"

    if is_test:
        # Ne récupérer qu'un seul lien et envoyer un seul résumé (NYTimes Chinese)
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=1)
            if ny_links:
                link = ny_links[0]
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
        report = generate_summarized_report(ny_summaries, "NYTimes (Chinois)")
        if ny_summaries:
            if send_telegram_message(report):
                print("Résumé de test envoyé à Telegram avec succès.")
                sys.exit(0)
            else:
                print("Échec de l'envoi du résumé de test à Telegram.")
                sys.exit(1)
        else:
            print("Aucune actualité collectée, rien envoyé à Telegram.")
            sys.exit(1)
    else:
        # --- Hacker News ---
        hn_html = fetch_html_content('https://news.ycombinator.com')
        hn_links = []
        hn_summaries = []
        if hn_html:
            hn_links = extract_hacker_news_links(hn_html)
            for link in hn_links:
                summary = fetch_and_summarize(link['url'], fallback_title=link['text'])
                hn_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(hn_summaries, "Hacker News")

        # --- GitHub Trending ---
        gh_html = fetch_html_content('https://github.com/trending')
        gh_links = []
        gh_summaries = []
        if gh_html:
            gh_links = extract_github_trending(gh_html)
            for link in gh_links:
                summary = fetch_and_summarize(link['url'], fallback_title=link['text'])
                gh_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(gh_summaries, "GitHub Trending")

        # --- NYTimes (cn.nytimes.com) ---
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=5)
            for link in ny_links:
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(ny_summaries, "NYTimes (Chinois)")

        if any([hn_summaries, gh_summaries, ny_summaries]):
            if len(report) > TELEGRAM_MAX_LENGTH:
                print(f"Le rapport dépasse {TELEGRAM_MAX_LENGTH} caractères, il sera divisé en plusieurs messages.")
            if send_telegram_message(report):
                print("Rapport d'actualité quotidien envoyé à Telegram avec succès.")
                sys.exit(0)
            else:
                print("Échec de l'envoi du rapport d'actualité quotidien à Telegram.")
                sys.exit(1)
        else:
            print("Aucune actualité collectée, rien envoyé à Telegram.")
            sys.exit(1)

if __name__ == "__main__":
    main()
```

```yml
name: News Bot

on:
  schedule:
    # Exécution tous les jours à 9h heure de Pékin (1h UTC).
    - cron: '0 1 * * *'
  workflow_dispatch:  # Permet un déclenchement manuel
  push:
    # Ne se déclenche que si LES DEUX fichiers changent dans le même commit/push
    # Nécessite un job de filtrage ci-dessous pour vérifier les deux fichiers
    paths:
      - scripts/nytimes/news_bot.py
      - .github/workflows/news.yml

concurrency:
  group: 'news'
  cancel-in-progress: false

jobs:
  send-news:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      MISTRAL_API_KEY: ${{ secrets.MISTRAL_API_KEY }}    

    steps:
      - name: Checkout du dépôt
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configuration de Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: Installation des dépendances
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: Exécution du script news bot
        run: python scripts/nytimes/news_bot.py
              
```