---
audio: false
generated: true
image: false
lang: es
layout: post
title: Script de Python para Registrar Interacciones de Chatbot
translated: true
type: note
---

### Ingenioso script en Python para registrar interacciones con chatbots

¿Alguna vez has querido una forma fácil de documentar tus conversaciones con chatbots de IA? Este ingenioso script de Python utiliza el portapapeles para capturar tus consultas y las respuestas del bot, guardándolas ordenadamente en un archivo Markdown. ¡Es como un registrador personal para chats de IA!

Simula ser GitHub Copilot pero en realidad te ayuda a interactuar con cualquier chatbot manejando el flujo de trabajo de copiar y pegar. Requiere `pyperclip` (instálalo via pip si es necesario).

Aquí está el código completo:

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
            
        # Copy user input to clipboard
        pyperclip.copy(user_input)
        print("I've copied your input to the clipboard. Please ask the chatbot and copy their answer. When ready, just press Enter.")
        
        # Wait for user to press Enter after copying the chatbot's answer
        input("Press Enter when you have the answer copied...")
        
        # Get the answer from clipboard
        answer = pyperclip.paste()
        print("Answer received. Saving to answer.md...")
        
        # Save the interaction to file
        interaction = f"**User Input:**\n{user_input}\n\n**Chatbot Answer:**\n{answer}\n{'-'*50}"
        save_to_file(interaction)
        print("Saved to answer.md. Anything else I can help with?")

if __name__ == "__main__":
    main()
```

Ejecútalo en tu terminal y te guiará a través del proceso. Ideal para investigadores, desarrolladores o cualquiera que archive salidas de IA. ¿Qué opinas—¿un truco útil o no? 🚀

#Python #AI #Chatbots #CodingTips