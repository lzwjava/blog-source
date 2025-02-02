---
audio: false
lang: de
layout: post
title: Eclipse in Emacs umwandeln
translated: true
---

Als Emacs-Nutzer für ein halbes Jahr kann ich mir kaum vorstellen, wie ich früher programmiert habe, meine Hände von der Standardposition wegzubewegen, um die Maus zu klicken oder die Pfeiltasten zu drücken, ohne das Gefühl zu haben, dass es umständlich und unerträglich ist. Jetzt, wenn ich meinen Freunden erzähle, dass ich die Tastenkombinationen Alt+P und Alt+N eingerichtet habe, um schnell zwischen XML-Dateien und der grafischen Layoutansicht zu wechseln, antworten sie nur mit "okay", was bedeutet, dass das Verwenden der Maus zum Wechseln auch in Ordnung ist.

Für mich ist das ein Albtraum; es ist einfach nicht schnell genug! Wenn du ein Emacs-Nutzer bist, verstehst du...

Dieser Artikel beschreibt einfache Techniken, um eine schnelle "Bearbeitungs"-Umgebung in Eclipse zu erstellen. Grundsätzlich können deine Hände in der Standardposition bleiben, sodass du mit maximaler Effizienz programmieren kannst!

Das Wichtigste ist, das Emacs+ Plugin zu installieren. Siehe "Emacs+: Emacs-Erfahrung in Eclipse".

Um den Code-Assistenten gut zu nutzen, musst du ihn so einrichten, dass er durch jedes Zeichen ausgelöst wird und die automatische Vervollständigung verhindert, wenn du auf Leertaste oder = drückst. Ich empfehle, diese jar-Datei von CSDN herunterzuladen. Mit ihr und einer schnellen Google-Suche kannst du Pakete in kürzester Zeit importieren.

Als Nächstes passen wir einige Tastenkombinationen an:

1) Binde Alt+P an "Vorheriger Sub-Tab" und Alt+N an "Nächster Sub-Tab."

Der Sub-Tab ist die Registerkarte unterhalb eines Editors, wie die "Grafische Layout"- und "XML"-Registerkarten beim Bearbeiten einer XML-Datei. Dies ermöglicht es dir, die Layoutansicht sofort anzuzeigen.

2) Binde Ctrl+C, Ctrl+C an "Ausführen."

Dies ist aus der Konfiguration von sbcl kopiert. Der Standard ist Ctrl+F11, was für eine so häufig verwendete Tastenkombination zu weit entfernt ist, was Emacs-Nutzer schrecklich finden! Ich habe dummerweise ein paar Tage lang Ctrl+F11 gedrückt, bevor ich es geändert habe.

3) Binde Ctrl+X, Ctrl+O an "Nächste Ansicht." Wenn in Windows und beim Bearbeiten von Text.

Dies ermöglicht es dir, sofort vom Editor zur Konsole zu springen, wenn du Java-Code schreibst.

4) Binde Ctrl+X, O an "Nächster Editor." Wenn in Windows und beim Bearbeiten von Text.

Dies ermöglicht es dir, schnell zwischen Java-Dateien zu wechseln.

5) Binde Ctrl+Q an "Schnellbehebung."

Auf diese Weise springst du, wenn du `@string/xx` eingibst, mit dem Cursor auf `xx` bei Drücken von Ctrl+Q und dann Enter sofort zu `string.xml`, wobei der Cursor an der `TODO` innerhalb von `<string name="xx">TODO</string>` positioniert ist.

6) Binde Ctrl+Shift+W an "Schließen" (wenn in Windows) und entferne die ursprüngliche Zuweisung (alle schließen).

Die ursprüngliche Schließen-Tastenkombination ist Ctrl+W, was sich mit unseren Gewohnheiten in Browsern, Chatboxen und Datei-Explorer deckt. Es steht jedoch im Konflikt mit dem Emacs-Schnittbefehl. In der Realität können viele Dateien in einer Sekunde geschlossen werden, wenn Ctrl+Shift+W gedrückt wird. Daher geht nichts verloren, wenn Ctrl+Shift+W von "alle schließen" zu "schließen" geändert wird.

Es gibt ein Problem: Nachdem Emacs+ installiert wurde, wenn du den Code-Assistenten beim Bearbeiten von Code verwendest und der Code-Assistent erscheint, wählen die Pfeilauf- und Pfeilabwärts-Tasten keine Elemente in der Kandidatenliste des Code-Assistenten aus; stattdessen bewegen sie sich nach oben und unten im bearbeiteten Code. Der Standard ist, ihn mit F2 zu aktivieren. Die Aktivierung des Code-Assistenten richtet den Fokus auf den Code-Assistenten ein, aber dann kannst du nur die Pfeilauf- und Pfeilabwärts-Tasten verwenden, um auszuwählen. Wie großartig wäre es, wenn wir Ctrl+P und Ctrl+N verwenden könnten! Das Bearbeiten von Code würde blitzschnell sein! Aber das Problem ist, dass nach der Installation des Emacs+ Plugins, obwohl Eclipse mehr wie Emacs wird, diese Funktion verloren geht. In einem sauberen Eclipse, wenn die Tastaturbelegung Emacs (nicht Emacs+Scheme) ausgewählt ist, kannst du Ctrl+N und Ctrl+P verwenden, um Abschlussartikel auszuwählen, wenn der Code-Assistent erscheint. Jemand fragte dies auf Stack Overflow, aber es gibt noch keine Antwort.

Wenn wir Ctrl+P und Ctrl+N verwenden könnten, um Abschlussartikel auszuwählen, wäre das wirklich wunderbar!