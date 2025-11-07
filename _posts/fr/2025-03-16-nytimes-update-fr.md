---
audio: true
generated: false
image: false
lang: fr
layout: post
title: Mises à jour des articles NYTimes News (CN) déclencheurs
translated: true
type: post
---

Cliquez sur le bouton ci-dessous pour mettre à jour les articles [NYTimes CN](./notes/2025-03-14-nytimes-en).

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes"></div>

Cette page vous permet de déclencher une mise à jour des articles NYTimes CN. Cliquer sur le bouton lancera un flux de travail qui récupère les derniers articles, les traduit et met à jour le contenu de ce site. Veuillez noter qu'il peut falloir quelques minutes pour que les modifications apparaissent après le déclenchement de la mise à jour.

Code Python :

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
    """Appelle l'API Mistral pour traduire le texte."""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Erreur : la variable d'environnement MISTRAL_API_KEY n'est pas définie.")
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
        print(f"Prompt envoyé : {prompt[:1000]}...")  # Affiche les 1000 premiers caractères du prompt
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Réponse de l'API Mistral : {response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"Contenu de l'API Mistral : {content}")
            return content
        else:
            print(f"Erreur de l'API Mistral : Format de réponse invalide : {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de l'API Mistral : {e}")
        if e.response:
            print(f"Code de statut de la réponse : {e.response.status_code}")
            print(f"Contenu de la réponse : {e.response.text}")
        return None

def fetch_html_content(url):
    """Récupère le contenu HTML d'une URL donnée."""
    try:
        # Créer un contexte SSL non vérifié
        context = ssl._create_unverified_context()
        print(f"Récupération du contenu HTML depuis : {url}")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Lève une HTTPError pour les réponses incorrectes (4xx ou 5xx)
        print(f"Contenu HTML récupéré avec succès depuis : {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Impossible de récupérer l'URL : {url} - {e}")
        return None

def extract_links(html):
    """Extrait les liens de la page principale de cn.nytimes.com."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"{len(links)} liens extraits de la page principale.")
    return links

def translate_title(title):
    """Traduit le titre du chinois vers l'anglais en utilisant Mistral."""
    base_prompt = "Traduisez le titre suivant en {target_language}. Fournissez uniquement le titre traduit, sans notes ou explications supplémentaires. Ne répétez pas ou ne mentionnez pas le texte d'entrée.\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"Traduction du titre : {title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"Titre traduit : {translated_title}")
        return translated_title
    else:
        raise Exception(f"Échec de la traduction du titre : {title}")

def summarize_article(html):
    """Résumé du contenu de l'article en anglais en utilisant l'API Mistral."""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"Titre extrait : {title}")

    # Extraire le texte principal de l'article
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("Impossible d'extraire le texte de l'article.")
        return None, None

    # Créer un prompt pour Mistral afin de résumer
    prompt = f"Résumé de l'article suivant en anglais, en se concentrant sur les points principaux et en évitant les phrases introductives comme 'Résumé:' ou 'Cet article traite de:'.\n\n{article_text[:30000]}\n\n"  # Limiter le texte de l'article à 30000 caractères
    print(f"Création d'un résumé pour le titre : {title}")
    summary = call_mistral_api(prompt)

    if summary:
        # Nettoyer le résumé en supprimant les phrases de début comme "Résumé:" ou similaires
        summary = summary.replace("Résumé:", "").strip()
        print(f"Résumé généré : {summary}")
        return title, summary
    else:
        print(f"Échec de la génération du résumé pour le titre : {title}")
        return None, None

def generate_markdown_list(articles):
    """Génère une liste Markdown à partir d'une liste de résumés d'articles."""
    if not articles:
        return '* Aucun article trouvé.\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("Liste Markdown générée.")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """Met à jour un fichier Markdown avec le contenu donné."""
    try:
        # Lire le contenu existant du fichier
        print(f"Lecture du contenu existant depuis {filename}")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # Trouver les positions de début et de fin du contenu après les métadonnées initiales
        start_index = existing_content.find('---', 3) + 4  # Trouver le deuxième '---' et passer au-delà
        end_index = len(existing_content)

        # Construire le contenu mis à jour
        updated_content = existing_content[:start_index].strip() + '\n\n'  # Garder les métadonnées et ajouter une nouvelle ligne
        updated_content += markdown_content.strip() + '\n'  # Ajouter la nouvelle liste Markdown
        # updated_content += existing_content[end_index:].strip() # Ajouter tout ce qui suit la liste, s'il existe

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"{filename} mis à jour avec succès")
        markdown_changed = existing_content != updated_content
        print(f"Markdown modifié : {markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"Erreur lors de la mise à jour de {filename} : {e}")
        return False

def main():
    """Fonction principale pour récupérer, traiter et mettre à jour le fichier Markdown."""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'Récupération des liens NYTimes depuis : {nytimes_url}')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("Échec de la récupération du contenu de la page principale.")
        return

    links = extract_links(html_content)
    print(f'{len(links)} liens trouvés sur la page principale. Extraction des liens...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'Traitement du lien {i + 1} sur {len(links)} : {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'Échec de la récupération du contenu depuis {link["url"]}')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("Le fichier Markdown a été mis à jour avec de nouveaux liens.")
        sys.exit(0)
    else:
        print("Le fichier Markdown n'a pas été mis à jour (aucune modification).")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Code frontend :

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'Mettre à jour les articles NYTimes';
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
                alert('Mise à jour déclenchée avec succès ! Veuillez attendre quelques minutes pour voir le résultat.');
            } else {
                alert(`La mise à jour a échoué. Code de statut : ${response.status}`);
                console.error('La mise à jour a échoué :', response);
            }
        })
        .catch(error => {
            alert('La mise à jour a échoué. Vérifiez la console pour les erreurs.');
            console.error('Erreur lors du déclenchement de la mise à jour :', error);
        });
    });
} else {
    console.error("Div nytimes non trouvé !");
}
```