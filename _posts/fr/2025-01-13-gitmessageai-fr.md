---
audio: true
lang: fr
layout: post
title: Messages de Commit Git Assistés par l'IA
translated: true
---

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

def gitmessageai(push=True):
    """
    Génère un message de commit en utilisant l'IA basée sur les changements mis en attente et les committe.

    Args:
        push (bool, optional): Indique si les changements doivent être poussés après le commit. Par défaut à True.
    """
    # Mettre en attente tous les changements
    subprocess.run(["git", "add", "-A"], check=True)

    # Obtenir le diff des changements mis en attente
    diff_process = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True, check=True)
    diff = diff_process.stdout

    if not diff:
        print("Aucun changement à committer.")
        return

    # Préparer le prompt pour l'IA
    prompt = f"""
Génère un message de commit concis au format Conventional Commits pour les changements de code suivants.
Utilise l'un des types suivants : feat, fix, docs, style, refactor, test, chore, perf, ci, build, ou revert.
Si applicable, inclut une portée entre parenthèses pour décrire la partie du codebase affectée.
Le message de commit ne doit pas dépasser 70 caractères.

Changements de code :
{diff}

Message de commit :
"""    

    # Envoyer le prompt à l'API DeepSeek
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Erreur : La variable d'environnement DEEPSEEK_API_KEY n'est pas définie.")
        return
    
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
        else:
            print("Erreur : Aucune réponse de l'API.")
            return
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API : {e}")
        return

    # Debug : Afficher la réponse de l'API
    print(f"Réponse de l'API : {response}")


    # Vérifier si le message de commit est vide
    if not commit_message:
        print("Erreur : Message de commit vide généré. Abandon du commit.")
        return

    # Committer avec le message généré
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Pousser les changements
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("Changements commités localement, mais non poussés.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère un message de commit avec l'IA et committe les changements.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='Commite les changements localement sans les pousser.')
    args = parser.parse_args()
    gitmessageai(push=args.push)
```

Ensuite, dans votre fichier `~/.zprofile`, ajoutez ce qui suit :

```
function gitpush {
  python ~/bin/gitmessageai.py
}

function gitcommit {
  python ~/bin/gitmessageai.py --no-push
}

alias gpa=gitpush
alias gca=gitcommit
```