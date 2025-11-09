---
audio: false
date: 2025-09-10
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Ignorer la construction Angular dans Maven
translated: true
type: note
---

Réponse courte : oui — vous pouvez sauter la build Angular/npm, mais pas avec un flag intégré comme `--skip-web`. Utilisez l'une de ces approches.

### 1) Exclure le module web dans une build multi-module

Si votre application Angular est son propre module Maven (par exemple, `web`), excluez-le simplement dans le réacteur :

```
mvn -pl '!web' -am clean package
```

Ou construisez uniquement le module backend :

```
mvn -pl :backend -am clean package
```

(`-am` construit les dépendances nécessaires ; la syntaxe `!web` exclut ce module.)

### 2) Ajouter une propriété "skip frontend" (fonctionne avec frontend-maven-plugin ou exec)

Protégez les goals npm avec une propriété et activez-la depuis la ligne de commande.

**POM (module web ou parent) :**

```xml
<properties>
  <skip.frontend>false</skip.frontend>
</properties>

<build>
  <plugins>
    <!-- Exemple : com.github.eirslett:frontend-maven-plugin -->
    <plugin>
      <groupId>com.github.eirslett</groupId>
      <artifactId>frontend-maven-plugin</artifactId>
      <version>...votre version...</version>
      <configuration>
        <skip>${skip.frontend}</skip>
      </configuration>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals>
            <goal>npm</goal>
          </goals>
          <configuration>
            <arguments>run build</arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>

    <!-- Si vous utilisez exec-maven-plugin pour appeler npm -->
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>...votre version...</version>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals><goal>exec</goal></goals>
          <configuration>
            <skip>${skip.frontend}</skip>
            <executable>npm</executable>
            <arguments>
              <argument>run</argument>
              <argument>build</argument>
            </arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

**CLI :**

```
mvn -Dskip.frontend=true clean package
```

### 3) Utiliser des profils Maven

Lieez la build frontend uniquement dans un profil "with-frontend" et faites d'un profil "skip-frontend" le profil par défaut en dev.

**POM :**

```xml
<profiles>
  <profile>
    <id>with-frontend</id>
    <activation>
      <property>
        <name>!skip.frontend</name>
      </property>
    </activation>
    <build>
      <plugins>
        <!-- même configuration de plugin que ci-dessus, sans skip -->
      </plugins>
    </build>
  </profile>
</profiles>
```

**CLI :**

* Normal (skip) : `mvn -Dskip.frontend clean package`
* Release (construire l'UI) : `mvn -Pwith-frontend clean package`

---

## Conseils de vitesse si vous *construisez* l'UI

* Assurez-vous que le cache persistant d'Angular est activé (Angular CLI cache par défaut ; conservez `node_modules` et `.angular/cache` en cache dans l'IC).
* Exécutez `ng build` uniquement pour la release ; en dev, servez l'UI séparément (`npm start`) et faites servir à Spring les assets statiques pré-construits (par exemple, placez `dist/` sous `src/main/resources/static` pour les builds empaquetées).
* Envisagez de scinder le repo pour que l'app Angular ne soit pas du tout un module Maven ; construisez-la uniquement lorsque les fichiers frontend changent.
* Si vous êtes sur une version récente d'Angular, utilisez le builder esbuild/Vite par défaut et gardez les source maps désactivées dans les builds de release en IC.

---

### Conclusion

Utilisez `-pl '!web'` pour exclure le module web, **ou** ajoutez une propriété `skip.frontend` et configurez vos exécutions de plugin pour la respecter. Il n'existe pas de `mvn package --skip-web` standard, mais les deux modèles ci-dessus sont fiables et courants.