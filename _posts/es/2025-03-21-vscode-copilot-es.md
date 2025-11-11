---
audio: false
generated: true
lang: es
layout: post
title: Cómo Empezar a Usar GitHub Copilot en VS Code
translated: true
type: note
---

Usar GitHub Copilot en Visual Studio Code (VS Code) es sencillo una vez que lo configuras. A continuación, una guía paso a paso para comenzar, actualizada al 20 de marzo de 2025:

---

### Paso 1: Instalar VS Code
- Asegúrate de tener Visual Studio Code instalado. Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/) si aún no lo tienes.
- Actualiza VS Code a la última versión para una compatibilidad óptima (ve a `Ayuda > Buscar actualizaciones`).

---

### Paso 2: Instalar la extensión GitHub Copilot
1. **Abre VS Code**.
2. **Ve al Marketplace de Extensiones**:
   - Haz clic en el icono de Extensiones en la Barra de Actividad de la izquierda (o presiona `Ctrl+Shift+X` / `Cmd+Shift+X` en Mac).
3. **Busca "GitHub Copilot"**:
   - Escribe "GitHub Copilot" en la barra de búsqueda.
   - Busca la extensión oficial de GitHub (tendrá una insignia verificada).
4. **Instala la Extensión**:
   - Haz clic en el botón `Instalar` junto a "GitHub Copilot".
5. **Opcional: Instalar Copilot Chat (Recomendado)**:
   - Busca "GitHub Copilot Chat" e instálala también. Esto añade funciones de IA conversacional, como hacer preguntas o generar código mediante chat.

---

### Paso 3: Iniciar sesión en GitHub Copilot
1. **Autentícate con GitHub**:
   - Después de la instalación, aparecerá un mensaje pidiéndote que inicies sesión.
   - Haz clic en `Iniciar sesión en GitHub` en la ventana emergente o ve al icono de estado de Copilot (en la esquina inferior derecha de VS Code) y selecciona "Iniciar sesión".
2. **Autoriza en el Navegador**:
   - Se abrirá una ventana del navegador pidiéndote que inicies sesión en tu cuenta de GitHub.
   - Aprueba la solicitud de autorización haciendo clic en `Authorize Git hypoxia`.
3. **Copia el Código**:
   - GitHub proporcionará un código de un solo uso. Cópialo y pégalo de nuevo en VS Code cuando se te solicite.
4. **Verifica la Activación**:
   - Una vez que hayas iniciado sesión, el icono de Copilot en la barra de estado debería volverse verde, indicando que está activo. También verás una notificación confirmando tu acceso.

---

### Paso 4: Configurar Copilot (Opcional)
- **Activar/Desactivar Sugerencias**:
  - Ve a `Archivo > Preferencias > Configuración` (o `Ctrl+,` / `Cmd+,`).
  - Busca "Copilot" para ajustar configuraciones, como activar sugerencias en línea o desactivarlas para lenguajes específicos.
- **Verificar Suscripción**:
  - Copilot requiere una suscripción ($10/mes o $100/año) después de una prueba de 30 días. Estudiantes, profesores y mantenedores de código abierto pueden solicitar acceso gratuito a través de [GitHub Education](https://education.github.com/) o la configuración de Copilot.

---

### Paso 5: Comenzar a usar Copilot
Así es como puedes aprovechar Copilot en tu flujo de trabajo de programación:

#### 1. **Sugerencias de Código**
- **Autocompletado en Línea**:
  - Comienza a escribir en un archivo (por ejemplo, `def calculate_sum(` en Python) y Copilot sugerirá completamientos en texto gris.
  - Presiona `Tab` para aceptar la sugerencia o sigue escribiendo para ignorarla.
- **Sugerencias Multilínea**:
  - Escribe un comentario como `// Función para ordenar un array` y presiona Enter. Copilot podría sugerir una implementación completa (por ejemplo, un algoritmo de ordenación).
  - Usa `Alt+]` (u `Option+]` en Mac) para alternar entre múltiples sugerencias.

#### 2. **Generación de Código desde Comentarios**
- Escribe un comentario descriptivo como:
  ```javascript
  // Obtener datos de una API y manejar errores
  ```
  Presiona Enter, y Copilot podría generar:
  ```javascript
  async function fetchData(url) {
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('Network response was not ok');
      return await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
  ```
- Acepta con `Tab` o modifica según sea necesario.

#### 3. **Copilot Chat (Si está instalado)**
- **Abrir Chat**:
  - Haz clic en el icono de chat en la barra lateral o usa `Ctrl+Alt+C` (personalizable).
- **Hacer Preguntas**:
  - Escribe algo como "Explica cómo funcionan las Promesas en JavaScript" o "Escribe un script en Python para leer un archivo CSV".
  - Copilot responderá en el panel de chat y puede insertar código directamente en tu editor.
- **Ayuda Contextual**:
  - Resalta código, haz clic derecho y selecciona "Ask Copilot" para explicarlo o refactorizarlo.

#### 4. **Depuración y Pruebas**
- Escribe un comentario como `// Escribe pruebas unitarias para esta función`, y Copilot puede generar casos de prueba usando frameworks como Jest o PyTest.

---

### Consejos para un Uso Efectivo
- **Sé Específico**: Cuanto más contexto proporciones (por ejemplo, comentarios, nombres de variables), mejores serán las sugerencias de Copilot.
- **Revisa las Sugerencias**: Copilot no es perfecto; siempre verifica su código para asegurar precisión y seguridad.
- **Soporte de Lenguajes**: Funciona mejor con lenguajes populares (Python, JavaScript, Java, etc.), pero admite docenas más.
- **Atajos de Teclado**:
  - `Alt+\` (u `Option+\` en Mac): Mostrar todas las sugerencias manualmente.
  - `Ctrl+Enter`: Abrir el panel de sugerencias.

---

### Resolución de Problemas
- **¿No Funciona?**:
  - Asegúrate de haber iniciado sesión (revisa la barra de estado).
  - Verifica que tu suscripción esté activa en la configuración de tu cuenta de GitHub.
  - Reinicia VS Code o reinstala la extensión si los problemas persisten.
- **¿No Hay Sugerencias?**:
  - Comprueba si Copilot está habilitado para el lenguaje actual (`editor.inlineSuggest.enabled` debe ser verdadero en la configuración).

---

¡Eso es todo! Ahora estás listo para usar GitHub Copilot en VS Code. Comienza abriendo un archivo, escribe algo de código o un comentario y deja que Copilot te asista. ¡Disfruta programando de manera más inteligente!