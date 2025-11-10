---
audio: false
generated: true
lang: fr
layout: post
title: Règles d'URL des sites de projet GitHub Pages
translated: true
type: note
---

Avec GitHub Pages, vous pouvez créer des **sites de projet** sous votre compte personnel en plus de votre site utilisateur (`username.github.io`). Cependant, le format de l'URL pour les sites de projet est limité à des modèles spécifiques, et toutes les configurations de sous-domaine ou de sous-chemin ne sont pas prises en charge nativement. Abordons votre question concernant l'utilisation de `username.github.io/project1` ou `project1.username.github.io` pour les sites de projet.

### Points clés
- **Site Utilisateur** : Un seul dépôt nommé `username.github.io` sert du contenu à l'adresse `https://username.github.io`.
- **Sites de Projet** : Tout autre dépôt dans votre compte personnel peut être configuré comme un site de projet, servi à l'adresse `https://username.github.io/nom-du-dépôt` (un sous-chemin, pas un sous-domaine).
- **Limitation des sous-domaines** : GitHub Pages ne prend pas en charge nativement les sous-domaines comme `project1.username.github.io` sous le domaine `github.io`. Le domaine `github.io` est géré par GitHub, et seuls `username.github.io` (pour les utilisateurs) ou `organization.github.io` (pour les organisations) sont pris en charge comme sous-domaines de premier niveau. Les sous-domaines personnalisés comme `project1.username.github.io` nécessitent un domaine personnalisé et une configuration DNS.

### Pouvez-vous utiliser `username.github.io/project1` ?
**Oui**, vous pouvez utiliser `username.github.io/project1` pour un site de projet. C'est la manière standard dont GitHub Pages gère les sites de projet :
- Créez un dépôt dans votre compte personnel (par exemple, `username/project1`).
- Activez GitHub Pages pour ce dépôt :
  - Allez dans l'onglet **Paramètres** du dépôt.
  - Descendez jusqu'à la section **Pages**.
  - Sous **Source**, sélectionnez la branche à publier (par exemple, `main` ou `gh-pages`) et enregistrez.
- Une fois configuré, le site sera accessible à l'adresse `https://username.github.io/project1`.
- Vous pouvez créer plusieurs sites de projet (par exemple, `username.github.io/project2`, `username.github.io/project3`) en activant GitHub Pages sur des dépôts supplémentaires (`username/project2`, `username/project3`, etc.).
- **Contenu** : Ajoutez un fichier `index.html` ou utilisez un générateur de site statique comme Jekyll dans la branche de publication de chaque dépôt.

### Pouvez-vous utiliser `project1.username.github.io` ?
**Non**, GitHub Pages ne prend pas en charge les sous-domaines comme `project1.username.github.io` nativement sous le domaine `github.io`. Le domaine `github.io` n'autorise que :
- `username.github.io` pour les sites utilisateur.
- `organization.github.io` pour les sites d'organisation.
- Les sous-chemins comme `username.github.io/nom-du-dépôt` pour les sites de projet.

Pour obtenir une URL comme `project1.username.github.io`, vous auriez besoin :
1. **D'un domaine personnalisé** : Achetez un domaine (par exemple, `example.com`) auprès d'un registrar comme Namecheap ou GoDaddy.
2. **D'une configuration DNS** : Configurez un enregistrement CNAME pour pointer un sous-domaine (par exemple, `project1.example.com`) vers votre site GitHub Pages (par exemple, `username.github.io` ou `username.github.io/project1`).
3. **Des paramètres GitHub Pages** :
   - Dans les paramètres **Pages** du dépôt, configurez le domaine personnalisé (par exemple, `project1.example.com`).
   - Optionnellement, activez "Forcer le HTTPS" pour la sécurité.
4. **Résultat** : Vous pouvez mapper `project1.example.com` vers le contenu du dépôt `project1`, mais pas `project1.username.github.io`, car GitHub contrôle le domaine `github.io` et n'autorise pas les sous-domaines personnalisés en dessous.

### Exemple de configuration pour `username.github.io/project1`
1. Créez un dépôt nommé `project1` sous votre compte (`username/project1`).
2. Ajoutez du contenu (par exemple, `index.html`) :
   ```bash
   git clone https://github.com/username/project1
   cd project1
   echo "Hello from Project 1" > index.html
   git add --all
   git commit -m "Initial commit"
   git push origin main
   ```
3. Activez GitHub Pages :
   - Allez dans `username/project1` → **Paramètres** → **Pages**.
   - Définissez la source sur `main` (ou une autre branche) et enregistrez.
4. Visitez `https://username.github.io/project1` pour voir le site en ligne (cela peut prendre quelques minutes pour se propager).

### Exemple pour un sous-domaine personnalisé avec un domaine personnalisé
Si vous voulez `project1.example.com` :
1. Possédez un domaine (par exemple, `example.com`).
2. Dans les paramètres de votre fournisseur DNS, ajoutez un enregistrement CNAME :
   - Nom : `project1`
   - Valeur : `username.github.io`
3. Dans les paramètres **Pages** du dépôt `project1`, définissez le domaine personnalisé sur `project1.example.com`.
4. Poussez le contenu vers le dépôt `project1`, et il sera servi à l'adresse `project1.example.com`.

### Limitations
- **Uniquement des sous-chemins pour `github.io`** : Sans domaine personnalisé, les sites de projet sont toujours servis comme des sous-chemins (`username.github.io/project1`), pas comme des sous-domaines (`project1.username.github.io`).
- **Un seul site utilisateur** : Votre dépôt `username.github.io` est réservé à votre site utilisateur. Les sites de projet utilisent d'autres dépôts et apparaissent comme des sous-chemins.
- **Les sous-domaines personnalisés nécessitent un domaine personnalisé** : Pour obtenir `project1.quelquechose`, vous devez posséder `quelquechose` (par exemple, `example.com`) et configurer le DNS.
- **Dépôts privés** : Les sites de projet dans des dépôts privés nécessitent GitHub Pro, Team ou Enterprise. Pour les comptes gratuits, les dépôts doivent être publics.

### Résumé
- **Utiliser `username.github.io/project1`** : Oui, c'est pris en charge nativement en créant un dépôt (`username/project1`) et en activant GitHub Pages. Vous pouvez créer plusieurs sites de projet de cette manière (par exemple, `username.github.io/project2`, etc.).
- **Utiliser `project1.username.github.io`** : Non, ce n'est pas pris en charge sous `github.io`. Vous auriez besoin d'un domaine personnalisé (par exemple, `project1.example.com`) et d'une configuration DNS pour obtenir un effet similaire.
- **Multiples sous-domaines** : Pour obtenir plusieurs sous-domaines `*.github.io`, créez des organisations GitHub (comme discuté précédemment) pour `org1.github.io`, `org2.github.io`, etc., ou utilisez un domaine personnalisé pour les sous-domaines comme `project1.example.com`.

Si vous avez besoin d'aide pour configurer un site de projet spécifique, configurer un domaine personnalisé ou gérer plusieurs sites, faites-le-moi savoir !