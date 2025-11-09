---
audio: false
date: 2025-09-10
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Stratégie de test d'API pour l'unicité et l'idempotence
translated: true
type: note
---

Excellente question. Prenons du recul, puis voyons comment aborder concrètement la notion d'« unicité » dans les tests d'API et d'intégration.

# De quoi parle-t-on ? (rappel rapide)

* **URL (chemin + requête)**

  * Le chemin représente généralement **l'identité de la ressource** : `/orders/123`.
  * Les paramètres de requête sont des **filtres/modificateurs** : `/orders?status=PAID&page=2`.

* **Méthode**

  * `GET/HEAD` sont sûres (safe).
  * `PUT` est **idempotente** (même appel, même résultat).
  * `POST` n'est **pas** idempotente, sauf si vous ajoutez un mécanisme **Idempotency-Key**.
  * `PATCH` n'est pas garantie idempotente.

* **En-têtes**

  * `Content-Type` : comment le **corps** est encodé.

    * `application/json` → corps JSON.
    * `application/x-www-form-urlencoded` → corps `a=1&b=2`.
    * `multipart/form-data; boundary=----abcd` → fichiers/téléchargements et parties multiples.
  * `Content-Disposition` apparaît **à l'intérieur des parties multipart**, pas au niveau supérieur de la requête. Une partie typique :

    ```
    --Boundary123
    Content-Disposition: form-data; name="file"; filename="x.png"
    Content-Type: image/png

    <binary bytes>
    --Boundary123--
    ```
  * En-têtes personnalisés utiles :

    * **Idempotency-Key** : dédupliquer les POST ayant des effets de bord.
    * **X-Request-ID / Correlation-ID** : tracer/journaliser une requête unique à travers les services.

* **Corps**

  * JSON : un document sérialisé.
  * `form-urlencoded` : paires clé-valeur comme une chaîne de requête mais dans le corps.
  * `multipart/form-data` : multiples « parties » séparées par le délimiteur `boundary` (`----WebKitFormBoundary...` est une chaîne courante des navigateurs).

# Où doit résider l'identité ?

* **Identité de la ressource** → dans le **chemin de l'URL** (`/users/{id}`), car elle est stable et permet la mise en signet.
* **Modificateurs d'opération** → requête ou en-têtes.
* **Représentation/état à écrire** → corps.

Tenter d'encoder l'unicité de la requête uniquement dans l'URL échoue souvent pour les opérations d'écriture (p. ex., POST avec un gros JSON). Pensez plutôt en **deux couches** :

1. **Identité de la requête (empreinte)** :
   Un hash déterministe de :

   * **Méthode** HTTP
   * **Chemin canonisé** (template + valeurs concrètes)
   * **Requête normalisée** (triée)
   * **En-têtes sélectionnés** (seulement ceux qui affectent la sémantique, p. ex. `Accept`, `Content-Language`, *pas* `Date`)
   * **Corps** (JSON normalisé ou un digest par partie pour le multipart)

2. **Identité de l'opération (idempotence métier)** :
   Pour les opérations ayant des effets de bord (créer/débiter/transférer), utilisez **Idempotency-Key** (un UUID par *intention métier*). Le serveur stocke le premier résultat sous cette clé et le renvoie pour les nouvelles tentatives.

Ces deux concepts résolvent des problèmes différents : les empreintes aident vos **tests** et votre **observabilité** ; les clés d'idempotence protègent la **production** contre les effets dupliqués.

# Stratégie de test pour l'« unicité »

1. **Définir une fonction d'empreinte de requête** (côté client/test). Logique exemple :

   * Mettre les noms d'en-têtes en minuscule ; n'inclure qu'une liste autorisée sûre.
   * Trier les paramètres de requête ; stringifier le JSON de manière stable (supprimer les espaces, trier les clés).
   * SHA-256 sur `METHOD\nPATH\nQUERY\nHEADERS\nBODY`.

2. **Donner un ID de corrélation à chaque test**

   * Générer un UUID par cas de test : `X-Request-ID: test-<suite>-<uuid>`.
   * Le journaliser côté serveur pour pouvoir lier les logs à un test.

3. **Utiliser Idempotency-Key si nécessaire**

   * Pour les POST qui créent des ressources ou débiter de l'argent :

     * `Idempotency-Key: <uuid>`
     * Le serveur doit renvoyer le même 200/201 et le même corps pour les nouvelles tentatives avec la même clé dans une fenêtre de rétention.

