---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: सीएसवी फ़ाइलें पढ़ना और लिखना
translated: true
type: note
---

### Python के `csv` मॉड्यूल का परिचय

`csv` मॉड्यूल Python की स्टैंडर्ड लाइब्रेरी का हिस्सा है और CSV (Comma-Separated Values) फाइलों को पढ़ने और लिखने के लिए उपयोग किया जाता है। यह पंक्तियों और कॉलम को कुशलतापूर्वक पार्स करता है। इसका उपयोग करने के लिए, पहले मॉड्यूल को इम्पोर्ट करें: `import csv`। आप फाइल ऑब्जेक्ट के साथ काम करेंगे, जो आमतौर पर रीड मोड (`'r'`) या राइट मोड (`'w'`) में खोले जाते हैं।

मुख्य घटक:
- **रीडर**: फाइल से CSV डेटा को पार्स करता है (उदाहरण के लिए, `csv.reader()` रो-आधारित एक्सेस के लिए)।
- **राइटर**: CSV फाइल में डेटा आउटपुट करता है (उदाहरण के लिए, `csv.writer()`)।
- CSV फाइलों को पंक्तियों के अनुक्रम के रूप में माना जाता है, जहाँ प्रत्येक पंक्ति स्ट्रिंग्स (कॉलम) की एक सूची होती है।

सुरक्षा और सुविधा के लिए, फाइलों को हमेशा `with` स्टेटमेंट के साथ हैंडल करें ताकि उनके सही तरीके से बंद होने की गारंटी रहे।

### एक CSV फाइल को बेसिक रीडिंग

CSV पढ़ने के लिए:
```python
import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # प्रत्येक 'row' कॉलम की एक सूची है
```
- यह फाइल को पंक्ति दर पंक्ति पढ़ता है। आप इंडेक्स द्वारा विशिष्ट कॉलम तक पहुँच सकते हैं (उदाहरण के लिए, पहले कॉलम के लिए `row[0]`)।
- हेडर के लिए, पहली पंक्ति को अलग से पढ़ें: `headers = next(reader)`।

### दो CSV फाइलों की तुलना: पंक्तियाँ और कॉलम

दो CSV (उदाहरण के लिए, `file1.csv` और `file2.csv`) की तुलना करने के लिए, उन्हें सूचियों की सूची (पंक्तियाँ) जैसी संरचनाओं में लोड करें, फिर तुलना करें। मान्यताएँ: दोनों CSV की संरचना समान है (कॉलम/पंक्तियों की समान संख्या)। तुलना सटीक मिलान, अंतर, या विशिष्ट लॉजिक (उदाहरण के लिए, किसी कुंजी कॉलम पर मिलान) की जांच कर सकती है।

#### उदाहरण 1: पंक्तियों की तुलना (संपूर्ण पंक्तियाँ)
पंक्तियों को संग्रहीत करने के लिए डिक्शनरी का उपयोग करें (यदि उनमें एक अद्वितीय ID कॉलम है) या प्रत्यक्ष तुलना के लिए सूचियों का उपयोग करें।

```python
import csv

def compare_rows(file1, file2, key_column=0):
    # file1 को एक dict में पढ़ें (key_column को कुंजी के रूप में उपयोग करके, संपूर्ण पंक्ति को मान के रूप में)
    data1 = {}
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        headers1 = next(reader1, None)  # हेडर को स्किप करें यदि मौजूद है
        for row in reader1:
            data1[row[key_column]] = row  # उदाहरण के लिए, पहले कॉलम पर कुंजी बनाएँ

    # file2 को इसी तरह पढ़ें
    data2 = {}
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        headers2 = next(reader2, None)
        for row in reader2:
            data2[row[key_column]] = row

    # तुलना करें
    common_keys = set(data1.keys()) & set(data2.keys())
    differing_rows = []
    for key in common_keys:
        if data1[key] != data2[key]:
            differing_rows.append((key, data1[key], data2[key]))
    
    return differing_rows  # (key, row_from_file1, row_from_file2) की सूची

# उपयोग
differences = compare_rows('file1.csv', 'file2.csv', key_column=0)  # कॉलम 0 पर कुंजी बनाएँ
print("भिन्न पंक्तियाँ:", differences)
```

