---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एज़ुर एप्लिकेशन इनसाइट्स सेटअप गाइड
translated: true
type: note
---

## Azure Application Insights क्या है?

Azure Application Insights, Azure Monitor में एक एप्लिकेशन परफॉर्मेंस मैनेजमेंट (APM) सेवा है जो आपको लाइव वेब एप्लिकेशन्स को मॉनिटर करने में मदद करती है। यह रिक्वेस्ट्स, डिपेंडेंसीज़, ट्रेस, मेट्रिक्स और लॉग्स जैसे टेलीमेट्री डेटा के माध्यम से समस्याओं का पता लगाने, समस्याओं का निदान करने और उपयोगकर्ता व्यवहार को समझने के लिए टूल्स प्रदान करती है। अब यह व्यापक संगतता के लिए OpenTelemetry द्वारा संचालित है।

## पूर्वापेक्षाएँ
- एक सक्रिय Azure सब्सक्रिप्शन।
- Azure में संसाधन बनाने की अनुमतियाँ (जैसे, Owner या Contributor भूमिका)।
- आपका एप्लिकेशन कोड (.NET, Java, Node.js, Python, और अन्य का समर्थन करता है)।

## चरण 1: एक Application Insights संसाधन बनाएँ
1. [Azure पोर्टल](https://portal.azure.com) में साइन इन करें।
2. ऊपरी-बाएँ मेनू में **Create a resource** पर क्लिक करें।
3. "Application Insights" खोजें और **Monitoring + management** के अंतर्गत परिणामों से इसे चुनें।
4. विवरण भरें:
   - **Subscription**: अपना Azure सब्सक्रिप्शन चुनें।
   - **Resource Group**: एक मौजूदा का चयन करें या एक नया बनाएँ।
   - **Name**: अपने संसाधन को एक अद्वितीय नाम दें।
   - **Region**: अपने उपयोगकर्ताओं या ऐप के निकट एक रीजन चुनें।
   - **Workspace**: वैकल्पिक रूप से एक मौजूदा Log Analytics वर्कस्पेस से लिंक करें; अन्यथा, एक नया स्वचालित रूप से बनाया जाता है।
5. समीक्षा करें और **Create** पर क्लिक करें। तैनाती में कुछ मिनट लगते हैं।
6. एक बार बन जाने पर, अपने संसाधन के **Overview** पेज पर जाएँ और **Connection string** कॉपी करें (इस पर होवर करें और कॉपी आइकन पर क्लिक करें)। यह पहचानता है कि आपका ऐप टेलीमेट्री डेटा कहाँ भेजता है।

**टिप**: डेटा को मिलाने से बचने के लिए डेव, टेस्ट और प्रोड वातावरण के लिए अलग-अलग संसाधनों का उपयोग करें।

## चरण 2: अपने एप्लिकेशन को इंस्ट्रूमेंट करें
टेलीमेट्री को स्वचालित रूप से एकत्र करने के लिए OpenTelemetry सपोर्ट जोड़ें (रिक्वेस्ट्स, एक्सेप्शन्स, मेट्रिक्स, आदि)। कनेक्शन स्ट्रिंग को `APPLICATIONINSIGHTS_CONNECTION_STRING` नामक एक एनवायरनमेंट वेरिएबल के माध्यम से सेट करें (प्रोडक्शन के लिए अनुशंसित)।

### .NET (ASP.NET Core) के लिए
1. NuGet पैकेज इंस्टॉल करें:
   ```
   dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
   ```
2. `Program.cs` में:
   ```csharp
   using Azure.Monitor.OpenTelemetry.AspNetCore;

   var builder = WebApplication.CreateBuilder(args);
   builder.Services.AddOpenTelemetry().UseAzureMonitor();
   var app = builder.Build();
   app.Run();
   ```
3. एनवायरनमेंट वेरिएबल को अपनी कनेक्शन स्ट्रिंग के साथ सेट करें और ऐप रन करें।

### Java के लिए
1. Azure Monitor OpenTelemetry Distro JAR डाउनलोड करें (जैसे, `applicationinsights-agent-3.x.x.jar`)।
2. उसी डायरेक्टरी में एक कॉन्फ़िग फ़ाइल `applicationinsights.json` बनाएँ:
   ```json
   {
     "connectionString": "Your connection string here"
   }
   ```
3. एजेंट के साथ अपना ऐप रन करें: `java -javaagent:applicationinsights-agent-3.x.x.jar -jar your-app.jar`.

### Node.js के लिए
1. पैकेज इंस्टॉल करें:
   ```
   npm install @azure/monitor-opentelemetry
   ```
2. अपने ऐप एंट्री पॉइंट में कॉन्फ़िगर करें:
   ```javascript
   const { AzureMonitorOpenTelemetry } = require('@azure/monitor-opentelemetry');
   const provider = new AzureMonitorOpenTelemetry({
     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
   });
   provider.start();
   ```
3. एनवायरनमेंट वेरिएबल सेट करें और अपना ऐप स्टार्ट करें।

### Python के लिए
1. पैकेज इंस्टॉल करें:
   ```
   pip install azure-monitor-opentelemetry
   ```
2. अपने ऐप में:
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   configure_azure_monitor(connection_string="Your connection string here")
   ```
3. ऐप रन करें।

अन्य भाषाओं या ऑटो-इंस्ट्रुमेंटेशन (जैसे, Azure App Service के लिए) के लिए, आधिकारिक डॉक्स देखें। पहले स्थानीय रूप से टेस्ट करें।

## चरण 3: डेटा देखें और विश्लेषण करें
1. अपना इंस्ट्रूमेंटेड ऐप रन करें और कुछ एक्टिविटी जनरेट करें (जैसे, रिक्वेस्ट्स भेजें)।
2. Azure पोर्टल में, अपना Application Insights संसाधन खोलें।
3. **Overview** पेज चेक करें: लाइव मेट्रिक्स, रिक्वेस्ट काउंट और रिस्पॉन्स टाइम देखें (डेटा ~1-2 मिनट में दिखाई देता है)।
4. फीचर्स एक्सप्लोर करें:
   - **Live Metrics**: प्रोडक्शन ऐप्स के लिए रीयल-टाइम स्ट्रीम।
   - **Failures**: एक्सेप्शन्स और ट्रेस में ड्रिल डाउन करें।
   - **Performance**: डिपेंडेंसीज़ और धीमी रिक्वेस्ट्स का विश्लेषण करें।
   - **Usage**: उपयोगकर्ता सत्रों और कस्टम इवेंट्स को ट्रैक करें।
   - **Alerts**: समस्याओं के लिए नोटिफिकेशन सेट करें (जैसे, उच्च विफलता दर)।
5. कस्टम विश्लेषण के लिए **Logs** में Kusto Query Language (KQL) का उपयोग करके डेटा क्वेरी करें।

## सर्वोत्तम अभ्यास
- बुनियादी टेलीमेट्री से शुरुआत करें; आवश्यकतानुसार कस्टम इवेंट/मेट्रिक्स जोड़ें।
- **Usage and estimated costs** पेज के माध्यम से लागतों की निगरानी करें (Log Analytics के माध्यम से बिल किया जाता है)।
- ब्राउज़र मॉनिटरिंग के लिए, JavaScript SDK स्निपेट को अपने वेब पेजों में जोड़ें।

[Application Insights संसाधन बनाएँ और कॉन्फ़िगर करें](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource)  
[Application Insights में OpenTelemetry सक्षम करें](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)  
[Application Insights अवलोकन](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)