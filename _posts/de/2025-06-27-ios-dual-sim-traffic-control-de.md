---
audio: false
generated: true
lang: de
layout: post
title: Verwaltung des Dual-SIM-Datenverkehrs unter iOS mit GFW-Überlegungen
translated: true
type: note
---

iOS bietet APIs, mit denen Sie bei Verwendung der Dual-SIM-Funktionalität den Netzwerkverkehr für verschiedene Mobilfunkdaten-Tarife verwalten und trennen können. Es gibt jedoch Einschränkungen, und eine direkte Kontrolle über das Routing bestimmten Verkehrs zu bestimmten SIMs basierend auf den Beschränkungen der Great Firewall of China (GFW) wird nativ nicht auf granularer Ebene unterstützt. Mit einer Kombination aus iOS-APIs, manueller Konfiguration und potenziell Tools von Drittanbietern können Sie jedoch ein gewisses Maß an Trennung erreichen, um den Datenverkehr für eine Macau-SIM und eine China Telecom SIM unterschiedlich zu behandeln. Im Folgenden werden die relevanten APIs, Konfigurationen und Überlegungen skizziert, einschließlich der Bewältigung GFW-bezogener Herausforderungen.

### Wichtige iOS-APIs und Funktionen für Dual SIM und Verkehrsverwaltung

1.  **CoreTelephony Framework**:
    *   **Zweck**: Bietet Zugriff auf mobilfunkbezogene Informationen und Konfigurationen für Dual-SIM-Geräte.
    *   **Wichtige Klassen**:
        *   `CTCellularPlanProvisioning`: Ermöglicht das Hinzufügen oder Verwalten von Mobilfunk-Tarifen (z.B. eSIM oder physische SIM).
        *   `CTTelephonyNetworkInfo`: Bietet Informationen über verfügbare Mobilfunk-Tarife und deren Eigenschaften, wie den Anbieternamen, den Mobile Country Code (MCC) und den Mobile Network Code (MNC).
        *   `CTCellularData`: Überwacht die Mobilfunkdatennutzung und den Netzwerkstatus (z.B. ob Mobilfunkdaten aktiviert sind).
    *   **Einschränkungen**: CoreTelephony ermöglicht das Abfragen und Verwalten von Mobilfunk-Tarifen, bietet aber keine direkte Kontrolle über das Routing bestimmten App-Verkehrs zu einer bestimmten SIM. Sie können erkennen, welche SIM für Daten aktiv ist, können aber bestimmten Verkehr (z.B. für eine bestimmte App oder ein Ziel) nicht programmgesteuert auf API-Ebene einer SIM zuweisen.

2.  **NetworkExtension Framework**:
    *   **Zweck**: Ermöglicht erweiterte Netzwerkkonfigurationen, wie das Erstellen benutzerdefinierter VPNs oder das Verwalten von Netzwerkverkehrsregeln.
    *   **Wichtige Funktionen**:
        *   **NEVPNManager**: Ermöglicht das Konfigurieren und Verwalten von VPN-Verbindungen, die verwendet werden können, um Datenverkehr über einen bestimmten Server zu leiten und so GFW-Beschränkungen zu umgehen.
        *   **NEPacketTunnelProvider**: Zum Erstellen benutzerdefinierter VPN-Tunnel, die konfiguriert werden können, um bestimmten Datenverkehr über eine Macau-SIM zu leiten und so GFW-Beschränkungen zu vermeiden.
    *   **Anwendungsfall für GFW**: Durch Einrichten eines VPN auf der Macau-SIM (die nicht der GFW-Zensur unterliegt, da Macaus Netzwerke unabhängig sind), können Sie Datenverkehr über einen Server außerhalb des chinesischen Festlands leiten, um auf blockierte Dienste wie Google, WhatsApp oder YouTube zuzugreifen.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)
    *   **Einschränkungen**: VPN-Konfigurationen werden normalerweise auf Systemebene und nicht pro SIM angewendet. Sie müssten die aktive Daten-SIM manuell wechseln oder eine benutzerdefinierte VPN-Lösung verwenden, um den Datenverkehr selektiv zu routen.

