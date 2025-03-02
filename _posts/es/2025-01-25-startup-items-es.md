---
audio: false
generated: true
lang: es
layout: post
title: Limpiar Elementos de Inicio en macOS
translated: true
---

Para gestionar las aplicaciones y procesos que se inician automáticamente cuando inicias sesión en macOS (incluyendo macOS 15.2 y versiones posteriores), puedes ajustar tus elementos de inicio. Aquí te explicamos cómo hacerlo:

### 1. **Usando Configuración del Sistema (o Preferencias del Sistema)**

   - **Paso 1:** Haz clic en el menú de Apple () en la esquina superior izquierda de tu pantalla y selecciona **Configuración del Sistema** (o **Preferencias del Sistema** en versiones anteriores de macOS).
   - **Paso 2:** Dirígete a **General** y luego a **Elementos de Inicio**.
   - **Paso 3:** Se mostrará una lista de aplicaciones y servicios que se inician al arrancar. Para eliminar un elemento, selecciónalo y haz clic en el botón **menos (–)** debajo de la lista.
   - **Paso 4:** Repite este proceso para todos los elementos que desees eliminar.

### 2. **Ajustando Configuraciones Específicas de la Aplicación**

   - Muchas aplicaciones incluyen sus propias configuraciones para controlar el comportamiento de inicio. Busca en las preferencias o ajustes de la aplicación para desactivar el inicio automático.

### 3. **Gestionando Agentes y Daemons de Inicio (Avanzado)**

   - Los procesos en segundo plano pueden ser gestionados por Agentes de Inicio o Daemons de Inicio. Estos suelen ubicarse en los siguientes directorios:
     - `~/Library/LaunchAgents` (para agentes específicos del usuario)
     - `/Library/LaunchAgents` (para agentes de todo el sistema)
     - `/Library/LaunchDaemons` (para daemons de todo el sistema)
   - **Precaución:** Modificar estos archivos puede afectar la estabilidad del sistema. Procede con cuidado.

### Consejos:

- **Reinicia tu Mac:** Después de realizar cambios, reinicia tu Mac para confirmar que los elementos de inicio ya no se ejecutan.