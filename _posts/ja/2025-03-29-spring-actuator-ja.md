---
audio: false
generated: true
lang: ja
layout: post
title: スプリングアクチュエータ
translated: true
type: note
---

Spring ActuatorはSpring Bootの強力な機能で、アプリケーションの監視と管理のためのプロダクションレディなツールを提供します。使用方法をステップバイステップで説明します：

### 1. **Spring Actuatorの依存関係を追加**
Spring Actuatorを使用するには、プロジェクトに依存関係を含める必要があります。Mavenを使用している場合は、`pom.xml`に以下を追加します：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

Gradleの場合は、`build.gradle`に以下を追加します：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

### 2. **Spring Bootアプリケーションを起動**
依存関係を追加したら、Spring Bootアプリケーションを起動します。Spring Actuatorは自動的に一連のエンドポイントを有効にし、アプリの監視と操作に使用できるようになります。

### 3. **デフォルトエンドポイントにアクセス**
Spring ActuatorはデフォルトでいくつかのエンドポイントをHTTP経由で公開します。ベースパスは`/actuator`です。よく使われるエンドポイントの例（アプリが`localhost:8080`で実行されている場合）：
- **ヘルスチェック**: `http://localhost:8080/actuator/health`
  - アプリケーションのステータスを返します（例：`{"status":"UP"}`）。
- **アプリケーション情報**: `http://localhost:8080/actuator/info`
  - 任意のアプリケーション情報を表示します（設定可能）。
- **メトリクス**: `http://localhost:8080/actuator/metrics`
  - メモリ使用量、CPUなど詳細なメトリクスを提供します。

セキュリティ上の理由から、デフォルトでは`/health`と`/info`のみが有効です。より多くのエンドポイントを公開するには、設定が必要です。

### 4. **Actuatorエンドポイントを設定**
`application.properties`または`application.yml`ファイルで、どのエンドポイントを公開するかをカスタマイズできます。例：

#### `application.properties`
```properties
# 特定のエンドポイントを有効化
management.endpoints.web.exposure.include=health,info,metrics,beans

# ベースパスを変更（オプション）
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

この設定により、`/manage/metrics`や`/manage/beans`などのエンドポイントが利用可能になります。

### 5. **利用可能なエンドポイントを探索**
有効化できる便利なActuatorエンドポイントの例：
- `/actuator/beans`: アプリケーション内のすべてのSpring beanを一覧表示します。
- `/actuator/env`: 環境プロパティを表示します。
- `/actuator/loggers`: ロガーレベルを表示および変更します。
- `/actuator/shutdown`: アプリケーションを正常にシャットダウンします（デフォルトでは無効）。

テスト用にすべてのエンドポイントを有効にするには：
```properties
management.endpoints.web.exposure.include=*
```

### 6. **Actuatorエンドポイントを保護**
Actuatorは機密データを公開するため、本番環境では保護する必要があります：
- Spring Securityを追加：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
- `application.properties`でセキュリティを設定：
```properties
spring.security.user.name=admin
spring.security.user.password=secret
management.endpoints.web.exposure.include=health,metrics
```
これで、エンドポイントにアクセスするには認証（例：`admin:secret`）が必要になります。

### 7. **カスタムヘルスチェックを追加（オプション）**
`HealthIndicator`インターフェースを実装してカスタムヘルスインジケーターを作成できます。例：

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
            return Health.up().withDetail("customCheck", "All good!").build();
        }
        return Health.down().withDetail("customCheck", "Something's wrong").build();
    }

    private boolean checkSomeCondition() {
        // ここにロジックを記述
        return true;
    }
}
```

これは`/actuator/health`エンドポイントに表示されます。

### 8. **メトリクスを監視**
メトリクスを詳細に調査するには、`/metrics`を有効にして以下のような特定のメトリクスを探索します：
- `http://localhost:8080/actuator/metrics/jvm.memory.used`
- `http://localhost:8080/actuator/metrics/http.server.requests`

高度な監視にはPrometheusやGrafanaなどのツールと統合できます。

### 9. **テスト**
アプリを実行し、ブラウザ、`curl`、またはPostmanなどのツールを使用してエンドポイントにアクセスします。例：
```bash
curl http://localhost:8080/actuator/health
```

### ヒント
- `/actuator/info`を使用してカスタム情報（例：アプリバージョン）を公開するには、以下を追加：
```properties
info.app.name=MyApp
info.app.version=1.0.0
```
- 設定変更後はアプリを再起動してください。

以上が基本です！特定のユースケースやトラブルシューティングについてサポートが必要な場合はお知らせください。