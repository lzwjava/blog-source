---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: AWS IAM Zugriffsverwaltungsleitfaden
translated: true
type: note
---

AWS Identity and Access Management (IAM) ist ein kostenloser Service, der Ihnen hilft, den Zugriff auf AWS-Ressourcen sicher zu steuern. Er ermöglicht Ihnen die Verwaltung von Benutzern und deren Berechtigungen, um sicherzustellen, dass die richtigen Personen und Anwendungen den entsprechenden Zugriff auf die richtigen Ressourcen haben. IAM kümmert sich um Authentifizierung (wer sich anmelden kann) und Autorisierung (welche Aktionen sie ausführen können).

## Kernkomponenten von IAM

- **Benutzer**: Stellt Personen oder Anwendungen dar, die Zugriff auf AWS benötigen. Jeder Benutzer hat eindeutige Sicherheitsanmeldeinformationen (z. B. Passwörter oder Zugriffsschlüssel).
- **Gruppen**: Sammlungen von Benutzern zur einfacheren Berechtigungsverwaltung. Berechtigungen werden Gruppen und nicht direkt einzelnen Benutzern zugewiesen.
- **Rollen**: Temporäre Identitäten mit Berechtigungen, die von Benutzern, Diensten oder Anwendungen angenommen werden können. Rollen haben keine permanenten Anmeldeinformationen; sie stellen kurzlebige Sicherheitstoken bereit.
- **Richtlinien**: JSON-Dokumente, die Berechtigungen definieren. Sie legen Aktionen (z. B. Lesen, Schreiben), Ressourcen (z. B. S3-Buckets) und Bedingungen (z. B. IP-Einschränkungen) fest. Es gibt AWS-verwaltete, kundenverwaltete und Inline-Richtlinien.

## Erste Schritte: Schritt-für-Schritt-Anleitung

### Voraussetzungen
- Melden Sie sich als Root-Benutzer (die E-Mail-Adresse und das Passwort Ihres Kontos) bei der AWS Management Console an. **Wichtig**: Vermeiden Sie die Nutzung des Root-Benutzers für tägliche Aufgaben – erstellen Sie sofort einen Administrator-Benutzer.
- Aktivieren Sie die Multi-Faktor-Authentifizierung (MFA) für den Root-Benutzer für zusätzliche Sicherheit.

### 1. Einen IAM-Benutzer erstellen
Verwenden Sie für Einfachheit die AWS Management Console (CLI- oder API-Optionen sind für die Automatisierung verfügbar).

