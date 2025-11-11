---
audio: false
generated: true
lang: de
layout: post
title: Android-Unterstützungsbibliothek
translated: true
type: note
---

Die Android Support Library Version `support-v4:19.1.0` ist eine ältere Version der Android Support Library (speziell die v4-Kompatibilitätsbibliothek), die abwärtskompatible APIs für Android-Geräte bereitstellt, die mit API-Levels unterhalb der zum Zeitpunkt ihrer Veröffentlichung (ca. 2014) neuesten Versionen laufen. Diese Bibliothek ermöglicht es Ihnen, Funktionen, die in neueren Android-Versionen eingeführt wurden, auf älteren Geräten zu verwenden, wie z.B. Fragments, Loader und andere Hilfsprogramme.

Da `support-v4:19.1.0` Teil der veralteten Android Support Library ist, wurde sie von AndroidX-Bibliotheken abgelöst. Wenn Sie jedoch diese spezielle Version verwenden müssen (z.B. zur Wartung eines älteren Projekts), finden Sie hier, wie Sie sie in Ihrem Android-Projekt einrichten und verwenden können:

---

### Schritt 1: Abhängigkeit hinzufügen
Um `support-v4:19.1.0` zu verwenden, müssen Sie sie als Abhängigkeit in Ihr Projekt aufnehmen. Dies geschieht typischerweise in Ihrer `build.gradle`-Datei (Module: app).

#### Für Gradle-basierte Projekte
1. Öffnen Sie Ihre `app/build.gradle`-Datei.
2. Fügen Sie die folgende Zeile zum `dependencies`-Block hinzu:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Synchronisieren Sie Ihr Projekt mit Gradle, indem Sie in Android Studio auf "Jetzt synchronisieren" klicken.

#### Hinweise:
- Stellen Sie sicher, dass Ihre `compileSdkVersion` auf mindestens 19 (Android 4.4 KitKat) oder höher gesetzt ist, da diese Bibliothek auf API-19-Funktionen ausgerichtet ist.
- Die minimale SDK-Version, die von `support-v4:19.1.0` unterstützt wird, ist API 4 (Android 1.6), aber Sie sollten Ihre `minSdkVersion` basierend auf den Anforderungen Ihrer App festlegen.

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
Die Android Support Libraries werden im Google Maven Repository gehostet. Ab Android Studio 3.0+ ist dieses Repository standardmäßig enthalten. Wenn Sie eine ältere Version von Android Studio verwenden, stellen Sie sicher, dass Folgendes in Ihrer `build.gradle` (Projektebene) enthalten ist:

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
2. Überprüfen Sie unter dem Tab "SDK Tools" "Android Support Repository" und installieren Sie es.

---

### Schritt 3: Verwendung der Bibliothek in Ihrem Code
Die `support-v4`-Bibliothek bietet eine Vielzahl von Klassen, wie z.B. `Fragment`, `Loader`, `AsyncTaskLoader` und Hilfsprogramme wie `ActivityCompat`. Im Folgenden finden Sie Beispiele für die Verwendung einiger gängiger Komponenten:

#### Beispiel 1: Verwenden von Fragments
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

Um dieses Fragment in einer Activity zu verwenden:
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

#### Beispiel 2: Verwenden von ActivityCompat
Die `ActivityCompat`-Klasse bietet Hilfsmethoden für abwärtskompatible Funktionen, wie z.B. das Anfordern von Berechtigungen (eingeführt in API 23, aber mit der Support Library auch früher nutzbar).

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
- **Veraltete Bibliothek**: Die Android Support Library, einschließlich `support-v4:19.1.0`, ist veraltet. Für die moderne Entwicklung migrieren Sie bitte zu AndroidX (z.B. `androidx.legacy:legacy-support-v4:1.0.0`). AndroidX ist der Nachfolger und bietet laufende Updates und Support.
- **Versionsabgleich**: Wenn Sie andere Support-Bibliotheken verwenden (z.B. `appcompat-v7`), stellen Sie sicher, dass diese die gleiche Version (19.1.0) haben, um Versionskonfliktfehler zu vermeiden.
- **Minimale SDK**: Während `support-v4:19.1.0` API 4+ unterstützt, erfordern einige Funktionen möglicherweise eine höhere `minSdkVersion` (z.B. API 14 für bestimmte später eingeführte Komponenten).

---

### Schritt 5: Migration zu AndroidX (Optional, aber empfohlen)
Wenn Sie ein altes Projekt warten, sollten Sie eine Migration zu AndroidX in Betracht ziehen:
1. Gehen Sie in Android Studio zu `Refactor > Migrate to AndroidX`.
2. Aktualisieren Sie Ihre Abhängigkeiten, ersetzen Sie z.B. `com.android.support:support-v4:19.1.0` durch `androidx.legacy:legacy-support-v4:1.0.0`.
3. Befolgen Sie den Migrationsleitfaden von Android Studio.

---

### Problembehandlung
- **"Could not find library"**: Stellen Sie sicher, dass Ihre Internetverbindung aktiv ist und das Google Maven Repository erreichbar ist.
- **Versionskonflikt**: Wenn Sie Fehler wegen nicht übereinstimmender Support-Bibliotheksversionen sehen, passen Sie alle `com.android.support`-Abhängigkeiten auf 19.1.0 an.
- **Veraltete Features**: Einige APIs in `support-v4:19.1.0` (z.B. `AsyncTask`) sind veraltet. Überprüfen Sie die Dokumentation auf Alternativen.

Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Anwendungsfall oder Setup benötigen!