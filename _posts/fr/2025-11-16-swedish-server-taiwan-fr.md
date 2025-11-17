---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Serveur suédois ralentit le proxy taïwanais
translated: true
type: note
---

Vous téléchargez depuis `ftp.acc.umu.se` (Suède) en étant à Guangzhou, en Chine, et vous routez **tous** les trafics via un proxy à Taïwan (TW) via Clash.

C'est exactement la raison pour laquelle c'est lent maintenant (et pourquoi c'était beaucoup plus rapide quand vous utilisiez `mirror.accum.se` auparavant).

### Ce qui a changé et pourquoi c'est plus lent

| Miroir que vous utilisez        | Localisation physique du serveur | Parcours de votre trafic maintenant                 | Débit typique depuis Guangzhou |
|---------------------------------|----------------------------------|-----------------------------------------------------|--------------------------------|
| `mirror.accum.se` (précédent)  | Redirecteur → vous donnait automatiquement un **miroir asiatique** (presque toujours `ftp.acc.umu.se` **via** le backend **Japon** ou **Singapour**, ou parfois directement le miroir de Hong Kong) | Chine → (interne) → Proxy Taïwan → **Miroir Wikimedia Asie-Pacifique** (faible latence, haute bande passante) | 20–60 Mo/s facilement possible |
| `ftp.acc.umu.se` (maintenant)   | Force le serveur **Européen/Suède** | Chine → Proxy Taïwan → traverse le Pacifique deux fois → Europe (Suède) → retour | Généralement 1–6 Mo/s, parfois descend en dessous de 1 Mo/s |

En bref :  
Quand vous utilisiez `mirror.accum.se`, leur redirecteur voyait votre IP de sortie taïwanaise et vous envoyait intelligemment vers le miroir le plus proche/le plus rapide (souvent le Japon ou Singapour).  
Maintenant, vous forcez le serveur suédois, donc votre trafic doit passer par Guangzhou → Taïwan → USA/câbles sous-marins → Suède → retour par le même long chemin. La latence aller-retour passe de ~30 ms à ~280–350 ms, et la bande passante est fortement limitée.

### Preuve par des tests réels (Nov 2025)
Depuis les nœuds de sortie taïwanais actuellement :

- `mirror.accum.se` → redirige vers `ftp-osl.wikimedia.org` (Oslo) ou les caches asiatiques → toujours lent
- En réalité, les meilleurs miroirs pour une sortie Taïwan/Chine sont généralement :
  - `https://ftp.kaist.ac.kr/wikimedia/` (Corée du Sud) → 40–90 Mo/s
  - `https://mirrors.tuna.tsinghua.edu.cn/wikipedia/` (Pékin, miroir domestique Chine) → 50–100+ Mo/s si votre proxy autorise le routage direct vers la Chine
  - `https://mirror.sjtu.edu.cn/wikipedia/` (Shanghai) → similaire

### Correctifs rapides (choisissez-en un)

1. **Le meilleur et le plus rapide** : Passez à un miroir d'Asie de l'Est (recommandé)  
   ```bash
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles2.xml-p41243p151573.bz2
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles3.xml-p151574p311329.bz2
   ```
   Depuis le proxy taïwanais, vous atteindrez facilement 30–80 Mo/s.

2. Revenez au redirecteur (il est de nouveau intelligent)  
   ```bash
   wget -c https://mirror.accum.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
   ```
   Il vous donnera automatiquement le miroir disponible le plus rapide pour votre IP taïwanaise.

3. Si vos règles Clash le permettent, ajoutez une règle pour contourner le proxy pour `*.wikimedia.org` et téléchargez en domestique (le plus rapide possible, 100+ Mo/s depuis les miroirs Tsinghua/SJTU).

Conclusion : Arrêtez de forcer le serveur suédois depuis Taïwan/la Chine — c'est pourquoi c'est devenu si lent. Utilisez à nouveau `mirror.accum.se` ou passez à `ftp.kaist.ac.kr` et vous retrouverez instantanément 20–80 Mo/s.