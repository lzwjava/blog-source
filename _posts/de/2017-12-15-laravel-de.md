---
audio: false
generated: false
image: false
lang: de
layout: post
title: Laravel verwenden
translated: true
type: post
---

Wenn du dich in die Webentwicklung stürzt und einen Framework suchst, der mächtig und dennoch leicht zu erlernen ist, ist Laravel deine erste Wahl. Es ist ein PHP-Framework, das die Entwicklerwelt im Sturm erobert hat, dank seiner eleganten Syntax, robusten Funktionen und einer Community, die dir den Rücken stärkt. In diesem Blog werde ich dich durch die Grundlagen des Einstiegs in Laravel führen und dir zeigen, warum es sich lohnt.

#### Schritt 1: Einrichten deiner Umgebung
Bevor du mit Laravel loslegen kannst, benötigst du die richtigen Werkzeuge. Hier ist, was du benötigst:
- **PHP**: Version 8.1 oder höher (Laravel entwickelt sich schnell, also bleibe auf dem neuesten Stand!).
- **Composer**: Dies ist ein Abhängigkeitsmanager für PHP. Lade es von [getcomposer.org](https://getcomposer.org/) herunter.
- **Ein lokaler Server**: Etwas wie XAMPP, WAMP oder der eingebaute Server von Laravel funktioniert großartig.
- **Ein Terminal**: Du wirst Befehle ausführen, also werde mit deiner Kommandozeile vertraut.

Sobald du diese hast, öffne dein Terminal und installiere Laravel global, indem du folgendes ausführst:
```
composer global require laravel/installer
```
Dies ermöglicht es dir, neue Laravel-Projekte mit einem einzigen Befehl zu erstellen.

#### Schritt 2: Erstelle dein erstes Laravel-Projekt
Bereit, etwas zu bauen? In deinem Terminal navigierst du zu dem Ordner, in dem dein Projekt liegen soll (z.B. `cd /pfad/zu/deinem/ordner`), und gibst folgendes ein:
```
laravel new meine-erste-app
```
Nach ein paar Minuten wird Composer ein frisches Laravel-Projekt namens `meine-erste-app` einrichten. Navigiere hinein:
```
cd meine-erste-app
```
Um es in Aktion zu sehen, starte den eingebauten Server von Laravel:
```
php artisan serve
```
Öffne deinen Browser und gehe zu `http://localhost:8000`. Boom—du hast eine Willkommensseite! Das ist Laravel, das hallo sagt.

#### Schritt 3: Grundlagen verstehen
Laravel folgt einer MVC-Struktur (Model-View-Controller), die deinen Code sauber und organisiert hält:
- **Models**: Diese handhaben deine Daten (denke an Datenbanktabellen).
- **Views**: Das Frontend, was die Benutzer sehen (HTML, CSS usw.).
- **Controllers**: Der Klebstoff, der Models und Views verbindet.

Du findest diese im `app/` Ordner. Zum Beispiel leben die Controller in `app/Http/Controllers` und die Views in `resources/views`.

#### Schritt 4: Erstelle eine einfache Seite
Lass uns eine schnelle „Hello, World“ Seite erstellen. Öffne `routes/web.php`—hier definierst du die URLs deiner App. Füge diese Zeile hinzu:
```php
Route::get('/hello', function () {
    return view('hello');
});
```
Erstelle nun eine Datei namens `hello.blade.php` in `resources/views`. Füge dies hinzu:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hallo, Laravel</title>
</head>
<body>
    <h1>Hallo, Welt!</h1>
</body>
</html>
```
Starte deinen Server neu (oder lasse ihn laufen), dann besuche `http://localhost:8000/hello`. Du wirst deine „Hello, World!“ Seite sehen. Die `.blade.php` Erweiterung bedeutet, dass du die Blade-Templating-Engine von Laravel verwendest—sehr nützlich für dynamischen Inhalt.

#### Schritt 5: Mit der Datenbank spielen
Laravel macht die Datenbankarbeit mit seinem Eloquent ORM (Object-Relational Mapping) zum Kinderspiel. Zuerst richte deine Datenbank in der `.env` Datei ein (z.B. MySQL, SQLite):
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=deine_datenbank_name
DB_USERNAME=dein_benutzername
DB_PASSWORD=dein_passwort
```
Erstelle eine Migration, um eine Tabelle einzurichten. Führe dies aus:
```
php artisan make:migration create_posts_table
```
In der neuen Datei unter `database/migrations` definierst du deine Tabelle:
```php
public function up()
{
    Schema::create('posts', function (Blueprint $table) {
        $table->id();
        $table->string('title');
        $table->text('body');
        $table->timestamps();
    });
}
```
Führe die Migration aus:
```
php artisan migrate
```
Jetzt hast du eine `posts` Tabelle! Du kannst ein `Post` Modell mit folgendem erstellen:
```
php artisan make:model Post
```
Dies bindet deine Tabelle an ein Modell, das du in deinem Code verwenden kannst.

#### Schritt 6: Weiter erkunden
Laravel hat noch viel mehr zu bieten—Authentifizierung, Middleware, Routing und Pakete über Composer. Möchtest du eine Benutzeranmeldung? Führe dies aus:
```
php artisan make:auth
```
Brauchst du einen Frontend-Boost? Verwende Laravel Breeze oder Jetstream. Die [offiziellen Dokumentationen](https://laravel.com/docs) sind hier dein bester Freund.

#### Warum Laravel verwenden?
Es ist schnell, sicher und spart dir das Rad neu zu erfinden. Egal, ob du einen Blog, eine E-Commerce-Seite oder eine API baust, die Tools von Laravel—wie Artisan-Befehle, Blade-Templates und Eloquent—machen das Leben leichter.

Also, worauf wartest du noch? Fange klein an, experimentiere und bald wirst du Web-Apps wie ein erfahrener Profi erstellen. Viel Spaß beim Codieren!