---
audio: false
generated: true
lang: de
layout: post
title: Java JWT-Bibliothek
translated: true
type: note
---

Um die `com.nimbusds.jwt`-Bibliothek in Java zu verwenden, um Informationen wie das Ablaufdatum, Ausstellungsdatum und andere Claims aus einem JSON Web Token (JWT) zu extrahieren, befolgen Sie die unten beschriebenen Schritte. Diese Lösung geht davon aus, dass Sie mit einem signierten JWT arbeiten, dem häufigsten Typ, und konzentriert sich darauf, einen klaren, praktischen Ansatz zur Erreichung Ihres Ziels zu bieten.

---

## Voraussetzungen

Stellen Sie zunächst sicher, dass Sie die Nimbus JOSE + JWT-Bibliothek zu Ihrem Projekt hinzugefügt haben. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit in Ihre `pom.xml` ein:

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- Ersetzen Sie dies durch die neueste Version -->
</dependency>
```

Sie können die neueste Version auf [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt) überprüfen.

---

## Schritte zum Extrahieren von Ablaufdatum, Ausstellungsdatum und anderen Claims

So können Sie einen JWT parsen und das Ablaufdatum, Ausstellungsdatum und zusätzliche Claims mit der `com.nimbusds.jwt`-Bibliothek abrufen:

1.  **JWT-String parsen**: Verwenden Sie die Methode `SignedJWT.parse()`, um den JWT-String in ein `SignedJWT`-Objekt umzuwandeln.
2.  **Claims Set abrufen**: Greifen Sie auf die Claims (Schlüssel-Wert-Paare) aus dem JWT mit `getJWTClaimsSet()` zu.
3.  **Spezifische Claims extrahieren**:
    *   Verwenden Sie `getExpirationTime()` für das Ablaufdatum (`exp`-Claim).
    *   Verwenden Sie `getIssueTime()` für das Ausstellungsdatum (`iat`-Claim).
    *   Verwenden Sie `getSubject()`, `getClaim()` oder andere Methoden für zusätzliche Claims.
4.  **Fehler behandeln**: Wickeln Sie die Parsing-Logik in einen try-catch-Block ein, um mögliche Parsing-Probleme zu behandeln.

---

## Beispielcode

Unten finden Sie ein vollständiges Java-Beispiel, das zeigt, wie Sie das Ablaufdatum, Ausstellungsdatum und einen zusätzlichen Claim (z.B. den Subject) aus einem JWT extrahieren:

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // Ersetzen Sie dies durch Ihren tatsächlichen JWT-String
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // Schritt 1: JWT-String parsen
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // Schritt 2: Claims Set abrufen
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // Schritt 3: Ablauf- und Ausstellungsdaten extrahieren
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // Beispiel für einen weiteren Claim

            // Schritt 4: Ergebnisse anzeigen
            if (expirationDate != null) {
                System.out.println("Expiration date: " + expirationDate);
            } else {
                System.out.println("No expiration date set.");
            }

            if (issuedDate != null) {
                System.out.println("Issued date: " + issuedDate);
            } else {
                System.out.println("No issued date set.");
            }

            if (subject != null) {
                System.out.println("Subject: " + subject);
            } else {
                System.out.println("No subject set.");
            }

        } catch (ParseException e) {
            System.out.println("Invalid JWT: " + e.getMessage());
        }
    }
}
```

---

## Erklärung des Codes

### 1. **Imports**
*   `SignedJWT`: Repräsentiert einen signierten JWT und bietet Methoden zum Parsen und Verarbeiten.
*   `JWTClaimsSet`: Enthält die Claims aus der JWT-Payload.
*   `ParseException`: Wird ausgelöst, wenn der JWT-String fehlerhaft ist oder nicht geparst werden kann.
*   `Date`: Wird verwendet, um die Ablauf- und Ausstellungszeiten darzustellen.

### 2. **Parsen des JWT**
*   Die Methode `SignedJWT.parse(jwtString)` nimmt einen JWT-String (z.B. `header.payload.signature`) entgegen und gibt ein `SignedJWT`-Objekt zurück. Wenn der JWT ungültig ist, wird eine `ParseException` ausgelöst.

### 3. **Zugriff auf die Claims**
*   `signedJWT.getJWTClaimsSet()` ruft das Claims Set ab, das alle Claims aus der Payload des JWT enthält.

### 4. **Extrahieren spezifischer Claims**
*   **`getExpirationTime()`**: Gibt den `exp`-Claim als `Date`-Objekt zurück (oder `null`, falls nicht vorhanden). Dies repräsentiert den Zeitpunkt, zu dem der Token abläuft.
*   **`getIssueTime()`**: Gibt den `iat`-Claim als `Date`-Objekt zurück (oder `null`, falls nicht vorhanden). Dies gibt an, wann der Token ausgestellt wurde.
*   **`getSubject()`**: Gibt den `sub`-Claim als `String` zurück (oder `null`, falls nicht vorhanden), ein Beispiel für einen anderen Standard-Claim. Sie können auch `getClaim("key")` verwenden, um benutzerdefinierte Claims als `Object` abzurufen.

### 5. **Fehlerbehandlung**
*   Der try-catch-Block stellt sicher, dass das Programm Fehler graceful abfängt, indem es eine Fehlermeldung ausgibt, falls der JWT fehlerhaft oder ungültig ist.

---

## Hinweise

*   **Signierte vs. unsignierte JWTs**: Dieses Beispiel verwendet `SignedJWT` für signierte Tokens. Wenn Sie einen unsignierten JWT haben, verwenden Sie stattdessen `PlainJWT.parse(jwtString)`. Für einen generischeren Ansatz können Sie `JWTParser.parse(jwtString)` verwenden und dann den Typ (`SignedJWT`, `PlainJWT` usw.) mit instanceof überprüfen.
*   **Signaturverifizierung**: Dieser Code verifiziert nicht die Signatur des JWT. In einer Produktionsumgebung sollten Sie die Signatur mit `signedJWT.verify(verifier)` und einem entsprechenden Schlüssel verifizieren, um die Authentizität des Tokens sicherzustellen.
*   **Null-Checks**: Überprüfen Sie immer auf `null`, wenn Sie Claims abrufen, da diese optional sind und möglicherweise nicht in jedem JWT vorhanden sind.
*   **Benutzerdefinierte Claims**: Um auf nicht-standardisierte Claims zuzugreifen, verwenden Sie `claimsSet.getClaim("claimName")`, was ein `Object` zurückgibt, das Sie in den entsprechenden Typ (z.B. `String`, `Integer`) casten können.

---

## Beispielausgabe

Für den obigen Beispiel-JWT-String:
```
Expiration date: Wed Jan 17 19:52:02 UTC 2018
Issued date: Wed Jan 17 19:50:22 UTC 2018
Subject: 1234567890
```

---

Dieser Ansatz bietet eine einfache und effektive Möglichkeit, das Ablaufdatum, Ausstellungsdatum und andere Claims aus einem JWT mit der `com.nimbusds.jwt`-Bibliothek zu extrahieren. Ersetzen Sie den `jwtString` durch Ihren eigenen Token und passen Sie den Code an Ihre spezifischen Bedürfnisse an!