---
audio: false
generated: true
lang: es
layout: post
title: Cursor y VS Code
translated: true
type: note
---

Sí, es legal que Cursor haga un fork de Visual Studio Code (VS Code) y construya un negocio alrededor de él, siempre que cumpla con los términos de la licencia MIT bajo la cual se publica el código fuente de VS Code. La licencia MIT es muy permisiva y permite a cualquier persona usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y vender copias del software, siempre que el aviso de copyright original y el aviso de permiso se incluyan en todas las copias o partes sustanciales del software.

Estos son los puntos clave con respecto a la legalidad del fork de Cursor:

1.  **Cumplimiento de la Licencia MIT**: El código fuente de VS Code, disponible en el repositorio de GitHub `vscode`, tiene licencia MIT. Esto permite a Cursor hacer un fork del código base, modificarlo y usarlo para fines comerciales, incluida la creación de un producto de código cerrado, siempre que incluyan la licencia MIT original y el aviso de copyright en su distribución. La licencia MIT no requiere que el proyecto bifurcado permanezca de código abierto, por lo que Cursor puede hacer legalmente su producto propietario.

2.  **Visual Studio Code vs. Code-OSS**: Existe una distinción entre el repositorio de código abierto `vscode` (a menudo referido como Code-OSS) y el producto Microsoft Visual Studio Code con marca. El VS Code con marca de Microsoft incluye adiciones propietarias (por ejemplo, telemetría, integración con el marketplace) y se distribuye bajo una licencia diferente. Sin embargo, hacer un fork del repositorio de código abierto `vscode`, que está bajo la licencia MIT, es lo que Cursor y proyectos similares como Windsurf han hecho. Esto está explícitamente permitido, y pueden construir sus propias personalizaciones sobre él.

3.  **Restricciones del Visual Studio Marketplace**: Una limitación significativa para los forks como Cursor es que no pueden acceder al Visual Studio Marketplace oficial debido a los Términos de Servicio de Microsoft. Esto significa que Cursor no puede ofrecer el mismo ecosistema de extensiones que VS Code a menos que configuren un registro de extensiones alternativo (por ejemplo, OpenVSX) o desarrollen el suyo propio. Además, algunas extensiones propietarias, como GitHub Copilot o las extensiones de C/C++ de Microsoft, están restringidas a las compilaciones oficiales de VS Code de Microsoft, lo que puede limitar la funcionalidad de los forks.

4.  **Preocupaciones Éticas y de la Comunidad**: Si bien hacer un fork es legal bajo la licencia MIT, algunos han planteado preocupaciones éticas sobre empresas como Cursor que toman un proyecto de código abierto, agregan funciones y lo venden como un producto propietario sin contribuir de vuelta a la comunidad original de VS Code. Por ejemplo, publicaciones en X han expresado sentimientos encontrados, con algunos usuarios cuestionando si es justo que Cursor obtenga ganancias de un código desarrollado en gran medida por el equipo de VS Code. Sin embargo, este es un debate moral, no legal, y la licencia MIT permite explícitamente dicho uso.

5.  **Respuesta de Microsoft**: Microsoft ha tomado medidas para proteger su ecosistema, como restringir el acceso al marketplace y las extensiones propietarias para los forks, como se vio con acciones como eliminar el soporte de la extensión C/C++ de las compilaciones no oficiales. Sin embargo, estas restricciones no afectan la legalidad de hacer un fork del repositorio `vscode` en sí, siempre que el fork cumpla con la licencia MIT.

En resumen, el fork de VS Code por parte de Cursor es legal bajo la licencia MIT, ya que son libres de modificar y comercializar el código base, siempre que incluyan los avisos de copyright y licencia requeridos. Los principales desafíos que enfrentan son prácticos, como la falta de acceso al VS Code Marketplace y a ciertas extensiones propietarias, en lugar de barreras legales. Si tiene inquietudes sobre aspectos específicos de la implementación o el cumplimiento de Cursor, es recomendable consultar a un profesional legal para su jurisdicción, ya que yo no soy abogado.