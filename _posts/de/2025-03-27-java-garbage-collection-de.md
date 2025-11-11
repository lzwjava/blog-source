---
audio: false
generated: true
lang: de
layout: post
title: Garbage Collection in Java
translated: true
type: note
---

Okay, lass uns etwas über Garbage Collection (GC) in Java lernen! Es ist ein entscheidender Aspekt der Speicherverwaltung in Java, der Entwicklern hilft, manuelle Speicherzuweisung und -freigabe zu vermeiden.

**Was ist Garbage Collection in Java?**

Garbage Collection ist der automatische Prozess der Speicherrückgewinnung, bei dem der von Objekten belegte Speicherplatz freigegeben wird, die von einer Java-Anwendung nicht mehr verwendet werden. Im Wesentlichen ist es Javas Methode, den "Müll" (unbenutzte Objekte) aufzuräumen, um Platz für neue Objekte zu schaffen.

**Warum wird Garbage Collection benötigt?**

In vielen anderen Programmiersprachen (wie C oder C++) sind Entwickler für die explizite Zuordnung und Freigabe von Speicher verantwortlich, indem sie Funktionen wie `malloc` und `free` verwenden. Diese manuelle Speicherverwaltung kann zu mehreren Problemen führen:

*   **Speicherlecks:** Wenn Speicher zugewiesen, aber nie freigegeben wird, kann der Anwendung irgendwann der Speicher ausgehen und sie stürzt ab.
*   **Dangling Pointer:** Wenn Speicher freigegeben wird, aber ein Zeiger noch immer auf diesen Speicherort verweist, kann die Verwendung dieses Zeigers zu unvorhersehbarem Verhalten oder Abstürzen führen.
*   **Erhöhte Entwicklungscomplexity:** Die manuelle Verwaltung von Speicher fügt der Softwareentwicklung eine erhebliche Komplexitätsebene hinzu.

Die automatische Garbage Collection in Java befreit Entwickler von der Last der manuellen Speicherverwaltung und erleichtert das Schreiben von sichererem und zuverlässigerem Code.

**Wie funktioniert Garbage Collection?**

Die Kernidee der Garbage Collection ist zu identifizieren, welche Objekte im Speicher von der Anwendung noch verwendet werden und welche nicht. Der Garbage Collector gibt dann den von den unbenutzten Objekten belegten Speicher frei.

Hier ist eine vereinfachte Übersicht des Prozesses:

1.  **Identifizieren lebender Objekte (Markieren):** Der Garbage Collector beginnt damit, die Menge der Objekte zu identifizieren, die von den "Root"-Objekten aus noch erreichbar sind. Root-Objekte sind typischerweise Objekte, auf die die Anwendung direkt zugreifen kann, wie zum Beispiel:
    *   Lokale Variablen in aktuell ausgeführten Methoden.
    *   Statische Variablen.
    *   Von nativem Code referenzierte Objekte.
    *   Die aktiven Threads der Java Virtual Machine (JVM).

    Der Garbage Collector durchläuft den Objektgraphen, beginnend von diesen Roots, und markiert alle Objekte, die erreichbar sind.

2.  **Speicherrückgewinnung (Sweeping und Komprimieren):** Sobald die lebenden Objekte markiert sind, muss der Garbage Collector den von den unmarkierten (nicht erreichbaren) Objekten belegten Speicher zurückfordern. Verschiedene Garbage-Collection-Algorithmen verwenden dafür unterschiedliche Strategien:

    *   **Mark and Sweep:** Dieser Algorithmus identifiziert und markiert die lebenden Objekte und durchkämmt dann den Speicher, wobei er den von den unmarkierten Objekten belegten Platz freigibt. Dies kann zu Speicherfragmentierung führen (kleine, verstreute Blöcke freien Speichers, die nicht groß genug sind, um neue Objekte zuzuweisen).
    *   **Mark and Compact:** Dieser Algorithmus markiert ebenfalls lebende Objekte. Nach dem Markieren bewegt (komprimiert) er die lebenden Objekte im Speicher zusammenhängend, beseitigt so die Fragmentierung und erleichtert die Zuweisung zusammenhängender Speicherblöcke für neue Objekte.
    *   **Copying:** Dieser Algorithmus unterteilt den Speicher in zwei oder mehr Regionen. Lebende Objekte werden von einer Region in eine andere kopiert, wodurch der Platz in der ursprünglichen Region effektiv freigegeben wird.

**Schlüsselkonzepte in der Java Garbage Collection:**

*   **Heap:** Der Speicherbereich, in dem Objekte in Java angelegt werden. Der Garbage Collector arbeitet primär auf dem Heap.
*   **Young Generation (Nursery):** Dies ist ein Teil des Heaps, in dem neu erstellte Objekte anfänglich zugewiesen werden. Er ist weiter unterteilt in:
    *   **Eden Space:** Wo die meisten neuen Objekte erstellt werden.
    *   **Survivor Spaces (S0 und S1):** Wird verwendet, um Objekte zu halten, die einige Minor-Garbage-Collection-Zyklen überlebt haben.
