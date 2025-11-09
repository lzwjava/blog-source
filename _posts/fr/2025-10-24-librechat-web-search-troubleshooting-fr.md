---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Dépannage de la recherche web LibreChat
translated: true
type: note
---

Procédons au dépannage avec soin — lorsque la **recherche web ne fonctionne pas dans LibreChat**, même après avoir ajouté les clés **Firecrawl**, **SerpApi** et **Jina API**, le problème est presque toujours l'un des suivants : des erreurs de configuration, des indicateurs d'activation manquants dans le backend, ou une mauvaise interprétation de l'interface utilisateur.

Voici une explication détaillée que vous pouvez suivre (pas de tableaux, juste des explications) :

---

### 1. **Vérifiez si "Web Search" est activé dans la configuration du backend**

Ouvrez votre fichier de configuration du serveur LibreChat (généralement `.env` ou `api/config.yaml` selon votre installation) et confirmez que vous avez quelque chose comme :

```
# Pour .env
SEARCH_ENABLED=true
```

Ou, si vous utilisez YAML :

```yaml
features:
  search: true
```

Si `SEARCH_ENABLED` ou `search` n'est pas explicitement défini sur `true`, le bouton dans l'interface utilisateur peut apparaître mais n'effectuera pas réellement de recherches.

---

### 2. **Confirmez que les clés API sont correctement nommées**

Chaque fournisseur attend des noms de variables d'environnement spécifiques. Par exemple :

* Pour **SerpApi** :

  ```
  SERPAPI_API_KEY=votre_clé_ici
  ```
* Pour **Firecrawl** :

  ```
  FIRECRAWL_API_KEY=votre_clé_ici
  ```
* Pour **Jina** :

  ```
  JINA_API_KEY=votre_clé_ici
  ```

Assurez-vous également qu'elles sont exportées ou chargées dans le même environnement que le processus `backend` en cours d'exécution.

Pour vérifier :

```bash
echo $SERPAPI_API_KEY
```

Si cela retourne un résultat vide, votre backend ne la voit pas.

---

### 3. **Redémarrez LibreChat après avoir modifié les clés**

LibreChat ne recharge pas à chaud les variables d'environnement. Exécutez :

```bash
docker compose down
docker compose up -d
```

(ou `npm run start` à nouveau si vous n'utilisez pas Docker).

---

### 4. **Vérifiez quel fournisseur de recherche LibreChat utilise réellement**

LibreChat choisit un backend de recherche web par défaut en fonction de l'ordre de configuration.

Si vous voulez qu'il utilise SerpApi, par exemple, vous devez spécifier :

```
SEARCH_PROVIDER=serpapi
```

Alternativement, si vous voulez Jina :

```
SEARCH_PROVIDER=jina
```

Si vous avez seulement défini les clés mais n'avez pas spécifié quel fournisseur utiliser, LibreChat peut ne sélectionner aucun par défaut.

---

### 5. **Consultez les logs du backend**

Exécutez :

```bash
docker logs librechat-backend
```

ou

```bash
npm run start:debug
```

Recherchez des messages comme :

```
[Search] Clé SerpApi manquante ou invalide
```

ou

```
Fournisseur de recherche non configuré
```

Ce sont les meilleurs indices.

---

### 6. **Testez les APIs directement**

Pour vous assurer que vos clés fonctionnent réellement :

**Test SerpApi :**

```bash
curl "https://serpapi.com/search.json?q=chatgpt&api_key=VOTRE_CLE"
```

**Test Firecrawl :**

```bash
curl "https://api.firecrawl.dev/v1/search?q=chatgpt" -H "Authorization: Bearer VOTRE_CLE"
```

**Test Jina :**

```bash
curl "https://r.jina.ai/chatgpt" -H "Authorization: Bearer VOTRE_CLE"
```

Si ces commandes échouent, les clés elles-mêmes sont invalides ou soumises à une limitation de débit.

---

### 7. **Incompatibilité de version du frontend**

Si vous avez récemment mis à jour LibreChat (surtout d'une version antérieure à la v0.7 vers la v0.8+), le bouton `Web Search` dans le frontend pourrait exister même si votre version du backend ne prend pas encore en charge le module de recherche intégré Firecrawl/Jina.
Exécutez :

```bash
git pull
```

et reconstruisez :

```bash
docker compose build --no-cache
docker compose up -d
```

---

### 8. **Vérification finale — confirmez depuis l'interface Web**

Ouvrez l'interface utilisateur, allez dans **Paramètres → Fonctionnalités**, et confirmez :

* Le bouton bascule "Web Search" est sur ON (Activé)
* Votre fournisseur sélectionné est listé (SerpApi, Firecrawl, ou Jina)

S'il indique *"Aucun fournisseur disponible"*, le backend ne lit pas vos clés.

---

Si vous le souhaitez, vous pouvez coller la partie pertinente de votre fichier `.env` (avec les clés masquées) et je vous indiquerai exactement quelle ligne est manquante ou mal nommée.

Souhaitez-vous me montrer cet extrait ?