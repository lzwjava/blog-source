---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Respecter un intervalle de construction de 30 minutes
translated: true
type: note
---

### Modifier le workflow pour imposer un intervalle de 30 minutes entre les builds

Pour garantir que votre workflow de déploiement Jekyll ne s'exécute pas trop fréquemment (c'est-à-dire au moins un intervalle de 30 minutes entre les exécutions consécutives), vous pouvez ajouter une étape conditionnelle au début de la tâche `build`. Cette étape interrogera l'API GitHub pour obtenir l'horodatage de la dernière exécution réussie de ce workflow. Si le déclencheur actuel se situe dans les 30 minutes suivant la fin de cette exécution, la tâche se terminera prématurément avec un message (en sautant le build).

Cette approche :
- Utilise l'API REST GitHub (aucun outil externe nécessaire).
- Ne vérifie que les exécutions précédentes **réussies** (statut : "completed", conclusion : "success").
- Calcule la différence de temps en secondes et la compare à 1800 (30 minutes).
- Fonctionne avec vos déclencheurs `push` et `workflow_dispatch` existants.
- N'interfère pas avec la configuration de concurrence (qui gère les exécutions simultanées).

#### Extrait YAML mis à jour
Insérez cette nouvelle étape juste après l'étape "Checkout Repository" dans votre tâche `build`. Le reste du workflow reste inchangé.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Imposer un intervalle de 30 minutes entre les builds
        id: cooldown
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Récupérer la dernière exécution réussie de ce workflow
          RUNS_RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${{ github.repository }}/actions/workflows/${{ github.workflow_ref }}/runs?status=completed&conclusion=success&per_page=1&sort=timestamp&direction=desc")

          # Extraire l'horodatage completed_at de la dernière exécution réussie (format ISO 8601)
          LAST_COMPLETED_AT=$(echo "$RUNS_RESPONSE" | jq -r '.[0].completed_at // empty')
          
          if [ -z "$LAST_COMPLETED_AT" ] || [ "$LAST_COMPLETED_AT" = "null" ]; then
            echo "Aucune exécution réussie précédente trouvée. Procéder au build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

          # Convertir les horodatages en secondes Unix pour la comparaison
          CURRENT_TIME=$(date -u +%s)
          LAST_TIME=$(date -d "$LAST_COMPLETED_AT" +%s)
          TIME_DIFF=$((CURRENT_TIME - LAST_TIME))

          echo "Dernière exécution réussie terminée à : $LAST_COMPLETED_AT (diff : ${TIME_DIFF}s)"

          if [ $TIME_DIFF -lt 1800 ]; then  # 1800 secondes = 30 minutes
            echo "Build ignoré : Moins de 30 minutes depuis la dernière exécution réussie."
            echo "skip_build=true" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "Intervalle de temps suffisant. Procéder au build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

      # Ignorer l'intégralité du build si la vérification de l'intervalle échoue (ajouter cette condition aux étapes suivantes ou encapsuler le build dans un if)
      - name: Set up Python 3.13.2
        if: steps.cooldown.outputs.skip_build != 'true'
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      # ... (répéter la condition 'if: steps.cooldown.outputs.skip_build != 'true'' sur TOUTES les étapes restantes après celle-ci)
```

#### Principaux changements expliqués
1. **Requête API** :
   - Utilise `curl` pour interroger le point de terminaison de l'API GitHub Actions pour les exécutions de workflow.
   - Filtre pour `status=completed` et `conclusion=success` pour n'obtenir que les exécutions terminées et réussies.
   - Limite à `per_page=1` et trie par `timestamp desc` pour la plus récente.
   - Extrait `completed_at` (l'heure exacte de fin de l'exécution précédente).

2. **Calcul du temps** :
   - Convertit l'heure actuelle et l'heure de fin précédente en horodatages Unix en utilisant `date`.
   - Calcule la différence en secondes.
   - Si `< 1800` secondes, définit `skip_build=true` et quitte l'étape prématurément.

3. **Exécution conditionnelle** :
   - Ajoutez `if: steps.cooldown.outputs.skip_build != 'true'` à **chaque étape suivante** (par exemple, Set up Python, Install Dependencies, jusqu'à Sync built site).
   - Cela garantit que la tâche indique "ignorée" dans l'interface GitHub si l'intervalle se déclenche, mais enregistre tout de même la raison.

4. **Cas particuliers gérés** :
   - Aucune exécution précédente : Procède (premier build).
   - Exécutions précédentes échouées/en cours : Les ignore et procède.
   - Erreurs API : Revient à procéder (comportement par défaut sécurisé).
   - `jq` est préinstallé sur `ubuntu-latest`, donc aucune configuration supplémentaire n'est nécessaire.

#### Tester le changement
- Validez ceci dans votre branche `main` (cela déclenchera le workflow).
- Déclenchez plusieurs pushes/dispatches rapides : Le deuxième dans les 30 minutes devrait être ignoré.
- Surveillez les journaux de la tâche pour le message "Build ignoré".
- Si vous souhaitez ajuster l'intervalle (par exemple, 1 heure), changez `1800` en `3600`.

#### Alternatives
- **Déclencheur planifié** : Si vous voulez des builds *périodiques* toutes les 30 minutes (indépendamment des pushes), ajoutez ceci à la section `on:` :
  ```yaml
  schedule:
    - cron: '*/30 * * * *'  # Toutes les 30 minutes
  ```
  Mais cela n'impose pas d'intervalle sur les déclencheurs push — utilisez-le conjointement avec l'étape d'intervalle si nécessaire.
- **Action personnalisée** : Pour la réutilisabilité, encapsulez la logique d'intervalle dans un workflow réutilisable ou une action composite.
- **Limitations** : Cela vérifie l'heure de fin d'exécution, pas l'heure de début. Si une exécution précédente est toujours en cours pendant >30 min, la concurrence l'annulera de toute façon.

Si cela ne correspond pas exactement à votre intention (par exemple, vous vouliez une planification *au moins* toutes les 30 min), fournissez plus de détails !