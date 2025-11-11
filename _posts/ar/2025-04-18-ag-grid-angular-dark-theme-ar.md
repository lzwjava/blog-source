---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: دليل الثيم الداكن لـ AG Grid مع Angular
translated: true
type: note
---

فهمت — أنت تسأل عن **Alpine Dark Theme** في **AG Grid** عند استخدامه في **تطبيق Angular**.

---

### 🔹 ما هو Alpine Dark Theme؟
يوفر AG Grid عدة سمات مدمجة لتنسيق الشبكة.  
إحداها هي سمة **Alpine**، والتي تأتي بكل من المتغيرين **الفاتح** و**الغامق**:

- `ag-theme-alpine` → سمة Alpine الفاتحة (المظهر الحديث الافتراضي).
- `ag-theme-alpine-dark` → سمة Alpine الغامقة.

لذا، فإن سمة **Alpine Dark** هي ببساطة متغير الوضع الداكن لسمة Alpine في AG Grid.

---

### 🔹 استخدام سمة Alpine Dark في Angular + AG Grid

1. **تثبيت حزم AG Grid**
   ```bash
   npm install ag-grid-community ag-grid-angular
   ```
   (إذا كنت تريد ميزات Enterprise، أضف أيضًا `ag-grid-enterprise`.)

---

2. **استيراد وحدة AG Grid في Angular**
   في ملف `app.module.ts` الخاص بك:
   ```ts
   import { AgGridModule } from 'ag-grid-angular';
   import { NgModule } from '@angular/core';
   import { BrowserModule } from '@angular/platform-browser';

   import { AppComponent } from './app.component';

   @NgModule({
     declarations: [AppComponent],
     imports: [
       BrowserModule,
       AgGridModule
     ],
     providers: [],
     bootstrap: [AppComponent]
   })
   export class AppModule {}
   ```

---

3. **تضمين أنماط AG Grid**
   في ملف `angular.json`، تحت `styles`، أضف CSS لـ Alpine Dark:
   ```json
   "styles": [
     "node_modules/ag-grid-community/styles/ag-grid.css",
     "node_modules/ag-grid-community/styles/ag-theme-alpine-dark.css",
     "src/styles.css"
   ]
   ```

---

4. **تطبيق السمة في القالب**
   في ملف `app.component.html` الخاص بك:
   ```html
   <ag-grid-angular
     style="width: 100%; height: 500px;"
     class="ag-theme-alpine-dark"
     [rowData]="rowData"
     [columnDefs]="columnDefs"
     [defaultColDef]="defaultColDef"
   ></ag-grid-angular>
   ```

---

5. **تحديد البيانات في المكون**
   في ملف `app.component.ts`:
   ```ts
   import { Component } from '@angular/core';
   import { ColDef } from 'ag-grid-community';

   @Component({
     selector: 'app-root',
     templateUrl: './app.component.html',
     styleUrls: ['./app.component.css']
   })
   export class AppComponent {
     columnDefs: ColDef[] = [
       { field: 'make', sortable: true, filter: true },
       { field: 'model', sortable: true, filter: true },
       { field: 'price', sortable: true, filter: true }
     ];

     rowData = [
       { make: 'Toyota', model: 'Celica', price: 35000 },
       { make: 'Ford', model: 'Mondeo', price: 32000 },
       { make: 'Porsche', model: 'Boxster', price: 72000 }
     ];

     defaultColDef: ColDef = {
       flex: 1,
       minWidth: 100,
       resizable: true
     };
   }
   ```

---

### 🔹 التبديل بين سمة Alpine الفاتحة والغامقة
يمكنك تبديل السمات ديناميكيًا فقط عن طريق تغيير الـ class في حاوية الشبكة:

```html
<ag-grid-angular
  class="{{ isDark ? 'ag-theme-alpine-dark' : 'ag-theme-alpine' }}"
  ...
></ag-grid-angular>
```

وفي المكون الخاص بك:
```ts
isDark = true;
```

---

✅ هذا كل شيء! الآن سيتم تنسيق AG Grid في Angular الخاص بك باستخدام **سمة Alpine Dark Theme**.

---

هل تريد مني أيضًا أن أوضح لك **كيفية التبديل بين السمات الغامقة والفاتحة أثناء التشغيل** (مثل مفتاح الوضع الداكن)، أم أن الشبكة الثابتة بالوضع الداكن كافية؟