4. **Garder les données de test uniques mais minimales**

   * Utiliser des ID déterministes (p. ex., email `user+T001@example.com`) ou suffixer avec l'UUID du test.
   * Nettoyer, ou mieux, concevoir les tests pour qu'ils soient **idempotents** en utilisant PUT/DELETE sur vos ID pré-générés lorsque c'est possible.

5. **Vérifier au bon niveau**

   * Pour les opérations **idempotentes** : vérifier le **statut**, la **représentation** et les **effets de bord** (p. ex., nombre d'enregistrements inchangé lors d'une répétition).
   * Pour les POST **non idempotents** avec Idempotency-Key : vérifier que le premier appel renvoie 201, et les tentatives suivantes 200 avec le même corps (ou 201 répété avec la même ressource).

# Extraits pratiques

**Exemples cURL**

* POST JSON :

  ```bash
  curl -X POST https://api.example.com/orders \
    -H 'Content-Type: application/json' \
    -H 'Idempotency-Key: 4b6f2d1a-...' \
    -H 'X-Request-ID: test-orders-create-...' \
    -d '{"customerId":"C123","items":[{"sku":"ABC","qty":1}]}'
  ```
* Téléchargement multipart :

  ```bash
  curl -X POST https://api.example.com/uploads \
    -H 'X-Request-ID: test-upload-...' \
    -F 'file=@/path/pic.png' \
    -F 'meta={"purpose":"avatar"};type=application/json'
  ```

  (curl définit `Content-Type: multipart/form-data; boundary=----...` et chaque partie a son propre `Content-Disposition`.)

**Empreinte de requête côté test en Python (illustratif) :**

```python
import hashlib, json, urllib.parse

def canonical_json(obj):
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)

def normalize_query(url):
    parsed = urllib.parse.urlsplit(url)
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q.sort()
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(q), '')), q

def request_fingerprint(method, url, headers=None, body_bytes=b''):
    headers = headers or {}
    # liste autorisée des en-têtes qui affectent la sémantique
    allow = {'accept', 'content-type', 'content-language'}
    norm_headers = {k.lower(): v.strip() for k, v in headers.items() if k.lower() in allow}
    header_line = '\n'.join(f'{k}:{norm_headers[k]}' for k in sorted(norm_headers))
    url_no_query, q_pairs = normalize_query(url)
    query_line = '&'.join(f'{k}={v}' for k, v in q_pairs)
    h = hashlib.sha256()
    h.update((method.upper() + '\n').encode())
    h.update((url_no_query + '\n').encode())
    h.update((query_line + '\n').encode())
    h.update((header_line + '\n').encode())
    h.update(body_bytes or b'')
    return h.hexdigest()
```

* Pour les corps JSON, passer `body_bytes=canonical_json(payload).encode()`.
* Pour le multipart, hacher chaque partie puis hacher la concaténation pour éviter le bruit du boundary.

# Répondre à votre idée centrale

> « Si l'URL est unique alors les requêtes sont uniques ; les paramètres/corps contribuent beaucoup—comment penser l'unicité pour les tests d'API/intégration ? »

* Considérer **l'URL seule** comme **insuffisante** pour l'unicité dans les tests, car les en-têtes et le corps changent matériellement la sémantique.
* Construire une **empreinte de requête** comme ci-dessus pour la déduplication/le traçage dans les tests.
* Pour la déduplication au niveau métier des **POST**, s'appuyer sur **Idempotency-Key**, pas sur l'URL.
* Garder **l'identité de la ressource** dans le chemin pour la clarté et une meilleure déterminisme des tests.

# Petite checklist à adopter dès aujourd'hui

* [ ] Ajouter `X-Request-ID` (UUID) à chaque requête de test.
* [ ] Ajouter `Idempotency-Key` aux POST qui créent/débitent.
* [ ] Implémenter un helper de test qui calcule une empreinte de requête et la journalise avec chaque assertion.
* [ ] Canonicaliser le JSON avant hachage ; trier les paramètres de requête ; liste autorisée pour les en-têtes sémantiques.
* [ ] Préférer PUT pour les upserts pour rendre les tests idempotents ; réserver POST pour les vraies créations.
* [ ] Pour le multipart, vérifier les **parties analysées par le serveur** (noms, noms de fichier, types de contenu) plutôt que les bytes bruts du boundary.

Si vous partagez votre stack de test actuelle (pytest/unittest + requests/httpx, ou Java/Kotlin), je peux fournir un helper prêt à l'emploi adapté.