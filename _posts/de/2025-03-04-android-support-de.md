---
audio: false
generated: true
lang: de
layout: post
title: Android-Support-Bibliothek
translated: true
---

Die Android Support Library Version `support-v4:19.1.0` ist eine ältere Version der Android Support Library (speziell die v4-Kompatibilitätsbibliothek), die rückwärtskompatible APIs für Android-Geräte bereitstellt, die API-Level verwenden, die niedriger sind als die neuesten zum Zeitpunkt ihrer Veröffentlichung (circa 2014). Diese Bibliothek ermöglicht es Ihnen, Funktionen zu verwenden, die in neueren Android-Versionen eingeführt wurden, auf älteren Geräten, wie z.B. Fragments, Loaders und andere Hilfsprogramme.

Da `support-v4:19.1.0` Teil der veralteten Android Support Library ist, wurde es durch die AndroidX-Bibliotheken ersetzt. Wenn Sie jedoch diese spezifische Version verwenden müssen (z.B. zur Wartung eines älteren Projekts), hier ist, wie Sie sie einrichten und in Ihrem Android-Projekt verwenden können:

---

### Schritt 1: Abhängigkeit hinzufügen
Um `support-v4:19.1.0` zu verwenden, müssen Sie es als Abhängigkeit in Ihrem Projekt hinzufügen. Dies geschieht normalerweise in Ihrer `build.gradle`-Datei (Modul: app).

#### Für Gradle-basierte Projekte
1. Öffnen Sie Ihre `app/build.gradle`-Datei.
2. Fügen Sie die folgende Zeile dem `dependencies`-Block hinzu:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Synchronisieren Sie Ihr Projekt mit Gradle, indem Sie auf "Jetzt synchronisieren" in Android Studio klicken.

#### Hinweise:
- Stellen Sie sicher, dass Ihre `compileSdkVersion` auf mindestens 19 (Android 4.4 KitKat) oder höher eingestellt ist, da diese Bibliothek mit den Funktionen von API 19 übereinstimmt.
- Die von `support-v4:19.1.0` unterstützte Mindest-SDK-Version ist API 4 (Android 1.6), aber Sie sollten Ihre `minSdkVersion` basierend auf den Anforderungen Ihrer App einstellen.

Beispiel `build.gradle`:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // Nach Bedarf anpassen
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### Schritt 2: Verfügbarkeit überprüfen
Die Android Support Libraries werden im Google Maven Repository gehostet. Ab Android Studio 3.0+ ist dieses Repository standardmäßig enthalten. Wenn Sie eine ältere Version von Android Studio verwenden, stellen Sie sicher, dass Folgendes in Ihrer `build.gradle`-Datei (Projekt-Ebene) enthalten ist:

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // Hinweis: JCenter ist veraltet, wurde aber für ältere Bibliotheken verwendet
    }
}
```

Wenn Sie Probleme beim Herunterladen der Bibliothek haben, müssen Sie möglicherweise das Android Support Repository über den SDK-Manager installieren:
1. Gehen Sie zu `Tools > SDK Manager`.
2. Unter der Registerkarte "SDK-Tools" aktivieren Sie "Android Support Repository" und installieren Sie es.

---

### Schritt 3: Verwendung der Bibliothek in Ihrem Code
Die `support-v4`-Bibliothek stellt eine Vielzahl von Klassen bereit, wie z.B. `Fragment`, `Loader`, `AsyncTaskLoader` und Hilfsprogramme wie `ActivityCompat`. Hier sind Beispiele zur Verwendung einiger gängiger Komponenten:

#### Beispiel 1: Verwendung von Fragments
Die `support-v4`-Bibliothek enthält eine zurückportierte `Fragment`-Klasse, die auf älteren Android-Versionen funktioniert.

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

Um dieses Fragment in einer Aktivität zu verwenden:
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

#### Beispiel 2: Verwendung von ActivityCompat
Die `ActivityCompat`-Klasse stellt Hilfsmethoden für rückwärtskompatible Funktionen bereit, wie z.B. das Anfordern von Berechtigungen (eingeführt in API 23, aber mit der Support-Bibliothek früher verwendbar).

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

### Schritt 4: Überlegungen
- **Veraltete Bibliothek**: Die Android Support Library, einschließlich `support-v4:19.1.0`, ist veraltet. Für die moderne Entwicklung migrieren Sie zu AndroidX (z.B. `androidx.legacy:legacy-support-v4:1.0.0`). AndroidX ist der Nachfolger und bietet laufende Updates und Unterstützung.
- **Versionsabgleich**: Wenn Sie andere Support-Bibliotheken verwenden (z.B. `appcompat-v7`), stellen Sie sicher, dass sie dieselbe Version (19.1.0) haben, um Versionenkonflikte zu vermeiden.
- **Mindest-SDK**: Während `support-v4:19.1.0` API 4+ unterstützt, erfordern einige Funktionen möglicherweise eine höhere `minSdkVersion` (z.B. API 14 für bestimmte Komponenten, die später eingeführt wurden).

---

### Schritt 5: Migration zu AndroidX (optional, aber empfohlen)
Wenn Sie ein altes Projekt pflegen, sollten Sie eine Migration zu AndroidX in Betracht ziehen:
1. In Android Studio gehen Sie zu `Refactor > Migrate to AndroidX`.
2. Aktualisieren Sie Ihre Abhängigkeiten, z.B. ersetzen Sie `com.android.support:support-v4:19.1.0` durch `androidx.legacy:legacy-support-v4:1.0.0`.
3. Folgen Sie der von Android Studio bereitgestellten Migrationsanleitung.

---

### Fehlerbehebung
- **"Bibliothek nicht gefunden"**: Stellen Sie sicher, dass Ihre Internetverbindung aktiv ist und das Google Maven Repository zugänglich ist.
- **Versionskonflikt**: Wenn Sie Fehler über nicht übereinstimmende Support-Bibliotheksversionen sehen, passen Sie alle `com.android.support`-Abhängigkeiten an 19.1.0 an.
- **Veraltete Funktionen**: Einige APIs in `support-v4:19.1.0` (z.B. `AsyncTask`) sind veraltet. Überprüfen Sie die Dokumentation auf Alternativen.

Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Anwendungsfall oder einer bestimmten Einrichtung benötigen!