---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: मोंगोडीबी व्यापक मार्गदर्शिका
translated: true
type: note
---

MongoDB एक लोकप्रिय ओपन-सोर्स NoSQL डॉक्यूमेंट डेटाबेस है जिसे आधुनिक एप्लिकेशन डेवलपमेंट के लिए डिज़ाइन किया गया है। यह डेटा को लचीले, JSON-जैसे दस्तावेज़ों में संग्रहीत करता है जिन्हें BSON (बाइनरी JSON) कहा जाता है, जो इसे असंरचित या अर्ध-संरचित डेटा को संभालने के लिए आदर्श बनाता है। पारंपरिक रिलेशनल डेटाबेस के विपरीत, MongoDB एक स्कीमा-रहित दृष्टिकोण का उपयोग करता है, जो संग्रहों (दस्तावेज़ों के समूह) को भिन्न-भिन्न संरचनाएँ रखने की अनुमति देता है। यह अत्यधिक स्केलेबल है, शार्डिंग के माध्यम से क्षैतिज स्केलिंग का समर्थन करता है, और प्रतिकृति के माध्यम से उच्च उपलब्धता प्रदान करता है। MongoDB को ऑन-प्रिमाइसेस, क्लाउड में MongoDB Atlas (एक मैनेज्ड सेवा) के माध्यम से, या हाइब्रिड वातावरण में तैनात किया जा सकता है। यह गाइड MongoDB शेल (mongosh) का उपयोग करके उदाहरणों के साथ बुनियादी बातों से लेकर उन्नत विषयों तक सब कुछ कवर करती है।

## परिचय

MongoDB उन परिदृश्यों में उत्कृष्टता प्राप्त करता है जिनमें तीव्र विकास, लचीले डेटा मॉडल और उच्च प्रदर्शन की आवश्यकता होती है। मुख्य विशेषताओं में शामिल हैं:
- **डॉक्यूमेंट मॉडल**: नेस्टेड संरचनाओं वाले स्व-निहित दस्तावेज़ों के रूप में डेटा।
- **क्वेरी भाषा**: JavaScript ऑब्जेक्ट्स के समान सिंटैक्स का उपयोग करके समृद्ध क्वेरीज़।
- **स्केलेबिलिटी**: वितरित सिस्टम के लिए अंतर्निहित समर्थन।
- **इकोसिस्टम**: आधिकारिक ड्राइवरों के माध्यम से Python, Node.js, Java जैसी भाषाओं के साथ एकीकृत।

इसका उपयोग Adobe, eBay, और Forbes जैसी कंपनियों द्वारा बिग डेटा, रियल-टाइम एनालिटिक्स और कंटेंट मैनेजमेंट से जुड़े एप्लिकेशन के लिए किया जाता है।

## इंस्टालेशन

MongoDB कम्युनिटी (मुफ्त, ओपन-सोर्स) और एंटरप्राइज़ संस्करण प्रदान करता है। इंस्टालेशन प्लेटफ़ॉर्म के अनुसार भिन्न होता है; सुरक्षा के लिए हमेशा आधिकारिक साइट से डाउनलोड करें।

### Windows
- MongoDB डाउनलोड सेंटर से MSI इंस्टॉलर डाउनलोड करें।
- इंस्टॉलर चलाएं, "कम्प्लीट" सेटअप चुनें, और MongoDB Compass (GUI टूल) शामिल करें।
- अपने PATH में MongoDB के `bin` डायरेक्टरी (जैसे, `C:\Program Files\MongoDB\Server\8.0\bin`) को जोड़ें।
- एक डेटा डायरेक्टरी बनाएं: `mkdir -p C:\data\db`।
- सर्वर शुरू करें: `mongod.exe --dbpath C:\data\db`।

समर्थित: Windows 11, Server 2022/2019।

### macOS
- Homebrew का उपयोग करें: `brew tap mongodb/brew && brew install mongodb-community`।
- या TGZ आर्काइव डाउनलोड करें, एक्सट्रैक्ट करें, और PATH में जोड़ें।
- डेटा डायरेक्टरी बनाएं: `mkdir -p /data/db`।
- शुरू करें: `mongod --dbpath /data/db` (या `brew services start mongodb/brew/mongodb-community` का उपयोग करें)।

समर्थित: macOS 11–14 (x86_64 और arm64)।

### Linux
- Ubuntu/Debian के लिए: MongoDB रेपो की और लिस्ट जोड़ें, फिर `apt-get install -y mongodb-org`।
- RHEL/CentOS के लिए: रेपो फ़ाइल के साथ yum/dnf का उपयोग करें।
- डेटा डायरेक्टरी बनाएं: `sudo mkdir -p /data/db && sudo chown -R $USER /data/db`।
- शुरू करें: `sudo systemctl start mongod`।

