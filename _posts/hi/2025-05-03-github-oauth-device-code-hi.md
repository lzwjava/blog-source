---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: GitHub OAuth डिवाइस कोड फ्लो
translated: true
type: note
---

### अवलोकन

यह JavaScript कोड GitHub के साथ प्रमाणीकरण करने और एक एक्सेस टोकन प्राप्त करने के लिए OAuth 2.0 डिवाइस ऑथराइजेशन ग्रांट फ्लो (जिसे डिवाइस कोड ग्रांट भी कहा जाता है) को लागू करता है। इस फ्लो का उपयोग आमतौर पर ऐसे हेडलेस एप्लिकेशन (जैसे, CLI टूल या एम्बेडेड सिस्टम) के लिए किया जाता है जहां उपयोगकर्ता प्रमाणीकरण को मंजूरी देने के लिए सीधे वेब ब्राउज़र के साथ इंटरैक्ट नहीं कर सकता है।

इस विशिष्ट मामले में, यह GitHub Copilot प्लगइन (उदाहरण के लिए, Neovim या Vim के लिए) के अनुरोधों की नकल करता प्रतीत होता है, ऐसे हेडर्स का उपयोग करते हुए जो एक Copilot क्लाइंट को स्पूफ करते हैं, संभवतः GitHub की प्रमाणीकरण प्रणाली के साथ एकीकृत होने या उस तक पहुंचने के लिए। लक्ष्य एक ऐसा एक्सेस टोकन जनरेट करना है जिसका उपयोग GitHub API कॉल के लिए किया जा सके जिसमें उपयोगकर्ता प्रमाणीकरण की आवश्यकता होती है, जैसे कि उपयोगकर्ता जानकारी पढ़ना (`scope: "read:user"` के अनुसार)।

यह कोड एक Node.js स्क्रिप्ट के रूप में चलता है, जो HTTP अनुरोधों के लिए `fetch` और पर्यावरण चर के लिए `process` का उपयोग करता है। यह मानता है कि Node.js में `fetch` उपलब्ध है (जैसा कि नए संस्करणों में या पॉलीफिल के माध्यम से होता है)। यदि सफल होता है, तो यह उपयोगकर्ता के अनुरोध को अधिकृत करने तक या टाइमआउट होने तक GitHub के सर्वर से पूछता रहता है।

**महत्वपूर्ण नोट्स:**
- इस कोड को एक पर्यावरण चर `MY_COPILOT_CLIENT_ID` सेट करने की आवश्यकता है, संभवतः GitHub Copilot के लिए पंजीकृत GitHub OAuth ऐप क्लाइंट आईडी।
- यह त्रुटियों को न्यूनतम रूप से हैंडल करता है—उदाहरण के लिए, यदि फ़ेच विफल होता है, तो यह लॉग करता है और जारी रखता है या बाहर निकल जाता है।
- सुरक्षा की दृष्टि से, एक्सेस टोकन को स्टोर करना या लॉग करना जोखिम भरा है (वे API एक्सेस प्रदान करते हैं)। यह कोड पूर्ण टोकन ऑब्जेक्ट को सीधे कंसोल पर प्रिंट कर देता है, जो वास्तविक उपयोग में गोपनीयता/सुरक्षा का मुद्दा हो सकता है। एक्सेस टोकन को सुरक्षित रूप से हैंडल किया जाना चाहिए (उदाहरण के लिए, एन्क्रिप्टेड स्टोर किया जाना चाहिए और रोटेट किया जाना चाहिए)।
- इस फ्लो में उपयोगकर्ता इंटरैक्शन शामिल है: उपयोगकर्ता को एक URL पर जाना होगा और अधिकृत करने के लिए GitHub की साइट पर एक कोड दर्ज करना होगा।
- यह "आधिकारिक" GitHub डॉक्यूमेंटेशन कोड नहीं है; यह GitHub Copilot के व्यवहार से रिवर्स-इंजीनियर किया गया प्रतीत होता है। API का उपयोग जिम्मेदारी से और GitHub की सेवा की शर्तों के अनुसार करें।

### चरण-दर-चरण विवरण

#### 1. पर्यावरण जांच
```javascript
const clientId = process.env.MY_COPILOT_CLIENT_ID;

if (!clientId) {
  console.error("MY_COPILOT_CLIENT_ID is not set");
  process.exit(1);
}
```
- पर्यावरण चर से `MY_COPILOT_CLIENT_ID` प्राप्त करता है (उदाहरण के लिए, आपके शेल में `export MY_COPILOT_CLIENT_ID=your_client_id` के माध्यम से सेट किया गया)।
- यदि सेट नहीं है, तो यह एक त्रुटि लॉग करता है और स्क्रिप्ट को समाप्त कर देता है (प्रक्रिया कोड 1 विफलता को इंगित करता है)।
- यह क्लाइंट आईडी एक पंजीकृत GitHub OAuth ऐप से है (OAuth फ्लो के लिए आवश्यक)।

