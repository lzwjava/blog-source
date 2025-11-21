---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: Profils Maven pour la configuration d'environnement WAS
translated: true
type: note
---

Pour IBM WebSphere Application Server (WAS traditionnel, pas Liberty), le packaging standard est un fichier **EAR** (même pour les applications web simples, car WAS préfère EAR aux WAR autonomes). La meilleure pratique pour gérer différents environnements — comme le développement local (utilisateur de connexion fixe/codé en dur pour les tests) par rapport au serveur/production (SSO ou domaine de sécurité approprié) — est d'utiliser **les profils de build Maven** dans un seul `pom.xml`. Cela évite de maintenir plusieurs fichiers POM distincts (par exemple, `pom.xml` et `build_pom.xml`), ce qui est sujet aux erreurs et n'est pas idiomatique pour Maven.

### Pourquoi des profils au lieu de multiples POMs ?
- Une seule source de vérité (POM unique).
- Activation facile : `mvn package -Plocal` ou `mvn package -Pserver`.
- Les profils peuvent filtrer les ressources, écraser des fichiers, modifier la configuration des plugins ou ajuster les liaisons (par exemple, `ibm-web-bnd.xml`, `ibm-application-ext.xml` pour l'authentification spécifique à WAS).
- Couramment utilisés pour les différences dev/test/prod, y compris les configurations d'authentification.

### Structure recommandée
Utilisez le Maven Resources Plugin avec le filtrage + des répertoires de ressources spécifiques au profil pour échanger les fichiers de configuration (par exemple, `web.xml`, fichiers `properties`, configuration de sécurité Spring, ou les liaisons WAS).

Exemple de structure de répertoire :
```
src/
├── main/
│   ├── resources/          (configurations communes)
│   ├── webapp/
│   │   ├── WEB-INF/
│   │   │   ├── web.xml      (version commune ou de base)
│   │   │   └── ibm-web-bnd.xml (optionnel, pour les liaisons JNDI/auth)
│   └── ...
├── local/                   (ressources spécifiques au profil, copiées/filtrées uniquement pour local)
│   └── webapp/
│       └── WEB-INF/
│           ├── web.xml      (version locale avec form-login + utilisateur/rôle codé en dur ou sans sécurité)
│           └── ...
└── server/                  (spécifique au profil pour la production/SSO)
    └── webapp/
        └── WEB-INF/
            ├── web.xml      (version serveur avec <login-config><auth-method>CLIENT-CERT</auth-method> ou SPNEGO pour SSO)
            └── ...
```

### Exemple d'extrait de pom.xml
```xml
<project ...>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-was-app</artifactId>
    <version>1.0.0</version>
    <packaging>ear</packaging>   <!-- Ou war si vous déployez en WAR, mais EAR est préféré pour WAS -->

    <properties>
        <maven.compiler.source>11</maven.compiler.source> <!-- ou votre version Java -->
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Vos dépendances d'application -->
        <!-- Pour les APIs WAS à la compilation (scope provided) -->
        <dependency>
            <groupId>com.ibm.tools.target</groupId>
            <artifactId>was</artifactId>
            <version>9.0</version> <!-- Correspond à votre version WAS, par ex. 8.5.5 ou 9.0 -->
            <type>pom</type>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Construire l'EAR (ajuster pour WAR si nécessaire) -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- Votre configuration EAR, modules, etc. -->
                </configuration>
            </plugin>

            <!-- Filtrage des ressources et remplacements spécifiques au profil -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <useDefaultDelimiters>true</useDefaultDelimiters>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Profils -->
    <profiles>
        <!-- Profil local/dev : utilisateur fixe, form login ou pas de sécurité -->
        <profile>
            <id>local</id>
            <activation>
                <activeByDefault>true</activeByDefault> <!-- Par défaut pour les builds locaux -->
            </activation>
            <build>
                <resources>
                    <!-- Ressources communes -->
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <!-- Remplacement par les fichiers spécifiques à l'environnement local -->
                    <resource>
                        <directory>src/local/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- Exemple de propriétés filtrées pour l'utilisateur local codé en dur -->
                <app.login.user>devuser</app.login.user>
                <app.login.password>devpass</app.login.password>
            </properties>
        </profile>

        <!-- Profil serveur/prod : vrai SSO (par ex. SPNEGO, LTPA, ou OpenIDConnect) -->
        <profile>
            <id>server</id>
            <build>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <resource>
                        <directory>src/server/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- Propriétés de production, par ex. activer les drapeaux SSO -->
                <app.auth.method>SSO</app.auth.method>
            </properties>
        </profile>
    </profiles>
</project>
```

### Points clés pour les différences d'authentification
- **Local** : Utilisez FORM login avec des utilisateurs/rôles simples dans `web.xml` ou un fichier properties, ou désactivez entièrement la sécurité (`<security-constraint>` supprimé).
- **Serveur** : Configurez le SSO spécifique à WAS dans `web.xml` (par exemple, `<auth-method>FORM</auth-method>` avec SPNEGO, ou utilisez la fonctionnalité OpenID Connect de type Liberty, mais pour WAS traditionnel, souvent LTPA + domaine de sécurité global). Les liaisons WAS (`ibm-web-bnd.xml`) peuvent également être remplacées par profil pour les mappages utilisateur/rôle.
- Si vous utilisez Spring Security ou similaire, échangez `applicationContext-security.xml` ou les properties de la même manière.
- Pour l'utilisateur local codé en dur : Évitez les véritables identifiants codés en dur ; utilisez un utilisateur de test mappé dans un `users.properties` local ou désactivez les vérifications d'authentification via un drapeau.

### Commandes de build
- Local (par défaut) : `mvn clean package`
- Serveur/Prod : `mvn clean package -Pserver`

Cela produit différents EAR adaptés à chaque environnement à partir de la **même base de code**. Si vous avez vraiment besoin de noms d'artefacts distincts (par exemple, `myapp-local.ear` vs `myapp.ear`), ajoutez `<finalName>${project.artifactId}-${profile}</finalName>` dans les sections `<build>` spécifiques au profil.

[Guide des profils Maven](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)  
[Plugin Maven EAR](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Intégration Maven IBM WAS](https://www.ibm.com/docs/en/wasdtfe/9.7.0?topic=suye-configuring-dependency-pom-files-that-emulate-classpath-specific-websphere-runtime-environments)