समर्थित: Ubuntu 24.04, RHEL 9+, Debian 12, Amazon Linux 2023, आदि। XFS/EXT4 फाइलसिस्टम का उपयोग करें; 32-बिट से बचें।

### क्लाउड (MongoDB Atlas)
- mongodb.com/atlas पर साइन अप करें।
- UI या CLI के माध्यम से एक मुफ्त क्लस्टर बनाएं: `atlas clusters create <नाम> --provider AWS --region us-east-1 --tier M0`।
- अपने IP को व्हाइटलिस्ट करें: `atlas network-access create <IP>`।
- कनेक्शन स्ट्रिंग प्राप्त करें और कनेक्ट करें: `mongosh "mongodb+srv://<user>:<pass>@cluster0.abcde.mongodb.net/"`।

Atlas बैकअप, स्केलिंग और मॉनिटरिंग को स्वचालित रूप से संभालता है।

## मूल अवधारणाएँ

### डेटाबेस
संग्रहों के लिए कंटेनर, डेटा को तार्किक रूप से अलग करते हैं। पहले उपयोग पर निहित रूप से बनाएं: `use mydb`। `use mydb` के साथ स्विच करें। सूची: `show dbs`।

### संग्रह
दस्तावेज़ों के समूह, टेबल्स की तरह लेकिन स्कीमा-लचीले। निहित रूप से बनाएं: `db.mycollection.insertOne({})`। सूची: `show collections`।

### दस्तावेज़
मूल इकाइयाँ: की-वैल्यू पेयर वाले BSON ऑब्जेक्ट्स। उदाहरण:
```javascript
{ "_id": ObjectId("..."), "name": "John", "age": 30, "address": { "city": "NYC", "zip": 10001 } }
```
एरेज़, नेस्टेड ऑब्जेक्ट्स और डेट्स, बाइनरीज़ जैसे प्रकारों का समर्थन करता है।

### BSON
कुशल संग्रहण/नेटवर्किंग के लिए बाइनरी फॉर्मेट। ObjectId, Date, Binary जैसे प्रकारों के साथ JSON का विस्तार करता है।

### नेमस्पेस
अद्वितीय पहचानकर्ता: `database.collection` (जैसे, `mydb.orders`)।

उदाहरण सेटअप:
```javascript
use test
db.orders.insertMany([
  { item: "almonds", price: 12, quantity: 2 },
  { item: "pecans", price: 20, quantity: 1 }
])
```

## CRUD ऑपरेशन्स

mongosh में `db.collection.method()` का उपयोग करें। मल्टी-डॉक्यूमेंट ACID के लिए सेशन के माध्यम से लेन-देन।

### बनाएँ (इन्सर्ट)
- एकल: `db.users.insertOne({ name: "Alice", email: "alice@example.com" })`
- एकाधिक: `db.users.insertMany([{ name: "Bob" }, { name: "Charlie" }])`
इन्सर्ट किए गए IDs लौटाता है।

### पढ़ें (फाइंड)
- सभी: `db.users.find()`
- फ़िल्टर्ड: `db.users.find({ age: { $gt: 25 } })`
- सुंदर प्रिंट: `.pretty()`
- सीमा/क्रमबद्ध करें: `db.users.find().limit(5).sort({ age: -1 })`

### अपडेट
- एकल: `db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })`
- एकाधिक: `db.users.updateMany({ age: { $lt: 20 } }, { $set: { status: "minor" } })`
- वृद्धि: `{ $inc: { score: 10 } }`

### हटाएँ
- एकल: `db.users.deleteOne({ name: "Bob" })`
- एकाधिक: `db.users.deleteMany({ status: "inactive" })`
- संग्रह ड्रॉप करें: `db.users.drop()`

## क्वेरी करना और इंडेक्सिंग

### क्वेरी करना
शर्तों के लिए प्रिडिकेट्स का उपयोग करें। समानता, रेंज, लॉजिकल ऑप्स का समर्थन करता है।

- बेसिक: `db.inventory.find({ status: "A" })` (SQL समतुल्य: `WHERE status = 'A'`)
- $in: `db.inventory.find({ status: { $in: ["A", "D"] } })`
- $lt/$gt: `db.inventory.find({ qty: { $lt: 30 } })`
- $or: `db.inventory.find({ $or: [{ status: "A" }, { qty: { $lt: 30 } }] })`
- रेगेक्स: `db.inventory.find({ item: /^p/ })` ("p" से शुरू होता है)
- एम्बेडेड: `db.users.find({ "address.city": "NYC" })`

प्रोजेक्शन (फ़ील्ड्स चुनें): `db.users.find({ age: { $gt: 25 } }, { name: 1, _id: 0 })`

### इंडेक्सिंग
पूर्ण स्कैन से बचाकर क्वेरी गति में सुधार करता है। B-ट्री आधारित।

