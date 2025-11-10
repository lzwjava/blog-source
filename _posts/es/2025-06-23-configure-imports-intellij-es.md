---
audio: false
generated: true
lang: es
layout: post
title: Configuración de importaciones de clase única en IntelliJ IDEA
translated: true
type: note
---

IntelliJ IDEA proporciona configuraciones para controlar cómo maneja las importaciones, incluyendo prevenir el uso de comodines. Así es como puedes configurarlo para usar siempre importaciones de clase única:

1.  **Abrir Configuración/Preferencias:**
    * **Windows/Linux:** `Ctrl + Alt + S`
    * **macOS:** `Cmd + ,` (Coma)

2.  **Navegar a Estilo de Código para Java:**
    * En el panel izquierdo del cuadro de diálogo de Configuración, navega a:
        `Editor` -> `Estilo de Código` -> `Java`

3.  **Ir a la pestaña "Imports":**
    * En el lado derecho, selecciona la pestaña `Imports`.

4.  **Configurar los Ajustes de Importación:**
    Verás algunos ajustes importantes aquí:

    * **`Usar importación de clase única`**: **Marca esta casilla.** Este es el ajuste principal que le dice a IntelliJ que prefiera importaciones de clases individuales sobre importaciones con comodín.

    * **`Número de clases para usar importación con '*'`**: Este ajuste determina cuántas clases de un solo paquete deben importarse antes de que IntelliJ cambie automáticamente a una importación con comodín (ej., `java.util.*`). Para deshabilitar efectivamente las importaciones con comodín, **establece esto en un número muy alto**, como `999` o `9999`. Esto asegura que casi nunca alcanzarás el umbral para una importación con comodín.

    * **`Número de nombres para usar importación estática con '*'`**: Esto es similar a lo anterior pero para importaciones estáticas. Establece esto también en un número alto (ej., `999` o `9999`) para prevenir importaciones estáticas con comodín.

    * **`Paquetes para usar importaciones con '*'`**: Esta tabla enumera los paquetes para los cuales IntelliJ *siempre* usará importaciones con comodín, independientemente de los otros ajustes. **Asegúrate de que esta tabla esté vacía** si quieres evitar completamente las importaciones con comodín. Si ves entradas como `java.util.*` o `java.awt.*`, elimínalas.

5.  **Aplicar los Cambios:**
    * Haz clic en `Aplicar` y luego en `Aceptar` para guardar tus cambios.

**Después de realizar estos cambios:**

* Cuando uses la función "Auto Import" (ej., presionando `Alt + Enter` en una clase no resuelta), IntelliJ ahora insertará importaciones de clases individuales en lugar de comodines.
* Si tienes archivos existentes con importaciones de comodín, puedes usar la acción "Optimizar Importaciones" (`Ctrl + Alt + O` en Windows/Linux, `Cmd + Option + O` en macOS) para convertirlas a importaciones de clase única de acuerdo con tus nuevos ajustes.

Siguiendo estos pasos, puedes prevenir efectivamente que IntelliJ IDEA use importaciones con comodín para archivos Java.