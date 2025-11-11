---
audio: false
generated: true
image: false
lang: de
layout: post
title: End-to-End-Trace-zu-LLM-Agent-Pipeline
translated: true
type: note
---

Du bist auf einem guten Weg: AOP (AspectJ), Servlet-Filter und Log4j2 haben jeweils ihre Stärken auf verschiedenen Ebenen. Hier ist ein kompakter, durchgängiger Ansatz, um sie gemeinsam zu nutzen – zunächst, um **Ausführungs-Traces und HTTP-I/O zu erfassen** (um damit automatisch Python-Tests zu generieren), und dann, um **reichen Kontext an einen LLM-"Agent"-Endpunkt in Spring** zu liefern.

---

## 1) Erfasse, was du brauchst (AOP + Filter + Log4j2)

**a) Methoden-Interception mit AOP (Laufzeiten, Argumente, Rückgaben/Exceptions).**

Verwende `@Around` Advice, um Service-Methoden zu wrappen; speichere eine `traceId` im MDC, damit Logs aus allen Schichten zusammengehören.

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

("Around Advice" ist das richtige Werkzeug, wenn du Pre/Post-Logik und Kontrolle über den Aufruf benötigst. ([Home][1], [DigitalOcean][2]))

**b) HTTP-Logging mit einem Filter (Request/Response-Body + Status).**

Wrappe den Request/Response einmal pro Aufruf; verwende dieselbe `traceId` (aus Header oder neu generiert). Das Pattern von Springs `OncePerRequestFilter` ist Standard. Gute Anleitungen zeigen, wie man den Body sicher puffert und Doppelkonsum vermeidet. ([Baeldung on Kotlin][3], [SigNoz][4])

**c) Leite Logs pro Benutzer/Tenant/Test mit Log4j2 RoutingAppender um.**

Dies ermöglicht es, passende Logs (z.B. nach `traceId` oder `tenantId` im MDC) in **separate Dateien** zu schreiben, die später in Tests umgewandelt werden.

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

(Log4j2's RoutingAppender + MDC Pattern ist der kanonische Weg, um Logs nach Schlüsseln aufzuteilen. ([Apache Logging][5], [Roy Tutorials][6], [Stack Overflow][7]))

---

## 2) Verwandle diese Logs in **Python-Tests** (pytest + requests)

Sobald die Logs JSON-ähnlich oder parsbare Zeilen sind, kann ein kleiner Generator deterministische Tests erzeugen:

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
      "    # optionally assert on structured fields from response JSON",
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

Tipps:

* Bevorzuge **JSON-Logs** für Requests/Responses; das macht die Testgenerierung trivial.
* Halte sensible Header draußen (z.B. Authorization).
* Wenn Bodies groß sind, speichere einen Hash in den Logs und prüfe auf Hash-Gleichheit anstelle des gesamten Strings.

---

## 3) Verwende Spring, um **Kontext** für LLM-"Agenten" bereitzustellen

Wenn du bereits auf Spring Boot setzt, ist der kürzeste Weg **Spring AI**:

**a) Richte einen `ChatClient` und Prompt-Templates ein.**
Spring AI bietet dir `ChatClient`/`PromptTemplate`-Abstraktionen und Tool-Calling, damit das Modell deine App zum Abrufen von Daten auffordern kann. ([Home][8], [Home][9])

```java
@Configuration
public class AiConfig {
  @Bean ChatClient chatClient(org.springframework.ai.chat.ChatModel model) {
    return ChatClient.builder(model).defaultSystem("You are a helpful banking agent.").build();
  }
}
```

**b) Stelle Kontext über Spring Beans (Services) und "Tools" bereit.**
Exponiere Domain-Lookups als **Tools**, damit das Modell sie während eines Chat-Turns aufrufen kann. (Spring AI unterstützt Tool Calling – das Modell entscheidet, wann es aufgerufen wird; das Ergebnis fließt als zusätzlicher Kontext zurück.) ([Home][9])

```java
@Component
public class AccountTools {
  @org.springframework.ai.tool.annotation.Tool
  public String fetchBalance(String userId){
    // query DB or downstream service
    return "{\"balance\": 1234.56, \"currency\": \"HKD\"}";
  }
}
```

**c) Füge Retrieval (RAG) für Dokumente/Code hinzu.**
Verbinde einen `VectorStore` (PGVector, etc.) und fülle ihn mit Embeddings deines Wissens. Zur Laufzeit hole die Top-k Chunks ab und füge sie dem Prompt hinzu. Es gibt ein aktuelles, praktisches Tutorial zum Aufbau eines vollständigen RAG-Stacks mit Spring Boot + PGVector. ([sohamkamani.com][10])

**d) Fädle Benutzer/Session-Kontext durch Interceptors.**
Verwende einen `HandlerInterceptor` (oder deinen Filter), um `userId`, `tenantId`, Rollen, Locale, die letzten N Aktionen aufzulösen – und packe sie in:

* Request-Attribute,
* eine Scoped Bean, oder
* die **System-** und **Benutzer-**Teile deines Prompts.

**e) Ein HTTP-Endpunkt, um sie alle zu beherrschen.**

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
    var userCtx = ctx.fromPrincipal(principal);          // ids, roles, preferences
    var docs   = retriever.findRelevant((String)req.get("message")); // RAG
    return chat.prompt()
      .system("Use tools if needed. Respect tenant="+userCtx.tenant()+" and role="+userCtx.role()+".")
      .user("Context:\n"+docs+"\n\nUser says: "+req.get("message"))
      .call().content();                                  // tool calls happen implicitly
  }
}
```

**f) Optional: Deploye "Skills" mit Spring Cloud Function.**
Wenn du jeden Agent-Skill als einzelne Funktion haben möchtest (ideal für Serverless und Routing per Header), ermöglicht dir **Spring Cloud Function**, reine `Function<T,R>` zu schreiben und dynamisch zu routen – gut für AWS Lambda/Azure und für interne "Agent Tool"-Endpunkte. ([cloud.spring.io][11], [Home][12], [Baeldung on Kotlin][13])

---

## 4) Alles zusammenfügen (Ablauf)

1.  **Filter** fügt `traceId` hinzu, loggt HTTP-I/O.
2.  **AOP** wrappt Service-Methoden und emittiert strukturierte Events.
3.  **Log4j2 RoutingAppender** schreibt pro-Trace-Dateien.
4.  **Python-Generator** liest diese Dateien → emittiert **pytest**, der echte Aufrufe replayt.
5.  **Spring AI** Endpunkt verwendet:

    * Request/Tenant/Benutzer-Kontext vom Interceptor/Filter,
    * Domain-"Tools" für Live-Daten,
    * Vector Store (RAG) für Dokument-/Code-Kontext,
    * `ChatClient` für Chat-Orchestrierung.

Das gibt dir reproduzierbare Tests und eine robuste, kontextuelle Agent-Schnittstelle – beide angetrieben von derselben Telemetrie.

Wenn du möchtest, kann ich eine minimale Repo-Struktur mit den Spring Boot-Teilen, einer Log4j2-Konfiguration und dem Python-Generator-Skript skizzieren, das in einen `make testgen && pytest` Workflow eingebunden ist.

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