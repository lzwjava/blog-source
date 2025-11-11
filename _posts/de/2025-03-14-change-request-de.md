---
audio: false
generated: true
lang: de
layout: post
title: Anleitung zur Verwendung von Änderungsanträgen
translated: true
type: note
---

Um einer Change Request in ServiceNow eine Gruppe hinzuzufügen, müssen Sie einer Gruppe das Feld **Assignment Group** im Change Request-Formular zuweisen. Im Folgenden finden Sie eine detaillierte Schritt-für-Schritt-Anleitung, die Sie durch den Prozess führt.

---

### Schritt-für-Schritt-Anleitung

1. **Navigieren Sie zum Change Request-Modul**
   - Melden Sie sich bei Ihrer ServiceNow-Instanz an.
   - Geben Sie im linken Navigationsbereich "Change" in den Filter-Navigator ein.
   - Wählen Sie **Change > All**, um die Liste aller Change Requests anzuzeigen.

2. **Öffnen Sie den Change Request**
   - Suchen Sie den spezifischen Change Request, dem Sie eine Gruppe zuweisen möchten. Sie können die Suchleiste oder Filter verwenden (z. B. nach Change Request-Nummer oder Kurzbeschreibung).
   - Klicken Sie auf den Change Request, um sein Formular zu öffnen.

3. **Suchen Sie das Feld Assignment Group**
   - Suchen Sie im Change Request-Formular nach dem Feld **Assignment Group**. Dies befindet sich typischerweise im Abschnitt "Planning" oder "Assignment" des Formulars, abhängig von der Konfiguration Ihrer Instanz.

4. **Wählen Sie die Gruppe aus**
   - Klicken Sie auf das Lupensymbol (Referenzsuche) neben dem Feld **Assignment Group**.
   - Ein Pop-up-Fenster zeigt eine Liste der verfügbaren Gruppen an.
   - Geben Sie den Namen der Gruppe in das Suchfeld ein, um die Liste zu filtern, und wählen Sie dann die gewünschte Gruppe durch Anklicken aus.
   - Wenn Sie den exakten Gruppennamen kennen, können Sie ihn auch direkt in das Feld eingeben, und ServiceNow schlägt passende Gruppen vor.

5. **Speichern Sie die Änderungen**
   - Nachdem Sie die Gruppe ausgewählt haben, klicken Sie auf **Update** oder **Save** (befindet sich normalerweise oben oder unten im Formular), um Ihre Änderungen am Change Request zu speichern.

---

### Wichtige Hinweise

- **Gruppentyp**
   Stellen Sie sicher, dass die Gruppe, die Sie zuweisen möchten, mit einem geeigneten Gruppentyp konfiguriert ist (z. B. "Change" oder "ITIL"). Einige ServiceNow-Instanzen schränken die im Feld **Assignment Group** verfügbaren Gruppen basierend auf deren Typ ein. Um den Typ einer Gruppe zu überprüfen oder zu aktualisieren:
   - Gehen Sie zu **User Administration > Groups**, suchen Sie die Gruppe und überprüfen Sie deren Feld "Type".

- **Berechtigungen**
   Sie benötigen ausreichende Berechtigungen, um Gruppen einem Change Request zuzuweisen. Typischerweise sind Rollen wie `change_manager` oder gleichwertig erforderlich. Wenn Sie keine Gruppe zuweisen können, wenden Sie sich an Ihren ServiceNow-Administrator, um Ihren Zugriff zu bestätigen.

- **Referenzqualifizierer**
   Das Feld **Assignment Group** könnte Filter (Reference Qualifiers) haben, die anzeigen, welche Gruppen erscheinen. Wenn die gewünschte Gruppe nicht aufgeführt wird, könnte dies an einer Konfiguration in den Dictionary-Einstellungen des Feldes liegen. Ein Administrator kann dies unter **System Definition > Dictionary** überprüfen.

- **Automatische Zuweisung (Optional)**
   Während diese Anleitung die manuelle Zuweisung behandelt, ist zu beachten, dass Gruppen auch automatisch über Workflows oder Zuweisungsregeln zugewiesen werden können, die von Ihrer Organisation konfiguriert wurden.

---

### Fehlerbehebung
- **Gruppe wird nicht angezeigt?**
   - Überprüfen Sie, ob die Gruppe unter **User Administration > Groups** existiert.
   - Überprüfen Sie deren Gruppentyp und eventuelle Referenzqualifizierer im Feld **Assignment Group**.
- **Keine Berechtigung zum Speichern?**
   - Stellen Sie sicher, dass Sie die notwendige Rolle zum Bearbeiten von Change Requests haben.

