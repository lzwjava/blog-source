---
audio: false
generated: true
lang: ja
layout: post
title: Angularでのデザインルート
translated: true
type: note
---

Angularでリフレッシュが容易で、サブルートやクエリパラメータを扱えるルートを設計する方法を解説します。

**1. 容易なリフレッシュと同一ページの維持**

Angularのデフォルトのルーティングメカニズムは、これをシームレスに処理するように設計されています。Angularアプリケーションで特定のルートにナビゲートすると、ブラウザのURLが変更されます。このURLはアプリケーションの現在の状態を表します。ページをリフレッシュすると、ブラウザはそのURLに関連付けられたリソースをサーバーに要求します。その後、Angularのルーティングモジュールが制御を引き継ぎ、そのルートに関連付けられたコンポーネントをレンダリングします。

**重要なポイント:**

*   **正しいルート設定:** `AppRoutingModule`（または作成した他のルーティングモジュール）でルートが正しく定義されていることを確認してください。各パスは特定のコンポーネントに関連付けられる必要があります。
*   **サーバーサイド設定（ディープリンキング用）:** 「パスロケーションストラテジー」（デフォルト）を使用している場合、すべてのアプリケーションルートに対して `index.html` ファイルを提供するようにサーバーを設定する必要があります。これにより、ディープリンクに直接アクセスしたり、リフレッシュしたりした場合でも、Angularがクライアントサイドでルーティングを処理できるようになります。

**`AppRoutingModule` の例:**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent }, // パラメータ付きルート
  { path: '**', redirectTo: '' } // 未知のパス用のワイルドカードルート
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

この例では:

*   `/products` にナビゲートすると、`ProductListComponent` がレンダリングされます。ページをリフレッシュしても、`ProductListComponent` のままです。
*   `/products/123` にナビゲートすると、`ProductDetailComponent` がレンダリングされ、`id` パラメータがコンポーネント内でアクセス可能になります。リフレッシュしても同じ商品詳細ページに留まります。

**2. サブルート（子ルート）の設計**

サブルート、または子ルートを使用すると、アプリケーション内にネストされたレイアウトを作成できます。これは、親コンポーネントが他の関連コンポーネントのコンテナとして機能するセクションで有用です。

**例:** 「Users」と「Settings」というサブセクションを持つ「Admin」セクションがあるとします。

**手順:**

1.  **親コンポーネントと子コンポーネントを作成:**
    ```bash
    ng generate component admin
    ng generate component users
    ng generate component settings
    ```

2.  **親のルーティングモジュール（またはメインの `AppRoutingModule`）で子ルートを設定:**

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
          { path: '', redirectTo: 'users', pathMatch: 'full' } // デフォルトの子ルート
        ]
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(adminRoutes)], // フィーチャーモジュールには forChild を使用
      exports: [RouterModule]
    })
    export class AdminRoutingModule { }
    ```

    **または、`AppRoutingModule` で定義することも可能:**

    ```typescript
    // AppRoutingModule 内
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

3.  **親コンポーネントのテンプレート (`admin.component.html`) に `<router-outlet>` を追加:**

    ```html
    <h1>Admin Dashboard</h1>
    <nav>
      <a routerLink="users" routerLinkActive="active">Users</a> |
      <a routerLink="settings" routerLinkActive="active">Settings</a>
    </nav>
    <hr>
    <router-outlet></router-outlet>
    ```

**説明:**

*   `admin` ルート内の `children` 配列がサブルートを定義します。
*   子ルートの `path` は親ルート (`/admin`) からの相対パスです。
*   `/admin/users` にナビゲートすると、`AdminComponent` がレンダリングされ、`UsersComponent` が `AdminComponent` の `<router-outlet>` 内に表示されます。
*   `admin` ルート内の `redirectTo: 'users', pathMatch: 'full'` は、`/admin` にナビゲートした場合に、自動的に `/admin/users` にリダイレクトすることを保証します。

**3. クエリパラメータを使用したルートの設計**

クエリパラメータは、ルートにオプションの情報を渡すために使用されます。URL内で疑問符 (`?`) の後に現れ、アンパサンド (`&`) で区切られたキーと値のペアです。

**例:** カテゴリでフィルタリングできる商品一覧ページ。

**手順:**

1.  **ルートを設定（クエリパラメータ用の特別な設定は不要）:**

    ```typescript
    // AppRoutingModule 内
    const routes: Routes = [
      { path: 'products', component: ProductListComponent },
      // ... 他のルート
    ];
    ```

2.  **クエリパラメータ付きでナビゲート:** `Router` サービスを使用して、クエリパラメータ付きでルートにナビゲートできます:

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

3.  **コンポーネント内でクエリパラメータにアクセス:** `ActivatedRoute` サービスを使用してクエリパラメータにアクセスします:

    ```typescript
    import { Component, OnInit } from '@angular/core';
    import { ActivatedRoute } from '@angular/router';

    @Component({
      selector: 'app-product-list',
      template: `
        <h2>Product List</h2>
        <p>Filtering by category: {{ categoryFilter }}</p>
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

**説明:**

*   「Electronics」ボタンがクリックされると、アプリケーションは `/products?category=electronics` にナビゲートします。
*   `ProductListComponent` では、`ActivatedRoute` サービスが `queryParams` オブザーバブルを提供します。このオブザーバブルを購読して現在のクエリパラメータを取得します。
*   `params['category']` は `category` クエリパラメータの値を取得します。
*   クエリパラメータがURLに含まれた状態でページがリフレッシュされると、`ngOnInit` ライフサイクルフックが再び実行され、コンポーネントは `queryParams` を再購読するため、リフレッシュ後もフィルタが適用された状態が維持されます。

**まとめ:**

*   Angularのルーティングは、ルートが正しく設定され、サーバーがディープリンキング用に設定されていれば、リフレッシュと同一ページの維持をデフォルトで処理します。
*   サブルートは、ルート設定内の `children` 配列と親コンポーネントのテンプレート内の `<router-outlet>` ディレクティブを使用して設計されます。
*   クエリパラメータはURLに追加され、コンポーネント内で `ActivatedRoute` サービスの `queryParams` オブザーバブルを使用してアクセスできます。これにより、クエリパラメータを通じて管理される状態は、ページのリフレッシュ後も保持されます。