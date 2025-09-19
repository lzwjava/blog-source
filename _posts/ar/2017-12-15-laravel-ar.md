---
audio: false
generated: false
image: false
lang: ar
layout: post
title: استخدام لارافيل
translated: true
---

إذا كنت تغمق في تطوير الويب وتريد إطارًا قويًا وسهل التعلم، فLaravel هو الخيار المناسب لك. إنه إطار PHP قد استحوذ على عالم المطورين بفضل نصوصه الجذابة، وميزاته القوية، ومجتمع يدعمك. في هذا المدون، سأرشدك عبر الخطوات الأساسية لبدء العمل مع Laravel وسأريك لماذا يستحق وقتك.

#### الخطوة 1: إعداد بيئتك
قبل أن تبدأ في بناء مع Laravel، تحتاج إلى الأدوات المناسبة. إليك ما تحتاج إليه:
- **PHP**: الإصدار 8.1 أو أعلى (Laravel يتطور بسرعة، لذا احرص على تحديثك!).
- **Composer**: هذا مدير الاعتماديات PHP. قم بتنزيله من [getcomposer.org](https://getcomposer.org/).
- **خادم محلي**: مثل XAMPP، WAMP، أو خادم Laravel المدمج يعمل بشكل رائع.
- **Terminal**: ستقوم بتشغيل الأوامر، لذا كن مرتاحًا مع سطر الأوامر الخاص بك.

بعد أن حصلت على هذه الأدوات، افتح Terminal وقلب Laravel على مستوى العالم من خلال تشغيل:
```
composer global require laravel/installer
```
هذا يسمح لك بإنشاء مشاريع Laravel جديدة بأمر واحد.

#### الخطوة 2: إنشاء مشروع Laravel الأول
هل أنت مستعد لإنشاء شيء؟ في Terminal، انتقل إلى المجلد الذي تريد أن يكون فيه مشروعك (مثل `cd /path/to/your/folder`), واكتب:
```
laravel new my-first-app
```
بعد بضع دقائق، سيقوم Composer بإعداد مشروع Laravel جديد يسمى `my-first-app`. انتقل إليه:
```
cd my-first-app
```
ليراه في العمل، ابدأ خادم Laravel المدمج:
```
php artisan serve
```
افتح متصفحك واذهب إلى `http://localhost:8000`. Boom—أنت تملك صفحة ترحيب! هذا Laravel يقول مرحبًا.

#### الخطوة 3: فهم الأساسيات
Laravel يتبع بنية MVC (Model-View-Controller)، التي تظل كودك نظيفًا ومتنظمًا:
- **Models**: تتعامل مع بياناتك (فكر في جداول قاعدة البيانات).
- **Views**: هو الجزء الأمامي الذي يراه المستخدمون (HTML، CSS، إلخ).
- **Controllers**: هو اللاصق الذي يربط Models وViews.

ستجد هذه في مجلد `app/`. على سبيل المثال، controllers تعيش في `app/Http/Controllers`، وviews في `resources/views`.

#### الخطوة 4: بناء صفحة بسيطة
دعونا نخلق صفحة "Hello, World" سريعة. افتح `routes/web.php`—هذا هو المكان الذي تحدد فيه URLs لمتجرك. أضف هذا السطر:
```php
Route::get('/hello', function () {
    return view('hello');
});
```
الآن، انشئ ملفًا باسم `hello.blade.php` في `resources/views`. أضف هذا:
```html
<!DOCTYPE html>
<html>
<head>
    <title>مرحبًا، Laravel</title>
</head>
<body>
    <h1>مرحبًا، عالم!</h1>
</body>
</html>
```
أعد تشغيل الخادم (أو احتفظ به يعمل)، ثم اذهب إلى `http://localhost:8000/hello`. ستشاهد صفحة "Hello, World!" الخاصة بك. امتداد `.blade.php` يعني أنك تستخدم محرك قالب Blade الخاص بـ Laravel—مفيد جدًا للمحتوى الديناميكي.

#### الخطوة 5: لعب مع قاعدة البيانات
Laravel يجعل العمل مع قاعدة البيانات سهلًا مع ORM الخاص بها (Object-Relational Mapping). أولاً، قم بإعداد قاعدة البيانات في ملف `.env` (مثل MySQL، SQLite):
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
```
إنشئ هجرة لإنشاء جدول. قم بتشغيل:
```
php artisan make:migration create_posts_table
```
في الملف الجديد تحت `database/migrations`، حدد جدولك:
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
قم بتشغيل الهجرة:
```
php artisan migrate
```
الآن لديك جدول `posts`! يمكنك إنشاء نموذج `Post` مع:
```
php artisan make:model Post
```
هذا يربط جدولك بنموذج يمكنك استخدامه في كودك.

#### الخطوة 6: استمر في الاستكشاف
لدي Laravel الكثير أكثر من تقديمه—التسجيل، الواسطات، التوجيه، والأكواد عبر Composer. هل تريد تسجيل المستخدم؟ قم بتشغيل:
```
php artisan make:auth
```
هل تحتاج إلى تعزيز الأمامي؟ استخدم Laravel Breeze أو Jetstream. [التوثيق الرسمي](https://laravel.com/docs) هو صديقك الأفضل هنا.

#### لماذا استخدام Laravel؟
هو سريع، آمن، ويوفر لك من إعادة اختراع العجلة. سواء كنت تبني مدونة، موقع تجاري إلكتروني، أو API، أدوات Laravel—مثل أوامر artisan، قوالب Blade، وEloquent—تجعل الحياة أسهل.

فما الذي تنتظره؟ ابدأ صغيرًا، تجريب، وسوف تكون قريبًا من إنشاء تطبيقات الويب مثل محترف. سعيد الترميز!