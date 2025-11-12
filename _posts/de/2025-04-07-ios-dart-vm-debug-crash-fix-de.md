---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: iOS Dart VM Debug Absturzbehebung
translated: true
type: note
---

Du stößt auf eine bekannte Interaktion zwischen iOS und der Dart VM: Die Dart VM im **Debug-Modus (JIT)** muss zur Laufzeit Speicherseiten als ausführbar markieren, und neuere iOS-Versionen haben die Richtlinien verschärft, sodass `mprotect(..., PROT_EXEC)` mit `13 (Permission denied)` fehlschlägt. Das führt dazu, dass die Dart VM beim Finalisieren von Code abbricht und den von dir eingefügten Absturz verursacht (SIGABRT). Dies ist kein Fehler in deinem Flutter-App-Code – es ist eine Inkompatibilität zwischen der Plattform (iOS / Systemrichtlinie) und dem VM-Modus. ([GitHub][1])

### Kurzzusammenfassung / Grundursache

* Debug-Builds verwenden die Dart-**JIT** (Hot Reload/Hot Restart), die den Speicherschutz ändern muss, um generierten Maschinencode ausführbar zu machen. Neuere iOS-Versionen blockieren dies, was zu `mprotect failed: 13 (Permission denied)` und einem Assert in der Dart VM führt. ([GitHub][1])

---

### Sofortige Workarounds (wähle einen, der zu deinem Workflow passt)

1. **Auf dem Simulator ausführen** – der Simulator führt x86/arm Simulator-Code aus, bei dem die JIT-Einschränkungen nicht durchgesetzt werden, daher funktionieren Debug und Hot Reload.
   Befehl: `flutter run -d <simulator-id>` (oder über Xcode öffnen). ([GitHub][1])

2. **Profile oder Release (AOT) auf dem Gerät verwenden** – baue AOT-Code, damit die VM keine Speicherseiten zur Laufzeit mit `mprotect` schützen muss. Du verlierst Hot Reload, aber die App wird auf dem Gerät laufen.

   * Für eine Testinstallation: `flutter build ios --release` und dann Installation via Xcode oder `flutter install --release`.
   * Oder `flutter run --profile` / `flutter run --release` zum direkten Ausführen. ([GitHub][1])

3. **Ein älteres iOS-Gerät/OS verwenden** (nur als temporäre Testmöglichkeit): Die Einschränkung trat in einigen iOS-Beta/Versionen auf; Geräte mit einer iOS-Version vor der strengeren Richtlinie lösen das Assert nicht aus. (Nicht ideal für die langfristige Nutzung.) ([Stack Overflow][2])

---

### Langfristige Lösungen / Empfehlungen

* **iOS / Xcode aktualisieren** – Apple hat das Verhalten in Beta-Versionen geändert; manchmal stellen spätere iOS-Beta-Patches das Verhalten wieder her oder ändern die Richtlinie. Wenn du eine iOS-Beta verwendest, die die Einschränkung eingeführt hat, aktualisiere auf die Version, die die Korrektur enthält. (Es gibt Berichte, dass bestimmte iOS-Betas dies eingeführt/zurückgesetzt haben und spätere Betas das Verhalten korrigiert oder geändert haben.) ([Stack Overflow][2])

* **Flutter/Dart auf die neueste Stable-Version upgraden** – Die Flutter/Dart-Teams haben dies in GitHub-Issues verfolgt und nach der Plattformänderung Updates/Workarounds veröffentlicht; stelle sicher, dass deine Flutter- und Dart-Versionen aktuell sind. Führe nach dem Upgrade `flutter clean` aus und baue neu. ([GitHub][3])

* **Dem Upstream-Issue(s) folgen** – Es gibt aktive Flutter-Issues und PRs zu iOS-JIT/`mprotect`-Fehlern. Abonniere die Flutter-Issue-Threads, um permanente Fixes oder empfohlene Entwickler-Workflows zu erhalten. (Ich kann die Links einfügen, wenn du möchtest.) ([GitHub][1])

---

### Zusätzlicher Hinweis zur `UIScene`-Meldung, die du ebenfalls gesehen hast

Die `UIScene`-Lifecycle-Meldung oben („`UIScene lifecycle will soon be required`…“) ist eine **Warnung** von iOS bezüglich des Wechsels zum modernen, szenenbasierten App-Lifecycle (iOS 13+). Sie steht in keinem Zusammenhang mit dem `mprotect`-Absturz. Du kannst sie vorübergehend ignorieren oder auf Scenes migrieren (implementiere `SceneDelegate` / aktualisiere `Info.plist`), wenn du die Warnung entfernen möchtest. Sie ist nicht die Ursache des SIGABRT. ([GitHub][1])

---

### Konkrete Schritt-für-Schritt-Empfehlung für jetzt

1. Wenn du Hot Reload benötigst: führe die App auf dem **Simulator** aus.
   `flutter run -d <simulator-id>`

2. Wenn du jetzt auf dem physischen Gerät testen möchtest: baue im **Release/Profile**-Modus (AOT).
   `flutter run --release` (oder `flutter build ios --release` + installieren)

3. Aktualisiere deine Umgebung: upgrade iOS (falls auf einer Beta mit dem Bug), update Xcode, upgrade Flutter/Dart, `flutter clean`, dann erneuter Versuch auf dem Gerät.

4. Wenn du möchtest, füge die Ausgabe von `flutter doctor -v` und die genaue iOS-/Geräteversion, die du testest, ein, und ich gebe dir die spezifischsten nächsten Schritte (z.B. „diese iOS-Version ist bekannt-fehlerhaft – aktualisiere auf X.Y.Z oder verwende Release-Builds“).

---

### Links / Referenzen (damit du der Upstream-Diskussion folgen kannst)

* GitHub Flutter Issue, der Debug-Modus JIT / `mprotect failed: 13` verfolgt (Diskussion & Workarounds). ([GitHub][1])
* StackOverflow-Thread, der denselben `mprotect failed: 13` Fehler in der iOS-Beta meldet – deutet auf Plattform-Regression und iOS-Beta-Fixes hin. ([Stack Overflow][2])
* Ein Blog/Summary, der die iOS 26 / Flutter-Problematik erklärt und empfohlene Entwickleroptionen auflistet. ([Medium][4])

---

Wenn du möchtest, kann ich:

* dir die genauen `flutter`-Befehle zum Erstellen einer Release-IPA und zur Installation auf deinem Gerät geben, oder
* deine `flutter doctor -v` Ausgabe und deine Geräte-OS-Version prüfen, um die eine beste aktuelle Aktion zu empfehlen.

Was würdest du bevorzugen?

[1]: https://github.com/flutter/flutter/issues/163984?utm_source=chatgpt.com "Debug mode and hot reload fail on iOS 26 due to JIT ..."
[2]: https://stackoverflow.com/questions/79473408/flutter-ios-18-4-debug-build-error-mprotect-failed-13-permission-denied?utm_source=chatgpt.com "Flutter iOS 18.4 Debug Build Error: mprotect failed"
[3]: https://github.com/flutter/flutter/actions/runs/15564769770?utm_source=chatgpt.com "Debug mode and hot reload fail on iOS 26 due to JIT ..."
[4]: https://vijay-mishra.medium.com/flutter-vs-ios26-what-broke-and-what-to-do-36c6d6bf1e16?utm_source=chatgpt.com "Flutter vs iOS 26: What Broke and How to Fix It - Vijay Mishra"