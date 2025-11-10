---
audio: false
generated: true
image: false
lang: de
layout: post
title: So ändern Sie den Besitzer einer Änderungsanfrage
translated: true
type: note
---

Das Ändern des Besitzers einer **Change Request (CR)** hängt von dem verwendeten Tool oder Workflow-System ab (zum Beispiel ServiceNow, Jira, HP ALM oder ein benutzerdefiniertes ITSM-Tool). Der allgemeine Prozess ist jedoch normalerweise auf den verschiedenen Plattformen ähnlich:

---

### 1. Die Change Request finden

* Gehen Sie zum Bereich **Change Management** oder **Requests** in Ihrem ITSM-Tool.
* Suchen Sie nach der CR anhand der ID, des Titels oder anderer Filter.
* Öffnen Sie die Detailseite der CR.

---

### 2. Das Feld "Owner" oder "Assigned To" finden

* Die meisten Systeme haben ein Feld wie **Change Owner**, **Assigned To** oder **Responsible Person**.
* Dieses Feld legt fest, wer für die CR verantwortlich ist.
* Wenn Sie es nicht sofort sehen, prüfen Sie die Tabs **Assignment** oder **Ownership**.

---

### 3. Den Besitzer aktualisieren

* Klicken Sie auf **Edit** oder **Modify** für die CR.
* Ändern Sie den Wert des Felds **Owner** (oder "Assigned To") auf die neue Person.
* Dies geschieht normalerweise durch die Auswahl eines Namens aus einer Dropdown-Liste von Benutzern.
* Speichern oder bestätigen Sie die Aktualisierung.

---

### 4. Rollen-/Berechtigungsanforderungen prüfen

* Einige Systeme schränken Besitzeränderungen auf bestimmte Rollen ein (z. B. **Change Manager**, **Admin**).
* Wenn Sie keine Berechtigung haben, müssen Sie einen Change Manager oder Administrator bitten, die Änderung für Sie vorzunehmen.

---

### 5. Stakeholder benachrichtigen

* Bewährte Vorgehensweise: Fügen Sie einen **Kommentar** oder eine **Work Note** in der CR hinzu, um zu erklären, warum der Besitzer gewechselt hat.
* Benachrichtigen Sie den neuen Besitzer, damit er über die Verantwortung informiert ist.

---

✅ **Beispiel (ServiceNow)**

1. Öffnen Sie die Change Request.
2. Wählen Sie im Feld "Assigned To" den neuen Benutzer aus.
3. Speichern Sie den Datensatz.

✅ **Beispiel (Jira)**

1. Öffnen Sie den Change Request-Issue.
2. Klicken Sie auf das Feld "Assignee".
3. Wählen Sie den neuen Besitzer aus.

---

Möchten Sie, dass ich Ihnen **schrittweise Anleitungen für ein bestimmtes System** (wie ServiceNow, Jira oder HP ALM) gebe?