- **यह कैसे काम करता है**: CSV को एक कॉलम (जैसे ID) द्वारा कुंजीबद्ध डिक्शनरी में बदल देता है। मिलान वाली पंक्तियों की सीधे तुलना करता है। कुंजी बनाने के लिए किस कॉलम का उपयोग करना है, इसे निर्दिष्ट करने के लिए `key_column` को एडजस्ट करें।
- **विविधताएँ**: कुंजियों के बिना पंक्ति-दर-पंक्ति तुलना के लिए, दोनों रीडर को एक साथ इटरेट करें (यदि क्रम/लंबाई समान है)।

#### उदाहरण 2: कॉलम की तुलना
पूरी फाइल में विशिष्ट कॉलम की तुलना करें (उदाहरण के लिए, जांचें कि क्या दोनों फाइलों में कॉलम 1 के मान समान हैं)।

```python
import csv

def compare_columns(file1, file2, col_index=0):
    # कॉलम डेटा को सूचियों के रूप में निकालें
    col1 = []
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        next(reader1, None)  # हेडर को स्किप करें यदि आवश्यक हो
        for row in reader1:
            if len(row) > col_index:
                col1.append(row[col_index])

    col2 = []
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        next(reader2, None)
        for row in reader2:
            if len(row) > col_index:
                col2.append(row[col_index])

    # कॉलम की तुलना करें
    are_equal = col1 == col2
    differences = []
    for i, (val1, val2) in enumerate(zip(col1, col2)):
        if val1 != val2:
            differences.append((i, val1, val2))
    
    return are_equal, differences  # मिलान के लिए Bool, (row_index, val1, val2) की सूची

# उपयोग
equal, diffs = compare_columns('file1.csv', 'file2.csv', col_index=1)  # कॉलम 1 की तुलना करें
print("कॉलम समान हैं?", equal)
print("अंतर (पंक्ति, val1, val2):", diffs)
```

- **यह कैसे काम करता है**: निर्दिष्ट कॉलम को सूचियों में निकालता है, फिर एलिमेंट-वाइज तुलना करता है। मानता है कि CSV में पंक्तियों की संख्या समान है; यदि आवश्यक हो तो मिसमैच को हैंडल करें।
- **विविधताएँ**: अधिक उन्नत कॉलम ऑपरेशन के लिए `pandas` का उपयोग करें (उदाहरण के लिए, `df1['column'] == df2['column']`), लेकिन शुद्ध स्टैंडर्ड लाइब्रेरी के लिए `csv` पर बने रहें।

#### टिप्स और एज केस
- **हेडर**: यदि CSV में हेडर हैं, तो उन्हें `next(reader)` से स्किप करें।
- **डेटा प्रकार**: CSV स्ट्रिंग के रूप में पढ़ता है; यदि आवश्यक हो तो int/float में कनवर्ट करें (उदाहरण के लिए, `int(row[0])`)।
- **बड़ी फाइलें**: बड़े CSV के लिए, कुंजीबद्ध एक्सेस के लिए DictReader का उपयोग करें: `csv.DictReader(file)` पंक्तियों को OrderedDicts के रूप में लौटाता है।
- **डिलीमीटर**: यदि कॉमा-सेपरेटेड नहीं है तो रीडर/राइटर में `delimiter=';'` का उपयोग करें।
- **त्रुटियाँ**: फाइल संबंधी समस्याओं के लिए try-except में रैप करें; इंडेक्स एरर से बचने के लिए कॉलम लंबाई को वैलिडेट करें।
- **विकल्प**: जटिल तुलना के लिए, `pandas` जैसी लाइब्रेरी पर विचार करें (डेटाफ्रेम के लिए `df1.equals(df2)`)।

पूर्ण डॉक्स के लिए, Python का [आधिकारिक csv मॉड्यूल गाइड](https://docs.python.org/3/library/csv.html) देखें। यदि आपके पास विशिष्ट CSV फाइलें या तुलना लॉजिक है, तो टेलर्ड कोड के लिए अधिक विवरण प्रदान करें!