---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: AWS लैम्ब्डा के साथ आरंभ करना
translated: true
type: note
---

### AWS Lambda के साथ शुरुआत करना

AWS Lambda एक सर्वरलेस कंप्यूट सर्विस है जो इवेंट्स के जवाब में बिना सर्वर मैनेज किए आपका कोड चलाती है। यहां आपके पहले Lambda फंक्शन को बनाने, डिप्लॉय करने और उपयोग करने के लिए एक शुरुआत-अनुकूल चरण-दर-चरण गाइड दी गई है। यह आधिकारिक AWS डॉक्यूमेंटेशन पर आधारित है।

#### आवश्यक शर्तें
- एक सक्रिय AWS अकाउंट। अगर आपके पास नहीं है तो [aws.amazon.com](https://aws.amazon.com/) पर साइन अप करें।
- Node.js या Python जैसी प्रोग्रामिंग भाषा से बुनियादी परिचितता (Lambda कई रनटाइम्स को सपोर्ट करती है)।

#### चरण 1: एक Lambda फंक्शन बनाएं
1. AWS मैनेजमेंट कंसोल में लॉग इन करें और Lambda सर्विस पर नेविगेट करें (सर्विसेज मेन्यू में "Lambda" सर्च करें)।
2. फंक्शंस पेज पर, **Create function** पर क्लिक करें।
3. **Author from scratch** चुनें।
4. एक **Function name** दर्ज करें (जैसे, `my-first-function`)।
5. एक **Runtime** चुनें (जैसे, Node.js 22.x या Python 3.13)।
6. डिफ़ॉल्ट आर्किटेक्चर (x86_64) को यथावत छोड़ दें और **Create function** पर क्लिक करें।

यह स्वचालित रूप से एक एक्जिक्यूशन रोल (एक IAM रोल) बना देगा, जिसमें Amazon CloudWatch में लॉग लिखने जैसे बेसिक परमिशन होंगे।

#### चरण 2: अपना कोड लिखें
Lambda कंसोल के कोड एडिटर (**Code** टैब के अंदर) में, डिफ़ॉल्ट "Hello World" कोड को कुछ सरल से बदलें। यहां एक उदाहरण दिया गया है जो `length` और `width` की वाली JSON इनपुट के आधार पर आयत के क्षेत्रफल की गणना करता है।

- **Node.js उदाहरण**:
  ```javascript
  exports.handler = async (event) => {
    const length = event.length;
    const width = event.width;
    const area = length * width;
    console.log(`The area is ${area}`);
    console.log('Log group: /aws/lambda/' + process.env.AWS_LAMBDA_FUNCTION_NAME);
    return { area: area };
  };
  ```

- **Python उदाहरण**:
  ```python
  import json

  def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = length * width
    print(f"The area is {area}")
    print(f"Log group: /aws/lambda/{context.function_name}")
    return {
        'statusCode': 200,
        'body': json.dumps({'area': area})
    }
  ```

बदलावों को सेव करें—इंटरप्रेटेड भाषाओं के लिए डिप्लॉयमेंट स्वचालित रूप से हो जाता है।

कंपाइल्ड भाषाओं (जैसे, Java) के लिए, स्थानीय रूप से एक डिप्लॉयमेंट पैकेज बनाएं और उसे कंसोल या AWS CLI के माध्यम से अपलोड करें।

#### चरण 3: अपने फंक्शन को टेस्ट करें
1. **Test** टैब में, **Create new test event** पर क्लिक करें।
2. इसका एक नाम दें (जैसे, `test-area-calc`)।
3. सैंपल JSON इनपुट पेस्ट करें:
   ```json
   {
     "length": 6,
     "width": 7
   }
   ```
4. सेव करें और **Test** पर क्लिक करें।

परिणाम **Execution results** सेक्शन में देखें (जैसे, `{"area": 42}`)। अवधि और मेमोरी उपयोग जैसे विवरणों के लिए CloudWatch में लॉग्स चेक करें।

#### चरण 4: इनवोक करें और मॉनिटर करें
- **मैन्युअल इनवोकेशन**: कंसोल के Test बटन का उपयोग करें या AWS CLI: `aws lambda invoke --function-name my-first-function output.json`।
- **इवेंट-ड्रिवन इनवोकेशन**: API Gateway, S3 बकेट्स, या DynamoDB स्ट्रीम्स जैसे ट्रिगर्स को कनेक्ट करें। उन्हें जोड़ने के लिए **Configuration** > **Triggers** टैब पर जाएं।
- **लॉग्स**: स्वचालित रूप से CloudWatch Logs पर भेजे जात