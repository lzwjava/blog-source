---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: AG Grid Angular 深色主題指南
translated: true
type: note
---

明白了 — 你詢問的是在 **Angular 應用程式**中使用 **AG Grid** 時的 **Alpine 深色主題**。

---

### 🔹 什麼是 Alpine 深色主題？
AG Grid 提供了多種內建主題來設定表格樣式。  
其中一個是 **Alpine** 主題，它包含 **淺色** 和 **深色** 兩種變體：

- `ag-theme-alpine` → Alpine 淺色主題（預設現代外觀）。
- `ag-theme-alpine-dark` → Alpine 深色主題。

因此，**Alpine 深色**主題就是 AG Grid Alpine 主題的深色模式變體。

---

### 🔹 在 Angular + AG Grid 中使用 Alpine 深色主題

1. **安裝 AG Grid 套件**
   ```bash
   npm install ag-grid-community ag-grid-angular
   ```
   （如果需要企業版功能，請同時安裝 `ag-grid-enterprise`。）

---

2. **在 Angular 中引入 AG Grid 模組**
   在你的 `app.module.ts` 中：
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

3. **引入 AG Grid 樣式**
   在 `angular.json` 中，於 `styles` 部分加入 Alpine 深色的 CSS：
   ```json
   "styles": [
     "node_modules/ag-grid-community/styles/ag-grid.css",
     "node_modules/ag-grid-community/styles/ag-theme-alpine-dark.css",
     "src/styles.css"
   ]
   ```

---

4. **在模板中套用主題**
   在你的 `app.component.html` 中：
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

5. **在元件中定義資料**
   在 `app.component.ts` 中：
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

### 🔹 在 Alpine 淺色與深色主題之間切換
你可以透過更改表格容器上的類別來動態切換主題：

```html
<ag-grid-angular
  class="{{ isDark ? 'ag-theme-alpine-dark' : 'ag-theme-alpine' }}"
  ...
></ag-grid-angular>
```

並在你的元件中：
```ts
isDark = true;
```

---

✅ 這樣就完成了！現在你的 Angular 中的 AG Grid 將會套用 **Alpine 深色主題** 的樣式。

---

你是否也希望我示範 **如何在運行時切換深色/淺色主題**（例如深色模式開關），還是靜態的深色表格已經足夠？