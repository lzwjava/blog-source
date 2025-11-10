---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía BDD con Cucumber para Desarrolladores Java
translated: true
type: note
---

Aquí tienes una introducción práctica y completa a **Cucumber**: qué es, por qué los equipos lo usan y cómo volverse productivo con él en Java (además de notas rápidas para usuarios de JS/Python).

---

# Qué es Cucumber (y qué no es)

* **Cucumber** es un framework de pruebas de **BDD (Desarrollo Guiado por el Comportamiento)**. Te permite describir el comportamiento en lenguaje natural (Gherkin) y vincular esas frases a código ejecutable (definiciones de pasos).
* Es ideal cuando quieres un **entendimiento compartido** entre producto, QA e ingeniería, y **documentación viva** que también sirva como pruebas.
* **No** es un reemplazo para frameworks de pruebas unitarias (JUnit/TestNG/Jest/PyTest). Los complementa al enfocarse en **pruebas de aceptación a nivel de negocio**.

---

# Componentes principales

**1) Gherkin (especificaciones en texto plano)**

* Escrito en archivos `.feature`.
* Palabras clave: `Feature`, `Scenario`, `Given/When/Then/And/But`, `Background`, `Scenario Outline` + `Examples`, `@tags`, (y opcionalmente `Rule` en Gherkin más reciente).
* Estilo de lenguaje natural; admite muchos idiomas.

**2) Definiciones de Pasos (código)**

* Vinculan los