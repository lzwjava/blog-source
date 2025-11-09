---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Résoudre les problèmes d'arrêt de Jetty fourchu
translated: true
type: note
---

Vous avez en fait fait la plupart des choses correctement — le blocage est presque toujours dû au fait que **le stop goal ne peut pas atteindre le Jetty forké** (mauvais stopHost/port/scope de la clé) ou parce que **`run-forked` maintient Maven attaché** de manière inattendue. Deux solutions robustes ci-dessous ; choisissez-en une.

### Option A — Modèle fiable : `jetty:start` (démon) + `jetty:stop`

Cela évite entièrement `run-forked` et est le plus stable pour les cycles de vie des tests d'intégration.

**Ce qu'il faut changer**

1. Épinglez la version du plugin et utilisez `start` avec `daemon=true` dans `pre-integration-test`.
2. Gardez vos tests d'intégration Python dans `integration-test`.
3. Utilisez `stop` dans `post-integration-test`.
4. Fournissez les *mêmes* `stopHost/stopPort/stopKey` dans **les deux** exécutions.

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <configuration>
    <httpConnector>
      <port>8080</port>
      <host>127.0.0.1</host>
    </httpConnector>
  </configuration>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>start</goal>
      </goals>
      <configuration>
        <daemon>true</daemon>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**Pourquoi cela corrige le problème de "blocage"**

* `daemon=true` fait que `start` rend le contrôle à Maven immédiatement, permettant ainsi à vos tests d'intégration de s'exécuter.
* Les `stopHost/stopPort/stopKey` correspondants garantissent que le goal `stop` atteint le même Jetty.
* Aucune dépendance au comportement du thread de surveillance de `run-forked`.

---

### Option B — Gardez `run-forked`, mais faites fonctionner le stop

Si vous préférez `run-forked`, les pièges courants sont :

* Les valeurs par défaut de `stopHost` peuvent différer de la façon dont le processus enfant se lie (IPv6 vs IPv4).
* `stopPort/stopKey` sont définis uniquement sur l'exécution de démarrage mais **ne sont pas** répliqués sur l'exécution d'arrêt.
* L'enfant n'expose pas de gestionnaire d'arrêt si la configuration est mal placée.

**Resserrez la configuration comme ceci :**

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>run-forked</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>

        <httpConnector>
          <host>127.0.0.1</host>
          <port>8080</port>
        </httpConnector>

        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**Garde-fous supplémentaires**

* Ajoutez `-Djava.net.preferIPv4Stack=true` aux `jvmArgs` de l'enfant si votre macOS/Java choisit IPv6 et que le goal stop utilise IPv4 :

  ```
  <jvmArgs>
    -Djava.net.preferIPv4Stack=true
    -javaagent:...
  </jvmArgs>
  ```
* Assurez-vous que rien d'autre n'utilise le port `8081`. Si c'est le cas, changez le port pour un autre port libre à la fois pour le démarrage et l'arrêt.
* Si vos tests d'intégration plantent ou se bloquent, `post-integration-test` risque de ne jamais s'exécuter ; dans ce cas, ajoutez une solution de repli pour tuer le processus dans la phase `verify` (voir ci-dessous).

---

### Filet de sécurité optionnel — tuez l'enfant si `stop` échoue

Ajoutez un petit utilitaire pour tuer forcément le Jetty forké via le PID écrit dans un fichier :

1. Dans la configuration de `run-forked`/`start` :

```
<pidFile>${project.build.directory}/jetty.pid</pidFile>
```

2. Après `post-integration-test`, ajoutez un `exec-maven-plugin` dans `verify` qui vérifie le fichier pid et tue le processus s'il est toujours en vie.

---

### Quelques remarques mineures tirées de votre log

* `No Spring WebApplicationInitializer types detected` est normal si vous utilisez `web.xml` + DispatcherServlet ; ce n'est pas lié au blocage à l'arrêt.
* Envisagez de déplacer les tests d'intégration vers **maven-failsafe-plugin** (se lie à `integration-test`/`verify`) et gardez les tests unitaires sur surefire. Votre approche actuelle avec `exec-maven-plugin` fonctionne, mais failsafe s'intègre mieux au cycle de vie des tests d'intégration.

---

Si vous le souhaitez, collez votre bloc de plugin Jetty **complet** + tout miroir `settings.xml` (pour le chemin du repository local) et je personnaliserai la différence minimale exacte pour votre dépôt.