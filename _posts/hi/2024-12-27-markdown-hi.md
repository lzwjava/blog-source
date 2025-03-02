---
audio: false
generated: false
lang: hi
layout: post
title: 'मार्कडेन समस्याएँ: Kramdown और XeLaTeX'
translated: true
---

अपने Jekyll ब्लॉग के लिए Markdown का उपयोग करके PDF जनरेट करने के लिए, मैं निम्नलिखित Pandoc कमांड का उपयोग करता हूँ:

```python
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '--resource-path=.:assets',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]
```

Kramdown और XeLaTeX दोनों का समर्थन करना

जब आप Markdown लिख रहे होते हैं जो kramdown (Jekyll HTML आउटपुट के लिए) और XeLaTeX (Pandoc के माध्यम से PDF आउटपुट के लिए) के साथ काम करने की आवश्यकता होती है, तो कुछ बातों का ध्यान रखना चाहिए:

1. छवि पथ संगतता
	•	Kramdown (HTML): संपत्तियों को संदर्भित करने के लिए / से शुरू होने वाले पथों को प्राथमिकता देता है।
	•	XeLaTeX (PDF): अग्रणी / के बिना सापेक्ष पथों को प्राथमिकता देता है।

समाधान: दोनों के लिए काम करने वाले सापेक्ष पथों का उपयोग करें:

```
![](assets/images/chatgpt/block.jpg)
```

2. kramdown एट्रिब्यूट्स को संभालना
	•	{:.responsive} kramdown के लिए विशिष्ट है और HTML आउटपुट को स्टाइल करने के लिए उपयोग किया जाता है।
	•	XeLaTeX इन एट्रिब्यूट्स को सपोर्ट नहीं करता है और इससे त्रुटि उत्पन्न होगी।

समाधान: PDF जनरेशन के लिए इरादा किए गए Markdown में kramdown-विशिष्ट विशेषताओं को हटा दें। उदाहरण के लिए:

```markdown
<!-- Kramdown-specific -->
```
![](assets/images/chatgpt/block.jpg){: .responsive }
```
```

<!-- दोनों के साथ संगत -->
```
![](assets/images/chatgpt/block.jpg)
```

यदि {:.responsive} आपके Jekyll HTML लेआउट के लिए महत्वपूर्ण है, तो इसे वेब आउटपुट के लिए चुनिंदा रूप से जोड़ने पर विचार करें, जबकि PDF जनरेशन प्रक्रिया में इसे छोड़ दें।

द्वैध संगतता के लिए वर्कफ़्लो

1.	kramdown-विशिष्ट सुविधाओं पर न्यूनतम निर्भरता के साथ Markdown सामग्री लिखें।
2.	HTML में उन्नत स्टाइलिंग के लिए, Markdown में इनलाइन के बजाय अपने Jekyll टेम्पलेट्स में सीधे CSS क्लासेस लागू करें।
3.	Markdown पोर्टेबिलिटी को बनाए रखते हुए PDF फ़ॉर्मेटिंग को नियंत्रित करने के लिए Pandoc विकल्पों का उपयोग करें।

इन प्रथाओं का पालन करके, Markdown सामग्री Jekyll HTML रेंडरिंग और XeLaTeX PDF जनरेशन में संगत रहती है, जिससे बहु-प्रारूप प्रकाशन के लिए एक सहज वर्कफ़्लो सुनिश्चित होता है।