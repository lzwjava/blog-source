---
audio: false
generated: true
lang: hi
layout: post
title: स्वच्छ ज़िप फ़ाइल
translated: true
type: note
---

1. **ZIP फ़ाइल पढ़ता है** `zipfile.ZipFile` का उपयोग करके और अंदर की सभी फ़ाइलों की सूची प्राप्त करता है।
2. **एक्सटेंशन के बिना फ़ाइलों को फ़िल्टर करता है**, जबकि डायरेक्टरीज़ (`/` के साथ समाप्त होने वाली एंट्रीज़) को रखता है।
3. **हटाई गई फ़ाइलों को लॉग करता है** ताकि उपयोगकर्ता को पता चले कि किन्हें बाहर रखा गया था।
4. **केवल वैध फ़ाइलों (एक्सटेंशन या डायरेक्टरी वाली) के साथ एक नई ZIP फ़ाइल बनाता है**।
5. **कमांड-लाइन तर्क के रूप में ZIP फ़ाइल पथ स्वीकार करने के लिए `argparse` का उपयोग करता है**।

यह सुनिश्चित करता है कि केवल उचित फ़ाइलें ही रहें जबकि डायरेक्टरी संरचनाएँ संरक्षित रहें। 🚀

```python
import zipfile
import os
import argparse

def clean_zip(zip_path):
    output_path = os.path.splitext(zip_path)[0] + "_output.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        
        # Separate valid files and files without extensions (excluding directories)
        valid_files = [f for f in file_names if os.path.splitext(os.path.basename(f))[1] or f.endswith('/')]
        removed_files = [f for f in file_names if not os.path.splitext(os.path.basename(f))[1] and not f.endswith('/')]
        
        if not valid_files:
            print("No valid files with extensions found. Exiting.")
            return
        
        # Log removed files
        if removed_files:
            print("Removing the following files (no extensions detected):")
            for f in removed_files:
                print(f" - {f}")
        
        # Create a new zip file excluding invalid files
        with zipfile.ZipFile(output_path, 'w') as clean_zip:
            for file in valid_files:
                with zip_ref.open(file) as source:
                    clean_zip.writestr(file, source.read())

    print(f"Cleaned ZIP file created: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean a ZIP file by removing files without extensions.")
    parser.add_argument("zip_path", help="Path to the input ZIP file")
    args = parser.parse_args()
    clean_zip(args.zip_path)

```