---
audio: false
generated: true
lang: es
layout: post
title: Cargador Universal de Imágenes en Android
translated: true
type: note
---

Universal Image Loader (UIL) versión 1.9.3 es una librería potente y flexible para cargar, almacenar en caché y mostrar imágenes en aplicaciones Android. A continuación se muestra una guía paso a paso sobre cómo usarla en tu proyecto de Android. Ten en cuenta que esta librería es antigua y ha sido descontinuada (última actualización alrededor de 2015), así que para proyectos modernos, podrías considerar alternativas como Glide o Picasso. Sin embargo, si específicamente necesitas usar UIL 1.9.3, aquí te explicamos cómo hacerlo:

---

### Paso 1: Añadir la Librería a Tu Proyecto
Dado que UIL 1.9.3 está disponible a través de Maven, puedes añadirla a tu proyecto usando Gradle. Si estás trabajando con una configuración antigua (por ejemplo, Eclipse), puedes descargar el archivo JAR manualmente.

#### Usando Gradle (Android Studio):
1. Abre el archivo `build.gradle` de tu app (Módulo: app).
2. Añade la siguiente dependencia en el bloque `dependencies`:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. Sincroniza tu proyecto con Gradle haciendo clic en "Sync Now" en Android Studio.

#### Configuración Manual del JAR (por ejemplo, Eclipse):
1. Descarga el `universal-image-loader-1.9.3.jar` desde el Repositorio Maven o GitHub.
2. Coloca el archivo JAR en la carpeta `libs` de tu proyecto.
3. Haz clic derecho en el JAR en tu IDE, luego selecciona "Add to Build Path" (Eclipse) o configúralo manualmente en la configuración de tu proyecto.

---

### Paso 2: Añadir Permisos
Para cargar imágenes desde internet o guardarlas en el almacenamiento, añade los siguientes permisos en tu `AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: Necesario para descargar imágenes desde URLs.
- `WRITE_EXTERNAL_STORAGE`: Necesario para el almacenamiento en caché en disco (opcional, pero recomendado para uso sin conexión). Para Android 6.0+ (API 23+), también necesitarás solicitar este permiso en tiempo de ejecución.

---

### Paso 3: Inicializar el ImageLoader
Antes de usar UIL, debes inicializarlo con una configuración. Esto se hace típicamente una vez en tu clase `Application` o `Activity` principal.

#### Crear una Clase Application Personalizada (Recomendado):
1. Crea una nueva clase (por ejemplo, `MyApplication.java`):
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // Crear configuración global e inicializar ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // Prioridad más baja para hilos de carga de imágenes
               .denyCacheImageMultipleSizesInMemory()    // Evitar almacenar múltiples tamaños en caché
               .diskCacheSize(50 * 1024 * 1024)          // Caché de disco de 50 MB
               .diskCacheFileCount(100)                  // Máximo 100 archivos en caché
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. Registra esta clase en tu `AndroidManifest.xml`:
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### O Inicializar en una Activity:
Si no quieres usar una clase `Application`, inicialízala en el método `onCreate()` de tu `Activity` (pero asegúrate de que solo se inicialice una vez):
```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
        .build();
    ImageLoader.getInstance().init(config);
}
```

---

### Paso 4: Cargar y Mostrar una Imagen
Una vez inicializado, puedes usar `ImageLoader` para cargar imágenes en un `ImageView`.

#### Uso Básico:
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // Cargar imagen en el ImageView
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### Uso Avanzado con Opciones de Visualización:
Puedes personalizar cómo se cargan y muestran las imágenes usando `DisplayImageOptions`:
```java
import com.nostra13.universalimageloader.core.DisplayImageOptions;
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // Definir opciones de visualización
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // Imagen mostrada mientras carga
            .showImageForEmptyUri(R.drawable.error)     // Imagen mostrada si la URL está vacía
            .showImageOnFail(R.drawable.error)          // Imagen mostrada si falla la carga
            .cacheInMemory(true)                        // Almacenar en caché en RAM
            .cacheOnDisk(true)                          // Almacenar en caché en disco
            .build();

        // Cargar imagen con opciones
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### Paso 5: Usar UIL en un ListView o GridView
Para listas o grids, usa UIL en tu adapter para cargar imágenes eficientemente.

#### Ejemplo de Adapter Personalizado:
```java
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import com.nostra13.universalimageloader.core.ImageLoader;

public class ImageAdapter extends BaseAdapter {
    private Context context;
    private String[] imageUrls; // Array de URLs de imágenes

    public ImageAdapter(Context context, String[] imageUrls) {
        this.context = context;
        this.imageUrls = imageUrls;
    }

    @Override
    public int getCount() {
        return imageUrls.length;
    }

    @Override
    public Object getItem(int position) {
        return imageUrls[position];
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.list_item, parent, false);
        }

        ImageView imageView = convertView.findViewById(R.id.imageView);
        ImageLoader.getInstance().displayImage(imageUrls[position], imageView);

        return convertView;
    }
}
```

#### Establecer el Adapter:
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### Características Clave de UIL 1.9.3
- **Tipos de URI Soportados**:
  - Web: `"http://example.com/image.jpg"`
  - Tarjeta SD: `"file:///mnt/sdcard/image.png"`
  - Content Provider: `"content://media/external/images/media/13"`
  - Assets: `"assets://image.png"`
  - Drawables: `"drawable://" + R.drawable.image`
- **Almacenamiento en Caché**: Soporta almacenamiento en caché en memoria y en disco.
- **Personalización**: El tamaño del grupo de hilos, el tamaño de la caché y las opciones de decodificación de imágenes se pueden ajustar en la configuración.

---

### Resolución de Problemas
- **Error: "ImageLoader must be init with configuration"**  
  Asegúrate de que `ImageLoader.getInstance().init(config)` se llama antes de cualquier llamada a `displayImage`.
- **Las Imágenes No Se Cargan**  
  - Verifica los permisos de internet y la validez de la URL.
  - Habilita el registro en la configuración (`.writeDebugLogs()`) para depurar problemas.
- **Errores de Memoria Insuficiente (Out of Memory)**  
  - Reduce `diskCacheSize` o `memoryCacheSize` en la configuración.
  - Usa imágenes más pequeñas o habilita el escalado hacia abajo en `DisplayImageOptions`.

---

### Notas
- **Descontinuación**: UIL 1.9.3 está obsoleto (última versión ~2014). Para el desarrollo moderno de Android, considera Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) o Coil (`implementation 'io.coil-kt:coil:2.6.0'`).
- **Contexto de Fecha**: A partir del 3 de marzo de 2025, esta guía asume que estás trabajando con código legado que requiere UIL 1.9.3.

¡Avísame si necesitas ayuda con un caso de uso específico!