*   **Old Generation (Tenured Generation):** Objekte, die mehrere Garbage-Collection-Zyklen in der Young Generation überlebt haben, werden schließlich in die Old Generation verschoben. Objekte in der Old Generation sind im Allgemeinen langlebig.
*   **Permanent Generation (PermGen) / Metaspace:** In älteren Java-Versionen (vor Java 8) speicherte die Permanent Generation Metadaten über Klassen und Methoden. In Java 8 und später wurde dies durch Metaspace ersetzt, das Teil des nativen Speichers ist (nicht des Java-Heaps).
*   **Garbage-Collection-Algorithmen:** Für die Garbage Collection werden verschiedene Algorithmen verwendet, die jeweils ihre eigenen Kompromisse in Bezug auf Leistung und Effizienz haben.

**Generational Garbage Collection:**

Die Java HotSpot JVM (die gebräuchlichste JVM) verwendet einen generationalen Ansatz für die Garbage Collection. Dies basiert auf der Beobachtung, dass die meisten Objekte in einer Anwendung eine kurze Lebensdauer haben.

1.  **Minor GC (Young Generation GC):** Wenn der Eden Space voll ist, wird ein Minor GC ausgelöst. Lebende Objekte aus Eden und einem der Survivor Spaces (z.B. S0) werden in den anderen Survivor Space (S1) kopiert. Objekte, die eine bestimmte Anzahl von Minor-GC-Zyklen überlebt haben, werden in die Old Generation verschoben. Nicht erreichbare Objekte werden verworfen.

2.  **Major GC (Old Generation GC) / Full GC:** Wenn die Old Generation voll wird, wird ein Major GC (oder manchmal ein Full GC, der sowohl die Young als auch die Old Generation umfassen kann) durchgeführt. Dieser Prozess ist im Allgemeinen zeitaufwändiger als ein Minor GC und kann längere Pausen in der Ausführung der Anwendung verursachen.

**Häufige Garbage Collector in der Java HotSpot JVM:**

Die Java HotSpot JVM bietet mehrere Garbage-Collection-Algorithmen, die basierend auf den Anforderungen der Anwendung (z.B. niedrige Latenz, hoher Durchsatz) ausgewählt werden können. Einige gebräuchliche sind:

*   **Serial Collector:** Verwendet einen einzelnen Thread für die Garbage Collection. Geeignet für kleine Anwendungen mit begrenzten Ressourcen.
*   **Parallel Collector:** Verwendet mehrere Threads für die Garbage Collection und verbessert so den Durchsatz. Geeignet für Anwendungen mit mittleren bis großen Datensätzen, die auf Multi-Core-Prozessoren laufen.
*   **CMS (Concurrent Mark Sweep) Collector:** Versucht, die Pausenzeiten zu minimieren, indem er den Großteil der Garbage-Collection-Arbeit parallel zu den Anwendungsthreads ausführt. Dies kann jedoch zu Fragmentierung führen und erfordert möglicherweise irgendwann einen Full GC.
*   **G1 (Garbage-First) Collector:** Ziel ist es, eine gute Balance zwischen Durchsatz und niedriger Latenz zu bieten. Er unterteilt den Heap in Regionen und priorisiert das Sammeln von Müll aus den Regionen mit dem meisten Müll. Er ist der Standard-Collector in Java 9 und später.
*   **ZGC (Z Garbage Collector):** Ein Garbage Collector mit niedriger Latenz, der für große Heaps entwickelt wurde. Er zielt auf Pausenzeiten von weniger als 10 ms ab.
*   **Shenandoah:** Ein weiterer Garbage Collector mit niedriger Latenz mit ähnlichen Zielen wie ZGC.

Sie können angeben, welchen Garbage Collector Sie über JVM-Kommandozeilenoptionen verwenden möchten.

**Wann läuft die Garbage Collection?**

Garbage Collection ist größtenteils ein automatischer Prozess, der von der JVM gesteuert wird. Sie läuft typischerweise, wenn:

*   Die Young Generation (Eden Space) voll ist.
*   Die Old Generation voll ist.
*   Das System wenig Speicher hat.

Während Sie nicht direkt steuern können, *wann* die Garbage Collection läuft, können Sie der JVM mit `System.gc()` vorschlagen, dass es ein guter Zeitpunkt für eine Garbage Collection sein könnte. Es gibt jedoch keine Garantie, dass die JVM den Garbage Collector tatsächlich sofort oder überhaupt ausführt, wenn Sie diese Methode aufrufen. Im Allgemeinen ist es besser, sich auf den automatischen Garbage-Collection-Mechanismus der JVM zu verlassen.

