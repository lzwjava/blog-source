---
audio: false
generated: true
lang: de
layout: post
title: Aufbau und Test einer JK-Flipflop-Schaltung
translated: true
type: note
---

In einem vorherigen Video haben wir das JK-Flipflop und seine Funktionsweise untersucht und festgestellt, dass es dem SR-Flipflop ähnelt, jedoch mit einem zusätzlichen Rückkopplungsmechanismus. Diese Rückkopplung ermöglicht es dem Ausgang, bei einem steigenden Taktflankenimpuls zu kippen, wenn beide Eingänge hoch sind, anstatt in einen undefinierten Zustand zu geraten. In diesem Video möchte ich seine praktische Funktionalität aufbauen und beobachten.

Ich habe ein JK-Flipflop gemäß dem bereitgestellten Schaltplan aufgebaut. Während des Aufbaus ist mir ein Beschriftungsfehler in der Schaltung aufgefallen: Dies ist tatsächlich der K-Eingang, und dies ist der J-Eingang. J entspricht dem Setzen, was bedeutet, dass der Q-Ausgang ebenfalls hoch gehen sollte, wenn J hoch geht. Umgekehrt entspricht K dem Rücksetzen, sodass der Q-Ausgang niedrig gehen sollte, wenn K hoch geht. Abgesehen von dieser kleinen Korrektur in der Beschriftung ist der Rest der Schaltung korrekt.

Für die NOR-Gatter verwende ich den 74LS02-Chip, speziell die beiden NOR-Gatter auf seiner Oberseite. Der andere Chip, der 74LS11, ist ein dreifaches 3-Eingang-UND-Gatter. Ich verwende zwei dieser drei Eingänge für die Schaltung.

Nach dem Einschalten der Stromversorgung stellt sich die Schaltung in einen Zustand ein, wobei der Q-Ausgang scheinbar "ein" ist. Dann habe ich meine Taktschaltung angeschlossen. Die beiden Schalter, die Sie sehen, sind über Pull-Down-Widerstände auf Low-Pegel gezogen; das Drücken eines Knopfes lässt den Eingang hoch gehen. Diese Schalter sind mit grünen Drähten mit den beiden UND-Gattern verbunden und dienen als die K- und J-Eingänge.

Das Taktsignal speist ebenfalls die UND-Gatter. Es durchläuft eine RC-Schaltung, bestehend aus einem 0,0001-Mikrofarad-Kondensator und einem 1000-Ohm-Widerstand. Die Ausgabe dieser RC-Schaltung, übertragen durch zwei weiße Drähte, geht zu einem weiteren Eingang an beiden UND-Gattern. Die Ausgänge dieser UND-Gatter werden durch blaue Drähte dargestellt, die mit zwei der Eingänge der NOR-Gatter verbunden sind. Die anderen Eingänge der NOR-Gatter erhalten über gelbe Drähte eine Rückkopplung von ihren eigenen Ausgängen. Diese gelben Drähte führen ebenfalls zurück zu den UND-Gattern. Schließlich treiben die NOR-Gatter-Ausgänge zwei LEDs an: eine für Q und eine für Q Komplement.

Wenn der K-Eingang auf hoch gesetzt wird, sollte die Kippstufe zurückgesetzt werden und der Q-Ausgang sollte ausgehen, was auch geschieht. Ebenso sollte das Setzen des J-Eingangs auf hoch die Kippstufe setzen und den Q-Ausgang einschalten, was ebenfalls funktioniert. Wichtig ist, zu beobachten, dass die Änderung nicht sofort beim Drücken des Knopfes erfolgt; sie geschieht mit dem nächsten Taktimpuls, da dieser Vorgang durch die steigende Taktflanke getaktet wird.

Nun, da es sich um ein JK-Flipflop handelt, sollten wir erwarten, dass der Ausgang mit jedem Taktimpuls kippt, wenn sowohl J- als auch K-Eingänge auf hoch gesetzt sind. Allerdings kippt er nicht konsistent. Manchmal tut er es, besonders wenn ich die Schaltung leicht manipuliere, aber es ist sehr unbeständig. Um sicherzustellen, dass ich beide Knöpfe drücke, werde ich Jumper darüber setzen, was effektiv einen kontinuierlichen High-Pegel an sowohl J als auch K liefert. Dies *sollte* dazu führen, dass es bei jeder steigenden Taktflanke kippt. Während es jetzt besser funktioniert, ist es immer noch unbeständig.

Dieses inkonsistente Verhalten hat eine klare Erklärung, und der beste Weg, es zu verstehen, ist die Verwendung eines Oszilloskops, um die Signale zu untersuchen.

Schauen wir uns zunächst den Takteingang als Referenz an. Das Oszilloskop zeigt das Taktsignal, das ein- und ausschaltet, ungefähr zweimal pro Sekunde. Jede Teilung auf dem Oszilloskop repräsentiert 100 Millisekunden, also pulst es über 10 Teilungen zweimal pro Sekunde.

Als nächstes möchte ich den Ausgang beobachten, da wir erwarten, dass dieser mit jedem Taktimpuls kippt. Der Takt pulst tatsächlich mit etwa zwei Pulsen pro Sekunde. Derzeit kippt der Ausgang nicht, aber mit einer leichten Anpassung kippt er, wenn auch inkonsistent. Wenn er *kippt*, tut er dies bei den steigenden Flanken des Takts, wie gewünscht.

