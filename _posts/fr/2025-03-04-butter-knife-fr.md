---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de ButterKnife pour la liaison de vues
translated: true
type: note
---

Butter Knife est une bibliothèque populaire de liaison de vues pour Android qui simplifie le processus de liaison des éléments d'interface utilisateur aux champs de votre code. Cependant, veuillez noter que Butter Knife est maintenant dépréciée, et le développement Android moderne recommande d'utiliser View Binding (introduit dans Android Jetpack) à la place. Néanmoins, si vous devez utiliser Butter Knife 6.1.0 (une ancienne version publiée vers 2015) avec un fichier `.jar` dans un projet Android, voici comment procéder dans Android Studio en date du 03 mars 2025.

### Prérequis
- Android Studio installé (toute version récente devrait fonctionner, bien que le processus puisse différer légèrement selon votre version).
- Un projet Android de base configuré.
- Le fichier `butterknife-6.1.0.jar` téléchargé. Vous pouvez généralement trouver les anciennes versions sur des dépôts comme Maven Central ou via des sources archivées si vous avez le fichier `.jar` localement.

### Étapes pour utiliser `butterknife-6.1.0.jar` dans le développement Android

#### Étape 1 : Ajouter le fichier `.jar` à votre projet
1. **Localiser le dossier `libs`** :
   - Dans votre projet Android Studio, naviguez jusqu'au module `app`.
   - À l'intérieur du dossier `app`, trouvez ou créez un dossier nommé `libs`. S'il n'existe pas, faites un clic droit sur le dossier `app`, sélectionnez `New > Directory`, et nommez-le `libs`.

2. **Copier le fichier `.jar`** :
   - Copiez le fichier `butterknife-6.1.0.jar` dans le dossier `libs`. Vous pouvez le faire en glissant-déposant le fichier dans le dossier `libs` dans Android Studio ou en le plaçant manuellement via votre explorateur de fichiers.

3. **Synchroniser le fichier `.jar` avec Gradle** :
   - Ouvrez le fichier `build.gradle` pour le module `app` (situé à `app/build.gradle`).
   - Ajoutez la ligne suivante dans le bloc `dependencies` pour inclure tous les fichiers `.jar` du dossier `libs` :
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - Synchronisez votre projet en cliquant sur le bouton "Sync Project with Gradle Files" dans Android Studio.

#### Étape 2 : Configurer votre projet
Étant donné que Butter Knife 6.1.0 utilise le traitement des annotations, vous n'avez pas besoin d'une dépendance de processeur d'annotations pour cette version spécifique (contrairement aux versions ultérieures comme 8.x et plus). Le fichier `.jar` inclut la bibliothèque d'exécution, et Butter Knife 6.1.0 repose sur la réflexion à l'exécution plutôt que sur la génération de code à la compilation pour la plupart de ses fonctionnalités.

Cependant, assurez-vous que votre projet est configuré pour prendre en charge les annotations Java :
- Dans votre `app/build.gradle`, assurez-vous que la version Java est compatible (Butter Knife 6.1.0 fonctionne avec Java 6+) :
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### Étape 3 : Utiliser Butter Knife dans votre code
1. **Ajouter les annotations Butter Knife** :
   - Dans votre Activity ou Fragment, importez Butter Knife et annotez vos vues avec `@InjectView` (l'annotation utilisée dans la version 6.1.0). Par exemple :
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
             ButterKnife.inject(this); // Lie les vues

             // Exemple d'utilisation
             myButton.setOnClickListener(v -> myText.setText("Bouton cliqué !"));
         }
     }
     ```

2. **Layout XML** :
   - Assurez-vous que votre fichier de layout (par exemple, `res/layout/activity_main.xml`) contient les vues avec les ID correspondants :
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
             android:text="Cliquez Ici" />
     </LinearLayout>
     ```

3. **Lier les vues** :
   - L'appel `ButterKnife.inject(this)` dans `onCreate` lie les champs annotés aux vues du layout. Notez que dans la version 6.1.0, `inject` est utilisé au lieu de `bind` (qui a été introduit dans les versions ultérieures comme 7.x et 8.x).

#### Étape 4 : Exécuter votre projet
- Construisez et exécutez votre projet. Si tout est configuré correctement, Butter Knife liera vos vues et vous devriez voir l'interface utilisateur fonctionner comme prévu.

### Notes importantes
- **Limitation de version** : Butter Knife 6.1.0 est assez ancienne (publiée en 2015) et manque des fonctionnalités introduites dans les versions ultérieures, telles que la génération de code à la compilation (via des processeurs d'annotations) et la prise en charge de `@BindView` au lieu de `@InjectView`. Elle utilise la réflexion à l'exécution, ce qui peut légèrement impacter les performances par rapport aux alternatives modernes.
- **Statut déprécié** : Butter Knife n'est plus maintenue (le développement s'est arrêté vers 2020), et la recommandation officielle est d'utiliser View Binding ou Jetpack Compose pour les nouveaux projets.
- **Configuration alternative** : Si vous utilisiez une version plus récente (par exemple, 10.2.3), vous auriez besoin d'ajouter une dépendance de processeur d'annotations (par exemple, `annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`), mais pour la version 6.1.0 avec un fichier `.jar`, ce n'est pas requis.
- **Dépannage** :
  - Si vous obtenez une erreur "cannot resolve symbol" pour les classes Butter Knife, assurez-vous que le fichier `.jar` est correctement ajouté au dossier `libs` et inclus dans les dépendances Gradle.
  - Si l'application plante avec une `NoClassDefFoundError`, vérifiez que le fichier `.jar` est dans le dossier `libs` et que le projet a été synchronisé.

### Recommandation
Bien que ce guide vous montre comment utiliser `butterknife-6.1.0.jar`, envisagez de migrer vers View Binding pour une approche plus moderne et prise en charge. Voici une comparaison rapide :
- **Butter Knife 6.1.0** : Utilise `@InjectView`, réflexion à l'exécution, intégration manuelle du `.jar`.
- **View Binding** : Intégré à Android, aucune dépendance externe, génère des classes de liaison à la compilation et est null-safe.

Souhaitez-vous des conseils pour passer à View Binding à la place ?