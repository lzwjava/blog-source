---
audio: true
generated: false
image: false
lang: es
layout: post
title: Actualización del disparador de artículos de NYTimes News (CN)
translated: true
---

Haga clic en el botón a continuación para actualizar los artículos de [NYTimes CN](./notes/2025-03-14-nytimes-en).

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes"></div>

Esta página le permite activar una actualización de los artículos de NYTimes CN. Hacer clic en el botón iniciará un flujo de trabajo que obtiene los artículos más recientes, los traduce y actualiza el contenido en este sitio. Tenga en cuenta que puede tardar unos minutos en que los cambios aparezcan después de que se active la actualización.

Código Python:

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
    """Llama a la API de Mistral para traducir texto."""
    api_key = os.environ.get("MISTRAL_API_KEY")
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
        print(f"Solicitud enviada: {prompt[:1000]}...")  # Imprime los primeros 100 caracteres de la solicitud
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Respuesta de la API de Mistral: {response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"Contenido de la API de Mistral: {content}")
            return content
        else:
            print(f"Error de la API de Mistral: Formato de respuesta no válido: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de la API de Mistral: {e}")
        if e.response:
            print(f"Código de estado de la respuesta: {e.response.status_code}")
            print(f"Contenido de la respuesta: {e.response.text}")
        return None

def fetch_html_content(url):
    """Obtiene el contenido HTML de una URL dada."""
    try:
        # Crear un contexto SSL no verificado
        context = ssl._create_unverified_context()
        print(f"Obteniendo contenido HTML desde: {url}")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Levantar HTTPError para respuestas incorrectas (4xx o 5xx)
        print(f"Contenido HTML obtenido con éxito desde: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"No se pudo obtener la URL: {url} - {e}")
        return None

def extract_links(html):
    """Extrae enlaces de la página principal de cn.nytimes.com."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"Se extrajeron {len(links)} enlaces de la página principal.")
    return links

def translate_title(title):
    """Traducir el título del chino al inglés usando Mistral."""
    base_prompt = "Traducir el siguiente título a {target_language}. Proporcionar solo el título traducido, sin notas adicionales o explicaciones. No repetir ni mencionar el texto de entrada.\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"Traducir título: {title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"Título traducido: {translated_title}")
        return translated_title
    else:
        raise Exception(f"No se pudo traducir el título: {title}")

def summarize_article(html):
    """Resumir el contenido del artículo usando la API de Mistral en inglés."""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"Título extraído: {title}")

    # Extraer el texto principal del artículo
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("No se pudo extraer el texto del artículo.")
        return None, None

    # Crear una solicitud para que Mistral resuma
    prompt = f"Resumir el siguiente artículo en inglés, centrándose en los puntos principales y evitando frases introductorias como 'Resumen:' o 'Este artículo trata sobre:'.\n\n{article_text[:30000]}\n\n"  # Limitar el texto del artículo a 30000 caracteres
    print(f"Creando resumen para el título: {title}")
    summary = call_mistral_api(prompt)

    if summary:
        # Limpiar el resumen eliminando "Resumen:" o frases similares al principio
        summary = summary.replace("Summary:", "").strip()
        print(f"Resumen generado: {summary}")
        return title, summary
    else:
        print(f"No se pudo generar el resumen para el título: {title}")
        return None, None

def generate_markdown_list(articles):
    """Genera una lista en Markdown a partir de una lista de resúmenes de artículos."""
    if not articles:
        return '* No se encontraron artículos.\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("Lista en Markdown generada.")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """Actualiza un archivo Markdown con el contenido dado."""
    try:
        # Leer el contenido existente del archivo
        print(f"Leyendo contenido existente desde {filename}")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # Encontrar las posiciones de inicio y fin del contenido después de los metadatos iniciales
        start_index = existing_content.find('---', 3) + 4  # Encontrar el segundo '---' y moverse más allá de él
        end_index = len(existing_content)

        # Construir el contenido actualizado
        updated_content = existing_content[:start_index].strip() + '\n\n'  # Mantener los metadatos y agregar una nueva línea
        updated_content += markdown_content.strip() + '\n'  # Agregar la nueva lista en Markdown
        # updated_content += existing_content[end_index:].strip() # Anexar cualquier cosa después de la lista, si existe

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Se actualizó {filename} con éxito")
        markdown_changed = existing_content != updated_content
        print(f"Markdown cambiado: {markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"Error al actualizar {filename}: {e}")
        return False

def main():
    """Función principal para obtener, procesar y actualizar el archivo Markdown."""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'Obteniendo enlaces de NYTimes desde: {nytimes_url}')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("No se pudo obtener el contenido de la página principal.")
        return

    links = extract_links(html_content)
    print(f'Se encontraron {len(links)} enlaces en la página principal. Extrayendo enlaces...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'Procesando enlace {i + 1} de {len(links)}: {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'No se pudo obtener el contenido desde {link["url"]}')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("El archivo Markdown se actualizó con nuevos enlaces.")
        sys.exit(0)
    else:
        print("El archivo Markdown no se actualizó (sin cambios).")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Código del frontend:

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'Actualizar Artículos de NYTimes';
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
                alert('Actualización iniciada con éxito. Por favor, espere unos minutos para ver el resultado.');
            } else {
                alert(`La actualización falló. Código de estado: ${response.status}`);
                console.error('La actualización falló:', response);
            }
        })
        .catch(error => {
            alert('La actualización falló. Consulte la consola para ver los errores.');
            console.error('Error al iniciar la actualización:', error);
        });
    });
} else {
    console.error("¡No se encontró el div de nytimes!");
}
```