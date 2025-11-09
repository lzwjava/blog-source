---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Microsoft Entra ID Zugriffsverwaltungsleitfaden
translated: true
type: note
---

Microsoft Entra ID ist ein cloudbasierter Identitäts- und Zugriffsverwaltungsdienst, der den gesicherten Zugriff auf Ressourcen wie Anwendungen, Daten und Geräte unterstützt. Er unterstützt Authentifizierung (z. B. Anmeldemethoden, MFA), Autorisierung (z. B. rollenbasierter Zugriff) und Integration mit Azure-Diensten. Für den Einstieg benötigen Sie ein Azure-Abonnement und entsprechende Berechtigungen (z. B. die Rolle "Globaler Administrator").

## Erste Schritte
1.  **Melden Sie sich beim Azure-Portal an**: Gehen Sie zu [portal.azure.com](https://portal.azure.com) und melden Sie sich mit Ihrem Microsoft-Konto an.
2.  **Navigieren Sie zu Microsoft Entra ID**: Suchen Sie in der oberen Suchleiste nach "Microsoft Entra ID" oder finden Sie es unter "Azure-Dienste".
3.  **Erkunden Sie das Dashboard**: Überprüfen Sie Ihre Mandantenübersicht, einschließlich Benutzer, Gruppen und Apps. Richten Sie bei Bedarf Grundlagen wie benutzerdefinierte Domänen ein.
4.  **Aktivieren Sie Schlüsselfunktionen**:
    - **Authentifizierung**: Konfigurieren Sie die Self-Service-Kennwortzurücksetzung oder Multi-Faktor-Authentifizierung (MFA) unter "Authentifizierungsmethoden".
    - **Bedingter Zugriff**: Erstellen Sie Richtlinien unter "Sicherheit" > "Bedingter Zugriff", um Regeln basierend auf Benutzer, Gerät oder Standort durchzusetzen.

## Verwalten von Benutzern und Gruppen
-   **Benutzer hinzufügen**: Gehen Sie zu "Benutzer" > "Neuer Benutzer". Geben Sie Details wie Name, Benutzername (z. B. user@ihredomain.com) ein und weisen Sie Rollen oder Lizenzen zu.
-   **Gruppen erstellen**: Wählen Sie unter "Gruppen" > "Neue Gruppe" den Typ "Sicherheit" oder "Microsoft 365", fügen Sie Mitglieder hinzu und verwenden Sie diese für Zugriffszuweisungen.
-   **Lizenzen zuweisen**: Gehen Sie in den Benutzer-/Gruppendetails zu "Lizenzen", um Entra ID P1/P2 für erweiterte Funktionen wie Privileged Identity Management (PIM) zuzuweisen.
-   **Bewährte Methode**: Befolgen Sie das Prinzip der geringsten Rechte – weisen Sie minimale Berechtigungen zu und verwenden Sie Gruppen für die Massenverwaltung.

## Verwalten von Anwendungen
-   **App registrieren**: Geben Sie unter "App-Registrierungen" > "Neue Registrierung" Name, Umleitungs-URIs und unterstützte Kontotypen (Single-Tenant, Multi-Tenant usw.) an.
-   **Unternehmens-Apps hinzufügen**: Für Drittanbieter-Apps gehen Sie zu "Unternehmensanwendungen" > "Neue Anwendung", um den Katalog zu durchsuchen oder Nicht-Katalog-Apps zu erstellen.
-   **Zugriff konfigurieren**: Weisen Sie der App unter "Benutzer und Gruppen" Benutzer/Gruppen zu und richten Sie Single Sign-On (SSO) über SAML oder OAuth ein.
-   **Identitäten bereitstellen**: Automatisieren Sie die Benutzersynchronisation mit Apps unter "Bereitstellung" für Just-in-Time-Zugriff.

Für Hybrid-Setups (lokale AD) verwenden Sie Microsoft Entra Connect zum Synchronisieren von Identitäten. Überwachen Sie die Nutzung über Protokolle unter "Überwachung" > "Anmeldeprotokolle".

# So überprüfen Sie den Zugriff auf eine Datenbank, Kubernetes (AKS) oder andere Ressource

Der Zugriff in Azure wird über die rollenbasierte Zugriffssteuerung (RBAC) verwaltet, die in Entra ID integriert ist. Benutzer authentifizieren sich mit Entra-Anmeldeinformationen, und Rollen definieren Berechtigungen. Um den Zugriff zu überprüfen, verwenden Sie die IAM-Tools (Identity and Access Management) des Azure-Portals. Diese listen direkte Zuweisungen, von übergeordneten Bereichen (z. B. Abonnement) geerbte Zuweisungen und Ablehnungszuweisungen auf.

## Allgemeine Schritte für jede Azure-Ressource
1.  **Öffnen Sie die Ressource**: Navigieren Sie im Azure-Portal zu der Ressource (z. B. Ressourcengruppe, VM, Speicherkonto).
2.  **Gehen Sie zu Zugriffssteuerung (IAM)**: Wählen Sie im linken Menü "Zugriffssteuerung (IAM)".
3.  **Zugriff überprüfen**:
    - Für Ihren eigenen Zugriff: Klicken Sie auf "Zugriff überprüfen" > "Meinen Zugriff anzeigen", um Zuweisungen in diesem Bereich und geerbte Zuweisungen zu sehen.
    - Für einen bestimmten Benutzer/eine Gruppe/einen Dienstprinzipal:
        - Klicken Sie auf "Zugriff überprüfen" > "Zugriff überprüfen".
        - Wählen Sie "Benutzer, Gruppe oder Dienstprinzipal".
        - Suchen Sie nach Name oder E-Mail.
        - Sehen Sie sich den Ergebnisbereich für Rollenzuweisungen (z. B. "Besitzer", "Mitwirkender") und effektive Berechtigungen an.
4.  **Berechtigte Zuweisungen anzeigen** (bei Verwendung von PIM): Wechseln Sie zum Tab "Berechtigte Zuweisungen" für Just-in-Time-Rollen.
5.  **PowerShell/CLI-Alternative**: Verwenden Sie `az role assignment list --assignee <Benutzer> --scope <Ressourcen-ID>` für scriptbasierte Überprüfungen.

Hinweis: Dies schließt keine Zuweisungen aus untergeordneten Bereichen ein; bei Bedarf tiefer gehen.

## Überprüfen des Zugriffs auf Azure SQL-Datenbank
Azure SQL verwendet die Entra-Authentifizierung für enthaltene Datenbankbenutzer (verknüpft mit Entra-Identitäten, nicht mit SQL-Anmeldungen).
1.  **Entra-Admin konfigurieren (falls nicht festgelegt)**: In der SQL-Server-Übersicht > "Microsoft Entra ID" unter Einstellungen > "Admin festlegen". Suchen und wählen Sie einen Benutzer/eine Gruppe aus und speichern Sie. Dies aktiviert die Entra-Authentifizierung clusterweit.
2.  **Serverweiten Zugriff überprüfen**:
    - Im SQL-Server-Bereich > "Microsoft Entra ID" sehen Sie das Admin-Feld, um die zugewiesene Identität anzuzeigen.
    - Abfrage der `master`-Datenbank: `SELECT name, type_desc FROM sys.database_principals WHERE type IN ('E', 'X');` (E für externe Benutzer, X für externe Gruppen).
3.  **Datenbankweiten Zugriff überprüfen**:
    - Verbinden Sie sich mit der Datenbank über SSMS mit Entra-Authentifizierung (im Verbindungsdialog "Microsoft Entra - Universell mit MFA" auswählen).
    - Führen Sie `SELECT * FROM sys.database_principals;` oder `EXEC sp_helprolemember;` aus, um Benutzer und Rollen aufzulisten.
4.  **Fehlerbehebung**: Wenn die Anmeldung fehlschlägt (z. B. Fehler 33134), überprüfen Sie, ob Entra Conditional Access-Richtlinien den Zugriff auf die Microsoft Graph-API erlauben.

Benutzer erhalten standardmäßig `CONNECT`; weisen Sie Rollen wie `db_datareader` über T-SQL zu: `ALTER ROLE db_datareader ADD MEMBER [user@domain.com];`.

## Überprüfen des Zugriffs auf AKS (Kubernetes-Cluster)
AKS integriert Entra ID für die Authentifizierung und verwendet Azure RBAC oder Kubernetes RBAC für die Autorisierung.
1.  **Azure-Ebene-Zugriff (auf AKS-Ressource)**:
    - Befolgen Sie die oben genannten allgemeinen Schritte für die AKS-Clusterressource.
    - Häufige Rollen: "Azure Kubernetes Service-Clusteradministrator" für vollen Kubeconfig-Zugriff; "Leser" für nur Lesezugriff.
2.  **Kubernetes-API-Zugriff**:
    - Authentifizieren Sie sich via `az login` (verwendet Entra-Token).
    - Kubeconfig abrufen: `az aks get-credentials --resource-group <rg> --name <cluster>`.
    - Bindungen überprüfen: `kubectl auth can-i <verb> <resource> --as <user@domain.com> -n <namespace>`.
    - Clusterrollen auflisten: `kubectl get clusterrolebindings | grep <user-or-group>`.
3.  **Verwenden von Entra-Gruppen**: Weisen Sie Kubernetes-Rollen/Bindungen Gruppen für Skalierbarkeit zu. Beispiel-YAML für eine Namespace-Rolle (anwenden mit `kubectl apply -f file.yaml`):
    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: example-binding
      namespace: default
    subjects:
    - kind: Group
      name: finance-group  # Entra-Gruppe
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: example-role
      apiGroup: rbac.authorization.k8s.io
    ```
4.  **Bewährte Methoden**: Verwenden Sie Rollen mit geringsten Rechten, integrieren Sie PIM für Just-in-Time-Rechteerhöhungen und vermeiden Sie feste Anmeldeinformationen – verwenden Sie Workload-Identities für Pods.

Für Pods, die auf Ressourcen zugreifen (z. B. SQL von AKS), weisen Sie verwaltete Identitäten zu und überprüfen Sie diese über Azure RBAC auf diese Identitäten.

[Microsoft Entra ID-Dokumentation](https://learn.microsoft.com/en-us/entra/identity/)  
[Zugriff auf eine einzelne Azure-Ressource überprüfen](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access)  
[Konfigurieren der Entra-Authentifizierung für Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-configure?view=azuresql)  
[AKS-Identitäts- und Zugriffsbewährte Methoden](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-identity)