---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 端到端追蹤至大型語言模型代理管道
translated: true
type: note
---

你的方向很正確：AOP（AspectJ）、servlet filters 和 Log4j2 各自在不同層面發揮作用。以下是一個緊湊的端到端整合方案——先用來**收集執行追蹤和 HTTP 輸入輸出**（以便自動生成 Python 測試），再將豐富的上下文資訊提供給 Spring 中的 LLM「代理」端點。

---

## 1) 捕捉所需資料（AOP + Filter + Log4j2）

**a) 使用 AOP 進行方法攔截（計時、參數、返回/異常）。**

使用 `@Around` 通知封裝服務方法；將 `traceId` 存入 MDC，使所有層級的日誌能關聯起來。

```java
@Aspect
@Component
public class TraceAspect {
  @Around("execution(* com.example.service..*(..))")
  public Object around(ProceedingJoinPoint pjp) throws Throwable {
    String traceId = java.util.UUID.randomUUID().toString();
    org.apache.logging.log4j.ThreadContext.put("traceId", traceId);
    long t0 = System.nanoTime();
    try {
      Object out = pjp.proceed();
      org.apache.logging.log4j.LogManager.getLogger(pjp.getTarget().getClass())
        .info("AOP", "method={},args={},ret={},ms={},traceId={}",
              pjp.getSignature().toShortString(),
              java.util.Arrays.toString(pjp.getArgs()), out,
              (System.nanoTime()-t0)/1_000_000.0, traceId);
      return out;
    } catch (Throwable e) {
      org.apache.logging.log4j.LogManager.getLogger(pjp.getTarget().getClass())
        .error("AOP_ERR", "method={},args={},err={},traceId={}",
               pjp.getSignature().toShortString(),
               java.util.Arrays.toString(pjp.getArgs()),
               e.toString(), traceId);
      throw e;
    } finally {
      org.apache.logging.log4j.ThreadContext.remove("traceId");
    }
  }
}
```

（當你需要前後邏輯並控制呼叫時，「Around advice」是合適的工具。（[首頁][1]、[DigitalOcean][2]））

**b) 使用 Filter 記錄 HTTP（請求/回應主體 + 狀態）。**

每次呼叫時封裝請求/回應一次；附上相同的 `traceId`（從標頭取得或生成）。Spring 的 `OncePerRequestFilter` 模式是標準做法。優質指南展示如何安全緩衝主體並避免重複消耗。（[Baeldung 關於 Kotlin][3]、[SigNoz][4]）

**c) 使用 Log4j2 RoutingAppender 按用戶/租戶/測試路由日誌。**

這讓你可以將匹配的日誌（例如通過 MDC 中的 `traceId` 或 `tenantId`）發送到**單獨的檔案**，之後再轉換為測試。

```xml
<Appenders>
  <Routing name="ByTrace">
    <Routes pattern="${ctx:traceId}">
      <Route ref="RollingTemplate" key="${ctx:traceId}"/>
    </Routes>
  </Routing>

  <RollingFile name="RollingTemplate"
               fileName="logs/${ctx:traceId}.log"
               filePattern="logs/${ctx:traceId}-%d{yyyy-MM-dd}.gz">
    <PatternLayout pattern="%d %p %c %X{traceId} - %m%n"/>
    <Policies><TimeBasedTriggeringPolicy/></Policies>
  </RollingFile>
</Appenders>
<Loggers>
  <Root level="info">
    <AppenderRef ref="ByTrace"/>
  </Root>
</Loggers>
```

（Log4j2 的 RoutingAppender + MDC 模式是按鍵分割日誌的標準方法。（[Apache Logging][5]、[Roy Tutorials][6]、[Stack Overflow][7]））

---

## 2) 將日誌轉換為 **Python 測試**（pytest + requests）

當日誌變成 JSON 格式或可解析的行時，一個小型生成器即可輸出確定性測試：

