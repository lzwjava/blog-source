---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Rollenbasierte Zugriffskontrolle in Jenkins
translated: true
type: note
---

### Rollenbasierte Zugriffskontrolle (RBAC) in Enterprise Jenkins (CloudBees CI)

Enterprise Jenkins, powered by CloudBees CI, verwendet das CloudBees Role-Based Access Control (RBAC) Plugin, um feingranulare, rollenbasierte Berechtigungen zu implementieren. Dies ermöglicht Administratoren, benutzerdefinierte Rollen zu definieren, diese Benutzern oder Gruppen zuzuweisen und den Zugriff auf globaler, Ordner- oder Job-Ebene zu steuern. Es integriert sich mit dem Folders Plugin für team-basierte Isolation und unterstützt externe Identitätsanbieter wie LDAP oder Active Directory für die Gruppenverwaltung. Berechtigungen werden aus allen Rollen aggregiert, die den Gruppen eines Benutzers zugewiesen sind, und sie können an untergeordnete Objekte (z.B. Unterordner) weitergegeben werden, sofern sie nicht angeheftet oder gefiltert werden.

RBAC ersetzt oder erweitert die eingebaute matrix-basierte Autorisierung von Jenkins und ermöglicht die Delegation von Administrationsaufgaben ohne vollen Systemzugriff. Es wird unter **Manage Jenkins > Manage Security > Authorization** konfiguriert, wo Sie die "Role-based matrix authorization strategy" auswählen.

#### Wichtige Berechtigungen und Zugriffsrechte
Berechtigungen definieren atomare Aktionen, die Benutzer an Jenkins-Objekten (z.B. Jobs, Ordner, Agents, Views) ausführen können. Enterprise Jenkins beinhaltet die Kern-Jenkins-Berechtigungen plus solche, die durch Plugins erweitert werden. Berechtigungen sind hierarchisch – einige implizieren andere (z.B. `Job/Configure` impliziert `Job/Read`).

Hier ist eine Tabelle gängiger Berechtigungskategorien und Beispiele, mit Fokus auf Build/Read wie erwähnt:

| Kategorie          | Beispiele für Berechtigungen                                                                 | Beschreibung |
|-------------------|-----------------------------------------------------------------------------------------|-------------|
| **Lesen/Nur Lesen** | - `Overall/Read`<br>- `Job/Read`<br>- `View/Read`<br>- `Agent/Read`                     | Gewährt Lesezugriff auf Konfigurationen, Builds, Logs und Artefakte ohne Änderungsrechte. Nützlich für Auditoren oder Betrachter. Das Extended Read Permission Plugin fügt granulare Lesekontrollen hinzu (z.B. Workspace einsehen ohne Build-Rechte). |
| **Build/Ausführen** | - `Job/Build`<br>- `Job/Cancel`<br>- `Job/Workspace`<br>- `Job/Read (für Artefakte)`   | Ermöglicht das Starten, Stoppen oder Zugreifen auf Build-Ausgaben. Kann auf bestimmte Jobs/Ordner beschränkt werden. |
| **Konfigurieren/Modifizieren** | - `Job/Configure`<br>- `Job/Create`<br>- `Job/Delete`<br>- `Folder/Configure`            | Ermöglicht das Bearbeiten von Job-Parametern, Hinzufügen von Triggern oder Verwalten von Unterelementen. |
| **Administrativ** | - `Overall/Administer`<br>- `Overall/Configure`<br>- `Group/Manage`<br>- `Role/View`     | Volle Systemkontrolle oder delegierte Aufgaben wie das Verwalten von Rollen/Gruppen. `Overall/Administer` ist die Super-User-Berechtigung. |
| **Sonstige**         | - `SCM/Tag`<br>- `Credentials/View`<br>- `Agent/Launch`<br>- `RunScripts`                | SCM-Operationen, Credential-Zugriff, Node-Management oder Skriptausführung. Negation (z.B. `-Job/Build`) kann vererbte Rechte einschränken. |

