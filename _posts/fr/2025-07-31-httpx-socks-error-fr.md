---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Schéma de proxy non pris en charge
translated: true
type: note
---

L'erreur indique que la bibliothèque `httpx`, utilisée par le client `openai` dans votre script `gitmessageai.py`, tente de configurer un proxy avec l'URL `socks://127.0.0.1:7891/`, mais le schéma `socks` n'est pas supporté ou reconnu, ce qui entraîne une `ValueError: Unknown scheme for proxy URL`. Cela suggère qu'une configuration de proxy est récupérée depuis votre environnement ou votre code, et qu'elle utilise un schéma de proxy SOCKS non supporté.

Décomposons d'où le proxy pourrait provenir et comment le corriger.

### D'où Vient le Proxy ?

La configuration du proxy (`socks://127.0.0.1:7891/`) provient probablement de l'un des endroits suivants :

1. **Variables d'Environnement**
   - La bibliothèque `httpx` vérifie automatiquement les paramètres de proxy dans les variables d'environnement comme `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY` ou leurs équivalents en minuscules (`http_proxy`, `https_proxy`, `all_proxy`).
   - Une valeur comme `socks://127.0.0.1:7891/` suggère qu'un proxy SOCKS (courant pour des outils comme Shadowsocks ou les VPN) a été défini dans une de ces variables.
   - Pour vérifier si ces variables sont définies, exécutez la commande suivante dans votre terminal :
     ```bash
     env | grep -i proxy
     ```
     Recherchez des variables comme `HTTP_PROXY=socks://127.0.0.1:7891` ou `HTTPS_PROXY=socks://127.0.0.1:7891`.

2. **Paramètres de Proxy Système**
   - Si vous utilisez un système Linux, les paramètres de proxy pourraient être configurés globalement (par exemple, dans `/etc/environment`, `/etc/profile`, ou votre configuration de shell comme `~/.bashrc`, `~/.zshrc`, ou `~/.profile`).
   - Vérifiez ces fichiers pour des lignes comme :
     ```bash
     export HTTP_PROXY="socks://127.0.0.1:7891"
     export HTTPS_PROXY="socks://127.0.0.1:7891"
     ```
   - Vous pouvez visualiser ces fichiers avec :
     ```bash
     cat ~/.bashrc | grep -i proxy
     cat ~/.zshrc | grep -i proxy
     cat /etc/environment | grep -i proxy
     ```

3. **Configuration dans un Outil de Proxy**
   - L'adresse `127.0.0.1:7891` est couramment utilisée par des outils de proxy ou VPN comme Shadowsocks, V2Ray, ou Clash, qui utilisent souvent des proxies SOCKS5 sur des ports comme 7890 ou 7891.
   - Si vous avez installé ou configuré un tel outil, il a pu définir automatiquement des variables d'environnement ou des paramètres de proxy système.

4. **Proxy Explicite dans le Code**
   - Bien que moins probable, votre script `gitmessageai.py` ou une bibliothèque qu'il utilise pourrait configurer explicitement un proxy. Étant donné que l'erreur se produit dans `httpx`, vérifiez si votre script passe un proxy au client `OpenAI` ou au client `httpx`.
   - Recherchez dans votre script les termes comme `proxy`, `proxies`, ou `httpx.Client` :
     ```bash
     grep -r -i proxy /home/lzwjava/bin/gitmessageai.py
     ```

5. **Configuration de la Bibliothèque Python**
   - Certaines bibliothèques Python (par exemple, `requests` ou `httpx`) pourraient hériter des paramètres de proxy depuis un fichier de configuration ou une configuration précédente. Cependant, `httpx` s'appuie principalement sur les variables d'environnement ou le code explicite.

### Pourquoi `socks://` Provoque-t-il un Problème ?

- La bibliothèque `httpx` (utilisée par `openai`) ne supporte pas nativement le schéma `socks` (proxies SOCKS4/SOCKS5) à moins que des dépendances supplémentaires comme `httpx-socks` ne soient installées.
- L'erreur `Unknown scheme for proxy URL` se produit car `httpx` attend des proxies avec des schémas comme `http://` ou `https://`, et non `socks://`.

### Comment Corriger le Problème

Vous avez deux options : **supprimer ou contourner le proxy** s'il n'est pas nécessaire, ou **supporter le proxy SOCKS** si vous souhaitez l'utiliser.

#### Option 1 : Supprimer ou Contourner le Proxy

Si vous n'avez pas besoin d'un proxy pour l'API DeepSeek, vous pouvez désactiver ou contourner la configuration du proxy.

