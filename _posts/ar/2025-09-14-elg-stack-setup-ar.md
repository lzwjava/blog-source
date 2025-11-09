---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: دليل إعداد وتثبيت ELG Stack
translated: true
type: note
---

### نظرة عامة على ELG Stack (Elasticsearch, Logstash, Grafana)

مكدس ELG (غالبًا ما يكون متغيرًا من مكدس ELK حيث يتم استبدال Kibana بـ Grafana للتخيل) هو مجموعة قوية مفتوحة المصدر لجمع ومعالجة وتخزين وتصور كميات كبيرة من البيانات، وخاصة السجلات من التطبيقات والخوادم والبنية التحتية. فهو يمكّن من المراقبة والتحليل والتنبيه في الوقت الفعلي. المكونات الرئيسية:

- **Elasticsearch**: محرك بحث وتحليل موزع لتخزين البيانات والبحث فيها وتحليلها على نطاق واسع.
- **Logstash**: خط أنابيب معالجة البيانات يستقبل البيانات من مصادر متعددة، يحولها، ويرسلها إلى Elasticsearch.
- **Grafana**: أداة لوحة تحكم للتخيل والمراقبة تتصل بمصادر البيانات مثل Elasticsearch لإنشاء مخططات ورسوم بيانية وتنبيهات.

يفترض هذا الدليل معرفة أساسية بـ Linux (مثل Ubuntu/Debian؛ قم بالتعديل لأنظمة التشغيل الأخرى). استخدم الوثائق الرسمية للحصول على التفاصيل الكاملة. يتم التثبيت عبر التنزيلات من elastic.co و grafana.com.

#### 1. تثبيت Elasticsearch
يتعامل Elasticsearch مع تخزين البيانات والفهرسة.

- **المتطلبات الأساسية**: Java 11+ (قم بالتثبيت عبر `sudo apt update && sudo apt install openjdk-11-jdk`).
- التنزيل والتثبيت:
  ```
  wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
  sudo apt update && sudo apt install elasticsearch
  ```
- التشغيل والتمكين: `sudo systemctl start elasticsearch && sudo systemctl enable elasticsearch`.
- التحقق: قم بزيارة `http://localhost:9200` – يجب أن تعود بـ JSON يحتوي على معلومات العنقود.
- الإعداد الأساسي (قم بتحرير `/etc/elasticsearch/elasticsearch.yml`): عيّن `network.host: 0.0.0.0` للوصول عن بُعد (قم بتأمينه بـ TLS/جدار حماية في بيئة الإنتاج).

#### 2. تثبيت Logstash
يقوم Logstash بسحب البيانات من المصادر (مثل الملفات، syslogs) وشحنها إلى Elasticsearch.

- التثبيت بجانب Elasticsearch:
  ```
  sudo apt install logstash
  ```
- التشغيل والتمكين: `sudo systemctl start logstash && sudo systemctl enable logstash`.
- مثال على الإعداد لاستيعاب السجلات (`/etc/logstash/conf.d/simple.conf`):
  ```
  input {
    file {
      path => "/var/log/syslog"
      start_position => "beginning"
    }
  }
  filter {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{WORD:program}: %{GREEDYDATA:message}" }
    }
  }
  output {
    elasticsearch {
      hosts => ["localhost:9200"]
    }
    stdout { codec => rubydebug }
  }
  ```
- اختبار خط الأنابيب: `sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/simple.conf` (شغّله في الخلفية للاستخدام المستمر).
- إعادة تحميل الإعداد: `sudo systemctl restart logstash`.

#### 3. تثبيت Grafana
توفر Grafana لوحات تحكم لتخيل بيانات Elasticsearch.

- التثبيت:
  ```
  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
  sudo apt update && sudo apt install grafana
  ```
- التشغيل والتمكين: `sudo systemctl start grafana-server && sudo systemctl enable grafana-server`.
- الوصول: قم بزيارة `http://localhost:3000` (تسجيل الدخول الافتراضي: admin/admin؛ قم بتغيير كلمة المرور).
- الاتصال بـ Elasticsearch:
  1. انتقل إلى Configuration > Data Sources > Add data source.
  2. اختر "Elasticsearch"، عيّن URL إلى `http://localhost:9200`، اسم الفهرس (مثل `logstash-*`)، وحقل الوقت (مثل `@timestamp`).
  3. احفظ واختبر الاتصال.

#### إعداد خط أنابيب ELG الكامل
1. **تدفق البيانات**: Logstash يجمع/يحلل السجلات → يرسلها إلى Elasticsearch → Grafana يستعلم ويصور البيانات.
2. **مثال على سير العمل**:
   - إرسال بيانات نموذجية: استخدم إضافات إدخال Logstash أو أدوات مثل `stdout` للاختبار.
   - الفهرسة في Elasticsearch: تظهر السجلات كمستندات (عبر واجهة برمجة تطبيقات Kibana على سبيل المثال أو curl مباشر: `curl -X GET "localhost:9200/_search?pretty"`).
   - لوحة التحكم في Grafana: أنشئ لوحات (مخطط خطي لأخطاء السجل عبر الزمن باستخدام استعلامات Lucene مثل `program:kern*`).
3. **أساسيات الأمان**: استخدم HTTPS/TLS، المصادقة (مثل X-Pack لـ Elasticsearch)، وجدران الحماية. لبيئة الإنتاج، قم بالتوسع باستخدام عقد/عناقيد متعددة.
4. **المراقبة**: مكّن مراقبة JVM في Elasticsearch؛ تحتوي Grafana على تنبيهات مدمجة للعتبات.

#### المشاكل الشائعة والنصائح
- **نفاد الذاكرة**: زد ذاكرة JVM في `/etc/elasticsearch/jvm.options` (مثل `-Xms1g -Xmx1g`).
- **تعارض المنافذ**: المنافذ الافتراضية: Elasticsearch 9200/9300, Logstash 5044, Grafana 3000 – تحقق من `netstat -tulpn`.
- **الأداء**: استخدم beats (مثل Filebeat) بدلاً من Logstash للنقل خفيف الوزن.
- **موارد التعلم**: أدلة Elastic الرسمية (elastic.co/guide)، وثائق Grafana (grafana.com/docs). تدرب باستخدام Docker: ابحث عن "ELG stack Docker Compose" على GitHub.

للمنشآت المخصصة أو استكشاف الأخطاء وإصلاحها لأخطاء محددة، قدم المزيد من التفاصيل. هذه نقطة بداية؛ يتفوق ELG في تحليل السجلات، بيانات IoT، ومراقبة التطبيقات.