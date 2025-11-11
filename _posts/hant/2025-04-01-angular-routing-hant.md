---
audio: false
generated: true
lang: hant
layout: post
title: Angular 中的路由設計
translated: true
type: note
---

好的，讓我們來解析如何在 Angular 中設計路由，以實現輕鬆刷新、子路由和處理查詢參數。

**1. 輕鬆刷新並停留在同一頁面**

Angular 的預設路由機制旨在無縫處理這種情況。當你導航到 Angular 應用程式中的特定路由時，瀏覽器的 URL 會改變。這個 URL 代表了應用程式的當前狀態。當你刷新頁面時，瀏覽器會向伺服器請求與該 URL 關聯的資源。然後 Angular 的路由模組會接管並渲染與該路由關聯的元件。

**關鍵點：**

* **正確的路由配置：** 確保你的路由在 `AppRoutingModule`（或你創建的任何其他路由模組）中正確定義。每個路徑都應與特定的元件關聯。
* **伺服器端配置（用於深度連結）：** 如果你使用「路徑位置策略」（這是預設值），則需要配置你的伺服器，使其為所有應用程式路由提供 `index.html` 檔案。這允許 Angular 在客戶端處理路由，即使你直接訪問深度連結或刷新頁面也是如此。

**`AppRoutingModule` 範例：**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent }, // 帶有參數的路由
  { path: '**', redirectTo: '' } // 用於未知路徑的萬用字元路由
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

在這個範例中：

* 當你導航到 `/products` 時，將渲染 `ProductListComponent`。如果你刷新頁面，你仍然會停留在 `ProductListComponent` 上。
* 當你導航到 `/products/123` 時，將渲染 `ProductDetailComponent`，並且 `id` 參數將可以在元件內訪問。刷新頁面將使你停留在同一產品詳細資訊頁面上。

**2. 設計子路由**

子路由允許你在應用程式中創建嵌套佈局。這對於那些你有一個父元件作為其他相關元件的容器的部分非常有用。

**範例：** 假設你有一個帶有「Users」和「Settings」子部分的「Admin」區域。

**步驟：**

1.  **創建父元件和子元件：**
    ```bash
    ng generate component admin
    ng generate component users
    ng generate component settings
    ```

2.  **在父元件的路由模組（或主要的 `AppRoutingModule`）中配置子路由：**

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
          { path: '', redirectTo: 'users', pathMatch: 'full' } // 預設子路由
        ]
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(adminRoutes)], // 對功能模組使用 forChild
      exports: [RouterModule]
    })
    export class AdminRoutingModule { }
    ```

    **或者，你可以在 `AppRoutingModule` 中定義它們：**

    ```typescript
    // 在 AppRoutingModule 中
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

3.  **在父元件的模板（`admin.component.html`）中添加 `<router-outlet>`：**

    ```html
    <h1>Admin Dashboard</h1>
    <nav>
      <a routerLink="users" routerLinkActive="active">Users</a> |
      <a routerLink="settings" routerLinkActive="active">Settings</a>
    </nav>
    <hr>
    <router-outlet></router-outlet> ```

**解釋：**

* `admin` 路由內的 `children` 陣列定義了子路由。
* 子路由的 `path` 是相對於父路由（`/admin`）的。
* 當你導航到 `/admin/users` 時，將渲染 `AdminComponent`，並且 `UsersComponent` 將顯示在 `AdminComponent` 的 `<router-outlet>` 內。
* `admin` 路由中的 `redirectTo: 'users', pathMatch: 'full'` 確保當你只導航到 `/admin` 時，它會自動重定向到 `/admin/users`。

**3. 設計帶有查詢參數的路由**

查詢參數用於向路由傳遞可選資訊。它們出現在 URL 中的問號（`?`）之後，並且是以「與」符號（`&`）分隔的鍵值對。

**範例：** 一個可以按類別篩選的產品列表頁面。

**步驟：**

1.  **配置路由（查詢參數不需要特殊配置）：**

    ```typescript
    // 在 AppRoutingModule 中
    const routes: Routes = [
      { path: 'products', component: ProductListComponent },
      // ... 其他路由
    ];
    ```

2.  **使用查詢參數進行導航：** 你可以使用 `Router` 服務導航到帶有查詢參數的路由：

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

3.  **在元件中訪問查詢參數：** 使用 `ActivatedRoute` 服務來訪問查詢參數：

    ```typescript
    import { Component, OnInit } from '@angular/core';
    import { ActivatedRoute } from '@angular/router';

    @Component({
      selector: 'app-product-list',
      template: `
        <h2>Product List</h2>
        <p>Filtering by category: {{ categoryFilter }}</p>
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

**解釋：**

* 當點擊「Electronics」按鈕時，應用程式會導航到 `/products?category=electronics`。
* 在 `ProductListComponent` 中，`ActivatedRoute` 服務提供了一個 `queryParams` observable。我們訂閱這個 observable 來獲取當前的查詢參數。
* `params['category']` 檢索 `category` 查詢參數的值。
* 當頁面帶有 URL 中的查詢參數被刷新時，`ngOnInit` 生命週期鉤子將再次執行，元件將重新訂閱 `queryParams`，確保即使在刷新後也會應用篩選器。

**總結：**

* Angular 的路由預設處理刷新和停留在同一頁面，前提是你的路由配置正確且你的伺服器已設置好用於深度連結。
* 子路由是使用路由配置中的 `children` 陣列和父元件模板中的 `<router-outlet>` 指令來設計的。
* 查詢參數附加在 URL 上，並可以使用 `ActivatedRoute` 服務的 `queryParams` observable 在你的元件中訪問。這確保了通過查詢參數管理的任何狀態即使在頁面刷新後也能保留下來。