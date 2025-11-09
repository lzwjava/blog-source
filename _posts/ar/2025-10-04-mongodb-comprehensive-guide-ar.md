---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل شامل لـ MongoDB
translated: true
type: note
---

MongoDB هي قاعدة بيانات وثائق NoSQL مفتوحة المصدر شائعة مصممة لتطوير التطبيقات الحديثة. تقوم بتخزين البيانات في وثائق مرنة تشبه JSON تسمى BSON (Binary JSON)، مما يجعلها مثالية للتعامل مع البيانات غير المهيكلة أو شبه المهيكلة. على عكس قواعد البيانات العلائقية التقليدية، تستخدم MongoDB نهجًا بدون مخطط (schema-less)، مما يسمح للمجموعات (مجموعات الوثائق) بأن يكون لها هياكل متغيرة. وهي قابلة للتوسع بدرجة كبيرة، وتدعم التوسع الأفقي عبر التقسيم (sharding)، وتوفر عالية التوفر عبر الاستنساخ (replication). يمكن نشر MongoDB في الموقع (on-premises)، أو في السحابة عبر MongoDB Atlas (خدمة مُدارة)، أو في بيئات هجينة. يغطي هذا الدليل كل شيء من الأساسيات إلى الموضوعات المتقدمة، مع أمثلة باستخدام MongoDB Shell (mongosh).

## المقدمة

تتفوق MongoDB في السيناريوهات التي تتطلب تطويرًا سريعًا، ونماذج بيانات مرنة، وأداءً عاليًا. تشمل الميزات الرئيسية:
- **نموذج الوثيقة (Document Model)**: البيانات كوثائق مستقلة ذات هياكل متداخلة.
- **لغة الاستعلام (Query Language)**: استعلامات غنية باستخدام بناء جملة مشابه لكائنات JavaScript.
- **القابلية للتوسع (Scalability)**: دعم مدمج للأنظمة الموزعة.
- **النظام البيئي (Ecosystem)**: يتكامل مع لغات مثل Python و Node.js و Java عبر برامج التشغيل (drivers) الرسمية.

يستخدمها شركات مثل Adobe و eBay و Forbes للتطبيقات التي تتضمن بيانات ضخمة (big data)، وتحليلات في الوقت الفعلي، وإدارة المحتوى.

## التثبيت

تقدم MongoDB إصدارات Community (مجاني، مفتوح المصدر) و Enterprise. يختلف التثبيت حسب المنصة؛ قم دائمًا بالتحميل من الموقع الرسمي لأسباب أمنية.

### Windows
- حمل برنامج التثبيت MSI من مركز تحميل MongoDB.
- شغل برنامج التثبيت، واختر إعداد "Complete"، وقم بتضمين MongoDB Compass (أداة واجهة المستخدم الرسومية).
- أضف دليل `bin` الخاص بـ MongoDB (مثال: `C:\Program Files\MongoDB\Server\8.0\bin`) إلى متغير البيئة PATH الخاص بك.
- أنشئ دليل بيانات: `mkdir -p C:\data\db`.
- ابدأ الخادم: `mongod.exe --dbpath C:\data\db`.

مدعوم: Windows 11, Server 2022/2019.

### macOS
- استخدم Homebrew: `brew tap mongodb/brew && brew install mongodb-community`.
- أو حمل أرشيف TGZ، وقم باستخراجه، وأضفه إلى PATH.
- أنشئ دليل بيانات: `mkdir -p /data/db`.
- ابدأ: `mongod --dbpath /data/db` (أو استخدم `brew services start mongodb/brew/mongodb-community`).

مدعوم: macOS 11–14 (x86_64 و arm64).

### Linux
- لأوبونتو/ديبيان: أضف مفتاح مستودع MongoDB والقائمة، ثم `apt-get install -y mongodb-org`.
- لـ RHEL/CentOS: استخدم yum/dnf مع ملف المستودع.
- أنشئ دليل بيانات: `sudo mkdir -p /data/db && sudo chown -R $USER /data/db`.
- ابدأ: `sudo systemctl start mongod`.

مدعوم: Ubuntu 24.04, RHEL 9+, Debian 12, Amazon Linux 2023، إلخ. استخدم أنظمة الملفات XFS/EXT4؛ تجنب 32-bit.

