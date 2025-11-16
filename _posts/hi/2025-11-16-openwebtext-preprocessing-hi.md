---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ओपनवेबटेक्स्ट डेटासेट प्रीप्रोसेसिंग स्क्रिप्ट
translated: true
type: note
---

### अवलोकन
यह पायथन स्क्रिप्ट ओपनवेबटेक्स्ट डेटासेट (वेब-स्क्रैप किए गए टेक्स्ट का एक संग्रह, जो जीपीटी-2 जैसे मॉडल को ट्रेन करने के लिए उपयोग किए जाने वाले डेटा के समान है) वाली एक बड़ी टेक्स्ट फ़ाइल को प्रोसेस करती है। इसका लक्ष्य है:
- कच्चे टेक्स्ट को प्रबंधनीय "दस्तावेज़ों" (टेक्स्ट के हिस्सों) में विभाजित करना।
- आसान हैंडलिंग के लिए एक हगिंग फेस `Dataset` ऑब्जेक्ट बनाना।
- टेक्स्ट को टिकटोकन से जीपीटी-2 बाइट पेयर एन्कोडिंग (बीपीई) टोकनाइज़र का उपयोग करके टोकनाइज़ करना (विशेष टोकन्स को नज़रअंदाज़ करते हुए और टेक्स्ट-समाप्ति मार्कर जोड़ना)।
- डेटासेट को प्रशिक्षण (99.95%) और सत्यापन (0.05%) सेट में विभाजित करना।
- टोकनाइज़ किए गए डेटा को नम्पी की मेमोरी-मैप्ड ऐरे का उपयोग करके कॉम्पैक्ट बाइनरी फ़ाइलों (`train.bin` और `val.bin`) के रूप में सहेजना। ये फ़ाइलें मशीन लर्निंग प्रशिक्षण के दौरान कुशल लोडिंग के लिए टोकन आईडी (16-बिट इंटीजर के रूप में) के अनुक्रम संग्रहीत करती हैं।

यह स्क्रिप्ट मल्टी-कोर सिस्टम पर दक्षता के लिए डिज़ाइन की गई है, जो टोकनाइज़ेशन के लिए मल्टीप्रोसेसिंग का उपयोग करती है। यह फ्लैश अटेंशन रिपॉजिटरी (कोड में लिंक किया गया) के एक डेटा लोडिंग मॉड्यूल से प्रेरित है, जो भाषा मॉडल प्रशिक्षण के लिए समान प्रीप्रोसेसिंग को हैंडल करता है। नोट: ओपनवेबटेक्सट बहुत बड़ा है (~40GB अनकंप्रेस्ड), लेकिन यह स्क्रिप्ट एक पहले से डाउनलोड की गई, स्थानीय `openwebtext.txt` फ़ाइल मानती है। आउटपुट फ़ाइलें बहुत छोटी हैं: `train.bin` ~17GB (9B टोकन) और `val.bin` ~8.5MB (4M टोकन)।

स्क्रिप्ट शुरुआत में प्रॉक्सी सेटिंग्स प्रिंट करती है (संभवतः किसी भी अंतर्निहित डाउनलोड के दौरान नेटवर्क समस्याओं को डीबग करने के लिए, हालांकि यहां कोई स्पष्ट डाउनलोड नहीं है)। यह डिफ़ॉल्ट रूप से टोकनाइज़ेशन के लिए 8 वर्कर प्रोसेस का उपयोग करती है।

### चरण-दर-चरण विवरण

