---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Aperçu des limites d'utilisation de GitHub Actions
translated: true
type: note
---

### Limites d'utilisation de GitHub Actions

GitHub Actions applique des limites par paliers selon votre abonnement (comptes personnels ou organisations). Cela inclut les minutes gratuites mensuelles pour les runners hébergés par GitHub dans les dépôts privés et le stockage pour les artefacts. Les dépôts publics et les runners auto-hébergés ne consomment pas ces minutes. Les limites sont réinitialisées mensuellement pour les minutes (le stockage est continu). Les dépassements sont facturés automatiquement si vous avez un moyen de paiement valide ; sinon, les jobs sont bloqués après avoir atteint la limite.

#### Minutes et stockage inclus par abonnement

| Abonnement                          | Stockage | Minutes (par mois) |
|-------------------------------------|----------|--------------------|
| GitHub Free (personnel/org)        | 500 Mo  | 2 000              |
| GitHub Pro (personnel)             | 1 Go    | 3 000              |
| GitHub Team (org)                  | 2 Go    | 3 000              |
| GitHub Enterprise Cloud (org)      | 50 Go   | 50 000             |

- **Minutes** : Comptent le temps d'exécution total des jobs sur les runners hébergés par GitHub (temps partiel pour les jobs échoués). Des multiplicateurs s'appliquent : Linux (1x), Windows (2x), macOS (10x). Toute personne ayant un accès en écriture à un dépôt utilise l'allocation du propriétaire du dépôt.
- **Stockage** : Basé sur les Go-heures de stockage d'artefacts (par exemple, les téléversements/téléchargements). Les journaux et les résumés ne sont pas comptabilisés.

#### Facturation des dépassements
Si vous dépassez les quotas :
- **Minutes** : Facturées par minute supplémentaire (tarifs USD pour les runners Linux standard : 0,008 $/min ; plus élevés pour Windows/macOS en raison des multiplicateurs).
- **Stockage** : Facturé en Go-mois (total des Go-heures / 744 heures par mois, arrondi à l'entier supérieur).
- Exemple : Sur un abonnement Team, 5 000 minutes supplémentaires (3 000 Linux + 2 000 Windows) coûtent environ 56 $.

Sans moyen de paiement, l'utilisation s'arrête au quota. L'erreur que vous avez vue ("les paiements récents du compte ont échoué ou votre limite de dépenses doit être augmentée") signifie que soit les paiements ont été rejetés, soit votre **limite de dépenses (budget)** plafonne les dépassements.

#### Limites de dépenses (Budgets)
- Il s'agit de seuils optionnels pour contrôler le total des dépenses mensuelles sur Actions (et autres fonctionnalités mesurées).
- Si elle est définie trop bas, elle bloque les jobs avant d'atteindre les quotas.
- **Comment vérifier/augmenter** :
  1. Allez dans Paramètres GitHub > Facturation et plans.
  2. Sous "Budgets et alertes", consultez ou modifiez votre budget pour GitHub Actions.
  3. Augmentez la limite, ajoutez un moyen de paiement, ou supprimez complètement le budget (dépassements illimités, mais surveillez via les alertes).
- Les comptes migrés peuvent avoir des budgets générés automatiquement à partir d'anciennes limites — mettez-les à jour pour correspondre à votre utilisation.

Pour plus de détails, consultez le tableau de bord de facturation de votre compte pour une utilisation en temps réel.

[Documentation de facturation de GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)