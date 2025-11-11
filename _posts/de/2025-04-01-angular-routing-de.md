---
audio: false
generated: true
lang: de
layout: post
title: Design-Routen in Angular
translated: true
type: note
---

Okay, lassen Sie uns durchgehen, wie man Routen in Angular für einfaches Aktualisieren, Sub-Routen und den Umgang mit Query-Parametern entwirft.

**1. Einfaches Aktualisieren und Verbleiben auf derselben Seite**

Angulars standardmäßiger Routing-Mechanismus ist dafür nahtlos ausgelegt. Wenn Sie zu einer bestimmten Route in Ihrer Angular-Anwendung navigieren, ändert sich die URL im Browser. Diese URL repräsentiert den aktuellen Zustand Ihrer Anwendung. Wenn Sie die Seite aktualisieren, sendet der Browser eine Anfrage an den Server für die Ressource, die mit dieser URL verknüpft ist. Das Routing-Modul von Angular übernimmt dann und rendert die Komponente, die dieser Route zugeordnet ist.

**Wichtige Punkte:**

*   **Korrekte Routen-Konfiguration:** Stellen Sie sicher, dass Ihre Routen korrekt in Ihrem `AppRoutingModule` (oder einem anderen von Ihnen erstellten Routing-Modul) definiert sind. Jeder Pfad sollte einer bestimmten Komponente zugeordnet sein.
*   **Server-Seitige Konfiguration (für Deep Linking):** Wenn Sie die "Path Location Strategy" verwenden (was der Standard ist), muss Ihr Server so konfiguriert sein, dass er die `index.html`-Datei für alle Anwendungsrouten ausliefert. Dies ermöglicht es Angular, das Routing clientseitig zu handhaben, selbst wenn Sie direkt auf einen Deep Link zugreifen oder die Seite aktualisieren.

**Beispiel `AppRoutingModule`:**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent }, // Route mit einem Parameter
  { path: '**', redirectTo: '' } // Wildcard-Route für unbekannte Pfade
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

In diesem Beispiel:

*   Wenn Sie zu `/products` navigieren, wird die `ProductListComponent` gerendert. Wenn Sie die Seite aktualisieren, bleiben Sie auf der `ProductListComponent`.
*   Wenn Sie zu `/products/123` navigieren, wird die `ProductDetailComponent` gerendert, und der `id`-Parameter ist innerhalb der Komponente zugänglich. Ein Aktualisieren hält Sie auf derselben Produktdetailseite.

**2. Entwerfen von Sub-Routen (Child Routes)**

Sub-Routen, oder Child Routes, ermöglichen es Ihnen, verschachtelte Layouts innerhalb Ihrer Anwendung zu erstellen. Dies ist nützlich für Bereiche, in denen Sie eine übergeordnete Komponente haben, die als Container für andere verwandte Komponenten dient.

**Beispiel:** Nehmen wir an, Sie haben einen "Admin"-Bereich mit "Users"- und "Settings"-Unterbereichen.

**Schritte:**

1.  **Erstellen von Parent- und Child-Komponenten:**
    ```bash
    ng generate component admin
    ng generate component users
    ng generate component settings
    ```

2.  **Konfigurieren der Child Routes im Routing-Modul des Parents (oder im Haupt-`AppRoutingModule`):**

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
          { path: '', redirectTo: 'users', pathMatch: 'full' } // Standard-Child-Route
        ]
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(adminRoutes)], // Verwenden Sie forChild für Feature-Module
      exports: [RouterModule]
    })
    export class AdminRoutingModule { }
    ```

    **Alternativ können Sie sie auch in Ihrem `AppRoutingModule` definieren:**

    ```typescript
    // In AppRoutingModule
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

3.  **Fügen Sie `<router-outlet>` in das Template der Parent-Komponente ein (`admin.component.html`):**

    ```html
    <h1>Admin Dashboard</h1>
    <nav>
      <a routerLink="users" routerLinkActive="active">Users</a> |
      <a routerLink="settings" routerLinkActive="active">Settings</a>
    </nav>
    <hr>
    <router-outlet></router-outlet> ```

**Erklärung:**

