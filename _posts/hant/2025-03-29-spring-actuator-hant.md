---
audio: false
generated: true
lang: hant
layout: post
title: 彈簧制動器
translated: true
type: note
---

Spring Actuator 是 Spring Boot 中一項強大的功能，提供生產環境就緒的監控與管理工具。以下是使用指南：

### 1. **添加 Spring Actuator 依賴**
要使用 Spring Actuator，需在專案中加入其依賴。若使用 Maven，請在 `pom.xml` 中添加：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

若使用 Gradle，請在 `build.gradle` 中添加：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

### 2. **啟動 Spring Boot 應用程式**
添加依賴後，啟動您的 Spring Boot 應用程式。Spring Actuator 會自動啟用一組端點，供您監控和與應用程式互動。

### 3. **存取預設端點**
Spring Actuator 預設透過 HTTP 暴露多個端點，基礎路徑為 `/actuator`。以下是一些常用端點（假設應用程式運行於 `localhost:8080`）：
- **健康檢查**：`http://localhost:8080/actuator/health`
  - 返回應用程式狀態（例如 `{"status":"UP"}`）
- **應用程式資訊**：`http://localhost:8080/actuator/info`
  - 顯示可設定的應用程式資訊
- **指標數據**：`http://localhost:8080/actuator/metrics`
  - 提供詳細指標，如記憶體使用量、CPU 等

基於安全考量，預設僅啟用 `/health` 和 `/info` 端點。要暴露更多端點，需進行配置。

### 4. **配置 Actuator 端點**
您可以在 `application.properties` 或 `application.yml` 檔案中自訂要暴露的端點。例如：

#### `application.properties`
```properties
# 啟用特定端點
management.endpoints.web.exposure.include=health,info,metrics,beans

# 變更基礎路徑（可選）
management.endpoints.web.base-path=/manage
```

#### `application.yml`
```yaml
management:
  endpoints:
    web:
      exposure:
        include: health, info, metrics, beans
      base-path: /manage
```

透過此配置，將可存取如 `/manage/metrics` 或 `/manage/beans` 等端點。

### 5. **探索可用端點**
以下是一些可啟用的實用 Actuator 端點：
- `/actuator/beans`：列出應用程式中所有 Spring bean
- `/actuator/env`：顯示環境屬性
- `/actuator/loggers`：顯示並修改紀錄器級別
- `/actuator/shutdown`：優雅關閉應用程式（預設禁用）

要啟用所有端點進行測試，請使用：
```properties
management.endpoints.web.exposure.include=*
```

### 6. **保護 Actuator 端點**
由於 Actuator 可能暴露敏感資料，在生產環境中應進行安全防護：
- 添加 Spring Security：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
- 在 `application.properties` 中配置安全性：
```properties
spring.security.user.name=admin
spring.security.user.password=secret
management.endpoints.web.exposure.include=health,metrics
```
現在存取端點需要進行身份驗證（例如使用 `admin:secret`）。

### 7. **添加自訂健康檢查（可選）**
您可以透過實作 `HealthIndicator` 介面建立自訂健康指標。範例：

```java
import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;

@Component
public class CustomHealthCheck implements HealthIndicator {
    @Override
    public Health health() {
        boolean isHealthy = checkSomeCondition();
        if (isHealthy) {
            return Health.up().withDetail("customCheck", "運作正常！").build();
        }
        return Health.down().withDetail("customCheck", "出現異常").build();
    }

    private boolean checkSomeCondition() {
        // 在此加入自訂邏輯
        return true;
    }
}
```

此檢查結果將顯示於 `/actuator/health` 端點。

### 8. **監控指標數據**
要深入分析指標，請啟用 `/metrics` 並探索特定指標如：
- `http://localhost:8080/actuator/metrics/jvm.memory.used`
- `http://localhost:8080/actuator/metrics/http.server.requests`

可整合 Prometheus 或 Grafana 等工具進行進階監控。

### 9. **實際測試**
運行應用程式後，透過瀏覽器、`curl` 或 Postman 等工具呼叫端點。例如：
```bash
curl http://localhost:8080/actuator/health
```

### 實用技巧
- 使用 `/actuator/info` 暴露自訂資訊（例如應用程式版本），可添加：
```properties
info.app.name=MyApp
info.app.version=1.0.0
```
- 變更配置後請重啟應用程式

以上是基礎操作！如需特定使用情境或故障排除的協助，歡迎隨時詢問。