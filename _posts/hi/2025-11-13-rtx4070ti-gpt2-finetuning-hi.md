---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: आरटीएक्स 4070 टीआई जीपीटी-2 फाइन-ट्यूनिंग गाइड
translated: true
type: note
---

## अपना वातावरण सेट करना

प्रशिक्षण से पहले, सुनिश्चित करें कि आपका NVIDIA RTX 4070 Ti ठीक से सेट अप है। इस GPU में 12GB VRAM है, जो फाइन-ट्यूनिंग के दौरान GPT-2 Small (124M पैरामीटर्स) के लिए पर्याप्त से अधिक है। OpenWebText जैसे बड़े डेटासेट पर स्क्रैच से प्रशिक्षण एकल कंज्यूमर GPU पर समय और कंप्यूट आवश्यकताओं के कारण अव्यावहारिक है—इसमें हफ्तों या महीनों लग सकते हैं। इसके बजाय, विशिष्ट कार्यों के लिए अपने स्वयं के डेटासेट पर पहले से प्रशिक्षित मॉडल को फाइन-ट्यून करने पर ध्यान दें।

### 1. NVIDIA ड्राइवर और CUDA इंस्टॉल करें
- अपने RTX 4070 Ti के लिए नवीनतम NVIDIA ड्राइवर आधिकारिक NVIDIA वेबसाइट से डाउनलोड और इंस्टॉल करें। सुनिश्चित करें कि यह पूर्ण संगतता के लिए संस्करण 535 या उच्चतर है।
- CUDA टूलकिट इंस्टॉल करें। RTX 4070 Ti (कंप्यूट क्षमता 8.9) CUDA 12.x को सपोर्ट करता है। CUDA 12.4 की सिफारिश की जाती है:
  - NVIDIA CUDA टूलकिट आर्काइव से डाउनलोड करें।
  - अपने OS (Windows/Linux) के लिए इंस्टॉलेशन गाइड का पालन करें।
- अपने CUDA संस्करण से मेल खाने वाला cuDNN (CUDA डीप न्यूरल नेटवर्क लाइब्रेरी) इंस्टॉल करें (उदाहरण के लिए, CUDA 12.4 के लिए cuDNN 8.9)।
- इंस्टॉलेशन सत्यापित करें:
  ```
  nvidia-smi  # आपका GPU और CUDA संस्करण दिखाना चाहिए
  nvcc --version  # CUDA इंस्टॉलेशन की पुष्टि करता है
  ```

### 2. Python वातावरण सेट करें
- Python 3.10 या 3.11 का उपयोग करें। आसान प्रबंधन के लिए Anaconda या Miniconda के माध्यम से इंस्टॉल करें।
- एक वर्चुअल एनवायरनमेंट बनाएं:
  ```
  conda create -n gpt2-train python=3.10
  conda activate gpt2-train
  ```

### 3. आवश्यक लाइब्रेरीज इंस्टॉल करें
- CUDA सपोर्ट के साथ PyTorch इंस्टॉल करें। CUDA 12.4 के लिए:
  ```
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  ```
  सत्यापित करें:
  ```
  python -c "import torch; print(torch.cuda.is_available())"  # True लौटाना चाहिए
  ```
- Hugging Face लाइब्रेरीज और अन्य इंस्टॉल करें:
  ```
  pip install transformers datasets accelerate sentencepiece pandas tqdm
  ```

## अपना डेटासेट तैयार करना
- एक टेक्स्ट डेटासेट चुनें या तैयार करें (उदाहरण के लिए, एक .txt फ़ाइल जिसमें प्रति लाइन एक नमूना हो या 'text' कॉलम वाली एक CSV)।
- उदाहरण के लिए, Hugging Face Datasets से एक सार्वजनिक डेटासेट का उपयोग करें:
  ```python
  from datasets import load_dataset
  dataset = load_dataset("bookcorpus")  # या आपका कस्टम डेटासेट: load_dataset("text", data_files="your_data.txt")
  ```
- यदि आवश्यक हो तो train/test में विभाजित करें:
  ```python
  dataset = dataset["train"].train_test_split(test_size=0.1)
  ```

## GPT-2 Small को फाइन-ट्यून करना
सरलता के लिए Hugging Face Transformers लाइब्रेरी का उपयोग करें। यहां कॉजल लैंग्वेज मॉडलिंग (अगले टोकन की भविष्यवाणी) के लिए एक संपूर्ण स्क्रिप्ट दी गई है।

### स्क्रिप्ट उदाहरण
इसे `train_gpt2.py` के रूप में सेव करें और `python train_gpt2.py` के साथ रन करें।

