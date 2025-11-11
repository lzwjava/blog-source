---
audio: false
generated: true
lang: hant
layout: post
title: Angular 錯誤
translated: true
type: note
---

使用 Angular 開發時，開發者經常會遇到特定的異常和錯誤。以下按類別列出常見問題、成因及解決方案：

---

### **模板與數據綁定錯誤**
1. **`ExpressionChangedAfterItHasBeenCheckedError`**  
   - **成因**：在 Angular 變更檢測週期後更改組件數據（例如在 `ngAfterViewInit` 或 `ngOnChanges` 中）。  
   - **解決**：使用 `ChangeDetectorRef.detectChanges()` 或確保數據變更在變更檢測完成前發生。

2. **`Cannot read property 'X' of undefined`**  
   - **成因**：在模板中訪問未初始化的物件屬性（例如當 `user` 為 `null` 時使用 `{{ user.name }}`）。  
   - **解決**：使用安全導航運算符（`{{ user?.name }}`）或正確初始化物件。

3. **`Can't bind to 'X' since it isn't a known property of 'Y'`**  
   - **成因**：缺少組件/指令聲明或屬性名稱拼寫錯誤。  
   - **解決**：將指令/組件導入模組或檢查拼寫錯誤。

---

### **依賴注入錯誤**
4. **`NullInjectorError: No provider for XService`**  
   - **成因**：服務未在模組/組件中提供或存在循環依賴。  
   - **解決**：將服務添加到模組/組件的 `providers` 陣列中。

5. **`No value accessor for form control`**  
   - **成因**：自訂表單控件缺少 `ControlValueAccessor` 實現或 `formControlName` 綁定錯誤。  
   - **解決**：為自訂控件實現 `ControlValueAccessor` 或檢查表單綁定。

---

### **TypeScript 與建置錯誤**
6. **`Type 'X' is not assignable to type 'Y'`**  
   - **成因**：類型不匹配（例如向組件傳遞錯誤的數據類型）。  
   - **解決**：確保類型一致或使用類型斷言（若為故意）。

7. **`ERROR in Cannot find module 'X'`**  
   - **成因**：缺少 npm 套件或導入路徑錯誤。  
   - **解決**：安裝套件（`npm install X`）或更正導入路徑。

---

### **組件與模組錯誤**
8. **`Component is not part of any NgModule`**  
   - **成因**：組件未在模組中聲明或模組未導入。  
   - **解決**：將組件添加到所屬模組的 `declarations` 中或導入模組。

9. **`ViewDestroyedError: Attempt to use a destroyed view`**  
   - **成因**：訂閱或異步操作在組件銷毀後繼續運行。  
   - **解決**：在 `ngOnDestroy` 中取消訂閱或使用 `async` 管道。

---

### **HTTP 與 API 錯誤**
10. **`HttpClient provider not found`**  
    - **成因**：模組中缺少 `HttpClientModule` 導入。  
    - **解決**：在 `AppModule` 中導入 `HttpClientModule`。

11. **CORS 問題**  
    - **成因**：後端未允許來自前端來源的請求。  
    - **解決**：在伺服器端配置 CORS 或在 Angular 中使用代理（`proxy.conf.json`）。

---

### **路由錯誤**
12. **`Route not found`**  
    - **成因**：路由定義錯誤或缺少懶加載模組。  
    - **解決**：檢查路由路徑及懶加載語法（`loadChildren: () => import(...)`）。

---

### **表單錯誤**
13. **`FormControl not found`**  
    - **成因**：使用 `formControlName` 時未以 `[formGroup]` 包裹。  
    - **解決**：確保父表單組已初始化並綁定。

---

### **其他錯誤**
14. **`Maximum call stack size exceeded`**  
    - **成因**：遞歸函數或循環依賴。  
    - **解決**：重構程式碼以消除遞歸/循環引用。

15. **`Zone.js Promise rejection`**  
    - **成因**：未處理的 Promise 拒絕。  
    - **解決**：添加 `.catch()` 或使用 `try/catch` 配合 `async/await`。

16. **AOT 編譯錯誤**  
    - **成因**：模板語法與預先編譯不兼容。  
    - **解決**：避免在模板中使用複雜表達式或改用 Angular 兼容語法。

---

### **避免錯誤的最佳實踐**
- 使用 `async` 管道處理 observables 以自動取消訂閱。
- 啟用嚴格 TypeScript 檢查（在 `tsconfig.json` 中設置 `strict: true`）。
- 運行 `ng lint` 以捕捉程式碼品質問題。
- 使用 `--prod` 標誌進行測試以模擬 AOT 建置。

通過有系統地處理這些常見問題，您可以簡化 Angular 開發流程並減少除錯時間。