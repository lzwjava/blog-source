---
audio: false
generated: false
image: false
lang: de
layout: post
title: Mehrregionale Softwareentwicklung
translated: true
type: post
---

Für internationale Unternehmen gibt es oft Projekte, die Menschen aus mehreren Regionen wie Singapur, Hongkong, UK, USA und China bedienen.

Ich habe an einigen Projekten gearbeitet, die Nutzer aus mehreren Regionen bedienen. Das richtig umzusetzen ist bei Backend-Projekten nicht einfach.

Für die Standard Chartered Bank gibt es Apps wie SC Mobile India und SC Mobile Hongkong. Für McDonald's gibt es Versionen wie McDonald's China und McDonald's USA. Für Starbucks gibt es Starbucks USA und Starbucks China. Im Wesentlichen bieten sie verschiedenen Ländern ihre eigenen Apps an. Oft unterscheiden sich die Anmeldeverfahren für Nutzer in China und internationale Nutzer. Neben der Nutzung von Mobiltelefonen haben chinesische Nutzer oft die Möglichkeit, sich mit WeChat anzumelden, während internationale Nutzer sich mit Facebook, Google oder Apple anmelden können.

Diese Apps nutzen wahrscheinlich unterschiedliche Backend-Server und haben einige unterschiedliche Funktionen, behalten aber dieselbe Designsprache bei. Das ist wahrscheinlich falsch. In den ersten Jahren scheint es einfach oder machbar. Aber nach einem Jahrzehnt werden sie wissen, dass es sehr schmerzhaft ist. Die Wartungskosten oder Synchronisierungskosten, die Testkosten – es gibt tonnenweise doppelte Anstrengungen.

Allerdings ist es für Facebook, Google oder Apple Pay irgendwie einfach. Jemand könnte sagen, sie seien keine Finanz-Apps; sie hätten einige Compliance-Regeln, die eingehalten werden müssen. Das ist nicht wahr. Die Compliance bedeutet oft den Datenbankserver oder die Datenbank oder einige Daten, die Regierungsbehörden überprüfen oder für Prüfungsunternehmen zur Prüfung benötigen wollen. Allerdings sind die anderen Anstrengungen dieselben. Die Software ist sehr flexibel. Wir sollten den Code im selben Repository haben, wir sollten die Datenquellenkonfiguration nutzen, um die Daten verschiedener Regionen zu hosten, und wir sollten denselben Code, dasselbe Design, denselben Workflow und dieselben Tests so weit wie möglich teilen.

Apple Pay ist ein gutes Beispiel dafür. Der App Store ist auch ein gutes Beispiel dafür. Sie bedienen jedes Land.

Es gibt wahrscheinlich einige Projekte in großen Tech-Unternehmen, die Kontinente zur Trennung nutzen, wie Asien und den Pazifik, Nordamerika. Auch dafür.

Das Erste, was man bei der Multi-Region-Entwicklung tun muss, ist zu wissen, was anders ist, welche Compliance man einhalten muss und wie man doppelte Anstrengungen so weit wie möglich reduzieren kann.

Für Text-to-Speech muss Google Cloud verschiedene Sprachen trainieren. Sie bieten verschiedene Modelle und verschiedene Sprachen dafür an. Bei Sprachen sind die Unterschiede zwischen den Sprachen ihre Klänge und ihr Schriftbild. Letzteres bedeutet, dass man bei der PDF-Generierung auf die Schriftauswahl achten muss.

Bei Multi-Region-Projekten kann man in Spring Boot-Projekten Aliase und unterschiedliche Objektinitialisierungen dafür nutzen. Man kann Eigenschaften oder YAML-Konfigurationen intelligent nutzen. Man kann alle unterschiedlichen Logiken basierend auf der Region in bestimmte Module oder Klassen packen.

Und für die Code-Hosting, scheinen unterschiedliche Branches für unterschiedliche Länder zunächst einfach, aber nach einigen Jahren wird man wissen, wie schmerzhaft es ist. Man muss für andere Regionen git cherry-pick machen. Und man muss in einem anderen Branch erneut testen. Bei jeder kleinen Änderung muss man sie in die Branches synchronisieren. Und mit der Zeit, wenn wir uns nicht bemühen, die Code- oder Logikunterschiede zu minimieren, werden die Unterschiede im Code zwischen mehreren Regionen oder Ländern groß genug, um nicht mehr reparierbar zu sein.

Die gute Nachricht ist, dass jetzt KI uns helfen kann, den Code zu refaktorieren oder besser zu schreiben oder die Multi-Region-Code-Design-Probleme zu beheben. Egal wie groß der Fehler ist, wenn wir ihn beheben, ist es ein kleiner Fehler.

Nicht nur für die Codierung, Bereitstellung und Release-Wartung, sondern auch für die Erweiterbarkeit. Man sollte bedenken, wie man ein neues Land oder eine neue Region hinzufügt. Wie viel Aufwand wird das erfordern? Wenn es minimal ist oder nur einige Konfigurationen erfordert, dann ist unser Design großartig. Wenn es einige Monate dauert, ist das auch akzeptabel. Wenn es mehrere Jahre dauert, werden wir es dann immer noch durchführen?

In Yin Wangs Essay, [On Linux, Windows And Mac](https://www.yinwang.org/blog-cn/2013/03/07/linux-windows-mac), erwähnte er, dass ein Adobe-Designer ihm sagte, sie hätten zwei Jahre damit verbracht, Photoshop von Windows auf macOS zu migrieren.

Wird die Unterstützung einer neuen Region zwei Jahre Anpassung erfordern? Bei einigen Projekten könnte das der Fall sein. Das ist eine kritische Designüberlegung.

Die Welt wird immer stärker vernetzt. Egal, welches Land oder welche Region wir zunächst anvisieren, wir müssen auch andere Regionen berücksichtigen. Es ist besser, es von Anfang an richtig zu machen. Für etablierte internationale Unternehmen ist es ratsam, Softwareprodukte für mindestens zwei Länder oder Regionen von Anfang an zu entwickeln. Behalten Sie diese Multi-Region-Mentalität von Anfang an bei. Wenn wir mehr Engineering-Ressourcen haben, können wir mehr Länder oder Regionen unterstützen.