Indem Sie diese Schritte befolgen und die oben genannten Punkte beachten, sollten Sie in der Lage sein, einer Change Request in ServiceNow erfolgreich eine Gruppe hinzuzufügen. Wenn Sie auf Probleme stoßen, wenden Sie sich an Ihren ServiceNow-Administrator, um Unterstützung zu erhalten, die auf das Setup Ihrer Instanz zugeschnitten ist.

---

Um Ihr Problem zu lösen, bei dem Ihr Change Request in ServiceNow leer erscheint – wobei Abschnitte wie Related Links, Planning, Affected CIs, Approvers und die Change Request-Liste alle keine Daten anzeigen – müssen Sie diese Bereiche mit den notwendigen Informationen füllen. Es scheint, dass zwar das Change Request-Formular selbst existiert, aber die zugehörigen Listen und Felder keine Einträge enthalten. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung, die Ihnen hilft, die erforderlichen Details und zugehörigen Listen auszufüllen.

---

### Schritt 1: Grundlegende Informationen überprüfen und ausfüllen
Auch wenn Ihr Change Request existiert, fehlen ihm möglicherweise wesentliche Details. Stellen Sie zunächst sicher, dass die grundlegenden Felder ausgefüllt sind:

- **Öffnen Sie den Change Request**: Navigieren Sie zum spezifischen Change Request in ServiceNow (z. B. über das Modul Change > All oder durch Suche nach seiner Nummer).
- **Überprüfen Sie die erforderlichen Felder**:
  - **Short Description**: Fügen Sie eine kurze Zusammenfassung der Änderung hinzu (z. B. "Server-Speicher upgraden").
  - **Description**: Geben Sie eine detaillierte Erläuterung des Änderungsinhalts an.
  - **Requester**: Geben Sie an, wer die Änderung anfordert (dies könnte standardmäßig auf Sie gesetzt sein, wenn Sie ihn erstellt haben).
  - **Assignment Group**: Weisen Sie das für die Änderung verantwortliche Team zu (z. B. "Server Team").
  - **Assigned To**: Weisen Sie optional eine bestimmte Person innerhalb der Gruppe zu.
- **Speichern Sie das Formular**: Klicken Sie auf **Save** oder **Update**, um sicherzustellen, dass diese Details gespeichert werden. Einige Felder könnten Pflichtfelder sein (mit einem roten Sternchen markiert), und das Speichern ist möglicherweise nicht möglich, bis sie ausgefüllt sind.

---

### Schritt 2: Planungsdetails vervollständigen
Der von Ihnen erwähnte "Planning"-Abschnitt bezieht sich wahrscheinlich auf Felder, die den Umfang und den Zeitplan der Änderung definieren. Füllen Sie diese aus, um Kontext zu liefern:

- **Change Type**: Wählen Sie den Typ (z. B. Normal, Emergency, Standard).
- **Category**: Wählen Sie eine geeignete Kategorie (z. B. Hardware, Software, Network).
- **Priority**: Legen Sie die Priorität basierend auf Dringlichkeit und Auswirkung fest (z. B. Low, Medium, High).
- **Risk and Impact**: Bewerten und geben Sie die potenziellen Risiko- und Auswirkungsstufen ein.
- **Planned Start and End Dates**: Geben Sie an, wann die Änderung beginnen und enden soll.
- **Änderungen speichern**: Stellen Sie sicher, dass diese Felder gespeichert werden, um den Change Request zu aktualisieren.

---

### Schritt 3: Betroffene CIs hinzufügen
Die Liste der "Affected CIs" ist leer, weil noch keine Configuration Items (CIs) verknüpft wurden. So füllen Sie sie aus:

- **Suchen Sie die zugehörige Liste**: Scrollen Sie zum Abschnitt **Affected CIs** am unteren Ende des Formulars.
- **CIs hinzufügen**:
  - Klicken Sie auf **Edit** oder **New** (abhängig vom Setup Ihrer Instanz).
  - Ein Auswahlfenster erscheint, in dem Sie nach CIs in der Configuration Management Database (CMDB) suchen und diese auswählen können.
  - Wählen Sie die relevanten CIs aus (z. B. Server, Anwendungen), die von der Änderung betroffen sind.
- **Speichern**: Klicken Sie auf **Save**, um diese CIs mit dem Change Request zu verknüpfen.

---

### Schritt 4: Genehmiger verwalten
Die Liste der "Approvers" ist leer, weil noch keine Genehmigungsdatensätze existieren. Abhängig vom Prozess Ihrer Organisation können Genehmiger automatisch oder manuell hinzugefügt werden:

