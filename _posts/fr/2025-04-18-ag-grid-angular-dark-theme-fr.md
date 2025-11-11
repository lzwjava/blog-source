---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide du thème sombre pour AG Grid et Angular
translated: true
type: note
---

Compris — vous vous interrogez sur le **Alpine Dark Theme** dans **AG Grid** lors de son utilisation dans une **application Angular**.

---

### 🔹 Qu'est-ce que le Alpine Dark Theme ?
AG Grid fournit plusieurs thèmes intégrés pour styliser le grid.
L'un d'eux est le thème **Alpine**, qui existe en variantes **claire** et **sombre** :

- `ag-theme-alpine` → Thème Alpine Light (apparence moderne par défaut).
- `ag-theme-alpine-dark` → Thème Alpine Dark.

Ainsi, le thème **Alpine Dark** est simplement la variante en mode sombre du thème Alpine d'AG Grid.

---

### 🔹 Utilisation du Alpine Dark Theme dans Angular + AG Grid

1. **Installer les Paquets AG Grid**
   ```bash
   npm install ag-grid-community ag-grid-angular
   ```
   (Si vous voulez les fonctionnalités enterprise, ajoutez aussi `ag-grid-enterprise`.)

---

2. **Importer le Module AG Grid dans Angular**
   Dans votre `app.module.ts` :
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

3. **Inclure les Styles AG Grid**
   Dans `angular.json`, sous `styles`, ajoutez le CSS pour Alpine Dark :
   ```json
   "styles": [
     "node_modules/ag-grid-community/styles/ag-grid.css",
     "node_modules/ag-grid-community/styles/ag-theme-alpine-dark.css",
     "src/styles.css"
   ]
   ```

---

4. **Appliquer le Thème dans le Template**
   Dans votre `app.component.html` :
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

5. **Définir les Données dans le Composant**
   Dans `app.component.ts` :
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

### 🔹 Basculer entre les Thèmes Alpine Light et Dark
Vous pouvez changer de thème dynamiquement simplement en modifiant la classe sur le conteneur du grid :

```html
<ag-grid-angular
  class="{{ isDark ? 'ag-theme-alpine-dark' : 'ag-theme-alpine' }}"
  ...
></ag-grid-angular>
```

Et dans votre composant :
```ts
isDark = true;
```

---

✅ C'est tout ! Votre AG Grid dans Angular sera maintenant stylisé avec le **Alpine Dark Theme**.

---

Souhaitez-vous que je vous montre également **comment basculer entre les thèmes sombre/clair à l'exécution** (comme un interrupteur de mode sombre), ou un grid sombre statique suffit-il ?