**`System.gc()` und Finalisierung:**

*   **`System.gc()`:** Wie erwähnt, ist dies eine Anfrage an die JVM, den Garbage Collector auszuführen. Es wird oft empfohlen, sich für die kritische Speicherverwaltung nicht auf diese Methode zu verlassen, da die JVM normalerweise besser entscheiden kann, wann sie eine GC durchführen soll.
*   **`finalize()`-Methode:** Bevor ein Objekt vom Garbage Collector eingesammelt wird, gibt ihm die JVM die Möglichkeit, Aufräumarbeiten durchzuführen, indem sie seine `finalize()`-Methode aufruft (falls implementiert). Allerdings hat `finalize()` mehrere Nachteile und wird in der modernen Java-Entwicklung generell nicht empfohlen. Es kann Leistungsprobleme verursachen und die Garbage Collection weniger vorhersehbar machen. Ziehen Sie andere Mechanismen wie try-with-resources für das Ressourcenmanagement in Betracht.

**Auswirkung der Garbage Collection auf die Anwendungsleistung:**

Obwohl Garbage Collection für die Speicherverwaltung unerlässlich ist, kann sie sich auch aufgrund der "Stop-the-World"-Pausen auf die Leistung einer Anwendung auswirken. Während dieser Pausen werden alle Anwendungsthreads angehalten, während der Garbage Collector seine Arbeit verrichtet. Dauer und Häufigkeit dieser Pausen hängen vom verwendeten Garbage-Collection-Algorithmus sowie der Größe und den Eigenschaften des Heaps ab.

Garbage Collector mit niedriger Latenz wie G1, ZGC und Shenandoah zielen darauf ab, diese Pausenzeiten zu minimieren, um Anwendungen reaktionsschneller zu machen.

**Abstimmen der Garbage Collection:**

Für Anwendungen mit spezifischen Leistungsanforderungen kann die Garbage Collection durch Anpassen von JVM-Parametern abgestimmt werden, wie z.B.:

*   Heap-Größe (`-Xms`, `-Xmx`)
*   Young-Generation-Größe (`-Xmn`)
*   Survivor-Verhältnisse (`-XX:SurvivorRatio`)
*   Auswahl eines bestimmten Garbage Collectors (`-XX:+UseG1GC`, `-XX:+UseZGC`, etc.)
*   Setzen von Garbage-Collection-Flags für eine feinere Kontrolle.

Das GC-Tuning ist ein fortgeschrittenes Thema und erfordert in der Regel eine sorgfältige Analyse des Anwendungsverhaltens und der Leistung.

**Beste Praktiken für Garbage-Collector-freundlichen Code:**

Während Java die Speicherverwaltung automatisch handhabt, kann das Schreiben von Code unter Berücksichtigung des Garbage Collectors zu besserer Leistung führen:

*   **Objekt-Erstellung minimieren:** Das Erstellen einer großen Anzahl kurzlebiger Objekte kann den Garbage Collector unter Druck setzen. Versuchen Sie, Objekte bei Bedarf wiederzuverwenden.
*   **Objekt-Referenzen freigeben:** Wenn Sie eine Referenz auf ein Objekt haben, das Sie nicht mehr benötigen, setzen Sie die Referenz auf `null`. Dies macht das Objekt früher für die Garbage Collection berechtigt.
*   **Datenstrukturen weise verwenden:** Wählen Sie Datenstrukturen, die für Ihre Anforderungen geeignet sind. Beispielsweise kann die Verwendung einer großen `ArrayList` und das anschließende Verwerfen der meisten ihrer Elemente ineffizient sein.
*   **Finalizer vermeiden:** Wie bereits erwähnt, sollten Sie sich nicht auf die `finalize()`-Methode zur Ressourcenbereinigung verlassen. Verwenden Sie try-with-resources für Ressourcen wie Dateien und Netzwerkverbindungen.
*   **Achtung bei statischen Variablen:** Objekte, auf die von statischen Variablen verwiesen wird, leben für die gesamte Dauer der Anwendung. Seien Sie daher vorsichtig, wenn Sie große oder unnötige Objekte in statischen Feldern speichern.

**Zusammenfassend:**

Garbage Collection in Java ist ein automatischer Speicherverwaltungsprozess, der den von unbenutzten Objekten belegten Speicher zurückgewinnt. Sie vereinfacht die Entwicklung, indem sie Entwickler von der manuellen Speicherverwaltung befreit. Das Verständnis ihrer Funktionsweise, der verschiedenen Generationen des Heaps und der verfügbaren Garbage-Collection-Algorithmen kann Ihnen helfen, effizientere und leistungsfähigere Java-Anwendungen zu schreiben.