#### 2. सामान्य हेडर्स सेटअप
```javascript
const commonHeaders = new Headers();
commonHeaders.append("accept", "application/json");
commonHeaders.append("editor-version", "Neovim/0.6.1");
commonHeaders.append("editor-plugin-version", "copilot.vim/1.16.0");
commonHeaders.append("content-type", "application/json");
commonHeaders.append("user-agent", "GithubCopilot/1.155.0");
commonHeaders.append("accept-encoding", "gzip,deflate,b");
```
- HTTP अनुरोधों के लिए की-वैल्यू जोड़े के साथ एक `Headers` ऑब्जेक्ट बनाता है।
- ये हेडर्स अनुरोधों को ऐसा दिखाते हैं जैसे वे GitHub Copilot Vim प्लगइन (Neovim 0.6.1 के लिए संस्करण 1.16.0) से आ रहे हों। यह संभवतः यूजर-एजेंट को स्पूफ करने और Copilot की API कॉल्स की नकल करने के लिए है, जो GitHub के लिए अनुरोधों को स्वीकार करने के लिए आवश्यक या सहायक हो सकता है।
- `"accept": "application/json"`: JSON प्रतिक्रियाओं की अपेक्षा करता है।
- `"content-type": "application/json"`: अनुरोध बॉडी में JSON भेजता है।
- `"accept-encoding"`: बैंडविड्थ बचाने के लिए gzip/deflate कम्प्रेशन की अनुमति देता है।

#### 3. `getDeviceCode()` फ़ंक्शन
```javascript
async function getDeviceCode() {
  const raw = JSON.stringify({
    "client_id": clientId,
    "scope": "read:user",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  const data = await fetch(
    "https://github.com/login/device/code",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
  return data;
}
```
- **उद्देश्य**: GitHub से एक डिवाइस कोड का अनुरोध करके डिवाइस कोड फ्लो शुरू करता है।
- निम्नलिखित के साथ एक JSON पेलोड बनाता है:
  - `client_id`: OAuth क्लाइंट आईडी (आपके ऐप के प्रमाणीकरण के लिए)।
  - `scope`: `"read:user"`—टोकन को बुनियादी उपयोगकर्ता प्रोफ़ाइल जानकारी (जैसे, उपयोगकर्तानाम, ईमेल GitHub API के माध्यम से) पढ़ने तक सीमित करता है। यह एक न्यूनतम स्कोप है।
- `https://github.com/login/device/code` (GitHub का OAuth डिवाइस कोड एंडपॉइंट) पर एक POST अनुरोध करता है।
- JSON प्रतिक्रिया को पार्स करता है (अपेक्षित फ़ील्ड: `device_code`, `user_code`, `verification_uri`, `expires_in`—कोड में नहीं दिखाया गया, लेकिन इस फ्लो के लिए मानक)।
- त्रुटि पर (जैसे, नेटवर्क समस्याएं), उसे लॉग करता है लेकिन जारी रखता है (`undefined` लौटा सकता है)।
- GitHub से पार्स किए गए JSON डेटा ऑब्जेक्ट को लौटाता है।

#### 4. `getAccessToken(deviceCode: string)` फ़ंक्शन
```javascript
async function getAccessToken(deviceCode: string) {
  const raw = JSON.stringify({
    "client_id": clientId,
    "device_code": deviceCode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  return await fetch(
    "https://github.com/login/oauth/access_token",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
}
```
- **उद्देश्य**: एक बार उपयोगकर्ता द्वारा अधिकृत करने के बाद डिवाइस कोड को एक्सेस टोकन के लिए एक्सचेंज करने के लिए GitHub से पूछता है।
- पिछले चरण से `device_code` लेता है।
- निम्नलिखित के साथ JSON बनाता है:
  - `client_id`: पहले की तरह ही।
  - `device_code`: इस डिवाइस/प्रमाणीकरण प्रयास की पहचान करने वाला अद्वितीय कोड।
  - `grant_type`: निर्दिष्ट करता है कि यह एक डिवाइस कोड ग्रांट है (मानक OAuth2 URN)।
- `https://github.com/login/oauth/access_token` पर एक POST अनुरोध करता है।
- पार्स की गई JSON प्रतिक्रिया लौटाता है, जो हो सकती है:
  - सफलता पर: `{ access_token: "...", token_type: "bearer", scope: "read:user" }`।
  - लंबित/त्रुटि पर: `{ error: "...", error_description: "..." }` (जैसे, "authorization_pending" या "slow_down")।
