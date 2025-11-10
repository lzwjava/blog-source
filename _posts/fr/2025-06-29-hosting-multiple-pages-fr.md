---
audio: false
generated: true
lang: fr
layout: post
title: Héberger plusieurs pages GitHub avec des organisations
translated: true
type: note
---

Oui, créer une organisation GitHub est une méthode viable pour héberger des sites GitHub Pages supplémentaires avec des sous-domaines `*.github.io` uniques, car chaque organisation peut avoir son propre site `organization.github.io`, distinct de votre site personnel `username.github.io`. Voici comment procéder et ce que vous devez savoir :

### Points Clés
- **Limitation du Compte Personnel** : Chaque compte utilisateur GitHub ne peut avoir qu'un seul Site Utilisateur, hébergé à l'adresse `username.github.io`, lié à un dépôt nommé `username.github.io`. Si vous avez déjà utilisé cela pour votre compte personnel, vous ne pouvez pas créer un autre sous-domaine `*.github.io` sous le même compte.
- **Sites d'Organisation** : Chaque organisation GitHub peut également avoir son propre Site d'Organisation, hébergé à l'adresse `organization.github.io`, en créant un dépôt nommé `organization.github.io`. Cela vous permet de créer des sous-domaines `*.github.io` supplémentaires en configurant plusieurs organisations.
- **Sites de Projet** : Les comptes utilisateur et organisation peuvent héberger plusieurs Sites de Projet (par exemple, `username.github.io/project` ou `organization.github.io/project`) à partir d'autres dépôts, mais ce sont des sous-chemins, pas des sous-domaines. Si vous voulez spécifiquement des sous-domaines distincts (par exemple, `sub.example.github.io`), vous ne pouvez pas les obtenir directement avec GitHub Pages sans un domaine personnalisé, car GitHub ne prend pas en charge les sous-domaines personnalisés comme `sub.example.github.io` sous le domaine `github.io`.[](https://github.com/orgs/community/discussions/54144)

### Étapes pour Créer une Organisation GitHub pour des Sous-domaines `*.github.io` Supplémentaires
1. **Créer une Organisation GitHub** :
   - Allez sur GitHub et connectez-vous avec votre compte.
   - Cliquez sur l'icône "+" dans le coin supérieur droit et sélectionnez **New organization**.
   - Suivez les instructions pour configurer l'organisation, en choisissant un nom unique (par exemple, `myorg`). Ce nom déterminera le sous-domaine (par exemple, `myorg.github.io`).
   - Note : Les organisations peuvent être créées gratuitement, mais certaines fonctionnalités (comme les dépôts privés) peuvent nécessiter un plan payant, selon vos besoins. GitHub Pages pour les dépôts publics est disponible avec GitHub Free.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

2. **Créer le Dépôt GitHub Pages de l'Organisation** :
   - Dans la nouvelle organisation, créez un dépôt nommé exactement `myorg.github.io` (remplacez `myorg` par le nom de votre organisation).
   - Ce dépôt hébergera le Site d'Organisation, accessible à l'adresse `https://myorg.github.io`.

3. **Configurer GitHub Pages** :
   - Allez dans l'onglet **Settings** du dépôt `myorg.github.io`.
   - Descendez jusqu'à la section **Pages**.
   - Sous **Source**, sélectionnez la branche que vous souhaitez publier (par exemple, `main` ou `gh-pages`) et enregistrez.
   - Une fois configuré, le site sera en ligne à l'adresse `https://myorg.github.io` après quelques minutes.[](https://dev.to/mohammedasker/how-to-get-github-subdomain-with-github-pages-4g0p)

