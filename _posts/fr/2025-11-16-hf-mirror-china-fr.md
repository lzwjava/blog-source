---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Utiliser hf-mirror.com en Chine
translated: true
type: note
---

### Comprendre hf-mirror.com
hf-mirror.com est un miroir géré par la communauté du Hub Hugging Face officiel (huggingface.co), conçu spécifiquement pour aider les utilisateurs en Chine (y compris Guangzhou) à contourner les restrictions réseau et à télécharger plus rapidement les modèles d'IA et les jeux de données. Il réplique la structure complète des dépôts, vous permettant ainsi d'accéder à des modèles comme GPT-2 ou à des jeux de données comme WikiText sans avoir à accéder directement au site original, qui est souvent lent ou bloqué. Étant donné que vous utilisez souvent le proxy Clash, notez que hf-mirror.com est hébergé en Chine et ne nécessite généralement pas de proxy pour y accéder — il est optimisé pour une utilisation directe en Chine. Si vous proxyfiez déjà le trafic via Clash, vous pouvez soit acheminer le trafic vers hf-mirror.com directement (pour éviter des sauts inutiles), soit le maintenir sous proxy si vous préférez.

### Configuration de base : Utilisation du miroir
La clé est de définir la variable d'environnement `HF_ENDPOINT` pour pointer vers le miroir. Cela fonctionne globalement pour les outils Hugging Face comme la bibliothèque `transformers`, `huggingface-cli`, ou `hfd` (un téléchargeur plus rapide). Faites cela **avant** d'importer les bibliothèques ou d'exécuter les téléchargements.

#### 1. Définir la variable d'environnement
- **Sur Linux/macOS (permanent)** : Ajoutez à votre `~/.bashrc` ou `~/.zshrc` :
  ```
  echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
  source ~/.bashrc
  ```
- **Sur Windows (PowerShell, permanent)** : Exécutez une fois :
  ```
  [System.Environment]::SetEnvironmentVariable('HF_ENDPOINT', 'https://hf-mirror.com', 'User')
  ```
  Puis redémarrez votre terminal.
- **Temporaire (tout OS)** : Préfixez les commandes comme suit :
  ```
  HF_ENDPOINT=https://hf-mirror.com your_command_here
  ```

Cela redirige tous les téléchargements Hugging Face vers le miroir sans modifier votre code.

#### 2. Installer les outils requis
- Installez le CLI Hugging Face Hub (pour les téléchargements) :
  ```
  pip install -U huggingface_hub
  ```
- Pour des téléchargements encore plus rapides, utilisez `hfd` (Hugging Face Downloader, utilise aria2 pour des vitesses multi-threads) :
  ```
  wget https://hf-mirror.com/hfd/hfd.sh  # Ou téléchargez via le navigateur
  chmod +x hfd.sh
  ```

