---
audio: false
generated: true
lang: ar
layout: post
title: دليل جيد لتطوير واجهات أمامية باستخدام أنجولار
translated: true
type: note
---

إنجولار هو إطار عمل قوي لبناء تطبيقات ديناميكية أحادية الصفحة (SPAs). يأخذك هذا الدليل خلال أساسيات تطوير واجهة المستخدم الأمامية باستخدام إنجولار، بدءًا من الإعداد وصولاً إلى أفضل الممارسات. سواء كنت مبتدئًا أو تريد تحديث مهاراتك، ستجد نصائح عملية ومفاهيم أساسية لمساعدتك في إنشاء تطبيقات قابلة للتوسيع والصيانة.

---

## الخطوة 1: الإعداد والتثبيت
قبل الغوص في إنجولار، تأكد من أن بيئة التطوير الخاصة بك جاهزة.

- **المتطلبات الأساسية**:  
  - قم بتثبيت [Node.js](https://nodejs.org/) (يُوصى بالإصدار LTS) و npm (مضمن مع Node.js).  
  - استخدم محرر أكواد مثل [Visual Studio Code](https://code.visualstudio.com/) للحصول على تجربة تطوير رائعة مع إضافات إنجولار.

- **تثبيت Angular CLI**:  
  يبسط واجهة سطر الأوامر الخاصة بإنجولار (CLI) عملية إنشاء المشروع وإدارته. قم بتثبيته عالميًا باستخدام:
  ```bash
  npm install -g @angular/cli
  ```

- **إنشاء مشروع جديد**:  
  قم بإنشاء تطبيق إنجولار جديد باستخدام:
  ```bash
  ng new my-angular-app
  ```
  أثناء الإعداد، سيُطلب منك:
  - تمكين التوجيه (موصى به لتطبيقات SPAs).  
  - اختيار تنسيق ورقة الأنماط (مثل CSS أو SCSS).

- **تشغيل التطبيق**:  
  قم بتشغيل خادم التطوير:
  ```bash
  ng serve
  ```
  افتح متصفحك على الرابط `http://localhost:4200/` لرؤية تطبيقك يعمل.

---

## الخطوة 2: المفاهيم الأساسية
تُبنى تطبيقات إنجولار حول عدد قليل من المفاهيم الأساسية.

### المكونات (Components)
المكونات هي اللبنات الأساسية لواجهة المستخدم الخاصة بك. لكل مكون منطق HTML و CSS و TypeScript الخاص به.  
- مثال (`app.component.ts`):
  ```typescript
  import { Component } from '@angular/core';

  @Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
  })
  export class AppComponent {
    title = 'my-angular-app';
  }
  ```

### الوحدات (Modules)
تنظم الوحدات تطبيقك إلى كتل متماسكة. الوحدة الجذرية هي `AppModule`.  
- مثال (`app.module.ts`):
  ```typescript
  import { NgModule } from '@angular/core';
  import { BrowserModule } from '@angular/platform-browser';
  import { AppComponent } from './app.component';

  @NgModule({
    declarations: [AppComponent],
    imports: [BrowserModule],
    bootstrap: [AppComponent]
  })
  export class AppModule {}
  ```

### الخدمات (Services)
تتعامل الخدمات مع المنطق المشترك أو الوصول إلى البيانات. استخدم حقن التبعية لتوفيرها للمكونات.  
- إنشاء خدمة:
  ```bash
  ng generate service data
  ```

### ربط البيانات (Data Binding)
يربط ربط البيانات بين بيانات المكون وواجهة المستخدم. يدعم إنجولار:
- **الاستيفاء (Interpolation)**: `{{ value }}`  
- **ربط الخاصية (Property Binding)**: `[property]="value"`  
- **ربط الحدث (Event Binding)**: `(event)="handler()"`  
- **الربط ثنائي الاتجاه (Two-Way Binding)**: `[(ngModel)]="value"` (يتطلب `FormsModule`).

---

## الخطوة 3: التوجيه (Routing)
يمكنك جهاز التوجيه في إنجولار من التنقل في تطبيقات SPAs دون إعادة تحميل كامل للصفحة.

- **الإعداد**:  
  قم بتمكين التوجيه عند إنشاء مشروعك (`ng new my-angular-app --routing`). يولد هذا `app-routing.module.ts`.

- **تحديد المسارات (Routes)**:  
  قم بتكوين المسارات في `app-routing.module.ts`:
  ```typescript
  import { NgModule } from '@angular/core';
  import { RouterModule, Routes } from '@angular/router';
  import { HomeComponent } from './home/home.component';
  import { AboutComponent } from './about/about.component';

  const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'about', component: AboutComponent }
  ];

  @NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
  })
  export class AppRoutingModule {}
  ```

- **منفذ الموجه (Router Outlet)**:  
  أضف `<router-outlet></router-outlet>` في `app.component.html` لعرض المكونات الموجهة.

- **التنقل**:  
  استخدم `routerLink` للروابط:
  ```html
  <a routerLink="/">الرئيسية</a>
  <a routerLink="/about">حول</a>
  ```

---

## الخطوة 4: النماذج (Forms)
تتعامل النماذج مع إدخال المستخدم، ويوفر إنجولار نهجين لذلك.

### النماذج المعتمدة على القوالب (Template-Driven Forms)
تستخدم النماذج البسيطة `ngModel` للربط ثنائي الاتجاه. تتطلب `FormsModule`.

### النماذج التفاعلية (Reactive Forms) (موصى بها)
تقدم النماذج التفاعلية تحكمًا أكبر، وهي مثالية للسيناريوهات المعقدة.  
- مثال (`my.component.ts`):
  ```typescript
  import { Component } from '@angular/core';
  import { FormBuilder, FormGroup } from '@angular/forms';

  @Component({
    selector: 'app-my',
    templateUrl: './my.component.html'
  })
  export class MyComponent {
    form: FormGroup;

    constructor(private fb: FormBuilder) {
      this.form = this.fb.group({
        name: [''],
        email: ['']
      });
    }
  }
  ```
- القالب (`my.component.html`):
  ```html
  <form [formGroup]="form">
    <input formControlName="name" placeholder="الاسم">
    <input formControlName="email" placeholder="البريد الإلكتروني">
  </form>
  ```

---

## الخطوة 5: طلبات HTTP
استخدم `HttpClient` الخاص بإنجولار لجلب البيانات من الخلفية (Backend).

- **الإعداد**:  
  قم باستيراد `HttpClientModule` في `app.module.ts`:
  ```typescript
  import { HttpClientModule } from '@angular/common/http';

  @NgModule({
    imports: [HttpClientModule, ...]
  })
  export class AppModule {}
  ```

- **إجراء الطلبات**:  
  إنشاء خدمة (`data.service.ts`):
  ```typescript
  import { Injectable } from '@angular/core';
  import { HttpClient } from '@angular/common/http';

  @Injectable({
    providedIn: 'root'
  })
  export class DataService {
    constructor(private http: HttpClient) {}

    getData() {
      return this.http.get('https://api.example.com/data');
    }
  }
  ```

- **الاستخدام في المكون**:  
  اشترك في الـ Observable:
  ```typescript
  import { Component } from '@angular/core';
  import { DataService } from './data.service';

  @Component({
    selector: 'app-my',
    template: '...'
  })
  export class MyComponent {
    constructor(private dataService: DataService) {
      this.dataService.getData().subscribe(data => {
        console.log(data);
      });
    }
  }
  ```

---

## الخطوة 6: أفضل الممارسات
- **استفد من TypeScript**: استخدم الأنواع والواجهات للحصول على كود أكثر أمانًا ونظافة.  
- **احتفظ بالمكونات صغيرة**: قسّم المكونات الكبيرة إلى قطع قابلة لإعادة الاستخدام.  
- **تحميل الوحدات بطريقة كسولة (Lazy Load Modules)**: حسّن الأداء باستخدام `loadChildren` في المسارات.  
- **استخدم Angular CLI**: أتمتة المهام (مثل `ng generate component my-component`).  
- **حسن الأداء باستخدام AOT**: قم بتمكين الترجمة المسبقة (Ahead-of-Time) (`ng build --aot`).  
- **اتبع دليل الأنماط**: راجع [دليل أنماط إنجولار الرسمي](https://angular.io/guide/styleguide).

---

## مزيد من التعلم
- [الوثائق الرسمية لإنجولار](https://angular.io/docs)  
- [Angular University](https://angular-university.io/)  
- [Stack Overflow](https://stackoverflow.com/questions/tagged/angular) للحصول على مساعدة المجتمع  

---

يمنحك هذا الدليل أساسًا متينًا لتطوير واجهة المستخدم الأمامية باستخدام إنجولار. مع تقدمك، استكشف المواضيع المتقدمة مثل إدارة الحالة (على سبيل المثال، NgRx)، واختبار الوحدات، وتحسين الأداء. تمنياتنا بالترمجة السعيدة!