---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erstellen einer Azure API Management-Instanz
translated: true
type: note
---

### Erstellen eines API-Gateways in Azure mit API Management

Azure API Management (APIM) ist der vollständig verwaltete Dienst, der als API-Gateway fungiert und Funktionen wie API-Veröffentlichung, Sicherheit, Analysen und Entwicklerportale bereitstellt. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zur Erstellung einer APIM-Instanz über das Azure-Portal.

#### Voraussetzungen
- Ein aktives Azure-Abonnement. Falls Sie noch keines haben, können Sie ein [kostenloses Azure-Konto](https://azure.microsoft.com/de-de/free/) erstellen.

#### Schritte zur Erstellung einer API Management-Instanz

1. **Beim Azure-Portal anmelden**  
   Rufen Sie das [Azure-Portal](https://portal.azure.com) auf und melden Sie sich mit Ihrem Azure-Konto an.

2. **Eine neue Ressource erstellen**  
   - Wählen Sie im Menü des Azure-Portals **Ressource erstellen**. (Alternativ können Sie **Ressource erstellen** von der Azure-Startseite auswählen.)  
   - Suchen Sie auf der Seite **Ressource erstellen** nach **API Management** und wählen Sie es unter der Kategorie **Integration** aus.  
   - Klicken Sie auf **Erstellen**.

3. **Die Grundeinstellungen konfigurieren**  
   Wechseln Sie auf der Seite **API Management erstellen** zum Tab **Grundlagen** und füllen Sie die Details aus:  
   | Einstellung              | Beschreibung                                                                 |
   |----------------------|-----------------------------------------------------------------------------|
   | Subscription         | Wählen Sie das Azure-Abonnement für diese Instanz.                            |
   | Resource group       | Wählen Sie eine bestehende Ressourcengruppe oder erstellen Sie eine neue (z.B. "APIM-RG").    |
   | Region               | Wählen Sie eine Region in der Nähe Ihrer Benutzer oder Backend-Dienste (z.B. USA, Osten).      |
   | Resource name        | Geben Sie einen eindeutigen Namen ein (z.B. "my-apim-instance"). Dieser wird Teil der Standarddomäne: `<name>.azure-api.net`. Er kann später nicht geändert werden. |
   | Organization name    | Der Name Ihrer Organisation (wird im Entwicklerportal und in E-Mails verwendet).             |
   | Administrator email  | Ihre E-Mail-Adresse für Systembenachrichtigungen.                                        |
   | Pricing tier         | Beginnen Sie mit **Basic v2** für Entwicklung/Test (schnelle Bereitstellung, ~30-40 Minuten). Andere Tarife wie Developer oder Standard bieten mehr Funktionen. |
   | Units                | Belassen Sie den Standardwert 1 für die Evaluierung.                                                |  
   Prüfen Sie die Eingaben und fahren Sie fort.

4. **Optional: Überwachung und Sicherheit konfigurieren**  
   Auf dem Tab **Überwachen + schützen**:  
   - Aktivieren Sie optionale Add-Ons wie Log Analytics für die Protokollierung (kann zusätzliche Kosten verursachen).  
   - Überspringen Sie diesen Schritt vorerst, wenn Sie gerade erst beginnen.

5. **Überprüfen und erstellen**  
   - Validieren Sie Ihre Einstellungen auf dem Tab **Überprüfen + erstellen**.  
   - Klicken Sie auf **Erstellen**. Die Bereitstellung dauert 30-40 Minuten oder länger.  
   - Tipp: Heften Sie die Ressource nach der Erstellung an Ihr Dashboard, um einfachen Zugriff zu haben.

6. **Die Instanz überprüfen**  
   - Suchen Sie im Azure-Portal nach **API Management-Dienste**.  
   - Wählen Sie Ihre neue Instanz aus.  
   - Vergewissern Sie sich auf der Seite **Übersicht**, dass der Status "Online" ist. Sie können jetzt APIs importieren, Richtlinien konfigurieren oder das Entwicklerportal einrichten.

#### Nächste Schritte
- Importieren Sie Ihre erste API: Befolgen Sie das [Tutorial zum Importieren und Veröffentlichen einer API](https://learn.microsoft.com/de-de/azure/api-management/import-and-publish).  
- Sichern Sie sie: Fügen Sie Richtlinien für Authentifizierung, Ratenbegrenzung etc. hinzu.  
- Bereinigen: Löschen Sie bei Tests die Ressourcengruppe über das Portal, um Gebühren zu vermeiden (suchen Sie nach **Ressourcengruppen** > Gruppe auswählen > **Ressourcengruppe löschen**).  

Informationen zu benutzerdefinierten Domänen oder erweiterten Konfigurationen finden Sie in der [APIM-Dokumentation](https://learn.microsoft.com/de-de/azure/api-management/).

[Schnellstart: Erstellen einer Azure API Management-Instanz – Portal](https://learn.microsoft.com/de-de/azure/api-management/get-started-create-service-instance)  
[Übersicht über Azure API Management](https://learn.microsoft.com/de-de/azure/api-management/api-management-key-concepts)