---
audio: false
generated: true
lang: de
layout: post
title: Verwendung eines AES-verschlüsselten Passworts in WebSphere Liberty
translated: true
---

Um ein AES-verschlüsseltes Passwort aus der `server.xml` von WebSphere Liberty im Squirrel SQL Client zu verwenden, befolgen Sie diese Schritte:

---

### **1. Passwort mit WebSphere Liberty's Tools entschlüsseln**
Das verschlüsselte Passwort (z. B. `password="{aes}ABC123..."`) muss zuerst entschlüsselt werden. Das `securityUtility`-Tool von Liberty kann dies tun, wenn Sie Zugriff auf den für die Verschlüsselung verwendeten Keystore haben.

#### **Befehl zum Entschlüsseln:**
```bash
# Navigieren Sie zum Verzeichnis bin von Liberty
cd /pfad/zu/wlp/bin

# Führen Sie den securityUtility decode Befehl aus
./securityUtility decode \
  --server=<LibertyServerPfad> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePasswort> \
  --source="{aes}ABC123..."
```

Ersetzen Sie:
- `<LibertyServerPfad>`: Pfad zu Ihrem Liberty-Server (z. B. `usr/servers/defaultServer`).
- `<KeyAlias>`: Alias des Schlüssels im Keystore (Standard: `default`).
- `<KeystorePasswort>`: Passwort für den Keystore (Standard: `KeystorePass` wenn unverändert).
- `{aes}ABC123...`: Das verschlüsselte Passwort aus `server.xml`.

---

### **2. Entschlüsseltes Passwort in Squirrel verwenden**
1. Öffnen Sie den Squirrel SQL Client.
2. Erstellen Sie einen neuen Verbindungsalias.
3. In den Verbindungs-Eigenschaften:
   - **Treiber**: Wählen Sie Ihren Oracle JDBC-Treiber.
   - **URL**: Verwenden Sie die JDBC-URL aus der `server.xml` von Liberty (z. B. `jdbc:oracle:thin:@//host:port/service`).
   - **Benutzername**: Der Benutzername aus dem `<dataSource>` von Liberty.
   - **Passwort**: Geben Sie das **entschlüsselte Passwort** ein, das Sie aus Schritt 1 erhalten haben.

---

### **Wichtige Hinweise**
- **Keystore-Zugriff**: Sie benötigen die Keystore-Datei (`key.jks` oder `key.p12`) und deren Passwort. Standardmäßig befindet sie sich im Verzeichnis `resources/security` von Liberty.
- **Sicherheit**: Speichern Sie das entschlüsselte Passwort niemals als Klartext. Geben Sie es direkt in Squirrel ein, ohne es in einer Datei zu speichern.
- **Admin-Hilfe**: Wenn Sie die Keystore-Anmeldeinformationen nicht haben, wenden Sie sich an Ihren Liberty-Administrator, um das Passwort sicher zu entschlüsseln.

---

### **Alternative Vorgehensweise (nicht empfohlen)**
Wenn die Entschlüsselung nicht möglich ist, ersetzen Sie das verschlüsselte Passwort in `server.xml` vorübergehend durch ein Klartext-Passwort (**nur für Tests**). Starten Sie Liberty neu und verwenden Sie das Klartext-Passwort in Squirrel. Kehren Sie danach zum verschlüsselten Passwort zurück.

```xml
<!-- Beispiel: Klartext-Passwort (in der Produktion vermeiden) -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

Durch die Befolgung dieser Schritte können Sie das entschlüsselte Passwort sicher in Squirrel verwenden und gleichzeitig die Einhaltung der Sicherheitsbest Practices gewährleisten.

---

Um den Squirrel SQL-Client mit einer Oracle-Datenbank zu verbinden, die in einer WebSphere Liberty Profile `server.xml`-Datei konfiguriert ist, insbesondere wenn die Oracle JDBC-Treiber-Eigenschaften ein AES-verschlüsseltes Passwort enthalten, befolgen Sie diese Schritte. Der Prozess umfasst das Extrahieren der Verbindungsdetails aus der `server.xml`-Datei, das Handhaben des verschlüsselten Passworts und das entsprechende Konfigurieren von Squirrel SQL. Hier ist eine vollständige Anleitung:

### Schritt 1: `server.xml`-Konfiguration verstehen
In WebSphere Liberty Profile werden Datenbankverbindungen in der `server.xml`-Datei mit einem `<dataSource>`-Element definiert. Dieses Element spezifiziert die Datenquelleneigenschaften, einschließlich derjenigen für eine Oracle-Datenbank über ein verschachteltes `<properties.oracle>`-Element. Eine Beispielkonfiguration könnte so aussehen:

```xml
<dataSource jndiName="jdbc/myOracleDS">
    <jdbcDriver libraryRef="OracleLib"/>
    <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" user="scott" password="{aes}verschlüsseltes_Passwort"/>
