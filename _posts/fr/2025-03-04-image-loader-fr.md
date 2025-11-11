---
audio: false
generated: true
lang: fr
layout: post
title: Chargeur d'image universel pour Android
translated: true
type: note
---

Universal Image Loader (UIL) version 1.9.3 est une bibliothèque puissante et flexible pour charger, mettre en cache et afficher des images dans les applications Android. Voici un guide étape par étape pour l'utiliser dans votre projet Android. Notez que cette bibliothèque est ancienne et a été abandonnée (dernière mise à jour vers 2015). Pour les projets modernes, vous pourriez envisager des alternatives comme Glide ou Picasso. Cependant, si vous avez spécifiquement besoin d'utiliser UIL 1.9.3, voici comment procéder :

---

### Étape 1 : Ajouter la bibliothèque à votre projet
Puisque UIL 1.9.3 est disponible via Maven, vous pouvez l'ajouter à votre projet en utilisant Gradle. Si vous travaillez avec une configuration plus ancienne (par exemple, Eclipse), vous pouvez télécharger manuellement le fichier JAR.

#### Utilisation de Gradle (Android Studio) :
1. Ouvrez le fichier `build.gradle` de votre application (Module : app).
2. Ajoutez la dépendance suivante dans le bloc `dependencies` :
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. Synchronisez votre projet avec Gradle en cliquant sur "Sync Now" dans Android Studio.

#### Configuration manuelle du JAR (par exemple, Eclipse) :
1. Téléchargez le fichier `universal-image-loader-1.9.3.jar` depuis le dépôt Maven ou GitHub.
2. Placez le fichier JAR dans le dossier `libs` de votre projet.
3. Faites un clic droit sur le JAR dans votre IDE, puis sélectionnez "Add to Build Path" (Eclipse) ou configurez-le manuellement dans les paramètres de votre projet.

---

### Étape 2 : Ajouter les autorisations
Pour charger des images depuis Internet ou les enregistrer dans le stockage, ajoutez les autorisations suivantes à votre `AndroidManifest.xml` :
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET` : Requise pour télécharger des images à partir d'URL.
- `WRITE_EXTERNAL_STORAGE` : Requise pour la mise en cache sur le disque (optionnelle, mais recommandée pour une utilisation hors ligne). Pour Android 6.0+ (API 23+), vous devrez également demander cette autorisation à l'exécution.

---

### Étape 3 : Initialiser l'ImageLoader
Avant d'utiliser UIL, vous devez l'initialiser avec une configuration. Cela se fait généralement une fois dans votre classe `Application` ou `Activity` principale.

#### Créer une classe Application personnalisée (Recommandé) :
1. Créez une nouvelle classe (par exemple, `MyApplication.java`) :
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // Créer une configuration globale et initialiser ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // Priorité plus basse pour les threads de chargement d'image
               .denyCacheImageMultipleSizesInMemory()    // Empêche la mise en cache de multiples tailles
               .diskCacheSize(50 * 1024 * 1024)          // Cache disque de 50 Mo
               .diskCacheFileCount(100)                  // Max 100 fichiers en cache
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. Enregistrez cette classe dans votre `AndroidManifest.xml` :
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### Ou initialiser dans une Activity :
Si vous ne souhaitez pas utiliser une classe `Application`, initialisez-la dans la méthode `onCreate()` de votre `Activity` (mais assurez-vous qu'elle n'est initialisée qu'une seule fois) :
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

### Étape 4 : Charger et afficher une image
Une fois initialisé, vous pouvez utiliser `ImageLoader` pour charger des images dans une `ImageView`.

#### Utilisation de base :
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // Charger l'image dans l'ImageView
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### Utilisation avancée avec DisplayImageOptions :
Vous pouvez personnaliser la façon dont les images sont chargées et affichées en utilisant `DisplayImageOptions` :
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

        // Définir les options d'affichage
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // Image affichée pendant le chargement
            .showImageForEmptyUri(R.drawable.error)     // Image affichée si l'URL est vide
            .showImageOnFail(R.drawable.error)          // Image affichée en cas d'échec du chargement
            .cacheInMemory(true)                        // Mettre en cache en RAM
            .cacheOnDisk(true)                          // Mettre en cache sur le disque
            .build();

        // Charger l'image avec les options
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### Étape 5 : Utiliser UIL dans une ListView ou GridView
Pour les listes ou grilles, utilisez UIL dans votre adaptateur pour charger les images efficacement.

#### Exemple d'adaptateur personnalisé :
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
    private String[] imageUrls; // Tableau d'URLs d'images

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

#### Définir l'adaptateur :
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### Fonctionnalités clés de UIL 1.9.3
- **Types d'URI pris en charge** :
  - Web : `"http://example.com/image.jpg"`
  - Carte SD : `"file:///mnt/sdcard/image.png"`
  - Content Provider : `"content://media/external/images/media/13"`
  - Assets : `"assets://image.png"`
  - Drawables : `"drawable://" + R.drawable.image`
- **Mise en cache** : Prend en charge la mise en cache en mémoire et sur le disque.
- **Personnalisation** : La taille du pool de threads, la taille du cache et les options de décodage d'image peuvent être ajustées dans la configuration.

---

### Dépannage
- **Plantage : "ImageLoader must be init with configuration"**  
  Assurez-vous que `ImageLoader.getInstance().init(config)` est appelé avant tout appel à `displayImage`.
- **Les images ne se chargent pas**  
  - Vérifiez les autorisations Internet et la validité de l'URL.
  - Activez la journalisation dans la configuration (`.writeDebugLogs()`) pour déboguer les problèmes.
- **Erreurs de mémoire insuffisante (Out of Memory)**  
  - Réduisez `diskCacheSize` ou `memoryCacheSize` dans la configuration.
  - Utilisez des images plus petites ou activez la réduction d'échelle dans `DisplayImageOptions`.

---

### Notes
- **Obsolescence** : UIL 1.9.3 est obsolète (dernière version ~2014). Pour le développement Android moderne, envisagez Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) ou Coil (`implementation 'io.coil-kt:coil:2.6.0'`).
- **Contexte de date** : Au 3 mars 2025, ce guide suppose que vous travaillez avec du code hérité nécessitant UIL 1.9.3.

N'hésitez pas à me demander si vous avez besoin d'aide pour un cas d'utilisation spécifique !