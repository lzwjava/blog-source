---
audio: false
generated: true
lang: hi
layout: post
title: सीएसवी सॉर्टर स्क्रिप्ट
translated: true
type: note
---

मैं एक Python स्क्रिप्ट बनाऊंगा जो argparse का उपयोग करके एक CSV फ़ाइल पथ को पार्स करेगी, अल्पविराम से अलग किए गए मानों की एकल पंक्ति को वर्णानुक्रम में क्रमबद्ध करेगी, और परिणाम को "name_sorted.csv" नामक फ़ाइल में आउटपुट करेगी।

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Argument parser सेट करें
    parser = argparse.ArgumentParser(description='Sort a single-line CSV file alphabetically')
    parser.add_argument('file_path', help='Path to the input CSV file')
    
    # Arguments को पार्स करें
    args = parser.parse_args()
    
    try:
        # Directory और filename प्राप्त करें
        file_dir = os.path.dirname(args.file_path)
        file_name = os.path.basename(args.file_path)
        
        # Output filename बनाएं
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{base_name}_sorted{ext}")
        
        # Input CSV फ़ाइल को पढ़ें
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # केवल पहली पंक्ति प्राप्त करें
            for row in reader:
                values = row
                break
        
        # मानों को वर्णानुक्रम में क्रमबद्ध करें
        sorted_values = sorted(values)
        
        # Output फ़ाइल में लिखें
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"Successfully sorted values and saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{args.file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

यह स्क्रिप्ट:
1. Input फ़ाइल पथ प्राप्त करने के लिए argparse का उपयोग करती है
2. CSV फ़ाइल को खोलती है और केवल पहली पंक्ति पढ़ती है
3. मानों को वर्णानुक्रम में क्रमबद्ध करती है
4. क्रमबद्ध मानों को "name_sorted.csv" में लिखती है

स्क्रिप्ट को चलाने के लिए, इसे एक फ़ाइल में सहेजें (उदाहरण के लिए, "sort_csv.py"), यदि आवश्यक हो तो इसे एक्ज़िक्यूटेबल बनाएं, और इसे अपनी CSV फ़ाइल के पथ के साथ चलाएं:

```
python sort_csv.py path/to/your/file.csv
```

क्या आप चाहेंगे कि मैं कोड के किसी भाग को और अधिक विस्तार से समझाऊं?