---
audio: false
generated: true
lang: fr
layout: post
title: Chargement d'images universel dans Android
translated: true
---

Universal Image Loader (UIL) version 1.9.3 est une bibliothèque puissante et flexible pour charger, mettre en cache et afficher des images dans les applications Android. Voici un guide étape par étape sur la façon de l'utiliser dans votre projet Android. Notez que cette bibliothèque est ancienne et a été abandonnée (dernière mise à jour autour de 2015), donc pour les projets modernes, vous pourriez envisager des alternatives comme Glide ou Picasso. Cependant, si vous avez spécifiquement besoin d'utiliser UIL 1.9.3, voici comment faire :

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

### Étape 2 : Ajouter des permissions
Pour charger des images depuis Internet ou les enregistrer dans le stockage, ajoutez les permissions suivantes à votre fichier `AndroidManifest.xml` :
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET` : Nécessaire pour télécharger des images à partir d'URL.
- `WRITE_EXTERNAL_STORAGE` : Nécessaire pour le cache disque (optionnel, mais recommandé pour une utilisation hors ligne). Pour Android 6.0+ (API 23+), vous devrez également demander cette permission au moment de l'exécution.

---

### Étape 3 : Initialiser l'ImageLoader
Avant d'utiliser UIL, vous devez l'initialiser avec une configuration. Cela est généralement fait une fois dans votre classe `Application` ou dans votre `Activity` principale.

#### Créer une classe Application personnalisée (recommandé) :
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
               .threadPriority(Thread.NORM_PRIORITY - 2) // Priorité inférieure pour les threads de chargement d'images
               .denyCacheImageMultipleSizesInMemory()    // Empêcher le cache de plusieurs tailles
               .diskCacheSize(50 * 1024 * 1024)          // Cache disque de 50 Mo
               .diskCacheFileCount(100)                  // Max 100 fichiers en cache
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. Enregistrez cette classe dans votre fichier `AndroidManifest.xml` :
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
Une fois initialisé, vous pouvez utiliser `ImageLoader` pour charger des images dans un `ImageView`.

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

        // Charger l'image dans ImageView
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### Utilisation avancée avec des options d'affichage :
Vous pouvez personnaliser la manière dont les images sont chargées et affichées en utilisant `DisplayImageOptions` :
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
            .cacheInMemory(true)                        // Cache en RAM
            .cacheOnDisk(true)                          // Cache sur disque
            .build();

        // Charger l'image avec les options
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### Étape 5 : Utiliser UIL dans un ListView ou GridView
Pour les listes ou les grilles, utilisez UIL dans votre adaptateur pour charger efficacement les images.

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
    private String[] imageUrls; // Tableau d'URL d'images

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
- **Types d'URI supportés** :
  - Web : `"http://example.com/image.jpg"`
  - Carte SD : `"file:///mnt/sdcard/image.png"`
  - Fournisseur de contenu : `"content://media/external/images/media/13"`
  - Assets : `"assets://image.png"`
  - Drawables : `"drawable://" + R.drawable.image`
- **Caching** : Prend en charge le cache en mémoire et sur disque.
- **Personnalisation** : La taille du pool de threads, la taille du cache et les options de décodage d'image peuvent être ajustées dans la configuration.

---

### Dépannage
- **Plantage : "ImageLoader doit être initialisé avec une configuration"**   \
  Assurez-vous que `ImageLoader.getInstance().init(config)` est appelé avant tout appel à `displayImage`.
- **Images ne se chargent pas**   \
  - Vérifiez les permissions Internet et la validité de l'URL.
  - Activez la journalisation dans la configuration (`.writeDebugLogs()`) pour déboguer les problèmes.
- **Erreurs de mémoire insuffisante**   \
  - Réduisez `diskCacheSize` ou `memoryCacheSize` dans la configuration.
  - Utilisez des images plus petites ou activez le redimensionnement dans `DisplayImageOptions`.

---

### Notes
- **Désuétude** : UIL 1.9.3 est obsolète (dernière version ~2014). Pour le développement Android moderne, envisagez Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) ou Coil (`implementation 'io.coil-kt:coil:2.6.0'`).
- **Contexte de la date** : À partir du 3 mars 2025, ce guide suppose que vous travaillez avec du code hérité nécessitant UIL 1.9.3.

Faites-moi savoir si vous avez besoin d'aide pour un cas d'utilisation spécifique !