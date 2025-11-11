---
audio: false
generated: true
image: false
lang: ar
layout: post
title: مسار التتبع الشامل إلى وكيل نموذج اللغة الكبير
translated: true
type: note
---

أنت على المسار الصحيح: AOP (AspectJ)، ومرشحات Servlet، و Log4j2 كل منهم يتفوق في طبقات مختلفة. إليك طريقة مدمجة وشاملة لاستخدامهم معًا — أولاً **لتجميع آثار التنفيذ ومدخلات/مخرحات HTTP** (حتى تتمكن من إنشاء اختبارات Python تلقائيًا)، ثم **لتغذية سياق غني إلى نقطة نهاية "الوكيل" LLM في Spring**.

---

## 1) احتجز ما تحتاجه (AOP + Filter + Log4j2)

**أ) اعتراض الاستدعاءات باستخدام AOP (التوقيتات، الوسائط، القيم المُرجعة/الاستثناءات).**

استخدم النصيحة `@Around` لتفريغ دوال الخدمة؛ خزن `traceId` في MDC بحيث تندمج السجلات من جميع الطبقات معًا.

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

(النصيحة "Around" هي الأداة المناسبة عندما تحتاج إلى منطق قبل/بعد الاستدعاء والتحكم في الاستدعاء. ([Home][1], [DigitalOcean][2]))

**ب) تسجيل HTTP باستخدام مرشح Filter (نص الطلب/الاستجابة + الحالة).**

لف الطلب/الاستجابة مرة واحدة لكل استدعاء؛ أرفق نفس `traceId` (من الرأس أو قم بتوليده). نمط `OncePerRequestFilter` في Spring هو المعيار. تظهر الأدلة الجيدة كيفية تخزين النص بأمان وتجنب الاستهلاك المزدوج. ([Baeldung on Kotlin][3], [SigNoz][4])

**ج) توجيه السجلات لكل مستخدم/عميل/اختبار باستخدام Log4j2 RoutingAppender.**

هذا يسمح لك بإرسال السجلات المطابقة (مثلًا بواسطة `traceId` أو `tenantId` في MDC) إلى **ملفات منفصلة** ستحولها لاحقًا إلى اختبارات.

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

(نمط RoutingAppender + MDC في Log4j2 هو الطريقة الأساسية لفصل السجلات بواسطة مفتاح. ([Apache Logging][5], [Roy Tutorials][6], [Stack Overflow][7]))

---

## 2) حول تلك السجلات إلى **اختبارات Python** (pytest + requests)

بمجرد أن تصبح السجلات بصيغة JSON أو أسطر قابلة للتحليل، يمكن لمولد صغير أن يصدر اختبارات حتمية:

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

نصائح:

* فضّل **سجلات JSON** للطلبات/الاستجابات؛ فهذا يجعل توليد الاختبارات تافهًا.
* احتفظ بالرؤوس الحساسة خارج السجلات (مثل Authorization).
* إذا كانت النصوص كبيرة، فخزن تجزئة hash في السجلات وتحقق من مساواة التجزئة بدلاً من النص الكامل.

---

## 3) استخدم Spring **لتوفير السياق** لوكلاء LLM

إذا كنت تستخدم Spring Boot حاليًا، فأقصر طريق هو **Spring AI**:

**أ) إعداد `ChatClient` وقوالب Prompt.**
يمنحك Spring AI تجريدات `ChatClient`/`PromptTemplate` واستدعاء الأدوات حتى يتمكن النموذج من طلب بيانات من تطبيقك. ([Home][8], [Home][9])

```java
@Configuration
public class AiConfig {
  @Bean ChatClient chatClient(org.springframework.ai.chat.ChatModel model) {
    return ChatClient.builder(model).defaultSystem("You are a helpful banking agent.").build();
  }
}
```

