---
audio: false
generated: true
image: false
lang: hi
layout: post
title: एंड टू एंड ट्रेस टू एलएलएम एजेंट पाइपलाइन
translated: true
type: note
---

आप एक सही रास्ते पर हैं: AOP (AspectJ), servlet filters, और Log4j2 अलग-अलग लेयर्स पर अपनी भूमिका निभाते हैं। यहां एक संक्षिप्त, एंड-टू-एंड तरीका है जिससे आप इन सभी को एक साथ इस्तेमाल कर सकते हैं—पहले **एग्जिक्यूशन ट्रेस और HTTP I/O को कैप्चर करने के लिए** (ताकि आप Python टेस्ट ऑटो-जेनरेट कर सकें), और फिर **Spring में एक LLM "एजेंट" एंडपॉइंट को समृद्ध कॉन्टेक्स्ट प्रदान करने के लिए**।

---

## 1) आपको जो चाहिए उसे कैप्चर करें (AOP + Filter + Log4j2)

**a) AOP के साथ मेथड इंटरसेप्शन (टाइमिंग, आर्ग्युमेंट्स, रिटर्न/एरर्स)।**

सर्विस मेथड्स को रैप करने के लिए `@Around` एडवाइस का उपयोग करें; MDC में एक `traceId` स्टोर करें ताकि सभी लेयर्स के लॉग्स इकट्ठे हो सकें।

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

("Around advice" सही टूल है जब आपको प्री/पोस्ट लॉजिक और कॉल पर कंट्रोल की जरूरत हो। ([Home][1], [DigitalOcean][2]))

**b) Filter के साथ HTTP लॉगिंग (रिक्वेस्ट/रिस्पॉन्स बॉडी + स्टेटस)।**

एक बार प्रति कॉल रिक्वेस्ट/रिस्पॉन्स को रैप करें; उसी `traceId` को अटैच करें (हेडर से या जेनरेट करें)। Spring का `OncePerRequestFilter` पैटर्न स्टैंडर्ड है। अच्छे गाइड दिखाते हैं कि बॉडी को सुरक्षित रूप से बफर कैसे करें और डबल-कंजम्पशन से कैसे बचें। ([Baeldung on Kotlin][3], [SigNoz][4])

**c) Log4j2 RoutingAppender का उपयोग करके प्रति यूजर/टेनेंट/टेस्ट लॉग्स को रूट करें।**

यह आपको मैच किए गए लॉग्स (जैसे, MDC में `traceId` या `tenantId` द्वारा) को **अलग-अलग फाइलों** में भेजने देता है, जिन्हें आप बाद में टेस्ट में कन्वर्ट करेंगे।

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

(Log4j2 का RoutingAppender + MDC पैटर्न की (key) द्वारा लॉग्स को अलग करने का मानक तरीका है। ([Apache Logging][5], [Roy Tutorials][6], [Stack Overflow][7]))

---

## 2) उन लॉग्स को **Python टेस्ट** में बदलें (pytest + requests)

एक बार लॉग्स JSON-जैसे या पार्स करने योग्य लाइनों में आ जाएं, तो एक छोटा जेनरेटर डिटरमिनिस्टिक टेस्ट बना सकता है:

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

सुझाव:

* रिक्वेस्ट/रिस्पॉन्स के लिए **JSON लॉग्स** को प्राथमिकता दें; इससे टेस्ट जनरेशन आसान हो जाता है।
* संवेदनशील हेडर (जैसे, Authorization) को बाहर रखें।
* अगर बॉडी बड़ी है, तो लॉग्स में हैश स्टोर करें और पूरी स्ट्रिंग के बजाय हैश इक्वलिटी का उपयोग करें।

---

## 3) LLM "एजेंट्स" को **कॉन्टेक्स्ट प्रदान** करने के लिए Spring का उपयोग करें

अगर आप आज Spring Boot पर हैं, तो सबसे छोटा रास्ता **Spring AI** है:

**a) एक `ChatClient` और प्रॉम्प्ट टेम्प्लेट सेटअप करें।**
Spring AI आपको `ChatClient`/`PromptTemplate` एब्स्ट्रक्शन और टूल-कॉलिंग देता है ताकि मॉडल आपके ऐप से डेटा फ़ेच करने के लिए कह सके। ([Home][8], [Home][9])

```java
@Configuration
public class AiConfig {
  @Bean ChatClient chatClient(org.springframework.ai.chat.ChatModel model) {
    return ChatClient.builder(model).defaultSystem("You are a helpful banking agent.").build();
  }
}
```

