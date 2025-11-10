---
audio: false
generated: true
image: false
lang: ar
layout: post
title: برنامج نصي بلغة بايثون لتسجيل تفاعلات روبوت الدردشة
translated: true
type: note
---

### نصيحة برمجية ذكية لتسجيل محادثات روبوتات الدردشة

هل سبق لك أن أردت طريقة سهلة لتوثيق محادثاتك مع روبوتات الدردشة الذكية؟ هذا السكريبت البسيط المكتوب بلغة Python يستخدم الحافظة لالتقاط استفساراتك وردود الروبوت، ثم يحفظها بدقة في ملف Markdown. إنه بمثابة مسجل شخصي لمحادثات الذكاء الاصطناعي!

يتظاهر البرنامج النصي بأنه GitHub Copilot ولكنه في الواقع يساعدك على التفاعل مع أي روبوت دردشة من خلال التعامل مع سير عمل النسخ واللصق. يتطلب تثبيت `pyperclip` (يمكن تثبيته عبر pip إذا لزم الأمر).

إليك الكود الكامل:

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

شغّله في الطرفية (Terminal)، وسوف يرشدك خلال العملية. رائع للباحثين والمطورين أو أي شخص يرغب في أرشفة مخرجات الذكاء الاصطناعي. ما رأيك – هل تعتبره اختراقًا مفيدًا؟ 🚀

#Python #AI #Chatbots #CodingTips