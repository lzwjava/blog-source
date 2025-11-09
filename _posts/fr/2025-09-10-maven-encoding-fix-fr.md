---
audio: false
date: 2025-09-10
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Correction des avertissements d'encodage de la plateforme Maven
translated: true
type: note
---

Cet avertissement Maven signifie que votre processus de build de projet dépend de **l'encodage de plateforme par défaut** (par exemple, GBK sur un système Windows chinois). Si d'autres développeurs ou serveurs d'intégration continue utilisent un encodage différent (comme UTF-8 sous Linux), les ressources textuelles (sources Java, propriétés, XML, etc.) peuvent être mal lues ou mal compilées.

Voici comment résoudre le problème :

---

### 1. Définir l'encodage source dans `pom.xml`

Dans la section `<properties>` de votre projet, déclarez explicitement l'encodage :

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <maven.compiler.encoding>UTF-8</maven.compiler.encoding>
</properties>
```

Cela garantit que Maven compile les sources et génère les rapports de manière cohérente en UTF-8, indépendamment de la valeur par défaut de votre système d'exploitation.

---

### 2. Configurer le plugin Compiler (si ce n'est pas déjà fait)

Certaines configurations Maven plus anciennes nécessitent de spécifier l'encodage dans le plugin compiler :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---

### 3. Vérifier les encodages de fichiers

* Assurez-vous que vos fichiers `.java`, `.properties`, `.yml`, etc. sont enregistrés en UTF-8, et non en GBK.
* Dans IntelliJ IDEA ou VS Code, définissez **File Encoding = UTF-8** dans les paramètres du projet.
* Pour Git, vous pouvez imposer un encodage cohérent avec `.gitattributes` si nécessaire.

---

### 4. Exécuter Maven avec un encodage explicite (Optionnel)

Vous pouvez également forcer l'encodage lors de l'exécution de Maven :

```bash
mvn clean install -Dfile.encoding=UTF-8
```

Mais la meilleure pratique est de corriger cela dans le `pom.xml`, afin que ce soit cohérent pour tout le monde.

---

✅ Après ces modifications, l'avertissement "platform dependent encoding GBK" devrait disparaître, et votre projet Spring + Maven sera sécurisé au niveau de l'encodage sur toutes les machines.

Souhaitez-vous que je vous montre également comment **convertir les fichiers sources existants de GBK vers UTF-8** de manière sécurisée (pour que votre dépôt soit propre et cohérent) ?