- प्रकार: सिंगल-फ़ील्ड (`db.users.createIndex({ name: 1 })`), कंपाउंड (`{ name: 1, age: -1 }`), यूनिक (`{ email: 1 }`)।
- लाभ: तेज समानता/रेंज क्वेरीज़, क्रमबद्ध परिणाम।
- निर्माण: `db.users.createIndex({ age: 1 })` (आरोही)।
- देखें: `db.users.getIndexes()`
- ड्रॉप: `db.users.dropIndex("age_1")`

सिफारिशों के लिए Atlas Performance Advisor का उपयोग करें। ट्रेड-ऑफ़: धीमे राइट्स।

## एग्रीगेशन फ्रेमवर्क

पाइपलाइन में चरणों के माध्यम से डेटा प्रोसेस करता है। SQL GROUP BY की तरह लेकिन अधिक शक्तिशाली।

- बेसिक: `db.orders.aggregate([ { $match: { price: { $lt: 15 } } } ])`
- चरण: `$match` (फ़िल्टर), `$group` (एग्रीगेट: `{ $sum: "$price" }`), `$sort`, `$lookup` (जॉइन: `{ from: "inventory", localField: "item", foreignField: "sku", as: "stock" }`), `$project` (रीशेप)।
- उदाहरण (जॉइन और सॉर्ट):
```javascript
db.orders.aggregate([
  { $match: { price: { $lt: 15 } } },
  { $lookup: { from: "inventory", localField: "item", foreignField: "sku", as: "inventory_docs" } },
  { $sort: { price: 1 } }
])
```
एक्सप्रेशन: `{ $add: [ "$price", 10 ] }`। Atlas UI में पूर्वावलोकन।

## स्कीमा डिज़ाइन

MongoDB की लचीलापन कठोर स्कीमा से बचाता है लेकिन प्रदर्शन के लिए विचारपूर्ण डिजाइन की आवश्यकता होती है।

- **सिद्धांत**: एक्सेस पैटर्न (रीड्स/राइट्स) के लिए मॉडल बनाएं, इंडेक्सेस का उपयोग करें, वर्किंग सेट को RAM में रखें।
- **एम्बेडिंग**: एटॉमिक रीड्स/राइट्स के लिए संबंधित डेटा को एक दस्तावेज़ में डीनॉर्मलाइज़ करें। जैसे, पोस्ट में कमेंट्स एम्बेड करें। पेशेवर: तेज क्वेरीज़। विपक्ष: डुप्लिकेशन, बड़े दस्तावेज़।
- **रेफरेंसिंग**: IDs के साथ नॉर्मलाइज़ करें। जैसे, `posts` `userId` के माध्यम से `users` को रेफर करता है। जॉइन के लिए `$lookup` का उपयोग करें। पेशेवर: कम डुप्लिकेशन। विपक्ष: एकाधिक क्वेरीज़।
- पैटर्न: एक-से-कुछ (एम्बेड), एक-से-अनेक (रेफरेंस या एम्बेड ऐरे), अनेक-से-अनेक (रेफरेंस)।
- वैलिडेशन: `db.createCollection("users", { validator: { $jsonSchema: { ... } } })` के साथ लागू करें।

डुप्लिकेशन ट्रेड-ऑफ़ और एटॉमिसिटी (दस्तावेज़-स्तर केवल) पर विचार करें।

## प्रतिकृति और शार्डिंग

### प्रतिकृति
रिप्लिका सेट (`mongod` इंस्टेंस के समूह) के माध्यम से अतिरेक/उच्च उपलब्धता प्रदान करता है।

- घटक: प्राइमरी (राइट्स), सेकेंडरीज़ (ओपलॉग के माध्यम से प्रतिकृति बनाते हैं, रीड्स वैकल्पिक), आर्बिटर (वोट करता है, कोई डेटा नहीं)।
- तैनाती: `rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "host1:27017" }] })` के साथ इनिशियलाइज़ करें। मेंबर जोड़ें: `rs.add("host2:27017")`।
- चुनाव: यदि प्राइमरी विफल हो जाती है, तो सेकेंडरी ~10-12s में चुनाव करती है।
- रीड प्रेफरेंस: `primary`, `secondary` (लेग हो सकता है)।
- फेलओवर, बैकअप के लिए उपयोग करें। लैग को प्रबंधित करने के लिए फ्लो कंट्रोल सक्षम करें।

### शार्डिंग
क्षैतिज स्केलिंग: शार्ड्स में डेटा वितरित करता है।

