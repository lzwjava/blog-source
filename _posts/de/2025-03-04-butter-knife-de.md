---
audio: false
generated: true
lang: de
layout: post
title: Verwendung Von Butterknife Zur View-Bindung
translated: true
type: note
---

Butter Knife ist eine beliebte View-Binding-Bibliothek für Android, die den Prozess des Bindens von UI-Elementen an Felder in Ihrem Code vereinfacht. Beachten Sie jedoch, dass Butter Knife inzwischen veraltet ist und die moderne Android-Entwicklung die Verwendung von View Binding (eingeführt in Android Jetpack) empfiehlt. Falls Sie dennoch Butter Knife 6.1.0 (eine ältere Version aus circa 2015) mit einer `.jar`-Datei in einem Android-Projekt verwenden müssen, finden Sie hier die Vorgehensweise in Android Studio, Stand 03. März 2025.

### Voraussetzungen
- Android Studio installiert (jede aktuelle Version sollte funktionieren, obwohl der Prozess je nach Version leicht abweichen kann).
- Ein grundlegendes Android-Projekt eingerichtet.
- Die `butterknife-6.1.0.jar`-Datei heruntergeladen. Ältere Versionen finden Sie typischerweise in Repositories wie Maven Central oder über archivierte Quellen, falls Sie die `.jar`-Datei lokal haben.

### Schritte zur Verwendung von `butterknife-6.1.0.jar` in der Android-Entwicklung

#### Schritt 1: Fügen Sie die `.jar`-Datei zu Ihrem Projekt hinzu
1. **Suchen Sie den `libs`-Ordner**:
   - Navigieren Sie in Ihrem Android Studio-Projekt zum `app`-Modul.
   - Suchen Sie innerhalb des `app`-Ordners nach einem Ordner namens `libs` oder erstellen Sie ihn. Falls er nicht existiert, klicken Sie mit der rechten Maustaste auf den `app`-Ordner, wählen Sie `New > Directory` und nennen Sie ihn `libs`.

2. **Kopieren Sie die `.jar`-Datei**:
   - Kopieren Sie die `butterknife-6.1.0.jar`-Datei in den `libs`-Ordner. Sie können dies tun, indem Sie die Datei per Drag & Drop in den `libs`-Ordner in Android Studio ziehen oder sie manuell über Ihren Datei-Explorer dort ablegen.

3. **Synchronisieren Sie die `.jar`-Datei mit Gradle**:
   - Öffnen Sie die `build.gradle`-Datei für das `app`-Modul (befindet sich unter `app/build.gradle`).
   - Fügen Sie die folgende Zeile unter dem `dependencies`-Block hinzu, um alle `.jar`-Dateien im `libs`-Ordner einzubinden:
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - Synchronisieren Sie Ihr Projekt, indem Sie auf den Button "Sync Project with Gradle Files" in Android Studio klicken.

#### Schritt 2: Konfigurieren Sie Ihr Projekt
Da Butter Knife 6.1.0 Annotation Processing verwendet, benötigen Sie für diese spezifische Version (im Gegensatz zu späteren Versionen wie 8.x und höher) keine Annotation Processor-Abhängigkeit. Die `.jar`-Datei enthält die Runtime-Bibliothek, und Butter Knife 6.1.0 verlässt sich für den Großteil seiner Funktionalität auf Runtime-Reflection anstatt auf Compile-Time-Code-Generierung.

Stellen Sie jedoch sicher, dass Ihr Projekt für die Unterstützung von Java-Annotationen eingerichtet ist:
- Stellen Sie in Ihrer `app/build.gradle`-Datei sicher, dass die Java-Version kompatibel ist (Butter Knife 6.1.0 funktioniert mit Java 6+):
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### Schritt 3: Verwenden Sie Butter Knife in Ihrem Code
1. **Fügen Sie Butter Knife-Annotationen hinzu**:
   - Importieren Sie in Ihrer Activity oder Fragment Butter Knife und annotieren Sie Ihre Views mit `@InjectView` (die in Version 6.1.0 verwendete Annotation). Zum Beispiel:
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
             ButterKnife.inject(this); // Bind views

             // Beispielverwendung
             myButton.setOnClickListener(v -> myText.setText("Button clicked!"));
         }
     }
     ```

2. **XML-Layout**:
   - Stellen Sie sicher, dass Ihre Layout-Datei (z.B. `res/layout/activity_main.xml`) die Views mit den entsprechenden IDs enthält:
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
             android:text="Click Me" />
     </LinearLayout>
     ```

3. **Binden Sie die Views**:
   - Der Aufruf `ButterKnife.inject(this)` in `onCreate` bindet die annotierten Felder an die Views aus dem Layout. Beachten Sie, dass in Version 6.1.0 `inject` anstelle von `bind` verwendet wird (welches in späteren Versionen wie 7.x und 8.x eingeführt wurde).

#### Schritt 4: Führen Sie Ihr Projekt aus
- Bauen Sie Ihr Projekt und führen Sie es aus. Wenn alles korrekt eingerichtet ist, wird Butter Knife Ihre Views binden und Sie sollten die Benutzeroberfläche wie erwartet funktionieren sehen.

### Wichtige Hinweise
- **Versionsbeschränkung**: Butter Knife 6.1.0 ist sehr alt (veröffentlicht 2015) und verfügt nicht über Funktionen, die in späteren Versionen eingeführt wurden, wie z.B. Compile-Time-Code-Generierung (über Annotation Processor) und Unterstützung für `@BindView` anstelle von `@InjectView`. Es verwendet Reflection zur Laufzeit, was die Leistung im Vergleich zu modernen Alternativen leicht beeinträchtigen kann.
- **Veralteter Status**: Butter Knife wird nicht mehr gepflegt (die Entwicklung wurde circa 2020 eingestellt), und die offizielle Empfehlung ist, View Binding oder Jetpack Compose für neue Projekte zu verwenden.
- **Alternative Einrichtung**: Wenn Sie eine neuere Version (z.B. 10.2.3) verwenden würden, müssten Sie eine Annotation Processor-Abhängigkeit hinzufügen (z.B. `annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`), aber für 6.1.0 mit einer `.jar`-Datei ist dies nicht erforderlich.
- **Fehlerbehebung**:
  - Wenn Sie einen "cannot resolve symbol"-Fehler für Butter Knife-Klassen erhalten, stellen Sie sicher, dass die `.jar`-Datei korrekt zum `libs`-Ordner hinzugefügt und in den Gradle-Abhängigkeiten enthalten ist.
  - Wenn die App mit einem `NoClassDefFoundError` abstürzt, überprüfen Sie erneut, ob die `.jar`-Datei im `libs`-Ordner ist und das Projekt synchronisiert wurde.

### Empfehlung
Während diese Anleitung zeigt, wie Sie `butterknife-6.1.0.jar` verwenden können, sollten Sie in Betracht ziehen, auf View Binding zu migrieren, für einen moderneren, unterstützten Ansatz. Hier ist ein kurzer Vergleich:
- **Butter Knife 6.1.0**: Verwendet `@InjectView`, Runtime-Reflection, manuelle `.jar`-Integration.
- **View Binding**: In Android integriert, keine externen Abhängigkeiten, generiert Binding-Klassen zur Compile-Zeit und ist null-sicher.

Möchten Sie stattdessen eine Anleitung zum Umstieg auf View Binding?