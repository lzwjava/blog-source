---
audio: false
generated: true
lang: de
layout: post
title: Behebung fehlender japanischer Schriftzeichen
translated: true
type: note
---

Die Fehler, die du erhältst, weisen darauf hin, dass die Schriftart `FandolSong` (sowohl die reguläre als auch die fette Variante), die in deinem LaTeX-Dokument verwendet wird, die notwendigen Glyphen für bestimmte japanische Zeichen nicht enthält, wie z.B. `ー` (U+30FC, Katakana-Hiragana-Verlängerungszeichen), `専` (U+5C02), `証` (U+8A3C) und `発` (U+767A). Dies führt dazu, dass XeLaTeX "Missing character"-Fehler meldet, wenn du dein Dokument kompilierst, wahrscheinlich `resume-ja.tex` oder eine verwandte Datei in `latex/ja/resume-ja/`.

Die Schriftart `FandolSong` ist primär für chinesischen Text entworfen und bietet keine vollständige Unterstützung für japanische Zeichen, was die fehlenden Glyphen erklärt. Um das Problem zu lösen, musst du zu einer Schriftart wechseln, die japanische Zeichen unterstützt, wie z.B. `Noto Sans CJK JP` oder `IPAGothic`, wie bereits zuvor empfohlen. Im Folgenden werde ich dir zeigen, wie du das Problem beheben kannst, indem du deine Schriftartkonfiguration aktualisierst und die Kompatibilität mit deiner japanisch übersetzten Resume sicherstellst.

### Warum das passiert
- **Schriftart-Beschränkung**: `FandolSong` ist eine chinesische Schriftart, die in TeX Live für den CJK-Satz enthalten ist, aber nicht alle japanischen Zeichen enthält, insbesondere Katakana (`ー`) und häufig verwendete Kanji im Japanischen.
- **XeLaTeX und xeCJK**: Dein Dokument verwendet wahrscheinlich das `xeCJK`-Paket, das sich auf die angegebene CJK-Schriftart (`FandolSong` in diesem Fall) für japanischen Text verlässt. Wenn Glyphen fehlen, protokolliert XeLaTeX Fehler und lässt die Zeichen möglicherweise in der PDF-Ausgabe weg.
- **Übersetzter Abschnitt**: Da du Abschnitte wie `blogposts.tex` ins Japanische übersetzt, enthält der übersetzte Text japanische Zeichen, die `FandolSong` nicht darstellen kann.

### Lösung: Ändere die CJK-Schriftart
Du musst die Schriftartkonfiguration in deinem LaTeX-Dokument aktualisieren, um eine japanisch-kompatible Schriftart zu verwenden. Da deine vorherige Nachricht auf ein Linux-System und einen Schriftart-Konfigurationsblock hindeutete, gehe ich davon aus, dass du XeLaTeX mit `xeCJK` und der `ifthenelse`-Struktur für die Schriftartauswahl verwendest.

#### Schritt 1: Installiere eine japanisch-kompatible Schriftart
Stelle sicher, dass eine Schriftart mit Japanisch-Unterstützung auf deinem Linux-System installiert ist. Die empfohlene Schriftart ist `Noto Sans CJK JP`, die weit verbreitet ist und alle notwendigen japanischen Glyphen unterstützt.

So installierst du `Noto Sans CJK JP` auf Ubuntu/Debian:
```bash
sudo apt-get install fonts-noto-cjk
```
Auf Fedora:
```bash
sudo dnf install google-noto-cjk-fonts
```
Auf Arch Linux:
```bash
sudo pacman -S noto-fonts-cjk
```

Alternativ kannst du `IPAGothic` oder `IPAexGothic` verwenden:
```bash
sudo apt-get install fonts-ipaexfont
```