4. **Ajouter du Contenu** :
   - Ajoutez un fichier `index.html` ou utilisez un générateur de site statique comme Jekyll dans la branche de publication du dépôt.
   - Validez et poussez vos changements. Par exemple :
     ```bash
     git clone https://github.com/myorg/myorg.github.io
     cd myorg.github.io
     echo "Hello World" > index.html
     git add --all
     git commit -m "Initial commit"
     git push origin main
     ```
   - Visitez `https://myorg.github.io` pour vérifier que le site est en ligne.[](https://dev.to/mohammedasker/how-to-get-github-subdomain-with-github-pages-4g0p)

5. **Répéter pour des Sous-domaines Supplémentaires** :
   - Créez des organisations supplémentaires (par exemple, `myorg2`, `myorg3`) et répétez le processus pour obtenir `myorg2.github.io`, `myorg3.github.io`, etc.
   - Chaque organisation peut avoir un sous-domaine `*.github.io`, vous permettant de créer autant de sous-domaines que vous avez d'organisations.

### Limitations et Considérations
- **Sous-domaines Personnalisés sur `github.io`** : Vous ne pouvez pas créer de sous-domaines comme `sub.myorg.github.io` directement avec GitHub Pages. Le domaine `github.io` est géré par GitHub, et seuls `username.github.io` ou `organization.github.io` sont pris en charge. Pour utiliser des sous-domaines personnalisés (par exemple, `blog.example.com`), vous devez posséder un domaine personnalisé et configurer les paramètres DNS (enregistrements CNAME) pour pointer vers `myorg.github.io`.[](https://github.com/orgs/community/discussions/54144)[](https://github.com/orgs/community/discussions/64133)
- **Dépôt Unique par Sous-domaine** : Chaque sous-domaine `*.github.io` est lié à un seul dépôt (`username.github.io` ou `organization.github.io`). Vous ne pouvez pas servir plusieurs sous-domaines à partir d'un seul dépôt sans un domaine personnalisé et des services d'hébergement ou de proxy supplémentaires.[](https://webmasters.stackexchange.com/questions/144484/separate-subdomains-on-one-github-page)
- **Surcharge de Gestion** : Chaque organisation nécessite une gestion séparée (par exemple, membres, permissions, facturation). Assurez-vous d'être à l'aise avec la gestion de plusieurs organisations.
- **DNS et Domaines Personnalisés** : Si vous souhaitez utiliser un domaine personnalisé (par exemple, `example.com` ou `sub.example.com`) au lieu de `*.github.io`, vous pouvez le configurer dans les paramètres **Pages** du dépôt et ajouter un enregistrement CNAME avec votre fournisseur DNS. Par exemple, pointez `sub.example.com` vers `myorg.github.io`. Assurez-vous de vérifier le domaine pour éviter les risques de détournement.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)[](https://dev.to/scc33/how-to-host-a-site-with-a-subdomain-on-github-pages-5a1j)
- **Dépôts Privés** : GitHub Pages pour les dépôts privés nécessite les plans GitHub Pro, Team ou Enterprise. Si vous utilisez des plans gratuits, assurez-vous que votre dépôt `myorg.github.io` est public.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

### Alternative pour les Sous-domaines Multiples
Si votre objectif est d'avoir plusieurs sous-domaines (par exemple, `blog.example.com`, `shop.example.com`) sous un seul domaine personnalisé, vous pouvez :
1. Acheter un domaine personnalisé (par exemple, `example.com`) auprès d'un registrar comme Namecheap ou GoDaddy.
2. Créer plusieurs dépôts dans votre organisation (par exemple, `myorg/blog`, `myorg/shop`).
3. Activer GitHub Pages pour chaque dépôt, en définissant des domaines personnalisés comme `blog.example.com` et `shop.example.com` dans leurs paramètres **Pages** respectifs.
4. Configurer les enregistrements CNAME avec votre fournisseur DNS pour pointer `blog.example.com` vers `myorg.github.io` et `shop.example.com` vers `myorg.github.io`. Notez que tous les dépôts sans leur propre domaine personnalisé apparaîtront sous le domaine personnalisé de l'organisation en tant que sous-chemins (par exemple, `example.com/blog`).[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)[](https://stackoverflow.com/questions/68505452/github-pages-with-single-custom-subdomain-for-multiple-repositories-using-paths)
5. Soyez conscient que servir plusieurs sous-domaines à partir d'un seul dépôt n'est pas pris en charge nativement par GitHub Pages et peut nécessiter des services externes comme un CDN ou un reverse proxy.[](https://webmasters.stackexchange.com/questions/144484/separate-subdomains-on-one-github-page)

### Exemple de Scénario
- Vous avez utilisé `username.github.io` pour votre site personnel.
- Créez une organisation nommée `myorg` et un dépôt `myorg.github.io` pour obtenir `myorg.github.io`.
- Créez une autre organisation nommée `myorg2` et un dépôt `myorg2.github.io` pour obtenir `myorg2.github.io`.
- Pour les sous-domaines personnalisés, possédez `example.com`, et configurez `blog.example.com` (pointant vers `myorg.github.io`) et `shop.example.com` (pointant vers `myorg2.github.io`) via des enregistrements CNAME.

### Notes Finales
- Créer plusieurs organisations est un moyen simple d'obtenir des sous-domaines `*.github.io` supplémentaires sans avoir besoin d'un domaine personnalisé.
- Si vous voulez de vrais sous-domaines (par exemple, `sub.myorg.github.io`), vous aurez besoin d'un domaine personnalisé et d'une configuration DNS, car le `github.io` de GitHub ne le prend pas en charge nativement.
- Vérifiez toujours les domaines personnalisés pour éviter les risques de sécurité comme les détournements de domaine.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- Les changements DNS peuvent prendre jusqu'à 24 heures pour se propager.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

Si vous avez d'autres questions ou besoin d'aide pour des configurations spécifiques, faites-le-moi savoir !