### السحابة (MongoDB Atlas)
- سجل الدخول في mongodb.com/atlas.
- أنشئ مجموعة (cluster) مجانية عبر واجهة المستخدم أو سطر الأوامر: `atlas clusters create <name> --provider AWS --region us-east-1 --tier M0`.
- أضف عنوان IP الخاص بك إلى القائمة البيضاء: `atlas network-access create <IP>`.
- احصل على سلسلة الاتصال وتواصل: `mongosh "mongodb+srv://<user>:<pass>@cluster0.abcde.mongodb.net/"`.

يقوم Atlas تلقائيًا بإدارة النسخ الاحتياطية، والتوسع، والمراقبة.

## المفاهيم الأساسية

### قواعد البيانات (Databases)
حاويات للمجموعات، تفصل البيانات منطقيًا. أنشئها ضمناً عند أول استخدام: `use mydb`. انتقل بينها باستخدام `use mydb`. اعرضها: `show dbs`.

### المجموعات (Collections)
مجموعات من الوثائق، تشبه الجداول ولكنها مرنة في المخطط. أنشئها ضمناً: `db.mycollection.insertOne({})`. اعرضها: `show collections`.

### الوثائق (Documents)
الوحدات الأساسية: كائنات BSON تحتوي على أزواج مفتاح-قيمة. مثال:
```javascript
{ "_id": ObjectId("..."), "name": "John", "age": 30, "address": { "city": "NYC", "zip": 10001 } }
```
تدعم المصفوفات، والكائنات المتداخلة، وأنواعًا مثل التواريخ والبيانات الثنائية.

### BSON
تنسيق ثنائي للتخزين/الشبكات بكفاءة. يمتد على JSON بأنواع مثل ObjectId و Date و Binary.

### مساحات الأسماء (Namespaces)
معرفات فريدة: `database.collection` (مثال: `mydb.orders`).

مثال للإعداد:
```javascript
use test
db.orders.insertMany([
  { item: "almonds", price: 12, quantity: 2 },
  { item: "pecans", price: 20, quantity: 1 }
])
```

## عمليات CRUD

استخدم `db.collection.method()` في mongosh. المعاملات (Transactions) عبر الجلسات (sessions) لضمان ACID للوثائق المتعددة.

### الإنشاء (إدراج)
- فردي: `db.users.insertOne({ name: "Alice", email: "alice@example.com" })`
- متعدد: `db.users.insertMany([{ name: "Bob" }, { name: "Charlie" }])`
تُرجع معرفات (IDs) الوثائق المُدرجة.

### القراءة (البحث)
- الكل: `db.users.find()`
- بفلتر: `db.users.find({ age: { $gt: 25 } })`
- طباعة منسقة: `.pretty()`
- تحديد/ترتيب: `db.users.find().limit(5).sort({ age: -1 })`

### التحديث
- فردي: `db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })`
- متعدد: `db.users.updateMany({ age: { $lt: 20 } }, { $set: { status: "minor" } })`
- زيادة: `{ $inc: { score: 10 } }`

### الحذف
- فردي: `db.users.deleteOne({ name: "Bob" })`
- متعدد: `db.users.deleteMany({ status: "inactive" })`
- حذف المجموعة: `db.users.drop()`

## الاستعلام والفهرسة

### الاستعلام
استخدم الشروط (predicates) للبحث. تدعم المساواة، والنطاقات، والعوامل المنطقية.

- أساسي: `db.inventory.find({ status: "A" })` (ما يعادل SQL: `WHERE status = 'A'`)
- $in: `db.inventory.find({ status: { $in: ["A", "D"] } })`
- $lt/$gt: `db.inventory.find({ qty: { $lt: 30 } })`
- $or: `db.inventory.find({ $or: [{ status: "A" }, { qty: { $lt: 30 } }] })`
- تعبير نمطي (Regex): `db.inventory.find({ item: /^p/ })` (يبدأ بـ "p")
- مضمن: `db.users.find({ "address.city": "NYC" })`

الإسقاط (اختيار الحقول): `db.users.find({ age: { $gt: 25 } }, { name: 1, _id: 0 })`

### الفهرسة
تحسن سرعة الاستعلام عن طريق تجنب المسح الكامل (full scans). تعتمد على شجرة B (B-tree).

