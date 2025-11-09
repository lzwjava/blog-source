---
audio: false
generated: true
image: false
lang: de
layout: post
title: Alternativen zu Java Code Coverage Tools
translated: true
type: note
---

Neben **JaCoCo** gibt es mehrere andere Code-Coverage-Tools und Plugins, die Sie im Java-Ökosystem in Betracht ziehen können, abhängig von Ihrem Build-System und Ihren Integrationsanforderungen:

### 1. **Cobertura**

* Eines der älteren Java-Code-Coverage-Frameworks.
* Funktioniert durch Instrumentierung von Bytecode.
* Integriert sich mit Maven, Ant und Gradle.
* Wird nicht so aktiv gepflegt wie JaCoCo, wird aber noch in einigen Legacy-Systemen verwendet.

### 2. **Clover (von Atlassian)**

* Kommerzielles Tool (ältere Versionen sind jedoch quelloffen).
* Bietet detaillierte Coverage-Berichte, einschließlich Branch-Coverage, Testoptimierung (Nur-Ausführen relevanter Tests) und historischer Daten.
* Funktioniert gut mit großen Enterprise-Projekten.

### 3. **OpenClover** (Community-Fork von Clover)

* Quelloffene Fortführung von Clover, nachdem Atlassian die aktive Entwicklung eingestellt hat.
* Ähnlicher Funktionsumfang wie Clover, einschließlich Coverage pro Test und erweiterter Berichterstattung.

### 4. **Pitest (Mutation Testing mit Coverage)**

* In erster Linie ein **Mutation-Testing**-Tool, generiert aber auch Coverage-Berichte als Teil der Mutationsanalyse.
* Bietet stärkere Garantien für Testqualität als einfache Line-/Branch-Coverage.
* Einfache Integration mit Maven/Gradle.

### 5. **EMMA**

* Ein leichtgewichtiges Coverage-Tool für Java.
* Wird heute größtenteils als Legacy betrachtet, war aber weit verbreitet, bevor JaCoCo an Popularität gewann.
* Einige Projekte verwenden es noch aus Kompatibilitätsgründen.

### 6. **TestNG / JUnit + Build-Tool-Integrationen**

* Obwohl keine eigenständigen Coverage-Tools, verwenden viele moderne Build-Setups **Maven Surefire**, **Failsafe** oder **Gradle Test-Plugins** zusammen mit JaCoCo, Cobertura oder Pitest, um Coverage direkt in Test-Pipelines zu integrieren.

---

👉 In der Praxis verwenden die meisten modernen Teams **JaCoCo** (am besten gepflegt, weit verbreitete Unterstützung), aber wenn Sie Alternativen suchen, sind **OpenClover** und **Pitest** eine ernsthafte Überlegung wert, insbesondere wenn Sie Einblicke in die Testeffektivität *jenseits von Coverage* wünschen.

Möchten Sie, dass ich auch erkläre, welche davon sich am besten mit **Jenkins / SonarQube Pipelines** (üblich in Enterprise-Java) integrieren lassen?