1. **Désactiver les Variables d'Environnement**
   - Si le proxy est défini dans les variables d'environnement, désactivez-les pour votre session :
     ```bash
     unset HTTP_PROXY
     unset HTTPS_PROXY
     unset ALL_PROXY
     unset http_proxy
     unset https_proxy
     unset all_proxy
     ```
   - Pour rendre cela permanent, supprimez les lignes `export` correspondantes de `~/.bashrc`, `~/.zshrc`, `/etc/environment`, ou d'autres fichiers de configuration du shell.

2. **Exécuter le Script Sans Proxy**
   - Exécutez temporairement votre script sans les paramètres de proxy :
     ```bash
     HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
     ```
   - Si cela fonctionne, le proxy était bien la cause du problème.

3. **Contourner le Proxy dans le Code**
   - Modifiez votre script `gitmessageai.py` pour désactiver explicitement les proxies dans le client `OpenAI` :
     ```python
     from openai import OpenAI
     import httpx

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(proxies=None)  # Désactive les proxies
         )
         # Votre logique d'appel API ici
         response = client.chat.completions.create(
             model="deepseek",  # Remplacez par le modèle correct
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - Définir `proxies=None` garantit que `httpx` ignore tous les paramètres de proxy d'environnement.

#### Option 2 : Supporter le Proxy SOCKS

Si vous devez utiliser le proxy SOCKS (par exemple, pour accéder à l'API DeepSeek via un VPN ou un serveur proxy), vous devez ajouter le support SOCKS à `httpx`.

1. **Installer `httpx-socks`**
   - Installez le package `httpx-socks` pour activer le support des proxies SOCKS4/SOCKS5 :
     ```bash
     pip install httpx-socks
     ```
   - Cela étend `httpx` pour gérer les schémas `socks://` et `socks5://`.

2. **Mettre à Jour Votre Code**
   - Modifiez votre script pour utiliser explicitement le proxy SOCKS :
     ```python
     from openai import OpenAI
     import httpx
     from httpx_socks import SyncProxyTransport

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         # Configurer le proxy SOCKS5
         proxy_transport = SyncProxyTransport.from_url("socks5://127.0.0.1:7891")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(transport=proxy_transport)
         )
         # Votre logique d'appel API ici
         response = client.chat.completions.create(
             model="deepseek",  # Remplacez par le modèle correct
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - Remplacez `socks5://` par `socks4://` si votre proxy utilise SOCKS4.

3. **Vérifier le Serveur Proxy**
   - Assurez-vous que le serveur proxy sur `127.0.0.1:7891` est en cours d'exécution. Si vous utilisez un outil comme Clash ou Shadowsocks, vérifiez son statut :
     ```bash
     netstat -tuln | grep 7891
     ```
   - Si aucun processus n'écoute sur le port 7891, démarrez votre outil de proxy ou corrigez le port dans l'URL du proxy.

### Étapes de Débogage Supplémentaires

- **Vérifier la Configuration de l'Outil de Proxy**
  - Si vous utilisez un outil de proxy comme Clash ou Shadowsocks, vérifiez son fichier de configuration (par exemple, `~/.config/clash/config.yaml`) pour confirmer qu'il est configuré pour utiliser `127.0.0.1:7891` pour SOCKS5.
  - Assurez-vous que l'outil est en cours d'exécution et accessible.

- **Tester la Connectivité du Proxy**
  - Testez le proxy avec un outil comme `curl` (nécessite `curl` compilé avec le support SOCKS) :
    ```bash
    curl --socks5 127.0.0.1:7891 https://api.deepseek.com
    ```
  - Si cela échoue, le serveur proxy est soit arrêté, soit mal configuré.

- **Journaliser l'Utilisation du Proxy**
  - Ajoutez la journalisation à votre script pour confirmer quel proxy est utilisé :
    ```python
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ```

### Correction Recommandée

Si vous n'avez pas besoin du proxy, la correction la plus simple est de le désactiver en déréglant les variables d'environnement et en exécutant :
```bash
HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
```

Si vous avez besoin du proxy, installez `httpx-socks` et mettez à jour votre code pour utiliser `SyncProxyTransport` comme montré ci-dessus.

### Références
- [Documentation httpx](https://www.python-httpx.org/advanced/#proxy-support)
- [httpx-socks GitHub](https://github.com/romis2012/httpx-socks)
- [Documentation de l'API DeepSeek](https://platform.deepseek.com/docs)