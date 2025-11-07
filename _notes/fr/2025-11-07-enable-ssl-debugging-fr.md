---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Débogage SSL TLS de Java
translated: true
---

### Activation du débogage SSL/TLS en Java

Pour activer la journalisation détaillée des activités liées à SSL/TLS en Java (par exemple, les négociations, la validation des certificats, les échanges de clés), vous utilisez la propriété système JVM `-Djavax.net.debug`. Cela envoie les informations de débogage vers la console (stdout/stderr) lors de l'exécution de votre application Java.

#### Instructions étape par étape

1. **Choisir le niveau de débogage** :
   - Utilisez `ssl` pour les détails de base de la négociation SSL/TLS.
   - Utilisez `ssl:handshake` pour des messages de négociation verbeux (incluant les suites de chiffrement et les certificats).
   - Utilisez `all` pour un débogage complet (inclut SSL ainsi que d'autres protocoles réseau — à utiliser avec parcimonie car c'est très verbeux).
   - Recommandation courante : Commencez par `ssl:handshake:verbose,keymanager:trustmanager` pour des informations SSL ciblées.

2. **Définir la propriété lors de l'exécution de votre application Java** :
   - **Exécution en ligne de commande** (par exemple, via la commande `java`) :
     ```
     java -Djavax.net.debug=ssl:handshake -jar votre-app.jar
     ```
     Remplacez `votre-app.jar` par votre application ou classe réelle (par exemple, `com.example.Main`).

   - **Dans un IDE (par exemple, IntelliJ IDEA, Eclipse)** :
     - Allez dans les Configurations d'exécution/de débogage.
     - Ajoutez `-Djavax.net.debug=ssl:handshake` dans le champ **Options de la VM**.
     - Exécutez ou déboguez la configuration.

   - **Dans un outil de build (par exemple, Maven ou Gradle)** :
     - **Maven** (dans `pom.xml` sous `<build><plugins><plugin>` pour surefire) :
       ```xml
       <configuration>
         <argLine>-Djavax.net.debug=ssl:handshake</argLine>
       </configuration>
       ```
     - **Gradle** (dans `build.gradle`) :
       ```groovy
       test {
         jvmArgs '-Djavax.net.debug=ssl:handshake'
       }
       ```

3. **Capturer les journaux** :
   - La sortie apparaît dans votre console/terminal.
   - Redirigez-la vers un fichier pour un examen plus facile :
     ```
     java -Djavax.net.debug=ssl:handshake -jar votre-app.jar > ssl-debug.log 2>&1
     ```
   - Recherchez les lignes commençant par `***` (par exemple, `*** ClientHello` pour le début des négociations) ou les préfixes `javax.net.ssl`.

4. **Le désactiver** :
   - Supprimez simplement l'option `-D` une fois terminé — elle n'est pas définie par défaut pour éviter une surcharge des performances.

#### Exemple d'extrait de sortie
Lorsqu'il est activé, vous verrez quelque chose comme :
```
*** ServerHello, TLSv1.2
RandomCookie:  GMT: 1731000000 bytes = { ... }
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
Compression Method: 0
***
```

#### Conseils
- Cela fonctionne pour Java 8+ (incluant 11, 17, 21). Dans les versions plus récentes, vous pouvez aussi activer `-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3` pour des journaux spécifiques au protocole.
- Une verbosité élevée peut ralentir votre application et inonder les journaux — testez dans un environnement de développement.
- Si vous utilisez un framework comme Spring Boot, ajoutez-le dans `application.properties` : `debug=true` (pour un débogage général) ou via les arguments de ligne de commande.

Pour plus de détails, consultez la documentation officielle d'Oracle : [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names).