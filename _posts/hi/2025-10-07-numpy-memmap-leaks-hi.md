---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: NumPy मेममैप मेमोरी लीक्स का समाधान
translated: true
type: note
---

### Stack Overflow पोस्ट क्या कहती है

यह पोस्ट NumPy के `np.memmap` के साथ एक सामान्य समस्या पर चर्चा करती है, जो डिस्क पर संग्रहीत बड़े डेटासेट को प्रोसेस करते समय आती है। मूल प्रश्न एक विशाल मैट्रिक्स (उदाहरण के लिए, shuffled indices के माध्यम से) पर पंक्तियों को chunks में पढ़ने के लिए iterate करने का वर्णन करता है, लेकिन यह देखता है कि इस प्रक्रिया के दौरान RAM और virtual memory का उपयोग लगातार बढ़ता जाता है, जिससे सिस्टम धीमा हो जाता है—भले ही प्रत्येक पंक्ति केवल एक बार एक्सेस की जाती है। पूछने वाला memory usage को केवल current chunk तक सीमित रखना चाहता है और generator-based iteration या direct file I/O (यह नोट करते हुए कि बाद वाला धीमा है) जैसे विकल्पों के लिए पूछता है।

लिंक किए गए उत्तर (ID 61472122, accepted) इस "memory leak" को NumPy के memmap द्वारा caching के लिए पूरे array को memory में retain करने के रूप में पहचानता है, भले ही read-only mode और single-pass access हो। यह दो समाधान प्रस्तावित करता है:

1.  **प्रति chunk memmap ऑब्जेक्ट को फिर से बनाएं**: प्रत्येक batch या chunk के लिए `np.memmap` को delete करें और फिर से initialize करें। यह पूरे array के RAM में build up होने से रोकता है, जिससे usage कम (chunk size से बंधा) रहता है। पुनर्निर्माण से minor CPU overhead होती है, लेकिन यह नगण्य है। उदाहरण कोड:
    ```python:disable-run
    def process_chunks(data_filename, chunk_size=4096):
        for start in range(0, total_size, chunk_size):
            # हर बार memmap को ताजा बनाएं
            data = np.memmap(data_filename, dtype=np.float32, mode='r', shape=full_shape)
            # केवल current chunk को प्रोसेस करें
            chunk = data[start:start + chunk_size]
            # ... काम करें ...
            del data  # स्पष्ट रूप से discard करें
    ```

2.  **OS memory advice के साथ custom mmap**: memmap में अंतर्निहित `mmap` ऑब्जेक्ट तक पहुंचें और Python 3.8+ के `madvise` (जैसे, `MADV_DONTNEED` या `MADV_DONTDUMP`) का उपयोग करके OS को unused pages को release करने के लिए कहें। यह अधिक low-level है लेकिन पुनर्निर्माण overhead से बचाता है। इसमें mmap तक पहुंचने के लिए NumPy के source से code snippets शामिल हैं।

उत्तर fixes को verify करने के लिए `memory-profiler` जैसे profiling tools का उपयोग करने की सलाह देता है।

### NanoGPT इस दृष्टिकोण का उपयोग क्यों करता है

NanoGPT (भाषा मॉडल प्रशिक्षण के लिए एक minimal GPT implementation) से प्रदान किए गए कोड में, `get_batch` फ़ंक्शन के अंदर `np.memmap` का पुनर्निर्माण उस उत्तर के पहले समाधान का ठीक अनुसरण करता है—बड़े binary files (जैसे, tokenized training data) से repeated batch sampling के दौरान memory leak से बचने के लिए।

NanoGPT विशाल datasets (जैसे अरबों tokens) पर प्रशिक्षण लेता है, इसलिए पूरी फ़ाइल को memory में लोड करना संभव नहीं है। इसके बजाय, यह efficient disk access के लिए memmap का उपयोग करता है, लेकिन पुनर्निर्माण के बिना, memory epochs के साथ बढ़ती जाएगी क्योंकि NumPy फ़ाइल के अधिक से अधिक हिस्से को cache करता जाता है। प्रति batch ताजा remapping करके (`if split == 'train': data = np.memmap(...)` लाइनों के माध्यम से), यह सुनिश्चित करता है कि RAM usage कम और स्थिर रहे—यह limited hardware जैसे single GPU पर लंबे training runs के लिए critical है। comment स्पष्ट रूप से इस "memory leak avoidance" trick का श्रेय SO पोस्ट को देती है। यह data loader को lightweight रखता है, साथ ही x/y input-target pairs के लिए random sampling (`torch.randint`) को सक्षम बनाता है।

[Stack Overflow: numpy memmap memory usage - want to iterate once](https://stackoverflow.com/questions/45132940/numpy-memmap-memory-usage-want-to-iterate-once/61472122#61472122)
```