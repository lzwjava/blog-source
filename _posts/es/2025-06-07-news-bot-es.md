---
audio: true
generated: false
image: false
lang: es
layout: post
title: Bot Automatizado de Resumen de Noticias
translated: true
type: post
---

Esta publicación presenta un bot de noticias basado en Python que recopila y resume las principales historias de Hacker News, GitHub Trending y NYTimes (en chino) utilizando la API de Mistral. Envía informes diarios concisos a través de Telegram, con un flujo de trabajo de GitHub Actions para su ejecución automatizada. Ideal para mantenerse al día con noticias tecnológicas y globales sin esfuerzo.

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
        print("Error: TELEGRAM_BOT_API_KEY o TELEGRAM_CHAT_ID no están configurados.")
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    url_pattern = re.compile(r'(https?://[^\s]+)')
    # Eliminar todos los asteriscos (para negrita/cursiva) del mensaje
    message_no_stars = message.replace('*', '')
    # Eliminar enlaces del mensaje
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
            print(f"Mensaje de Telegram enviado exitosamente ({len(part)} caracteres).")
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar mensaje de Telegram: {e}")
            success = False
    return success

def fetch_html_content(url):
    try:
        print(f"Obteniendo contenido HTML de: {url}")
        response = requests.get(url, timeout=15, verify=False)
        response.raise_for_status()
        print(f"Contenido HTML obtenido exitosamente de: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"No se pudo obtener la URL: {url} - {e}")
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
    print(f"Se extrajeron {len(links)} enlaces de Hacker News.")
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
    print(f"Se extrajeron {len(links)} repositorios destacados de GitHub.")
    return links

def call_mistral_api(prompt, model="mistral-small-latest"):
    api_key = MISTRAL_API_KEY
    if not api_key:
        print("Error: La variable de entorno MISTRAL_API_KEY no está configurada.")
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
        print(f"Llamando a la API de Mistral con el modelo: {model}")
        print(f"Prompt enviado: {prompt[:1000]}...")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Respuesta de la API de Mistral: {response_json}")
        if response_json and response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Contenido de la API de Mistral: {content}")
            return content
        else:
            print(f"Error en la API de Mistral: Formato de respuesta inválido: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la API de Mistral: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Código de estado de la respuesta: {e.response.status_code}")
            print(f"Contenido de la respuesta: {e.response.text}")
        return None

def fetch_and_summarize(url, fallback_title=None):
    print(f"Resumiendo: {url}")
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "No se pudo obtener el contenido.", "title": fallback_title or url}
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
        print("No hay MISTRAL_API_KEY configurada. Se devuelven las primeras 15 palabras como resumen.")
        return limit_to_n_words(text, 15)
    prompt = (
        "Si el texto original está en chino, resúmelo en inglés. "
        "Resume el siguiente contenido de una página web en inglés claro y conciso. "
        "Enfócate en el punto o insight más importante. "
        "Tu resumen debe tener alrededor de 300 caracteres. "
        "Solo muestra la oración del resumen:\n"
        f"Título: {title if title else ''}\n"
        f"{text}\n"
        f"{'Enlace original: ' + url if url else ''}"
    )
    summary = call_mistral_api(prompt)
    if summary is None:
        return limit_to_n_words(text, 15)
    # Truncar a 300 caracteres como último recurso
    return summary.strip()[:300]

def generate_summarized_report(summaries, source_name):
    text = f"{source_name}\n"
    text += "-" * len(source_name) + "\n"
    if not summaries:
        text += "No se encontraron elementos.\n\n"
        return text
    url_pattern = re.compile(r'(https?://[^\s]+)')
    for idx, item in enumerate(summaries, 1):
        summary = item.get('summary', '').replace('\n', ' ').replace('\r', ').strip()
        summary = summary.replace('*', '')
        summary = url_pattern.sub('', summary)
        # Truncar cada resumen a 300 caracteres como último recurso
        summary = summary[:300]
        text += f"{idx}. {summary}\n\n"  # Añadir un salto de línea adicional entre resúmenes
    text += "\n"
    return text

# --- Integración con NYTimes (m.cn.nytimes.com) ---

def extract_nytimes_links(html, max_links=5):
    """
    Extrae enlaces de la página principal de cn.nytimes.com.
    Solo incluye enlaces que comienzan con 'https://cn.nytimes.com/'.
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
    print(f"Se extrajeron {len(links)} enlaces de la página principal.")
    return links

def summarize_nytimes_article(url):
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "No se pudo obtener el contenido.", "title": url}
    soup = BeautifulSoup(html, 'html.parser')
    # Intentar extraer el título principal del artículo
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else (soup.title.text.strip() if soup.title else url)
    # Extraer el texto principal del artículo
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
    # Verificar el argumento --test
    is_test = "--test" in sys.argv

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report = f"Resumen Diario de Noticias - {today}\n\n"

    if is_test:
        # Solo recopilar un enlace y enviar un resumen (NYTimes en chino)
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=1)
            if ny_links:
                link = ny_links[0]
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
        report = generate_summarized_report(ny_summaries, "NYTimes (Chino)")
        if ny_summaries:
            if send_telegram_message(report):
                print("Resumen de prueba enviado a Telegram exitosamente.")
                sys.exit(0)
            else:
                print("Error al enviar el resumen de prueba a Telegram.")
                sys.exit(1)
        else:
            print("No se recopilaron noticias, no se envió nada a Telegram.")
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
        report += generate_summarized_report(ny_summaries, "NYTimes (Chino)")

        if any([hn_summaries, gh_summaries, ny_summaries]):
            if len(report) > TELEGRAM_MAX_LENGTH:
                print(f"El informe excede {TELEGRAM_MAX_LENGTH} caracteres, se dividirá en múltiples mensajes.")
            if send_telegram_message(report):
                print("Informe diario de noticias enviado a Telegram exitosamente.")
                sys.exit(0)
            else:
                print("Error al enviar el informe diario de noticias a Telegram.")
                sys.exit(1)
        else:
            print("No se recopilaron noticias, no se envió nada a Telegram.")
            sys.exit(1)

if __name__ == "__main__":
    main()
```

```yml
name: Bot de Noticias

on:
  schedule:
    # Se ejecuta todos los días a las 9 AM hora de Beijing (1 AM UTC).
    - cron: '0 1 * * *'
  workflow_dispatch:  # Permite activación manual
  push:
    # Solo se activa si AMBOS archivos cambian en el mismo commit/push
    # Esto requiere un trabajo de filtro abajo para verificar ambos archivos
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
      - name: Checkout del repositorio
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configurar Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: Ejecutar script del bot de noticias
        run: python scripts/nytimes/news_bot.py
              
```