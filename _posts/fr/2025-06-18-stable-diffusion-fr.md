---
audio: false
generated: true
lang: fr
layout: post
title: Problème de Proxy Stable Diffusion
translated: true
type: note
---

Sur base de l'erreur et de votre environnement, voici comment résoudre le problème "Unknown scheme for proxy URL" :

### Solution :
L'erreur se produit car **`httpx` ne prend pas en charge les proxies `socks://` par défaut**. Vous avez deux options :

#### Option 1 : Supprimer la référence au proxy SOCKS
1. Vérifiez les variables d'environnement pour des paramètres de proxy indésirables :
   ```bash
   env | grep -i proxy
   ```
   Recherchez les références `socks://` (en particulier `ALL_PROXY` ou `http_proxy`).

2. Désactivez la variable problématique (remplacez `VAR_NAME` par le nom réel trouvé ci-dessus) :
   ```bash
   unset VAR_NAME  # par exemple, unset ALL_PROXY
   ```

#### Option 2 : Ajouter la prise en charge de SOCKS à `httpx`
1. Activez votre environnement virtuel Python :
   ```bash
   source /home/lzw/Projects/stable-diffusion-webui/venv/bin/activate
   ```

2. Installez les dépendances requises :
   ```bash
   pip install -U "httpx[socks]"
   ```

3. Désactivez l'environnement :
   ```bash
   deactivate
   ```

### Pourquoi cela arrive :
- Vos proxies principaux (`HTTP_PROXY/HTTPS_PROXY`) utilisent `http://` (supporté), mais quelque chose (probablement une autre application/script) définit un proxy `socks://` que `httpx` ne peut pas gérer sans paquets supplémentaires.
- La stack trace montre que Gradio/`httpx` essaie d'utiliser `socks://127.0.0.1:7891`, qui n'apparaît pas dans votre sortie `checkproxy`.

### Vérification :
Après correction, exécutez :
```bash
./webui.sh
```
L'erreur de proxy SOCKS devrait disparaître.

> 💡 **Note** : Si vous n'avez pas intentionnellement configuré un proxy SOCKS, vérifiez les applications qui pourraient configurer automatiquement les proxies (par exemple, les VPN, les gestionnaires de réseau, ou les fichiers de configuration du shell comme `~/.bashrc`).

---

L'erreur `Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check` indique que PyTorch, utilisé par Stable Diffusion WebUI, ne peut pas détecter ou accéder à un GPU compatible. Cela est probablement dû à des bibliothèques CUDA manquantes, un GPU incompatible, des problèmes de pilote ou un problème de configuration. Voici les étapes pour résoudre ce problème, adaptées à votre environnement (glibc 2.35, Python 3.10.12, GCC 11.4.0, probablement Ubuntu 22.04 basé sur la version de glibc).

### Étapes pour résoudre le problème

#### 1. **Vérifier la compatibilité du GPU et de CUDA**
   - **Vérifiez si vous avez un GPU NVIDIA** :
     Exécutez :
     ```bash
     lspci | grep -i nvidia
     ```
     Cela liste le matériel NVIDIA. Si rien n'apparaît, votre système peut ne pas avoir de GPU NVIDIA, et PyTorch nécessite un GPU NVIDIA pour la prise en charge CUDA.
   - **Vérifiez l'installation du pilote NVIDIA** :
     Exécutez :
     ```bash
     nvidia-smi
     ```
     Si installé, cela affiche un tableau avec les détails du GPU (par exemple, version du pilote, version CUDA). Sinon, installez le pilote NVIDIA :
     ```bash
     sudo apt-get update
     sudo apt-get install nvidia-driver-<version> nvidia-utils-<version> -y
     ```
     Remplacez `<version>` par le dernier pilote stable (par exemple, `535` ou `550`). Trouvez la version appropriée du pilote avec :
     ```bash
     ubuntu-drivers devices
     sudo ubuntu-drivers autoinstall
     ```
   - **Vérifiez la version de CUDA** :
     PyTorch nécessite les bibliothèques CUDA. Vérifiez la version de CUDA installée :
     ```bash
     nvcc --version
     ```
     Si non installé, installez le CUDA Toolkit :
     ```bash
     sudo apt-get install nvidia-cuda-toolkit -y
     ```
     Alternativement, téléchargez le dernier CUDA Toolkit depuis le site web de NVIDIA (par exemple, CUDA 11.8 ou 12.1) et suivez leur guide d'installation.

