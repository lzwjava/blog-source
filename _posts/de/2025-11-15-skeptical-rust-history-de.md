---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Eine skeptische Geschichte von Rust
translated: true
type: note
---

### Englische Übersetzung & Erklärung des Beitrags  
Titel: „Die Geschichte von Rust, wie ich sie erlebt habe“

Dies ist eine lange, persönliche und sehr kritische Reflexion eines erfahrenen Programmierers (wahrscheinlich taiwanesisch, verfasst auf Chinesisch) über seine frühe Begegnung mit Rust und darüber, warum er der Sprache trotz ihrer aktuellen Popularität technisch wie kulturell tiefgreifend skeptisch gegenübersteht.

#### Frühe Begegnung (2009, Indiana University)
- Während seines Studiums an der Indiana University (IU) hatte der Autor zwei Kommilitonen (Nebenfächler ohne CS-Hauptfach), die in Dan Friedmans fortgeschrittenem Programmiersprachenkurs starke Probleme hatten.
- Diese Kommilitonen waren der Typ, der „große Töne spuckte“, aber die tiefgründigen Konzepte nicht wirklich verstand. Dennoch waren sie gut im Netzwerken und Selbstvermarkten.
- Im Sommer 2009 absolvierten diese beiden Kommilitonen ein Praktikum bei Mozilla Research und arbeiteten an einer frühen Version der Programmiersprache Rust (dies war wahrscheinlich Graydon Hoares persönliches Projekt, das Mozilla später übernahm; die Kommilitonen waren wohl sehr frühe Mitwirkende oder Sommerpraktikanten beim Projekt).
- Am Ende des Sommers hielten sie einen universitären Vortrag, in dem sie Rust allen vorstellten. Dies war die allererste Begegnung des Autors mit der Sprache.

#### Der Vortrag 2009 (der erste Eindruck des Autors)
- Der Vortrag war reines Marketing: große Schlagworte, fast keine technische Substanz.
- Sie zeigten eine Folie mit einem Dreieck und „Rusts drei großen Merkmalen“ – eines war „Sicherheit“, die anderen beiden hat der Autor vergessen.
- Die bahnbrechende Behauptung: Rust würde komplett sichere Speicherverwaltung durch rein statische Analyse ohne jegliche Garbage Collection (überhaupt kein GC) erreichen.
- Der Autor ging mit dem Gedanken hinaus: „Das ist nur Mozilla-Hype. Sie werden niemals einen Browser darin ausliefern. Es wird sterben wie all ihre anderen Forschungsprojekte.“ (Er erwähnt speziell DrServ/DrJS als ein weiteres Mozilla-Forschungsprojekt, das im Nichts endete.)

#### Zweifel am Designer & der Bootstrap-Entscheidung
- Der Autor stellt Graydon Hoares (des ursprünglichen Schöpfers) Tiefe in der Programmiersprachentheorie in Frage.
- Insbesondere hält er die Wahl von OCaml als erste Implementierungssprache für geschmacklos oder als Zeichen mangelnden tiefen Verständnisses (eine kontroverse, aber nicht unübliche Meinung unter einigen PL-Altvorderen, die OCamls Eigenarten nicht mögen).

#### Spätere Entwicklungen
- Einer dieser Kommilitonen startete später ein PhD-Projekt für eine „allgemeine“ GPU-Sprache, die behauptete, man könne Bäume, Graphen usw. auf GPUs aufbauen. Der Autor hielt das für zum Scheitern verurteilt, da GPUs für datenparallele Workloads ausgelegt sind, nicht für beliebige, zeigerlastige Strukturen. Das Projekt wurde in der Tat nie praktisch, aber der Kommilitone promovierte trotzdem und arbeitet jetzt am Rust-Compiler in einem großen Technologieunternehmen.

#### Die eigene Reise des Autors mit Speicherverwaltung
- Der Autor war persönlich fasziniert von der Idee einer 100% statischen Speichersicherheit ohne GC (genau das ursprüngliche Versprechen von Rust).
- Er verbrachte viel Zeit damit, Speichermodelle und statische Analysen zu entwerfen, um diesen Traum zu verwirklichen.
- Eines Tages erzählte er seinem Betreuer Kent Dybvig (dem legendären Autor von Chez Scheme) von der Idee. Kent antwortete ruhig:  
  „Komplett statische Speicherverwaltung – ist das überhaupt möglich? Speicherverwaltung ist inhärent ein dynamischer Prozess.“
