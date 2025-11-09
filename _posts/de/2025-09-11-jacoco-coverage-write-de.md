---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Jacoco-Abdeckungsdaten-Schreibverhalten
translated: true
type: note
---

Bei **Integrationstests** (oder anderen JVM-Prozessen), die den **JaCoCo-Agenten** verwenden, werden die Abdeckungsdaten **nicht automatisch in die `.exec`-Datei geschrieben, wenn die JVM beendet wird**. So funktioniert es:

---

### Wann schreibt JaCoCo die Abdeckungsdaten?
- **Während des JVM-Shutdowns**: Der JaCoCo-Agent **leert die Daten und schreibt** die gesammelten Abdeckungsdaten in die `.exec`-Datei, **wenn die JVM ordnungsgemäß heruntergefahren wird** (z.B. wenn die Hauptmethode endet oder die Testsuite abgeschlossen ist).
- **Bei einem JVM-Absturz**: Wenn die JVM abrupt beendet wird (z.B. aufgrund eines Absturzes oder `System.exit()`), hat der Agent möglicherweise **keine** Gelegenheit, die Daten zu schreiben, und einige Abdeckungsinformationen könnten verloren gehen.

---

### Wie stellt man sicher, dass die Daten geschrieben werden?
1. **Ordentliches Herunterfahren**: Stellen Sie sicher, dass Ihre Integrationstests oder Anwendung normal enden (z.B. keine erzwungenen Beendigungen).
2. **Expliziter Dump (Optional)**: Sie können manuell einen Dump der Abdeckungsdaten während der Laufzeit über die JaCoCo-Runtime-API auslösen (z.B. `org.jacoco.agent.rt.RT.getAgentRuntime().dump(true, outputFile)`). Dies ist nützlich für langlebige Prozesse oder wenn Sie Zwischendaten erfassen möchten.

---

### Beispielszenario
- Wenn Ihre Integrationstest-Suite normal läuft und abgeschlossen wird, schreibt der JaCoCo-Agent die Abdeckungsdaten am Ende des JVM-Prozesses in `jacoco.exec` (oder Ihre angegebene Datei).
- Wenn die JVM gewaltsam beendet wird (z.B. `kill -9`), werden die Daten möglicherweise nicht geschrieben.

---

### Best Practice
- **Verwenden Sie `append=true`**: Wenn Sie mehrere Testsuites ausführen, setzen Sie `append=true` in den JaCoCo-Agenten-Argumenten, um Abdeckungsdaten über mehrere Läufe hinweg zu sammeln.
- **Auf Teil-Daten prüfen**: Wenn die JVM abstürzt, könnte die `.exec`-Datei unvollständig sein oder Daten des letzten Laufs fehlen.

---