---
audio: false
generated: true
image: false
lang: ja
layout: post
title: エンドツーエンドトレースからLLMエージェントパイプライン
translated: true
type: note
---

あなたは確かな道を進んでいます：AOP（AspectJ）、サーブレットフィルター、Log4j2はそれぞれ異なるレイヤーで優れています。以下に、これらを組み合わせて使用するコンパクトでエンドツーエンドの方法を示します。まず、**実行トレースとHTTPの入出力を収集**し（これによりPythonテストを自動生成できます）、次に、Spring内のLLM「エージェント」エンドポイントに**豊富なコンテキストを提供**します。

---

## 1) 必要な情報をキャプチャする (AOP + フィルター + Log4j2)

**a) AOPを用いたメソッドインターセプション（実行時間、引数、戻り値/例外）**

サービスメソッドをラップするために`@Around`アドバイスを使用します。すべてのレイヤーのログを関連付けるために、MDCに`traceId`を保存します。

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

（「Aroundアドバイス」は、呼び出しの前後ロジックと制御が必要な場合に適したツールです。（[Home][1], [DigitalOcean][2]））

**b) フィルターを用いたHTTPロギング（リクエスト/レスポンスボディ + ステータス）**

呼び出しごとにリクエスト/レスポンスを一度ラップします。同じ`traceId`を（ヘッダーから取得するか生成して）関連付けます。Springの`OncePerRequestFilter`パターンが標準です。優れたガイドでは、ボディを安全にバッファリングし、二重消費を回避する方法が示されています。（[Baeldung on Kotlin][3], [SigNoz][4]）

**c) Log4j2のRoutingAppenderを使用して、ユーザー/テナント/テストごとにログをルーティング**

これにより、一致したログ（例：MDC内の`traceId`や`tenantId`）を**個別のファイル**に送信し、後でテストに変換できます。

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

（Log4j2のRoutingAppender + MDCパターンは、キーによってログを分割する標準的な方法です。（[Apache Logging][5], [Roy Tutorials][6], [Stack Overflow][7]））

---

## 2) それらのログを**Pythonテスト**に変換する (pytest + requests)

ログがJSON形式または解析可能な行になれば、小さなジェネレーターが決定論的なテストを出力できます：

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

ヒント：

* リクエスト/レスポンスには**JSONログ**を優先します。これによりテスト生成が簡単になります。
* 機密性の高いヘッダー（例：Authorization）はログに含めないでください。
* ボディが大きい場合は、ログに完全な文字列ではなくハッシュを保存し、ハッシュの等価性をアサートします。

---

## 3) Springを使用してLLM「エージェント」に**コンテキストを提供**する

現在Spring Bootを使用している場合、最短の経路は**Spring AI**です：

**a) `ChatClient`とプロンプトテンプレートをセットアップする。**
Spring AIは`ChatClient`/`PromptTemplate`の抽象化とツール呼び出しを提供するため、モデルがアプリにデータ取得を依頼できます。（[Home][8], [Home][9]）

```java
@Configuration
public class AiConfig {
  @Bean ChatClient chatClient(org.springframework.ai.chat.ChatModel model) {
    return ChatClient.builder(model).defaultSystem("You are a helpful banking agent.").build();
  }
}
```

**b) Spring Bean（サービス）と「ツール」を介してコンテキストを提供する。**
ドメインルックアップを**ツール**として公開し、モデルがチャットのターン中にそれらを呼び出せるようにします。（Spring AIはツール呼び出しをサポートしています—モデルが呼び出すタイミングを決定し、結果が追加のコンテキストとして戻ります。（[Home][9]））

```java
@Component
public class AccountTools {
  @org.springframework.ai.tool.annotation.Tool
  public String fetchBalance(String userId){
    // DBまたはダウンストリームサービスにクエリ
    return "{\"balance\": 1234.56, \"currency\": \"HKD\"}";
  }
}
```

**c) ドキュメント/コードの検索（RAG）を追加する。**
`VectorStore`（PGVectorなど）を配線し、ナレッジの埋め込みを投入します。実行時に、トップkのチャンクを取得し、それらをプロンプトに添付します。Spring Boot + PGVectorを使用した完全なRAGスタックを構築する、現在利用可能で実用的なチュートリアルがあります。（[sohamkamani.com][10]）

**d) インターセプターを介してユーザー/セッションコンテキストをスレッド化する。**
`HandlerInterceptor`（またはあなたのフィルター）を使用して、`userId`、`tenantId`、ロール、ロケール、直近のNアクションを解決し、それらを以下に配置します：

* リクエスト属性、
* スコープ付きBean、または
* あなたのプロンプトの**システム**部分と**ユーザー**部分。

**e) すべてを統括する1つのHTTPエンドポイント。**

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
      .call().content();                                  // ツール呼び出しは暗黙的に行われる
  }
}
```

**f) オプション：Spring Cloud Functionで「スキル」をデプロイする。**
各エージェントスキルを単一の関数としてデプロイしたい場合（サーバーレスおよびヘッダーによるルーティングに最適）、**Spring Cloud Function**を使用すると、純粋な`Function<T,R>`を記述し、動的にルーティングできます—AWS Lambda/Azureへの接続や、内部の「エージェントツール」エンドポイントに組み込むのに便利です。（[cloud.spring.io][11], [Home][12], [Baeldung on Kotlin][13]）

---

## 4) すべてをまとめる（フロー）

1.  **フィルター**が`traceId`を追加し、HTTPの入出力をログに記録します。
2.  **AOP**がサービスメソッドをラップし、構造化されたイベントを出力します。
3.  **Log4j2 RoutingAppender**がトレースごとのファイルを書き込みます。
4.  **Pythonジェネレーター**がそれらのファイルを読み取り、実際の呼び出しを再生する**pytest**を出力します。
5.  **Spring AI**エンドポイントは以下を使用します：
    *   Interceptor/Filterからのリクエスト/テナント/ユーザーコンテキスト、
    *   ライブデータ用のドメイン「ツール」、
    *   ドキュメント/コードコンテキスト用のベクターストア（RAG）、
    *   チャットオーケストレーション用の`ChatClient`。

これにより、再現可能なテストと、堅牢で文脈に応じたエージェントインターフェースの両方が得られます—どちらも同じテレメトリによって駆動されます。

必要であれば、Spring Bootのコンポーネント、Log4j2設定、および`make testgen && pytest`ワークフローに組み込まれたPythonジェネレータースクリプトを含む、最小限のリポジトリ構造をスケッチできます。

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