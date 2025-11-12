---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca de Compatibilidad de Android
translated: true
type: note
---

La versión `support-v4:19.1.0` de la Android Support Library es una versión anterior de la biblioteca de compatibilidad de Android (específicamente la biblioteca de compatibilidad v4), que proporciona APIs con retrocompatibilidad para dispositivos Android que ejecutan niveles de API inferiores a los más recientes en el momento de su lanzamiento (alrededor de 2014). Esta biblioteca te permite utilizar funciones introducidas en versiones más nuevas de Android en dispositivos antiguos, como Fragments, Loaders y otras utilidades.

Dado que `support-v4:19.1.0` es parte de la antigua Android Support Library, ha sido reemplazada por las bibliotecas AndroidX. Sin embargo, si necesitas usar esta versión específica (por ejemplo, para mantener un proyecto antiguo), aquí se explica cómo puedes configurarla y usarla en tu proyecto de Android:

---

### Paso 1: Agregar la Dependencia
Para usar `support-v4:19.1.0`, necesitas incluirla como una dependencia en tu proyecto. Esto se hace típicamente en tu archivo `build.gradle` (Módulo: app).

#### Para Proyectos Basados en Gradle
1. Abre tu archivo `app/build.gradle`.
2. Agrega la siguiente línea en el bloque `dependencies`:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Sincroniza tu proyecto con Gradle haciendo clic en "Sync Now" en Android Studio.

#### Notas:
- Asegúrate de que tu `compileSdkVersion` esté establecido al menos en 19 (Android 4.4 KitKat) o superior, ya que esta biblioteca está alineada con las características de API 19.
- La versión mínima del SDK compatible con `support-v4:19.1.0` es API 4 (Android 1.6), pero debes establecer tu `minSdkVersion` según los requisitos de tu aplicación.

Ejemplo de `build.gradle`:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // Ajusta según sea necesario
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com