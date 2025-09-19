---
audio: false
generated: false
image: false
lang: hi
layout: post
title: ब्लॉग प्रबंधन के लिए VSCode रीस्टार्ट के साथ स्वचालित ड्राफ्ट
translated: true
---

आपके द्वारा प्रदान की गई स्क्रिप्ट एक संरचित तरीके से ड्राफ्ट ब्लॉग पोस्ट्स को प्रकाशित करने की प्रक्रिया को स्वचालित करने के लिए डिज़ाइन की गई है। यह विशेष रूप से उन ब्लॉगर्स या सामग्री निर्माताओं के लिए उपयोगी है जो अपने पोस्ट्स को ड्राफ्ट के रूप में प्रबंधित करते हैं जब तक कि वे प्रकाशित होने के लिए तैयार नहीं होते। यहां स्क्रिप्ट के बारे में अधिक संदर्भ प्रदान करने के लिए एक विस्तृत परिचय दिया गया है:

## परिचय

एक ब्लॉग या किसी भी सामग्री-चालित वेबसाइट का प्रबंधन अक्सर ड्राफ्ट्स बनाना और उन्हें प्रकाशित होने से पहले संग्रहीत करना शामिल होता है। यह स्क्रिप्ट विशेष रूप से जेकिल या समान फ्रेमवर्क का उपयोग करने वाले स्टैटिक साइट जनरेटर सेटअप के लिए ड्राफ्ट पोस्ट्स को एक निर्दिष्ट प्रकाशन डायरेक्टरी में स्थानांतरित करने के कार्यप्रवाह को सरल बनाने के लिए बनाई गई है।

स्क्रिप्ट निम्नलिखित मुख्य कार्यों को पूरा करती है:

```python
import os
import datetime
import glob
import shutil
import sys
import subprocess
import time

def publish_drafts_to_posts():
    """आज के दिन बनाए गए ड्राफ्ट फाइलों की जांच करता है और उन्हें _posts/en डायरेक्टरी में स्थानांतरित करता है।"""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    drafts_dir = '_drafts'
    posts_en_dir = "original"

    if not os.path.exists(drafts_dir):
        print(f"ड्राफ्ट्स डायरेक्टरी '{drafts_dir}' मौजूद नहीं है। प्रकाशित करने के लिए कोई फाइलें नहीं हैं।")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # ड्राफ्ट्स डायरेक्टरी में आज के दिन के साथ शुरू होने वाली और -en.md से समाप्त होने वाली फाइलों को ढूंढने के लिए पैटर्न
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")

    found_files = glob.glob(pattern)

    if not found_files:
        print(f"ड्राफ्ट्स डायरेक्टरी '{drafts_dir}' में '{date_str}' से शुरू होने वाली कोई ड्राफ्ट फाइलें नहीं मिलीं जो प्रकाशित की जा सकें।")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"'{file_name}' को '{drafts_dir}' से '{posts_en_dir}' में स्थानांतरित किया गया।")
        except Exception as e:
            print(f"'{file_name}' को स्थानांतरित करने में त्रुटि: {e}")

    restart_vscode()

def restart_vscode():
    print("ड्राफ्ट फाइलों के दुर्घटनावश पुनः निर्माण से बचाने के लिए VSCode को सुचारू रूप से रीस्टार्ट कर रहा है...")
    try:
        if sys.platform == 'win32':
            # /f के बिना सुचारू बंद
            os.system('taskkill /im Code.exe /t')
            time.sleep(3)  # साफ़ करने के लिए देरी
            subprocess.Popen(['code', '.'])  # पुनः खोलना
        elif sys.platform == 'darwin':
            # सुचारू बंद के लिए AppleScript का उपयोग
            os.system('osascript -e \'quit app "Visual Studio Code"\'')
            time.sleep(3)
            subprocess.call(['open', '-a', 'Visual Studio Code', '.'])
        elif sys.platform.startswith('linux'):
            # सुचारू समाप्ति के लिए SIGTERM
            os.system('killall code')
            time.sleep(3)
            subprocess.Popen(['code', '.'])
        else:
            print("VSCode को रीस्टार्ट करने के लिए असमर्थ प्लेटफॉर्म।")
    except Exception as e:
        print(f"रीस्टार्ट के दौरान त्रुटि: {e}. कृपया VSCode को स्वयं रीस्टार्ट करें।")

if __name__ == "__main__":
    publish_drafts_to_posts()
```