- الأنواع: حقل مفرد (`db.users.createIndex({ name: 1 })`)، مركب (`{ name: 1, age: -1 }`)، فريد (`{ email: 1 }`).
- الفوائد: استعلامات مساواة/نطاق أسرع، نتائج مرتبة.
- الإنشاء: `db.users.createIndex({ age: 1 })` (تصاعدي).
- العرض: `db.users.getIndexes()`
- الحذف: `db.users.dropIndex("age_1")`

استخدم Atlas Performance Advisor للحصول على توصيات. المقايضة: عمليات الكتابة أبطأ.

## إطار التجميع (Aggregation Framework)

يعالج البيانات عبر مراحل في خط أنابيب (pipeline). يشبه GROUP BY في SQL ولكنه أكثر قوة.

- أساسي: `db.orders.aggregate([ { $match: { price: { $lt: 15 } } } ])`
- المراحل: `$match` (تصفية)، `$group` (تجميع: `{ $sum: "$price" }`)، `$sort`، `$lookup` (دمج: `{ from: "inventory", localField: "item", foreignField: "sku", as: "stock" }`)، `$project` (إعادة تشكيل).
- مثال (دمج وترتيب):
```javascript
db.orders.aggregate([
  { $match: { price: { $lt: 15 } } },
  { $lookup: { from: "inventory", localField: "item", foreignField: "sku", as: "inventory_docs" } },
  { $sort: { price: 1 } }
])
```
التعبيرات: `{ $add: [ "$price", 10 ] }`. معاينة في واجهة مستخدم Atlas.

## تصميم المخطط (Schema Design)

مرونة MongoDB تتجنب المخططات الصارمة ولكنها تتطلب تصميمًا مدروسًا للأداء.

- **المبادئ**: صمم لأنماط الوصول (قراءة/كتابة)، استخدم الفهارس، حافظ على مجموعة العمل (working set) في الذاكرة RAM.
- **التضمين (Embedding)**: عدم تسوية (Denormalize) البيانات المرتبطة في وثيقة واحدة للقراءات/الكتابات الذرية. مثال: تضمين التعليقات في المنشورات. الإيجابيات: استعلامات سريعة. السلبيات: تكرار، وثائق كبيرة الحجم.
- **الإحالة (Referencing)**: تسوية (Normalize) باستخدام المعرفات (IDs). مثال: `posts` تشير إلى `users` عبر `userId`. استخدم `$lookup` للدمج. الإيجابيات: تكرار أقل. السلبيات: استعلامات متعددة.
- الأنماط: واحد إلى قليل (تضمين)، واحد إلى كثير (إحالة أو تضمين مصفوفة)، كثير إلى كثير (إحالة).
- التحقق (Validation): فرضه باستخدام `db.createCollection("users", { validator: { $jsonSchema: { ... } } })`.

ضع في اعتبارك مقايضات التكرار والذرية (فقط على مستوى الوثيقة).

## الاستنساخ (Replication) والتقسيم (Sharding)

### الاستنساخ
يوفر التكرار/عالي التوفر عبر مجموعات مستنسخة (replica sets) (مجموعة من مثيلات `mongod`).

- المكونات: أساسي (Primary) (الكتابة)، ثانوي (Secondaries) (يستنسخ عبر سجل العمليات (oplog)، قراءة اختيارية)، محكم (Arbiter) (يصوت، لا يخزن بيانات).
- النشر: ابدأ بـ `rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "host1:27017" }] })`. أضف أعضاء: `rs.add("host2:27017")`.
- الانتخابات: إذا فشل الأساسي، ينتخب ثانوي خلال ~10-12 ثانية.
- تفضيل القراءة: `primary`، `secondary` (قد يكون متأخرًا).
- استخدمه لتحقيق التكرار عند الفشل، والنسخ الاحتياطية. مكن التحكم في التدفق (flow control) لإدارة التأخر.

### التقسيم
التوسع الأفقي: توزيع البيانات عبر القطع (shards).