*   Das `children`-Array innerhalb der `admin`-Route definiert die Sub-Routen.
*   Der `path` für die Child-Routes ist relativ zur Parent-Route (`/admin`).
*   Wenn Sie zu `/admin/users` navigieren, wird die `AdminComponent` gerendert und die `UsersComponent` wird innerhalb des `<router-outlet>` der `AdminComponent` angezeigt.
*   `redirectTo: 'users', pathMatch: 'full'` in der `admin`-Route stellt sicher, dass bei der Navigation zu nur `/admin` automatisch zu `/admin/users` weitergeleitet wird.

**3. Entwerfen von Routen mit Query-Parametern**

Query-Parameter werden verwendet, um optionale Informationen an eine Route zu übergeben. Sie erscheinen in der URL nach einem Fragezeichen (`?`) und sind Schlüssel-Wert-Paare, die durch kaufmännische Unds (`&`) getrennt sind.

**Beispiel:** Eine Produktlistenseite, auf der Sie nach Kategorie filtern können.

**Schritte:**

1.  **Konfigurieren der Route (Keine spezielle Konfiguration für Query-Parameter erforderlich):**

    ```typescript
    // In AppRoutingModule
    const routes: Routes = [
      { path: 'products', component: ProductListComponent },
      // ... andere Routen
    ];
    ```

2.  **Navigieren mit Query-Parametern:** Sie können mit Query-Parametern zur Route navigieren, indem Sie den `Router`-Service verwenden:

    ```typescript
    import { Router } from '@angular/router';
    import { Component } from '@angular/core';

    @Component({
      selector: 'app-filter',
      template: `
        <button (click)="filterProducts('electronics')">Electronics</button>
        <button (click)="filterProducts('clothing')">Clothing</button>
      `
    })
    export class FilterComponent {
      constructor(private router: Router) {}

      filterProducts(category: string) {
        this.router.navigate(['/products'], { queryParams: { category: category } });
      }
    }
    ```

3.  **Auf Query-Parameter in der Komponente zugreifen:** Verwenden Sie den `ActivatedRoute`-Service, um auf die Query-Parameter zuzugreifen:

    ```typescript
    import { Component, OnInit } from '@angular/core';
    import { ActivatedRoute } from '@angular/router';

    @Component({
      selector: 'app-product-list',
      template: `
        <h2>Product List</h2>
        <p>Filter nach Kategorie: {{ categoryFilter }}</p>
        <ul>
          <li *ngFor="let product of products">
            {{ product.name }}
          </li>
        </ul>
      `
    })
    export class ProductListComponent implements OnInit {
      products: any[] = [
        { id: 1, name: 'Laptop', category: 'electronics' },
        { id: 2, name: 'T-Shirt', category: 'clothing' },
        { id: 3, name: 'Headphones', category: 'electronics' },
        { id: 4, name: 'Jeans', category: 'clothing' }
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

**Erklärung:**

*   Wenn der "Electronics"-Button geklickt wird, navigiert die Anwendung zu `/products?category=electronics`.
*   In der `ProductListComponent` stellt der `ActivatedRoute`-Service ein `queryParams` Observable bereit. Wir abonnieren dieses Observable, um die aktuellen Query-Parameter zu erhalten.
*   `params['category']` ruft den Wert des `category` Query-Parameters ab.
*   Wenn die Seite mit den Query-Parametern in der URL aktualisiert wird, wird der `ngOnInit` Lifecycle-Hook erneut ausgeführt und die Komponente abonniert die `queryParams` erneut, was sicherstellt, dass der Filter auch nach einem Aktualisieren angewendet wird.

**Zusammenfassend:**

*   Angulars Routing handhabt das Aktualisieren und Verbleiben auf derselben Seite standardmäßig, vorausgesetzt Ihre Routen sind korrekt konfiguriert und Ihr Server ist für Deep Linking eingerichtet.
*   Sub-Routen werden mit dem `children`-Array in Ihrer Routen-Konfiguration und der `<router-outlet>`-Direktive im Template der Parent-Komponente entworfen.
*   Query-Parameter werden an die URL angehängt und können in Ihren Komponenten über das `queryParams` Observable des `ActivatedRoute`-Services abgerufen werden. Dies stellt sicher, dass jeder durch Query-Parameter verwaltete Zustand selbst nach einem Seiten-Reload erhalten bleibt.