- **Genehmigungsprozess überprüfen**:
  - Suchen Sie nach einer Schaltfläche **Request Approval** oder einer UI-Aktion im Formular. Ein Klick darauf kann einen Genehmigungs-Workflow basierend auf vordefinierten Regeln auslösen (z. B. Änderungstyp oder Risikostufe).
- **Genehmiger manuell hinzufügen** (falls erforderlich):
  - Gehen Sie zur zugehörigen Liste **Approvals**.
  - Klicken Sie auf **New**, um einen Genehmigungssatz zu erstellen.
  - Wählen Sie den Genehmiger aus (z. B. einen Manager oder ein Mitglied des Change Advisory Board) und speichern Sie.
- **Status überwachen**: Sobald hinzugefügt, müssen die Genehmiger die Änderung genehmigen oder ablehnen.

---

### Schritt 5: Die Change Request-Liste auffüllen (Child Changes oder Tasks)
Sie erwähnten, dass eine "Change Request"-Liste leer ist, was sich auf untergeordnete Change Requests oder **Change Tasks** beziehen könnte. So gehen Sie vor:

- **Change Tasks** (wahrscheinlicher):
  - Scrollen Sie zur zugehörigen Liste **Change Tasks**.
  - Klicken Sie auf **New**, um einen Task zu erstellen.
  - Füllen Sie Details wie Task-Beschreibung, Assignment Group, Assigned To und Fälligkeitsdatum aus.
  - Speichern Sie den Task. Wiederholen Sie dies für alle erforderlichen Tasks.
- **Child Change Requests** (falls zutreffend):
  - Wenn Ihre Organisation übergeordnete-untergeordnete Change Requests verwendet, suchen Sie nach einer zugehörigen Liste wie **Child Changes**.
  - Klicken Sie auf **New**, um einen verknüpften Change Request zu erstellen und füllen Sie dessen Details aus.
- **Änderungen speichern**: Stellen Sie sicher, dass alle Tasks oder untergeordneten Anfragen gespeichert sind.

---

### Schritt 6: "Related Links" bearbeiten
Sie erwähnten, dass "Related Links" leer sind. Dies könnte ein Missverständnis für zugehörige Listen (wie Incidents oder Problems) sein und nicht für den UI-Bereich "Related Links". Um verknüpfte Datensätze aufzufüllen:

- **Verknüpfen Sie verwandte Datensätze**:
  - Überprüfen Sie zugehörige Listen wie **Related Incidents**, **Related Problems** oder **Caused by Change**.
  - Klicken Sie auf **Edit** oder **New** in diesen Listen.
  - Suchen Sie nach relevanten Datensätzen und verknüpfen Sie diese (z. B. einen Incident, der diese Änderung ausgelöst hat).
- **Speichern**: Aktualisieren Sie das Formular, nachdem Sie diese Verknüpfungen hinzugefügt haben.

---

### Schritt 7: Den Change Request voranbringen
Sobald die grundlegenden Informationen und zugehörigen Listen ausgefüllt sind, bringen Sie den Change Request voran:

- **Prüfen Sie den State**: Überprüfen Sie den aktuellen State (wahrscheinlich "New").
- **Zum nächsten State wechseln**: Verwenden Sie die **State** Dropdown-Liste oder UI-Aktionen (z. B. **Assess**, **Authorize**), um ihn weiterzubewegen. Einige Felder oder Listen könnten erst in späteren States relevant werden (z. B. tatsächliche Daten in "Implement").
- **Workflow befolgen**: Der Workflow Ihrer Instanz leitet den Prozess – füllen Sie die erforderlichen Felder in jeder Phase aus.

---

### Wichtige Hinweise
- **Berechtigungen**: Stellen Sie sicher, dass Sie über die notwendigen Zugriffsrechte verfügen (z. B. die Rolle `change_manager`), um diese Felder und Listen zu bearbeiten. Wenn nicht, wenden Sie sich an Ihren ServiceNow-Administrator.
- **Benutzerdefinierte Konfiguration**: Ihre Instanz verwendet möglicherweise Vorlagen, Change Models oder automatisierte Workflows, die einige Daten vorab füllen. Wenden Sie sich an Ihren Administrator, wenn sich Felder nicht wie erwartet verhalten.
- **Sichtbarkeit**: Einige Abschnitte könnten basierend auf dem State oder Ihren Berechtigungen ausgeblendet oder gesperrt sein – das Weiterschalten des States kann mehr Optionen offenlegen.

Indem Sie diese Schritte befolgen, verwandeln Sie Ihren leeren Change Request in einen vollständig ausgefüllten Datensatz, der zur Bearbeitung bereit ist. Wenn Probleme bestehen bleiben, geben Sie Ihrem ServiceNow-Administrator Details (z. B. Change Request-Nummer) zur weiteren Untersuchung.