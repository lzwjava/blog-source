---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Comprensión de los Ciclos de Vida de Maven y JaCoCo
translated: true
type: note
---

Buena pregunta — esto se reduce a las *fases del ciclo de vida* de Maven y cómo los plugins se vinculan a ellas.

### Conceptos básicos del ciclo de vida

Maven tiene tres ciclos de vida estándar: `clean`, `default` (a veces llamado *build*), y `site`.
Dentro del ciclo de vida *default*, las fases importantes siguen un orden como este:

* `validate`
* `compile`
* `test`
* `package`
* `verify`
* `install`
* `deploy`

Cada fase incluye todas las anteriores (si ejecutas `mvn verify`, Maven ejecuta todo desde `validate` hasta `verify`). Ejecutar `mvn package` se detendrá después de crear el artefacto (JAR/WAR), y no ejecutará `verify`.

### Por qué JaCoCo está involucrado

El plugin de Maven JaCoCo típicamente vincula su objetivo **`prepare-agent`** a la fase `initialize` o `verify` dependiendo de la configuración.

* Si está vinculado a `verify` (la configuración común para los informes de cobertura), entonces `mvn verify` lo activará.
* `mvn package` no llega tan lejos en el ciclo de vida, por lo que la fase `verify` (y por lo tanto el paso de JaCoCo) se omite.

Es por eso que ves que JaCoCo se ejecuta cuando ejecutas `mvn verify` pero no cuando ejecutas `mvn package`.

### Conclusión práctica

* Usa **`mvn package`** cuando solo quieras el artefacto de build (rápido, sin comprobaciones adicionales).
* Usa **`mvn verify`** cuando quieras ejecutar *pruebas de integración, comprobaciones, informes de cobertura o plugins de QA* que están vinculados a fases posteriores.

👉 Si quieres que JaCoCo se ejecute siempre, incluso con `mvn package`, puedes volver a vincular el objetivo `prepare-agent` a una fase anterior como `test` o `package` en tu `pom.xml`.

¿Te gustaría que te muestre un fragmento concreto de `pom.xml` que haga que el `prepare-agent` de JaCoCo se ejecute ya en `test` en lugar de en `verify`?