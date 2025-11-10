---
audio: false
generated: true
image: false
lang: ja
layout: post
title: チャットボット対話ログ記録用Pythonスクリプト
translated: true
type: note
---

### チャットボットとの対話を記録する賢いPythonスクリプト

AIチャットボットとの会話を簡単に記録したいと思ったことはありませんか？この便利なPythonスクリプトは、クリップボードを使用してあなたの質問とボットの応答をキャプチャし、Markdownファイルにきれいに保存します。AIチャット用のパーソナルロガーのようなものです！

GitHub Copilotを装っていますが、実際にはコピー＆ペーストのワークフローを処理することで、あらゆるチャットボットとの対話を支援します。`pyperclip`が必要です（必要に応じてpipでインストールしてください）。

コード全体は以下の通りです：

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

ターミナルで実行すると、プロセスを案内してくれます。研究者、開発者、AIの出力をアーカイブしたい人に最適です。便利なハックだと思いませんか？🚀

#Python #AI #Chatbots #CodingTips