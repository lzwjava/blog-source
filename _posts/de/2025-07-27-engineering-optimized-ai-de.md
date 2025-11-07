---
audio: false
generated: false
image: false
lang: de
layout: post
title: Optimierung der Softwareentwicklung für KI
translated: true
type: post
---

### Inhaltsverzeichnis

1. [Optimierung der Softwareentwicklung für KI](#optimizing-software-engineering-for-ai)
    - Flache Architektur für KI-gesteuerte Entwicklung
    - Vorteile von Python in KI-gesteuerten Workflows
    - Kontext-Engineering und Token-Optimierung
    - Code-Strukturierung für KI-Unterstützung

2. [Erfolg als manueller KI-Agent](#thriving-as-a-manual-ai-agent)
    - Arbeit mit KI-Tools in Unternehmensumgebungen
    - Tool-Auswahl und Kontextmanagement
    - Aufbau wiederverwendbarer Prompt-Systeme

3. [Python für die Java-Entwicklung nutzen](#leveraging-python-for-java-development)
    - Python-Skripte für die Unterstützung von Java-Projekten
    - Strategien für die Entwicklung in mehreren Sprachen
    - KI-gestützte Code-Generierung

4. [Programmiersprachen im Zeitalter der KI](#programming-languages-in-the-ai-era)
    - Zukunft von Python, Rust und Java
    - Performance vs. Einfachheit
    - Sprachentwicklung und KI-Integration

### Optimierung der Softwareentwicklung für KI

In diesem Blog habe ich Hunderte von Skripten genutzt, um bei Übersetzungen, Playgrounds, Frontmatter-Wartung und Telegram-Bots zu unterstützen. Ich glaube, dieser Entwicklungsansatz könnte die Zukunft der für KI optimierten Softwareentwicklung darstellen.

Ich setze nicht stark auf Python-Modulfunktionen, und ich möchte den Code nicht wie ein großes Java-Spring-Projekt strukturieren.

Ich habe im Laufe meiner Karriere an vielen Softwareprojekten gearbeitet. Ich habe beeindruckende Bankarchitekturen, Microservices, effektive mehrländische Designs zur Minimierung von Duplikaten, robuste Grundrahmen auf Basis von Spring und starke Governance mit zentralisierter Konfiguration beobachtet.

Obwohl diese Bankarchitekturen beeindruckend sind, würde ich, wenn wir heute anfangen würden, die Optimierung für LLMs und KI in Betracht ziehen. Dies würde besseres Kontext-Engineering, eine verbesserte Trennung von Verantwortlichkeiten und die Priorisierung von KI-zentriertem Denken gegenüber menschzentriertem Design beinhalten. Obwohl Spring mehrere Ebenen und gute Abstraktion bietet, kann es für LLMs und KI schwierig sein, diese zu navigieren.

Ich glaube, wir sollten flachere Strukturen anstreben, ähnlich einer flachen Organisation. Das bedeutet, nur zwei Ebenen zu verwenden: Die erste Ebene ruft die zweite Ebene auf. In einer Funktion ist es besser, direkt 50 andere Funktionen aufzurufen, anstatt 50 verschachtelte Ebenen oder Stapel zu haben. KI/LLMs haben Schwierigkeiten, übermäßig komplexe, verschachtelte Strukturen zu beurteilen oder abzuleiten, aber sie glänzen bei der Handhabung kleinerer Funktionen mit 100 bis 200 Codezeilen. Python eignet sich gut zum Aufrufen und Importieren aus anderen Dateien.

Ein Grund, warum Python-Code einfacher ist als Java, ist das einfache Abhängigkeitsmanagement. Man muss nur `pip install` verwenden, um eine Abhängigkeit hinzuzufügen. Mit Maven muss man die Abhängigkeit in einer POM-XML-Datei schreiben und dann `mvn compile` ausführen, damit Maven die Abhängigkeiten herunterlädt.

Ein weiterer Grund für die Einfachheit von Python ist, dass der Code direkt ohne Umstände ausgeführt werden kann.

Obwohl ab Java 11 der `java`-Befehl Einzeldatei-Quellcode-Programme direkt ausführen kann, ohne sie separat mit `javac` kompilieren zu müssen, sind Java-Projekte oft groß, sodass man sie mit `mvn spring-boot:run` zusammen mit einigen Eigenschaftskonfigurationen ausführen muss.

Ein dritter Grund ist, dass das Modul-Design von Python einfach ist; man kann `from` und `import` verwenden, um Code einfach aus anderen Dateien zu importieren.

Derzeit können viele KI-Chatbots Python-Code direkt im Chatbot-Fenster ausführen, wie z. B. Grok.

Beim Vergleich von 100 Java-Dateien, jeweils mit etwa 1000 Codezeilen, mit einigen einfachen Python-Skripten ist das kein fairer Vergleich. Für dieses Projekt würde ich 1000 Python-Dateien bevorzugen, jeweils mit etwa 100 Codezeilen.

Es ist akzeptabel, Codezeilen oder eine Funktion zur Bearbeitung auszuwählen. Man muss jedoch wissen, wo man auswählen soll. Warum nicht diese Aufgabe von der KI erledigen lassen, um unser Leben einfacher zu machen? Wir müssen also nur "Alles auswählen" verwenden, um den gesamten Code auszuwählen und der KI/LLM mitzuteilen, wie er bearbeitet werden soll.

Für Python ist es einfacher, `if __name__ == "__main__":` zu verwenden, um Funktionen in einer Datei auszuführen und zu testen. Es ist auch einfacher für andere Python-Dateien, die Funktionen in dieser Datei aufzurufen, ohne die Tests ausführen zu müssen.

Das ist Kontext-Engineering, das für KI optimiert ist. Könnten wir es auf andere Weise angehen? KI/LLM ist autoregressiv. Wenn wir jedoch Copilot oder Claude Code verwenden, wissen wir nicht, wie das KI-Software-Agent uns hilft. Sie sollten darüber nachdenken, anstatt wir es zu tun.

Könnten wir auf der Benutzerseite den Code speziell anordnen, um den Token-Verbrauch zu reduzieren? An diesem Punkt ist der Ansatz mit 1000 Python-Dateien mit jeweils 100 Codezeilen gut für diesen Zweck. Denn Sie können Funktionen und Code-Dateien leicht überprüfen, bevor Sie andere Python-Code sie aufrufen lassen.

Aber ein Problem besteht darin, dass es nicht einfach ist, mehrere Code-Dateien gleichzeitig zu ändern. Auf einfache Weise können Sie den Code in KI-Chatbots kopieren und sie können Ihnen mitteilen, wie Sie den Code in diesen Dateien bearbeiten sollen.

Möglicherweise müssen wir nicht die Anzahl der Zeilen verwenden, um Funktionen oder Logik zu trennen. Aber wir sollten dies tun, um die Logik in kleine Funktionen zu trennen. Wir können dies tun, indem wir sie natürlich nach Art der Logik trennen, sodass sie kürzer erscheinen.

Warum wollen wir Software-Engineering, das für KI optimiert ist? Weil KI mächtig ist, sollten wir alles für KI optimieren und dann die KI die Software-Engineering so weit wie möglich unterstützen lassen.

Es ist nicht nur für Code möglich, sondern auch für jeden Text. Angenommen, wir sind sehr wählerische Redakteure; wir wollen nicht, dass KI unsere großen Texte auf einmal bearbeitet. Wir wollen Absatz für Absatz überprüfen. Bei Code können wir kleinere Fehler oder Bugs tolerieren. Bei Text können wir sie tolerieren, weil die meisten Leser nicht so wählerisch sind.

Aber Code ist anders, weil manchmal sogar ein kleiner Fehler zum vollständigen Ausfall eines großen Projekts führen kann.

Für XML- oder YAML-Dateien müssen wir sie wahrscheinlich nicht so stark trennen, weil sie bereits hoch strukturiert sind.

Und für HTML-Dateien sollten wir eine Trennung vornehmen. Statt Hunderte von JavaScript-Dateien zusammen mit Hunderte von HTML-Dateien zu schreiben, was es einfach macht, 1000 Codezeilen zu überschreiten, sollten wir `import` für JavaScript verwenden, um dies zu verwalten. Für JavaScript-Code können wir die oben genannten Methoden zur Trennung verwenden.

Wir wollen den Code so strukturieren, dass KI uns leicht helfen kann, Code hinzuzufügen, zu bearbeiten, zu löschen und auszuführen. Das ist der Anfang. Stellen Sie sich einen Tag vor, an dem der gesamte Code von KI leicht generiert oder repariert werden kann. Die Welt wird hochgradig digitalisiert sein.

Stellen Sie sich vor, ich schreibe 100 große Softwareprojekte und biete APIs zum Verbinden mit anderen an. Dazu gehört auch mein täglicher Kalender; ich bin heute wie ein Technologieunternehmen mit 1000 Mitarbeitern. Sie sind auf meine Bedürfnisse zugeschnitten, um Geld zu verdienen oder Geld für meinen Nutzen auszugeben. Das ist wirklich erstaunlich.

### Erfolg als manueller KI-Agent

KI-Agenten sollten automatisch mit Code ausgeführt werden. Jetzt lautet der Titel dieses Essays "Manueller KI-Agent". Sie könnten denken, ich mache Witze, aber das tue ich nicht.

Der Grund, warum ich "manueller KI-Agent" sage, ist, dass in großen Unternehmen die Technologieadoption aufgrund von Sicherheitsdatenbedenken und langfristigen Überlegungen langsam ist.

Es gibt viele neue Technologien auf dem Markt; wer weiß, was bleibt und was schnell verschwindet.

Sie haben auch Sicherheitsdatenbedenken. Typischerweise wollen sie mit großen Marken zusammenarbeiten, deren Datenschutzrichtlinien streng sind und von der Öffentlichkeit überwacht werden. Das erklärt, warum Microsoft zu einem Top-Partner unter den Fortune-500-Unternehmen geworden ist. Andere Unternehmen nutzen ihre Teams, Microsoft Office 365, Azure und Copilot.

Aber was, wenn große Unternehmen ihren Mitarbeitern keine LLM-APIs zur Verfügung stellen, um sie zu nutzen? Wir müssen darüber nachdenken, wie wir als manuelle KI-Agenten arbeiten können.

Das bedeutet, dass wir viele Tools verwenden werden, um zu arbeiten, ähnlich wie die Toolnutzung oder Funktionsaufrufe in diesen APIs. Wir werden unser eigenes Prompt-Engineering oder Kontext-Engineering durchführen.

Anstatt Claude Code oder Manus für eine komplexe Aufgabe zu verwenden, können wir die Aufgaben selbst mit einem einfachen KI-Chatbot durchführen.

AspectJ ist gut, weil es AOP-Programmierung zur Interzeption von Methoden verwendet. Filter in Spring sind auch gut, um die Protokolle von HTTP-Anfragen zu erfassen. Der Logger in Log4j ist gut, um bestimmte Protokolle in eine Datei umzuleiten. IntelliJ IDEA ist gut, weil es eine Funktion zum Exportieren von Objekten als Text hat.

SQL-Clients sind gut, weil sie leicht CSV- oder Excel-Dateien von Zeilen exportieren können. Git diff ist gut, weil es Ihnen Vergleichstexte geben kann.

Sie alle helfen Ihnen, bessere Kontexte für KI-Chatbots bereitzustellen. Und KI-Chatbots können auch vielen Python-Skripten helfen, Aufgaben auszuführen.

Um ein effektiver KI-Agent zu sein, müssen Sie viele effektive Tools verwenden, um Ihnen bei der Durchführung von Aufgaben zu helfen, ob einfach oder komplex.

Ohne APIs für LLM/KI-Chatbots müssen Sie Text in die Chatbots kopieren. Es ist etwas umständlicher, als die KI direkt aufzurufen, aber die gute Nachricht ist, dass Sie Kontexte oder Prompts sorgfältiger auswählen können.

Sie müssen KI-Chatbots also nicht so oft fragen wie automatische KI-Agenten. Sie können die Tools sorgfältig auswählen, die Sie verwenden werden.

Das Arbeiten wie ein manueller KI-Agent hat also seine Vorteile. Allerdings entwickelt sich die KI-Agententechnologie schnell und zeigt ihr Potenzial der Welt.

Wenn sie sehr nützlich sind, werden große Unternehmen sie genauso übernehmen wie KI-Chatbots. Andernfalls können sie nicht mit anderen Unternehmen konkurrieren, die sie übernommen haben – nicht nur mit anderen großen Unternehmen, sondern auch mit kleinen Startups. Denn KI ist jetzt so mächtig, dass ein Startup mit zehn Mitarbeitern Unternehmen mit 1.000 Mitarbeitern schlagen kann.

Das Arbeiten als manuelle KI-Agenten ist manchmal unvermeidbar. Der Job hat neben dem Fehlen fortgeschrittener KI-Technologie andere Vorteile. Es ist nicht einfach, gute Jobs zu finden. In diesem Fall gibt uns das Raum, unsere traditionelle Weisheit zu nutzen, um das Beste aus KI-Chatbots zu machen.

Und es bedeutet, dass wir unsere Prompts organisieren und ansammeln können, um Systemprompts für KI-Chatbots zu erstellen, ähnlich wie die von Claude oder Grok, die öffentlich zugänglich sind. Auf diese Weise müssen wir Prompts nicht wiederholt schreiben. Wir können Python-Skripte verwenden, um uns beim Schreiben von Prompts zu unterstützen. Wir können die Protokolle von HTTP-Anfragen erhalten und Prompts schreiben, um API-Testfälle zu generieren.

Die Magie des Programmierens liegt in seinen unbegrenzten Abstraktionsstufen. Es ist ähnlich wie Funktionen, bei denen Sie 100 Ebenen von Funktionsaufrufen haben können. Zum Beispiel ist WeChat auf iOS aufgebaut, und WeChat-Mini-Programme sind auf WeChat aufgebaut. iOS selbst ist auf Objective-C oder Swift aufgebaut, die wiederum auf LLVM und dem Befehlssatz der ARM-Chips von Apple aufgebaut sind.

### Python für die Java-Entwicklung nutzen

Wie kann man Python nutzen, um die Java-Entwicklung im Zeitalter der KI zu unterstützen? Ich mag Python. Ich habe in den letzten etwa drei Jahren am meisten mit Python gearbeitet, seit ChatGPT Ende November 2022 veröffentlicht wurde.

Eine Möglichkeit der Unterstützung besteht darin, Python zu verwenden, um SQL-Hilfsskripte, Testskripte und Log-Suchskripte für Java-Projekte zu schreiben.

Verwenden Sie Python, um POM-Dateien und Paketabhängigkeiten für Java zu analysieren. Verwenden Sie Python, um die Datenkonsistenz in Java zu überprüfen. Es gibt viele Dinge, die wir in Python anstelle von Java tun können.

Aber Java hat kein PyTorch. Python kann alles in 200 Codezeilen helfen, was in Java 500 Zeilen erfordern würde. Aber durch die Verwendung von KI-Tools können Sie auch nicht leicht Ihre eigene Version von PyTorch erhalten. Selbst etwas wie TinyGrad benötigt Zeit zum Aufbau.

Warum unsere eigenen Skripte zuerst schreiben? Ein Grund ist, dass sie super anpassbar sind. Es gibt keine öffentlichen Software oder Open-Source-Projekte, die uns direkt in unseren Projekten helfen können, insbesondere in großen Unternehmen.

Die großen Projekte in großen Unternehmen werden über ein Jahrzehnt oder länger entwickelt. Sie haben bereits viele Anpassungen.

Daher wird es in Zukunft viele umliegende Projekte um die großen Projekte in großen Unternehmen geben. Es wird mehr Claude-ähnliche Code-Router in internen Coding-Agent-Tools in großen Unternehmen geben. Es wird mehr angepasste Postman-, SQL-Clients und Compiler für große Unternehmen geben.

Python-Code kann auch mit Java-Agenten verbunden werden.

Das bedeutet, dass ich Python und Java gut lernen muss, damit ich weiß, wie ich eines nutzen kann, um das andere zu unterstützen.

Und ich kann Python mit der Hilfe von KI verwenden, um viele Dinge für mich selbst und in Unternehmensprojekten zu erstellen. Java scheint kein Hindernis zu sein. Java mit Spring, Datenbanken und mit Angular, Vue oder React als Frontend sollte kein Hindernis für Python sein, viel zu helfen.

Programmieren ist so etwas Flexibles. Die Grenze ist unsere Vorstellungskraft.

Daher wächst KI schnell. Wir können den Fortschritt der KI daran messen, wie viel und wie leicht wir Code verwenden können, um Dinge mit der Hilfe der KI beim Codieren und Lernen zu erreichen.

Könnten wir eines Tages einige KI-Agenten schreiben, und dann helfen diese Agenten, ein ganzes TikTok zu erstellen, einschließlich seiner vielen Microservices und großen iOS- oder Android-Projekte?

Wenn KI so mächtig ist, was sollten wir heute tun? Wahrscheinlich nichts, denn was wir heute tun, wird leicht mit KI umzusetzen sein. Im Jahr 2025 wird unsere einjährige Arbeit mit der Hilfe der KI wahrscheinlich in einem Monat mit der KI-Fähigkeit von 2030 erledigt sein.

Das wirft unsere grundlegende Frage auf: Was ist unser Lebenszweck? Worum geht es überhaupt? Wie lebt man ein gutes Leben?

KI kommt wie andere Technologien, um uns Freiheit zu bringen. Aber es scheint, als ob jeder wie eine Maschine in dieser kapitalistischen Gesellschaft beschäftigt ist.

Zurück zum Thema. Also kann Python auch Java-Code schreiben. Sie können Python verwenden, um den Kontext für das Schreiben von Code zu erhalten und Copilot es für Sie schreiben lassen, um es beim ersten Versuch richtig zu machen.

KI geht um Prompt-Engineering und Kontext-Engineering. Prompts und Kontext helfen den Antworten von KI-Chatbots.

Python kann beim Kontext helfen; Python kann Prompts generieren.

Daher geht es nicht nur um Java, sondern um jede andere Programmiersprache. Python kann ihnen tief helfen. Warum brauchen wir also immer noch andere Programmiersprachen?

Es ist das inhärente Design von Python, das es im Vergleich zu anderen Programmiersprachen wie C, C++ oder Rust schlechter performen lässt.

### Programmiersprachen im Zeitalter der KI

KI ist jetzt so mächtig, dass wir alles aus der Perspektive der KI neu überdenken müssen. Welche Programmiersprachen werden in den nächsten 10 Jahren beliebt sein?

Python wird sicherlich beliebt sein. Viele KI-Chatbots verwenden Python, um Code im Browser auszuführen, wie z. B. Grok. Python ist beliebt für seine Einfachheit, Leichtigkeit des Lernens und annehmbare Performance. Es wird von vielen Softwareprojekten übernommen.

Python ist langsamer als C++, Java und Rust. Java hat eine große Community. Rust ist auf C aufgebaut.

Ich frage mich, ob viele Projekte in Rust neu geschrieben oder ersetzt werden. Neu geschrieben bedeutet, sich auf ein altes Projekt zu beziehen und Rust verwenden, um dieselbe Funktionalität zu implementieren. Ersetzt bedeutet, dass Software, die in anderen Sprachen geschrieben ist, jetzt durch ähnliche Software ersetzt wird, die in Rust geschrieben ist.

Rust hat eine relativ komplexe Syntax. Aber im Zeitalter der KI ist das kein großes Problem, weil KI beim Schreiben von Code hilft. Bei komplexer Syntax haben Menschen auch nicht viel Schwierigkeiten.

Ich denke, Hindi oder Tamil sind ziemlich komplex. Aber für Inder, die im Norden leben, ist Hindi kein Problem, und für diejenigen im Süden ist Tamil kein Problem.

Aber für einen chinesischen Staatsbürger wie mich ist es ein großes Problem, es zu lernen.

Auf den ersten Blick sehen alle Zeichen in Hindi für mich ähnlich aus. Ich denke, der Unterschied zwischen Hindi und Arabisch ist wie der Unterschied zwischen Chinesisch und Japanisch oder Englisch und Spanisch.

Die Unterschiede zwischen Programmiersprachen sind geringer als die zwischen natürlichen Sprachen. Ein großer Grund dafür ist, dass sich Programmiersprachen nur in der Zeichenerscheinung unterscheiden, während natürliche Sprachen auch im Klang unterschiedlich sind. Natürliche Sprachen unterscheiden sich in zwei Aspekten: Zeichensatz und Aussprache.

Programmiersprachen haben nur etwa ein Jahrhundert Geschichte, aber natürliche Sprachen haben mehr als 100 Jahrhunderte. Je mehr Zeit Menschen mit etwas verbringen, desto mehr Unterschiede entwickeln sich. Menschen mit leicht unterschiedlichen Meinungen werden ihre eigenen Versionen von Dingen schaffen.

Das erklärt den englischen Akzent. In einigen TikTok-Videos sagen die Leute, dass der schlechteste englische Akzent Birmingham ist.

Tatsächlich hat Rust also nicht viele Probleme. Seine Performance ist ziemlich gut, da er auf C/C++ aufgebaut ist.

Performance ist für viele Anwendungen entscheidend. Heutzutage werden viele Apps von Milliarden von Menschen verwendet. Für die zugrunde liegende Cloud-Computing-Infrastruktur werden ihre Dienste viele Male aufgerufen. Daher kann selbst eine kleine Leistungssteigerung viel Geld sparen.

Hat Rust viele Nachteile? Eine Sache, über die sich Leute beschweren, ist, dass es schwer zu lernen ist. Die Lernkurve ist steil. KI bringt gute Nachrichten, da sie beim Lernen sehr hilft.

Ich muss nicht viel über Rust wissen. Als Software-Ingenieur mit 10 Jahren Erfahrung kann ich KI verwenden, um viele einfache Rust-Anwendungen zu schreiben. Ich muss nur die grundlegenden Rust-Kompilierungsbefehle wie `cargo` und `cargo build` kennen. Ich muss nicht einmal viel über die Rust-Syntax selbst wissen.

Bei Rust verursacht das Mutability- oder Borrow-Modell für mich keine Probleme. Für einfache Anwendungen mit weniger als 200 Codezeilen kann ich KI bitten, Fehler direkt durch Bereitstellung von Fehlermeldungen zu beheben.

Aber warum wird Python immer noch viel verwendet, wenn Rust so gut ist? Weil Python in einem anderen Aspekt gut ist. Es ist sehr einfach zu verwenden und zu lernen. Es hat eine große Community und viele Bibliotheken.

Python hat immer noch eine gute genug Performance und kann Produkte für Millionen, sogar Dutzende von Millionen von Nutzern unterstützen. Die meisten Produkte haben nicht so viele Nutzer. Wenn Sie so viele Nutzer haben, können Sie Rust- oder Java-Programmierer einstellen, um die Performance zu optimieren.

Python ist gut für viele Entwicklungen: maschinelles Lernen, Webentwicklung, Mathematik, Lehre und Skripting. Während Python nicht gut für Desktop-Anwendungen ist, wird MicroPython in Raspberry Pi verwendet.

Was ist mit Java im Zeitalter der KI? Es wird auch gut sein, da es eine große Nutzerbasis und Community hat. KI hilft dabei sehr. Es wird von vielen großen Unternehmen verwendet. Sie neigen dazu, ihre Hauptprogrammiersprachen nicht zu ändern. Für einige ihrer großen Legacy-Projekte würde das Neu schreiben eines Projekts in einer neuen Programmiersprache ein Jahrzehnt an Aufwand erfordern. KI wird dabei helfen, aber der Prozess wird immer noch langsam sein.

Oft werden rationale Menschen in großen Unternehmen nicht in Betracht ziehen, ihre Hauptprogrammiersprache zu ändern. Ihr Hauptgeschäft liegt in anderen Sektoren. Sie kümmern sich nicht viel um Technologie. Wenn sie es täten, würden sie Software- oder Internetunternehmen werden und in Open-Source-Communities führen. Allerdings kümmern sich nicht viele Fortune-500-Unternehmen darum.

Es wird viele Startups aufgrund von KI geben. Startups mögen es, Neues zu tun, also werden sie neue Programmiersprachen ausprobieren. Im Zeitalter der KI werden agile Programmiersprachen in kleinen und mittleren Unternehmen gewinnen.

Wird sich die bevorzugte Programmiersprache in Algorithmuswettbewerben ändern? C++ hat diesen Sektor seit Jahrzehnten dominiert. In tatsächlichen Algorithmuswettbewerben können Sie keine KI verwenden. Aber ich denke, dass in der Ära der KI weniger Menschen teilnehmen werden.

Da diese Menschen sehr gut im Programmieren sind und es so viele Möglichkeiten aufgrund der KI gibt, warum sollten nicht mehr Menschen echte Produkte für Benutzer erstellen, anstatt Algorithmusprobleme zu üben? Selbst der GOAT der Algorithmuswettbewerbe, Gennady Korotkevich, hat sich entschieden, Devin beizutreten.

Aber Algorithmuswettbewerbe können ein entspannendes oder Ruhestands-Hobby für intelligente Programmierer sein. Es ist wie Schach oder Basketball. Menschen tun es, weil sie es mögen oder es brauchen, nicht aus anderen Gründen. Viele Menschen spielen Basketball in ihren 30ern oder 40ern. Sie tun es wahrscheinlich aus gesundheitlichen Gründen oder um das Leben unterhaltsamer zu machen.

Für iOS und Android ist es Java, Kotlin, Swift und Objective-C. Es wird aufgrund von KI keine signifikanten Änderungen geben, weil es begrenzte Optionen gibt. Auf der Endbenutzerseite sind die Leistungsanforderungen nicht so hoch. Google und Apple haben sehr hohe Kontrolle über ihre Plattformen. Wenn Google und Apple sich nicht ändern, werden Programmierer sich nicht ändern.

Aber für Server gibt es viele Optionen. Sprachen, die KI-freundlicher sind, werden gewinnen.

Prozedurale Programmiersprachen werden mehr gewinnen als objektorientierte Sprachen. Prozedurale Sprachen sind direkt und einfach von KI zu generieren, während OOP-Sprachen viele verschachtelte Ebenen oder Designmuster haben.

Wird es aufgrund von KI mehr Programmiersprachen geben? Ich denke schon. Zed und OCaml werden mehr Nutzer haben. LLMs/KI sind sehr gut im Erlernen von Mustern, sodass es einfach ist, Projekte in anderen Sprachen neu zu schreiben.

Programmiersprachen werden in Zukunft mehr Konkurrenz erleben. Diejenigen, die gut in Performance, Syntax und Compilerqualität sind, werden von Natur aus beliebter werden. Der Wettbewerb ist ähnlich wie bei LLMs. Diejenigen, die von Natur aus gut sind, wie Claude und DeepSeek, werden beliebt.

Was, wenn KI so mächtig wird, dass wir Programmieren nicht mehr lernen müssen? Das ist noch ein langer Weg entfernt. Angenommen, wir haben ein sehr großes Projekt mit 1.000 Java-Dateien. KI würde wahrscheinlich 10 Jahre brauchen, um diese Aufgaben leicht auszuführen.