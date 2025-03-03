audio: false
lang: en
layout: post
title: ButterKnife: a View binding Library
translated: false
generated: true

Butter Knife ist eine beliebte View-Binding-Bibliothek für Android, die den Prozess des Bindens von UI-Elementen an Felder in Ihrem Code vereinfacht. Beachten Sie jedoch, dass Butter Knife jetzt veraltet ist und die moderne Android-Entwicklung empfiehlt, View Binding (eingeführt in Android Jetpack) zu verwenden. Wenn Sie jedoch Butter Knife 6.1.0 (eine ältere Version, die etwa 2015 veröffentlicht wurde) mit einer `.jar`-Datei in einem Android-Projekt verwenden müssen, hier ist, wie Sie dies in Android Studio ab dem 03. März 2025 tun können.

### Voraussetzungen
- Installiertes Android Studio (jede aktuelle Version sollte funktionieren, obwohl der Prozess je nach Ihrer Version leicht unterschiedlich sein könnte).
- Ein grundlegendes Android-Projekt eingerichtet.
- Die `butterknife-6.1.0.jar`-Datei heruntergeladen. Sie können ältere Versionen normalerweise in Repositories wie Maven Central oder durch archivierte Quellen finden, wenn Sie die `.jar`-Datei lokal haben.

### Schritte zur Verwendung von `butterknife-6.1.0.jar` in der Android-Entwicklung

#### Schritt 1: Fügen Sie die `.jar`-Datei zu Ihrem Projekt hinzu
1. **Navigieren Sie zum `libs`-Ordner**:
   - In Ihrem Android Studio-Projekt navigieren Sie zum `app`-Modul.
   - Im `app`-Ordner finden oder erstellen Sie einen Ordner mit dem Namen `libs`. Wenn er nicht existiert, klicken Sie mit der rechten Maustaste auf den `app`-Ordner, wählen Sie `New > Directory` und benennen Sie ihn `libs`.

2. **Kopieren Sie die `.jar`-Datei**:
   - Kopieren Sie die `butterknife-6.1.0.jar`-Datei in den `libs`-Ordner. Dies können Sie tun, indem Sie die Datei in den `libs`-Ordner in Android Studio ziehen und ablegen oder sie manuell über Ihren Datei-Explorer dort platzieren.

3. **Synchronisieren Sie die `.jar`-Datei mit Gradle**:
   - Öffnen Sie die `build.gradle`-Datei für das `app`-Modul (unter `app/build.gradle`).
   - Fügen Sie die folgende Zeile unter dem `dependencies`-Block hinzu, um alle `.jar`-Dateien im `libs`-Ordner zu enthalten:
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - Synchronisieren Sie Ihr Projekt, indem Sie auf die Schaltfläche "Sync Project with Gradle Files" in Android Studio klicken.

#### Schritt 2: Konfigurieren Sie Ihr Projekt
Da Butter Knife 6.1.0 Annotationsverarbeitung verwendet, benötigen Sie keine Annotationsprozessor-Abhängigkeit für diese spezifische Version (im Gegensatz zu späteren Versionen wie 8.x und höher). Die `.jar`-Datei enthält die Laufzeitbibliothek, und Butter Knife 6.1.0 verwendet Laufzeitreflexion anstelle von Codegenerierung zur Kompilierzeit für den Großteil seiner Funktionalität.

Stellen Sie jedoch sicher, dass Ihr Projekt so eingerichtet ist, dass es Java-Anmerkungen unterstützt:
- In Ihrer `app/build.gradle` stellen Sie sicher, dass die Java-Version kompatibel ist (Butter Knife 6.1.0 funktioniert mit Java 6+):
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### Schritt 3: Verwenden Sie Butter Knife in Ihrem Code
1. **Fügen Sie Butter Knife-Anmerkungen hinzu**:
   - In Ihrer Aktivität oder Ihrem Fragment importieren Sie Butter Knife und versehen Sie Ihre Ansichten mit `@InjectView` (die in Version 6.1.0 verwendete Anmerkung). Zum Beispiel:
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
             ButterKnife.inject(this); // Ansichten binden

             // Beispielverwendung
             myButton.setOnClickListener(v -> myText.setText("Button geklickt!"));
         }
     }
     ```

2. **XML-Layout**:
   - Stellen Sie sicher, dass Ihre Layout-Datei (z. B. `res/layout/activity_main.xml`) die Ansichten mit den entsprechenden IDs enthält:
     ```xml
     <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         android:orientation="vertical">

         <TextView
             android:id="@+id/my_text"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Hello World" />

         <Button
             android:id="@+id/my_button"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Klicken Sie mich" />
     </LinearLayout>
     ```

3. **Binden Sie Ansichten**:
   - Der `ButterKnife.inject(this)`-Aufruf in `onCreate` bindet die annotierten Felder an die Ansichten aus dem Layout. Beachten Sie, dass in Version 6.1.0 `inject` anstelle von `bind` verwendet wird (das in späteren Versionen wie 7.x und 8.x eingeführt wurde).

#### Schritt 4: Führen Sie Ihr Projekt aus
- Bauen und führen Sie Ihr Projekt aus. Wenn alles korrekt eingerichtet ist, bindet Butter Knife Ihre Ansichten und Sie sollten die UI wie erwartet funktionieren sehen.

### Wichtige Hinweise
- **Versionsbeschränkung**: Butter Knife 6.1.0 ist ziemlich alt (veröffentlicht 2015) und verfügt nicht über Funktionen, die in späteren Versionen eingeführt wurden, wie z. B. Codegenerierung zur Kompilierzeit (über Annotationsprozessoren) und Unterstützung für `@BindView` anstelle von `@InjectView`. Es verwendet Laufzeitreflexion, was die Leistung im Vergleich zu modernen Alternativen leicht beeinträchtigen könnte.
- **Veralteter Status**: Butter Knife wird nicht mehr gepflegt (die Entwicklung wurde etwa 2020 eingestellt) und die offizielle Empfehlung lautet, View Binding oder Jetpack Compose für neue Projekte zu verwenden.
- **Alternative Einrichtung**: Wenn Sie eine neuere Version (z. B. 10.2.3) verwenden würden, müssten Sie eine Annotationsprozessor-Abhängigkeit hinzufügen (z. B. `annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`), aber für 6.1.0 mit einer `.jar`-Datei ist dies nicht erforderlich.
- **Fehlerbehebung**:
  - Wenn Sie einen Fehler "cannot resolve symbol" für Butter Knife-Klassen erhalten, stellen Sie sicher, dass die `.jar`-Datei korrekt zum `libs`-Ordner hinzugefügt und in den Gradle-Abhängigkeiten enthalten ist.
  - Wenn die App mit einem `NoClassDefFoundError` abstürzt, überprüfen Sie doppelt, dass die `.jar`-Datei im `libs`-Ordner ist und das Projekt synchronisiert wurde.

### Empfehlung
Obwohl diese Anleitung zeigt, wie Sie `butterknife-6.1.0.jar` verwenden, überlegen Sie, auf View Binding umzusteigen, um eine modernere, unterstützte Methode zu verwenden. Hier ist ein schneller Vergleich:
- **Butter Knife 6.1.0**: Verwendet `@InjectView`, Laufzeitreflexion, manuelle `.jar`-Integration.
- **View Binding**: In Android integriert, keine externen Abhängigkeiten, generiert Binding-Klassen zur Kompilierzeit und ist null-sicher.

Möchten Sie eine Anleitung zum Übergang zu View Binding?