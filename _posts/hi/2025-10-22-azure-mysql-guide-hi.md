---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एज़्योर डेटाबेस फॉर MySQL फ्लेक्सिबल सर्वर गाइड
translated: true
type: note
---

Azure Database for MySQL, MySQL कम्युनिटी एडिशन द्वारा संचालित एक पूरी तरह से प्रबंधित रिलेशनल डेटाबेस सेवा है। यह बैकअप, पैचिंग और मॉनिटरिंग जैसे नियमित कार्यों को संभालता है, जिससे आप अपने एप्लिकेशन पर ध्यान केंद्रित कर सकते हैं। अनुशंसित डेप्लॉयमेंट विकल्प **फ्लेक्सिबल सर्वर** है, जो पुराने सिंगल सर्वर (जिसे रिटायर किया जा रहा है) की तुलना में अधिक कॉन्फ़िगरेशन विकल्प और बेहतर परफॉर्मेंस प्रदान करता है।

यह गाइड एक सर्वर बनाने, उससे कनेक्ट होने और बेसिक ऑपरेशन करने को कवर करती है। यह सरलता के लिए Azure पोर्टल पर आधारित है।

## पूर्वापेक्षाएँ
- एक एक्टिव Azure सब्सक्रिप्शन (अगर जरूरत हो तो [azure.microsoft.com](https://azure.microsoft.com/free/) पर बनाएं)।
- Azure पोर्टल (portal.azure.com) तक पहुंच।
- MySQL कॉन्सेप्ट्स की बेसिक जानकारी।
- पोर्ट 3306 (MySQL के लिए डिफॉल्ट) पर आउटबाउंड नेटवर्क एक्सेस।
- कनेक्शन के लिए MySQL वर्कबेंच इंस्टॉल होना ( [mysql.com](https://dev.mysql.com/downloads/workbench/) से डाउनलोड करें)।

## चरण 1: Azure पोर्टल में एक फ्लेक्सिबल सर्वर बनाएं
अपना सर्वर प्रोविजन करने के लिए इन चरणों का पालन करें।

1. [Azure पोर्टल](https://portal.azure.com) में साइन इन करें।

2. टॉप सर्च बार में "Azure Database for MySQL Flexible Servers" सर्च करें और उसे सेलेक्ट करें।

3. विज़ार्ड शुरू करने के लिए **Create** पर क्लिक करें।

4. **Basics** टैब पर, कॉन्फ़िगर करें:
   - **Subscription**: अपना सब्सक्रिप्शन चुनें।
   - **Resource group**: एक नया बनाएं (जैसे, `myresourcegroup`) या मौजूदा चुनें।
   - **Server name**: यूनिक नाम (जैसे, `mydemoserver`), 3-63 करैक्टर, लोअरकेस अक्षर/नंबर/हाइफन। पूरा होस्टनेम `<name>.mysql.database.azure.com` होगा।
   - **Region**: अपने यूजर्स के सबसे नजदीक चुनें।
   - **MySQL version**: 8.0 (नवीनतम मेजर वर्जन)।
   - **Workload type**: डेवलपमेंट (टेस्टिंग के लिए; प्रोडक्शन के लिए Small/Medium यूज करें)।
   - **Compute + storage**: बर्स्टेबल टियर, Standard_B1ms (1 vCore), 10 GiB स्टोरेज, 100 IOPS, 7-दिन का बैकअप। जरूरत के हिसाब से एडजस्ट करें (जैसे, माइग्रेशन के लिए IOPS बढ़ाएं)।
   - **Availability zone**: No preference (या अपने ऐप की ज़ोन से मिलाएं)।
   - **High availability**: शुरुआत के लिए Disabled (प्रोडक्शन के लिए zone-redundant enable करें)।
   - **Authentication**: MySQL और Microsoft Entra (फ्लेक्सिबिलिटी के लिए)।
   - **Admin username**: जैसे, `mydemouser` (root/admin आदि नहीं, मैक्स 32 करैक्टर)।
   - **Password**: स्ट्रॉन्ग पासवर्ड (8-128 करैक्टर, अपरकेस/लोअरकेस/नंबर/सिंबल का मिक्स)।

5. **Networking** टैब पर स्विच करें:
   - **Connectivity method**: पब्लिक एक्सेस (सरलता के लिए; प्रोडक्शन सिक्योरिटी के लिए प्राइवेट VNet)।
   - **Firewall rules**: अपना करंट क्लाइंट IP एड करें (या Azure सर्विसेज को अलाउ करें)। इसे बाद में नहीं बदल सकते।

6. **Review + create** पर सेटिंग्स रिव्यू करें, फिर **Create** पर क्लिक करें। डेप्लॉयमेंट में 5-10 मिनट लगते हैं। नोटिफिकेशन के जरिए मॉनिटर करें।

7. एक बार हो जाने पर, डैशबोर्ड पर पिन करें और रिसोर्स के **Overview** पेज पर जाएं। डिफॉल्ट डेटाबेस में `information_schema`, `mysql`, आदि शामिल हैं।

## चरण 2: अपने सर्वर से कनेक्ट करें
GUI कनेक्शन के लिए MySQL वर्कबेंच का उपयोग करें। (विकल्प: Azure Data Studio, mysql CLI, या Azure Cloud Shell।)

1. पोर्टल में, अपने सर्वर के **Overview** पर जाएं और नोट करें:
   - सर्वर नाम (जैसे, `mydemoserver.mysql.database.azure.com`)।
   - एडमिन यूजरनेम।
   - अगर जरूरत हो तो पासवर्ड रीसेट करें।

2. MySQL वर्कबेंच खोलें।

3. **New Connection** पर क्लिक करें (या मौजूदा को एडिट करें)।

4. **Parameters** टैब में:
   - **Connection Name**: जैसे, `Demo Connection`।
   - **Connection Method**: Standard (TCP/IP)।
   - **Hostname**: पूरा सर्वर नाम।
   - **Port**: 3306।
   - **Username**: एडमिन यूजरनेम।
   - **Password**: एंटर करें और वॉल्ट में स्टोर करें।

5. **Test Connection** पर क्लिक करें। अगर फेल होता है:
   - पोर्टल से डिटेल्स वेरिफाई करें।
   - सुनिश्चित करें कि फायरवॉल आपके IP को अलाउ करता है।
   - TLS/SSL एनफोर्स है (TLS 1.2); अगर जरूरत हो तो [DigiCert](https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem) से CA सर्ट डाउनलोड करें और वर्कबेंच में बाइंड करें (SSL टैब के अंदर: Use SSL > Require और CA फाइल स्पेसिफाई करें)।

6. सेव करने के लिए **OK** पर क्लिक करें। क्वेरी एडिटर खोलने के लिए कनेक्शन टाइल पर डबल-क्लिक करें।

## चरण 3: डेटाबेस बनाएं और मैनेज करें
एक बार कनेक्ट हो जाने पर, पोर्टल या क्लाइंट के जरिए डेटाबेस मैनेज करें।

### Azure पोर्टल के माध्यम से:
1. अपने सर्वर के पेज पर, लेफ्ट मेन्यू से **Databases** सेलेक्ट करें।
2. **+ Add** पर क्लिक करें:
   - **Database name**: जैसे, `testdb`।
   - **Charset**: utf8 (डिफॉल्ट)।
   - **Collation**: utf8_general_ci।
3. **Save** पर क्लिक करें।

डिलीट करने के लिए: डेटाबेस सेलेक्ट करें, **Delete** पर क्लिक करें।

### MySQL वर्कबेंच के माध्यम से (SQL क्वेरीज):
क्वेरी एडिटर में इन्हें रन करें:

- डेटाबेस बनाएं: `CREATE DATABASE testdb CHARACTER SET utf8 COLLATE utf8_general_ci;`
- डेटाबेस लिस्ट करें: `SHOW DATABASES;`
- डेटाबेस यूज करें: `USE testdb;`
- टेबल बनाएं: `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));`
- डेटा इन्सर्ट करें: `INSERT INTO users (name) VALUES ('Alice');`
- क्वेरी: `SELECT * FROM users;`

अगर ऑटो-कमिट नहीं हो रहा है तो `COMMIT;` के साथ चेंजेज कमिट करें।

## बेसिक यूज टिप्स
- **स्केलिंग**: **Overview** > **Compute + storage** से, vCores/स्टोरेज/IOPS एडजस्ट करें (ज्यादातर चेंजेज के लिए कोई डाउनटाइम नहीं)।
- **बैकअप**: ऑटोमेटेड डेली; पॉइंट-इन-टाइम रिस्टोर 35 दिनों तक (**Backup** सेटिंग्स में कॉन्फ़िगर करें)।
- **मॉनिटरिंग**: CPU/स्टोरेज इनसाइट्स के लिए **Metrics** यूज करें; अलर्ट सेट करें।
- **सिक्योरिटी**: हमेशा SSL यूज करें (एनफोर्स)। प्रोडक्शन के लिए, HA, प्राइवेट नेटवर्किंग, और Entra ID ऑथ एनेबल करें।
- **माइग्रेशन**: छोटे DBs के लिए mysqldump यूज करें; बड़े के लिए DMS।
- **कॉस्ट**: कंप्यूट/स्टोरेज के लिए पे करें; छोटे से शुरू करें और स्केल करें। कैलकुलेटर [azure.microsoft.com](https://azure.microsoft.com/pricing/calculator/) पर यूज करें।
- **क्लीनअप**: सर्वर को हटाने और चार्जेस से बचने के लिए रिसोर्स ग्रुप डिलीट करें।

रीड रेप्लिका या सर्वर पैरामीटर जैसी एडवांस्ड फीचर्स के लिए, पोर्टल के लेफ्ट मेन्यू को एक्सप्लोर करें।

## संदर्भ
- [क्विकस्टार्ट: Azure पोर्टल का उपयोग करके एक फ्लेक्सिबल सर्वर बनाएं](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal)
- [MySQL वर्कबेंच का उपयोग करके कनेक्ट करें](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [डेटाबेस बनाएं और मैनेज करें](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-create-manage-databases)
- [Azure Database for MySQL डॉक्यूमेंटेशन](https://learn.microsoft.com/en-us/azure/mysql/)