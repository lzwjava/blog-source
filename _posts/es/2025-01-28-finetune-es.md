---
audio: true
lang: es
layout: post
title: Ajustar un modelo
translated: true
---

```python
import os
import glob
import json
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling, LlamaTokenizerFast
from datasets import Dataset, load_dataset
import torch

load_dotenv()

NOMBRE_MODELO = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"  # Cambiado al modelo especificado
DIR_SALIDA = "modelo_entrenado"
ARCHIVO_ENTRENAMIENTO = "train.jsonl"
LONGITUD_MAXIMA = 512
TAMANO_LOT = 8
EPOCAS = 3

def crear_datos_entrenamiento(posts_dir):
    todos_textos = []
    for dir_lang in os.listdir(posts_dir):
        ruta_lang = os.path.join(posts_dir, dir_lang)
        if not os.path.isdir(ruta_lang):
            continue
        for ruta_archivo in glob.glob(os.path.join(ruta_lang, "*.md")):
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    # Eliminar front matter
                    contenido = contenido.split("---", 2)[-1].strip()
                    todos_textos.append(contenido)
            except Exception as e:
                print(f"Error al leer archivo {ruta_archivo}: {e}")
    return todos_textos

def preparar_conjunto_datos(textos, tokenizer):
    codificaciones = tokenizer(textos, truncation=True, padding=True, max_length=LONGITUD_MAXIMA, return_tensors="pt")
    return Dataset.from_dict(codificaciones)

def entrenar_modelo(conjunto_datos, tokenizer):
    args_entrenamiento = TrainingArguments(
        output_dir=DIR_SALIDA,
        overwrite_output_dir=True,
        num_train_epochs=EPOCAS,
        per_device_train_batch_size=TAMANO_LOT,
        save_steps=10_000,
        save_total_limit=2,
        prediction_loss_only=True,
        remove_unused_columns=False,
    )
    modelo = AutoModelForCausalLM.from_pretrained(NOMBRE_MODELO, trust_remote_code=True)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    trainer = Trainer(
        model=modelo,
        args=args_entrenamiento,
        train_dataset=conjunto_datos,
        data_collator=data_collator,
    )
    trainer.train()
    trainer.save_model(DIR_SALIDA)

def main():
    posts_dir = "_posts"
    textos = crear_datos_entrenamiento(posts_dir)
    tokenizer = LlamaTokenizerFast.from_pretrained(NOMBRE_MODELO, trust_remote_code=True, use_fast=True)
    tokenizer.pad_token = tokenizer.eos_token
    conjunto_datos = preparar_conjunto_datos(textos, tokenizer)
    entrenar_modelo(conjunto_datos, tokenizer)

if __name__ == "__main__":
    main()

```