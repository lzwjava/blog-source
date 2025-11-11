---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: AG Grid Angular Dunkles Theme Handbuch
translated: true
type: note
---

Verstanden — Sie fragen nach dem **Alpine Dark Theme** in **AG Grid**, wenn es in einer **Angular-Anwendung** verwendet wird.

---

### 🔹 Was ist das Alpine Dark Theme?
AG Grid bietet mehrere integrierte Themes zur Gestaltung des Grids.
Eines davon ist das **Alpine**-Theme, das sowohl in **hellen** als auch **dunklen** Varianten verfügbar ist:

- `ag-theme-alpine` → Alpine Light Theme (standardmäßiges, modernes Erscheinungsbild).
- `ag-theme-alpine-dark` → Alpine Dark Theme.

Das **Alpine Dark** Theme ist also einfach die Dark-Mode-Variante des AG Grid Alpine Themes.

---

### 🔹 Verwendung des Alpine Dark Themes in Angular + AG Grid

1. **AG Grid-Pakete installieren**
   ```bash
   npm install ag-grid-community ag-grid-angular
   ```
   (Falls Sie Enterprise-Features wünschen, fügen Sie auch `ag-grid-enterprise` hinzu.)

---

2. **AG Grid-Modul in Angular importieren**
   In Ihrer `app.module.ts`:
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

3. **AG Grid-Styles einbinden**
   In `angular.json` unter `styles` das CSS für Alpine Dark hinzufügen:
   ```json
   "styles": [
     "node_modules/ag-grid-community/styles/ag-grid.css",
     "node_modules/ag-grid-community/styles/ag-theme-alpine-dark.css",
     "src/styles.css"
   ]
   ```

---

4. **Das Theme im Template anwenden**
   In Ihrer `app.component.html`:
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

5. **Daten in der Komponente definieren**
   In `app.component.ts`:
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

### 🔹 Wechseln zwischen Alpine Light & Dark Theme
Sie können Themes dynamisch wechseln, indem Sie einfach die Klasse auf dem Grid-Container ändern:

```html
<ag-grid-angular
  class="{{ isDark ? 'ag-theme-alpine-dark' : 'ag-theme-alpine' }}"
  ...
></ag-grid-angular>
```

Und in Ihrer Komponente:
```ts
isDark = true;
```

---

✅ Das war's! Ihr AG Grid in Angular wird nun mit dem **Alpine Dark Theme** formatiert.

---

Möchten Sie, dass ich Ihnen auch zeige, **wie man zur Laufzeit zwischen Dark/Light-Themes umschaltet** (wie ein Dark-Mode-Schalter), oder reicht ein statisches Dark Grid aus?