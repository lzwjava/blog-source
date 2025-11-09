---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erzwinge 30-Minütige Baupause
translated: true
type: note
---

### Ändern Sie den Workflow, um eine 30-minütige Pause zwischen Builds zu erzwingen

Um sicherzustellen, dass Ihr Jekyll-Deployment-Workflow nicht zu häufig ausgeführt wird (d.h. mindestens eine 30-minütige Pause zwischen aufeinanderfolgenden Läufen), können Sie einen bedingten Schritt früh im `build`-Job hinzufügen. Dieser Schritt fragt die GitHub-API nach dem Zeitstempel des letzten erfolgreichen Laufs dieses Workflows ab. Wenn der aktuelle Auslöser innerhalb von 30 Minuten nach dem Abschluss dieses Laufs liegt, wird der Job frühzeitig mit einer Meldung beendet (und überspringt den Build).

Dieser Ansatz:
- Verwendet die GitHub REST-API (keine externen Tools erforderlich).
- Prüft nur auf **erfolgreiche** vorherige Läufe (Status: "completed", Conclusion: "success").
- Berechnet den Zeitunterschied in Sekunden und vergleicht ihn mit 1800 (30 Minuten).
- Funktioniert mit Ihren bestehenden Push- und `workflow_dispatch`-Triggern.
- Stört das Concurrency-Setup nicht (das überlappende Läufe behandelt).

#### Aktualisierter YAML-Auszug
Fügen Sie diesen neuen Schritt direkt nach dem "Checkout Repository"-Schritt in Ihrem `build`-Job ein. Der Rest des Workflows bleibt unverändert.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: 30-Minuten-Build-Abstand erzwingen
        id: cooldown
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Den letzten erfolgreichen Lauf dieses Workflows abrufen
          RUNS_RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${{ github.repository }}/actions/workflows/${{ github.workflow_ref }}/runs?status=completed&conclusion=success&per_page=1&sort=timestamp&direction=desc")

          # Den completed_at-Zeitstempel des letzten erfolgreichen Laufs extrahieren (ISO 8601 Format)
          LAST_COMPLETED_AT=$(echo "$RUNS_RESPONSE" | jq -r '.[0].completed_at // empty')
          
          if [ -z "$LAST_COMPLETED_AT" ] || [ "$LAST_COMPLETED_AT" = "null" ]; then
            echo "Kein vorheriger erfolgreicher Lauf gefunden. Führe Build durch."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

          # Zeitstempel in Unix-Sekunden für den Vergleich umwandeln
          CURRENT_TIME=$(date -u +%s)
          LAST_TIME=$(date -d "$LAST_COMPLETED_AT" +%s)
          TIME_DIFF=$((CURRENT_TIME - LAST_TIME))

          echo "Letzter erfolgreicher Lauf abgeschlossen um: $LAST_COMPLETED_AT (Diff: ${TIME_DIFF}s)"

          if [ $TIME_DIFF -lt 1800 ]; then  # 1800 Sekunden = 30 Minuten
            echo "Build übersprungen: Weniger als 30 Minuten seit dem letzten erfolgreichen Lauf."
            echo "skip_build=true" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "Ausreichender Zeitabstand. Führe Build durch."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

      # Den gesamten Build überspringen, wenn die Cooldown-Prüfung fehlschlägt (diese Bedingung zu nachfolgenden Schritten hinzufügen oder den Build in ein if einpacken)
      - name: Python 3.13.2 einrichten
        if: steps.cooldown.outputs.skip_build != 'true'
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      # ... (wiederhole die 'if: steps.cooldown.outputs.skip_build != 'true'' Bedingung bei ALLEN verbleibenden Schritten nach diesem hier)
```

#### Wichtige Änderungen erklärt
1. **API-Abfrage**:
   - Verwendet `curl`, um den GitHub Actions API-Endpunkt für Workflow-Läufe aufzurufen.
   - Filtert nach `status=completed` und `conclusion=success`, um nur beendete, erfolgreiche Läufe zu erhalten.
   - Beschränkt auf `per_page=1` und sortiert nach `timestamp desc` für den neuesten Lauf.
   - Extrahiert `completed_at` (die genaue Endzeit des vorherigen Laufs).

2. **Zeitberechnung**:
   - Wandelt sowohl die aktuelle Zeit als auch die letzte Abschlusszeit mit `date` in Unix-Zeitstempel um.
   - Berechnet die Differenz in Sekunden.
   - Wenn `< 1800` Sekunden, setzt es `skip_build=true` und beendet den Schritt frühzeitig.

3. **Bedingte Ausführung**:
   - Fügen Sie `if: steps.cooldown.outputs.skip_build != 'true'` zu **jedem nachfolgenden Schritt** hinzu (z.B. Python einrichten, Abhängigkeiten installieren, bis hin zu "Sync built site").
   - Dies stellt sicher, dass der Job in der GitHub-UI als "übersprungen" gemeldet wird, wenn der Cooldown ausgelöst wird, aber dennoch den Grund protokolliert.

4. **Behandelte Randfälle**:
   - Keine vorherigen Läufe: Führt den Build durch (erster Build).
   - Fehlgeschlagene/laufende vorherige Läufe: Ignoriert sie und führt den Build durch.
   - API-Fehler: Fällt auf Build-Durchführung zurück (sichere Standardeinstellung).
   - `jq` ist auf `ubuntu-latest` vorinstalliert, daher ist kein zusätzliches Setup nötig.

#### Die Änderung testen
- Committen Sie dies in Ihren `main`-Branch (es wird den Workflow auslösen).
- Lösen Sie mehrere schnelle Pushes/Dispatches aus: Der zweite innerhalb von 30 Min sollte übersprungen werden.
- Beobachten Sie die Job-Logs auf die "Build übersprungen"-Meldung.
- Wenn Sie den Abstand anpassen möchten (z.B. 1 Stunde), ändern Sie `1800` zu `3600`.

#### Alternativen
- **Schedule-Trigger**: Wenn Sie *periodische* Builds alle 30 Min möchten (unabhängig von Pushes), fügen Sie dies zum `on:`-Abschnitt hinzu:
  ```yaml
  schedule:
    - cron: '*/30 * * * *'  # Alle 30 Minuten
  ```
  Dies erzwingt jedoch keine Pause bei Push-Triggern – verwenden Sie es bei Bedarf zusätzlich zum Cooldown-Schritt.
- **Custom Action**: Für Wiederverwendbarkeit, kapseln Sie die Cooldown-Logik in einem wiederverwendbaren Workflow oder einer Composite Action.
- **Einschränkungen**: Dies prüft die Lauf-Abschlusszeit, nicht die Startzeit. Wenn ein vorheriger Lauf noch länger als 30 Min läuft, wird Concurrency ihn ohnehin abbrechen.

Wenn dies nicht Ihrer genauen Absicht entspricht (z.B. Sie meinten *mindestens* alle 30 Min zu planen), geben Sie mehr Details an!