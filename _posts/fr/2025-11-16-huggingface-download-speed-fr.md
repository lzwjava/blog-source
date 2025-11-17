---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Solutions pour la Vitesse de Téléchargement de Hugging Face
translated: true
type: note
---

Votre problème est très typique pour les personnes en Chine continentale (surtout dans le sud comme Guangzhou) lors du téléchargement de gros fichiers depuis Hugging Face.

### Pourquoi sans proxy → extrêmement lent (~200–300 Ko/s)
- Même si vous utilisez **hf-mirror.com** (le miroir chinois officiel géré par HF + 01.AI), les véritables gros fichiers parquet de FineWeb **ne sont pas mis en cache en Chine**.
- hf-mirror.com vous redirige simplement vers le CDN global (qui utilise maintenant xet-bridge sur AWS us-east-1).
- Depuis Guangzhou sans proxy → votre trafic passe par les passerelles internationales (backbone China Telecom/Unicom/Mobile → AWS aux États-Unis), et les téléchargements de gros fichiers sont fortement limités ou soumis à de la QoS. Les fichiers de 2 Go tombent facilement à < 500 Ko/s, parfois même 100 Ko/s.

### Pourquoi avec le proxy Clash → soudainement très rapide (souvent 20–100 Mo/s)
- Votre Clash utilise presque certainement un nœud à Hong Kong, Taïwan, Japon, Singapour ou Corée (très courant pour les utilisateurs de Guangzhou).
- Ces nœuds ont :
  - Un peering direct ou une très bonne connectivité vers AWS us-east-1 (ou Cloudflare qu'HF utilise aussi)
  - Aucune limitation du GFW sur le trafic sortant
  - Une bande passante bien plus élevée
- Donc, même si vous faites un "détour" par le proxy, le chemin réel est beaucoup plus rapide que la sortie internationale directe depuis la Chine continentale.

### En bref
Direct (même via hf-mirror.com) depuis Guangzhou → lent car le stockage réel est toujours aux États-Unis, et la bande passante Chine → États-Unis pour les gros fichiers est terrible en 2025.
Proxy Clash (nœud HK/TW/JP/SG) → rapide car ces nœuds ont une excellente connectivité vers AWS aux États-Unis.

### Solutions recommandées (de la plus rapide à la plus lente)

1. **Continuez à utiliser Clash (ou v2rayN, Surge, etc.) avec un nœud HK/TW/JP à faible latence** — c'est actuellement la méthode la plus rapide en Chine continentale pour FineWeb, RedPajama, The Stack, etc.

2. Utilisez **le point de terminaison accéléré officiel d'HF en Chine** (fonctionne sans aucun proxy pour beaucoup de gens en 2024-2025) :
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```
   Ensuite, utilisez directement huggingface-cli ou la bibliothèque datasets (pas wget). De nombreux utilisateurs en Chine rapportent des vitesses de 50 à 200 Mo/s de cette manière maintenant, car HF a commencé à mettre en cache plus de fragments sur Aliyun/Tencent Cloud en 2025.

3. Utilisez **FastGit + hugger** ou les miroirs **openi/pkulaw** (certains fragments sont mis en cache en Chine) :
   Exemple :
   ```bash
   pip install hugger
   hugger download HuggingFaceFW/fineweb --revision main --include "CC-MAIN-2013-20/*.parquet"
   ```

4. Gardez wget + hf-mirror.com mais forcez le passage par votre proxy Clash (ce que vous faites déjà).

### Commande rapide pour télécharger n'importe quel fragment de FineWeb rapidement depuis Guangzhou
```bash
# Définir le proxy HTTP de Clash (port généralement 7890)
export https_proxy=http://127.0.0.1:7890

# Puis utilisez aria2 (beaucoup plus rapide + reprise que wget)
aria2c -x16 -s16 -k1M "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet"
```

Vous obtiendrez facilement 30–100 Mo/s selon votre nœud proxy.

Donc, en conclusion : en Chine continentale en 2025, pour les fichiers >1 Go sur Hugging Face, utiliser un proxy HK/TW/JP est presque toujours plus rapide qu'une connexion directe, même en utilisant hf-mirror.com. C'est simplement la réalité de la bande passante internationale depuis la Chine actuellement.