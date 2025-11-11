---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque JWT Java
translated: true
type: note
---

Pour utiliser la bibliothèque `com.nimbusds.jwt` en Java afin d'extraire des informations telles que la date d'expiration, la date d'émission et d'autres claims d'un JSON Web Token (JWT), suivez les étapes décrites ci-dessous. Cette solution suppose que vous travaillez avec un JWT signé, qui est le type le plus courant, et se concentre sur une approche claire et pratique pour atteindre votre objectif.

---

## Prérequis

Assurez-vous d'abord d'avoir ajouté la bibliothèque Nimbus JOSE + JWT à votre projet. Si vous utilisez Maven, incluez la dépendance suivante dans votre fichier `pom.xml` :

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- Remplacez par la dernière version -->
</dependency>
```

Vous pouvez vérifier la dernière version sur [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt).

---

## Étapes pour extraire la date d'expiration, la date d'émission et d'autres claims

Voici comment parser un JWT et récupérer la date d'expiration, la date d'émission et des claims supplémentaires en utilisant la bibliothèque `com.nimbusds.jwt` :

1. **Parser la chaîne JWT** : Utilisez la méthode `SignedJWT.parse()` pour convertir la chaîne JWT en un objet `SignedJWT`.
2. **Obtenir le jeu de claims** : Accédez aux claims (paires clé-valeur) du JWT en utilisant `getJWTClaimsSet()`.
3. **Extraire des claims spécifiques** :
   - Utilisez `getExpirationTime()` pour la date d'expiration (claim `exp`).
   - Utilisez `getIssueTime()` pour la date d'émission (claim `iat`).
   - Utilisez `getSubject()`, `getClaim()` ou d'autres méthodes pour des claims supplémentaires.
4. **Gérer les erreurs** : Encapsulez la logique de parsing dans un bloc try-catch pour gérer les problèmes de parsing potentiels.

---

## Exemple de code

Voici un exemple Java complet démontrant comment extraire la date d'expiration, la date d'émission et un claim supplémentaire (par exemple, le sujet) d'un JWT :

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // Remplacez ceci par votre vraie chaîne JWT
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // Étape 1 : Parser la chaîne JWT
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // Étape 2 : Obtenir le jeu de claims
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // Étape 3 : Extraire les dates d'expiration et d'émission
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // Exemple d'un autre claim

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
- `SignedJWT` : Représente un JWT signé et fournit des méthodes pour le parser et le traiter.
- `JWTClaimsSet` : Contient les claims du payload du JWT.
- `ParseException` : Lancée si la chaîne JWT est malformée ou ne peut pas être parsée.
- `Date` : Utilisée pour représenter les heures d'expiration et d'émission.

### 2. **Parsing du JWT**
- La méthode `SignedJWT.parse(jwtString)` prend une chaîne JWT (par exemple, `header.payload.signature`) et retourne un objet `SignedJWT`. Si le JWT est invalide, elle lance une `ParseException`.

### 3. **Accès aux claims**
- `signedJWT.getJWTClaimsSet()` récupère le jeu de claims, qui contient tous les claims du payload du JWT.

### 4. **Extraction de claims spécifiques**
- **`getExpirationTime()`** : Retourne le claim `exp` sous forme d'objet `Date` (ou `null` s'il n'est pas présent). Cela représente la date d'expiration du token.
- **`getIssueTime()`** : Retourne le claim `iat` sous forme d'objet `Date` (ou `null` s'il n'est pas présent). Cela indique la date d'émission du token.
- **`getSubject()`** : Retourne le claim `sub` sous forme de `String` (ou `null` s'il n'est pas présent), un exemple d'un autre claim standard. Vous pouvez également utiliser `getClaim("key")` pour récupérer des claims personnalisés sous forme d'`Object`.

### 5. **Gestion des erreurs**
- Le bloc try-catch garantit que si le JWT est malformé ou invalide, le programme gère l'erreur de manière élégante en affichant un message d'erreur.

---

## Notes

- **JWTs signés vs non signés** : Cet exemple utilise `SignedJWT` pour les tokens signés. Si vous avez un JWT non signé, utilisez plutôt `PlainJWT.parse(jwtString)`. Pour une approche plus générique, vous pouvez utiliser `JWTParser.parse(jwtString)` puis vérifier le type (`SignedJWT`, `PlainJWT`, etc.) en utilisant instanceof.
- **Vérification de la signature** : Ce code ne vérifie pas la signature du JWT. Dans un environnement de production, vous devriez vérifier la signature en utilisant `signedJWT.verify(verifier)` avec une clé appropriée pour garantir l'authenticité du token.
- **Vérifications de null** : Vérifiez toujours la présence de `null` lors de la récupération des claims, car ils sont optionnels et peuvent être absents dans certains JWT.
- **Claims personnalisés** : Pour accéder à des claims non standard, utilisez `claimsSet.getClaim("claimName")`, qui retourne un `Object` que vous pouvez caster vers le type approprié (par exemple, `String`, `Integer`).

---

## Exemple de sortie

Pour la chaîne JWT d'exemple ci-dessus :
```
Date d'expiration : Wed Jan 17 19:52:02 UTC 2018
Date d'émission : Wed Jan 17 19:50:22 UTC 2018
Sujet : 1234567890
```

---

Cette approche fournit un moyen simple et efficace d'extraire la date d'expiration, la date d'émission et d'autres claims d'un JWT en utilisant la bibliothèque `com.nimbusds.jwt`. Remplacez la `jwtString` par votre propre token et adaptez le code à vos besoins spécifiques !