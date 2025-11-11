---
audio: false
generated: true
lang: hant
layout: post
title: 優質Angular前端開發指南
translated: true
type: note
---

Angular 是一個強大的框架，用於建構動態單頁應用程式（SPA）。本指南將帶您掌握 Angular 前端開發的核心要點，從環境設定到最佳實踐。無論您是初學者還是想精進技能，都能在此找到實用技巧與關鍵概念，助您打造可擴展且易維護的應用程式。

---

## 步驟一：環境設定與安裝
在開始使用 Angular 前，請先準備好開發環境。

- **環境需求**：  
  - 安裝 [Node.js](https://nodejs.org/)（建議使用 LTS 版本）及 npm（隨 Node.js 附帶）。  
  - 推薦使用 [Visual Studio Code](https://code.visualstudio.com/) 等程式編輯器，並安裝 Angular 擴充套件以提升開發體驗。

- **安裝 Angular CLI**：  
  Angular 命令行介面（CLI）能簡化專案建立與管理流程。透過以下指令全域安裝：
  ```bash
  npm install -g @angular/cli
  ```

- **建立新專案**：  
  使用以下指令生成新的 Angular 應用程式：
  ```bash
  ng new my-angular-app
  ```
  設定過程中會詢問：  
  - 是否啟用路由功能（建議 SPA 專案開啟）。  
  - 選擇樣式表格式（如 CSS 或 SCSS）。

- **啟動應用程式**：  
  執行開發伺服器：
  ```bash
  ng serve
  ```
  在瀏覽器開啟 `http://localhost:4200/` 即可預覽應用程式。

---

## 步驟二：核心概念
Angular 應用程式建構於幾個基礎概念之上。

### 元件 (Components)
元件是使用者介面的基礎區塊，每個元件包含獨立的 HTML、CSS 與 TypeScript 邏輯。  
- 範例 (`app.component.ts`)：
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

### 模組 (Modules)
模組將應用程式組織為結構化區塊，根模組為 `AppModule`。  
- 範例 (`app.module.ts`)：
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

### 服務 (Services)
服務用於處理共享邏輯或資料存取，透過依賴注入提供給元件使用。  
- 生成服務：
  ```bash
  ng generate service data
  ```

### 資料繫結 (Data Binding)
資料繫結將元件資料與使用者介面連接，Angular 支援以下方式：
- **插值運算式**：`{{ value }}`  
- **屬性繫結**：`[property]="value"`  
- **事件繫結**：`(event)="handler()"`  
- **雙向繫結**：`[(ngModel)]="value"`（需導入 `FormsModule`）。

---

## 步驟三：路由設定
Angular 路由機制讓 SPA 能實現無需重新載入頁面的導航功能。

- **設定流程**：  
  建立專案時啟用路由功能（`ng new my-angular-app --routing`），系統將自動生成 `app-routing.module.ts`。

- **定義路由規則**：  
  在 `app-routing.module.ts` 中設定路由：
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

- **路由出口**：  
  在 `app.component.html` 中加入 `<router-outlet></router-outlet>` 以顯示路由元件。

- **導航連結**：  
  使用 `routerLink` 建立連結：
  ```html
  <a routerLink="/">首頁</a>
  <a routerLink="/about">關於我們</a>
  ```

---

## 步驟四：表單處理
表單用於處理使用者輸入，Angular 提供兩種實作方式。

### 模板驅動表單 (Template-Driven Forms)
適合簡單表單，使用 `ngModel` 實現雙向繫結，需導入 `FormsModule`。

### 響應式表單 (Reactive Forms)（推薦）
提供更精準的控制，適合複雜表單情境。  
- 範例 (`my.component.ts`)：
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
- 模板範例 (`my.component.html`)：
  ```html
  <form [formGroup]="form">
    <input formControlName="name" placeholder="姓名">
    <input formControlName="email" placeholder="電子郵件">
  </form>
  ```

---

## 步驟五：HTTP 請求
透過 Angular 的 `HttpClient` 與後端伺服器進行資料交換。

- **環境設定**：  
  在 `app.module.ts` 中導入 `HttpClientModule`：
  ```typescript
  import { HttpClientModule } from '@angular/common/http';

  @NgModule({
    imports: [HttpClientModule, ...]
  })
  export class AppModule {}
  ```

- **發送請求**：  
  建立服務 (`data.service.ts`)：
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

- **在元件中使用**：  
  訂閱可觀察物件：
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

## 步驟六：最佳實踐
- **善用 TypeScript**：透過型別與介面提升程式碼安全性與整潔度。  
- **保持元件精簡**：將大型元件拆分為可複用的小型元件。  
- **模組延遲載入**：在路由中使用 `loadChildren` 提升效能。  
- **活用 Angular CLI**：使用自動化指令（例如 `ng generate component my-component`）。  
- **啟用 AOT 編譯**：使用 `ng build --aot` 啟動預先編譯優化。  
- **遵循風格指南**：參考 [官方 Angular 風格指南](https://angular.io/guide/styleguide)。

---

## 延伸學習資源
- [官方 Angular 文件](https://angular.io/docs)  
- [Angular University](https://angular-university.io/)  
- [Stack Overflow](https://stackoverflow.com/questions/tagged/angular) 社群討論區  

---

本指南為您奠定 Angular 前端開發的紮實基礎。隨著技能成長，可進一步探索進階主題，例如狀態管理（如 NgRx）、單元測試與效能優化。祝您編碼愉快！