```python
# gen_tests_from_logs.py
import json, re, pathlib

def extract_calls(log_text):
    calls = []
    for line in log_text.splitlines():
        if '"HTTP_IN"' in line or 'HTTP_IN' in line:
            d = json.loads(re.search(r'({.*})', line).group(1))
            calls.append({
              "method": d["method"],
              "url": d["path"],
              "headers": d.get("headers", {}),
              "body": d.get("body", None),
              "expect_status": d.get("status", 200)
            })
    return calls

def emit_pytest(calls):
    lines = [
      "import requests",
      "import pytest",
      "",
      "@pytest.mark.parametrize('call', ["
    ]
    for c in calls:
      lines.append(f"  {json.dumps(c)},")
    lines += ["])",
      "def test_replay(call):",
      "    resp = requests.request(call['method'], 'http://localhost:8080'+call['url'],",
      "                             headers=call.get('headers'),",
      "                             json=call.get('body'))",
      "    assert resp.status_code == call['expect_status']",
      "    # 可選地對回應 JSON 中的結構化字段進行斷言",
    ]
    return "\n".join(lines)

def main():
    all_calls = []
    for p in pathlib.Path('logs').glob('*.log'):
      all_calls += extract_calls(p.read_text(encoding='utf-8'))
    pathlib.Path('tests/test_replay_generated.py').write_text(emit_pytest(all_calls), encoding='utf-8')

if __name__ == "__main__":
    main()
```

提示：

* 對於請求/回應，**優先使用 JSON 日誌**；這使測試生成變得簡單。
* 避免記錄敏感標頭（例如 Authorization）。
* 如果主體很大，在日誌中儲存哈希值並斷言哈希相等性，而非完整字串。

---

## 3) 使用 Spring 為 LLM「代理」**提供上下文**

如果你目前使用 Spring Boot，最短路徑是 **Spring AI**：

**a) 設定 `ChatClient` 和提示模板。**
Spring AI 提供 `ChatClient`/`PromptTemplate` 抽象和工具呼叫功能，使模型能要求你的應用獲取數據。（[首頁][8]、[首頁][9]）

```java
@Configuration
public class AiConfig {
  @Bean ChatClient chatClient(org.springframework.ai.chat.ChatModel model) {
    return ChatClient.builder(model).defaultSystem("You are a helpful banking agent.").build();
  }
}
```

**b) 透過 Spring beans（服務）和「工具」提供上下文。**
將領域查詢公開為**工具**，以便模型在聊天回合中呼叫它們。（Spring AI 支援工具呼叫——模型決定何時呼叫；結果作為額外上下文流回。）（[首頁][9]）

```java
@Component
public class AccountTools {
  @org.springframework.ai.tool.annotation.Tool
  public String fetchBalance(String userId){
    // 查詢數據庫或下游服務
    return "{\"balance\": 1234.56, \"currency\": \"HKD\"}";
  }
}
```

**c) 為文件/代碼添加檢索（RAG）。**
連接 `VectorStore`（PGVector 等）並將你的知識嵌入填充其中。在運行時，檢索前 k 個塊並將其附加到提示中。目前有一個實用的教程，使用 Spring Boot + PGVector 構建完整的 RAG 堆疊。（[sohamkamani.com][10]）

**d) 透過攔截器傳遞用戶/會話上下文。**
使用 `HandlerInterceptor`（或你的 Filter）來解析 `userId`、`tenantId`、角色、語言環境、最近 N 個操作——將它們放入：

* 請求屬性、
* 一個作用域 bean，或
* 你的提示的**系統**和**用戶**部分。

**e) 一個統一的 HTTP 端點。**

```java
@RestController
@RequestMapping("/agent")
public class AgentController {
  private final ChatClient chat;
  private final UserContextProvider ctx;
  private final Retriever retriever;

  public AgentController(ChatClient chat, UserContextProvider ctx, Retriever retriever) {
    this.chat = chat; this.ctx = ctx; this.retriever = retriever;
  }

  @PostMapping
  public String chat(@RequestBody Map<String,Object> req, Principal principal) {
    var userCtx = ctx.fromPrincipal(principal);          // 身份、角色、偏好
    var docs   = retriever.findRelevant((String)req.get("message")); // RAG
    return chat.prompt()
      .system("Use tools if needed. Respect tenant="+userCtx.tenant()+" and role="+userCtx.role()+".")
      .user("Context:\n"+docs+"\n\nUser says: "+req.get("message"))
      .call().content();                                  // 工具呼叫隱含發生
  }
}
```