**ب) توفير السياق عبر Spring beans (الخدمات) و "الأدوات".**
عرض عمليات البحث في المجال كـ **أدوات** حتى يتمكن النموذج من استدعائها أثناء جلسة المحادثة. (يدعم Spring AI استدعاء الأدوات — النموذج يقرر متى يستدعي؛ تتدفق النتيجة مرة أخرى كسياق إضافي.) ([Home][9])

```java
@Component
public class AccountTools {
  @org.springframework.ai.tool.annotation.Tool
  public String fetchBalance(String userId){
    // استعلام قاعدة البيانات أو خدمة تابعة
    return "{\"balance\": 1234.56, \"currency\": \"HKD\"}";
  }
}
```

**ج) أضف الاسترجاع (RAG) للمستندات/الكود.**
اربط `VectorStore` (مثل PGVector، إلخ.) وقم بتعبئته بتضميمات embeddings للمعارف الخاصة بك. أثناء التشغيل، استرجع أجزاء top-k وألحقها بالـ prompt. هناك برنامج تعليمي عملي حالي يبني بنية RAG كاملة مع Spring Boot + PGVector. ([sohamkamani.com][10])

**د) تمرير سياق المستخدم/الجلسة عبر المعترضات Interceptors.**
استخدم `HandlerInterceptor` (أو الـ Filter الخاص بك) لحل `userId`، `tenantId`، الأدوار، اللغة، آخر N إجراء — وضعهم في:

* سمات الطلب request attributes،
* أو bean ذي نطاق scope،
* أو أجزاء **النظام system** و **المستخدم user** في الـ prompt الخاص بك.

**هـ) نقطة نهاية HTTP واحدة لتجميعهم جميعًا.**

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
    var userCtx = ctx.fromPrincipal(principal);          // المعرفات، الأدوار، التفضيلات
    var docs   = retriever.findRelevant((String)req.get("message")); // RAG
    return chat.prompt()
      .system("Use tools if needed. Respect tenant="+userCtx.tenant()+" and role="+userCtx.role()+".")
      .user("Context:\n"+docs+"\n\nUser says: "+req.get("message"))
      .call().content();                                  // استدعاءات الأدوات تحدث ضمنيًا
  }
}
```

**و) اختياري: نشر "المهارات" باستخدام Spring Cloud Function.**
إذا كنت تريد أن تكون كل مهارة وكيل كدالة function واحدة (رائع للخوادمless serverless والتوجيه بواسطة الرؤوس)، فإن **Spring Cloud Function** يسمح لك بكتابة `Function<T,R>` خالصة والتوجيه ديناميكيًا — مفيد للتوصيل مع AWS Lambda/Azure ولنقاط نهاية "أدوات الوكيل" الداخلية. ([cloud.spring.io][11], [Home][12], [Baeldung on Kotlin][13])

---

## 4) تجميع كل شيء معًا (التدفق)

1.  **المرشح Filter** يضيف `traceId`، ويسجل مدخلات/مخرجات HTTP.
2.  **AOP** يلف دوال الخدمة ويصدر أحداثًا منظمة.
3.  **Log4j2 RoutingAppender** يكتب ملفات لكل أثر trace.
4.  **المولد Python** يقرأ تلك الملفات → يصدر **pytest** يعيد تشغيل الاستدعاءات الحقيقية.
5.  **نقطة نهاية Spring AI** تستخدم:
    * سياق الطلب/العميل/المستخدم من المعترض Interceptor/المرشح Filter،
    * "أدوات" المجال للبيانات الحية،
    * مخزن المتجهات Vector store (RAG) لسياق المستند/الكود،
    * `ChatClient` لتنسيق المحادثة.

هذا يمنحك اختبارات قابلة لإعادة الإنتاج وواجهة وكيل قوية ومرنة — كلاهما مدفوع بنفس بيانات Telemetry.

إذا أردت، يمكنني رسم هيكل مستودع minimal مع أجزاء Spring Boot، وتكوين Log4j2، وسكريبت المولد Python موصولة في سير عمل `make testgen && pytest`.

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