#### 1. इम्पोर्ट्स और प्रारंभिक सेटअप
```python
import os
import tarfile
from tqdm import tqdm
import numpy as np
import tiktoken
from huggingface_hub import hf_hub_download
from datasets import load_dataset # huggingface datasets
import datasets

print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))

# number of workers in .map() call
# good number to use is ~order number of cpu cores // 2
num_proc = 8

# number of workers in load_dataset() call
# best number might be different from num_proc above as it also depends on NW speed.
# it is better than 1 usually though
num_proc_load_dataset = num_proc

enc = tiktoken.get_encoding("gpt2")

datasets.logging.set_verbosity_info()
```
- **उद्देश्य**: फ़ाइल हैंडलिंग (`os`, `tarfile`), प्रोग्रेस बार (`tqdm`), न्यूमेरिकल ऑपरेशन (`numpy`), टोकनाइज़ेशन (`tiktoken`), और हगिंग फेस यूटिलिटीज (`huggingface_hub`, `datasets`) के लिए लाइब्रेरीज़ इम्पोर्ट करता है।
- **प्रॉक्सी प्रिंट**: एचटीटीपी/एचटीटीपीएस प्रॉक्सी के लिए एनवायरनमेंट वेरिएबल लॉग करता है, उपयोगी यदि स्क्रिप्ट को नेटवर्क प्रतिबंधों का सामना करना पड़े (जैसे टोकनाइज़र मॉडल डाउनलोड करने के लिए, हालांकि टिकटोकन इसे आंतरिक रूप से हैंडल करता है)।
- **वर्कर्स**: टोकनाइज़ेशन में समानांतर प्रोसेसिंग के लिए `num_proc=8` सेट करता है (संतुलन के लिए लगभग सीपीयू कोर की आधी संख्या)। `num_proc_load_dataset` इससे मेल खाता है लेकिन यहां उपयोग नहीं किया गया है (प्रेरणा कोड से बचा हुआ, जो हगिंग फेस से लोड करता है)।
- **एनकोडर**: जीपीटी-2 बीपीई टोकनाइज़र (`enc`) लोड करता है। यह टेक्स्ट को इंटीजर टोकन आईडी (0–50,256 रेंज) में बदलता है।
- **लॉगिंग**: प्रोसेसिंग के दौरान वर्बोज़ आउटपुट के लिए हगिंग फेस डेटासेट्स लॉगिंग को "इन्फो" लेवल पर सेट करता है।

`if __name__ == '__main__':` गार्ड यह सुनिश्चित करता है कि मुख्य लॉजिक तभी चले जब स्क्रिप्ट को सीधे निष्पादित किया जाए (इम्पोर्ट नहीं किया गया हो)।

#### 2. टेक्स्ट फ़ाइल को पढ़ना और विभाजित करना
```python
if __name__ == '__main__':
    # Read the local openwebtext.txt file
    txt_file = os.path.join(os.path.dirname(__file__), 'openwebtext.txt')
    print(f"Reading from local file: {txt_file}")

    # Read the text content
    texts = []
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        # Read the entire file
        full_text = f.read().strip()

        # Try to split into documents by double newlines first
        documents = full_text.split('\n\n')

        # If we only got one document, split by single newlines
        if len(documents) <= 1:
            documents = full_text.split('\n')

        # If we still only have one document, split by period followed by space
        if len(documents) <= 1:
            # Split on period followed by space, then join back sentences
            sentences = full_text.split('. ')
            # Group sentences into chunks of ~100 sentences per document
            chunk_size = 100
            for i in range(0, len(sentences), chunk_size):
                chunk = '. '.join(sentences[i:i+chunk_size])
                if chunk.strip():
                    texts.append(chunk.strip() + '.')
        else:
            # Process documents from double/single newline splits
            for doc in documents:
                doc = doc.strip()
                if doc:  # Only add non-empty documents
                    texts.append(doc)

        print(f"Created {len(texts)} documents from the text file")
```
- **फ़ाइल रीडिंग**: `openwebtext.txt` (माना जाता है कि स्क्रिप्ट के समान डायरेक्टरी में है) को यूटीएफ-8 मोड में खोलता है, एन्कोडिंग एरर को नज़रअंदाज़ करते हुए। संपूर्ण सामग्री को `full_text` में पढ़ता है और व्हाइटस्पेस हटाता है।
- **विभाजन लॉजिक**: टेक्स्ट को "दस्तावेज़ों" (तार्किक हिस्से जैसे पैराग्राफ या लेख) में विभाजित करने का प्रयास करता है:
  - **प्राथमिक**: डबल न्यूलाइन्स (`\n\n`) द्वारा विभाजित करें, जो कॉर्पोरा में दस्तावेज़ों को अलग करने के लिए आम है।
  - **फॉलबैक 1**: यदि उससे ≤1 हिस्सा मिलता है (जैसे, कोई डबल न्यूलाइन नहीं), तो लाइन-आधारित टेक्स्ट के लिए सिंगल न्यूलाइन्स (`\n`) द्वारा विभाजित करें।
  - **फॉलबैक 2**: यदि फिर भी ≤1 हिस्सा रहता है (जैसे, टेक्स्ट का एक ही ब्लॉक), तो `. ` (पीरियड + स्पेस) द्वारा वाक्यों में विभाजित करें, फिर प्रत्येक 100 वाक्यों को एक "दस्तावेज़" हिस्से में समूहित करें। यह बहुत लंबी एकल प्रविष्टियों को रोकता है। पूर्णता के लिए प्रत्येक हिस्से के अंत में एक पीरियड जोड़ता है।
