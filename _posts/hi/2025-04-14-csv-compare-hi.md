---
audio: false
generated: true
lang: hi
layout: post
title: दो एकल पंक्ति सीएसवी की तुलना
translated: true
type: note
---

नीचे एक Python स्क्रिप्ट है जो स्ट्रिंग्स (जैसे, "P0001") वाली दो सिंगल-रो CSV फाइलों की तुलना करती है और पहचानती है:
- सामान्य आइटम (दोनों फाइलों में मौजूद)
- पहली फाइल के लिए अद्वितीय आइटम
- दूसरी फाइल के लिए अद्वितीय आइटम

स्क्रिप्ट `argparse` का उपयोग दो CSV फाइल पथों को स्वीकार करने, प्रत्येक से पहली पंक्ति पढ़ने, सेट-आधारित तुलना करने और परिणामों को `comparison.txt` में लिखने के लिए करती है।

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Compare two single-row CSV files for common and unique items')
    parser.add_argument('file1_path', help='Path to the first CSV file')
    parser.add_argument('file2_path', help='Path to the second CSV file')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Read the first row of the first CSV file
        with open(args.file1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                values1 = row
                break
        
        # Read the first row of the second CSV file
        with open(args.file2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                values2 = row
                break
        
        # Convert to sets for comparison
        set1 = set(values1)
        set2 = set(values2)
        
        # Find common and unique items
        common_items = set1.intersection(set2)
        unique_to_file1 = set1.difference(set2)
        unique_to_file2 = set2.difference(set1)
        
        # Determine output directory (use directory of first file)
        output_dir = os.path.dirname(args.file1_path) or '.'
        output_file = os.path.join(output_dir, 'comparison.txt')
        
        # Write results to output file
        with open(output_file, 'w') as file:
            file.write("Comparison Results:\n\n")
            
            file.write("Common Items (in both files):\n")
            if common_items:
                for item in sorted(common_items):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
                
            file.write("\nItems only in first file:\n")
            if unique_to_file1:
                for item in sorted(unique_to_file1):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
                
            file.write("\nItems only in second file:\n")
            if unique_to_file2:
                for item in sorted(unique_to_file2):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
        
        print(f"Comparison complete. Results saved to {output_file}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### यह कैसे काम करती है:
1. **इनपुट**: कमांड-लाइन आर्गुमेंट्स के माध्यम से दो CSV फाइल पथ लेती है।
2. **रीडिंग**: प्रत्येक CSV फाइल से केवल पहली पंक्ति पढ़ती है।
3. **तुलना**:
   - कुशल तुलना के लिए पंक्तियों को सेट में बदलती है।
   - ढूँढती है:
     - **सामान्य आइटम**: दोनों पंक्तियों में मौजूद आइटम (सेट इंटरसेक्शन)।
     - **पहली फाइल के लिए अद्वितीय**: केवल पहली पंक्ति में मौजूद आइटम (सेट डिफरेंस: file1 - file2)।
     - **दूसरी फाइल के लिए अद्वितीय**: केवल दूसरी पंक्ति में मौजूद आइटम (सेट डिफरेंस: file2 - file1)।
4. **आउटपुट**: परिणामों को पहली फाइल के डायरेक्टरी में `comparison.txt` में लिखती है, जिसमें सूचीबद्ध होते हैं:
   - सामान्य आइटम
   - केवल पहली फाइल में आइटम
   - केवल दूसरी फाइल में आइटम
   - प्रत्येक सेक्शन वर्णानुक्रम में क्रमबद्ध होता है; यदि कोई सेक्शन खाली है तो "None" लिखा जाता है।
5. **एरर हैंडलिंग**: फाइल-नॉट-फाउंड एरर और अन्य एक्सेप्शन को कैच करती है।

### उदाहरण उपयोग:
स्क्रिप्ट को `compare_csv.py` के रूप में सेव करें। दो CSV फाइलें बनाएं, उदाहरण के लिए:
- `file1.csv`: `P0001,P0002,P0003`
- `file2.csv`: `P0001,P0004,P0003`

स्क्रिप्ट चलाएं:
```
python compare_csv.py file1.csv file2.csv
```

**आउटपुट** (`comparison.txt`):
```
Comparison Results:

Common Items (in both files):
P0001
P0003

Items only in first file:
P0002

Items only in second file:
P0004
```

### नोट्स:
- स्क्रिप्ट आइटम की पोजीशन को नजरअंदाज करती है और केवल उपस्थिति/अनुपस्थिति पर ध्यान केंद्रित करती है।
- एक पंक्ति में डुप्लिकेट आइटम स्वचालित रूप से हैंडल हो जाते हैं (सेट डुप्लिकेट्स को हटा देते हैं)।
- आउटपुट पहली इनपुट फाइल के डायरेक्टरी में `comparison.txt` में लिखा जाता है।
- यदि कोई फाइल खाली है या उसमें कोई पंक्ति नहीं है, तो स्क्रिप्ट इसे एक खाली सेट के रूप में मानेगी।

क्या आप चाहते हैं कि मैं स्क्रिप्ट को संशोधित करूं (जैसे, आउटपुट फॉर्मेट बदलूं या अधिक विवरण जोड़ूं)?