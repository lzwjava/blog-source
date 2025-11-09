---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एडब्ल्यूएस क्लाउडवॉच लॉग्स पढ़ना
translated: true
type: note
---

### AWS CloudWatch में रीडिंग लॉग्स का परिचय
AWS CloudWatch Logs एक ऐसी सेवा है जो आपके AWS संसाधनों (जैसे EC2 इंस्टेंस, Lambda फंक्शन, या RDS डेटाबेस) और एप्लिकेशन से लॉग फाइलों को केंद्रीकृत, मॉनिटर और स्टोर करती है। लॉग पढ़ने के लिए, सबसे पहले यह सुनिश्चित करें कि लॉग CloudWatch में भेजे जा रहे हैं (उदाहरण के लिए, EC2 पर CloudWatch एजेंट के माध्यम से या अन्य सेवाओं के साथ स्वचालित एकीकरण)। एक बार सेटअप हो जाने के बाद, आप AWS Management Console, AWS CLI, या SDK के माध्यम से प्रोग्रामेटिक रूप से लॉग देख सकते हैं।

### पूर्वापेक्षाएँ
- **AWS अनुमतियाँ**: सुनिश्चित करें कि आपके IAM उपयोगकर्ता या भूमिका के पास `logs:DescribeLogGroups`, `logs:DescribeLogStreams`, `logs:GetLogEvents`, और `logs:FilterLogEvents` अनुमतियाँ हैं (`CloudWatchLogsReadOnlyAccess` पॉलिसी संलग्न करें)।
- **लॉग्स कॉन्फ़िगरेशन**: लॉग्स को CloudWatch में रूट किया जाना चाहिए। उदाहरण के लिए:
  - EC2 इंस्टेंस पर CloudWatch Logs एजेंट इंस्टॉल करें।
  - Lambda या ECS जैसी सेवाओं में लॉगिंग सक्षम करें।
- **AWS CLI (वैकल्पिक)**: यदि CLI का उपयोग कर रहे हैं, तो इसे `aws configure` के साथ इंस्टॉल और कॉन्फ़िगर करें।

### AWS Management Console में लॉग देखना
1. [AWS Management Console](https://console.aws.amazon.com/) में साइन इन करें और CloudWatch सेवा खोलें।
2. बाएं नेविगेशन पेन में, **Logs** > **Log groups** चुनें।
3. अपने लॉग वाले लॉग ग्रुप का चयन करें (उदाहरण के लिए, Lambda लॉग के लिए `/aws/lambda/my-function`)।
4. लॉग स्ट्रीम की सूची में (चयनित लॉग ग्रुप के अंतर्गत), विशिष्ट स्ट्रीम चुनें (उदाहरण के लिए, प्रति इंस्टेंस या एक्सेक्यूशन)।
5. लॉग इवेंट लोड हो जाएंगे। दृश्य को अनुकूलित करें:
   - **इवेंट्स विस्तारित करें**: किसी इवेंट के आगे तीर पर क्लिक करके उसे विस्तारित करें, या सादे टेक्स्ट के लिए सूची के ऊपर **Text** व्यू पर स्विच करें।
   - **फ़िल्टर/खोज**: खोज बॉक्स में एक फ़िल्टर दर्ज करें (उदाहरण के लिए, केवल त्रुटि पंक्तियाँ दिखाने के लिए "ERROR")।
   - **समय सीमा**: खोज बॉक्स के बगल में समय चयनकर्ता पर क्लिक करें। **Relative** (उदाहरण के लिए, पिछला 1 घंटा) या **Absolute** (कस्टम तिथियाँ) चुनें, और UTC और स्थानीय समय के बीच टॉगल करें।
6. इवेंट्स के माध्यम से स्क्रॉल करें या आवश्यकतानुसार उन्हें डाउनलोड करें।

एकाधिक स्ट्रीम या ग्रुप में उन्नत क्वेरी के लिए, **CloudWatch Logs Insights** (Logs > Logs Insights के अंतर्गत) का उपयोग करें। लॉग का विश्लेषण और विज़ुअलाइज़ेशन करने के लिए `fields @timestamp, @message | filter @level = "ERROR" | sort @timestamp desc` जैसे क्वेरी लिखें।

### AWS CLI का उपयोग करके लॉग पढ़ना
लॉग्स को प्रोग्रामेटिक रूप से सूचीबद्ध करने और पुनर्प्राप्त करने के लिए इन कमांडों का उपयोग करें। प्लेसहोल्डर्स जैसे `my-log-group` को अपने वास्तविक नामों से बदलें।

1. **लॉग ग्रुप सूचीबद्ध करें**:
   ```
   aws logs describe-log-groups --log-group-name-prefix my-log-group
   ```
   यह ARN, रिटेंशन, और संग्रहीत बाइट्स जैसे मेटाडेटा लौटाता है।

2. **एक ग्रुप में लॉग स्ट्रीम सूचीबद्ध करें**:
   ```
   aws logs describe-log-streams --log-group-name my-log-group --log-stream-name-prefix 2025
   ```
   उपसर्ग (जैसे, तिथि-आधारित नाम) द्वारा स्ट्रीम को फ़िल्टर करता है और निर्माण समय और आकार दिखाता है।

3. **एक स्ट्रीम से लॉग इवेंट प्राप्त करें**:
   ```
   aws logs get-log-events --log-group-name my-log-group --log-stream-name my-stream --start-time 1730137600000
   ```
   - `--start-time` और `--end-time`: समय सीमा के लिए यूनिक्स टाइमस्टैम्प (मिलीसेकंड)।
   - `--limit`: लौटाए जाने वाले अधिकतम इवेंट (डिफ़ॉल्ट 1,000)।
   - आउटपुट में टाइमस्टैम्प, इन्जेस्शन समय और संदेश टेक्स्ट शामिल होते हैं।
   - पेजिनेट करने के लिए प्रतिक्रिया से `--next-token` का उपयोग करें।

स्ट्रीम में फ़िल्टर्ड खोज के लिए, `filter-log-events` का उपयोग करें:
```
aws logs filter-log-events --log-group-name my-log-group --filter-pattern "ERROR" --start-time 1730137600000
```

### सुझाव और सर्वोत्तम अभ्यास
- **रिटेंशन**: लॉग डिफ़ॉल्ट रूप से अनिश्चित काल तक रखे जाते हैं; लागत प्रबंधित करने के लिए प्रति ग्रुप समायोजित करें (उदाहरण के लिए, 30 दिन)।
- **लागत**: देखना मुफ़्त है, लेकिन इन्जेस्शन और स्टोरेज पर शुल्क लगते हैं—CloudWatch मेट्रिक्स के माध्यम से मॉनिटर करें।
- **समस्या निवारण**: यदि कोई लॉग दिखाई नहीं देते हैं, तो एजेंट इंस्टॉलेशन या सेवा लॉगिंग सक्षम होना सत्यापित करें।
- रीयल-टाइम मॉनिटरिंग के लिए, लॉग पैटर्न पर मेट्रिक फ़िल्टर या अलार्म सेटअप करें।

[लॉग ग्रुप और लॉग स्ट्रीम के साथ कार्य - Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)  
[AWS CLI का उपयोग करके CloudWatch Logs उदाहरण](https://docs.aws.amazon.com/cli/v1/userguide/cli_cloudwatch-logs_code_examples.html)  
[CloudWatch Logs Insights के साथ लॉग डेटा का विश्लेषण](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)