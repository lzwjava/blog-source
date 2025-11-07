---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تدقيق نموذج
translated: true
type: post
---

```python
import os
import glob
import json
من مكتبة النقاط البيضاء import load_dotenv
من مكتبة التحولات import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling, LlamaTokenizerFast
من مجموعة البيانات import Dataset, load_dataset
import torch

load_dotenv()

اسم_النموذج = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"  # تم تغييره الى النموذج المحدد
دليل_الاخراج = "trained_model"
ملف_التدريب = "train.jsonl"
حد_الطول_القصوى = 512
حجم_الدفعة = 8
العوارض = 3

def إنشاء_بيانات_التدريب(دليل_المنشورات):
    جميع_النصوص = []
    for دليل_اللغة in os.listdir(دليل_المنشورات):
        دليل_اللغة = os.path.join(دليل_المنشورات, دليل_اللغة)
        if not os.path.isdir(دليل_اللغة):
            استمر
        for مسار_الملف in glob.glob(os.path.join(دليل_اللغة, "*.md")):
            نشطه_بالقراءة_في_الملف = سعة_فتح(مسار_الملف, 'r', encoding='utf-8')
            محتوى = القراءة.read()
            # تبديل بيانات البداية
            محتوى = محتوى.split("---", 2)[-1].strip()
            النصوص.append(محتوى)
        except Exception as e:
            print(f"خطأ في قراءة الملف {مسار_الملف}: {e}")
    return النصوص

def إعداد_مجموعة_البيانات(نصوص, توكنايزر):
    تشفير = توكنايزر(نصوص, truncation=True, padding=True, max_length=MAX_LENGTH, return_tensors="pt")
    استرجاع مجموعة_البيانات.from_dict(تشفير)

def تدريب_النموذج(مجموعة_البيانات, توكنايزر):
    الإعدادات_التدريبية = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        save_steps=10_000,
        save_total_limit=2,
        prediction_loss_only=True,
        remove_unused_columns=False,
    )
    النموذج = AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True)
    جمع_البيانات = DataCollatorForLanguageModeling(توكنايزر=توكنايزر, mlm=False)
    المدرب = Trainer(
        model=النموذج,
        args=الإعدادات_التدريبية,
        train_dataset=مجموعة_البيانات,
        data_collator=جمع_البيانات,
    )
    المدرب.train()
    المدرب.save_model(OUTPUT_DIR)

def من_خلال():
    دليل_المنشورات = "_posts"
    النصوص = إنشاء_بيانات_التدريب(دليل_المنشورات)
    التوكنايزر = LlamaTokenizerFast.from_pretrained(MODEL_NAME, trust_remote_code=True, use_fast=True)
    التوكنايزر.pad_token = التوكنايزر.eos_token
    مجموعة_البيانات = إعداد_مجموعة_البيانات(النصوص, التوكنايزر)
    تدريب_النموذج(مجموعة_البيانات, التوكنايزر)

if __name__ == "__main__":
    من_خلال()

```