Zugriffsrechte werden in mehreren Bereichen kontrolliert:
- **Global**: Gilt für die gesamte Instanz (z.B. über Root-Level-Gruppen).
- **Objekt-spezifisch**: Wird für Jobs, Ordner oder Agents überschrieben (z.B. ein Team kann nur in seinem Ordner bauen).
- **Weitergabe**: Rollen werden automatisch an Kinder vererbt, sofern sie nicht "gepinnt" (lokal überschrieben) oder gefiltert werden (z.B. ein Projekt vor einer Rolle verstecken).
- **Implikationen**: Bestimmte Berechtigungen gewähren automatisch untergeordnete Rechte (in neueren Versionen für Sicherheit konfigurierbar).

Admins können Rollen filtern, um die Weitergabe zu verhindern (z.B. über **Roles > Filter** bei einem Job), oder nicht filterbare Rollen für erzwungenen globalen Zugriff verwenden.

#### Verwalten von Benutzerrollen
Rollen sind vordefinierte Berechtigungssätze:
1. Gehen Sie zu **Manage Jenkins > Manage Roles**.
2. Klicken Sie auf **Add Role** und benennen Sie sie (z.B. "Developer").
3. Weisen Sie Berechtigungen zu, indem Sie Kästchen ankreuzen (verwenden Sie "Check all" oder "Clear all" für Massenaktionen). Systemrollen wie "anonymous" (für nicht authentifizierte Benutzer) und "authenticated" (eingeloggte Benutzer) sind vorgebaut und können nicht gelöscht werden.
4. Speichern. Rollen können als "non-filterable" markiert werden, um sie immer global anzuwenden.

Benutzer erben Berechtigungen von Rollen, die ihren Gruppen zugewiesen sind – keine direkte Benutzer-Rollen-Zuweisung; es ist gruppenbasiert für Skalierbarkeit.

#### Zuweisen von Rollen zu Gruppen und Benutzern
Gruppen bündeln Benutzer und Rollen und ermöglichen einfache Delegation:
1. Gehen Sie bei einem Objekt (z.B. Root, Ordner oder Job) zu **Groups > New Group**.
2. Geben Sie einen Gruppennamen ein (z.B. "DevTeam").
3. Weisen Sie Rollen zu, indem Sie sie ankreuzen (wird standardmäßig an Kinder weitergegeben; deaktivieren Sie die Option, um lokal anzupinnen).
4. Fügen Sie Mitglieder hinzu (siehe unten).
5. Speichern.

Gruppen unterstützen Verschachtelung (z.B. Untergruppen) und externe Integration (z.B. LDAP-Gruppen).

#### Wie Admins einen Benutzer zu einer Gruppe hinzufügen
Admins mit der `Group/Manage`-Berechtigung können Mitgliedschaften bearbeiten:
1. Navigieren Sie zur Konfiguration der Gruppe (z.B. **Groups** auf Root oder Objekt).
2. Klicken Sie im Abschnitt "Members" auf **Add user** (oder **Add group** für externe/verschachtelte Gruppen).
3. Geben Sie die Benutzer-ID ein (z.B. Benutzername aus der Jenkins-Benutzerdatenbank, LDAP-DN oder externer Gruppenname). Verwenden Sie `/whoAmI`, um IDs zu überprüfen.
4. Klicken Sie auf **Add** und speichern. Bestätigen Sie die Entfernung bei Bedarf mit einer Abfrage.
5. Für Massenaktionen/Automatisierung:
   - CLI verwenden: `java -jar jenkins-cli.jar group-membership <object-path> <group-name> <user-id>` (listet/setzt Mitglieder).
   - REST API: POST an `/rbac/api/v1/groups/<group>/members` mit JSON-Payload.

Vermeiden Sie zirkuläre Gruppenmitgliedschaften, um Schleifen zu verhindern. Für externe Realms (z.B. Active Directory) konfigurieren Sie zuerst den Security Realm unter **Manage Security > Security Realm**.

Dieser Aufbau gewährleistet eine sichere, skalierbare Kontrolle – z.B. erhalten Entwickler `Job/Build` + `Job/Read` in ihrem Ordner, während Admins alles verwalten.

[Zugriff einschränken und Administration delegieren mit Role-Based Access Control](https://docs.cloudbees.com/docs/cloudbees-ci/latest/secure/rbac)