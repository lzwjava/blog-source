---
audio: false
generated: true
lang: fr
layout: post
title: Conception de routes dans Angular
translated: true
type: note
---

D'accord, décomposons la conception des routes dans Angular pour un rafraîchissement facile, les sous-routes et la gestion des paramètres de requête.

**1. Rafraîchissement Facile et Maintien sur la Même Page**

Le mécanisme de routage par défaut d'Angular est conçu pour gérer cela de manière transparente. Lorsque vous naviguez vers une route spécifique dans votre application Angular, l'URL du navigateur change. Cette URL représente l'état actuel de votre application. Lorsque vous rafraîchissez la page, le navigateur envoie une requête au serveur pour la ressource associée à cette URL. Le module de routage d'Angular prend alors le relais et affiche le composant associé à cette route.

**Points clés :**

* **Configuration Correcte des Routes :** Assurez-vous que vos routes sont correctement définies dans votre `AppRoutingModule` (ou tout autre module de routage que vous avez créé). Chaque chemin doit être associé à un composant spécifique.
* **Configuration Côté Serveur (pour le Lien Profond) :** Si vous utilisez la "stratégie d'emplacement de chemin" (path location strategy, qui est la valeur par défaut), votre serveur doit être configuré pour servir le fichier `index.html` pour toutes les routes de l'application. Cela permet à Angular de gérer le routage côté client même lorsque vous accédez directement à un lien profond ou que vous rafraîchissez.

**Exemple de `AppRoutingModule` :**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent }, // Route avec un paramètre
  { path: '**', redirectTo: '' } // Route générique pour les chemins inconnus
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

Dans cet exemple :

* Lorsque vous naviguez vers `/products`, le `ProductListComponent` sera affiché. Si vous rafraîchissez la page, vous serez toujours sur le `ProductListComponent`.
* Lorsque vous naviguez vers `/products/123`, le `ProductDetailComponent` sera affiché, et le paramètre `id` sera accessible dans le composant. Un rafraîchissement vous maintiendra sur la même page de détail du produit.

**2. Conception des Sous-routes (Routes Enfants)**

Les sous-routes, ou routes enfants, vous permettent de créer des mises en page imbriquées dans votre application. C'est utile pour les sections où vous avez un composant parent qui agit comme un conteneur pour d'autres composants liés.

**Exemple :** Supposons que vous ayez une section "Admin" avec des sous-sections "Utilisateurs" et "Paramètres".

**Étapes :**

1.  **Créer les Composants Parent et Enfants :**
    ```bash
    ng generate component admin
    ng generate component users
    ng generate component settings
    ```

2.  **Configurer les Routes Enfants dans le Module de Routage du Parent (ou dans le `AppRoutingModule` principal) :**

    ```typescript
    import { NgModule } from '@angular/core';
    import { RouterModule, Routes } from '@angular/router';
    import { AdminComponent } from './admin/admin.component';
    import { UsersComponent } from './users/users.component';
    import { SettingsComponent } from './settings/settings.component';

    const adminRoutes: Routes = [
      {
        path: 'admin',
        component: AdminComponent,
        children: [
          { path: 'users', component: UsersComponent },
          { path: 'settings', component: SettingsComponent },
          { path: '', redirectTo: 'users', pathMatch: 'full' } // Route enfant par défaut
        ]
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(adminRoutes)], // Utiliser forChild pour les modules de fonctionnalité
      exports: [RouterModule]
    })
    export class AdminRoutingModule { }
    ```

    **Alternativement, vous pouvez les définir dans votre `AppRoutingModule` :**

    ```typescript
    // Dans AppRoutingModule
    const routes: Routes = [
      { path: '', component: HomeComponent },
      {
        path: 'admin',
        component: AdminComponent,
        children: [
          { path: 'users', component: UsersComponent },
          { path: 'settings', component: SettingsComponent },
          { path: '', redirectTo: 'users', pathMatch: 'full' }
        ]
      },
      { path: 'products', component: ProductListComponent },
      { path: 'products/:id', component: ProductDetailComponent },
      { path: '**', redirectTo: '' }
    ];
    ```

3.  **Ajouter `<router-outlet>` dans le Modèle du Composant Parent (`admin.component.html`) :**

    ```html
    <h1>Tableau de Bord Admin</h1>
    <nav>
      <a routerLink="users" routerLinkActive="active">Utilisateurs</a> |
      <a routerLink="settings" routerLinkActive="active">Paramètres</a>
    </nav>
    <hr>
    <router-outlet></router-outlet>
    ```

**Explication :**

