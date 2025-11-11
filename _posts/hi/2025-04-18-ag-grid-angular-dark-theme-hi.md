---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: एजी ग्रिड एंगुलर डार्क थीम गाइड
translated: true
type: note
---

ठीक है — आप **Angular एप्लिकेशन** में **AG Grid** के **Alpine Dark Theme** के बारे में पूछ रहे हैं।

---

### 🔹 Alpine Dark Theme क्या है?
AG Grid ग्रिड को स्टाइल करने के लिए कई बिल्ट-इन थीम प्रदान करता है।  
उनमें से एक **Alpine** थीम है, जो **लाइट** और **डार्क** दोनों वेरिएंट में आती है:

- `ag-theme-alpine` → Alpine लाइट थीम (डिफ़ॉल्ट मॉडर्न लुक)।
- `ag-theme-alpine-dark` → Alpine डार्क थीम।

तो, **Alpine Dark** थीम, AG Grid की Alpine थीम का डार्क मोड वेरिएंट है।

---

### 🔹 Angular + AG Grid में Alpine Dark Theme का उपयोग करना

1. **AG Grid पैकेज इंस्टॉल करें**
   ```bash
   npm install ag-grid-community ag-grid-angular
   ```
   (यदि आप एंटरप्राइज़ फीचर्स चाहते हैं, तो `ag-grid-enterprise` भी एड करें।)

---

2. **Angular में AG Grid मॉड्यूल इम्पोर्ट करें**
   अपने `app.module.ts` में:
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

3. **AG Grid स्टाइल्स शामिल करें**
   `angular.json` में, `styles` के अंदर, Alpine Dark के लिए CSS एड करें:
   ```json
   "styles": [
     "node_modules/ag-grid-community/styles/ag-grid.css",
     "node_modules/ag-grid-community/styles/ag-theme-alpine-dark.css",
     "src/styles.css"
   ]
   ```

---

4. **टेम्पलेट में थीम लागू करें**
   अपने `app.component.html` में:
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

5. **कम्पोनेंट में डेटा डिफाइन करें**
   `app.component.ts` में:
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

### 🔹 Alpine Light और Dark Theme के बीच स्विच करना
आप ग्रिड कंटेनर पर क्लास बदलकर थीम्स को डायनामिक रूप से स्विच कर सकते हैं:

```html
<ag-grid-angular
  class="{{ isDark ? 'ag-theme-alpine-dark' : 'ag-theme-alpine' }}"
  ...
></ag-grid-angular>
```

और अपने कम्पोनेंट में:
```ts
isDark = true;
```

---

✅ बस! अब आपकी Angular में AG Grid **Alpine Dark Theme** के साथ स्टाइल हो जाएगी।

---

क्या आप मुझे **रनटाइम पर डार्क/लाइट थीम के बीच टॉगल करना** (जैसे एक डार्क मोड स्विच) भी दिखाना चाहेंगे, या एक स्टेटिक डार्क ग्रिड ही काफी है?