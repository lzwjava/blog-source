---
audio: false
generated: true
lang: ar
layout: post
title: تصميم المسارات في أنجولار
translated: true
type: note
---

حسنًا، دعنا نفكك كيفية تصميم المسارات (Routes) في Angular لتسهيل عملية التحديث، وإنشاء المسارات الفرعية، والتعامل مع معلمات الاستعلام (Query Parameters).

**1. التحديث السهل والبقاء على نفس الصفحة**

تم تصميم آلية التوجيه الافتراضية في Angular للتعامل مع هذا بسلاسة. عندما تنتقل إلى مسار محدد في تطبيق Angular، يتغير عنوان URL في المتصفح. يمثل عنوان URL هذا الحالة الحالية لتطبيقك. عند تحديث الصفحة، يطلب المتصفح المورد المرتبط بعنوان URL ذلك. ثم تتولى وحدة التوجيه في Angular الأمر وتقوم بعرض المكون المرتبط بهذا المسار.

**النقاط الرئيسية:**

* **تكوين المسار بشكل صحيح:** تأكد من تعريف مساراتك بشكل صحيح في `AppRoutingModule` (أي وحدة توجيه أخرى قمت بإنشائها). يجب أن يرتبط كل مسار بمكون محدد.
* **تكوين جانب الخادم (للربط العميق Deep Linking):** إذا كنت تستخدم "إستراتيجية موقع المسار" (path location strategy) (وهي الإعداد الافتراضي)، فيجب تكوين خادمك لخدمة ملف `index.html` لجميع مسارات التطبيق. هذا يسمح لـ Angular بالتعامل مع التوجيه على جانب العميل حتى عند الوصول المباشر إلى رابط عميق أو عند التحديث.

**مثال `AppRoutingModule`:**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent }, // مسار يحتوي على معامل (parameter)
  { path: '**', redirectTo: '' } // مسار عام (Wildcard route) للمسارات غير المعروفة
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

في هذا المثال:

* عند الانتقال إلى `/products`، سيتم عرض `ProductListComponent`. إذا قمت بتحديث الصفحة، ستظل على `ProductListComponent`.
* عند الانتقال إلى `/products/123`، سيتم عرض `ProductDetailComponent`، وسيكون معامل `id` قابلاً للوصول داخل المكون. سيؤدي التحديث إلى إبقائك على نفس صفحة تفاصيل المنتج.

**2. تصميم المسارات الفرعية (Child Routes)**

تسمح المسارات الفرعية، أو المسارات التابعة، بإنشاء تخطيطات متداخلة داخل تطبيقك. هذا مفيد للأقسام التي يكون فيها مكون أصل (parent) يعمل كحاوية لمكونات أخرى مرتبطة.

**مثال:** لنفترض أن لديك قسم "Admin" به أقسام فرعية مثل "Users" و "Settings".

**الخطوات:**

1.  **إنشاء المكونات الأصلية والتابعة:**
    ```bash
    ng generate component admin
    ng generate component users
    ng generate component settings
    ```

2.  **تكوين المسارات التابعة في وحدة توجيه المكون الأصل (أو في `AppRoutingModule` الرئيسي):**

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
          { path: '', redirectTo: 'users', pathMatch: 'full' } // المسار التابع الافتراضي
        ]
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(adminRoutes)], // استخدم forChild لوحدات الميزات (feature modules)
      exports: [RouterModule]
    })
    export class AdminRoutingModule { }
    ```

    **بدلاً من ذلك، يمكنك تعريفها في `AppRoutingModule` الخاص بك:**

    ```typescript
    // في AppRoutingModule
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

3.  **أضف `<router-outlet>` في قالب المكون الأصل (`admin.component.html`):**

    ```html
    <h1>Admin Dashboard</h1>
    <nav>
      <a routerLink="users" routerLinkActive="active">Users</a> |
      <a routerLink="settings" routerLinkActive="active">Settings</a>
    </nav>
    <hr>
    <router-outlet></router-outlet> ```

**الشرح:**

* مصفوفة `children` داخل مسار `admin` تحدد المسارات التابعة.
* `path` للمسارات التابعة تكون نسبية بالنسبة للمسار الأصل (`/admin`).
* عند الانتقال إلى `/admin/users`، سيتم عرض `AdminComponent`، وسيتم عرض `UsersComponent` داخل `<router-outlet>` الخاص بـ `AdminComponent`.
* `redirectTo: 'users', pathMatch: 'full'` في مسار `admin` تضمن أنه عند الانتقال إلى `/admin` فقط، سيتم إعادة التوجيه تلقائيًا إلى `/admin/users`.

**3. تصميم المسارات مع معلمات الاستعلام (Query Parameters)**

تُستخدم معلمات الاستعلام لتمرير معلومات اختيارية إلى مسار. تظهر في عنوان URL بعد علامة الاستفهام (`?`) وهي أزواج من المفاتيح والقيم مفصولة بعلامة (`&`).

**مثال:** صفحة قائمة منتجات حيث يمكنك التصفية حسب الفئة.

**الخطوات:**

1.  **تكوين المسار (لا حاجة لتكوين خاص لمعلمات الاستعلام):**

    ```typescript
    // في AppRoutingModule
    const routes: Routes = [
      { path: 'products', component: ProductListComponent },
      // ... مسارات أخرى
    ];
    ```

2.  **الانتقال مع معلمات الاستعلام:** يمكنك الانتقال إلى المسار مع معلمات الاستعلام باستخدام خدمة `Router`:

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

3.  **الوصول إلى معلمات الاستعلام في المكون:** استخدم خدمة `ActivatedRoute` للوصول إلى معلمات الاستعلام:

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

**الشرح:**

* عند النقر على زر "Electronics"، ينتقل التطبيق إلى `/products?category=electronics`.
* في `ProductListComponent`، توفر خدمة `ActivatedRoute` خاصية `queryParams` القابلة للملاحظة (observable). نشترك في هذه الخاصية للحصول على معلمات الاستعلام الحالية.
* `params['category']` تسترجع قيمة معامل الاستعلام `category`.
* عند تحديث الصفحة مع وجود معلمات الاستعلام في عنوان URL، ستنفذ دورة الحياة `ngOnInit` مرة أخرى، وسيعيد المكون الاشتراك في `queryParams`، مما يضمن تطبيق التصفية حتى بعد التحديث.

**باختصار:**

* يتعامل توجيه Angular مع التحديث والبقاء على نفس الصفحة افتراضيًا، بشرط تكوين مساراتك بشكل صحيح وإعداد خادمك للربط العميق.
* يتم تصميم المسارات الفرعية باستخدام مصفوفة `children` في تكوين المسار وأمر `<router-outlet>` في قالب المكون الأصل.
* تُلحق معلمات الاستعلام بعنوان URL ويمكن الوصول إليها في مكوناتك باستخدام خاصية `queryParams` القابلة للملاحظة التابعة لخدمة `ActivatedRoute`. يضمن هذا الحفاظ على أي حالة تتم إدارتها عبر معلمات الاستعلام حتى بعد تحديث الصفحة.