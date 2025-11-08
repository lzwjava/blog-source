---
audio: false
generated: false
image: false
lang: de
layout: post
title: Personalisieren Sie Ihren USB-Stick mit einem Hintergrund und einem Icon
translated: true
type: post
---

Dieser Beitrag wurde ursprünglich auf Chinesisch verfasst und auf Qzone veröffentlicht.

---

**I. Anpassen des USB-Laufwerkssymbols:**

1. Wählen Sie zunächst ein Symbol, das Ihnen gefällt. Die Dateierweiterung des Symbols sollte `.ico` sein.
2. Kopieren Sie die Symboldatei auf Ihr USB-Laufwerk und erstellen Sie ein neues Textdokument auf dem USB-Laufwerk.
3. Schreiben Sie im Textdokument Folgendes:
   ```
   [autorun]
   ICON=\xxx.ico,0
   ```
   Wobei `xxx.ico` der Name Ihrer Symboldatei (inklusive der Erweiterung) ist.
4. Speichern Sie die Textdatei als `autorun.inf`.
   **Hinweis:** Es ist wichtig, die Erweiterung in `.inf` und nicht in `.txt` zu ändern. Wenn sich das Dateisymbol in ein Symbol mit einem gelben Zahnrad ändert, haben Sie es richtig gemacht.
   Ziehen Sie das USB-Laufwerk heraus und stecken Sie es erneut ein. Sie werden feststellen, dass sich das Symbol des USB-Laufwerks in das von Ihnen ausgewählte geändert hat.
   Diese Methode kann auch für externe Festplatten oder CD/DVD-Brenner verwendet werden.

**II. Anpassen des Hintergrunds:**

1. Wählen Sie zunächst ein Hintergrundbild, das Ihnen gefällt, und kopieren Sie es auf Ihr USB-Laufwerk.
2. Erstellen Sie eine neue Textdatei und kopieren Sie den folgenden Text hinein:
   ```
   [ExtShellFolderViews]
   {BE098140-A513-11D0-A3A4-00C04FD706EC}={BE098140-A513-11D0-A3A4-00C04FD706EC}
   [{BE098140-A513-11D0-A3A4-00C04FD706EC}]
   Attributes=1
   IconArea_Image=aaa.jpg
   IconArea_Text=0x00FFFFFF
   [.ShellClassInfo]
   ConfirmFileOp=0
   ```
   Dieser Code bedeutet:

   Wobei `aaa.jpg` der Name Ihrer ausgewählten Bilddatei (inklusive der Erweiterung) ist.

   `IconArea_Text= 0x00FFFFFF` Diese Zeile ändert die Textfarbe auf dem USB-Laufwerk.

   Farbcodes sind:

   - Rot: `0x000000FF`
   - Gelb: `0x0000FFFF`
   - Blau: `0x00FF0000`
   - Grau: `0x00808080`
   - Limonengrün: `0x006BDEC7`
   - Schwarz: `0x00000000`
   - Excel-Hintergrundfarbe: `0x00848284`
   - Weiß: `0x00FFFFFF`
   - Grün: `0x00008000`
   - Lila: `0x00C000C0`

   Wählen Sie eine Farbe, die Ihnen gefällt (die zu Ihrem Hintergrund passt) und ersetzen Sie den vorhandenen Farbcode.

   Sie können die Farbe nach `IconArea_Text=` in Ihre bevorzugte Farbe ändern.

3. Speichern Sie die Textdatei als `Desktop.ini`. Die Änderung ist abgeschlossen.
   Aktualisieren Sie das USB-Laufwerk und Sie sollten die Änderungen sehen.
   Alle vier oben genannten Dateien können ausgeblendet werden, um eine versehentliche Löschung zu vermeiden.
   Nach dem Ändern des Symbols müssen Sie das USB-Laufwerk herausziehen und erneut einstecken, um die Wirkung zu sehen.
   Nach dem Ändern des Hintergrunds aktualisieren Sie das USB-Laufwerk, um die Änderungen zu sehen.