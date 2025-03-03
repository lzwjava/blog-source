---
audio: false
generated: true
lang: de
layout: post
title: Universeller Bildlader in Android
translated: true
---

Universal Image Loader (UIL) Version 1.9.3 ist eine leistungsstarke und flexible Bibliothek zum Laden, Cachen und Anzeigen von Bildern in Android-Anwendungen. Hier ist eine Schritt-für-Schritt-Anleitung zur Verwendung in Ihrem Android-Projekt. Beachten Sie, dass diese Bibliothek älter ist und eingestellt wurde (zuletzt aktualisiert um 2015), daher sollten Sie für moderne Projekte Alternativen wie Glide oder Picasso in Betracht ziehen. Wenn Sie jedoch spezifisch UIL 1.9.3 verwenden müssen, hier ist wie:

---

### Schritt 1: Bibliothek zum Projekt hinzufügen
Da UIL 1.9.3 über Maven verfügbar ist, können Sie es mit Gradle zu Ihrem Projekt hinzufügen. Wenn Sie mit einer älteren Einrichtung arbeiten (z.B. Eclipse), können Sie die JAR-Datei manuell herunterladen.

#### Verwenden von Gradle (Android Studio):
1. Öffnen Sie die `build.gradle`-Datei Ihrer App (Modul: app).
2. Fügen Sie die folgende Abhängigkeit im `dependencies`-Block hinzu:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. Synchronisieren Sie Ihr Projekt mit Gradle, indem Sie auf "Sync Now" in Android Studio klicken.

#### Manuelle JAR-Einrichtung (z.B. Eclipse):
1. Laden Sie die `universal-image-loader-1.9.3.jar` von dem Maven Repository oder GitHub herunter.
2. Legen Sie die JAR-Datei in den `libs`-Ordner Ihres Projekts.
3. Klicken Sie mit der rechten Maustaste auf die JAR in Ihrer IDE und wählen Sie "Add to Build Path" (Eclipse) oder konfigurieren Sie sie manuell in den Projekteinstellungen.

---

### Schritt 2: Berechtigungen hinzufügen
Um Bilder aus dem Internet zu laden oder sie auf dem Speicher zu speichern, fügen Sie die folgenden Berechtigungen zu Ihrer `AndroidManifest.xml` hinzu:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: Erforderlich zum Herunterladen von Bildern von URLs.
- `WRITE_EXTERNAL_STORAGE`: Erforderlich für das Disk-Caching (optional, aber für die Offline-Nutzung empfohlen). Für Android 6.0+ (API 23+) müssen Sie diese Berechtigung auch zur Laufzeit anfordern.

---

### Schritt 3: ImageLoader initialisieren
Bevor Sie UIL verwenden, müssen Sie es mit einer Konfiguration initialisieren. Dies wird normalerweise einmal in Ihrer `Application`-Klasse oder Haupt-`Activity` durchgeführt.

#### Erstellen Sie eine benutzerdefinierte Application-Klasse (Empfohlen):
1. Erstellen Sie eine neue Klasse (z.B. `MyApplication.java`):
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // Erstellen Sie eine globale Konfiguration und initialisieren Sie ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // Niedrigere Priorität für Bildlade-Threads
               .denyCacheImageMultipleSizesInMemory()    // Verhindern Sie das Cachen mehrerer Größen im Speicher
               .diskCacheSize(50 * 1024 * 1024)          // 50 MB Disk-Cache
               .diskCacheFileCount(100)                  // Max. 100 Dateien im Cache
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. Registrieren Sie diese Klasse in Ihrer `AndroidManifest.xml`:
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### Oder Initialisieren in einer Activity:
Wenn Sie keine `Application`-Klasse verwenden möchten, initialisieren Sie sie in der `onCreate()`-Methode Ihrer `Activity` (stellen Sie sicher, dass sie nur einmal initialisiert wird):
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

### Schritt 4: Bild laden und anzeigen
Sobald initialisiert, können Sie `ImageLoader` verwenden, um Bilder in ein `ImageView` zu laden.

#### Grundlegende Verwendung:
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // Bild in ImageView laden
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### Fortgeschrittene Verwendung mit Anzeigeoptionen:
Sie können anpassen, wie Bilder geladen und angezeigt werden, indem Sie `DisplayImageOptions` verwenden:
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

        // Anzeigeoptionen definieren
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // Bild, das beim Laden angezeigt wird
            .showImageForEmptyUri(R.drawable.error)     // Bild, das angezeigt wird, wenn die URL leer ist
            .showImageOnFail(R.drawable.error)          // Bild, das angezeigt wird, wenn das Laden fehlschlägt
            .cacheInMemory(true)                        // Cache im RAM
            .cacheOnDisk(true)                          // Cache auf der Festplatte
            .build();

        // Bild mit Optionen laden
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### Schritt 5: Verwenden von UIL in einer ListView oder GridView
Für Listen oder Raster verwenden Sie UIL in Ihrem Adapter, um Bilder effizient zu laden.

#### Beispiel für benutzerdefinierten Adapter:
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
    private String[] imageUrls; // Array von Bild-URLs

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

#### Adapter setzen:
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### Wichtige Funktionen von UIL 1.9.3
- **Unterstützte URI-Typen**:
  - Web: `"http://example.com/image.jpg"`
  - SD-Karte: `"file:///mnt/sdcard/image.png"`
  - Content Provider: `"content://media/external/images/media/13"`
  - Assets: `"assets://image.png"`
  - Drawables: `"drawable://" + R.drawable.image`
- **Caching**: Unterstützt Speicher- und Disk-Caching.
- **Anpassung**: Thread-Pool-Größe, Cache-Größe und Bilddecodierungsoptionen können in der Konfiguration angepasst werden.

---

### Fehlerbehebung
- **Absturz: "ImageLoader muss mit Konfiguration initialisiert werden"**
  Stellen Sie sicher, dass `ImageLoader.getInstance().init(config)` vor jedem `displayImage`-Aufruf aufgerufen wird.
- **Bilder werden nicht geladen**
  - Überprüfen Sie Internet-Berechtigungen und URL-Gültigkeit.
  - Aktivieren Sie das Protokollieren in der Konfiguration (`.writeDebugLogs()`), um Probleme zu debuggen.
- **Out-of-Memory-Fehler**
  - Reduzieren Sie `diskCacheSize` oder `memoryCacheSize` in der Konfiguration.
  - Verwenden Sie kleinere Bilder oder aktivieren Sie das Herunterskalieren in `DisplayImageOptions`.

---

### Hinweise
- **Veraltet**: UIL 1.9.3 ist veraltet (letzte Veröffentlichung ~2014). Für moderne Android-Entwicklung sollten Sie Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) oder Coil (`implementation 'io.coil-kt:coil:2.6.0'`) in Betracht ziehen.
- **Datumskontext**: Stand 3. März 2025 geht diese Anleitung davon aus, dass Sie mit Legacy-Code arbeiten, der UIL 1.9.3 erfordert.

Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Anwendungsfall benötigen!