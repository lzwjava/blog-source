---
audio: false
generated: true
lang: de
layout: post
title: Entfernen benutzerdefinierter Modelle in GitHub Copilot
translated: true
type: note
---

Um ein Modell in der GitHub Copilot-Erweiterung für Visual Studio Code (VS Code) zu entfernen, beachten Sie, dass integrierte Modelle (wie das standardmäßige GitHub Copilot-Modell) nicht entfernt werden können, da sie Teil der Erweiterung sind. Wenn Sie sich jedoch auf ein benutzerdefiniertes Modell beziehen, das Sie über einen Drittanbieter (z. B. Anthropic, OpenAI, Google Gemini oder andere) mit Ihrem eigenen API-Schlüssel hinzugefügt haben, können Sie es effektiv entfernen, indem Sie den zugehörigen API-Schlüssel und die Anbieterdetails löschen. Diese Funktion befindet sich in der Vorschau und ist möglicherweise noch nicht für Copilot Business- oder Enterprise-Benutzer verfügbar.

Hier sind die Schritte basierend auf der offiziellen Dokumentation:

1.  Öffnen Sie die Chat-Ansicht in VS Code (falls nicht bereits geöffnet, verwenden Sie die Befehlspalette mit `Strg+Umschalt+P` oder `Befehl+Umschalt+P` auf macOS und suchen Sie dann nach "Copilot: Open Chat").
2.  Klicken Sie in der Chat-Ansicht auf das Dropdown-Menü zur Modellauswahl (neben dem Eingabefeld) und wählen Sie **Manage Models**. Alternativ können Sie die Befehlspalette öffnen und den Befehl **GitHub Copilot: Manage Models** ausführen.
3.  Bewegen Sie den Mauszeiger in der Oberfläche "Manage Models" über den Anbieter des Modells, das Sie entfernen möchten, und klicken Sie auf das Zahnradsymbol, um dessen Details zu bearbeiten.
4.  Löschen Sie den API-Schlüssel (und gegebenenfalls eine Endpunkt-URL) aus den Feldern und speichern Sie die Änderungen. Dadurch sollte das Modell aus der Auswahl entfernt werden.

Wenn Sie Probleme haben (z. B. das Feld für den API-Schlüssel aktualisiert sich nicht oder lässt sich nicht richtig löschen, was in einigen Fällen als Bug gemeldet wurde), versuchen Sie zuerst diese Problemumgehung:
-   Wählen Sie in der Chat-Ansicht im Dropdown-Menü zur Modellauswahl ein anderes Modell aus, um das zu entfernende Modell abzuwählen.
-   Kehren Sie zu "Manage Models" zurück, bearbeiten Sie den Anbieter und löschen Sie dann den API-Schlüssel.

Voraussetzungen und Hinweise:
-   Dies betrifft nur Chat-Funktionen; es hat keine Auswirkung auf Code-Vervollständigungen oder andere Tools.
-   Stellen Sie sicher, dass Ihr Copilot-Abonnement den Zugriff auf mehrere Modelle erlaubt (z. B. Individual, Pro oder aktivierte Vorschaufunktionen für Organisationen).
-   Wenn das Modell weiterhin vorhanden ist oder Sie Fehler erhalten, starten Sie VS Code neu oder prüfen Sie auf Erweiterungs-Updates.

Wenn dies nicht dem entspricht, was Sie mit "Modell entfernen" meinen (wenn Sie z. B. versuchen, die gesamte Erweiterung zu deaktivieren oder Copilot-Funktionen auszublenden), teilen Sie dies bitte mit, um maßgeschneiderte Schritte zu erhalten.