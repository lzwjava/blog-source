---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Liberar Espacio en Disco Limpiando Basura de Xcode
translated: true
type: note
---

Buena pregunta 👍 Xcode (y el iOS Simulator) pueden acumular *mucha* basura con el tiempo: caché de compilación, datos derivados, dispositivos simulador, archivos de soporte para dispositivos, registros, etc. Limpiarlos libera gigabytes. Aquí tienes un enfoque estructurado:

---

### 1. Borrar Datos Derivados (Caché de Compilación)

Esto elimina productos de compilación antiguos, intermedios e índices.

* Desde la **Interfaz de Xcode**:
  `Xcode → Settings → Locations → Derived Data → haz clic en la flecha → elimina las carpetas.`
* Desde la **Terminal**:

  ```bash
  rm -rf ~/Library/Developer/Xcode/DerivedData/*
  ```

---

### 2. Limpiar Datos del Simulador

* Restablecer o eliminar contenidos del simulador:

  ```bash
  xcrun simctl erase all
  ```

  (borra aplicaciones y datos, pero mantiene las definiciones de dispositivos)

* Para eliminar todos los dispositivos de simulador no utilizados (si has acumulado versiones antiguas de iOS):

  ```bash
  xcrun simctl delete unavailable
  ```

* Para eliminar todos los dispositivos de simulador (ten cuidado, eliminará todo):

  ```bash
  xcrun simctl delete all
  ```

* Eliminar manualmente directorios pesados:

  ```bash
  rm -rf ~/Library/Developer/CoreSimulator/Devices/*
  ```

---

### 3. Eliminar Archivos de Soporte de Dispositivos Antiguos

Cuando conectas dispositivos reales, Xcode descarga símbolos de depuración para cada versión de iOS. Se acumulan.

```bash
rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*
```

---

### 4. Limpiar Archivos de Archivo (Archives)

Los archivos de aplicación de "Product → Archive" consumen mucho espacio.

* Desde el Organizador en Xcode → Archives → elimina los antiguos.
* O vía Terminal:

  ```bash
  rm -rf ~/Library/Developer/Xcode/Archives/*
  ```

---

### 5. Limpiar Registros (Logs)

```bash
rm -rf ~/Library/Developer/Xcode/DocumentationCache/*
rm -rf ~/Library/Developer/Xcode/ios device logs/*
rm -rf ~/Library/Logs/CoreSimulator/*
```

---

### 6. Limpiar Índices Derivados y Caché de Módulos

```bash
rm -rf ~/Library/Developer/Xcode/DerivedDataModuleCache/*
```

---

### 7. Opcional: Restablecimiento Completo

Si quieres restablecer completamente las cachés relacionadas con Xcode:

```bash
rm -rf ~/Library/Developer/Xcode/*
rm -rf ~/Library/Developer/CoreSimulator/*
```

(Esto elimina todo: simuladores, archivos de archivo, datos derivados, etc. El próximo inicio de Xcode se sentirá como una "instalación nueva").

---

⚠️ **Consejos**

* Siempre cierra Xcode y el Simulador antes de ejecutar estos comandos.
* Usa `du -sh ~/Library/Developer/*` para ver qué carpetas son las más grandes.
* A veces `Clean Build Folder` (`⇧⌘K`) en Xcode es suficiente, pero una limpieza profunda ahorra más espacio.

---

¿Quieres que te proporcione un **script único** que puedas ejecutar para limpiar toda la basura común de una vez (con banderas opcionales)?