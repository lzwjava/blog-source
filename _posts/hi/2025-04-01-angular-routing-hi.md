---
audio: false
generated: true
lang: hi
layout: post
title: एंगुलर में डिज़ाइन रूट्स
translated: true
type: note
---

ठीक है, आइए समझते हैं कि Angular में रूट्स को आसान रीफ्रेश, सब-रूट्स और क्वेरी पैरामीटर्स को हैंडल करने के लिए कैसे डिज़ाइन किया जाए।

**1. आसान रीफ्रेश और उसी पेज पर बने रहना**

Angular की डिफ़ॉल्ट रूटिंग मैकेनिज्म इसे सहजता से संभालने के लिए डिज़ाइन की गई है। जब आप अपने Angular एप्लिकेशन में किसी विशेष रूट पर नेविगेट करते हैं, तो ब्राउज़र का URL बदल जाता है। यह URL आपके एप्लिकेशन की वर्तमान स्थिति को दर्शाता है। जब आप पेज को रीफ्रेश करते हैं, तो ब्राउज़र उस URL से संबंधित रिसोर्स के लिए सर्वर को रिक्वेस्ट भेजता है। Angular का रूटिंग मॉड्यूल फिर कंट्रोल लेता है और उस रूट से संबंधित कंपोनेंट रेंडर करता है।

**मुख्य बिंदु:**

* **सही रूट कॉन्फ़िगरेशन:** सुनिश्चित करें कि आपके रूट आपके `AppRoutingModule` (या आपके द्वारा बनाए गए किसी अन्य रूटिंग मॉड्यूल) में सही तरीके से परिभाषित हैं। प्रत्येक पथ एक विशिष्ट कंपोनेंट से जुड़ा होना चाहिए।
* **सर्वर-साइड कॉन्फ़िगरेशन (डीप लिंकिंग के लिए):** यदि आप "पाथ लोकेशन स्ट्रैटेजी" (जो डिफ़ॉल्ट है) का उपयोग कर रहे हैं, तो आपके सर्वर को सभी एप्लिकेशन रूट्स के लिए `index.html` फ़ाइल सर्व करने के लिए कॉन्फ़िगर किया जाना चाहिए। यह Angular को क्लाइंट-साइड रूटिंग को हैंडल करने की अनुमति देता है, भले ही आप सीधे किसी डीप लिंक को एक्सेस करें या रीफ्रेश करें।

**उदाहरण `AppRoutingModule`:**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent }, // एक पैरामीटर के साथ रूट
  { path: '**', redirectTo: '' } // अज्ञात पथों के लिए वाइल्डकार्ड रूट
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

इस उदाहरण में:

* जब आप `/products` पर नेविगेट करते हैं, तो `ProductListComponent` रेंडर होगा। यदि आप पेज को रीफ्रेश करते हैं, तो आप अभी भी `ProductListComponent` पर होंगे।
* जब आप `/products/123` पर नेविगेट करते हैं, तो `ProductDetailComponent` रेंडर होगा, और `id` पैरामीटर कंपोनेंट के अंदर एक्सेसिबल होगा। रीफ्रेश करने पर आप उसी प्रोडक्ट डिटेल पेज पर बने रहेंगे।

**2. सब-रूट्स (चाइल्ड रूट्स) डिज़ाइन करना**

सब-रूट्स, या चाइल्ड रूट्स, आपको अपने एप्लिकेशन के अंदर नेस्टेड लेआउट बनाने की अनुमति देते हैं। यह उन सेक्शन्स के लिए उपयोगी है जहां आपके पास एक पैरेंट कंपोनेंट होता है जो अन्य संबंधित कंपोनेंट्स के लिए एक कंटेनर के रूप में कार्य करता है।

**उदाहरण:** मान लीजिए आपके पास "एडमिन" सेक्शन है जिसमें "यूजर्स" और "सेटिंग्स" सब-सेक्शन हैं।

**चरण:**

1.  **पैरेंट और चाइल्ड कंपोनेंट बनाएँ:**
    ```bash
    ng generate component admin
    ng generate component users
    ng generate component settings
    ```

2.  **पैरेंट के रूटिंग मॉड्यूल (या मुख्य `AppRoutingModule`) में चाइल्ड रूट्स कॉन्फ़िगर करें:**

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
          { path: '', redirectTo: 'users', pathMatch: 'full' } // डिफ़ॉल्ट चाइल्ड रूट
        ]
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(adminRoutes)], // फीचर मॉड्यूल के लिए forChild का उपयोग करें
      exports: [RouterModule]
    })
    export class AdminRoutingModule { }
    ```

    **वैकल्पिक रूप से, आप उन्हें अपने `AppRoutingModule` में परिभाषित कर सकते हैं:**

    ```typescript
    // AppRoutingModule में
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