**b) Spring beans (सर्विसेज) और "टूल्स" के जरिए कॉन्टेक्स्ट प्रदान करें।**
डोमेन लुकअप्स को **टूल्स** के रूप में एक्सपोज करें ताकि मॉडल चैट के दौरान उन्हें कॉल कर सके। (Spring AI टूल कॉलिंग सपोर्ट करता है—मॉडल तय करता है कि कब इनवोक करना है; रिजल्ट एक्स्ट्रा कॉन्टेक्स्ट के रूप में वापस आता है।) ([Home][9])

```java
@Component
public class AccountTools {
  @org.springframework.ai.tool.annotation.Tool
  public String fetchBalance(String userId){
    // DB या डाउनस्ट्रीम सर्विस को क्वेरी करें
    return "{\"balance\": 1234.56, \"currency\": \"HKD\"}";
  }
}
```

**c) डॉक्यूमेंट्स/कोड के लिए रिट्रीवल (RAG) जोड़ें।**
एक `VectorStore` (PGVector, आदि.) वायर करें और अपने नॉलेज के एम्बेडिंग्स से इसे भरें। रनटाइम पर, टॉप-के चंक्स रिट्रीव करें और उन्हें प्रॉम्प्ट से अटैच करें। Spring Boot + PGVector के साथ एक पूर्ण RAG स्टैक बनाने का एक करंट, प्रैक्टिकल ट्यूटोरियल मौजूद है। ([sohamkamani.com][10])

**d) इंटरसेप्टर्स के जरिए यूजर/सेशन कॉन्टेक्स्ट को थ्रेड करें।**
`userId`, `tenantId`, भूमिकाएं, लोकेल, आखिरी-N एक्शन्स को रिजॉल्व करने के लिए एक `HandlerInterceptor` (या आपका Filter) का उपयोग करें—उन्हें इसमें डालें:

* रिक्वेस्ट एट्रिब्यूट्स,
* एक स्कोप्ड बीन, या
* आपके प्रॉम्प्ट के **सिस्टम** और **यूजर** भाग।

**e) सभी को नियंत्रित करने वाला एक HTTP एंडपॉइंट।**

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

**f) वैकल्पिक: Spring Cloud Function के साथ "स्किल्स" डिप्लॉय करें।**
अगर आप प्रत्येक एजेंट स्किल को एक सिंगल फंक्शन के रूप में चाहते हैं (सर्वरलेस और हेडर द्वारा रूटिंग के लिए बढ़िया), **Spring Cloud Function** आपको शुद्ध `Function<T,R>` लिखने देता है और डायनामिक रूप से रूट करता है—AWS Lambda/Azure में प्लग इन करने और आंतरिक "एजेंट टूल" एंडपॉइंट्स के लिए उपयोगी। ([cloud.spring.io][11], [Home][12], [Baeldung on Kotlin][13])

---

## 4) सभी को एक साथ लाना (फ्लो)

1. **Filter** `traceId` जोड़ता है, HTTP I/O लॉग करता है।
2. **AOP** सर्विस मेथड्स को रैप करता है और स्ट्रक्चर्ड इवेंट्स भेजता है।
3. **Log4j2 RoutingAppender** प्रति-ट्रेस फाइलें लिखता है।
4. **Python जेनरेटर** उन फाइलों को पढ़ता है → **pytest** जनरेट करता है जो रियल कॉल्स को दोहराता है।
5. **Spring AI** एंडपॉइंट इस्तेमाल करता है:

   * इंटरसेप्टर/Filter से रिक्वेस्ट/टेनेंट/यूजर कॉन्टेक्स्ट,
   * लाइव डेटा के लिए डोमेन "टूल्स",
   * डॉक/कोड कॉन्टेक्स्ट के लिए वेक्टर स्टोर (RAG),
   * चैट ऑर्केस्ट्रेशन के लिए `ChatClient`।

यह आपको रिप्रोड्यूसिबल टेस्ट और एक मजबूत, कॉन्टेक्स्चुअल एजेंट इंटरफेस देता है—दोनों एक ही टेलीमेट्री द्वारा संचालित।

अगर आप चाहें, तो मैं Spring Boot पार्ट्स, एक Log4j2 कॉन्फ़िग, और Python जेनरेटर स्क्रिप्ट के साथ एक मिनिमल रेपो स्ट्रक्चर का स्केच बना सकता हूं, जो एक `make testgen && pytest` वर्कफ्लो में वायर्ड हो।

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