- त्रुटियाँ (जैसे, फ़ेच विफलताएँ) लॉग की जाती हैं लेकिन स्पष्ट रूप से हैंडल नहीं की जाती हैं, इसलिए कॉलर को रिटर्न वैल्यू की जांच करनी चाहिए।

#### 5. मुख्य निष्पादन (तुरंत लागू किया गया Async फ़ंक्शन)
```javascript
(async function () {
  const { device_code, user_code, verification_uri, expires_in } =
    await getDeviceCode();
  console.info(`enter user code:\n${user_code}\n${verification_uri}`);
  console.info(`Expires in ${expires_in} seconds`);
  while (true) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const accessToken = await getAccessToken(device_code);
    if (accessToken.error) {
      console.info(`${accessToken.error}: ${accessToken.error_description}`);
    }
    if (accessToken.access_token) {
      console.info(`access token:\n${JSON.stringify(accessToken, null, 1)}`);
      break;
    }
  }
})();
```
- **समग्र फ्लो**: पूर्ण OAuth 2.0 डिवाइस कोड ग्रांट को ऑर्केस्ट्रेट करता है।
- `getDeviceCode()` को कॉल करता है और प्रतिक्रिया को वेरिएबल्स में डिस्ट्रक्चर करता है (मानता है कि यह सफल होता है और इसमें ये गुण हैं)।
- उपयोगकर्ता के लिए निर्देश लॉग करता है:
  - `user_code`: एक छोटा अल्फ़ान्यूमेरिक कोड (जैसे, "ABCD-EFGH")।
  - `verification_uri`: आमतौर पर `https://github.com/login/device`, जहां उपयोगकर्ता प्रमाणीकरण करता है।
  - `expires_in`: कोड के समाप्त होने तक का सेकंड में समय (जैसे, 15 मिनट के लिए 900)।
- उपयोगकर्ता को URL पर जाना होगा, GitHub में साइन इन करना होगा, और ऐप को अधिकृत करने के लिए उपयोगकर्ता कोड दर्ज करना होगा।
- टोकन के लिए पूछताछ करने के लिए एक अनंत लूप में प्रवेश करता है:
  - प्रयासों के बीच 5 सेकंड प्रतीक्षा करता है (पोलिंग अंतराल; GitHub बहुत बार-बार अनुरोधों के लिए slow_down की सिफारिश करता है)।
  - `getAccessToken(device_code)` को कॉल करता है।
  - यदि प्रतिक्रिया में `error` है: इसे लॉग करता है (जैसे, यदि "authorization_pending" है तो प्रतीक्षा करता रहता है)।
  - यदि इसमें `access_token` है: पूर्ण टोकन ऑब्जेक्ट को लॉग करता है (इंडेंटेशन के साथ फॉर्मेट किया गया) और लूप से बाहर निकल जाता है।
- **एज केस/समस्याएं**:
  - यदि `getDeviceCode()` विफल होता है, तो डिस्ट्रक्चरिंग त्रुटि दे सकता है (कोड इसकी जांच नहीं करता)।
  - कोई लूप टाइमआउट नहीं—एक्सेस टोकन प्राप्त होने तक या स्क्रिप्ट क्रैश होने तक अनिश्चित काल तक पोलिंग करता रहता है।
  - एक्सेस टोकन को कंसोल पर लॉग करने से उसे उजागर किया जाता है; प्रोडक्शन में, आप इसे सुरक्षित रूप से सेव करेंगे (जैसे, किसी फ़ाइल या डेटाबेस में)।

### यह एंड-टू-एंड कैसे काम करता है
1. **चरण 1: डिवाइस कोड का अनुरोध करें** → स्क्रिप्ट GitHub से एक अस्थायी कोड प्राप्त करती है।
2. **चरण 2: उपयोगकर्ता प्राधिकरण** → उपयोगकर्ता GitHub पर जाता है और अनुमति देने के लिए कोड दर्ज करता है।
3. **चरण 3: टोकन के लिए पोल करें** → स्क्रिप्ट टोकन जारी होने तक GitHub से पूछती रहती है।
4. **परिणाम**: निर्दिष्ट स्कोप (जैसे, GitHub API के माध्यम से उपयोगकर्ता डेटा पढ़ना) के लिए एक एक्सेस टोकन।

यह एक सिमुलेशन है कि कैसे GitHub CLI जैसे टूल काम कर सकते हैं, जिसे Copilot के लिए अनुकूलित किया गया है। आधिकारिक GitHub OAuth दस्तावेज़ के लिए, https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow देखें। यदि आप कुछ इसी तरह का निर्माण कर रहे हैं, तो OAuth मानकों और GitHub की नीतियों का अनुपालन सुनिश्चित करें। यदि इसे संशोधित करने या चलाने के बारे में आपके कोई प्रश्न हैं, तो मुझे बताएं!