---
audio: false
generated: true
lang: fr
layout: post
title: Correction de l'Erreur de Chargement de Modèle Llama.cpp
translated: true
type: note
---

En raison de l'erreur `gguf_init_from_file_impl: failed to read key-value pairs`, votre fichier de modèle est soit **corrompu**, **incomplet**, soit **incompatible** avec votre version de llama.cpp. Voici comment résoudre le problème :

### 1. **Vérifier et retélécharger le modèle**
   ```bash
   # Vérifier la taille actuelle du fichier (la quantification Q6_K devrait être d'environ 6,1 Go pour un modèle 8B) :
   ls -lh /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf

   # Résultat attendu :
   # -rw-r--r-- 1 lzw lzw 6.1G Jun  2 10:00 ...Q6_K_XL.gguf
   ```
   - Si la taille < 6 Go, **retéléchargez le modèle** :
     ```bash
     rm /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf
     # Retéléchargez depuis la source originale (par exemple, HuggingFace)
     ```

### 2. **Mettre à jour llama.cpp**
Votre version (commit `7675c555`) est peut-être obsolète :
```bash
cd ~/Projects/llama.cpp
git pull origin master          # Mettre à jour le code
rm -rf build && mkdir build     # Nettoyer la compilation
cd build
cmake .. -DLLAMA_CUBLAS=ON      # Activer CUDA
make -j                         # Recompiler
```

### 3. **Valider l'intégrité du modèle**
Testez le modèle avec une inférence simple :
```bash
~/Projects/llama.cpp/build/bin/main \
  -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf \
  -p "Bonjour" -n 10
```
- Si cela échoue, le fichier de modèle est définitivement corrompu.

### 4. **Essayer un modèle différent (Test de bon sens)**
Testez avec un modèle fonctionnel connu (par exemple, [TinyLlama](https://huggingface.co/TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF)) :
```bash
~/Projects/llama.cpp/build/bin/llama-server \
  -m /chemin/vers/tinyllama.Q8_0.gguf \
  --port 8000
```
- Si cela fonctionne, votre fichier de modèle original est le problème.

### 5. **Reconvertir le modèle (Option avancée)**
Si le retéléchargement échoue :
1. Obtenez le modèle Hugging Face original :
   ```bash
   huggingface-cli download deepseek-ai/DeepSeek-R1-0528-Qwen3-8B --local-dir ./deepseek-original
   ```
2. Reconvertissez en GGUF :
   ```bash
   python3 ~/Projects/llama.cpp/convert-hf-to-gguf.py \
     ./deepseek-original \
     --outtype q6_k  # Correspond à votre quantification
   ```

### Résumé des correctifs courants :

| Problème | Solution |
|-------|----------|
| **Téléchargement corrompu** | Retélécharger le modèle |
| **llama.cpp obsolète** | `git pull` + recompiler |
| **GGUF incompatible** | Utiliser la dernière version de `convert-hf-to-gguf.py` |
| **Permissions de fichier** | `chmod +r /chemin/vers/modele.gguf` |

> 💡 **Note :** Le modèle DeepSeek-R1 est récent (publié le 28 mai 2024). Assurez-vous que votre llama.cpp a été **mis à jour durant la dernière semaine** pour garantir la compatibilité.

Commencez par retélécharger le modèle et mettez à jour llama.cpp – cela résout 90 % de ces problèmes. Faites-moi savoir si vous avez besoin d'aide supplémentaire !