```python
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# टोकनाइज़र और मॉडल लोड करें (GPT-2 Small)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # पैडिंग टोकन सेट करें
model = GPT2LMHeadModel.from_pretrained("gpt2")

# डेटासेट लोड और प्रीप्रोसेस करें (अपने डेटासेट से बदलें)
dataset = load_dataset("bookcorpus")
dataset = dataset["train"].train_test_split(test_size=0.1)

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512, padding="max_length")

tokenized_dataset = dataset.map(preprocess, batched=True, remove_columns=["text"])

# लैंग्वेज मॉडलिंग के लिए डेटा कलेक्टर
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# प्रशिक्षण तर्क (सिंगल GPU के लिए ऑप्टिमाइज़्ड)
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=4,  # VRAM के आधार पर समायोजित करें; OOM से बचने के लिए कम से शुरू करें
    per_device_eval_batch_size=4,
    num_train_epochs=3,  # आवश्यकतानुसार समायोजित करें
    weight_decay=0.01,
    fp16=True,  # तेज प्रशिक्षण और कम VRAM के लिए मिश्रित परिशुद्धता
    gradient_accumulation_steps=4,  # प्रभावी बैच आकार = batch_size * accumulation_steps
    save_steps=1000,
    logging_steps=500,
    report_to="none",  # या ट्रैकिंग के लिए "wandb"
)

# ट्रेनर
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    data_collator=data_collator,
)

# प्रशिक्षण दें
trainer.train()

# मॉडल सेव करें
trainer.save_model("./gpt2-finetuned")
```

### प्रशिक्षण चलाना
- दूसरे टर्मिनल में `nvidia-smi` के साथ GPU उपयोग की निगरानी करें।
- यदि आपको आउट-ऑफ-मेमोरी (OOM) एरर्स आती हैं:
  - `per_device_train_batch_size` को 2 या 1 तक कम करें।
  - प्रभावी बैच आकार बनाए रखने के लिए `gradient_accumulation_steps` बढ़ाएं।
  - छोटा max_length (उदाहरण के लिए, 512 के बजाय 256) उपयोग करें।
- प्रशिक्षण समय: 4070 Ti पर, एक मध्यम आकार के डेटासेट (उदाहरण के लिए, 100k नमूनों) के लिए, बैच आकार के आधार पर प्रति युग 1-5 घंटे की उम्मीद करें।

## मूल्यांकन और अनुमान
प्रशिक्षण के बाद:
```python
from transformers import pipeline

generator = pipeline("text-generation", model="./gpt2-finetuned", device=0)  # GPU के लिए device=0
output = generator("आपका प्रॉम्प्ट यहाँ", max_length=50, num_return_sequences=1)
print(output)
```

- पर्प्लेक्सिटी का मूल्यांकन करें (कम बेहतर है):
  ```python
  import math
  eval_results = trainer.evaluate()
  perplexity = math.exp(eval_results["eval_loss"])
  print(f"Perplexity: {perplexity}")
  ```

## सुझाव और समस्या निवारण
- VRAM बचाने और प्रशिक्षण की गति बढ़ाने के लिए मिश्रित परिशुद्धता (`fp16=True`) का उपयोग करें।
- यदि स्क्रैच से प्रशिक्षण देना है (अनुशंसित नहीं): एक कस्टम ट्रांसफॉर्मर आर्किटेक्चर लागू करें (उदाहरण के लिए, NanoGPT या इसी तरह के रेपो के माध्यम से) और एक विशाल डेटासेट का उपयोग करें, लेकिन बहुत लंबे रनटाइम की अपेक्षा रखें।
- बड़े डेटासेट के लिए, यदि आपके पास एकाधिक GPU हैं तो वितरित प्रशिक्षण का उपयोग करें, लेकिन यह एकल 4070 Ti से परे है।
- सामान्य समस्याएं: यदि PyTorch GPU का पता नहीं लगाता है, तो ड्राइवर/CUDA को पुनः इंस्टॉल करें। सुनिश्चित करें कि कोई अन्य प्रक्रिया GPU का उपयोग नहीं कर रही है।

## संदर्भ
- [Fine-Tuning GPT-2: A Practical Guide](https://mr-amit.medium.com/fine-tuning-gpt-2-a-practical-guide-2805b4af738b)
- [Training GPT-2 From Scratch: A Step-by-Step Guide](https://youssefh.substack.com/p/training-gpt-2-from-scratch-a-step)
- [How To Train Your Own GenAI Model](https://developer.squareup.com/blog/how-to-train-your-own-genai-model/)
- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
- [RTX 4070 CUDA version](https://www.reddit.com/r/pytorch/comments/1kwb5fh/rtx_4070_cuda_version/)
- [Geforce RTX 4070 Ti Super CUDA support for Deep Learning](https://forums.developer.nvidia.com/t/geforce-rtx-4070-ti-super-cuda-support-for-deep-learning/282154)
- [CUDA compatibility with RTX 4070](https://forums.developer.nvidia.com/t/cuda-compatibility-with-rtx-4070/287989)