---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: Amazon आरडीएस फॉर MySQL का उपयोग
translated: true
type: note
---

Amazon RDS (Relational Database Service) for MySQL एक managed database service है जो cloud में MySQL databases को सेट अप, operate और scale करना आसान बनाती है। यह backups, patching, और scaling जैसे routine tasks को संभालती है, ताकि आप अपने application पर ध्यान केंद्रित कर सकें। यह guide आपको मूल बातों से गुजारेगी: एक MySQL DB instance बनाना, उससे कनेक्ट करना, और सरल operations perform करना। सरलता के लिए हम AWS Management Console का उपयोग करेंगे।

**लागत पर ध्यान दें:** AWS Free Tier नए अकाउंट्स के लिए सीमित उपयोग प्रदान करता है, लेकिन उससे अधिक resources के लिए आपसे शुल्क लिया जाएगा। अप्रत्याशित बिलों से बचने के लिए काम पूरा होने पर resources को हमेशा delete कर दें। Production के लिए, security best practices का पालन करें जैसे VPCs, encryption, और least-privilege access का उपयोग करना।

## पूर्वापेक्षाएँ
- एक AWS अकाउंट (यदि आवश्यक हो तो [aws.amazon.com](https://aws.amazon.com) पर साइन अप करें)।
- AWS console और MySQL से बुनियादी परिचय।
- secure connection testing के लिए, हम एक EC2 instance उसी VPC (Virtual Private Cloud) में बनाएँगे। SSH access के लिए अपने public IP address का पता लगाएँ (उदाहरण के लिए, [checkip.amazonaws.com](https://checkip.amazonaws.com) के माध्यम से)।
- अपने नज़दीकी एक AWS Region चुनें (उदाहरण के लिए, US East (N. Virginia))।

**बेस्ट प्रैक्टिस:** विश्वसनीय resources तक ही access को प्रतिबंधित करने के लिए एक private DB instance का VPC में उपयोग करें। encrypted connections के लिए SSL/TLS enable करें।

## चरण 1: कनेक्शन के लिए एक EC2 Instance बनाएँ
यह आपके private DB instance से कनेक्ट होने के लिए एक साधारण Linux server सेट अप करता है।

1. [AWS Management Console](https://console.aws.amazon.com) में साइन इन करें और EC2 console खोलें।
2. अपना Region select करें।
3. **Launch instance** पर क्लिक करें।
4. कॉन्फ़िगर करें:
   - **Name:** `ec2-database-connect`.
   - **AMI:** Amazon Linux 2023 (free tier eligible).
   - **Instance type:** t3.micro (free tier eligible).
   - **Key pair:** SSH access के लिए एक नया बनाएँ या मौजूदा एक को select करें।
   - **Network settings:** Edit > SSH traffic को **My IP** से allow करें (या आपका specific IP, उदाहरण के लिए, `192.0.2.1/32`). सुरक्षा के लिए `0.0.0.0/0` से बचें।
   - storage और tags के लिए defaults को छोड़ दें।
5. **Launch instance** पर क्लिक करें।
6. Instance details से instance ID, Public IPv4 DNS, और key pair name नोट कर लें।
7. status के **Running** (2-5 मिनट) दिखने तक प्रतीक्षा करें।

**सुरक्षा टिप:** SSH को केवल अपने IP तक ही सीमित रखें। key pair (.pem file) को सुरक्षित रूप से डाउनलोड करें।

## चरण 2: एक MySQL DB Instance बनाएँ
त्वरित सेटअप के लिए "Easy create" का उपयोग करें।

1. [RDS console](https://console.aws.amazon.com/rds/) खोलें।
2. अपने EC2 instance के समान ही Region select करें।
3. navigation pane में, **Databases** > **Create database** पर क्लिक करें।
4. **Easy create** select करें।
5. **Configuration** के अंतर्गत:
   - Engine type: **MySQL**.
   - Templates: **Free tier** (या paid accounts के लिए **Sandbox**)।
   - DB instance identifier: `database-test1` (या आपकी पसंद)।
   - Master username: `admin` (या custom)।
   - Master password: Auto-generate करें या एक मजबूत पासवर्ड सेट करें (इसे सुरक्षित रूप से रिकॉर्ड कर लें)।
6. (वैकल्पिक) **Connectivity** के अंतर्गत, **Connect to an EC2 compute resource** select करें और आसान सेटअप के लिए अपना EC2 instance चुनें।
7. **Create database** पर क्लिक करें।
8. credentials popup (username/password) देखें—उन्हें सहेज लें, क्योंकि password बाद में पुनः प्राप्त नहीं किया जा सकता है।
9. status के **Available** (10-20 मिनट तक) में बदलने तक प्रतीक्षा करें। **Connectivity & security** टैब से **Endpoint** (DNS name) और port (default: 3306) नोट कर लें।

**बेस्ट प्रैक्टिस:** Production के लिए, VPC, backups (automated enable करें), और storage को customize करने के लिए "Standard create" का उपयोग करें। high availability के लिए deletion protection और multi-AZ enable करें।

## चरण 3: DB Instance से कनेक्ट करें
MySQL client का उपयोग करके अपने EC2 instance से कनेक्ट करें।

1. अपने EC2 instance में SSH करें:
   ```
   ssh -i /path/to/your-key-pair.pem ec2-user@your-ec2-public-dns
   ```
   (अपने विवरणों से बदलें; उदाहरण के लिए, `ssh -i ec2-database-connect-key-pair.pem ec2-user@ec2-12-345-678-90.compute-1.amazonaws.com`.)

2. EC2 instance पर, packages update करें:
   ```
   sudo dnf update -y
   ```

3. MySQL client इंस्टॉल करें:
   ```
   sudo dnf install mariadb105 -y
   ```

4. DB से कनेक्ट करें:
   ```
   mysql -h your-db-endpoint -P 3306 -u admin -p
   ```
   prompt होने पर master password दर्ज करें।

यदि सफल हुआ, तो आप MySQL prompt (`mysql>`) देखेंगे।

**समस्या निवारण:** सुनिश्चित करें कि security groups EC2 instance से port 3306 पर inbound traffic allow करती हैं। external connections के लिए, DB को public बनाएँ (अनुशंसित नहीं) या bastion hosts/VPN का उपयोग करें।

**सुरक्षा टिप:** encrypted connections के लिए `--ssl-mode=REQUIRED` का उपयोग करें: `mysql -h endpoint -P 3306 -u admin -p --ssl-mode=REQUIRED`.

## चरण 4: बेसिक उपयोग
एक बार कनेक्ट हो जाने पर, आप SQL commands चला सकते हैं। उदाहरण:

- Databases दिखाएँ: `SHOW DATABASES;`
- एक sample database बनाएँ: `CREATE DATABASE myapp;`
- इसका उपयोग करें: `USE myapp;`
- एक टेबल बनाएँ:
  ```
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
  );
  ```
- डेटा insert करें: `INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');`
- Query करें: `SELECT * FROM users;`
- बाहर निकलें: `EXIT;`

Applications (उदाहरण के लिए, Python, Node.js) से, connection strings के रूप में endpoint, port, username, और password के साथ standard MySQL drivers का उपयोग करें।

**बेस्ट प्रैक्टिस:** CloudWatch के माध्यम से performance monitor करें, automated backups enable करें, और आवश्यकतानुसार vertically (instance size) या horizontally (read replicas) scale करें।

## क्लीनअप: Resources Delete करें
शुल्क रोकने के लिए:

1. **EC2 instance delete करें:** EC2 console > Instance select करें > **Instance state** > **Terminate** > Confirm करें।
2. **DB instance delete करें:** RDS console > DB select करें > **Actions** > **Delete** > snapshot creation uncheck करें > Confirm करें।

किसी भी चल रहे resource के लिए AWS Billing console जांचें।

Migrations, performance tuning, या API/CLI usage जैसे अधिक उन्नत विषयों के लिए, AWS documentation देखें।

## संदर्भ
- [Creating and connecting to a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)
- [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
- [Getting started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)