- **आउटपुट**: गैर-खाली, साफ किए गए दस्तावेज़ों को `texts` सूची में संग्रहीत करता है। बनाई गई कुल संख्या प्रिंट करता है (जैसे, एक सबसेट के लिए 10k उदाहरण)।
- **यह तरीका क्यों?** ओपनवेबटेक्स्ट वेब पेजों का संयोजन है, इसलिए विभाजन से प्रशिक्षण उदाहरण बनते हैं जो केवल कच्चे डंप नहीं होते। यह उस तरह की नकल करता है जैसे बुककॉर्पस जैसे डेटासेट प्रोसेस किए जाते हैं।

#### 3. डेटासेट बनाना और विभाजित करना
```python
    # Create dataset from texts
    dataset = datasets.Dataset.from_dict({'text': texts})

    # create train/val split from the 10k examples
    split_dataset = dataset.train_test_split(test_size=0.0005, seed=2357, shuffle=True)
    split_dataset['val'] = split_dataset.pop('test') # rename the test split to val
```
- **डेटासेट निर्माण**: `texts` सूची को एक हगिंग फेस `Dataset` में लपेटता है जिसमें एक ही कॉलम `'text'` होता है। यह मैपिंग जैसे कुशल समानांतर ऑपरेशन सक्षम करता है।
- **विभाजन**: प्रशिक्षण (99.95%) और परीक्षण (0.05%) सेट में विभाजित करने के लिए `train_test_split` का उपयोग करता है। छोटा सत्यापन आकार बड़े डेटासेट के लिए जानबूझकर है—कम्प्यूट बर्बाद किए बिना मूल्यांकन के लिए पर्याप्त।
  - `test_size=0.0005`: वैल के लिए 0.05% (जैसे, 100k से ~50 उदाहरण)।
  - `seed=2357`: पुनरुत्पादनशीलता के लिए फिक्स्ड रैंडम सीड।
  - `shuffle=True`: विभाजन से पहले यादृच्छिक करता है।
- **नाम बदलना**: `'test'` को पॉप करता है और वैल का नाम बदलता है। अब `split_dataset` `'train'` और `'val'` कुंजियों वाली एक डिक्शनरी है, प्रत्येक एक `Dataset` ऑब्जेक्ट।

