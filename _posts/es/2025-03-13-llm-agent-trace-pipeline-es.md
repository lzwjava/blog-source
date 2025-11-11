---
audio: false
generated: true
image: false
lang: es
layout: post
title: Rastreo Integral al Agente de Modelo de Lenguaje
translated: true
type: note
---

Vas por buen camino: AOP (AspectJ), los filtros de servlets y Log4j2 brillan cada uno en diferentes capas. Aquí tienes una forma compacta e integral de usarlos juntos: primero para **capturar trazas de ejecución e E/S HTTP** (y así poder generar automáticamente tests de Python), y luego para **alimentar con contexto enriquecido a un endpoint "agente" LLM en Spring**.

---

## 1) Captura lo que necesitas (AOP + Filter + Log4j2)

**a) Intercepción de métodos con AOP (tiempos, argumentos, retornos/excepciones).**

Usa el consejo `@Around` para envolver métodos de servicio; almacena un `traceId` en MDC para que los logs de todas las capas se unan.

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

(El "consejo Around" es la herramienta correcta cuando necesitas lógica previa/posterior y control de la llamada. ([Home][1], [DigitalOcean][2]))

**b) Logging HTTP con un Filter (cuerpo de petición/respuesta + estado).**

Envuelve la petición/respuesta una vez por llamada; asocia el mismo `traceId` (desde la cabecera o generándolo). El patrón `OncePerRequestFilter` de Spring es estándar. Buenas guías muestran cómo almacenar en búfer el cuerpo de forma segura y evitar doble consumo. ([Baeldung on Kotlin][3], [SigNoz][4])

**c) Dirige los logs por usuario/tenant/test usando Log4j2 RoutingAppender.**

Esto te permite enviar logs coincidentes (ej., por `traceId` o `tenantId` en MDC) a **archivos separados** que luego convertirás en tests.

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

(El patrón RoutingAppender + MDC de Log4j2 es la forma canónica de dividir logs por clave. ([Apache Logging][5], [Roy Tutorials][6], [Stack Overflow][7]))

---

## 2) Convierte esos logs en **tests de Python** (pytest + requests)

Una vez que los logs sean líneas JSON o parseables, un pequeño generador puede emitir tests deterministas:

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
      "    # opcionalmente verificar campos estructurados del JSON de respuesta",
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

Consejos:

* Prefiere **logs JSON** para peticiones/respuestas; hace la generación de tests trivial.
* Mantén fuera las cabeceras sensibles (ej., Authorization).
* Si los cuerpos son grandes, almacena un hash en los logs y verifica la igualdad del hash en lugar del string completo.

---

## 3) Usa Spring para **proporcionar contexto** a "agentes" LLM

Si ya estás en Spring Boot, el camino más corto es **Spring AI**:

**a) Configura un `ChatClient` y plantillas de prompt.**
Spring AI te da abstracciones `ChatClient`/`PromptTemplate` y tool-calling para que el modelo pueda pedir a tu app que obtenga datos. ([Home][8], [Home][9])

```java
@Configuration
public class AiConfig {
  @Bean ChatClient chatClient(org.springframework.ai.chat.ChatModel model) {
    return ChatClient.builder(model).defaultSystem("Eres un agente bancario útil.").build();
  }
}
```

**b) Proporciona contexto mediante beans de Spring (servicios) y "tools".**
Expone búsquedas del dominio como **tools** para que el modelo pueda llamarlas durante un turno de chat. (Spring AI soporta tool calling: el modelo decide cuándo invocar; el resultado fluye de vuelta como contexto extra.) ([Home][9])

```java
@Component
public class AccountTools {
  @org.springframework.ai.tool.annotation.Tool
  public String fetchBalance(String userId){
    // consultar BD o servicio downstream
    return "{\"balance\": 1234.56, \"currency\": \"HKD\"}";
  }
}
```

**c) Añade recuperación (RAG) para documentos/código.**
Conecta un `VectorStore` (PGVector, etc.) y rellénalo con embeddings de tu conocimiento. En tiempo de ejecución, recupera los top-k chunks y adjúntalos al prompt. Hay un tutorial actual y práctico construyendo una pila RAG completa con Spring Boot + PGVector. ([sohamkamani.com][10])

**d) Propaga el contexto de usuario/sesión mediante Interceptors.**
Usa un `HandlerInterceptor` (o tu Filter) para resolver `userId`, `tenantId`, roles, locale, últimas-N acciones—ponlos en:

* atributos de la petición,
* un bean con ámbito, o
* las partes **system** y **user** de tu prompt.

**e) Un endpoint HTTP para gobernarlos a todos.**

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
    var userCtx = ctx.fromPrincipal(principal);          // ids, roles, preferencias
    var docs   = retriever.findRelevant((String)req.get("message")); // RAG
    return chat.prompt()
      .system("Usa tools si es necesario. Respeta tenant="+userCtx.tenant()+" y role="+userCtx.role()+".")
      .user("Contexto:\n"+docs+"\n\nEl usuario dice: "+req.get("message"))
      .call().content();                                  // las llamadas a tools suceden implícitamente
  }
}
```

**f) Opcional: Despliega "skills" con Spring Cloud Function.**
Si quieres que cada skill del agente sea una única función (ideal para serverless y enrutamiento por cabeceras), **Spring Cloud Function** te permite escribir `Function<T,R>` puras y enrutar dinámicamente—útil para conectar con AWS Lambda/Azure y para endpoints internos de "agent tools". ([cloud.spring.io][11], [Home][12], [Baeldung on Kotlin][13])

---

## 4) Integrando todo (flujo)

1.  **Filter** añade `traceId`, registra E/S HTTP.
2.  **AOP** envuelve métodos de servicio y emite eventos estructurados.
3.  **Log4j2 RoutingAppender** escribe archivos por traza.
4.  **Generador Python** lee esos archivos → emite **pytest** que reproduce llamadas reales.
5.  **Endpoint Spring AI** usa:
    * contexto de petición/tenant/usuario desde Interceptor/Filter,
    * "tools" del dominio para datos en vivo,
    * almacén vectorial (RAG) para contexto de doc/código,
    * `ChatClient` para la orquestación del chat.

Eso te da tests reproducibles y una interfaz de agente robusta y contextual—ambas impulsadas por la misma telemetría.

Si quieres, puedo esbozar una estructura mínima de repositorio con las piezas de Spring Boot, una configuración de Log4j2 y el script generador de Python integrado en un flujo de trabajo `make testgen && pytest`.

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