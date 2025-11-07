---
audio: true
generated: false
image: false
lang: de
layout: post
title: Automatisierter Nachrichtenzusammenfassungs-Bot
translated: true
type: post
---

Dieser Beitrag präsentiert einen Python-basierten News-Bot, der Top-Stories von Hacker News, GitHub Trending und NYTimes (Chinesisch) mithilfe der Mistral-API extrahiert und zusammenfasst. Er sendet täglich kompakte Berichte über Telegram, unterstützt durch einen GitHub Actions-Workflow für die automatisierte Ausführung. Ideal, um mühelos über Tech- und globale Nachrichten auf dem Laufenden zu bleiben.

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
    # Entferne alle Sternchen (für Fett/Kursiv) aus der Nachricht
    message_no_stars = message.replace('*', '')
    # Entferne Links aus der Nachricht
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
            print(f"Telegram-Nachrichtenteil erfolgreich gesendet ({len(part)} Zeichen).")
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Senden der Telegram-Nachricht: {e}")
            success = False
    return success

def fetch_html_content(url):
    try:
        print(f"HTML-Inhalt wird abgerufen von: {url}")
        response = requests.get(url, timeout=15, verify=False)
        response.raise_for_status()
        print(f"HTML-Inhalt erfolgreich abgerufen von: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"URL konnte nicht abgerufen werden: {url} - {e}")
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
    print(f"{len(links)} Links von Hacker News extrahiert.")
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
    print(f"{len(links)} trendige Repositories von GitHub extrahiert.")
    return links

def call_mistral_api(prompt, model="mistral-small-latest"):
    api_key = MISTRAL_API_KEY
    if not api_key:
        print("Fehler: MISTRAL_API_KEY Umgebungsvariable nicht gesetzt.")
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
        print(f"Mistral-API wird aufgerufen mit Modell: {model}")
        print(f"Gesendeter Prompt: {prompt[:1000]}...")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral-API-Antwort: {response_json}")
        if response_json and response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral-API-Inhalt: {content}")
            return content
        else:
            print(f"Mistral-API-Fehler: Ungültiges Antwortformat: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral-API-Fehler: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Antwortstatuscode: {e.response.status_code}")
            print(f"Antwortinhalt: {e.response.text}")
        return None

def fetch_and_summarize(url, fallback_title=None):
    print(f"Zusammenfassung wird erstellt für: {url}")
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "Inhalt konnte nicht abgerufen werden.", "title": fallback_title or url}
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
        print("Kein MISTRAL_API_KEY gesetzt. Erste 15 Wörter werden als Zusammenfassung zurückgegeben.")
        return limit_to_n_words(text, 15)
    prompt = (
        "Wenn der Originaltext auf Chinesisch ist, fasse ihn auf Englisch zusammen. "
        "Fasse den folgenden Webseiteninhalt in klarem, prägnantem Englisch zusammen. "
        "Konzentriere dich auf den wichtigsten Punkt oder die wichtigste Erkenntnis. "
        "Deine Zusammenfassung sollte etwa 300 Zeichen umfassen. "
        "Gib nur den Zusammenfassungssatz aus:\n"
        f"Titel: {title if title else ''}\n"
        f"{text}\n"
        f"{'Original-Link: ' + url if url else ''}"
    )
    summary = call_mistral_api(prompt)
    if summary is None:
        return limit_to_n_words(text, 15)
    # Kürze auf 300 Zeichen als letzten Ausweg
    return summary.strip()[:300]

def generate_summarized_report(summaries, source_name):
    text = f"{source_name}\n"
    text += "-" * len(source_name) + "\n"
    if not summaries:
        text += "Keine Einträge gefunden.\n\n"
        return text
    url_pattern = re.compile(r'(https?://[^\s]+)')
    for idx, item in enumerate(summaries, 1):
        summary = item.get('summary', '').replace('\n', ' ').replace('\r', ').strip()
        summary = summary.replace('*', '')
        summary = url_pattern.sub('', summary)
        # Kürze jede Zusammenfassung auf 300 Zeichen als letzten Ausweg
        summary = summary[:300]
        text += f"{idx}. {summary}\n\n"  # Füge eine zusätzliche Leerzeile zwischen den Zusammenfassungen ein
    text += "\n"
    return text

# --- NYTimes (m.cn.nytimes.com) Integration ---

def extract_nytimes_links(html, max_links=5):
    """
    Extrahiert Links von der Hauptseite von cn.nytimes.com.
    Beinhaltet nur Links, die mit 'https://cn.nytimes.com/' beginnen.
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
    print(f"{len(links)} Links von der Hauptseite extrahiert.")
    return links

def summarize_nytimes_article(url):
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "Inhalt konnte nicht abgerufen werden.", "title": url}
    soup = BeautifulSoup(html, 'html.parser')
    # Versuche, den Hauptartikeltitel zu extrahieren
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else (soup.title.text.strip() if soup.title else url)
    # Extrahiere den Hauptartikeltext
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
    # Prüfe auf --test Argument
    is_test = "--test" in sys.argv

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report = f"Tägliche Nachrichtenzusammenfassung - {today}\n\n"

    if is_test:
        # Extrahiere nur einen Link und sende eine Zusammenfassung (NYTimes Chinesisch)
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=1)
            if ny_links:
                link = ny_links[0]
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
        report = generate_summarized_report(ny_summaries, "NYTimes (Chinesisch)")
        if ny_summaries:
            if send_telegram_message(report):
                print("Testzusammenfassung erfolgreich an Telegram gesendet.")
                sys.exit(0)
            else:
                print("Testzusammenfassung konnte nicht an Telegram gesendet werden.")
                sys.exit(1)
        else:
            print("Keine Nachrichten gesammelt, nichts an Telegram gesendet.")
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
        report += generate_summarized_report(ny_summaries, "NYTimes (Chinesisch)")

        if any([hn_summaries, gh_summaries, ny_summaries]):
            if len(report) > TELEGRAM_MAX_LENGTH:
                print(f"Bericht überschreitet {TELEGRAM_MAX_LENGTH} Zeichen, wird in mehrere Nachrichten aufgeteilt.")
            if send_telegram_message(report):
                print("Täglicher Nachrichtenbericht erfolgreich an Telegram gesendet.")
                sys.exit(0)
            else:
                print("Täglicher Nachrichtenbericht konnte nicht an Telegram gesendet werden.")
                sys.exit(1)
        else:
            print("Keine Nachrichten gesammelt, nichts an Telegram gesendet.")
            sys.exit(1)

if __name__ == "__main__":
    main()
```

```yml
name: News Bot

on:
  schedule:
    # Läuft täglich um 9 Uhr Pekinger Zeit (1 Uhr UTC).
    - cron: '0 1 * * *'
  workflow_dispatch:  # Ermöglicht manuelle Auslösung
  push:
    # Wird nur ausgelöst, wenn BEIDE Dateien im selben Commit/Push geändert werden
    # Erfordert einen Filter-Job unten, um beide Dateien zu prüfen
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
      - name: Repository auschecken
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.10.x einrichten
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: Abhängigkeiten installieren
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: News-Bot-Skript ausführen
        run: python scripts/nytimes/news_bot.py
              
```