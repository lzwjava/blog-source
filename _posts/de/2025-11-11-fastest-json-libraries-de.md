---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Schnellste JSON-Bibliotheken in Rust und Java
translated: true
type: note
---

### Die schnellsten JSON-Bibliotheken in Rust und Java

Um die schnellsten JSON-Bibliotheken in Rust und Java zu vergleichen, müssen wir uns die Leistung beim Parsen (Deserialisierung) und bei der Serialisierung ansehen, da dies die Kernoperationen sind. Die Leistung wird typischerweise als Durchsatz (z.B. GB/s) oder Zeit für Standarddatensätze wie twitter.json (mittelgroße Objekt-Array), canada.json (großes Zahlen-Array) und citm_catalog.json (verschachtelte Objekte) gemessen. Diese Datensätze sind in JSON-Benchmarks üblich.

#### Der Schnellste in Rust: sonic-rs
- **Überblick**: sonic-rs ist eine SIMD-beschleunigte Bibliothek von CloudWeGo, die für hochgeschwindigkeits JSON-Verarbeitung in Rust entwickelt wurde. Sie parst direkt in Rust-Structs ohne Zwischenschritte (wie das "Band" in simd-json), was sie für die Deserialisierung schneller macht. Sie unterstützt sowohl strukturiertes (zu Structs) als auch untypisiertes (zu DOM-ähnlich) Parsing.
- **Wichtige Leistungshöhepunkte** (aus Benchmarks auf Intel Xeon Platinum 8260 @ 2.40GHz):
  - Deserialisierung zu Struct (Zeit in ms, niedriger ist besser):
    - twitter.json: ~0.7 ms
    - canada.json: ~3.8 ms
    - citm_catalog.json: ~1.2 ms
  - Das macht sonic-rs 1,5-2x schneller als simd-json (eine weitere Top-Rust-Bibliothek) für die Deserialisierung und 3-4x schneller als serde_json (der Standard).
  - Serialisierung: Vergleichbar oder leicht schneller als simd-json, z.B. ~0.4 ms für twitter.json.
  - Durchsatz: Übersteigt oft 2-4 GB/s für große Eingaben, dank SIMD-Optimierungen für Strings, Zahlen und Leerzeichen.
- **Stärken**: Zero-Copy wo möglich, geringer Speicherverbrauch, sichere (geprüfte) und unsichere (ungeprüfte) Modi für zusätzliche Geschwindigkeit.
- **Schwächen**: Neuere Bibliothek, weniger ausgereiftes Ökosystem als serde_json.

#### Der Schnellste in Java: DSL-JSON oder simdjson-java (je nach Anwendungsfall)
- **Überblick**:
  - DSL-JSON verwendet Compile-Time-Code-Generierung (über Annotationen wie @CompiledJson), um Reflection zu vermeiden und GC zu minimieren, was es für die Deserialisierung in Hochlast-Szenarien außerordentlich schnell macht.
  - simdjson-java ist ein Java-Port der simdjson C++-Bibliothek, der SIMD für Gigabyte-pro-Sekunde-Parsing verwendet. Es ist besonders stark für große Eingaben, hatte aber in frühen Versionen Einschränkungen wie teilweise Unicode-Unterstützung.
- **Wichtige Leistungshöhepunkte**:
  - DSL-JSON: 3-5x schneller als Jackson für die Deserialisierung in engen Schleifen (z.B. mittelgroße Objekte ~500 Bytes). Spezifische Datensatzzahlen sind rar, aber es wird behauptet, dass es mit binären Codecs wie Protobuf gleichzieht. In allgemeinen Benchmarks übertrifft es Jackson um 3x+ bei Serialisierung und Parsing.
  - simdjson-java: ~1450 ops/sec auf Intel Core i5-4590 für typische Operationen, 3x schneller als Jackson, Jsoniter und Fastjson2. Für große Eingaben nähert es sich 1-3 GB/s, ähnlich wie sein C++-Gegenstück. In Vergleichen ist es 3x schneller als Jsoniter beim Parsing.
  - Jsoniter (ehrenvolle Erwähnung): 2-6x schneller als Jackson, mit Decodiergeschwindigkeiten wie 3,22x Jackson für Ganzzahlen und 2,91x für Objektlisten (Durchsatzverhältnisse in JMH-Benchmarks).
  - Zum Kontext: Jackson (beliebt, aber nicht der schnellste) verarbeitet Standarddatensätze in der 2-3-fachen Zeit dieser Spitzenreiter.
