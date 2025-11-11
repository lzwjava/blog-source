---
audio: false
generated: true
lang: es
layout: post
title: Diseño de Rutas en Angular
translated: true
type: note
---

De acuerdo, desglosemos cómo diseñar rutas en Angular para facilitar la actualización, las sub-rutas y el manejo de parámetros de consulta.

**1. Fácil Actualización y Permanecer en la Misma Página**

El mecanismo de enrutamiento predeterminado de Angular está diseñado para manejar esto sin problemas. Cuando navegas a una ruta específica en tu aplicación Angular, la URL del navegador cambia. Esta URL representa el estado actual de tu aplicación. Cuando actualizas la página, el navegador hace una solicitud al servidor para el recurso asociado con esa URL. El módulo de enrutamiento de Angular se hace cargo y renderiza el componente asociado con esa ruta.

**Puntos clave:**

* **Configuración Correcta de Rutas:** Asegúrate de que tus rutas estén correctamente definidas en tu `AppRoutingModule` (o en cualquier otro módulo de enrutamiento que hayas creado). Cada ruta debe estar asociada a un componente específico.
* **Configuración del Lado del Servidor (para Deep Linking):** Si estás usando la "estrategia de ubicación de ruta" (que es la predeterminada), tu servidor necesita estar configurado para servir el archivo `index.html` para todas las rutas de la aplicación. Esto permite que Angular maneje el enrutamiento en el lado del cliente incluso cuando accedes directamente a un enlace profundo o actualizas la página.

**Ejemplo de `AppRoutingModule`:**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent }, // Ruta con un parámetro
  { path: '**', redirectTo: '' } // Ruta comodín para rutas desconocidas
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

En este ejemplo:

* Cuando navegas a `/products`, se renderizará el `ProductListComponent`. Si actualizas la página, seguirás en el `ProductListComponent`.
* Cuando navegas a `/products/123`, se renderizará el `ProductDetailComponent`, y el parámetro `id` será accesible dentro del componente. Al actualizar, permanecerás en la misma página de detalles del producto.

**2. Diseño de Sub-rutas (Rutas Hijas)**

Las sub-rutas, o rutas hijas, te permiten crear diseños anidados dentro de tu aplicación. Esto es útil para secciones donde tienes un componente padre que actúa como contenedor para otros componentes relacionados.

**Ejemplo:** Supongamos que tienes una sección "Admin" con las sub-secciones "Users" y "Settings".

**Pasos:**

1.  **Crear Componentes Padre e Hijos:**
    ```bash
    ng generate component admin
    ng generate component users
    ng generate component settings
    ```

2.  **Configurar Rutas Hijas en el Módulo de Enrutamiento del Padre (o en el `AppRoutingModule` principal):**

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
          { path: '', redirectTo: 'users', pathMatch: 'full' } // Ruta hija por defecto
        ]
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(adminRoutes)], // Usa forChild para módulos de funcionalidad
      exports: [RouterModule]
    })
    export class AdminRoutingModule { }
    ```

    **Alternativamente, puedes definirlas en tu `AppRoutingModule`:**

    ```typescript
    // En AppRoutingModule
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

3.  **Añadir `<router-outlet>` en la Plantilla del Componente Padre (`admin.component.html`):**

    ```html
    <h1>Admin Dashboard</h1>
    <nav>
      <a routerLink="users" routerLinkActive="active">Users</a> |
      <a routerLink="settings" routerLinkActive="active">Settings</a>
    </nav>
    <hr>
    <router-outlet></router-outlet> ```

**Explicación:**

* El array `children` dentro de la ruta `admin` define las sub-rutas.
* La `path` para las rutas hijas es relativa a la ruta padre (`/admin`).
* Cuando navegas a `/admin/users`, se renderizará el `AdminComponent`, y el `UsersComponent` se mostrará dentro del `<router-outlet>` del `AdminComponent`.
* `redirectTo: 'users', pathMatch: 'full'` en la ruta `admin` asegura que cuando navegas solo a `/admin`, redirigirá automáticamente a `/admin/users`.

**3. Diseño de Rutas con Parámetros de Consulta**

Los parámetros de consulta se utilizan para pasar información opcional a una ruta. Aparecen en la URL después de un signo de interrogación (`?`) y son pares clave-valor separados por ampersands (`&`).

**Ejemplo:** Una página de lista de productos donde puedes filtrar por categoría.

**Pasos:**

1.  **Configurar la Ruta (No se necesita configuración especial para los parámetros de consulta):**

    ```typescript
    // En AppRoutingModule
    const routes: Routes = [
      { path: 'products', component: ProductListComponent },
      // ... otras rutas
    ];
    ```

2.  **Navegar con Parámetros de Consulta:** Puedes navegar a la ruta con parámetros de consulta usando el servicio `Router`:

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

3.  **Acceder a los Parámetros de Consulta en el Componente:** Usa el servicio `ActivatedRoute` para acceder a los parámetros de consulta:

    ```typescript
    import { Component, OnInit } from '@angular/core';
    import { ActivatedRoute } from '@angular/router';

    @Component({
      selector: 'app-product-list',
      template: `
        <h2>Product List</h2>
        <p>Filtrando por categoría: {{ categoryFilter }}</p>
        <ul>
          <li *ngFor="let product of filteredProducts">
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

**Explicación:**

* Cuando se hace clic en el botón "Electronics", la aplicación navega a `/products?category=electronics`.
* En el `ProductListComponent`, el servicio `ActivatedRoute` proporciona un observable `queryParams`. Nos suscribimos a este observable para obtener los parámetros de consulta actuales.
* `params['category']` recupera el valor del parámetro de consulta `category`.
* Cuando la página se actualiza con los parámetros de consulta en la URL, el hook del ciclo de vida `ngOnInit` se ejecutará nuevamente, y el componente se volverá a suscribir a `queryParams`, asegurando que el filtro se aplique incluso después de una actualización.

**En resumen:**

* El enrutamiento de Angular maneja la actualización y la permanencia en la misma página por defecto, siempre que tus rutas estén correctamente configuradas y tu servidor esté configurado para deep linking.
* Las sub-rutas se diseñan usando el array `children` en tu configuración de ruta y la directiva `<router-outlet>` en la plantilla del componente padre.
* Los parámetros de consulta se añaden a la URL y se pueden acceder en tus componentes usando el observable `queryParams` del servicio `ActivatedRoute`. Esto asegura que cualquier estado gestionado a través de parámetros de consulta se conserve incluso después de una actualización de página.