3.  **पैरेंट कंपोनेंट के टेम्पलेट (`admin.component.html`) में `<router-outlet>` जोड़ें:**

    ```html
    <h1>Admin Dashboard</h1>
    <nav>
      <a routerLink="users" routerLinkActive="active">Users</a> |
      <a routerLink="settings" routerLinkActive="active">Settings</a>
    </nav>
    <hr>
    <router-outlet></router-outlet> ```

**स्पष्टीकरण:**

* `admin` रूट के अंदर `children` ऐरे सब-रूट्स को परिभाषित करता है।
* चाइल्ड रूट्स के लिए `path` पैरेंट रूट (`/admin`) के सापेक्ष होती है।
* जब आप `/admin/users` पर नेविगेट करते हैं, तो `AdminComponent` रेंडर होगा, और `UsersComponent` `AdminComponent` के `<router-outlet>` के अंदर प्रदर्शित होगा।
* `admin` रूट में `redirectTo: 'users', pathMatch: 'full'` यह सुनिश्चित करता है कि जब आप सिर्फ `/admin` पर नेविगेट करते हैं, तो यह स्वचालित रूप से `/admin/users` पर रीडायरेक्ट हो जाएगा।

**3. क्वेरी पैरामीटर्स के साथ रूट्स डिज़ाइन करना**

क्वेरी पैरामीटर्स का उपयोग किसी रूट को वैकल्पिक जानकारी पास करने के लिए किया जाता है। वे URL में प्रश्न चिह्न (`?`) के बाद दिखाई देते हैं और एम्परसेंड (`&`) द्वारा अलग किए गए की-वैल्यू पेयर होते हैं।

**उदाहरण:** एक प्रोडक्ट लिस्ट पेज जहां आप श्रेणी के अनुसार फिल्टर कर सकते हैं।

**चरण:**

1.  **रूट कॉन्फ़िगर करें (क्वेरी पैरामीटर्स के लिए किसी विशेष कॉन्फ़िगरेशन की आवश्यकता नहीं है):**

    ```typescript
    // AppRoutingModule में
    const routes: Routes = [
      { path: 'products', component: ProductListComponent },
      // ... अन्य रूट्स
    ];
    ```

2.  **क्वेरी पैरामीटर्स के साथ नेविगेट करें:** आप `Router` सर्विस का उपयोग करके क्वेरी पैरामीटर्स के साथ रूट पर नेविगेट कर सकते हैं:

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

3.  **कंपोनेंट में क्वेरी पैरामीटर्स तक पहुंचें:** क्वेरी पैरामीटर्स तक पहुंचने के लिए `ActivatedRoute` सर्विस का उपयोग करें:

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

**स्पष्टीकरण:**

* जब "Electronics" बटन क्लिक किया जाता है, तो एप्लिकेशन `/products?category=electronics` पर नेविगेट करता है।
* `ProductListComponent` में, `ActivatedRoute` सर्विस एक `queryParams` ऑब्ज़र्वेबल प्रदान करती है। हम वर्तमान क्वेरी पैरामीटर्स प्राप्त करने के लिए इस ऑब्ज़र्वेबल की सदस्यता लेते हैं।
* `params['category']` `category` क्वेरी पैरामीटर का मान प्राप्त करता है।
* जब पेज URL में क्वेरी पैरामीटर्स के साथ रीफ्रेश किया जाता है, तो `ngOnInit` लाइफसाइकल हुक फिर से एक्ज़िक्यूट होगा, और कंपोनेंट `queryParams` की सदस्यता फिर से लेगा, यह सुनिश्चित करते हुए कि फिल्टर रीफ्रेश के बाद भी लागू रहे।

**संक्षेप में:**

* Angular की रूटिंग डिफ़ॉल्ट रूप से रीफ्रेशिंग और उसी पेज पर बने रहने को हैंडल करती है, बशर्ते आपके रूट सही तरीके से कॉन्फ़िगर हों और आपका सर्वर डीप लिंकिंग के लिए सेट अप हो।
* सब-रूट्स को आपके रूट कॉन्फ़िगरेशन में `children` ऐरे और पैरेंट कंपोनेंट के टेम्पलेट में `<router-outlet>` डायरेक्टिव का उपयोग करके डिज़ाइन किया जाता है।
* क्वेरी पैरामीटर्स URL में जोड़े जाते हैं और आपके कंपोनेंट्स में `ActivatedRoute` सर्विस के `queryParams` ऑब्ज़र्वेबल का उपयोग करके एक्सेस किए जा सकते हैं। यह सुनिश्चित करता है कि क्वेरी पैरामीटर्स के माध्यम से प्रबंधित कोई भी स्टेट पेज रीफ्रेश के बाद भी संरक्षित रहता है।