- المكونات: القطع (Shards) (مجموعات مستنسخة)، Mongos (موجهات)، خوادم التكوين (Config servers) (بيانات وصفية).
- مفتاح التقسيم (Shard Key): الحقل (الحقول) المستخدم للتقسيم (مثال: مشفر (hashed) للتوزيع المتساوي). أنشئ الفهرس أولاً.
- الإعداد: مكن التقسيم `sh.enableSharding("mydb")`، قم بتقسيم المجموعة `sh.shardCollection("mydb.users", { userId: "hashed" })`.
- الموزع (Balancer): ينقل القطع (chunks) لتوزيع الحمل. المناطق (Zones) للتجميع الجغرافي.
- الاستراتيجيات: مشفر (Hashed) (موحد)، بالنطاق (Ranged) (للاستعلامات المستهدفة).

تواصل عبر mongos؛ يدعم المعاملات (transactions).

## الأمان

امنع النشر باستخدام حمايات متعددة الطبقات.

- **المصادقة (Authentication)**: SCRAM, LDAP, OIDC, X.509. أنشئ مستخدمين: `db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })`.
- **الترخيص (Authorization)**: التحكم في الوصول القائم على الأدوار (RBAC). أدوار مدمجة: read, readWrite, dbAdmin.
- **التشفير (Encryption)**: TLS/SSL للبيانات أثناء النقل، تشفير البيانات في حالة السكون (EAR) عبر AWS KMS/Google Cloud KMS/Azure Key Vault. التشفير من جانب العميل على مستوى الحقل (CSFLE) للحقول الحساسة.
- الشبكة: قوائم التحكم في الوصول لعناوين IP، وربط VPC في Atlas.
- التدقيق (Auditing): تسجيل العمليات.

مكن المصادقة عند البدء: `--auth`. استخدم Atlas للأمان المدمج.

## أفضل الممارسات

- **إعداد الإنتاج**: شغله كخدمة (systemctl/brew). افصل البيانات/سجلات المعاملات (journal)/سجلات النظام (logs) على أقراص SSD. استخدم محرك WiredTiger (الإفتراضي).
- **المراقبة**: `mongostat`, `mongotop`, مخططات Atlas. راقب الاتصالات (`connPoolStats`)، طرد ذاكرة التخزين المؤقت، الإدخال/الإخراج (`iostat`).
- **النسخ الاحتياطي**: `mongodump`/`mongorestore`، أو لقطات Atlas. منطقي (JSON) مقابل مادي (ملفات).
- **الأداء**: فهرس بحكمة، حدد الإسقاطات، تجنب المصفوفات الكبيرة. عيّن `ulimit -n 64000`، عطّل المبادلة (swap) (`vm.swappiness=0`)، اضبط إبقاء اتصال TCP (TCP keepalive).
- **التوسع**: ابدأ بمجموعات مستنسخة؛ قم بالتقسيم عند تجاوز 100GB أو معدل نقل عالي.
- **استيراد البيانات**: `mongoimport --db test --collection users --file users.json`.
- **الأدوات**: MongoDB Compass (واجهة رسومية)، mongosh (سطر أوامر)، برامج التشغيل (drivers) للتطبيقات.
- **الأخطاء الشائعة**: الإفراط في التضمين (حد حجم الوثيقة 16MB)، تجاهل الفهارس، عدم معالجة تأخر الاستنساخ.

للتطوير، استخدم الطبقة المجانية Atlas M0. اختبر أحمال العمل باستخدام `mongoperf`.

## المراجع
- [دليل MongoDB](https://www.mongodb.com/docs/manual/)
- [تثبيت MongoDB](https://www.mongodb.com/docs/manual/installation/)
- [مفاهيم MongoDB الأساسية](https://www.mongodb.com/docs/manual/core/)
- [عمليات CRUD في MongoDB](https://www.mongodb.com/docs/manual/crud/)
- [الاستعلام في MongoDB](https://www.mongodb.com/docs/manual/tutorial/query-documents/)
- [فهارس MongoDB](https://www.mongodb.com/docs/manual/indexes/)
- [تجميع MongoDB](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
- [تصميم مخطط MongoDB](https://www.mongodb.com/docs/manual/core/data-model-design/)
- [استنساخ MongoDB](https://www.mongodb.com/docs/manual/replication/)
- [تقسيم MongoDB](https://www.mongodb.com/docs/manual/sharding/)
- [أمان MongoDB](https://www.mongodb.com/docs/manual/core/security/)
- [ملاحظات إنتاج MongoDB](https://www.mongodb.com/docs/manual/administration/production-notes/)