#### 3. Téléchargement de modèles ou de jeux de données
- **Utilisation de huggingface-cli** (prend en charge la reprise en cas d'interruption) :
  ```
  # Télécharger un modèle (par exemple, GPT-2)
  huggingface-cli download gpt2 --resume-download --local-dir ./gpt2

  # Télécharger un jeu de données (par exemple, WikiText)
  huggingface-cli download --repo-type dataset wikitext --resume-download --local-dir ./wikitext
  ```
- **Utilisation de hfd** (plus rapide, surtout pour les gros fichiers) :
  ```
  # Modèle
  ./hfd.sh gpt2

  # Jeu de données
  ./hfd.sh wikitext --dataset
  ```
- **Dans le code Python** (par exemple, avec la bibliothèque transformers) :
  ```python
  import os
  os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # Définir avant les imports

  from transformers import AutoModel, AutoTokenizer
  model = AutoModel.from_pretrained('gpt2')  # Télécharge depuis le miroir automatiquement
  tokenizer = AutoTokenizer.from_pretrained('gpt2')
  ```
  Exécutez avec : `HF_ENDPOINT=https://hf-mirror.com python your_script.py`

#### 4. Gestion des modèles avec accès restreint/connecté
Certains modèles (par exemple, Llama-2) nécessitent un compte Hugging Face et un token :
- Connectez-vous sur huggingface.co (utilisez votre proxy Clash si le site est bloqué).
- Générez un token sur https://huggingface.co/settings/tokens.
- Téléchargez avec :
  ```
  huggingface-cli download --token hf_YourTokenHere meta-llama/Llama-2-7b-hf --resume-download --local-dir ./Llama-2-7b-hf
  ```
  Ou pour hfd :
  ```
  ./hfd.sh meta-llama/Llama-2-7b-hf --hf_username your_username --hf_token hf_YourTokenHere
  ```

### Intégration avec le proxy Clash
Étant donné que hf-mirror.com est un miroir chinois, il devrait être accessible sans Clash (la connexion directe est plus rapide). Cependant, si vous souhaitez le proxyfier (par exemple, pour des raisons de cohérence ou si vous rencontrez des problèmes), configurez Clash pour acheminer le trafic vers hf-mirror.com via votre groupe de proxy préféré. Clash n'a pas besoin de configuration "HF" spéciale — il est système.

#### Conseils de configuration rapide pour Clash
- Assurez-vous que Clash est en cours d'exécution et défini comme proxy système (dans Clash : Allez dans "General" > Activez "System Proxy").
- **Acheminer hf-mirror.com directement (recommandé pour la vitesse)** : Modifiez votre configuration YAML de Clash (généralement `config.yaml` dans le dossier de Clash). Ajoutez une règle pour contourner le proxy pour le miroir :
  ```
  rules:
    # ... vos règles existantes ...
    - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # Contourne le proxy, passe en direct
    # ... reste des règles ...
  ```
  Rechargez la configuration dans Clash (Profiles > Reload).
- **Le proxyfier si nécessaire** : Si vous préférez l'acheminer via Clash, n'ajoutez pas de règle spéciale — il suivra votre règle par défaut (par exemple, `MATCH,Proxy`). Testez en pingant hf-mirror.com dans un navigateur avec Clash activé/désactivé.
- Pour les téléchargements : Exécutez les commandes dans un terminal où le proxy système est actif (Clash s'en occupe). Si vous utilisez Python, les bibliothèques comme `requests` (utilisée par transformers) respectent les variables d'environnement `HTTP_PROXY`/`HTTPS_PROXY` définies par Clash (par exemple, `http://127.0.0.1:7890` pour le port HTTP).
- Test : Essayez de télécharger un petit modèle comme `distilbert-base-uncased`. Si c'est lent, désactivez Clash pour le trafic hf-mirror.com.

### Dépannage
- **Les téléchargements atteignent-ils toujours huggingface.co ?** Assurez-vous que `HF_ENDPOINT` est défini **avant** d'importer toute bibliothèque HF (redémarrez votre notebook/terminal).
- **Vitesses lentes ?** Utilisez `hfd` avec aria2 (il prend en charge les connexions multiples). Ou vérifiez votre réseau — les utilisateurs de Guangzhou obtiennent souvent 10-50 Mo/s sur hf-mirror.com.
- **Erreurs avec les jeux de données ?** Certains ont des scripts personnalisés ; modifiez-les pour utiliser `https://hf-mirror.com` comme URL de base.
- **Spécifique à Windows** : Si vous utilisez Anaconda, définissez la variable d'environnement dans l'environnement de base.
- Pour l'hébergement local avancé d'un miroir (si vous voulez un contrôle total), consultez des outils open-source comme Olah ou hf-mirror-site sur GitHub, mais commencez par le miroir public.

Cette configuration devrait vous permettre de télécharger de manière fiable. Si vous rencontrez des erreurs spécifiques, partagez la sortie pour obtenir plus d'aide !

### Références
- [Guide Officiel HF-Mirror](https://hf-mirror.com/)
- [Documentation Hugging Face Hub sur les Endpoints](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#huggingface_hub_constants.HF_ENDPOINT)
- [Téléchargeur hfd](https://hf-mirror.com/hfd/hfd.sh)
- [Règles de configuration Clash](https://github.com/Dreamacro/clash/wiki/Configuration#rules)
- [Stack Overflow : Téléchargement en Chine](https://stackoverflow.com/questions/77388822/how-to-download-huggingface-bert-base-uncased-in-china)