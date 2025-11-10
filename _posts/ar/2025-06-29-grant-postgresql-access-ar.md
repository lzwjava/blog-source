---
audio: false
generated: true
lang: ar
layout: post
title: منح صلاحية الوصول لقاعدة بيانات PostgreSQL
translated: true
type: note
---

لمنح مستخدم حق الوصول إلى قاعدة بيانات في PostgreSQL، تحتاج إلى اتباع هذه الخطوات. سأرشدك خلال العملية باستخدام أوامر SQL في واجهة سطر الأوامر psql.

الاتصال بـ PostgreSQL: لقد قمت بالفعل بالاتصال بـ PostgreSQL باستخدام مستخدم postgres، الذي يتمتع عادةً بامتيازات المستخدم المتفوق.

إنشاء مستخدم (إذا لم يكن موجودًا بالفعل): إذا لم يكن المستخدم موجودًا، يمكنك إنشاؤه باستخدام الأمر التالي. استبدل username و password باسم المستخدم وكلمة المرور المطلوبين.

```
CREATE USER username WITH PASSWORD 'password';
```

إنشاء قاعدة بيانات (إذا لم تكن موجودة بالفعل): إذا لم تكن قاعدة البيانات موجودة، يمكنك إنشاؤها باستخدام الأمر التالي. استبدل database_name باسم قاعدة البيانات المطلوب.

```
CREATE DATABASE database_name;
```

منح الصلاحيات على قاعدة البيانات: لمنح جميع الصلاحيات على قاعدة بيانات محددة للمستخدم، استخدم الأمر التالي. استبدل database_name و username بالأسماء المناسبة.

```
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

منح حق الاستخدام على مخطط Schema: إذا أردت أن يحصل المستخدم على حق الوصول إلى مخطط محدد داخل قاعدة البيانات، يمكنك منح حق الاستخدام على المخطط. استبدل schema_name و username بالأسماء المناسبة.

```
GRANT USAGE ON SCHEMA schema_name TO username;
```

منح الصلاحيات على الجداول: لمنح صلاحيات محددة على الجداول داخل مخطط، يمكنك استخدام الأمر التالي. استبدل schema_name و table_name و username بالأسماء المناسبة.

```
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;
```

جعل الصلاحيات سارية المفعول: إذا قمت بمنح صلاحيات على الجداول، قد تحتاج إلى تعيين الصلاحيات الافتراضية للجداول المستقبلية أيضًا.

```
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO username;
```

إليك مثالًا على كيف قد تبدو الأوامر:

```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\c mydatabase
GRANT USAGE ON SCHEMA public TO myuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

هذه الأوامر ستنشئ مستخدمًا مع حق وصول كامل إلى قاعدة بيانات محددة وجداولها. قم بتعديل الأوامر وفقًا لاحتياجاتك وسياسات الأمان المحددة.