3.  **Dual-SIM-Konfiguration (einstellungsbasiert)**:
    *   iOS unterstützt Dual SIM Dual Standby (DSDS) auf kompatiblen iPhones (z.B. iPhone XS, XR oder neuer, gekauft in Regionen wie Macau oder Hongkong, die Dual SIM mit zwei Nano-SIMs oder eSIM unterstützen). Dies ermöglicht Ihnen:[](https://support.apple.com/en-us/109317)[](https://support.apple.com/en-us/108898)
        *   Eine Standard-SIM für Mobilfunkdaten zuzuweisen (Einstellungen > Mobilfunk > Mobilfunkdaten).
        *   „Mobilfunkdaten-Wechsel zulassen“ zu aktivieren, um automatisch zwischen SIMs basierend auf Empfang oder Verfügbarkeit zu wechseln (Einstellungen > Mobilfunk > Mobilfunkdaten > Mobilfunkdaten-Wechsel zulassen).[](https://support.apple.com/en-us/108898)
        *   SIMs zu benennen (z.B. „Macau-SIM“ für uneingeschränkten Zugang, „China Telecom“ für lokale Dienste) und manuell auszuwählen, welche SIM Daten für bestimmte Aufgaben verarbeitet.
    *   **Manuelle Verkehrstrennung**: Sie können die aktive Daten-SIM in den Einstellungen manuell wechseln, um den gesamten Mobilfunkverkehr entweder über die Macau-SIM (zur Umgehung der GFW) oder die China Telecom SIM (für lokale Dienste, die der GFW unterliegen) zu leiten. iOS bietet jedoch keine API, um Datenverkehr dynamisch basierend auf App oder Ziel ohne Benutzereingriff einer bestimmten SIM zuzuordnen.

4.  **App-spezifisches VPN (NetworkExtension)**:
    *   iOS unterstützt app-spezifische VPN-Konfigurationen über die Klassen `NEAppProxyProvider` oder `NEAppRule` im NetworkExtension-Framework, typischerweise verwendet in Unternehmensumgebungen (z.B. Managed App Configurations).
    *   **Anwendungsfall**: Sie könnten ein app-spezifisches VPN konfigurieren, um Datenverkehr von bestimmten Apps (z.B. YouTube, Google) über einen VPN-Tunnel unter Verwendung der Datenverbindung der Macau-SIM zu leiten, um GFW-Beschränkungen zu umgehen, während andere Apps die China Telecom SIM für lokale Dienste verwenden.
    *   **Voraussetzungen**: Dies erfordert eine benutzerdefinierte VPN-App oder eine Enterprise-Mobile Device Management (MDM)-Lösung, die für einzelne Entwickler komplex zu implementieren ist. Zusätzlich müssten Sie sicherstellen, dass die Macau-SIM als aktive Daten-SIM eingestellt ist, wenn das VPN verwendet wird.

5.  **URLSession und benutzerdefinierte Netzwerkkonfiguration**:
    *   Die `URLSession`-API ermöglicht es Ihnen, Netzwerkanfragen mit bestimmten Mobilfunk-Schnittstellen zu konfigurieren, indem Sie `allowsCellularAccess` verwenden oder durch Bindung an eine bestimmte Netzwerkschnittstelle.
    *   **Anwendungsfall**: Sie können den Mobilfunkzugriff für bestimmte Anfragen programmgesteuert deaktivieren (erzwingen von Wi-Fi oder einer anderen Schnittstelle) oder ein VPN zur Datenverkehrsleitung verwenden. Die Bindung bestimmter Anfragen an eine bestimmte Mobilfunk-Schnittstelle einer SIM wird jedoch nicht direkt unterstützt; Sie müssten sich auf die aktive Daten-SIM-Einstellung des Systems verlassen.
    *   **Workaround**: Kombinieren Sie `URLSession` mit einem VPN, das für die Verwendung der Daten der Macau-SIM konfiguriert ist, um Datenverkehr zu Servern außerhalb Chinas zu leiten.

### Umgang mit GFW-Beschränkungen mit Dual SIMs

Die Great Firewall of China (GFW) blockiert den Zugriff auf viele ausländische Websites und Dienste (z.B. Google, YouTube, WhatsApp), wenn Festland-Anbieter wie China Telecom verwendet werden, da deren Datenverkehr durch die zensierte Infrastruktur Chinas geleitet wird. Im Gegensatz dazu leitet eine Macau-SIM (z.B. von CTM oder Three Macau) den Datenverkehr durch Macaus unabhängige Netzwerke, die nicht der GFW-Zensur unterliegen (außer China Telecom Macau, die GFW-Beschränkungen durchsetzt). So können Sie dies mit einer Macau-SIM und einer China Telecom SIM nutzen:[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)

1.  **Macau-SIM für uneingeschränkten Zugang**:
    *   Verwenden Sie die Macau-SIM als Standard-Mobilfunkdatentarif für Apps oder Dienste, die von der GFW blockiert werden (z.B. Google, YouTube).
    *   **Konfiguration**:
        *   Gehen Sie zu Einstellungen > Mobilfunk > Mobilfunkdaten und wählen Sie die Macau-SIM.
        *   Stellen Sie sicher, dass Datenroaming für die Macau-SIM aktiviert ist, wenn Sie sich im chinesischen Festland befinden, da der Datenverkehr so über Macaus Netzwerk geleitet wird und die GFW umgeht.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
        *   Optional: Konfigurieren Sie ein VPN (z.B. mit `NEVPNManager`), um den Datenverkehr weiter abzusichern, obwohl für eine Macau-SIM typischerweise kein VPN benötigt wird, um auf blockierte Dienste zuzugreifen.
    *   **API-Unterstützung**: Verwenden Sie `CTTelephonyNetworkInfo`, um zu bestätigen, dass die Macau-SIM für Daten aktiv ist (`dataServiceIdentifier`-Eigenschaft) und um ihren Status zu überwachen.

2.  **China Telecom SIM für lokale Dienste**:
    *   Verwenden Sie die China Telecom SIM für lokale Apps und Dienste (z.B. WeChat, Alipay), die eine chinesische Telefonnummer benötigen oder für Festland-Netzwerke optimiert sind.
    *   **Konfiguration**:
        *   Wechseln Sie manuell zur China Telecom SIM in Einstellungen > Mobilfunk > Mobilfunkdaten, wenn Sie auf lokale Dienste zugreifen.
        *   Seien Sie sich bewusst, dass der Datenverkehr auf dieser SIM GFW-Beschränkungen unterliegt und den Zugriff auf viele ausländische Seiten blockiert, sofern kein VPN verwendet wird.
    *   **API-Unterstützung**: Verwenden Sie `CTCellularData`, um die Mobilfunkdatennutzung zu überwachen und sicherzustellen, dass die richtige SIM aktiv ist. Sie können auch `NEVPNManager` verwenden, um ein VPN für bestimmte Apps zu konfigurieren, um die GFW auf der China Telecom SIM zu umgehen, obwohl die VPN-Zuverlässigkeit in China aufgrund aktiver Blockierung inkonsistent ist.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

3.  **Praktischer Workflow für Verkehrstrennung**:
    *   **Manuelles Wechseln**: Wechseln Sie der Einfachheit halber die aktive Daten-SIM in den Einstellungen basierend auf der Aufgabe (z.B. Macau-SIM für internationale Apps, China Telecom SIM für lokale Apps). Dies ist der einfachste Ansatz, erfordert jedoch Benutzereingriffe.
    *   **VPN für China Telecom SIM**: Wenn Sie auf blockierte Dienste zugreifen müssen, während Sie die China Telecom SIM verwenden, konfigurieren Sie ein VPN mit `NEVPNManager`. Beachten Sie, dass viele VPNs (z.B. ExpressVPN, NordVPN) in China aufgrund von GFW-Blockierung unzuverlässig sein können, testen Sie daher Anbieter wie Astrill oder benutzerdefinierte Lösungen vorab. Einige eSIM-Anbieter (z.B. Holafly, ByteSIM) bieten integrierte VPNs an, die aktiviert werden können, um Beschränkungen zu umgehen.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/chinalife/comments/1ebjcxi/can_you_use_esims_to_get_around_the_firewall/)[](https://esim.holafly.com/internet/mobile-internet-china/)
    *   **App-spezifisches VPN**: Für fortgeschrittene Anwendungen entwickeln Sie eine benutzerdefinierte App mit `NEAppProxyProvider`, um Datenverkehr bestimmter Apps über ein VPN zu leiten, wenn die China Telecom SIM aktiv ist, während andere Apps die Macau-SIM direkt verwenden können.
    *   **Automatisierungs-Einschränkungen**: iOS bietet keine API, um die aktive Daten-SIM programmgesteuert basierend auf App oder Ziel-URL zu wechseln. Sie müssten sich auf benutzerinitiiertes SIM-Switching oder ein VPN zur Verwaltung des Datenverkehrs-Routings verlassen.

### Schritte zur Implementierung der Verkehrstrennung

1.  **Dual SIM einrichten**:
    *   Stellen Sie sicher, dass Ihr iPhone Dual SIM unterstützt (z.B. iPhone XS oder neuer mit iOS 12.1 oder neuer).[](https://support.apple.com/en-us/109317)
    *   Setzen Sie die Macau-SIM und die China Telecom SIM ein (oder konfigurieren Sie eine eSIM für eine von beiden).
    *   Gehen Sie zu Einstellungen > Mobilfunk, benennen Sie die Tarife (z.B. „Macau“ und „China Telecom“) und legen Sie die Standard-Daten-SIM fest (z.B. Macau für uneingeschränkten Zugang).[](https://support.apple.com/en-us/108898)

2.  **Mobilfunkdaten-Einstellungen konfigurieren**:
    *   Deaktivieren Sie „Mobilfunkdaten-Wechsel zulassen“, um automatisches SIM-Switching zu verhindern und manuelle Kontrolle darüber zu haben, welche SIM für Daten verwendet wird (Einstellungen > Mobilfunk > Mobilfunkdaten > Mobilfunkdaten-Wechsel zulassen).[](https://support.apple.com/en-us/108898)
    *   Verwenden Sie `CTTelephonyNetworkInfo`, um programmgesteuert zu überprüfen, welche SIM in Ihrer App für Daten aktiv ist.

3.  **VPN für GFW-Umgehung implementieren**:
    *   Konfigurieren Sie für die China Telecom SIM ein VPN mit `NEVPNManager` oder einer VPN-App eines Drittanbieters (z.B. Astrill, Holaflys integriertes VPN), um GFW-Beschränkungen zu umgehen.
    *   Für die Macau-SIM ist ein VPN möglicherweise nicht notwendig, da deren Datenverkehr außerhalb der zensierten Infrastruktur Chinas geroutet wird.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)

4.  **Datenverkehr überwachen und verwalten**:
    *   Verwenden Sie `CTCellularData`, um die Mobilfunkdatennutzung zu überwachen und sicherzustellen, dass die richtige SIM verwendet wird.
    *   Für erweitertes Routing erkunden Sie `NEPacketTunnelProvider`, um ein benutzerdefiniertes VPN zu erstellen, das Datenverkehr basierend auf App oder Ziel selektiv routet, was jedoch erheblichen Entwicklungsaufwand erfordert.

5.  **Testen und optimieren**:
    *   Testen Sie die Konnektivität im chinesischen Festland mit beiden SIMs, um sicherzustellen, dass die Macau-SIM die GFW wie erwartet umgeht und die China Telecom SIM für lokale Dienste funktioniert.
    *   Überprüfen Sie die VPN-Leistung auf der China Telecom SIM, da die GFW viele VPN-Protokolle aktiv blockiert.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### Einschränkungen und Herausforderungen

*   **Keine native API für dynamisches SIM-Routing**: iOS bietet keine API, um Datenverkehr dynamisch basierend auf App, URL oder Ziel einer bestimmten SIM zuzuordnen. Sie müssen die aktive Daten-SIM manuell wechseln oder ein VPN zur Verwaltung des Datenverkehrs verwenden.
*   **GFW-VPN-Blockierung**: Die GFW blockiert aktiv viele VPN-Protokolle (z.B. IPsec, PPTP), und selbst SSL-basierte VPNs können bei Erkennung gedrosselt werden. Eine Macau-SIM ist oft zuverlässiger, um die GFW ohne VPN zu umgehen.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)
*   **China Telecom SIM-Beschränkungen**: China Telecoms CDMA-basiertes Netzwerk kann Kompatibilitätsprobleme mit einigen ausländischen Telefonen verursachen, obwohl sein LTE/5G-Netzwerk breiter kompatibel ist. Zusätzlich unterliegt sein Datenverkehr der GFW-Zensur, was ein VPN für blockierte Dienste erforderlich macht.[](https://esim.holafly.com/sim-card/china-sim-card/)[](https://yesim.app/blog/mobile-internet-and-sim-card-in-china/)
*   **Registrierung mit echtem Namen**: Sowohl Macau- als auch China Telecom SIMs können eine Registrierung mit echtem Namen erfordern (z.B. Passdetails), was die Einrichtung verkomplizieren kann.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
*   **Leistung**: Roaming mit einer Macau-SIM im chinesischen Festland kann zu langsameren Geschwindigkeiten im Vergleich zu einer lokalen China Telecom SIM führen, insbesondere in ländlichen Gebieten.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### Empfehlungen

*   **Primärstrategie**: Verwenden Sie die Macau-SIM als Standard-Mobilfunkdatentarif für den Zugriff auf blockierte Dienste, da sie die GFW natürlich umgeht, indem sie Datenverkehr durch Macaus unzensierte Netzwerke leitet. Wechseln Sie zur China Telecom SIM für lokale Apps wie WeChat oder Alipay, die eine chinesische Nummer benötigen oder für Festland-Netzwerke optimiert sind.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
*   **VPN als Backup**: Verwenden Sie für die China Telecom SIM einen zuverlässigen VPN-Anbieter (z.B. Astrill oder eSIMs mit integrierten VPNs wie Holafly oder ByteSIM), um auf blockierte Dienste zuzugreifen. Installieren und testen Sie das VPN vor der Einreise nach China, da das Herunterladen von VPN-Apps in China eingeschränkt sein kann.[](https://esim.holafly.com/internet/mobile-internet-china/)[](https://bytesim.com/blogs/esim/mobile-internet-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
*   **Entwicklungsaufwand**: Wenn Sie eine App entwickeln, verwenden Sie `NetworkExtension`, um ein benutzerdefiniertes VPN für selektives Datenverkehrs-Routing zu implementieren, aber beachten Sie, dass dies komplex ist und möglicherweise Enterprise-Berechtigungen erfordert. Für die meisten Benutzer ist manuelles SIM-Switching in Kombination mit einem VPN ausreichend.
*   **Vorbereitung vor der Reise**: Kaufen und aktivieren Sie beide SIMs (oder eSIMs) vor der Ankunft in China, da lokale Richtlinien den Kauf von eSIMs im chinesischen Festland einschränken können. Anbieter wie Nomad oder Holafly ermöglichen beispielsweise den Vorabkauf und die Aktivierung von eSIMs mit integrierter GFW-Umgehung.[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://esim.holafly.com/internet/mobile-internet-china/)

### Codebeispiel

Nachfolgend ein einfaches Beispiel für die Verwendung von `CTTelephonyNetworkInfo` zur Überprüfung des aktiven Mobilfunk-Tarifs und `NEVPNManager` zur Konfiguration eines VPN für die China Telecom SIM:

```swift
import CoreTelephony
import NetworkExtension

// Aktiven Mobilfunk-Tarif prüfen
func checkActiveCellularPlan() {
    let networkInfo = CTTelephonyNetworkInfo()
    if let dataService = networkInfo.serviceCurrentRadioAccessTechnology {
        for (serviceIdentifier, rat) in dataService {
            print("Service: \(serviceIdentifier), Radio Access Technology: \(rat)")
            // Identifizieren, welche SIM aktiv ist (z.B. Macau oder China Telecom)
        }
    }
}

// VPN für China Telecom SIM konfigurieren
func setupVPN() {
    let vpnManager = NEVPNManager.shared()
    vpnManager.loadFromPreferences { error in
        if let error = error {
            print("Fehler beim Laden der VPN-Einstellungen: \(error)")
            return
        }
        
        let vpnProtocol = NEVPNProtocolIKEv2()
        vpnProtocol.serverAddress = "vpn.example.com" // Ersetzen Sie durch Ihren VPN-Server
        vpnProtocol.remoteIdentifier = "vpn.example.com"
        vpnProtocol.authenticationMethod = .certificate // Nach Bedarf konfigurieren
        
        vpnManager.protocolConfiguration = vpnProtocol
        vpnManager.isEnabled = true
        
        vpnManager.saveToPreferences { error in
            if let error = error {
                print("Fehler beim Speichern der VPN-Einstellungen: \(error)")
            } else {
                print("VPN erfolgreich konfiguriert")
            }
        }
    }
}
```

### Fazit

Während iOS keine native API bietet, um Datenverkehr dynamisch basierend auf App oder Ziel bestimmten SIMs zuzuordnen, können Sie Verkehrstrennung erreichen durch:
1.  Verwendung der Macau-SIM für uneingeschränkten Zugang, um die GFW ohne VPN zu umgehen.
2.  Verwendung der China Telecom SIM für lokale Dienste, gepaart mit einem VPN (konfiguriert über `NEVPNManager` oder eine Drittanbieter-App), um auf blockierte Dienste zuzugreifen.
3.  Manuelles Wechseln der aktiven Daten-SIM in den Einstellungen für verschiedene Aufgaben.
4.  Optional: Entwicklung einer benutzerdefinierten VPN-Lösung mit `NetworkExtension` für app-spezifisches Datenverkehrs-Routing, was jedoch komplex ist.

Für den einfachsten Ansatz verlassen Sie sich auf die Macau-SIM für GFW-blockierte Dienste und wechseln zur China Telecom SIM für lokale Bedürfnisse, wobei Sie im Voraus ein zuverlässiges VPN für Letzteres installieren. Testen Sie Konfigurationen immer vor der Reise nach China, da sich die GFW-Richtlinien und die VPN-Zuverlässigkeit schnell ändern können.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://prepaid-data-sim-card.fandom.com/wiki/China)

Wenn Sie weitere Erklärungen oder Hilfe bei spezifischen API-Implementierungen benötigen, lassen Sie es mich wissen!