---
audio: true
lang: es
layout: post
title: Mensajes de Commit en Git Potenciados por IA
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
    Genera un mensaje de commit usando IA basado en los cambios preparados y los commitea.

    Args:
        push (bool, opcional): Si se deben enviar los cambios después de hacer el commit. Por defecto es True.
    """
    # Prepara todos los cambios
    subprocess.run(["git", "add", "-A"], check=True)

    # Obtiene el diff de los cambios preparados
    diff_process = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True, check=True)
    diff = diff_process.stdout

    if not diff:
        print("No hay cambios para committear.")
        return

    # Prepara el prompt para la IA
    prompt = f"""
Genera un mensaje de commit conciso en formato Conventional Commits para los siguientes cambios en el código.
Usa uno de los siguientes tipos: feat, fix, docs, style, refactor, test, chore, perf, ci, build, o revert.
Si es aplicable, incluye un scope entre paréntesis para describir la parte del código afectada.
El mensaje de commit no debe exceder los 70 caracteres.

Cambios en el código:
{diff}

Mensaje de commit:
"""    

    # Envía el prompt a la API de DeepSeek
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: La variable de entorno DEEPSEEK_API_KEY no está configurada.")
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
            print("Error: No hubo respuesta de la API.")
            return
    except Exception as e:
        print(f"Error durante la llamada a la API: {e}")
        return

    # Depuración: Imprime la respuesta de la API
    print(f"Respuesta de la API: {response}")


    # Verifica si el mensaje de commit está vacío
    if not commit_message:
        print("Error: Se generó un mensaje de commit vacío. Abortando el commit.")
        return

    # Commitea con el mensaje generado
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Envía los cambios
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("Cambios committeados localmente, pero no enviados.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera un mensaje de commit con IA y commitea los cambios.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='Commitea los cambios localmente sin enviarlos.')
    args = parser.parse_args()
    gitmessageai(push=args.push)
```

Luego, en tu archivo `~/.zprofile`, agrega lo siguiente:

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