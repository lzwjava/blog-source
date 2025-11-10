---
audio: false
generated: true
image: false
lang: de
layout: post
title: Mac-Sicherheit entspricht Windows-Banken
translated: true
type: note
---

Das ist eine gute Frage – große Banken wie **HSBC** oder **DBS** operieren mit extrem strengen Endpunkt-Sicherheitsvorkehrungen, und traditionell waren die meisten dieser Setups auf Windows ausgelegt. Aber Macs können genauso streng kontrolliert werden; die Werkzeuge sind etwas anders, obwohl die Ziele (VPN, Internetzugangskontrollen, Rechteverwaltung, Monitoring, Compliance) dieselben sind. Lassen Sie es mich für Sie aufschlüsseln.

---

## 1. **VPN & Netzwerkzugangskontrolle**

* **Windows (heute üblich)**: Cisco AnyConnect (VPN), Zscaler oder Palo Alto GlobalProtect. Oft gekoppelt an Active Directory und Network Access Control (NAC).
* **Mac-Entsprechungen**:

  * Cisco AnyConnect, GlobalProtect, Zscaler und Fortinet haben alle **macOS Agents**.
  * Dieselbe Integration mit **zertifikatbasierter Authentifizierung** und MFA (RSA SecurID, Duo, etc.).
  * NAC-Richtlinien können prüfen, ob der Mac verschlüsselt (FileVault), gepatcht ist und Endpoint Protection ausgeführt wird, bevor die VPN-Verbindung erlaubt wird.

---

## 2. **Administrative Rechte & Rechteverwaltung**

* **Windows**: Die IT blockiert normalerweise lokale Admin-Rechte über Group Policy (GPO). Wenn eine App höhere Rechte benötigt, müssen Benutzer die IT oder Privileged Access Management (PAM) Tools durchlaufen.
* **Mac**:

  * **Mobile Device Management (MDM)** Frameworks (Jamf Pro, Kandji, Intune, VMware Workspace ONE) erlauben es der IT, **Admin-Rechte** von macOS-Benutzern **zu entfernen**.
  * Einige Banken setzen **Just-in-Time (JIT) Rechteerweiterung** über Tools wie BeyondTrust oder CyberArk EPM für Mac ein. Das bedeutet, Ingenieure können `sudo` nicht ausführen, es sei denn, die IT genehmigt es oder gewährt ein zeitlich begrenztes Token.
  * Konfigurationsprofile können die Installation unsignierter Apps verhindern, Änderungen an Systemeinstellungen blockieren und Code Signing erzwingen.

---

## 3. **Internetzugangskontrollen**

* **Windows**: Typischerweise erzwungen via Zscaler, Blue Coat, Cisco Umbrella oder der Proxy/Firewall der Bank. Browser werden abgesichert; manchmal nur IE/Edge/Chrome mit benutzerdefinierten Richtlinien.
* **Mac**:

  * Dieselben Anbieter (Zscaler, Umbrella, Palo Alto) unterstützen **macOS Agents**, die gesamten DNS/HTTP/S-Datenverkehr abfangen.
  * Die IT kann **Browser-Einschränkungen** durchsetzen (z.B. Safari deaktiviert, Chrome mit Enterprise-Konfiguration).
  * Einige Banken blockieren direkte ausgehende Verbindungen – nur Datenverkehr, der durch VPN/Proxy getunnelt wird, funktioniert.

---

## 4. **Endpoint Protection & Monitoring**

* **Windows**: Symantec, McAfee, Microsoft Defender for Endpoint, CrowdStrike.
* **Mac**:

  * Alle diese (CrowdStrike, Defender, SentinelOne, Carbon Black) haben **macOS-Versionen**.
  * FileVault-Datenträgerverschlüsselung wird normalerweise erzwungen.
  * macOS **System Integrity Protection (SIP)** fügt eine weitere Schutzschicht gegen Rootkits hinzu.

---

## 5. **Patch- & Softwareverteilung**

* **Windows**: WSUS, SCCM, Intune – Patches werden zentral ausgeliefert.
* **Mac**:

  * Die MDM-API von Apple erlaubt es Banken, **OS-Updates und Sicherheitspatches zu erzwingen**.
  * Jamf oder Intune können genehmigte Software, Zertifikate und Konfigurationen ausspielen.
  * Die IT kann den **App Store sperren**, um die Selbstinstallation zu blockieren.

---

## 6. **Audit & Compliance**

* **Windows**: Group Policy + SIEM (Splunk, ArcSight) sammelt Logs.
* **Mac**:

  * Syslog-Weiterleitung + MDM-Monitoring speist das SIEM.
  * Banken können **vollständige Festplatten-Audit-Logs** vorschreiben, USB-Nutzung verfolgen und Datenexfiltration verhindern.

---

✅ **Das Fazit:**
Alles, was Banken unter Windows tun (VPN-Erzwingung, keine Admin-Rechte, strikte Internetkontrolle, Patch-Erzwingung, Monitoring), kann auch unter **macOS** umgesetzt werden. Der Unterschied ist, dass Banken statt **Group Policy Objects (GPOs)** und SCCM auf **MDM-Plattformen (Jamf, Intune, Workspace ONE)** mit den Management-Frameworks von Apple setzen. Anbieter wie Cisco, Palo Alto, Zscaler, CrowdStrike bieten alle vollständige Mac-Unterstützung.

---

Möchten Sie, dass ich einen **"Banken-tauglichen Mac-Security-Stack"** skizziere (z.B. empfohlenes VPN + MDM + EDR + PAM), der dem, was HSBC/DBS intern einsetzen könnten, am nächsten kommt?