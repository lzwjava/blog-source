---
audio: false
generated: true
lang: hant
layout: post
title: 從執行環境的命名空間中擷取金鑰
translated: true
type: note
---

要使用執行上下文從命名空間中獲取鍵值，具體方法取決於您使用的框架或系統，因為「執行上下文」和「命名空間」的含義會隨上下文而變化。由於您未指定具體框架，我將提供通用指南供您調整適應，同時假設一個常見場景（如基於Java的Spring應用程式）給出具體範例。若與您的設定不符，請進一步說明！

### 從執行上下文的命名空間中獲取鍵值的通用步驟

執行上下文通常指承載當前執行流程相關資料的物件或結構（例如執行緒、請求或事務）。其中的命名空間則是組織資料的方式，常以命名作用域或鍵值對集合的形式存在。以下是操作方式：

1. **存取當前執行上下文**
   - 確定在應用程式中獲取執行上下文的方法，可能途徑包括：
     - 靜態方法（如 `Context.getCurrent()`）
     - 執行緒區域變數（如 `ThreadLocal<Context>`）
     - 若框架（如 Spring）管理上下文，則透過依賴注入
   - 確保上下文在當前執行作用域中可用

2. **導航至命名空間**
   - 取得上下文後，識別命名空間的呈現方式。命名空間可能為：
     - 特定方法呼叫（如 `context.getNamespace("myNamespace")`）
     - 上下文中的嵌套映射或結構（如 `context.get("myNamespace")` 返回 `Map`）
     - 若未明確區分命名空間，則為直接作用域
   - 查閱上下文 API 以理解其結構

3. **獲取鍵對應值**
   - 從命名空間使用 `get("myKey")` 之類的方法取得鍵對應值
   - 處理上下文或命名空間不可用的情況（如空值檢查）

### 範例：在純 Java 中使用自訂執行上下文

假設您在 Java 應用程式中使用自訂的 `ExecutionContext` 類別，且上下文可透過靜態方式存取並包含作為鍵值對集合的命名空間。實作方式如下：

```java
// 假設的 ExecutionContext 類別
public class ExecutionContext {
    private Map<String, Map<String, Object>> namespaces = new HashMap<>();

    // 獲取當前上下文的靜態方法（實際可能基於 ThreadLocal）
    private static ExecutionContext current = new ExecutionContext();
    public static ExecutionContext getCurrent() {
        return current;
    }

    // 獲取命名空間的方法
    public Map<String, Object> getNamespace(String namespaceName) {
        return namespaces.getOrDefault(namespaceName, new HashMap<>());
    }

    // 用於設定目的（不屬於獲取流程）
    public void setValue(String namespaceName, String key, Object value) {
        namespaces.computeIfAbsent(namespaceName, k -> new HashMap<>()).put(key, value);
    }
}

// 使用範例
public class MyClass {
    public void retrieveKeyFromNamespace() {
        // 步驟 1：存取當前執行上下文
        ExecutionContext context = ExecutionContext.getCurrent();

        if (context != null) {
            // 步驟 2：取得命名空間
            Map<String, Object> ns = context.getNamespace("myNamespace");

            // 步驟 3：獲取鍵對應值
            Object value = ns.get("myKey");

            if (value != null) {
                System.out.println("數值: " + value);
            } else {
                System.out.println("在命名空間 'myNamespace' 中找不到鍵 'myKey'");
            }
        } else {
            System.out.println("執行上下文不可用");
        }
    }

    public static void main(String[] args) {
        // 示範設定
        ExecutionContext.getCurrent().setValue("myNamespace", "myKey", "Hello, World!");
        
        new MyClass().retrieveKeyFromNamespace();
    }
}
```

**輸出：**
```
數值: Hello, World!
```

#### 說明：
- **步驟 1：** `ExecutionContext.getCurrent()` 提供當前上下文。實際應用中可能使用 `ThreadLocal` 確保執行緒專屬上下文
- **步驟 2：** `getNamespace("myNamespace")` 獲取代表命名空間的 `Map`
- **步驟 3：** `ns.get("myKey")` 取得 `"myKey"` 對應值

### 替代範例：Spring Web 應用程式

若在 Spring Web 應用程式中，「執行上下文」可能指請求或會話作用域，「命名空間」則可能是儲存在這些作用域中的屬性。存取方式如下：

```java
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import javax.servlet.http.HttpServletRequest;

public class MyClass {
    public Object getKeyFromRequestScope(String key) {
        // 步驟 1：存取當前執行上下文（請求屬性）
        ServletRequestAttributes attributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        
        if (attributes != null) {
            HttpServletRequest request = attributes.getRequest();
            
            // 步驟 2：命名空間即請求作用域本身
            // 步驟 3：獲取鍵值
            return request.getAttribute(key);
        }
        return null; // 上下文不可用
    }
}
```

- **命名空間：** 此處請求作用域即作為命名空間
- **鍵值獲取：** `request.getAttribute(key)` 取得數值

若為會話作用域，將 `request.getAttribute(key)` 替換為 `request.getSession().getAttribute(key)`

### 關鍵注意事項
- **框架專屬 API：** 存取上下文和命名空間的具體方法取決於框架。例如：
  - Spring 中可使用 `ApplicationContext`、`RequestContextHolder` 或 `Environment` 應對不同上下文
  - 自訂系統請參考其文件
- **空值處理：** 務必檢查空值避免執行階段錯誤
- **執行緒安全：** 若上下文跨執行緒共享，需確保正確同步或使用執行緒區域儲存

若您使用特定框架，或對「執行上下文」與「命名空間」有不同定義，請提供更多細節以便進一步調整解答！目前這些通用方法應能協助您從執行上下文的命名空間中獲取鍵值。