**f) 可選：使用 Spring Cloud Function 部署「技能」。**
如果你希望每個代理技能作為單一函數（非常適合無伺服器架構和按標頭路由），**Spring Cloud Function** 讓你編寫純 `Function<T,R>` 並動態路由——便於接入 AWS Lambda/Azure 以及內部「代理工具」端點。（[cloud.spring.io][11]、[首頁][12]、[Baeldung 關於 Kotlin][13]）

---

## 4) 整體流程整合

1. **Filter** 添加 `traceId`，記錄 HTTP 輸入輸出。
2. **AOP** 封裝服務方法並發出結構化事件。
3. **Log4j2 RoutingAppender** 寫入每個追蹤的檔案。
4. **Python 生成器** 讀取這些檔案 → 發出重放真實呼叫的 **pytest**。
5. **Spring AI** 端點使用：

   * 來自攔截器/Filter 的請求/租戶/用戶上下文、
   * 用於實時數據的領域「工具」、
   * 用於文件/代碼上下文的向量儲存（RAG）、
   * 用於聊天編排的 `ChatClient`。

這為你提供了可重現的測試和一個穩健的、具上下文感知的代理介面——兩者都由相同的遙測數據驅動。

如果你需要，我可以繪製一個包含 Spring Boot 組件、Log4j2 配置和 Python 生成器腳本的最小倉庫結構，並將其連接到 `make testgen && pytest` 工作流程中。

[1]: https://docs.spring.io/spring-framework/reference/core/aop/ataspectj/advice.html?utm_source=chatgpt.com "Declaring Advice :: Spring Framework"
[2]: https://www.digitalocean.com/community/tutorials/spring-aop-example-tutorial-aspect-advice-pointcut-joinpoint-annotations?utm_source=chatgpt.com "Spring AOP Example Tutorial - Aspect, Advice, Pointcut, ..."
[3]: https://www.baeldung.com/spring-http-logging?utm_source=chatgpt.com "Log Incoming Requests - Spring"
[4]: https://signoz.io/guides/spring-boot-how-to-log-all-requests-and-responses-with-exceptions-in-single-place/?utm_source=chatgpt.com "How to Log All Spring Boot Requests and Responses"
[5]: https://logging.apache.org/log4j/2.12.x/manual/configuration.html?utm_source=chatgpt.com "Configuring Log4j 2 - Apache Logging Services"
[6]: https://roytuts.com/how-to-create-separate-log-file-for-each-module-using-routingappender-and-mdc-mapped-diagnostic-context-in-log4j2-slf4j/?utm_source=chatgpt.com "How to create separate log file for each module using ..."
[7]: https://stackoverflow.com/questions/18279656/wildcard-pattern-for-routingappender-of-log4j2?utm_source=chatgpt.com "Wildcard pattern for RoutingAppender of Log4j2 - java"
[8]: https://spring.io/projects/spring-ai?utm_source=chatgpt.com "Spring AI"
[9]: https://docs.spring.io/spring-ai/reference/api/tools.html?utm_source=chatgpt.com "Tool Calling :: Spring AI Reference"
[10]: https://sohamkamani.com/java/spring-ai-rag-application?utm_source=chatgpt.com "Build a RAG-Powered Chat App with Spring AI and PGVector"
[11]: https://cloud.spring.io/spring-cloud-function/reference/html/spring-cloud-function.html?utm_source=chatgpt.com "Spring Cloud Function"
[12]: https://docs.spring.io/spring-cloud-function/docs/current/reference/html/spring-cloud-function.html?utm_source=chatgpt.com "Spring Cloud Function"
[13]: https://www.baeldung.com/spring-cloud-function-microsoft-azure?utm_source=chatgpt.com "Spring Cloud Function for Azure Function"