</dataSource>
<library id="OracleLib">
    <fileset dir="${server.config.dir}/lib" includes="ojdbc6.jar"/>
</library>
```

Hier:
- **`url`**: Die JDBC-URL zum Verbinden mit der Oracle-Datenbank (z. B. `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **`user`**: Der Datenbank-Benutzername (z. B. `scott`).
- **`password`**: Das mit AES verschlüsselte Passwort, mit `{aes}` als Präfix (z. B. `{aes}verschlüsseltes_Passwort`).
- **`<jdbcDriver>`**: Verweist auf die Oracle JDBC-Treiber JAR-Datei.

Da Squirrel SQL ein eigenständiger Client ist und nicht direkt auf die WebSphere-verwaltete Datenquelle zugreifen kann (z. B. über JNDI-Lookup), müssen Sie es manuell mit denselben Verbindungsdetails konfigurieren.

### Schritt 2: Verbindungsdetails aus `server.xml` extrahieren
Lokalisieren Sie das `<dataSource>`-Element in Ihrer `server.xml`-Datei, das Ihrer Oracle-Datenbank entspricht. Aus dem `<properties.oracle>`-Element notieren Sie sich Folgendes:
- **JDBC-URL**: Gefunden im `url`-Attribut (z. B. `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **Benutzername**: Gefunden im `user`-Attribut (z. B. `scott`).
- **Verschlüsseltes Passwort**: Gefunden im `password`-Attribut (z. B. `{aes}verschlüsseltes_Passwort`).

Die JDBC-URL gibt an, wie mit der Oracle-Datenbank verbunden wird, normalerweise in einem dieser Formate:
- `jdbc:oracle:thin:@//hostname:port/service_name` (Verwendung eines Servicenamens)
- `jdbc:oracle:thin:@hostname:port:SID` (Verwendung einer SID)

Überprüfen Sie Ihre `server.xml`, um die genaue URL zu bestätigen.

### Schritt 3: AES-verschlüsseltes Passwort dekodieren
Das Passwort in der `server.xml` ist mit AES verschlüsselt, was durch das Präfix `{aes}` angezeigt wird. WebSphere Liberty verschlüsselt Passwörter aus Sicherheitsgründen, aber Squirrel SQL benötigt das Klartext-Passwort, um eine Verbindung herzustellen. Um das verschlüsselte Passwort zu dekodieren:

1. **Verwenden Sie das `securityUtility`-Tool von WebSphere**:
   - Dieses Tool ist Teil Ihrer WebSphere Liberty-Installation, normalerweise im `bin`-Verzeichnis (z. B. `<liberty_install_dir>/bin/`).
   - Führen Sie den folgenden Befehl in einem Terminal oder einer Eingabeaufforderung aus dem `bin`-Verzeichnis aus:
     ```
     securityUtility decode --encoding=aes <verschlüsseltes_Passwort>
     ```
     Ersetzen Sie `<verschlüsseltes_Passwort>` durch die tatsächliche verschlüsselte Zeichenfolge aus dem `password`-Attribut (alles nach `{aes}`). Zum Beispiel:
     ```
     securityUtility decode --encoding=aes verschlüsseltes_Passwort
     ```
   - Das Tool gibt das Klartext-Passwort aus.

2. **Alternative**:
   - Wenn Sie keinen Zugriff auf die WebSphere Liberty-Installation oder das `securityUtility`-Tool haben, müssen Sie das Klartext-Passwort von Ihrem Systemadministrator oder der Person, die die Datenquelle konfiguriert hat, erhalten.

Speichern Sie das dekodierte Passwort sicher, da Sie es für Squirrel SQL benötigen.

### Schritt 4: Oracle JDBC-Treiber in Squirrel SQL konfigurieren
Squirrel SQL benötigt den Oracle JDBC-Treiber, um eine Verbindung zur Datenbank herzustellen. Sie benötigen dieselbe Treiber JAR-Datei, die in der `server.xml` `<library>`-Element referenziert wird (z. B. `ojdbc6.jar`).

1. **Treiber JAR erhalten**:
   - Lokalisieren Sie die Oracle JDBC-Treiber JAR-Datei, die im `<fileset>`-Element der `server.xml` angegeben ist (z. B. `ojdbc6.jar` in `${server.config.dir}/lib`).
   - Wenn Sie sie nicht haben, laden Sie die entsprechende Version von Oracles Website herunter (z. B. `ojdbc6.jar` oder `ojdbc8.jar`, passend zur Datenbankversion).

2. **Treiber zu Squirrel SQL hinzufügen**:
   - Öffnen Sie Squirrel SQL.
   - Gehen Sie zur Registerkarte **Treiber** links.
   - Klicken Sie auf das **+**-Symbol, um einen neuen Treiber hinzuzufügen.
   - Konfigurieren Sie den Treiber:
     - **Name**: Geben Sie einen Namen ein (z. B. „Oracle JDBC-Treiber“).
     - **Beispiel-URL**: Geben Sie eine Beispiel-URL ein (z. B. `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Klassenname**: Geben Sie `oracle.jdbc.OracleDriver` ein.
     - **Zusätzlicher Klassenpfad**: Klicken Sie auf **Hinzufügen**, dann durchsuchen Sie und wählen Sie die Oracle JDBC-Treiber JAR-Datei aus.
   - Klicken Sie auf **OK**, um den Treiber zu speichern.

### Schritt 5: Verbindung (Alias) in Squirrel SQL erstellen
Erstellen Sie nun einen Verbindungsalias mit den extrahierten Details:

1. **Neuen Alias hinzufügen**:
   - Gehen Sie zur Registerkarte **Aliases** in Squirrel SQL.
   - Klicken Sie auf das **+**-Symbol, um einen neuen Alias hinzuzufügen.
   - Konfigurieren Sie den Alias:
     - **Name**: Geben Sie einen Namen für die Verbindung ein (z. B. „Oracle DB via WebSphere“).
     - **Treiber**: Wählen Sie den Oracle JDBC-Treiber, den Sie gerade konfiguriert haben.
     - **URL**: Geben Sie die JDBC-URL aus dem `server.xml` `<properties.oracle>`-Element ein (z. B. `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Benutzername**: Geben Sie den Benutzernamen aus der `server.xml` ein (z. B. `scott`).
     - **Passwort**: Geben Sie das dekodierte Klartext-Passwort aus Schritt 3 ein.

2. **Optionale: Zusätzliche Eigenschaften**:
   - Wenn das `<properties.oracle>`-Element in `server.xml` zusätzliche Attribute enthält (z. B. `ssl="true"` oder `connectionTimeout="30000"`), klicken Sie auf die Registerkarte **Eigenschaften** in der Alias-Konfiguration und fügen Sie sie als Schlüssel-Wert-Paare hinzu.

3. **Verbindung testen**:
   - Klicken Sie auf **Verbindung testen**, um zu überprüfen, ob Squirrel SQL eine Verbindung zur Datenbank herstellen kann.
   - Wenn erfolgreich, klicken Sie auf **OK**, um den Alias zu speichern.

### Die JDBC-URL
Die URL, die Sie in Squirrel SQL verwenden, ist der Wert, der im `url`-Attribut des `<properties.oracle>`-Elements in der `server.xml`-Datei angegeben ist. Zum Beispiel:
- Wenn `server.xml` `<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>` hat, dann verwenden Sie:
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

Diese URL, kombiniert mit dem Benutzernamen und dem dekodierten Passwort, ermöglicht es Squirrel SQL, eine Verbindung zur Oracle-Datenbank herzustellen.

### Hinweise
- **Verschlüsseltes Passwort**: Sie können das verschlüsselte Passwort nicht direkt in Squirrel SQL verwenden; es muss in Klartext dekodiert werden.
- **DataSource-Bereich**: Das `<dataSource>` in `server.xml` ist für Anwendungen konzipiert, die in WebSphere Liberty ausgeführt werden. Squirrel SQL, als externer Client, erfordert eine manuelle Konfiguration, die diese Einstellungen spiegelt.
- **JAR-Kompatibilität**: Stellen Sie sicher, dass die Version der Oracle JDBC-Treiber JAR-Datei mit Ihrer Datenbankversion übereinstimmt.

Durch die Befolgung dieser Schritte können Sie Squirrel SQL erfolgreich so konfigurieren, dass es sich mit der Oracle-Datenbank verbindet, die in der WebSphere Liberty Profile `server.xml` konfiguriert ist.

---

Da der `securityUtility`-Befehl in WebSphere Liberty keine Dekodierungsoption für AES-verschlüsselte Passwörter bietet (z. B. solche, die mit `{aes}` in der `server.xml`-Datei vorangestellt sind), müssen Sie einen programmatischen Ansatz verwenden, um diese zu entschlüsseln. Die empfohlene Methode besteht darin, die `com.ibm.websphere.crypto.PasswordUtil`-Klasse zu nutzen, die Teil des Liberty-Runtime ist und solche Passwörter dekodieren kann. Hier sind zwei praktische Lösungen, um dies zu erreichen:

### Option 1: Verwenden einer temporären Webanwendung (empfohlen)
Durch das Bereitstellen einer einfachen Webanwendung auf Ihrem Liberty-Server können Sie die Dekodierungslogik innerhalb der Serverumgebung ausführen, wodurch sichergestellt wird, dass der richtige Verschlüsselungsschlüssel (Standard oder benutzerdefiniert, wie in `server.xml` definiert) verwendet wird.

#### Schritte:
1. **Erstellen Sie eine JSP-Datei**
   Erstellen Sie eine Datei namens `decode.jsp` mit folgendem Inhalt:
   ```jsp
   <%@ page import="com.ibm.websphere.crypto.PasswordUtil" %>
   <%
       String encoded = request.getParameter("encoded");
       if (encoded != null) {
           try {
               String decoded = PasswordUtil.decode(encoded);
               out.println("Dekodiertes Passwort: " + decoded);
           } catch (Exception e) {
               out.println("Fehler beim Dekodieren des Passworts: " + e.getMessage());
           }
       }
   %>
   ```

2. **Bereitstellen der JSP**
   - Legen Sie `decode.jsp` in ein Webanwendungsverzeichnis, z. B. `wlp/usr/servers/yourServer/apps/myApp.war/WEB-INF/`.
   - Wenn nötig, erstellen Sie eine grundlegende WAR-Datei mit dieser JSP und stellen Sie sie über die Liberty Admin-Konsole bereit oder indem Sie sie in das `dropins`-Verzeichnis legen.

3. **Zugreifen auf die JSP**
   - Starten Sie Ihren Liberty-Server (`server start yourServer`).
   - Öffnen Sie einen Browser und navigieren Sie zu:
     `http://localhost:9080/myApp/decode.jsp?encoded={aes}Ihr_verschlüsseltes_Passwort`
     Ersetzen Sie `{aes}Ihr_verschlüsseltes_Passwort` durch das tatsächliche verschlüsselte Passwort aus `server.xml`.

4. **Abrufen des dekodierten Passworts**
   Die Seite zeigt das dekodierte Passwort an, das Sie dann verwenden können (z. B. in Squirrel SQL, um eine Verbindung zu einer Datenbank herzustellen).

5. **Sichern der Anwendung**
   Entfernen oder beschränken Sie nach dem Erhalten des Passworts den Zugriff auf die JSP, um eine unbefugte Nutzung zu verhindern.

#### Warum dies funktioniert:
Durch das Ausführen innerhalb des Liberty-Servers wird sichergestellt, dass `PasswordUtil.decode()` denselben Verschlüsselungsschlüssel (Standard oder benutzerdefiniert, wie über `wlp.password.encryption.key` in `server.xml` angegeben) verwendet, der zum Kodieren des Passworts verwendet wurde.

---

### Option 2: Verwenden eines eigenständigen Java-Programms
Wenn das Bereitstellen einer Webanwendung nicht möglich ist, können Sie ein eigenständiges Java-Programm schreiben und es mit den Liberty-Runtime-Bibliotheken im Klassenspeicher ausführen. Dieser Ansatz ist kniffliger, da er eine manuelle Handhabung des Verschlüsselungsschlüssels erfordert, insbesondere wenn ein benutzerdefinierter Schlüssel verwendet wurde.

#### Beispielcode:
```java
import com.ibm.websphere.crypto.PasswordUtil;

public class PasswordDecoder {
    public static void main(String[] args) {
        if (args.length < 1 || args.length > 2) {
            System.out.println("Verwendung: java PasswordDecoder <verschlüsseltes_Passwort> [crypto_key]");
            return;
        }
        String encoded = args[0];
        String cryptoKey = args.length == 2 ? args[1] : null;
        try {
            String decoded;
            if (cryptoKey != null) {
                decoded = PasswordUtil.decode(encoded, cryptoKey);
            } else {
                decoded = PasswordUtil.decode(encoded);
            }
            System.out.println("Dekodiertes Passwort: " + decoded);
        } catch (Exception e) {
            System.err.println("Fehler beim Dekodieren des Passworts: " + e.getMessage());
        }
    }
}
```

#### Schritte:
1. **Kompilieren Sie das Programm**
   - Speichern Sie den Code als `PasswordDecoder.java`.
   - Kompilieren Sie es mit den Liberty-JARs:
     ```bash
     javac -cp /pfad/zu/wlp/lib/* PasswordDecoder.java
     ```
     Ersetzen Sie `/pfad/zu/wlp` durch Ihr Liberty-Installationsverzeichnis (z. B. `/opt/ibm/wlp`).

2. **Führen Sie das Programm aus**
   - Wenn das Passwort mit dem Standardschlüssel verschlüsselt wurde:
     ```bash
     java -cp /pfad/zu/wlp/lib/*:. PasswordDecoder "{aes}Ihr_verschlüsseltes_Passwort"
     ```
   - Wenn ein benutzerdefinierter Schlüssel verwendet wurde (z. B. in `server.xml` als `<variable name="wlp.password.encryption.key" value="IhrKey"/>` definiert):
     ```bash
     java -cp /pfad/zu/wlp/lib/*:. PasswordDecoder "{aes}Ihr_verschlüsseltes_Passwort" "IhrKey"
     ```

3. **Verarbeiten Sie die Ausgabe**
   Das Programm gibt das dekodierte Passwort oder einen Fehler aus, wenn der Schlüssel falsch ist.

#### Hinweise:
- Die Liberty-JARs (z. B. in `wlp/lib`) enthalten `com.ibm.websphere.crypto.PasswordUtil` und dessen Abhängigkeiten.
- Wenn ein benutzerdefinierter Schlüssel verwendet wurde und Sie ihn nicht angeben, schlägt die Dekodierung fehl. Überprüfen Sie `server.xml` oder enthaltene Konfigurationsdateien auf den Schlüssel.

---

### Wichtige Überlegungen
- **Standard- vs. benutzerdefinierter Schlüssel**:
  - Wenn kein `wlp.password.encryption.key` in `server.xml` angegeben ist, wird der Standardschlüssel verwendet, und `PasswordUtil.decode(encoded)` sollte ohne zusätzliche Parameter funktionieren.
  - Wenn ein benutzerdefinierter Schlüssel definiert ist, müssen Sie ihn explizit angeben, wenn Sie außerhalb des Servers dekodieren (Option 2) oder auf die Serverumgebung (Option 1) zurückgreifen.

- **Sicherheit**:
  Handhaben Sie das dekodierte Passwort sorgfältig, da es im Klartext vorliegt. Vermeiden Sie das Protokollieren oder unnötige Freigeben.

- **Bevorzugung**:
  Option 1 (Webanwendung) ist in der Regel zuverlässiger, da sie innerhalb der Liberty-Umgebung ausgeführt wird und automatisch den Schlüssel und die Abhängigkeiten handelt.

Durch die Befolgung einer der beiden Ansätze können Sie das AES-verschlüsselte Passwort aus `server.xml` erfolgreich dekodieren, trotz des Fehlens einer Dekodierungsoption in `securityUtility`.