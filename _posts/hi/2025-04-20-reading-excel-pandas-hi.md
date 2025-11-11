---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पांडा के साथ एक्सेल फ़ाइलें पढ़ना
translated: true
type: note
---

### पूर्वापेक्षाएँ
Python में Excel फ़ाइलें पढ़ने के लिए, आपको `pandas` लाइब्रेरी और एक Excel इंजन की आवश्यकता होती है। pandas इंस्टॉल करें यदि पहले से इंस्टॉल नहीं है:
```
pip install pandas
```
आधुनिक Excel फॉर्मेट (.xlsx) के लिए, `openpyxl` इंस्टॉल करें:
```
pip install openpyxl
```
.xls फ़ाइलों के लिए, `xlrd` का उपयोग करें:
```
pip install xlrd
```

### बुनियादी उपयोग
Pandas, Excel डेटा को DataFrame में लोड करने के लिए `pd.read_excel()` फ़ंक्शन प्रदान करता है।

1. pandas को इम्पोर्ट करें:
   ```python
   import pandas as pd
   ```

2. Excel फ़ाइल पढ़ें (फ़ाइल पथ निर्दिष्ट करें):
   ```python
   df = pd.read_excel('path/to/your/file.xlsx')
   ```
   - यह डिफ़ॉल्ट रूप से पहली शीट लोड करता है।
   - परिणाम एक DataFrame होता है जिसमें Excel डेटा होता है।

3. डेटा का निरीक्षण करें:
   ```python
   print(df.head())  # पहली 5 पंक्तियाँ देखें
   print(df.info())  # कॉलम और डेटा प्रकारों का सारांश
   ```

### उन्नत विकल्प
- **कोई शीट निर्दिष्ट करें**: `sheet_name` पैरामीटर का उपयोग करें (पहली शीट के लिए डिफ़ॉल्ट 0 है):
  ```python
  df = pd.read_excel('file.xlsx', sheet_name='Sheet2')  # नाम से
  df = pd.read_excel('file.xlsx', sheet_name=1)        # इंडेक्स से (0-आधारित)
  ```
- **एकाधिक शीट पढ़ें**: सभी शीट को डिक्शनरी के रूप में लोड करने के लिए एक लिस्ट या `None` पास करें:
  ```python
  all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # शीट नाम से कुंजीबद्ध DataFrames का डिक्शनरी
  ```
- **डेटा रेंज निर्दिष्ट करें**: कॉलम के लिए `usecols` (उदा. कॉलम A से C के लिए `'A:C'`) और प्रारंभिक पंक्तियों को छोड़ने के लिए `skiprows` का उपयोग करें:
  ```python
  df = pd.read_excel('file.xlsx', usecols='A,C,E', skiprows=2)
  ```
- **हेडर हैंडल करें**: यदि हेडर row 0 में नहीं है, तो `header` के साथ निर्दिष्ट करें:
  ```python
  df = pd.read_excel('file.xlsx', header=1)  # हेडर row 1 में (0-आधारित इंडेक्स)
  ```
- **इंडेक्स सेट करें**: किसी कॉलम को इंडेक्स के रूप में सेट करने के लिए `index_col` का उपयोग करें:
  ```python
  df = pd.read_excel('file.xlsx', index_col='Column Name')
  ```

### उदाहरण
मान लीजिए आपके पास एक Excel फ़ाइल `sales.xlsx` है जिसमें "Data" नामक एक शीट है जिसमें सेल्स डेटा है।

```python
import pandas as pd

# विशिष्ट शीट पढ़ें
df = pd.read_excel('sales.xlsx', sheet_name='Data')

# DataFrame प्रदर्शित करें
print(df)

# CSV में सेव करें यदि आवश्यक हो
df.to_csv('sales.csv', index=False)
```

अधिक जानकारी के लिए, [pandas documentation on read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) देखें। यदि आपको त्रुटियाँ मिलती हैं, तो Excel फ़ाइल फॉर्मेट जांचें और सुनिश्चित करें कि आवश्यक पैकेज इंस्टॉल हैं।