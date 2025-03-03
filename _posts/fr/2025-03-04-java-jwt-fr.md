---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque Java JWT
translated: true
---

Pour utiliser la bibliothèque `com.nimbusds.jwt` en Java afin d'extraire des informations telles que la date d'expiration, la date d'émission et d'autres revendications à partir d'un JSON Web Token (JWT), suivez les étapes décrites ci-dessous. Cette solution suppose que vous travaillez avec un JWT signé, qui est le type le plus courant, et se concentre sur la fourniture d'une approche claire et pratique pour atteindre votre objectif.

---

## Prérequis

Assurez-vous d'avoir la bibliothèque Nimbus JOSE + JWT ajoutée à votre projet. Si vous utilisez Maven, incluez la dépendance suivante dans votre `pom.xml` :

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- Remplacez par la dernière version -->
</dependency>
```

Vous pouvez vérifier la dernière version sur [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt).

---

## Étapes pour extraire la date d'expiration, la date d'émission et d'autres revendications

Voici comment vous pouvez analyser un JWT et récupérer la date d'expiration, la date d'émission et les revendications supplémentaires en utilisant la bibliothèque `com.nimbusds.jwt` :

1. **Analyser la chaîne JWT** : Utilisez la méthode `SignedJWT.parse()` pour convertir la chaîne JWT en un objet `SignedJWT`.
2. **Obtenir l'ensemble des revendications** : Accédez aux revendications (paires clé-valeur) du JWT en utilisant `getJWTClaimsSet()`.
3. **Extraire des revendications spécifiques** :
   - Utilisez `getExpirationTime()` pour la date d'expiration (`exp` revendication).
   - Utilisez `getIssueTime()` pour la date d'émission (`iat` revendication).
   - Utilisez `getSubject()`, `getClaim()`, ou d'autres méthodes pour des revendications supplémentaires.
4. **Gérer les erreurs** : Enveloppez la logique d'analyse dans un bloc try-catch pour gérer les problèmes d'analyse potentiels.

---

## Exemple de code

Voici un exemple complet en Java démontrant comment extraire la date d'expiration, la date d'émission et une revendication supplémentaire (par exemple, le sujet) à partir d'un JWT :

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // Remplacez ceci par votre chaîne JWT réelle
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // Étape 1 : Analyser la chaîne JWT
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // Étape 2 : Obtenir l'ensemble des revendications
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // Étape 3 : Extraire les dates d'expiration et d'émission
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // Exemple d'une autre revendication

            // Étape 4 : Afficher les résultats
            if (expirationDate != null) {
                System.out.println("Date d'expiration : " + expirationDate);
            } else {
                System.out.println("Aucune date d'expiration définie.");
            }

            if (issuedDate != null) {
                System.out.println("Date d'émission : " + issuedDate);
            } else {
                System.out.println("Aucune date d'émission définie.");
            }

            if (subject != null) {
                System.out.println("Sujet : " + subject);
            } else {
                System.out.println("Aucun sujet défini.");
            }

        } catch (ParseException e) {
            System.out.println("JWT invalide : " + e.getMessage());
        }
    }
}
```

---

## Explication du code

### 1. **Imports**
- `SignedJWT` : Représente un JWT signé et fournit des méthodes pour l'analyser et le traiter.
- `JWTClaimsSet` : Contient les revendications du payload du JWT.
- `ParseException` : Lancée si la chaîne JWT est mal formée ou ne peut pas être analysée.
- `Date` : Utilisée pour représenter les temps d'expiration et d'émission.

### 2. **Analyser le JWT**
- La méthode `SignedJWT.parse(jwtString)` prend une chaîne JWT (par exemple, `header.payload.signature`) et retourne un objet `SignedJWT`. Si le JWT est invalide, elle lance une `ParseException`.

### 3. **Accéder aux revendications**
- `signedJWT.getJWTClaimsSet()` récupère l'ensemble des revendications, qui contient toutes les revendications du payload du JWT.

### 4. **Extraire des revendications spécifiques**
- **`getExpirationTime()`** : Retourne la revendication `exp` en tant qu'objet `Date` (ou `null` si elle n'est pas présente). Cela représente quand le jeton expire.
- **`getIssueTime()`** : Retourne la revendication `iat` en tant qu'objet `Date` (ou `null` si elle n'est pas présente). Cela indique quand le jeton a été émis.
- **`getSubject()`** : Retourne la revendication `sub` en tant que `String` (ou `null` si elle n'est pas présente), un exemple d'une autre revendication standard. Vous pouvez également utiliser `getClaim("key")` pour récupérer des revendications personnalisées en tant qu'objet `Object`.

### 5. **Gestion des erreurs**
- Le bloc try-catch assure que si le JWT est mal formé ou invalide, le programme gère l'erreur de manière élégante en imprimant un message d'erreur.

---

## Notes

- **JWT signés vs non signés** : Cet exemple utilise `SignedJWT` pour les jetons signés. Si vous avez un JWT non signé, utilisez `PlainJWT.parse(jwtString)` à la place. Pour une approche plus générique, vous pouvez utiliser `JWTParser.parse(jwtString)` puis vérifier le type (`SignedJWT`, `PlainJWT`, etc.) en utilisant `instanceof`.
- **Vérification de la signature** : Ce code ne vérifie pas la signature du JWT. Dans un environnement de production, vous devriez vérifier la signature en utilisant `signedJWT.verify(verifier)` avec une clé appropriée pour garantir l'authenticité du jeton.
- **Vérifications de nullité** : Vérifiez toujours la nullité lors de la récupération des revendications, car elles sont optionnelles et peuvent ne pas être présentes dans chaque JWT.
- **Revendications personnalisées** : Pour accéder aux revendications non standard, utilisez `claimsSet.getClaim("claimName")`, qui retourne un `Object` que vous pouvez caster au type approprié (par exemple, `String`, `Integer`).

---

## Exemple de sortie

Pour la chaîne JWT d'exemple ci-dessus :
```
Date d'expiration : mer. janv. 17 19:52:02 UTC 2018
Date d'émission : mer. janv. 17 19:50:22 UTC 2018
Sujet : 1234567890
```

---

Cette approche fournit une méthode simple et efficace pour extraire la date d'expiration, la date d'émission et d'autres revendications d'un JWT en utilisant la bibliothèque `com.nimbusds.jwt`. Remplacez la `jwtString` par votre propre jeton et adaptez le code à vos besoins spécifiques !