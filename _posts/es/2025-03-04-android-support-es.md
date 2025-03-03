---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca de soporte de Android
translated: true
---

La biblioteca de soporte de Android versión `support-v4:19.1.0` es una versión antigua de la biblioteca de compatibilidad v4 de la biblioteca de soporte de Android, que proporciona APIs compatibles hacia atrás para dispositivos Android que ejecutan niveles de API inferiores a los más recientes en el momento de su lanzamiento (circa 2014). Esta biblioteca te permite usar características introducidas en versiones más nuevas de Android en dispositivos más antiguos, como Fragments, Loaders y otras utilidades.

Dado que `support-v4:19.1.0` forma parte de la biblioteca de soporte de Android heredada, ha sido reemplazada por las bibliotecas AndroidX. Sin embargo, si necesitas usar esta versión específica (por ejemplo, para mantener un proyecto antiguo), aquí te explicamos cómo configurarla y usarla en tu proyecto de Android:

---

### Paso 1: Agregar la Dependencia
Para usar `support-v4:19.1.0`, necesitas incluirla como una dependencia en tu proyecto. Esto generalmente se hace en tu archivo `build.gradle` (Módulo: app).

#### Para Proyectos Basados en Gradle
1. Abre tu archivo `app/build.gradle`.
2. Agrega la siguiente línea al bloque `dependencies`:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Sincroniza tu proyecto con Gradle haciendo clic en "Sync Now" en Android Studio.

#### Notas:
- Asegúrate de que tu `compileSdkVersion` esté configurada en al menos 19 (Android 4.4 KitKat) o superior, ya que esta biblioteca está alineada con las características de la API 19.
- La versión mínima de SDK soportada por `support-v4:19.1.0` es la API 4 (Android 1.6), pero debes configurar tu `minSdkVersion` según los requisitos de tu aplicación.

Ejemplo `build.gradle`:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // Ajusta según sea necesario
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### Paso 2: Verificar la Disponibilidad
Las bibliotecas de soporte de Android se alojan en el repositorio Maven de Google. A partir de Android Studio 3.0+, este repositorio se incluye por defecto. Si usas una versión anterior de Android Studio, asegúrate de que lo siguiente esté en tu `build.gradle` (nivel de proyecto):

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // Nota: JCenter está obsoleto, pero se usaba para bibliotecas más antiguas
    }
}
```

Si encuentras problemas al descargar la biblioteca, es posible que necesites instalar el repositorio de soporte de Android a través del Administrador de SDK:
1. Ve a `Herramientas > Administrador de SDK`.
2. En la pestaña "Herramientas de SDK", marca "Repositorio de soporte de Android" e instálalo.

---

### Paso 3: Usar la Biblioteca en tu Código
La biblioteca `support-v4` proporciona una variedad de clases, como `Fragment`, `Loader`, `AsyncTaskLoader` y utilidades como `ActivityCompat`. A continuación, se muestran ejemplos de cómo usar algunos componentes comunes:

#### Ejemplo 1: Usar Fragments
La biblioteca `support-v4` incluye una clase `Fragment` retrocompatible que funciona en versiones más antiguas de Android.

```java
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class MyFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_layout, container, false);
    }
}
```

Para usar este fragmento en una actividad:
```java
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.os.Bundle;

public class MainActivity extends FragmentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FragmentManager fm = getSupportFragmentManager();
        fm.beginTransaction()
            .add(R.id.fragment_container, new MyFragment())
            .commit();
    }
}
```

#### Ejemplo 2: Usar ActivityCompat
La clase `ActivityCompat` proporciona métodos de ayuda para características compatibles hacia atrás, como solicitar permisos (introducidos en la API 23 pero utilizables en versiones anteriores con la biblioteca de soporte).

```java
import android.support.v4.app.ActivityCompat;
import android.Manifest;
import android.content.pm.PackageManager;

public class MainActivity extends FragmentActivity {
    private static final int REQUEST_CODE = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.CAMERA},
                    REQUEST_CODE);
        }
    }
}
```

---

### Paso 4: Consideraciones
- **Biblioteca Obsoleta**: La biblioteca de soporte de Android, incluida `support-v4:19.1.0`, está obsoleta. Para el desarrollo moderno, migra a AndroidX (por ejemplo, `androidx.legacy:legacy-support-v4:1.0.0`). AndroidX es el sucesor y proporciona actualizaciones y soporte continuos.
- **Coincidencia de Versiones**: Si usas otras bibliotecas de soporte (por ejemplo, `appcompat-v7`), asegúrate de que sean de la misma versión (19.1.0) para evitar errores de incompatibilidad de versiones.
- **Versión Mínima de SDK**: Aunque `support-v4:19.1.0` soporta la API 4+, algunas características pueden requerir una `minSdkVersion` más alta (por ejemplo, API 14 para ciertos componentes introducidos más tarde).

---

### Paso 5: Migrar a AndroidX (Opcional pero Recomendado)
Si estás manteniendo un proyecto antiguo, considera migrar a AndroidX:
1. En Android Studio, ve a `Refactor > Migrate to AndroidX`.
2. Actualiza tus dependencias, por ejemplo, reemplaza `com.android.support:support-v4:19.1.0` con `androidx.legacy:legacy-support-v4:1.0.0`.
3. Sigue la guía de migración proporcionada por Android Studio.

---

### Solución de Problemas
- **"No se encontró la biblioteca"**: Asegúrate de que tu conexión a Internet esté activa y que el repositorio Maven de Google sea accesible.
- **Incompatibilidad de Versiones**: Si ves errores sobre versiones incompatibles de bibliotecas de soporte, alinea todas las dependencias `com.android.support` a 19.1.0.
- **Características Obsoletas**: Algunas APIs en `support-v4:19.1.0` (por ejemplo, `AsyncTask`) están desactualizadas. Consulta la documentación para alternativas.

¡Hazme saber si necesitas ayuda con un caso de uso específico o configuración!