---
audio: false
generated: true
lang: de
layout: post
title: Große Sprachmodelle bestätigen meine CFA-Erkenntnisse
translated: true
type: note
---

https://weibo.com/6347862377/5183994120372979

https://substack.com/inbox/post/167355695

---

Wie ich bereits in meinem vorherigen Weibo-Post erwähnt habe, nutze ich gerne LLMs, um komplexe, mühsame Dinge zu erledigen, die ich nicht gerne mache oder lese. Dazu gehören viele akademische Arbeiten.

Mehr als ein Jahrzehnt nachdem ich PySonar2 (einen Python-Typinferenz- und Statikanalysator) in den Jahren 2009-2010 erstellt hatte, fand ich mich in einer Diskussion über Control-Flow-Analyse (CFA) mit ChatGPT wieder, was Erinnerungen an eine Debatte wachrief, die ich vor zehn Jahren mit einem bestimmten "CFA-Studenten" hatte.

https://www.yinwang.org/blog-cn/2016/04/07/cfa

(Die Screenshots, die ich damals auf eine Website hochgeladen hatte, sind jetzt verschwunden. Nehmt einfach das, was übrig ist.)

Es ist ziemlich interessant – Dinge, die ich vor über einem Jahrzehnt klar erkannt hatte, wurden nun von ChatGPT "bestätigt".

Vor fünfzehn Jahren, als PySonar2 zum ersten Mal erstellt wurde, hatte es bereits die gesamte akademische CFA-Forschung der damaligen Zeit (einschließlich der neuesten CFA2) übertroffen. Für eine quasi-funktionale Sprache wie Python mit Lambda-Closures war es das erste Mal, dass eine so präzise Typinferenz erreicht wurde. Es war nicht nur äußerst genau, sondern seine Leistung war auch gut genug, um alle großen Python-Projekte auf GitHub zu analysieren.

Der Gründer von Sourcegraph, der größte Nutzer von PySonar2, erzählte mir damals, dass die Analyse von PySonar2 überraschend präzise sei. Damals dachte ich mir nicht viel dabei, weil mein Ansatz so einfach war, dass ich annahm, jeder hätte darauf kommen können. Erst als ich feststellte, dass niemand anderes es zuvor geschafft hatte, dachte ich, dass ich vielleicht seinen Wert hervorheben sollte.

Selbst jetzt kann JetBrains' PyCharm IDE keine so präzise Analyse oder "Definition finden"-Funktionalität erreichen. Wenn man beispielsweise eine globale Variable definiert, die initial mit None belegt wird und ihr später in einer "Initialisierungsfunktion" eine Struktur zuweist, kann man die Mitglieder dieser Struktur nicht finden. Ich sage nicht, dass man solch schlechten Code schreiben sollte, aber dies ist ein Beispiel.

Wenn ihr wüsstet, was ich an der Indiana University geleistet habe, würdet ihr verstehen, dass PySonar2 für mich wirklich keine große Sache war – es erforderte nur einen winzigen Teil meiner Anstrengung. Damals kümmerte ich mich nicht sonderlich um die Python-Sprache. Und diese CFA-Papiere waren so obskur, dass ich kein Interesse hatte, mich in sie zu vertiefen. Ich überflog sie nur und konnte erkennen, dass sie größtenteils Unsinn waren. Also baute ich PySonar2 in ein paar Monaten, ließ andere es frei nutzen und machte mir nicht die Mühe, ein Papier zu schreiben. Ich konnte seine Prinzipien in nur wenigen Sätzen erklären.

Ich war zu bescheiden. Seht euch all diese CFA-, k-CFA-, CFA2-Papiere an – ein Haufen davon, und doch konnten sie keine realen Probleme lösen und wurden nie praktisch eingesetzt. k-CFA hatte sogar ein grundlegendes Problem, bei dem "Aufrufe und Rückgaben nicht übereinstimmen" – etwas, von dem ich nie gedacht hätte, dass es passieren könnte. PySonar2 hatte dieses Problem nie. Wie kann jemand ein so törichtes Design machen, ein Papier darüber veröffentlichen und Nachfolger haben, die es weiter "verbessern"?

Matt Mights CFA2 führte einen "Pushdown-Automaten" ein, was nur eine Methode war, um den Funktionsaufruf-Stack aus den fehlerhaften Designs früherer Arbeiten wiederherzustellen. PySonar2 hatte immer schon einen "Pushdown-Automaten", weil sich bei der Interpretation von Funktionsaufrufen natürlich ein Stack ergibt.

Matt Might hatte einen Blog, in dem er stolz erklärte, wie die "automatische CPS-Transformation" zustande kam, als ob er der Einzige wäre, der sie versteht. Aber seine Ideen entwickelten sich eindeutig aus übermäßig komplexen CPS-Papieren und waren nicht das Ergebnis unabhängigen Denkens; sie trugen viel historischen Ballast mit sich. Seine Schreibweise klingt oft tiefgründig, ist aber schwer zu folgen – könnt ihr sie tatsächlich verstehen? Seine Ideen können sich nicht mit meinem "40 Zeilen Code"-Ansatz messen. Ich musste lachen, als ich seinen Blog las, aber aus Höflichkeit und "Bescheidenheit" schwieg ich. Ich denke, Matt Might fehlt es an wirklicher Substanz, und diese Gruppe von Leuten schwafelte nur Unsinn. Das ist die Wahrheit, die ich nach all den Jahren nun preisgeben kann.

Produzieren diese Papiere nicht einfach Kauderwelsch? Ja, das wusste ich schon vor über einem Jahrzehnt. Aber wer konnte damals verstehen, was vor sich ging? Jetzt könnt ihr es mit ChatGPT überprüfen :)

Tatsächlich hat ChatGPT auch etwas anderes bestätigt: Die Verwendung von CPS in Olin Shivers' grundlegendem CFA-Papier war die Wurzel allen Übels:

PySonar2 wurde vollständig unabhängig gebaut, ohne Bezugnahme auf akademische Arbeiten. Es ging das Grundproblem direkt an, ohne akademischen Ballast. Das ist der Wert einfachen Denkens. Dies war nicht das erste Mal, dass ich sowohl die akademische Welt als auch die Industrie mit einem so scharfen Ergebnis unabhängig übertroffen habe.

Nachdem ich PySonar2 erstellt hatte, verbrachte ein Google-Team über zwei Jahre damit, zu versuchen, etwas Besseres zu bauen, aber sie scheiterten, und Google musste weiterhin meinen verbesserten Open-Source-Code verwenden. Warum? Weil ihre Strategie von Anfang an falsch war. Sie wollten eine logische Programmiersprache wie Prolog für die Typinferenz von Python verwenden, und ich wusste sofort, dass dies zum Scheitern verurteilt war. Woher wusste ich das? Weil ich diese Methoden bereits implementiert und die Grenzen des Hindley-Milner-Systems und von Prolog verstanden hatte. Woher wusste ich das? Weil ich an der IU logische Programmiersprachen implementiert und verbessert hatte.

Ich muss ChatGPT dafür danken, dass es die Fakten, die ich sah, klar artikuliert hat und mir so das Lesen dieser obskuren Papiere erspart hat. Ich bin dankbar für seine Bestätigung des Werts meiner Ideen. Ich glaube, dass LLMs einen großen Beitrag zum menschlichen Fortschritt leisten werden.

Nun teile ich eine Unterhaltung, die ich mit ChatGPT über CFA hatte, in der Hoffnung, dass sie Forschern auf diesem Gebiet hilft:

https://chatgpt.com/share/6864e9a1-66c8-8002-b9f5-55e845fde7ae