#### 4. टोकनाइज़ेशन फ़ंक्शन
```python
    # we now want to tokenize the dataset. first define the encoding function (gpt2 bpe)
    def process(example):
        ids = enc.encode_ordinary(example['text']) # encode_ordinary ignores any special tokens
        ids.append(enc.eot_token) # add the end of text token, e.g. 50256 for gpt2 bpe
        # note: I think eot should be prepended not appended... hmm. it's called "eot" though...
        out = {'ids': ids, 'len': len(ids)}
        return out
```
- **उद्देश्य**: मॉडल इनपुट के लिए टेक्स्ट को टोकन आईडी में बदलता है।
- **`encode_ordinary`**: टेक्स्ट स्ट्रिंग को इंटीजर (जीपीटी-2 वोकैब) की सूची में टोकनाइज़ करता है। टेक्स्ट में किसी भी गैर-मानक टोकन को नज़रअंदाज़ करता है।
- **ईओटी जोड़ें**: अंत में एंड-ऑफ-टेक्स्ट टोकन (जीपीटी-2 के लिए आईडी 50256) जोड़ता है। यह प्रशिक्षण के दौरान अनुक्रम की सीमा का संकेत देता है। (टिप्पणी प्रीपेंड बनाम अपेंड बहस पर सवाल उठाती है, लेकिन अपेंडिंग सीज़ुअल एलएम सेटअप जैसे जीपीटी में आम है।)
- **आउटपुट**: `'ids'` (टोकन आईडी की सूची) और `'len'` (अनुक्रम लंबाई, बाद में जोड़ने के लिए) वाली एक डिक्शनरी लौटाता है।

#### 5. टोकनाइज़ेशन लागू करना
```python
    # tokenize the dataset
    tokenized = split_dataset.map(
        process,
        remove_columns=['text'],
        desc="tokenizing the splits",
        num_proc=num_proc,
    )
```
- **मैपिंग**: समानांतर वर्कर्स (`num_proc=8`) का उपयोग करके ट्रेन/वैल डेटासेट में प्रत्येक उदाहरण पर `process` लागू करता है।
- **`remove_columns=['text']`**: मेमोरी बचाने के लिए मूल टेक्स्ट को हटा देता है (अब हमें केवल टोकन चाहिए)।
- **प्रोग्रेस**: `desc` के माध्यम से एक प्रोग्रेस बार दिखाता है। एन्कोडिंग के कारण बड़े डेटासेट के लिए यह चरण समय ले सकता है।

#### 6. टोकनाइज़्ड डेटा को बाइनरी फ़ाइलों में सहेजना
```python
    # concatenate all the ids in each dataset into one large file we can use for training
    for split, dset in tokenized.items():
        arr_len = np.sum(dset['len'], dtype=np.uint64)
        filename = os.path.join(os.path.dirname(__file__), f'{split}.bin')
        dtype = np.uint16 # (can do since enc.max_token_value == 50256 is < 2**16)
        arr = np.memmap(filename, dtype=dtype, mode='w+', shape=(arr_len,))

        # Use adaptive batch size based on dataset size
        total_batches = min(1024, len(dset))
        if total_batches < 1024:
            print(f"Using {total_batches} batches for {split} dataset (size: {len(dset)})")

        idx = 0
        for batch_idx in tqdm(range(total_batches), desc=f'writing {filename}'):
            # Only process if this batch index is valid for the dataset size
            if batch_idx < len(dset):
                # Batch together samples for faster write
                batch = dset.shard(num_shards=total_batches, index=batch_idx, contiguous=True).with_format('numpy')
                arr_batch = np.concatenate(batch['ids'])
                # Write into mmap
                arr[idx : idx + len(arr_batch)] = arr_batch
                idx += len(arr_batch)
        arr.flush()
```
- **स्प्लिट्स पर लूप**: `'train'` और `'val'` के लिए, `'len'` फ़ील्ड को जोड़कर कुल टोकन गिनती (`arr_len`) की गणना करता है।
- **मेमोरी-मैप्ड ऐरे**: एक नम्पी मेममैप फ़ाइल (`train.bin` या `val.bin`) बनाता है जो uint16 इंटीजर की एक लिखने योग्य ऐरे के रूप में होती है (जीपीटी-2 के 50,256 अधिकतम टोकन मान के अनुकूल; int32 की तुलना में ~50% स्थान बचाती है)। आकार 1डी है: `(total_tokens,)`।
- **दक्षता के लिए बैचिंग**: एक साथ सब कुछ रैम में लोड करने से बचने के लिए डेटासेट को अधिकतम 1024 शार्ड्स (`total_batches`) में विभाजित करता है। छोटे डेटासेट (<1024 उदाहरण) के लिए, सटीक संख्या का उपयोग करता है।
  - **`shard`**: डेटासेट को सन्निकट बैचों में विभाजित करता है (यहां कोई शफलिंग नहीं)।
  - **`with_format('numpy')`**: तेज संयोजन के लिए बैच को नम्पी ऐरे में बदलता है।
