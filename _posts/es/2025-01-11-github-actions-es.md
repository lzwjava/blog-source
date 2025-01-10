---
audio: true
lang: es
layout: post
title: "Tiempo Máximo de Ejecución de un Trabajo en GitHub Actions\n\nGitHub Actions\
  \ es una herramienta poderosa para la automatización de flujos de trabajo en el\
  \ desarrollo de software. Sin embargo, es importante tener en cuenta que los trabajos\
  \ en GitHub Actions tienen un límite de tiempo de ejecución. Este límite varía dependiendo\
  \ del tipo de repositorio y del plan de GitHub que estés utilizando.\n\n### Límites\
  \ de Tiempo de Ejecución\n\n- **Repositorios Públicos y Privados (Plan Gratuito):**\
  \ Cada trabajo tiene un tiempo máximo de ejecución de **6 horas**.\n- **Repositorios\
  \ Privados (Plan Pro o Team):** Cada trabajo tiene un tiempo máximo de ejecución\
  \ de **6 horas**.\n- **Repositorios Privados (Plan Enterprise):** Cada trabajo tiene\
  \ un tiempo máximo de ejecución de **72 horas**.\n\n### ¿Qué Ocurre si se Supera\
  \ el Tiempo Máximo?\n\nSi un trabajo supera el tiempo máximo de ejecución permitido,\
  \ GitHub Actions automáticamente cancelará el trabajo y lo marcará como fallido.\
  \ Esto puede interrumpir tu flujo de trabajo y requerir que reinicies el proceso\
  \ manualmente.\n\n### Cómo Evitar Superar el Tiempo Máximo\n\n1. **Optimiza tu Flujo\
  \ de Trabajo:** Revisa y optimiza los pasos de tu flujo de trabajo para reducir\
  \ el tiempo de ejecución.\n2. **Divide el Trabajo:** Si tienes un trabajo que requiere\
  \ mucho tiempo, considera dividirlo en varios trabajos más pequeños.\n3. **Usa Matrices:**\
  \ Si estás ejecutando pruebas en múltiples entornos, considera usar matrices para\
  \ ejecutar pruebas en paralelo.\n4. **Monitorea el Tiempo:** Usa herramientas de\
  \ monitoreo para rastrear el tiempo de ejecución de tus trabajos y ajusta según\
  \ sea necesario.\n\n### Ejemplo de Configuración\n\nAquí tienes un ejemplo de cómo\
  \ podrías configurar un trabajo en GitHub Actions para evitar superar el tiempo\
  \ máximo de ejecución:\n\n```yaml\nname: CI\n\non: [push]\n\njobs:\n  build:\n \
  \   runs-on: ubuntu-latest\n    steps:\n    - name: Checkout code\n      uses: actions/checkout@v2\n\
  \n    - name: Set up Node.js\n      uses: actions/setup-node@v2\n      with:\n \
  \       node-version: '14'\n\n    - name: Install dependencies\n      run: npm install\n\
  \n    - name: Run tests\n      run: npm test\n```\n\nEn este ejemplo, el trabajo\
  \ `build` ejecuta una serie de pasos para construir y probar una aplicación Node.js.\
  \ Si alguno de estos pasos toma demasiado tiempo, podrías considerar dividirlos\
  \ en trabajos separados o optimizar los comandos para reducir el tiempo de ejecución.\n\
  \n### Conclusión\n\nEntender y gestionar el tiempo máximo de ejecución de los trabajos\
  \ en GitHub Actions es crucial para mantener un flujo de trabajo eficiente y evitar\
  \ interrupciones. Al optimizar tus flujos de trabajo y monitorear el tiempo de ejecución,\
  \ puedes asegurarte de que tus trabajos se completen dentro de los límites establecidos."
translated: true
---

He estado utilizando GitHub Actions para automatizar la traducción de las publicaciones de mi blog. Inicialmente, intenté traducir todas las publicaciones en un solo trabajo, con los cambios confirmados en el repositorio solo después de que todas las traducciones estuvieran completas.

Era optimista y me fui a dormir, esperando que el proceso terminara. Sin embargo, después de 8 horas, me desperté y encontré el siguiente error:

> El trabajo que se ejecuta en el runner GitHub Actions 12 ha excedido el tiempo máximo de ejecución de 360 minutos.

Esto significaba que las 6 horas de trabajo de traducción se perdieron, ya que la confirmación solo ocurrió al final.

Para solucionar esto, modifiqué el flujo de trabajo para confirmar los cambios cada 10 archivos.

Además, implementé programación multihilo para reducir el tiempo total de traducción de 6 horas a aproximadamente una hora.

GitHub Actions ofrece mucha flexibilidad. Admite múltiples trabajos de flujo de trabajo, lo que permite la separación de tareas. Algunos trabajos pueden activarse en cada confirmación, mientras que otros pueden activarse por diferentes eventos.