#### 2. **Vérifier l'installation de PyTorch**
   L'erreur suggère que PyTorch est installé mais ne peut pas utiliser le GPU. Assurez-vous d'avoir la bonne version de PyTorch avec la prise en charge CUDA.
   - **Vérifiez l'installation de PyTorch** :
     Exécutez :
     ```bash
     python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
     ```
     Le résultat attendu devrait inclure une version de PyTorch (par exemple, `2.0.1`) et `True` pour `torch.cuda.is_available()`. Si `False`, PyTorch ne détecte pas le GPU.
   - **Réinstallez PyTorch avec la prise en charge CUDA** :
     Pour Python 3.10 et CUDA (par exemple, 11.8), installez PyTorch dans votre environnement Stable Diffusion :
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```
     Remplacez `cu118` par votre version de CUDA (par exemple, `cu121` pour CUDA 12.1). Vérifiez les versions supportées sur le site officiel de PyTorch.
   - **Vérifiez après réinstallation** :
     Exécutez à nouveau la vérification :
     ```bash
     python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
     ```

#### 3. **Contourner la vérification CUDA (Solution temporaire)**
   Si vous voulez exécuter Stable Diffusion sans prise en charge GPU (par exemple, pour tester sur CPU), contournez la vérification CUDA en ajoutant `--skip-torch-cuda-test` aux arguments de ligne de commande.
   - Modifiez `webui-user.sh` (ou créez-le s'il n'existe pas) :
     ```bash
     nano /home/lzw/Projects/stable-diffusion-webui/webui-user.sh
     ```
     Ajoutez ou modifiez la ligne `COMMANDLINE_ARGS` :
     ```bash
     export COMMANDLINE_ARGS="--skip-torch-cuda-test"
     ```
     Sauvegardez et quittez.
   - Exécutez le script :
     ```bash
     ./webui.sh
     ```
     Cela permet à Stable Diffusion de s'exécuter sur CPU, mais les performances seront considérablement plus lentes.

#### 4. **S'assurer que TCMalloc est correctement configuré**
   Votre sortie montre que TCMalloc (`libtcmalloc_minimal.so.4`) est détecté et lié avec `LD_PRELOAD`. Confirmez son fonctionnement :
   ```bash
   echo $LD_PRELOAD
   ```
   Si le résultat est `/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4`, c'est bon. Sinon, définissez-le manuellement :
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```
   Ou ajoutez-le à `webui-user.sh` :
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```

#### 5. **Vérifier les variables d'environnement et les chemins**
   Assurez-vous que votre environnement est correctement configuré :
   - **Vérifiez LD_LIBRARY_PATH** :
     Les bibliothèques CUDA doivent être accessibles. Ajoutez-les si nécessaire :
     ```bash
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     Ajoutez ceci à `~/.bashrc` ou `webui-user.sh` pour la persistance.
   - **Activez l'environnement virtuel** :
     Activez toujours l'environnement virtuel Stable Diffusion avant l'exécution :
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     ```

#### 6. **Mettre à jour Stable Diffusion WebUI**
   Votre version (`v1.10.1`, commit `82a973c`) peut avoir des problèmes de compatibilité. Mettez à jour vers la dernière version :
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   git pull
   ```
   Puis, réinstallez les dépendances :
   ```bash
   ./webui.sh
   ```

#### 7. **Dépannage**
   - **Si `nvidia-smi` échoue** : Réinstallez le pilote NVIDIA ou vérifiez les problèmes matériels du GPU.
   - **Si PyTorch ne détecte toujours pas le GPU** :
     - Assurez-vous que CUDA et cuDNN sont installés correctement. Installez cuDNN si manquant :
       ```bash
       sudo apt-get install libcudnn8
       ```
     - Vérifiez la compatibilité de la version CUDA avec votre GPU et PyTorch. Par exemple, les anciens GPU (par exemple, série Kepler) peuvent ne pas supporter CUDA 12.
   - **Si les erreurs persistent** : Vérifiez les logs de Stable Diffusion pour des erreurs détaillées :
     ```bash
     cat /home/lzw/Projects/stable-diffusion-webui/log/webui.log
     ```
     Partagez toute erreur spécifique pour une assistance supplémentaire.
   - **Limitations matérielles** : Si votre GPU est trop ancien (par exemple, GPU NVIDIA d'avant 2016), il peut ne pas supporter les versions modernes de CUDA. Dans ce cas, utilisez `--skip-torch-cuda-test` ou mettez à niveau votre GPU.

#### 8. **Exécuter l'application**
   Après avoir appliqué les correctifs, exécutez la WebUI :
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   ./webui.sh
   ```
   Si vous avez résolu le problème GPU, l'erreur devrait disparaître. Si vous utilisez `--skip-torch-cuda-test`, elle s'exécutera sur CPU.

### Notes
- **Informations système** : Votre configuration (glibc 2.35, Python 3.10.12, GCC 11.4.0) suggère Ubuntu 22.04, qui est compatible avec CUDA 11.8 ou 12.1 et les versions récentes de PyTorch.
- **Performances** : L'exécution sur CPU (avec `--skip-torch-cuda-test`) est une solution de repli mais sera lente. Il est recommandé de corriger la prise en charge GPU pour Stable Diffusion.
- **TCMalloc** : Le problème TCMalloc semble résolu sur base de votre sortie. Assurez-vous que `LD_PRELOAD` reste défini si vous rencontrez des problèmes liés à la mémoire.

Si vous rencontrez toujours des problèmes ou avez besoin d'aide avec des messages d'erreur spécifiques, veuillez fournir des détails supplémentaires (par exemple, modèle du GPU, version de CUDA, ou logs complets), et je peux affiner la solution !