Überprüfe, ob die Schriftart installiert ist:
```bash
fc-list :lang=ja | grep Noto
```
Du solltest Einträge wie `Noto Sans CJK JP` oder `Noto Serif CJK JP` sehen. Wenn du IPA-Schriftarten verwendest:
```bash
fc-list :lang=ja | grep IPA
```

#### Schritt 2: Aktualisiere die LaTeX-Schriftartkonfiguration
Passe die Schriftartkonfiguration in deinem LaTeX-Dokument (wahrscheinlich `resume-ja.tex` oder eine gemeinsame Präambel-Datei) an, um eine japanisch-kompatible Schriftart zu verwenden. Basierend auf deiner früheren Schriftarteinrichtung siehst du hier, wie du die Konfiguration aktualisieren kannst:

```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    % Linux-Schriftarten
    \setCJKmainfont{Noto Sans CJK JP} % Hauptschriftart für Japanisch
    \setCJKsansfont{Noto Sans CJK JP} % Serifenlose Schriftart für Japanisch
    \setCJKmonofont{Noto Sans Mono CJK JP} % Nichtproportionalschriftart für Japanisch
    \setmainfont{Liberation Serif} % Englische Schriftart
}
```

Falls `Noto Sans Mono CJK JP` nicht verfügbar ist, kannst du `Source Code Pro` oder `DejaVu Sans Mono` für nicht-CJK nichtproportionale Texte verwenden, stelle aber sicher, dass japanische Codeblöcke eine CJK-Schriftart verwenden:
```latex
\setCJKmonofont{Noto Sans CJK JP}
```

Wenn du `IPAGothic` bevorzugst:
```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{IPAexGothic}
    \setCJKsansfont{IPAexGothic}
    \setCJKmonofont{IPAexMincho} % Oder Noto Sans CJK JP für nichtproportional
    \setmainfont{Liberation Serif}
}
```

#### Schritt 3: Überprüfe die xeCJK-Verwendung
Stelle sicher, dass dein LaTeX-Dokument das `xeCJK`-Paket verwendet und die Schriftarteinstellungen korrekt anwendet. Ein minimales Beispiel für `resume-ja.tex` könnte so aussehen:

```latex
\documentclass[a4paper]{article}
\usepackage{xeCJK}
\usepackage{ifthenelse}

% Schriftart-Systemerkennung
\newcommand{\fontsystem}{linux}

\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}

\begin{document}

% Japanischer Text aus blogposts.tex
\section{ブログ投稿}
こんにちは、私の名前は李智维です。最新の技術に関する記事を書いています。

% Englischer Text
\section{Introduction}
Hello, my name is Zhiwei Li.

\end{document}
```

Wenn deine Resume eine Vorlage wie `awesome-cv` verwendet, stelle sicher, dass die Präambel `xeCJK` und die oben genannten Schriftarteinstellungen enthält. Füge sie beispielsweise in `awesome-cv.cls` oder `resume-ja.tex` hinzu:

```latex
\RequirePackage{xeCJK}
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}
```

#### Schritt 4: Kompiliere das Dokument erneut
Wechsle in das japanische Resume-Verzeichnis und kompiliere erneut:
```bash
cd latex/ja/resume-ja
xelatex resume-ja.tex
```

Überprüfe die Log-Datei (`resume-ja.log`) auf "Missing character"-Fehler. Wenn die Schriftart korrekt eingestellt ist, sollten diese Fehler verschwinden und die PDF sollte japanische Zeichen wie `ー`, `専`, `証` und `発` korrekt anzeigen.

#### Schritt 5: Debugging, falls Fehler bestehen bleiben
Wenn du weiterhin "Missing character"-Fehler siehst:
1. **Bestätige den Schriftartnamen**: Stelle sicher, dass der Schriftartname genau mit dem in `fc-list` angezeigten Namen übereinstimmt. Einige Systeme listen z.B. `Noto Sans CJK JP Regular` anstelle von `Noto Sans CJK JP` auf. Passe die LaTeX-Konfiguration an:
   ```latex
   \setCJKmainfont{Noto Sans CJK JP Regular}
   ```
