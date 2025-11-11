---
audio: false
generated: true
image: false
lang: zh
layout: post
model: openai/gpt-5
title: AG Grid Angular 深色主题指南
translated: true
type: note
---

明白了 — 你是在询问在 **Angular 应用**中使用 **AG Grid** 时的 **Alpine 深色主题**。

---

### 🔹 什么是 Alpine 深色主题？
AG Grid 提供了多种内置主题用于表格样式设计。  
其中之一是 **Alpine** 主题，它包含 **浅色** 和 **深色** 两种变体：

- `ag-theme-alpine` → Alpine 浅色主题（默认现代外观）。
- `ag-theme-alpine-dark` → Alpine 深色主题。

因此，**Alpine 深色**主题就是 AG Grid Alpine 主题的深色模式变体。

---

### 🔹 在 Angular + AG Grid 中使用 Alpine 深色主题

1. **安装 AG Grid 包**
   ```bash
   npm install ag-grid-community ag-grid-angular
   ```
   （如果需要企业版功能，还需添加 `ag-grid-enterprise`。）

---

2. **在 Angular 中导入 AG Grid 模块**
   在你的 `app.module.ts` 文件中：
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

3. **引入 AG Grid 样式**
   在 `angular.json` 文件的 `styles` 部分，添加 Alpine 深色主题的 CSS：
   ```json
   "styles": [
     "node_modules/ag-grid-community/styles/ag-grid.css",
     "node_modules/ag-grid-community/styles/ag-theme-alpine-dark.css",
     "src/styles.css"
   ]
   ```

---

4. **在模板中应用主题**
   在你的 `app.component.html` 文件中：
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

5. **在组件中定义数据**
   在 `app.component.ts` 文件中：
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

### 🔹 在 Alpine 浅色与深色主题之间切换
你可以通过更改表格容器上的类来动态切换主题：

```html
<ag-grid-angular
  class="{{ isDark ? 'ag-theme-alpine-dark' : 'ag-theme-alpine' }}"
  ...
></ag-grid-angular>
```

在你的组件中：
```ts
isDark = true;
```

---

✅ 就是这样！现在你的 Angular 中的 AG Grid 将使用 **Alpine 深色主题** 进行样式设置。

---

你是希望我也展示一下 **如何在运行时在深色/浅色主题之间切换**（比如一个深色模式开关），还是静态的深色表格就足够了？