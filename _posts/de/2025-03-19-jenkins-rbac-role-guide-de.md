---
audio: false
generated: true
image: false
lang: de
layout: post
title: Jenkins RBAC-Leitfaden mit Role-Plugin
translated: true
type: note
---

In Jenkins geht es bei der **rollenbasierten Zugriffskontrolle (RBAC)** darum, festzulegen, wer was und wo tun darf. Standardmäßig hat Jenkins nur ein einfaches Benutzer/Administrator-Modell, aber mit dem **Role-Based Strategy Plugin** (oder ähnlichen Autorisierungsstrategien) können Sie feingranulare Zugriffe definieren.

---

### Grundkonzepte von RBAC in Jenkins

1. **Globale Rollen**
   Diese gelten für die gesamte Jenkins-Instanz. Beispiele:

   * **Admin**: Vollständige Kontrolle.
   * **Read-only**: Kann Jobs einsehen, aber nicht ausführen.
   * **Developer**: Kann Jobs erstellen und konfigurieren.

2. **Projekt/Job-Rollen**
   Sie können Berechtigungen pro Job oder pro Ordner vergeben. Zum Beispiel:

   * Benutzer A kann *Projekt X* bauen, aber *Projekt Y* nicht einsehen.
   * Auftragnehmer können Builds auslösen, aber keine Konfigurationen ändern.

3. **Build-Berechtigungen**
   Berechtigungen können aufgeteilt werden:

   * `Job/Read` (Job-Definition und Build-Verlauf einsehen)
   * `Job/Build` (Builds auslösen)
   * `Job/Configure` (Pipeline oder Einstellungen ändern)
   * `Job/Delete` (Jobs oder Builds entfernen)
   * `Job/Cancel` (laufende Builds abbrechen)

---

### Verwaltung von Job- oder Build-Zugriffsrechten

1. **Installieren des Role-Based Strategy Plugins**

   * Gehen Sie zu **Manage Jenkins → Plugins → Available Plugins → Role-based Authorization Strategy**.
   * Wählen Sie es nach der Installation unter **Manage Jenkins → Configure Global Security → Authorization** aus.

2. **Rollen definieren**

   * Gehen Sie zu **Manage Jenkins → Manage and Assign Roles**.
   * Erstellen Sie globale Rollen (wie *admin*, *viewer*, *developer*) und Projektrollen (wie *projectX-builder*).
   * Weisen Sie jeder Rolle die benötigten Berechtigungen zu (`Job/Build`, `Job/Configure`, etc.).

3. **Rollen Benutzern/Gruppen zuweisen**

   * Weisen Sie unter **Manage and Assign Roles** Ihre Jenkins-Benutzer (oder LDAP-Gruppen, falls integriert) den Rollen zu.
   * Zum Beispiel:

     * Weise *alice* → `developer` zu
     * Weise *bob* → `viewer` zu
     * Weise *qa-team* → `projectX-builder` zu

4. **Verwenden Sie Folders für bessere Granularität**

   * Organisieren Sie Jobs in **Folders** (über das *Folders Plugin*).
   * Wenden Sie Rollenbeschränkungen auf Ordnerebene an, sodass nur das richtige Team die Jobs darin einsehen/bauen/ändern kann.

---

### Beispielszenarien

* **Developers**: Können die Jobs ihres Teams bauen und konfigurieren, aber keine Admin-Einstellungen ändern.
* **QA Team**: Kann nur Builds auslösen (Pipelines nicht neu konfigurieren).
* **Externe Benutzer**: Können den Job-Status einsehen, aber keine Builds ändern oder auslösen.

---

👉 In der Praxis: Sie halten die Anzahl der **Admins gering**, geben **Developers Configure + Build-Zugriff** auf ihre eigenen Jobs und gewähren anderen **Read-only oder Build-only Rechte**. Dies gewährleistet Konsistenz, reduziert Fehler und schützt sensible Jobs.

---

Möchten Sie, dass ich Ihnen eine **schrittweise Beispielkonfiguration** (mit Rollen, Berechtigungen und Job-Zuordnung) zeige, die einem typischen Enterprise-Setup entspricht?