---
audio: false
generated: true
lang: es
layout: post
title: 'GitHub Actions: La Evolución de CI/CD'
translated: true
type: note
---

GitHub Actions es una potente **plataforma de integración continua y entrega continua (CI/CD)** integrada directamente en GitHub. Permite a los desarrolladores automatizar varias etapas de su flujo de trabajo de desarrollo de software, desde la construcción y prueba del código hasta la implementación de aplicaciones.

### Cómo se desarrolló y cuándo se lanzó

GitHub mismo fue fundado en **2007**, y su sitio web se lanzó en **abril de 2008**. El desarrollo de la plataforma GitHub comenzó en **octubre de 2005**, y fue lanzada oficialmente por Tom Preston-Werner, Chris Wanstrath, P. J. Hyett y Scott Chacon.

GitHub Actions, como plataforma específica de CI/CD, se anunció por primera vez en **octubre de 2018** y se lanzó oficialmente para disponibilidad general en **noviembre de 2019**. Evolucionó a partir de la misión central de GitHub de proporcionar herramientas que simplifiquen la colaboración y la automatización para los desarrolladores.

### ¿Cuántos usuarios tiene?

Si bien es difícil obtener un número exacto y en tiempo real de *usuarios* de GitHub Actions específicamente, vale la pena señalar que **el propio GitHub tiene más de 100 millones de desarrolladores** a principios de 2023. Dada la profunda integración de GitHub Actions y la creciente demanda de CI/CD, una parte significativa de estos usuarios aprovecha GitHub Actions para sus proyectos. Muchos equipos de desarrollo en diversas industrias, desde pequeñas startups hasta grandes empresas, lo utilizan.

### ¿Qué repositorios tienen muchas Actions?

Las GitHub Actions se definen dentro de repositorios individuales, típicamente en el directorio `.github/workflows`. Los repositorios que utilizan extensamente GitHub Actions a menudo incluyen:

* **Repositorios oficiales de GitHub Actions:** La organización `github/actions` en GitHub contiene muchas de las acciones principales y de uso común como `actions/checkout`, `actions/setup-python`, `actions/setup-node`, `actions/upload-artifact` y `actions/download-artifact`. Estas son fundamentales para muchos flujos de trabajo.
* **Grandes proyectos de código abierto:** Los principales proyectos de código abierto en varios lenguajes de programación (por ejemplo, aquellos para Python, JavaScript, Go, C++) utilizan intensamente GitHub Actions para sus pipelines de construcción, prueba y lanzamiento. Los ejemplos a menudo incluyen proyectos de empresas como Google, Microsoft y otros gigantes tecnológicos, así como frameworks y librerías populares.
* **Proyectos centrados en la automatización y DevOps:** Los repositorios que demuestran prácticas de DevOps, automatizando varios aspectos de la infraestructura, las pruebas o la implementación, naturalmente tendrán un rico conjunto de flujos de trabajo de GitHub Actions.
* **Repositorios populares:** Muchos repositorios populares en GitHub hoy en día (que se pueden encontrar en la página de tendencias de GitHub) a menudo muestran usos innovadores de GitHub Actions para cosas como generar contenido, ejecutar análisis de seguridad o automatizar lanzamientos.

En esencia, cualquier repositorio que se beneficie de procesos automatizados para la calidad del código, las pruebas, la implementación o la gestión general del repositorio es un candidato para tener un conjunto sólido de GitHub Actions.