- **Stärken**: DSL-JSON für Low-GC, High-Throughput-Apps; simdjson-java für rohe Geschwindigkeit bei großen Daten. Beide bewältigen JVM-Einschränkungen gut.
- **Schwächen**: DSL-JSON erfordert Annotationen für maximale Geschwindigkeit; simdjson-java hat Funktionslücken (z.B. vollständiges Float-Parsing in älteren Versionen).

#### Direkter Vergleich: Rust vs Java
- **Leistungslücke**: Rusts sonic-rs ist im Allgemeinen 2-5x schneller als Javas Top-Bibliotheken für ähnliche Aufgaben. Zum Beispiel:
  - In einem realen AWS-Lambda-Benchmark, der 1 GB JSON-Logs (Streaming + Parsing) verarbeitete, brauchte Rust mit simd-json ~2 Sekunden (0,5 GB/s), während Java mit Jsoniter 8-10 Sekunden (0,1 GB/s) brauchte. Die Verwendung von simdjson-java könnte die Lücke auf ~3 Sekunden (0,3 GB/s) schließen, aber Rust gewinnt immer noch aufgrund nativer Kompilierung, keiner GC-Pausen und besserer SIMD-Nutzung.
  - Bei Standarddatensätzen deserialisiert sonic-rs canada.json in ~4 ms, während Java-Bibliotheken wie Jsoniter oder DSL-JSON in vergleichbaren Setups 10-20 ms benötigen (indirekt, da direkte Vergleiche selten sind).
  - Die Serialisierung ist enger, wobei Rust manchmal nur 1,5-2x schneller ist.
- **Warum Rust schneller ist**: Native Code, kein JVM-Overhead, Zero-Cost-Abstraktionen und bessere Kontrolle über den Speicher. Java-Bibliotheken sind durch GC und Bytecode eingeschränkt, obwohl Optimierungen wie Compile-Time-Generierung (DSL-JSON) helfen.
- **Andere Faktoren**:
  - Funktionen: Rust-Bibliotheken integrieren sich gut in das serde-Ökosystem für Flexibilität. Java-Bibliotheken wie Jackson haben mehr Plugins für komplexe Schemata.
  - Anwendungsfälle: Rust für Ultra-Hochleistung (z.B. Server, CLI-Tools); Java für Enterprise mit einfacherer Integration.
  - Einschränkungen: Benchmarks variieren je nach Hardware, Datensatz und JVM-Version (z.B. verbessert Java 21+ die GC). Rusts Sicherheitsprüfungen können Overhead hinzufügen, wenn nicht ungeprüfte Modi verwendet werden.

Wenn Sie einen spezifischen Datensatz oder Anwendungsfall haben (z.B. nur Serialisierung), kann ich tiefer graben.

### Referenzen
- sonic-rs GitHub (Rust Benchmarks) (https://github.com/cloudwego/sonic-rs)
- simdjson GitHub (Basis für Rust- und Java-Ports) (https://github.com/simdjson/simdjson)
- Serverless Speed: Rust vs. Go, Java, and Python in AWS Lambda (Benchmark) (https://scanner.dev/blog/serverless-speed-rust-vs-go-java-and-python-in-aws-lambda-functions)
- The Lightning Fast JSON Parser Library For Java (simdjson-java) (https://www.i-programmer.info/news/80-java/16553-the-lightning-fast-json-parser-library-for-java.html)
- Jsoniter Benchmark (Java-Vergleiche) (https://jsoniter.com/benchmark.html)
- DSL-JSON vs Jackson (Java-Deserialisierung) (https://medium.com/@vishalpriyadarshi/dsl-json-vs-jackson-who-deserializes-faster-in-java-7f0ee164606a)
- Optimizing JSON Performance in Java - 2025 Edition (https://medium.com/towardsdev/optimizing-json-performance-in-java-what-actually-works-2025-edition-4f124e24d786)