- **लिखना**: प्रत्येक बैच से टोकन आईडी को संयोजित करता है और उन्हें `idx` से शुरू होकर मेममैप ऐरे में क्रमिक रूप से कॉपी करता है। `tqdm` के साथ प्रगति को ट्रैक करता है।
- **`flush()`**: यह सुनिश्चित करता है कि सभी डेटा डिस्क पर लिखा गया है।
- **बाइनरी/मेममैप क्यों?** ये फ़ाइलें बहुत बड़ी हैं लेकिन स्ट्रीम करने योग्य हैं। प्रशिक्षण के दौरान, आप उन्हें `np.memmap('train.bin', dtype=np.uint16, mode='r')` के साथ लोड कर सकते हैं बिना सब कुछ मेमोरी में लोड किए।

#### 7. आउटपुट और उपयोग पर टिप्पणियाँ
```python
    # train.bin is ~17GB, val.bin ~8.5MB
    # train has ~9B tokens (9,035,582,198)
    # val has ~4M tokens (4,434,897)

    # to read the bin files later, e.g. with numpy:
    # m = np.memmap('train.bin', dtype=np.uint16, mode='r')
```
- ये पूर्ण ओपनवेबटेक्स्ट के लिए उदाहरण आकार हैं (आपकी स्थानीय फ़ाइल भिन्न हो सकती है)।
- **रीडिंग टिप**: रीड-ओनली एक्सेस के लिए मेममैप का उपयोग करें। प्रशिक्षण लूप में, आप फ्लैट ऐरे से यादृच्छिक प्रारंभिक सूचकांकों को नमूना सकते हैं और निश्चित-लंबाई अनुक्रम (जैसे, 1024 टोकन) पढ़ सकते हैं।

### संभावित समस्याएं और नोट्स
- **मेमोरी उपयोग**: बहुत बड़ी फ़ाइलों (40GB+) के लिए पूर्ण `openwebtext.txt` को रैम में पढ़ना विफल हो सकता है। आवश्यकता पड़ने पर स्ट्रीमिंग रीड पर विचार करें।
- **ईओटी प्लेसमेंट**: टिप्पणी अपेंडिंग बनाम प्रीपेंडिंग ईओटी पर सवाल उठाती है; व्यवहार में, अपेंडिंग ऑटोरेग्रेसिव मॉडल के लिए काम करती है (यह सामग्री के बाद अंत को चिह्नित करती है)।
- **कस्टमाइज़ेशन**: एक स्थानीय फ़ाइल मानता है; प्रेरणा कोड हगिंग फेस से डाउनलोड करता है, लेकिन यह संस्करण स्थानीय रूप से पढ़ता है (तेज़, कोई ऑथ की आवश्यकता नहीं)।
- **निर्भरताएं**: `tiktoken`, `datasets`, `numpy`, `tqdm` की आवश्यकता है। गायब होने पर पिप के माध्यम से इंस्टॉल करें।
- **स्केलेबिलिटी**: वास्तविक ओपनवेबटेक्स्ट के लिए, 64GB+ रैम और फास्ट स्टोरेज (एसएसडी) वाली मशीन पर चलाएं। 10k-उदाहरण विभाजन से पता चलता है कि यह किसी सबसेट के लिए हो सकता है।

यह स्क्रिप्ट कच्चे टेक्स्ट को प्रशिक्षण-तैयार प्रारूप में बदल देती है, जो जीपीटी जैसे भाषा मॉडल के लिए अनुकूलित है। यदि आपके पास इसे संशोधित करने के बारे में प्रश्न हैं (जैसे अलग टोकनाइज़र या चंक आकार), तो मुझे बताएं!