1. Öffnen Sie die IAM-Konsole unter https://console.aws.amazon.com/iam/.
2. Wählen Sie im Navigationsbereich **Benutzer** > **Benutzer erstellen**.
3. Geben Sie einen Benutzernamen ein (z. B. "admin-user") und wählen Sie **Weiter**.
4. Wählen Sie unter **Berechtigungen festlegen** die Option **Richtlinien direkt anfügen** und wählen Sie eine AWS-verwaltete Richtlinie wie "AdministratorAccess" für vollen Zugriff (beginnen Sie in der Produktion mit dem Prinzip der geringsten Rechte).
5. (Optional) Legen Sie ein Konsolenpasswort fest: Wählen Sie **Benutzerdefiniertes Passwort** und aktivieren Sie **Zurücksetzen des Passworts erforderlich**.
6. Überprüfen Sie die Angaben und wählen Sie **Benutzer erstellen**.
7. Stellen Sie dem Benutzer seine Anmelde-URL (z. B. https://[account-alias].signin.aws.amazon.com/console), seinen Benutzernamen und das temporäre Passwort zur Verfügung.

Für programmatischen Zugriff können Sie Zugriffsschlüssel generieren (bevorzugen Sie jedoch Rollen für Anwendungen).

### 2. Gruppen erstellen und verwalten
Gruppen vereinfachen die Skalierung von Berechtigungen.

1. Wählen Sie in der IAM-Konsole **Benutzergruppen** > **Gruppe erstellen**.
2. Geben Sie einen Gruppennamen ein (z. B. "Developers").
3. Fügen Sie Richtlinien an (z. B. "AmazonEC2ReadOnlyAccess").
4. Wählen Sie **Gruppe erstellen**.
5. Um Benutzer hinzuzufügen: Wählen Sie die Gruppe > **Benutzer zur Gruppe hinzufügen** > Wählen Sie bestehende Benutzer aus.

Benutzer erben alle Gruppenberechtigungen. Ein Benutzer kann mehreren Gruppen angehören.

### 3. Richtlinien erstellen und anfügen
Richtlinien definieren, welche Aktionen erlaubt sind.

- **Typen**:
  - AWS-verwaltet: Vorgefertigt für häufige Aufgaben (z. B. "ReadOnlyAccess").
  - Kundenverwaltet: Benutzerdefinierte JSON-Datei für Ihre Anforderungen.
  - Inline: Direkt in einen Benutzer/eine Gruppe/eine Rolle eingebettet (sparsam verwenden).

So erstellen Sie eine benutzerdefinierte Richtlinie:
1. Wählen Sie in der IAM-Konsole **Richtlinien** > **Richtlinie erstellen**.
2. Verwenden Sie den visuellen Editor oder den JSON-Tab (z. B. Erlauben von "s3:GetObject" für einen bestimmten Bucket).
3. Geben Sie einen Namen ein und wählen Sie **Richtlinie erstellen**.
4. Hängen Sie sie über **Richtlinie anfügen** an Benutzer/Gruppen/Rollen an.

Bewährte Methode: Gewähren Sie die geringsten Rechte – beginnen Sie breit und verfeinern Sie dann mit Tools wie IAM Access Analyzer.

### 4. IAM-Rollen verwenden
Rollen sind ideal für temporären Zugriff und vermeiden langfristige Anmeldeinformationen.

1. Wählen Sie in der IAM-Konsole **Rollen** > **Rolle erstellen**.
2. Wählen Sie die vertrauenswürdige Entität (z. B. "AWS service" für EC2 oder "Another AWS account" für kontountibergreifenden Zugriff).
3. Fügen Sie Berechtigungsrichtlinien an.
4. Fügen Sie eine Vertrauensrichtlinie hinzu (JSON, das definiert, wer die Rolle annehmen darf, z. B. EC2 Service Principal).
5. Geben Sie einen Namen ein und wählen Sie **Rolle erstellen**.

**Häufige Szenarien**:
- **EC2-Instances**: Hängen Sie eine Rolle an eine Instanz an, um sicheren Zugriff auf andere Dienste (z. B. S3) zu ermöglichen, ohne Schlüssel einzubetten.
- **Kontountibergreifender Zugriff**: Erstellen Sie in Konto A (dem vertrauenden Konto) eine Rolle mit einer Vertrauensrichtlinie, die Prinzipale aus Konto B erlaubt. Benutzer in B nehmen die Rolle über AWS STS an, um auf Ressourcen von A zuzugreifen.

Nehmen Sie eine Rolle über die Konsole, die CLI (`aws sts assume-role`) oder SDKs an, um temporäre Anmeldeinformationen zu erhalten.

### 5. MFA und zusätzliche Sicherheit aktivieren
- Für Benutzer: In der IAM-Konsole > Benutzer > Benutzer auswählen > **Sicherheitsanmeldeinformationen** > MFA verwalten.
- Verwenden Sie virtuelle (app-basierte) oder Hardware-MFA-Geräte.

## Bewährte Methoden für Sicherheit
- **Root-Benutzer sperren**: Verwenden Sie ihn nur für Aufgaben, die ihn erfordern (z. B. Ändern von Kontoeinstellungen). Aktivieren Sie MFA und erstellen Sie keine Zugriffsschlüssel.
- **Temporäre Anmeldeinformationen verwenden**: Bevorzugen Sie Federation (z. B. über IAM Identity Center) und Rollen gegenüber langfristigen Schlüsseln. Rotieren Sie Schlüssel, falls verwendet.
- **Prinzip der geringsten Rechte**: Gewähren Sie minimale Berechtigungen; verwenden Sie Bedingungen (z. B. Zeit-/IP-Beschränkungen) in Richtlinien.
- **Überwachen und Prüfen**: Aktivieren Sie AWS CloudTrail, verwenden Sie IAM Access Analyzer, um ungenutzte Berechtigungen oder unbeabsichtigten Zugriff zu erkennen, und überprüfen Sie die "Zuletzt verwendet"-Informationen.
- **Ungenutzte Ressourcen entfernen**: Löschen Sie regelmäßig inaktive Benutzer/Rollen/Richtlinien.
- **Für Multi-Account**: Verwenden Sie AWS Organizations mit Service Control Policies (SCPs) als Schutzmaßnahmen.
- **Richtlinien validieren**: Verwenden Sie die Richtlinienprüfung des IAM Access Analyzers, bevor Sie sie anwenden.

Für praktisches Lernen erkunden Sie IAM-Tutorials in der Konsole oder in der Dokumentation für Szenarien wie attributbasierte Zugriffskontrolle (ABAC).

## Referenzen
- [Was ist IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Einen IAM-Benutzer erstellen](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [IAM-Gruppen](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [IAM-Rollen](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [IAM-Bewährte Methoden](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM-Tutorials](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorials.html)