---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 記錄聊天機械人互動的 Python 腳本
translated: true
type: note
---

### 用於記錄聊天機械人互動的巧妙 Python 腳本

是否曾想過要輕鬆記錄與 AI 聊天機械人的對話？這個精巧的 Python 腳本利用剪貼簿來擷取你的查詢和機械人的回覆，然後整齊地儲存到 Markdown 檔案中。就像是一個專為 AI 對話而設的個人記錄器！

它假裝是 GitHub Copilot，但實際上透過處理複製貼上的工作流程，幫助你與任何聊天機械人互動。需要安裝 `pyperclip`（如有需要可透過 pip 安裝）。

以下是完整程式碼：

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

在終端機中執行它，它會引導你完成整個流程。非常適合研究人員、開發人員或任何需要歸檔 AI 輸出的人。你覺得如何——實用的小技巧對吧？🚀

#Python #AI #Chatbots #CodingTips