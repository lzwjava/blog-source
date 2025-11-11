---
audio: false
generated: true
lang: ar
layout: post
title: 'الإخراج المُفصَّل: أمثلة'
translated: true
type: note
---

إليك أمثلة إضافية لتمكين الإخراج المفصل عبر مختلف الأدوات والأنظمة، توسيعًا لموضوع تقديم ملاحظات أو تسجيل أكثر تفصيلاً:

- **PowerShell**: لتمكين الإخراج المفصل، استخدم مفتاح `-Verbose` مع cmdlets التي تدعمه. على سبيل المثال:
  ```powershell
  Get-Process -Verbose
  ```
  بدلاً من ذلك، عيّن متغير `$VerbosePreference` بشكل عام:
  ```powershell
  $VerbosePreference = "Continue"
  ```

- **CMake**: للحصول على إخراج مفصل أثناء عملية البناء، استخدم علم `--verbose` أو عيّن `VERBOSE=1`:
  ```bash
  cmake --build . --verbose
  ```
  أو:
  ```bash
  make VERBOSE=1
  ```

- **Make**: لتمكين الإخراج المفصل ورؤية جميع الأوامر المنفذة، استخدم علم `-d` لتصحيح الأخطاء أو تجنب كتم الإخراج باستخدام `@`:
  ```bash
  make -d
  ```
  أو قم بتحرير ملف Makefile لإزالة بادئات `@` من الأوامر.

- **GCC (GNU Compiler Collection)**: للحصول على إخراج مفصل للترجمة، استخدم علم `-v`:
  ```bash
  gcc -v -o output source.c
  ```

- **GDB (GNU Debugger)**: لزيادة التفصيل، استخدم الأمر `set verbose on` داخل GDB:
  ```gdb
  (gdb) set verbose on
  (gdb) run
  ```

- **Ruby**: تشغيل نصوص Ruby بالوضع المفصل باستخدام علم `-v` أو `--verbose`:
  ```bash
  ruby -v script.rb
  ```
  للحصول على تحذيرات إضافية، استخدم `-w`:
  ```bash
  ruby -w script.rb
  ```

- **Perl**: تمكين الإخراج المفصل مع علم `-v` أو استخدم pragma `diagnostics` للحصول على رسائل خطأ مفصلة:
  ```bash
  perl -v script.pl
  ```
  أو في النص:
  ```perl
  use diagnostics;
  ```

- **PHP**: تشغيل نصوص PHP مع الإبلاغ المفصل عن الأخطاء عن طريق تعيين `error_reporting` و `display_errors` في `php.ini`:
  ```ini
  error_reporting = E_ALL
  display_errors = On
  ```
  أو من سطر الأوامر:
  ```bash
  php -d error_reporting=E_ALL script.php
  ```

- **R**: لتمكين الإخراج المفصل في نصوص R، استخدم الوسيطة `verbose=TRUE` في الدوال التي تدعمها (مثل `install.packages`):
  ```R
  install.packages("dplyr", verbose=TRUE)
  ```

- **Go (Golang)**: للحصول على إخراج مفصل أثناء الترجمة أو الاختبار، استخدم علم `-v`:
  ```bash
  go build -v
  go test -v
  ```

- **Rust (Cargo)**: تمكين الإخراج المفصل مع Cargo باستخدام علم `-v` أو `-vv`:
  ```bash
  cargo build -v
  cargo run -vv
  ```

- **Jenkins**: لتمكين التسجيل المفصل لخط أنابيب، أضف خيار `verbose` في النص أو قم بتكوين إخراج وحدة التحكم في إعدادات المهمة. على سبيل المثال، في Jenkinsfile:
  ```groovy
  sh 'some_command --verbose'
  ```
  بدلاً من ذلك، عيّن خاصية النظام `-Dhudson.model.TaskListener.verbose=true` عند بدء تشغيل Jenkins.

- **Vagrant**: الحصول على إخراج مفصل مع علم `--debug`:
  ```bash
  vagrant up --debug
  ```

- **Puppet**: تشغيل Puppet مع زيادة التفصيل باستخدام علم `--verbose` أو `--debug`:
  ```bash
  puppet apply site.pp --verbose
  puppet apply site.pp --debug
  ```

- **Chef**: تمكين الإخراج المفصل مع علم `-l` (مستوى التسجيل):
  ```bash
  chef-client -l debug
  ```

- **SaltStack**: زيادة التفصيل مع علم `-l` (مثل `debug` أو `trace`):
  ```bash
  salt '*' test.ping -l debug
  ```

- **PostgreSQL (psql)**: للحصول على إخراج مفصل من `psql`، استخدم علم `-e` لعرض الاستعلامات أو `\set VERBOSITY verbose` للحصول على رسائل خطأ مفصلة:
  ```bash
  psql -e -f script.sql
  ```
  أو في `psql`:
  ```sql
  \set VERBOSITY verbose
  ```

- **MySQL**: تشغيل عميل MySQL مع إخراج مفصل باستخدام `--verbose`:
  ```bash
  mysql --verbose < script.sql
  ```

- **SQLite**: استخدم الأمر `.explain` للحصول على خطط تنفيذ استعلام مفصلة:
  ```sqlite
  sqlite3 database.db
  sqlite> .explain
  sqlite> SELECT * FROM table;
  ```

- **MongoDB**: تمكين التسجيل المفصل عن طريق بدء `mongod` مع علم `-v` (حتى `-vvvvv` لمزيد من التفاصيل):
  ```bash
  mongod -v
  ```

- **Elasticsearch**: بدء Elasticsearch مع التسجيل المفصل عن طريق ضبط ملف `log4j2.properties`:
  ```properties
  logger.action.level = debug
  ```
  أو تمرير `--verbose` عند البدء:
  ```bash
  elasticsearch --verbose
  ```

- **NGINX**: اختبار التكوين مع إخراج مفصل باستخدام `-T`:
  ```bash
  nginx -T
  ```
  للتفصيل أثناء وقت التشغيل، زد مستوى `error_log` في `nginx.conf`:
  ```nginx
  error_log /var/log/nginx/error.log debug;
  ```

- **Apache HTTP Server**: تمكين التسجيل المفصل عن طريق تعيين توجيه `LogLevel` في `httpd.conf` أو `apache2.conf`:
  ```apache
  LogLevel debug
  ```

- **OpenSSL**: الحصول على إخراج مفصل مع أوامر مثل `s_client`:
  ```bash
  openssl s_client -connect example.com:443 -debug
  ```

- **JUnit (Java Testing)**: تشغيل اختبارات JUnit مع إخراج مفصل عن طريق تكوين مشغل الاختبار (مثل إضافة Maven Surefire):
  ```xml
  <configuration>
      <argLine>-verbose</argLine>
  </configuration>
  ```

هذه الأمثلة تغطي مجموعة واسعة من الأدوات عبر لغات البرمجة، وأنظمة البناء، وقواعد البيانات، والخوادم، وأدوات DevOps. أعلمني إذا كنت تريد المزيد من الأمثلة المحددة أو التفاصيل لأي أداة معينة!