* Le tableau `children` dans la route `admin` définit les sous-routes.
* Le `path` pour les routes enfants est relatif à la route parent (`/admin`).
* Lorsque vous naviguez vers `/admin/users`, le `AdminComponent` sera affiché, et le `UsersComponent` sera affiché dans le `<router-outlet>` du `AdminComponent`.
* `redirectTo: 'users', pathMatch: 'full'` dans la route `admin` garantit que lorsque vous naviguez vers `/admin`, vous serez automatiquement redirigé vers `/admin/users`.

**3. Conception des Routes avec Paramètres de Requête**

Les paramètres de requête sont utilisés pour transmettre des informations optionnelles à une route. Ils apparaissent dans l'URL après un point d'interrogation (`?`) et sont des paires clé-valeur séparées par des esperluettes (`&`).

**Exemple :** Une page de liste de produits où vous pouvez filtrer par catégorie.

**Étapes :**

1.  **Configurer la Route (Aucune configuration spéciale n'est nécessaire pour les paramètres de requête) :**

    ```typescript
    // Dans AppRoutingModule
    const routes: Routes = [
      { path: 'products', component: ProductListComponent },
      // ... autres routes
    ];
    ```

2.  **Naviguer avec les Paramètres de Requête :** Vous pouvez naviguer vers la route avec des paramètres de requête en utilisant le service `Router` :

    ```typescript
    import { Router } from '@angular/router';
    import { Component } from '@angular/core';

    @Component({
      selector: 'app-filter',
      template: `
        <button (click)="filterProducts('electronics')">Électronique</button>
        <button (click)="filterProducts('clothing')">Vêtements</button>
      `
    })
    export class FilterComponent {
      constructor(private router: Router) {}

      filterProducts(category: string) {
        this.router.navigate(['/products'], { queryParams: { category: category } });
      }
    }
    ```

3.  **Accéder aux Paramètres de Requête dans le Composant :** Utilisez le service `ActivatedRoute` pour accéder aux paramètres de requête :

    ```typescript
    import { Component, OnInit } from '@angular/core';
    import { ActivatedRoute } from '@angular/router';

    @Component({
      selector: 'app-product-list',
      template: `
        <h2>Liste des Produits</h2>
        <p>Filtrage par catégorie : {{ categoryFilter }}</p>
        <ul>
          <li *ngFor="let product of filteredProducts">
            {{ product.name }}
          </li>
        </ul>
      `
    })
    export class ProductListComponent implements OnInit {
      products: any[] = [
        { id: 1, name: 'Ordinateur Portable', category: 'electronics' },
        { id: 2, name: 'T-Shirt', category: 'clothing' },
        { id: 3, name: 'Casque Audio', category: 'electronics' },
        { id: 4, name: 'Jean', category: 'clothing' }
      ];
      categoryFilter: string | null = null;
      filteredProducts: any[] = [];

      constructor(private route: ActivatedRoute) {}

      ngOnInit(): void {
        this.route.queryParams.subscribe(params => {
          this.categoryFilter = params['category'];
          this.filterProductsByCategory();
        });
      }

      filterProductsByCategory() {
        if (this.categoryFilter) {
          this.filteredProducts = this.products.filter(
            product => product.category.toLowerCase() === this.categoryFilter?.toLowerCase()
          );
        } else {
          this.filteredProducts = this.products;
        }
      }
    }
    ```

**Explication :**

* Lorsque le bouton "Électronique" est cliqué, l'application navigue vers `/products?category=electronics`.
* Dans le `ProductListComponent`, le service `ActivatedRoute` fournit un observable `queryParams`. Nous nous abonnons à cet observable pour obtenir les paramètres de requête actuels.
* `params['category']` récupère la valeur du paramètre de requête `category`.
* Lorsque la page est rafraîchie avec les paramètres de requête dans l'URL, le hook de cycle de vie `ngOnInit` s'exécute à nouveau, et le composant se ré-abonne aux `queryParams`, garantissant que le filtre est appliqué même après un rafraîchissement.

**En résumé :**

* Le routage d'Angular gère le rafraîchissement et le maintien sur la même page par défaut, à condition que vos routes soient correctement configurées et que votre serveur soit configuré pour les liens profonds.
* Les sous-routes sont conçues en utilisant le tableau `children` dans votre configuration de route et la directive `<router-outlet>` dans le modèle du composant parent.
* Les paramètres de requête sont ajoutés à l'URL et peuvent être accédés dans vos composants en utilisant l'observable `queryParams` du service `ActivatedRoute`. Cela garantit que tout état géré via les paramètres de requête est préservé même après un rafraîchissement de la page.