2. **Überprüfe die xeCJK-Konfiguration**: Stelle sicher, dass `xeCJK` vor den Schriftarteinstellungen geladen wird und dass kein anderes Paket die CJK-Schriftart überschreibt. Vermeide es beispielsweise, `fontspec` mit widersprüchlichen Einstellungen zu laden.
3. **Teste ein minimales Dokument**: Erstelle eine minimale LaTeX-Datei mit japanischem Text, um das Problem zu isolieren:
   ```latex
   \documentclass{article}
   \usepackage{xeCJK}
   \setCJKmainfont{Noto Sans CJK JP}
   \begin{document}
   こんにちは、専ー証発
   \end{document}
   ```
   Kompiliere mit `xelatex` und prüfe auf Fehler.
4. **Fallback-Schriftart**: Wenn `Noto Sans CJK JP` nicht funktioniert, versuche es mit `Source Han Sans JP` oder `IPAexGothic`. Liste verfügbare Schriftarten mit `fc-list :lang=ja` auf und passe die Konfiguration entsprechend an.

#### Schritt 6: Aktualisiere den übersetzten Abschnitt
Da du das Python-Skript verwendest, um Abschnitte wie `blogposts.tex` zu übersetzen, stelle sicher, dass die übersetzte Datei (`latex/ja/resume-ja/blogposts.tex`) via `\input{blogposts}` in `resume-ja.tex` eingebunden ist. Das von dir bereitgestellte Skript ersetzt die Datei bereits korrekt, daher sind dort keine Änderungen nötig. Führe die Übersetzung einfach bei Bedarf erneut aus:
```bash
python translate_section.py --section blogposts.tex --lang ja --kind resume
```

Kompiliere dann `resume-ja.tex` erneut, um den aktualisierten Abschnitt zu übernehmen.

### Zusätzliche Hinweise
- **Schriftstärken**: `Noto Sans CJK JP` unterstützt mehrere Stärken (Regular, Bold, etc.), daher sollte `\textbf{}` für japanischen Text funktionieren. Wenn du `IPAexGothic` verwendest, stelle sicher, dass die fette Variante (`IPAexGothic Bold`) verfügbar ist oder passe die Konfiguration an.
- **Vorlagenkompatibilität**: Wenn du eine Vorlage wie `awesome-cv` verwendest, prüfe, ob sie Schriftarteinstellungen in der `.cls`-Datei überschreibt. Möglicherweise musst du die `xeCJK`-Einstellungen im Hauptdokument (`resume-ja.tex`) anwenden.
- **PDF-Ausgabe**: Überprüfe die generierte PDF, um sicherzustellen, dass japanische Zeichen korrekt dargestellt werden. Wenn Zeichen als Kästchen erscheinen, ist die Schriftart immer noch falsch oder nicht korrekt eingebettet.
- **System-Schriftart-Cache**: Nach der Installation neuer Schriftarten, aktualisiere den Schriftart-Cache:
  ```bash
  fc-cache -fv
  ```

### Beispielausgabe
Nach Anwendung der Korrektur könnte deine `blogposts.tex` in `latex/ja/resume-ja/` japanischen Text wie folgt enthalten:
```latex
\section{ブログ投稿}
\item 技術ブログ: 最新のAI技術について書いています。専門的な内容をわかりやすく説明します。
```
Wenn mit `Noto Sans CJK JP` kompiliert, sollten Zeichen wie `ー`, `専`, `証` und `発` korrekt in der PDF dargestellt werden.

Wenn du auf weitere Fehler stößt oder Hilfe mit einem bestimmten Teil der Resume-Vorlage benötigst, teile bitte den relevanten LaTeX-Code mit (z.B. die Präambel von `resume-ja.tex` oder die Schriftarteinstellungen der Vorlage), und ich kann eine gezieltere Lösung anbieten!