Der interessante Teil zeigt sich, wenn wir in die steigende Flanke des Takts hineinzoomen. Wir sehen dort einige Aktivitäten. Beim weiteren Hineinzoomen wird es ganz klar: Wenn der Takt hoch geht, *kippt* der Ausgang tatsächlich, aber er kippt mehrmals hin und her, bevor er sich schließlich in einen stabilen Zustand einpendelt. Dies ist genau der Grund, warum das Verhalten so inkonsistent ist. Der Ausgang kippt wie gewünscht bei der steigenden Taktflanke, kippt dann aber kurz darauf erneut schnell hin und her. Die Periode dieser schnellen Kippvorgänge beträgt etwa 82 Nanosekunden.

Dieses Phänomen, bekannt als "Racing" oder "Takt-Wettlauf", ergibt Sinn, wenn wir den Schaltplan erneut betrachten. Der Taktimpuls, obwohl wir nur seine steigende Flanke nutzen wollen, bleibt für eine beträchtliche Dauer (in diesem Fall 250 Millisekunden) hoch. Wenn der Ausgang *bevor* dieser Impuls wieder auf Null zurückgeht, schaltet, verursacht die Rückkopplungsschleife, dass er erneut und wiederum schaltet, was zu mehrfachem Kippen führt. Wenn also der Taktimpuls hoch geht, schaltet der Ausgang ein, schaltet dann aber sofort wieder aus und ein und wiederholt dies. Es ist rein zufällig, dass er sich manchmal in den gewünschten Zustand einpendelt.

Die Ursache für diese Wettlaufsituation liegt in der RC-Schaltung, die zur Erkennung der steigenden Flanke verwendet wird. Ich erwähnte, dass der Kondensator 0,0001 Mikrofarad und der Widerstand 1000 Ohm beträgt. Das Multiplizieren dieser Werte ergibt die Zeitkonstante der RC-Schaltung, die die Impulsbreite angibt. Diese Zeitkonstante beträgt ungefähr 100 Nanosekunden.

Lassen Sie uns den Impulseingang für die Schaltung messen. Zunächst sieht er, wenn herausgezoomt, großartig aus – ein schneller Impuls bei der steigenden Taktflanke, wie gewünscht. Das Problem ist, dass dieser Impuls nicht schnell *genug* ist. Es ist ein 1-Mikrosekunden-Impuls, und während dieser 1 Mikrosekunde kippt der Ausgang wiederholt ein und aus, bevor er sich schließlich einpendelt, wenn der Impuls auf logisch Null fällt.

Was kann man dagegen tun? Eine Möglichkeit ist, den Impuls kürzer zu machen. Da die Kippperiode bei etwa 80 Nanosekunden liegt, benötigen wir einen Impuls, der deutlich kürzer als 1 Mikrosekunde ist. Wir können versuchen, den 1000-Ohm-Widerstand durch einen 100-Ohm-Widerstand zu ersetzen, was die Zeitkonstante auf 100 Nanosekunden reduzieren sollte.

Nach dem Austauschen des Widerstands beobachten wir einen viel kleineren Impuls. Allerdings funktioniert es immer noch nicht konsistent. An diesem Punkt stoßen wir an die Grenzen von Steckbrettern. Hochgeschwindigkeitssignale im Bereich von Zehnern von Nanosekunden sind auf Steckbrettern aufgrund von Streukapazitäten, Induktivitäten und anderen parasitären Effekten schwierig zu handhaben. Dies erklärt, warum schon das Bewegen meiner Hand in der Nähe der Schaltung ihr Verhalten ändern kann, da meine Hand als geerdetes Objekt die Kapazität verändert.

Sie können sehen, dass der Ausgang jetzt hoch geht, dann niedrig und niedrig bleibt. Aber wiederum, wenn ich meine Hand bewege, könnte er anfangen zu kippen. Ich ändere keine Verbindungen, nur die Bewegung meiner Hand beeinflusst die Kapazität.

Selbst die steigende Flanke unseres Takts ist auf dieser Zeitskala aufgrund der Steckbrettgrenzen nicht perfekt scharf. Der von uns erzeugte Impuls ist nicht so sauber wie mit dem größeren Widerstand. Letztendlich deutet all dies darauf hin, dass wir die Grenzen des Machbaren auf einem Steckbrett ausreizen. Diese spezielle Methode zur Erkennung einer steigenden Flanke mit einer RC-Schaltung ist in einem JK-Flipflop aufgrund der Wettlaufsituation von Natur aus problematisch. Wenn der Impuls nicht schmal genug ist (idealweise nur wenige Nanosekunden), wird der Ausgang zurückgekoppelt und kippt mehr als einmal pro steigender Taktflanke.

Was ist also die Lösung? Im nächsten Video werde ich eine weit überlegene Methode zum Aufbau eines JK-Flipflops demonstrieren, die dieses Wettlaufproblem vollständig beseitigt: das Master-Slave-JK-Flipflop. Es ist ein viel robusteres Design und sollte ohne Probleme auf einem Steckbrett funktionieren.