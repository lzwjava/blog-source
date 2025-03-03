audio: false
lang: en
layout: post
title: ButterKnife: a View binding Library
translated: false
generated: true

Butter Knife es una popular biblioteca de enlace de vistas para Android que simplifica el proceso de enlazar elementos de la interfaz de usuario a campos en tu código. Sin embargo, ten en cuenta que Butter Knife ahora está obsoleto y el desarrollo moderno de Android recomienda usar View Binding (introducido en Android Jetpack) en su lugar. Aún así, si necesitas usar Butter Knife 6.1.0 (una versión más antigua lanzada alrededor de 2015) con un archivo `.jar` en un proyecto de Android, aquí te mostramos cómo hacerlo en Android Studio a partir del 3 de marzo de 2025.

### Requisitos Previos
- Android Studio instalado (cualquier versión reciente debería funcionar, aunque el proceso puede variar ligeramente según tu versión).
- Un proyecto de Android básico configurado.
- El archivo `butterknife-6.1.0.jar` descargado. Puedes encontrar versiones más antiguas en repositorios como Maven Central o a través de fuentes archivadas si tienes el archivo `.jar` localmente.

### Pasos para Usar `butterknife-6.1.0.jar` en el Desarrollo de Android

#### Paso 1: Agregar el Archivo `.jar` a tu Proyecto
1. **Localizar la Carpeta `libs`**:
   - En tu proyecto de Android Studio, navega al módulo `app`.
   - Dentro de la carpeta `app`, encuentra o crea una carpeta llamada `libs`. Si no existe, haz clic derecho en la carpeta `app`, selecciona `New > Directory` y nómbrala `libs`.

2. **Copiar el Archivo `.jar`**:
   - Copia el archivo `butterknife-6.1.0.jar` en la carpeta `libs`. Puedes hacerlo arrastrando y soltando el archivo en la carpeta `libs` en Android Studio o colocándolo manualmente a través de tu explorador de archivos.

3. **Sincronizar el Archivo `.jar` con Gradle**:
   - Abre el archivo `build.gradle` para el módulo `app` (ubicado en `app/build.gradle`).
   - Agrega la siguiente línea bajo el bloque `dependencies` para incluir todos los archivos `.jar` en la carpeta `libs`:
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - Sincroniza tu proyecto haciendo clic en el botón "Sync Project with Gradle Files" en Android Studio.

#### Paso 2: Configurar tu Proyecto
Dado que Butter Knife 6.1.0 utiliza procesamiento de anotaciones, no necesitas una dependencia de procesador de anotaciones para esta versión específica (a diferencia de versiones posteriores como 8.x y superiores). El archivo `.jar` incluye la biblioteca de tiempo de ejecución, y Butter Knife 6.1.0 se basa en la reflexión en tiempo de ejecución en lugar de la generación de código en tiempo de compilación para la mayoría de sus funcionalidades.

Sin embargo, asegúrate de que tu proyecto esté configurado para soportar anotaciones de Java:
- En tu `app/build.gradle`, asegúrate de que la versión de Java sea compatible (Butter Knife 6.1.0 funciona con Java 6+):
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### Paso 3: Usar Butter Knife en tu Código
1. **Agregar Anotaciones de Butter Knife**:
   - En tu Activity o Fragment, importa Butter Knife y anota tus vistas con `@InjectView` (la anotación utilizada en la versión 6.1.0). Por ejemplo:
     ```java
     import android.os.Bundle;
     import android.widget.Button;
     import android.widget.TextView;
     import butterknife.InjectView;
     import butterknife.ButterKnife;
     import androidx.appcompat.app.AppCompatActivity;

     public class MainActivity extends AppCompatActivity {

         @InjectView(R.id.my_button)
         Button myButton;

         @InjectView(R.id.my_text)
         TextView myText;

         @Override
         protected void onCreate(Bundle savedInstanceState) {
             super.onCreate(savedInstanceState);
             setContentView(R.layout.activity_main);
             ButterKnife.inject(this); // Enlazar vistas

             // Ejemplo de uso
             myButton.setOnClickListener(v -> myText.setText("¡Botón clicado!"));
         }
     }
     ```

2. **Archivo de Diseño XML**:
   - Asegúrate de que tu archivo de diseño (por ejemplo, `res/layout/activity_main.xml`) contenga las vistas con los IDs correspondientes:
     ```xml
     <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         android:orientation="vertical">

         <TextView
             android:id="@+id/my_text"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Hola Mundo" />

         <Button
             android:id="@+id/my_button"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Haz clic aquí" />
     </LinearLayout>
     ```

3. **Enlazar Vistas**:
   - La llamada `ButterKnife.inject(this)` en `onCreate` enlaza los campos anotados a las vistas del diseño. Ten en cuenta que en la versión 6.1.0, se utiliza `inject` en lugar de `bind` (que se introdujo en versiones posteriores como 7.x y 8.x).

#### Paso 4: Ejecutar tu Proyecto
- Compila y ejecuta tu proyecto. Si todo está configurado correctamente, Butter Knife enlazará tus vistas y deberías ver la interfaz de usuario funcionando como se espera.

### Notas Importantes
- **Limitación de Versión**: Butter Knife 6.1.0 es bastante antiguo (lanzado en 2015) y carece de características introducidas en versiones posteriores, como la generación de código en tiempo de compilación (a través de procesadores de anotaciones) y el soporte para `@BindView` en lugar de `@InjectView`. Utiliza reflexión en tiempo de ejecución, lo que puede afectar ligeramente el rendimiento en comparación con alternativas modernas.
- **Estado Obsoleto**: Butter Knife ya no se mantiene (el desarrollo se detuvo alrededor de 2020) y la recomendación oficial es usar View Binding o Jetpack Compose para nuevos proyectos.
- **Configuración Alternativa**: Si estuvieras utilizando una versión más nueva (por ejemplo, 10.2.3), necesitarías agregar una dependencia de procesador de anotaciones (por ejemplo, `annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`), pero para 6.1.0 con un archivo `.jar`, esto no es necesario.
- **Solución de Problemas**:
  - Si obtienes un error "cannot resolve symbol" para las clases de Butter Knife, asegúrate de que el archivo `.jar` esté correctamente agregado a la carpeta `libs` e incluido en las dependencias de Gradle.
  - Si la aplicación se bloquea con un `NoClassDefFoundError`, verifica que el archivo `.jar` esté en la carpeta `libs` y que el proyecto se haya sincronizado.

### Recomendación
Aunque esta guía te muestra cómo usar `butterknife-6.1.0.jar`, considera migrar a View Binding para un enfoque más moderno y soportado. Aquí tienes una comparación rápida:
- **Butter Knife 6.1.0**: Usa `@InjectView`, reflexión en tiempo de ejecución, integración manual de `.jar`.
- **View Binding**: Incorporado en Android, sin dependencias externas, genera clases de enlace en tiempo de compilación y es seguro contra nulos.