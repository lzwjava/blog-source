---
audio: false
generated: false
lang: de
layout: post
title: Eclipse in Emacs verwandeln
translated: true
---

Als Emacs-Nutzer seit sechs Monaten kann ich mir nicht vorstellen, wie ich früher programmiert habe, indem ich meine Hände von der Standardposition wegbewegte, um die Maus zu klicken oder die Pfeiltasten zu drücken, ohne das es umständlich und unerträglich erschien. Jetzt, wenn ich meinen Freunden erzähle, dass ich die Tastenkombinationen Alt+P und Alt+N eingerichtet habe, um schnell zwischen XML-Dateien und der grafischen Layout-Ansicht zu wechseln, lautet ihre Antwort einfach nur "okay," was impliesiert, dass das Verwenden der Maus zum Umschalten auch in Ordnung ist.
Für mich ist das ein Albtraum; es ist einfach nicht schnell genug! Wenn du ein Emacs-Nutzer bist, verstehst du...

Dieser Artikel beschreibt einfache Techniken, um eine schnelle "Bearbeitungs"-Umgebung in Eclipse zu erstellen. Grundsätzlich bleiben deine Hände in der Standardposition, sodass du mit maximaler Effizienz programmieren kannst!

Das Wichtigste ist, das Emacs+ Plugin zu installieren. Siehe "Emacs+: Emacs-Erfahrung in Eclipse".

Um die Code-Assistentenfunktion gut zu nutzen, musst du sie so einstellen, dass sie durch jedes Zeichen ausgelöst wird und die automatische Vervollständigung verhindert, wenn Leertaste oder = gedrückt wird. Ich empfehle, diese Jar-Datei von CSDN herunterzuladen. Mit ihr und einer schnellen Google-Suche kannst du Pakete in kürzester Zeit importieren.

Als Nächstes passen wir einige Tastenkombinationen an:

1) Binde Alt+P an "Vorgängiges Sub-Fenster" und Alt+N an "Nächstes Sub-Fenster."

Das Sub-Fenster ist die Registerkartenleiste unter einem Editor, wie z.B. die "Grafische Layout" und "XML" Registerkarten beim Bearbeiten einer XML-Datei. Dies ermöglicht es dir, die Layoutansicht sofort zu betrachten.

2) Binde Ctrl+C, Ctrl+C an "Ausführen."

Dies wurde aus der Konfiguration von sbcl übernommen. Standardmäßig ist es Ctrl+F11, was für eine so häufig verwendete Tastenkombination zu weit entfernt ist, was Emacs-Nutzer fühlen lässt, dass es furchtbar ist! Ich habe dummerweise ein paar Tage lang Ctrl+F11 gedrückt, bevor ich es geändert habe.

3) Binde Ctrl+X, Ctrl+O an "Nächste Ansicht." Wenn in Windows und im Text bearbeiten.

Dies ermöglicht es dir, sofort von dem Editor zum Konsolenfenster zu springen, wenn du Java-Code schreibst.

4) Binde Ctrl+X, O an "Nächster Editor." Wenn in Windows und im Text bearbeiten.

Dies ermöglicht es dir, schnell zwischen Java-Dateien zu wechseln.

5) Binde Ctrl+Q an "Schnellkorrektur."

Auf diese Weise springst du, wenn du `@string/xx` eingibst und der Cursor sich auf `xx` befindet, durch Drücken von Ctrl+Q und dann Enter sofort zu `string.xml`, wobei der Cursor an der Stelle `TODO` innerhalb von `<string name="xx">TODO</string>` positioniert ist.

6) Binde Ctrl+Shift+W an "Schließen" (wenn in Windows) und entferne die ursprüngliche Zuweisung (alles schließen).
Die ursprüngliche Schließen-Tastenkombination ist Ctrl+W, die mit unseren Gewohnheiten in Browsern, Chatboxen und Datei-Explorern übereinstimmt. Allerdings steht sie im Konflikt mit dem Emacs-Schnitt-Befehl. In Wirklichkeit kann das Drücken von Ctrl+Shift+W für eine Sekunde viele Dateien schließen. Daher wird durch das Ändern von Ctrl+Shift+W von "alles schließen" zu "schließen" nichts verloren.

Es gibt ein Problem: nach der Installation von Emacs+, wenn du Code bearbeitest und der Code-Assistent erscheint, wählen die Auf und Ab Pfeiltasten keine Elemente in der Kandidatenliste des Code-Assistenten aus, sondern bewegen den Cursor im bearbeiteten Code nach oben und unten. Standardmäßig wird er durch F2 aktiviert. Aktivieren des Code-Assistenten setzt den Fokus auf den Code-Assistenten, aber dann kannst du nur die Auf und Ab Pfeiltasten verwenden, um auszuwählen. Wie großartig wäre es, wenn wir Ctrl+P und Ctrl+N verwenden könnten! Das Bearbeiten von Code wäre blitzschnell! Aber das Problem ist, dass nach der Installation des Emacs+ Plugins, obwohl Eclipse mehr wie Emacs wird, diese Funktionalität verloren geht. In einem sauberen Eclipse, mit dem Emacs (nicht Emacs+Scheme) Tastaturlayout ausgewählt, kannst du Ctrl+N und Ctrl+P verwenden, um Abschluss-Elemente auszuwählen, wenn der Code-Assistent erscheint. Jemand hat dies auf Stack Overflow gefragt, aber es gibt noch keine Antwort.

Wenn wir Ctrl+P und Ctrl+N verwenden könnten, um Abschluss-Elemente auszuwählen, wäre das wirklich fantastisch!