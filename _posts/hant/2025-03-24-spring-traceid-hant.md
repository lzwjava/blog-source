---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot Log4j 請求追蹤
translated: true
type: note
---

在使用 Log4j 但未內建追蹤 ID 設計的 Java Spring Boot 應用程式中，要將特定日誌條目追溯至前端發起的請求確實具有挑戰性。您說得對，Log4j 中的 `%t`（執行緒名稱）有助於識別與特定執行緒關聯的日誌，但正如您所指出的，當請求跨越多個執行緒時（例如由於非同步處理、執行緒池或下游呼叫），這種方式就變得不可靠。使用時間範圍搜尋日誌是一種變通方法，但這種方式不精確且繁瑣，尤其在流量高的系統中。讓我們探討一些實用建議來改善這種情況，而無需徹底重構現有設定。

### 快速實用建議
1. **利用 Log4j 的 MDC（映射診斷上下文）**
   - Log4j 支援 MDC，可讓您在執行緒內（若稍加處理甚至能跨執行緒傳播）將上下文鍵值對附加到日誌中。
   - 當前端請求觸達 Spring Boot 應用程式時生成唯一請求 ID（例如 UUID），並將其儲存在 MDC 中。然後在日誌模式中包含此 ID。
   - **實作方式：**
     - 在 Spring Boot 過濾器或攔截器（例如 `OncePerRequestFilter`）中生成 ID：
       ```java
       import org.slf4j.MDC;
       import javax.servlet.FilterChain;
       import javax.servlet.http.HttpServletRequest;
       import javax.servlet.http.HttpServletResponse;
       import java.util.UUID;

       public class RequestTracingFilter extends OncePerRequestFilter {
           @Override
           protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) {
               try {
                   String traceId = UUID.randomUUID().toString();
                   MDC.put("traceId", traceId);
                   filterChain.doFilter(request, response);
               } finally {
                   MDC.clear(); // 請求完成後清理
               }
           }
       }
       ```
     - 在 Spring Boot 配置中註冊過濾器：
       ```java
       @Bean
       public FilterRegistrationBean<RequestTracingFilter> tracingFilter() {
           FilterRegistrationBean<RequestTracingFilter> registrationBean = new FilterRegistrationBean<>();
           registrationBean.setFilter(new RequestTracingFilter());
           registrationBean.addUrlPatterns("/*");
           return registrationBean;
       }
       ```
     - 在 `log4j.properties` 或 `log4j.xml` 中更新 Log4j 模式以包含 `traceId`：
       ```properties
       log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1} - %m [traceId=%X{traceId}]%n
       ```
     - 現在，與該請求相關的每個日誌行都將包含 `traceId`，便於追溯至前端按鈕點擊。

2. **跨執行緒傳播追蹤 ID**
   - 若應用程式使用執行緒池或非同步呼叫（例如 `@Async`），MDC 上下文可能不會自動傳播。處理方式：
     - 使用自定義執行器包裝非同步任務以複製 MDC 上下文：
       ```java
       import java.util.concurrent.Executor;
       import org.springframework.context.annotation.Bean;
       import org.springframework.context.annotation.Configuration;
       import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

       @Configuration
       public class AsyncConfig {
           @Bean(name = "taskExecutor")
           public Executor taskExecutor() {
               ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
               executor.setCorePoolSize(10);
               executor.setMaxPoolSize(20);
               executor.setQueueCapacity(100);
               executor.setTaskDecorator(task -> {
                   Map<String, String> context = MDC.getCopyOfContextMap();
                   return () -> {
                       try {
                           if (context != null) MDC.setContextMap(context);
                           task.run();
                       } finally {
                           MDC.clear();
                       }
                   };
               });
               executor.initialize();
               return executor;
           }
       }
       ```
     - 這可確保 `traceId` 即使跨越執行緒邊界也能持續跟隨請求。

3. **加入前端關聯**
   - 若可行，讓前端在點擊按鈕時發送帶有唯一 ID 的自定義標頭（例如 `X-Request-ID`）。後端可直接使用此 ID 而非自行生成 UUID。這樣能直接將日誌與前端操作關聯，無需額外推測。

4. **備選方案：透過上下文資料增強日誌記錄**
   - 若目前覺得 MDC 開銷過大，可在關鍵點用更多上下文豐富日誌（例如使用者 ID、工作階段 ID 或端點名稱）。例如：
     ```java
     logger.info("Button clicked, endpoint=/api/example, user={}", userId);
     ```
   - 結合 `%t`（執行緒名稱）與緊湊的時間範圍來手動縮小日誌範圍。雖非理想方案，但可臨時應急。

### 為何不單靠時間範圍？
僅依賴時間戳記十分脆弱，因為：
- 併發請求的日誌會相互重疊，特別在繁忙系統中。
- 時間精度（例如毫秒）可能不足以隔離單一請求。
- 跨服務或深層呼叫堆疊的日誌關聯十分繁瑣。

### 長期建議
若追蹤需求增長，可考慮採用 Spring Boot 內建的分散式追蹤支援（例如透過 Sleuth 或 Micrometer 搭配 Zipkin）。Sleuth 會自動生成追蹤與跨度 ID，並與 Log4j 無縫整合，但設定較為複雜。目前而言，MDC 是輕量且有效的折衷方案。

### 最終建議
先從 MDC 方案著手——它簡單易用，能充分發揮 Log4j 原生功能，並提供清晰方式將日誌與前端發起的請求關聯。您會在該請求的所有日誌行中看到類似 `[traceId=123e4567-e89b-12d3-a456-426614174000]` 的標記，讓搜尋與追蹤變得輕而易舉。若需進一步調整協助，請隨時告知！