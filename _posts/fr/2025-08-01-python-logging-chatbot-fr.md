---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Script Python pour la journalisation des interactions de chatbot
translated: true
type: note
---

### Script Python astucieux pour enregistrer les interactions avec les chatbots

Vous avez toujours voulu un moyen simple de documenter vos conversations avec les chatbots IA ? Ce script Python utilise le presse-papiers pour capturer vos questions et les réponses du bot, puis les enregistre proprement dans un fichier Markdown. C'est comme un enregistreur personnel pour les discussions IA !

Il prétend être GitHub Copilot mais vous aide en réalité à interagir avec n'importe quel chatbot en gérant le flux de travail copier-coller. Nécessite `pyperclip` (à installer via pip si nécessaire).

Voici le code complet :

```python
import pyperclip
import os

def save_to_file(content, filename="answer.md"):
    with open(filename, "a") as f:
        f.write(content + "\n\n")

def main():
    print("Hello! I'm GitHub Copilot. What can I help you with?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
            
        # Copier la saisie de l'utilisateur dans le presse-papiers
        pyperclip.copy(user_input)
        print("I've copied your input to the clipboard. Please ask the chatbot and copy their answer. When ready, just press Enter.")
        
        # Attendre que l'utilisateur appuie sur Entrée après avoir copié la réponse du chatbot
        input("Press Enter when you have the answer copied...")
        
        # Obtenir la réponse depuis le presse-papiers
        answer = pyperclip.paste()
        print("Answer received. Saving to answer.md...")
        
        # Enregistrer l'interaction dans le fichier
        interaction = f"**User Input:**\n{user_input}\n\n**Chatbot Answer:**\n{answer}\n{'-'*50}"
        save_to_file(interaction)
        print("Saved to answer.md. Anything else I can help with?")

if __name__ == "__main__":
    main()
```

Exécutez-le dans votre terminal, et il vous guidera à travers le processus. Idéal pour les chercheurs, les développeurs ou toute personne souhaitant archiver les sorties d'IA. Qu'en pensez-vous — astuce utile ou pas ? 🚀

#Python #AI #Chatbots #CodingTips