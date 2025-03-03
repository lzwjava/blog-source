---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque de support Android
translated: true
---

La bibliothèque de support Android version `support-v4:19.1.0` est une version plus ancienne de la bibliothèque de support Android (plus précisément la bibliothèque de compatibilité v4), qui fournit des API compatibles avec les versions antérieures pour les appareils Android fonctionnant avec des niveaux d'API inférieurs aux plus récents au moment de sa sortie (vers 2014). Cette bibliothèque vous permet d'utiliser des fonctionnalités introduites dans les versions plus récentes d'Android sur des appareils plus anciens, telles que les Fragments, les Loaders et d'autres utilitaires.

Puisque `support-v4:19.1.0` fait partie de la bibliothèque de support Android héritée, elle a été remplacée par les bibliothèques AndroidX. Cependant, si vous avez besoin d'utiliser cette version spécifique (par exemple, pour maintenir un projet plus ancien), voici comment vous pouvez la configurer et l'utiliser dans votre projet Android :

---

### Étape 1 : Ajouter la dépendance
Pour utiliser `support-v4:19.1.0`, vous devez l'inclure comme dépendance dans votre projet. Cela se fait généralement dans votre fichier `build.gradle` (Module: app).

#### Pour les projets basés sur Gradle
1. Ouvrez votre fichier `app/build.gradle`.
2. Ajoutez la ligne suivante au bloc `dependencies` :

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Synchronisez votre projet avec Gradle en cliquant sur "Sync Now" dans Android Studio.

#### Notes :
- Assurez-vous que votre `compileSdkVersion` est définie à au moins 19 (Android 4.4 KitKat) ou une version supérieure, car cette bibliothèque est alignée avec les fonctionnalités de l'API 19.
- La version SDK minimale prise en charge par `support-v4:19.1.0` est l'API 4 (Android 1.6), mais vous devriez définir votre `minSdkVersion` en fonction des exigences de votre application.

Exemple `build.gradle` :
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // Ajustez selon les besoins
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### Étape 2 : Vérifier la disponibilité
Les bibliothèques de support Android sont hébergées dans le dépôt Maven de Google. À partir d'Android Studio 3.0+, ce dépôt est inclus par défaut. Si vous utilisez une version plus ancienne d'Android Studio, assurez-vous que ce qui suit est dans votre `build.gradle` (niveau projet) :

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // Note : JCenter est obsolète, mais était utilisé pour les bibliothèques plus anciennes
    }
}
```

Si vous rencontrez des problèmes de téléchargement de la bibliothèque, vous devrez peut-être installer le dépôt Android Support via le gestionnaire SDK :
1. Allez dans `Outils > Gestionnaire SDK`.
2. Sous l'onglet "Outils SDK", cochez "Android Support Repository" et installez-le.

---

### Étape 3 : Utiliser la bibliothèque dans votre code
La bibliothèque `support-v4` fournit une variété de classes, telles que `Fragment`, `Loader`, `AsyncTaskLoader` et des utilitaires comme `ActivityCompat`. Voici des exemples d'utilisation de certains composants courants :

#### Exemple 1 : Utiliser des Fragments
La bibliothèque `support-v4` inclut une classe `Fragment` rétroportée qui fonctionne sur les versions plus anciennes d'Android.

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

Pour utiliser ce fragment dans une activité :
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

#### Exemple 2 : Utiliser ActivityCompat
La classe `ActivityCompat` fournit des méthodes d'assistance pour les fonctionnalités compatibles avec les versions antérieures, telles que la demande de permissions (introduite dans l'API 23 mais utilisable plus tôt avec la bibliothèque de support).

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

### Étape 4 : Considérations
- **Bibliothèque obsolète** : La bibliothèque de support Android, y compris `support-v4:19.1.0`, est obsolète. Pour le développement moderne, migrez vers AndroidX (par exemple, `androidx.legacy:legacy-support-v4:1.0.0`). AndroidX est le successeur et fournit des mises à jour et un support continus.
- **Correspondance des versions** : Si vous utilisez d'autres bibliothèques de support (par exemple, `appcompat-v7`), assurez-vous qu'elles sont de la même version (19.1.0) pour éviter les erreurs de correspondance de versions.
- **SDK minimum** : Bien que `support-v4:19.1.0` prenne en charge l'API 4+, certaines fonctionnalités peuvent nécessiter une version `minSdkVersion` plus élevée (par exemple, l'API 14 pour certains composants introduits plus tard).

---

### Étape 5 : Migration vers AndroidX (facultatif mais recommandé)
Si vous maintenez un ancien projet, envisagez de migrer vers AndroidX :
1. Dans Android Studio, allez dans `Refactor > Migrate to AndroidX`.
2. Mettez à jour vos dépendances, par exemple, remplacez `com.android.support:support-v4:19.1.0` par `androidx.legacy:legacy-support-v4:1.0.0`.
3. Suivez le guide de migration fourni par Android Studio.

---

### Dépannage
- **"Could not find library"** : Assurez-vous que votre connexion Internet est active et que le dépôt Maven de Google est accessible.
- **Incompatibilité des versions** : Si vous voyez des erreurs concernant les versions incompatibles des bibliothèques de support, alignez toutes les dépendances `com.android.support` sur 19.1.0.
- **Fonctionnalités obsolètes** : Certaines API dans `support-v4:19.1.0` (par exemple, `AsyncTask`) sont obsolètes. Consultez la documentation pour des alternatives.

Faites-moi savoir si vous avez besoin d'aide pour un cas d'utilisation ou une configuration spécifique !