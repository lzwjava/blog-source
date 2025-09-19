---
audio: true
generated: true
image: false
lang: de
layout: post
title: NYTimes Nachrichten (CN) Artikelaktualisierung Auslöser
translated: true
---

Klicken Sie auf die Schaltfläche unten, um die [NYTimes CN Artikel](./nytimes-en) zu aktualisieren.

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes"></div>

Diese Seite ermöglicht es Ihnen, eine Aktualisierung der NYTimes CN Artikel auszulösen. Durch Klicken auf die Schaltfläche wird ein Workflow gestartet, der die neuesten Artikel abruft, sie übersetzt und den Inhalt auf dieser Website aktualisiert. Bitte beachten Sie, dass es einige Minuten dauern kann, bis die Änderungen nach dem Auslösen der Aktualisierung sichtbar werden.

Python-Code:

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
    """Ruft die Mistral-API auf, um Text zu übersetzen."""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Fehler: Die Umgebungsvariable MISTRAL_API_KEY ist nicht gesetzt.")
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
        print(f"Mistral-API mit Modell aufrufen: {model}")
        print(f"Gesendete Eingabeaufforderung: {prompt[:1000]}...")  # Die ersten 1000 Zeichen der Eingabeaufforderung ausgeben
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral-API-Antwort: {response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral-API-Inhalt: {content}")
            return content
        else:
            print(f"Mistral-API-Fehler: Ungültiges Antwortformat: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral-API-Fehler: {e}")
        if e.response:
            print(f"Statuscode der Antwort: {e.response.status_code}")
            print(f"Inhalt der Antwort: {e.response.text}")
        return None

def fetch_html_content(url):
    """Holt den HTML-Inhalt einer bestimmten URL."""
    try:
        # Erstellen eines unverifizierten SSL-Kontexts
        context = ssl._create_unverified_context()
        print(f"HTML-Inhalt von abrufen: {url}")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # HTTPError für schlechte Antworten (4xx oder 5xx) auslösen
        print(f"HTML-Inhalt erfolgreich von abgerufen: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"URL konnte nicht abgerufen werden: {url} - {e}")
        return None

def extract_links(html):
    """Extrahiert Links von der Hauptseite von cn.nytimes.com."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"{len(links)} Links von der Hauptseite extrahiert.")
    return links

def translate_title(title):
    """Übersetzt den Titel von Chinesisch in Englisch mit Mistral."""
    base_prompt = "Übersetzen Sie den folgenden Titel in {target_language}. Geben Sie nur den übersetzten Titel an, ohne zusätzliche Hinweise oder Erklärungen. Wiederholen oder erwähnen Sie den Eingabetext nicht.\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"Titel übersetzen: {title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"Übersetzter Titel: {translated_title}")
        return translated_title
    else:
        raise Exception(f"Titelübersetzung fehlgeschlagen: {title}")

def summarize_article(html):
    """Zusammenfassung des Artikelinhalts mit der Mistral-API auf Englisch."""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"Titel extrahiert: {title}")

    # Hauptartikeltext extrahieren
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("Artikeltext konnte nicht extrahiert werden.")
        return None, None

    # Erstellen einer Eingabeaufforderung für Mistral, um zusammenzufassen
    prompt = f"Fassen Sie den folgenden Artikel in Englisch zusammen, indem Sie sich auf die Hauptpunkte konzentrieren und einleitende Phrasen wie 'Zusammenfassung:' oder 'Dieser Artikel handelt von:' vermeiden.\n\n{article_text[:30000]}\n\n"  # Artikeltext auf 30000 Zeichen begrenzen
    print(f"Zusammenfassung für Titel erstellen: {title}")
    summary = call_mistral_api(prompt)

    if summary:
        # Zusammenfassung bereinigen, indem führende "Zusammenfassung:" oder ähnliche Phrasen entfernt werden
        summary = summary.replace("Zusammenfassung:", "").strip()
        print(f"Erstellte Zusammenfassung: {summary}")
        return title, summary
    else:
        print(f"Zusammenfassung für Titel konnte nicht erstellt werden: {title}")
        return None, None

def generate_markdown_list(articles):
    """Erstellt eine Markdown-Liste aus einer Liste von Artikelzusammenfassungen."""
    if not articles:
        return '* Keine Artikel gefunden.\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("Markdown-Liste erstellt.")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """Aktualisiert eine Markdown-Datei mit dem angegebenen Inhalt."""
    try:
        # Lesen des bestehenden Inhalts der Datei
        print(f"Lese bestehenden Inhalt von {filename}")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # Finden der Start- und Endpositionen des Inhalts nach den anfänglichen Metadaten
        start_index = existing_content.find('---', 3) + 4  # Finden des zweiten '---' und darüber hinausgehen
        end_index = len(existing_content)

        # Konstruieren des aktualisierten Inhalts
        updated_content = existing_content[:start_index].strip() + '\n\n'  # Metadaten beibehalten und eine neue Zeile hinzufügen
        updated_content += markdown_content.strip() + '\n'  # Neue Markdown-Liste hinzufügen
        # updated_content += existing_content[end_index:].strip() # Alles nach der Liste anhängen, falls vorhanden

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"{filename} erfolgreich aktualisiert")
        markdown_changed = existing_content != updated_content
        print(f"Markdown geändert: {markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"Fehler beim Aktualisieren von {filename}: {e}")
        return False

def main():
    """Hauptfunktion zum Abrufen, Verarbeiten und Aktualisieren der Markdown-Datei."""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'NYTimes-Links von abrufen: {nytimes_url}')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("Hauptseiteninhalt konnte nicht abgerufen werden.")
        return

    links = extract_links(html_content)
    print(f'{len(links)} Links auf der Hauptseite gefunden. Links extrahieren...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'Verarbeiten von Link {i + 1} von {len(links)}: {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'Inhalt von {link["url"]} konnte nicht abgerufen werden')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("Die Markdown-Datei wurde mit neuen Links aktualisiert.")
        sys.exit(0)
    else:
        print("Die Markdown-Datei wurde nicht aktualisiert (keine Änderungen).")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Frontend-Code:

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'NYTimes Artikel aktualisieren';
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
                alert('Aktualisierung erfolgreich ausgelöst! Bitte warten Sie einige Minuten, um das Ergebnis zu sehen.');
            } else {
                alert(`Aktualisierung fehlgeschlagen. Statuscode: ${response.status}`);
                console.error('Aktualisierung fehlgeschlagen:', response);
            }
        })
        .catch(error => {
            alert('Aktualisierung fehlgeschlagen. Überprüfen Sie die Konsole auf Fehler.');
            console.error('Fehler beim Auslösen der Aktualisierung:', error);
        });
    });
} else {
    console.error("nytimes div nicht gefunden!");
}
```