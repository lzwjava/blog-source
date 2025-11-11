---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía del Tema Oscuro de AG Grid Angular
translated: true
type: note
---

Entendido — estás preguntando sobre **Alpine Dark Theme** en **AG Grid** cuando se usa en una **aplicación Angular**.

---

### 🔹 ¿Qué es Alpine Dark Theme?
AG Grid proporciona varios temas integrados para estilizar la cuadrícula.  
Uno de ellos es el tema **Alpine**, que viene en variantes **clara** y **oscura**:

- `ag-theme-alpine` → Tema Alpine Claro (apariencia moderna por defecto).
- `ag-theme-alpine-dark` → Tema Alpine Oscuro.

Por lo tanto, el tema **Alpine Dark** es simplemente la variante de modo oscuro del tema Alpine de AG Grid.

---

### 🔹 Usando Alpine Dark Theme en Angular + AG Grid

1. **Instalar los Paquetes de AG Grid**
   ```bash
   npm install ag-grid-community ag-grid-angular
   ```
   (Si quieres funciones enterprise, añade también `ag-grid-enterprise`.)

---

2. **Importar el Módulo de AG Grid en Angular**
   En tu `app.module.ts`:
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

3. **Incluir los Estilos de AG Grid**
   En `angular.json`, bajo `styles`, añade el CSS para Alpine Dark:
   ```json
   "styles": [
     "node_modules/ag-grid-community/styles/ag-grid.css",
     "node_modules/ag-grid-community/styles/ag-theme-alpine-dark.css",
     "src/styles.css"
   ]
   ```

---

4. **Aplicar el Tema en la Plantilla**
   En tu `app.component.html`:
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

5. **Definir los Datos en el Componente**
   En `app.component.ts`:
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

### 🔹 Cambiar entre Alpine Light & Dark Theme
Puedes cambiar dinámicamente de tema simplemente cambiando la clase en el contenedor de la cuadrícula:

```html
<ag-grid-angular
  class="{{ isDark ? 'ag-theme-alpine-dark' : 'ag-theme-alpine' }}"
  ...
></ag-grid-angular>
```

Y en tu componente:
```ts
isDark = true;
```

---

✅ ¡Eso es todo! Ahora tu AG Grid en Angular estará estilizado con el **Alpine Dark Theme**.

---

¿Te gustaría que también te muestre **cómo alternar entre temas oscuro/claro en tiempo de ejecución** (como un interruptor de modo oscuro), o es suficiente con una cuadrícula oscura estática?