- Dieser einzige Satz zerstörte die Illusionen des Autors. Ihm wurde klar, dass präzise Garbage Collection im Allgemeinen unentscheidbar ist (im Zusammenhang mit dem Halteproblem).
- Als er stattdessen Referenzzählung vorschlug, wies Kent darauf hin, dass Referenzzählung hohen Overhead hat und oft schlechter abschneidet als ein guter generationaler GC. Gute GC-Pausen sind kein wirkliches Problem, wenn der Collector gut konstruiert ist (Chez Scheme beweist das).

#### Chez Scheme als Gegenbeispiel
- Der Autor hat großen Respekt vor Kent Dybvig und Chez Scheme:
  - Blitzschnelle Kompilierung
  - Hoch anpassbarer, pausenarmer GC
  - Philosophie: Verschwende keine Zeit mit der Optimierung von dummem Code; gehe von einem kompetenten Programmierer aus; wähle die richtigen, einfachen Abstraktionen.
- Mit anderen Worten: Weisheit > rohe, komplexe Raffinesse.

#### Wie Rust sich tatsächlich entwickelt hat
- Der ursprüngliche Traum von „rein statischer Speicherverwaltung, niemals GC“ ist tot.
- Modernes Rust hat:
  - `Rc<T>` / `Arc<T>` (Referenzzählung mit Zyklen-Sammlung via `Weak`)
  - `unsafe`-Code (obligatorisch für viele Bibliotheken in der echten Welt: Netzwerkstacks, Browser, OS-Kernel, etc.)
  - Laufende Forschung, die Teile von `unsafe` sicherer machen will (Stacked Borrows, Tree Borrows, etc.), aber jedes neue Modell fügt wieder Einschränkungen hinzu.
- Dennoch wiederholen Marketing und Community immer noch das Mantra von „starken statischen Garantien“ und „furchtloser Nebenläufigkeit“.
- Wenn man auf die Lücken hinweist, lautet die offizielle Antwort „das ist einfach Rusts Philosophie“ oder „du verstehst den Borrow Checker nicht“.

#### Die aktuelle Haltung des Autors
- Er versteht Lifetimes, Borrowing etc. vollständig und hat sogar fortgeschrittene Rust-Kurse unterrichtet, in denen Studenten Interpreter für funktionale Sprachen in Rust implementierten.
- Aber je mehr er Rust unterrichtet, desto mehr schätzt er C++:
  - C++ Smart Pointer + RAII sind für viele Aufgaben einfacher und ausdrucksstärker.
  - Wenn man wirklich maximale Performance braucht, würde er immer noch C/C++ gegenüber Rust wählen.
- Er findet Rusts Fehlermeldungen notorisch schwer zu entziffern, und den ständigen Kampf mit dem Borrow Checker nervt.
- Die „Philosophie“-Verteidigung fühlt sich an wie eine religiöse Ausrede für Designkompromisse.

#### Fazit
Der Autor sieht den Erfolg von modernem Rust größtenteils als Triumph des Marketings und des Ökosystem-Schwungs, nicht als Beweis dafür, dass seine Kerngedanken fundamental solider waren als jahrzehntealte Vorarbeit (Region Systems, Cyclone, lineare Typen, hochperformante GCs, etc.). Er glaubt, dass die ursprünglichen großspurigen Behauptungen naiv waren, die Kompromisse unvermeidlich sind und die Community sich jetzt hinter „Philosophie“ versteckt, wenn sie mit den Lücken konfrontiert wird.

Es ist eine seltene Kritik von jemandem mit Insider-Perspektive, der:
1. Rust buchstäblich bei seiner Geburt sah,
2. sich selbst tiefgehend mit Speichersicherheit beschäftigte,
3. Kent Dybvig als Mentor hatte,
4. sich trotz des Hypes im Jahr 2025 immer noch für C/C++ entscheidet.

Ob man zustimmt oder nicht, es ist eine durchdachte Gegenerzählung zur dominanten Geschichte „Rust ist die Zukunft, die bereits angekommen ist“.