- घटक: शार्ड्स (रिप्लिका सेट), मोंगोस (राउटर), कॉन्फ़िग सर्वर (मेटाडेटा)।
- शार्ड कुंजी: पार्टीशनिंग के लिए फ़ील्ड(स) (जैसे, समान वितरण के लिए हैश्ड)। पहले इंडेक्स बनाएं।
- सेटअप: शार्डिंग सक्षम करें `sh.enableSharding("mydb")`, संग्रह शार्ड करें `sh.shardCollection("mydb.users", { userId: "hashed" })`।
- बैलेंसर: समान लोड के लिए चंक्स माइग्रेट करता है। जियो-लोकैलिटी के लिए ज़ोन।
- रणनीतियाँ: हैश्ड (यूनिफ़ॉर्म), रेंज्ड (टार्गेटेड क्वेरीज़)।

मोंगोस के माध्यम से कनेक्ट करें; लेन-देन का समर्थन करता है।

## सुरक्षा

परतबद्ध सुरक्षा के साथ सुरक्षित तैनाती।

- **प्रमाणीकरण**: SCRAM, LDAP, OIDC, X.509। उपयोगकर्ता बनाएँ: `db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })`।
- **अधिकार**: रोल-आधारित एक्सेस कंट्रोल (RBAC)। अंतर्निहित भूमिकाएँ: read, readWrite, dbAdmin।
- **एन्क्रिप्शन**: ट्रांजिट के लिए TLS/SSL, एन्क्रिप्शन एट रेस्ट (EAR) AWS KMS/Google Cloud KMS/Azure Key Vault के माध्यम से। संवेदनशील फ़ील्ड्स के लिए क्लाइंट-साइड फ़ील्ड लेवल एन्क्रिप्शन (CSFLE)।
- नेटवर्क: IP एक्सेस लिस्ट, Atlas में VPC पीयरिंग।
- ऑडिटिंग: ऑपरेशन लॉग करें।

स्टार्टअप पर ऑथ सक्षम करें: `--auth`। अंतर्निहित सुरक्षा के लिए Atlas का उपयोग करें।

## सर्वोत्तम अभ्यास

- **प्रोडक्शन सेटअप**: सेवा के रूप में चलाएं (systemctl/brew)। SSDs पर डेटा/जर्नल/लॉग्स अलग करें। WiredTiger इंजन (डिफ़ॉल्ट) का उपयोग करें।
- **मॉनिटरिंग**: `mongostat`, `mongotop`, Atlas चार्ट्स। कनेक्शन (`connPoolStats`), कैश एविक्शन, I/O (`iostat`) पर नज़र रखें।
- **बैकअप**: `mongodump`/`mongorestore`, या Atlas स्नैपशॉट्स। लॉजिकल (JSON) बनाम फिजिकल (फाइलें)।
- **प्रदर्शन**: समझदारी से इंडेक्स करें, प्रोजेक्शन सीमित करें, बड़े ऐरे से बचें। `ulimit -n 64000` सेट करें, स्वैप अक्षम करें (`vm.swappiness=0`), TCP कीपअलाइव ट्यून करें।
- **स्केलिंग**: रिप्लिका सेट के साथ शुरू करें; >100GB या उच्च थ्रूपुट पर शार्ड करें।
- **डेटा आयात**: `mongoimport --db test --collection users --file users.json`।
- **टूल्स**: MongoDB Compass (GUI), mongosh (शेल), एप्स के लिए ड्राइवर।
- **सामान्य गलतियाँ**: ओवर-एम्बेडिंग (दस्तावेज़ आकार सीमा 16MB), इंडेक्सेस को नज़रअंदाज़ करना, रिप्लिकेशन लैग को हैंडल न करना।

विकास के लिए, Atlas M0 फ्री टियर का उपयोग करें। `mongoperf` के साथ वर्कलोड का परीक्षण करें।

## संदर्भ
- [MongoDB मैनुअल](https://www.mongodb.com/docs/manual/)
- [MongoDB इंस्टालेशन](https://www.mongodb.com/docs/manual/installation/)
- [MongoDB मूल अवधारणाएँ](https://www.mongodb.com/docs/manual/core/)
- [MongoDB CRUD](https://www.mongodb.com/docs/manual/crud/)
- [MongoDB क्वेरी करना](https://www.mongodb.com/docs/manual/tutorial/query-documents/)
- [MongoDB इंडेक्स](https://www.mongodb.com/docs/manual/indexes/)
- [MongoDB एग्रीगेशन](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
- [MongoDB स्कीमा डिज़ाइन](https://www.mongodb.com/docs/manual/core/data-model-design/)
- [MongoDB प्रतिकृति](https://www.mongodb.com/docs/manual/replication/)
- [MongoDB शार्डिंग](https://www.mongodb.com/docs/manual/sharding/)
- [MongoDB सुरक्षा](https://www.mongodb.com/docs/manual/core/security/)
- [MongoDB प्रोडक्शन नोट्स](https://www.mongodb.com/docs/manual/administration/production-notes/)