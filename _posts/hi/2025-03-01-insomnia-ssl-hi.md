---
audio: true
generated: true
lang: hi
layout: post
title: SSL सर्टिफिकेट वैलिडेशन इन इंसोम्निया
translated: true
---

इस "SSL peer certificate या SSH remote key was not OK" error को Insomnia में ठीक करने के लिए, यह error आमतौर पर तब होता है जब Insomnia उस server के SSL certificate को verify नहीं कर पata है जिससे आप connect करना चाहते हैं। नीचे दिए गए हैं इस issue को resolve करने के लिए step-by-step solutions:

### 1. **Disable SSL Certificate Validation (For Local Development Only)**
अगर आप एक local development server के साथ काम कर रहे हैं जो एक self-signed या invalid SSL certificate use करता है, तो आप Insomnia में certificate validation disable कर सकते हैं:
- Insomnia खोलें और **Application** > **Preferences** पर जाएँ.
- **Request / Response** section पर जाएँ.
- **Validate certificates** के box को uncheck करें.
- अपने request को फिर से try करें.

**Important**: यह option security checks को bypass करता hai aur **only testing या local development के लिए use किया जाना चाहिए**. production environments के लिए इसे use नहीं करें, क्योंकि यह आपके connection ko vulnerable बनata hai.

---

### 2. **Verify the Server’s SSL Certificate**
इस error में server के SSL certificate (e.g., expired, self-signed, या hostname mismatch) का issue हो सकता है। check करने ke liye:
- server के URL ko एक web browser mein open करें.
- address bar mein padlock icon par click करें certificate details ko view karne ke liye.
- ensure karein ki certificate valid hai, expired nahi hai, aur domain name ke saath match karta hai.
- अगर certificate invalid ya misconfigured hai, तो server administrator ko contact karein usse fix karne ke liye.

---

### 3. **Import a Client Certificate (If Required)**
अगर server ke liye authentication ke liye एक client certificate required hai, तो Insomnia mein usse configure karna padega:
- Insomnia mein **Client Certificates** par जाएँ (main dashboard ya preferences se accessible).
- **Add Certificate** par click करें.
- apna certificate file import karein (supported formats mein PFX ya PEM shamil hain).
- usse specific domain ya hostname ko assign karein jahan aap connect kar rahe hain.
- request ko phir se test karein.

---

### 4. **Update Insomnia**
SSL-related issues ka karan ek older version of Insomnia mein ek bug ho sakta hai. ensure karne ke liye ki aap latest version par hain:
- **Application** > **About** mein updates check karein ya official Insomnia website se latest release download karein.
- update install karein aur apna request phir se try karein.

---

### 5. **Test with Curl**
अगर उपर दिए गए steps se issue resolve nahi hota, तो request ko Insomnia ke bahar test karein problem ko isolate karne ke liye:
- एक terminal open karein aur `curl` command use karein same URL aur parameters ke saath (e.g., `curl -v https://example.com`).
- अगर `curl` bhi fail hota hai, तो issue likely server ke configuration ke saath hai rather than Insomnia.
- अगर `curl` succeed karta hai, तो yeh indicate kar sakta hai ki ek specific problem Insomnia ke saath hai, aur aap isse unke support team ko report kar sakte hain.

---

### Summary
शुरू करने के लिए, अगर यह एक local server है, तो SSL validation disable karein, फिर server ke certificate ko verify karein ya agar required hai to client certificate configure karein. ensure karein ki Insomnia up to date hai, aur `curl` ko troubleshoot ke liye use karein agar zaroorat ho. इन steps se most cases of the "SSL peer certificate या SSH remote key was not OK" error resolve hone chahiye.

अगर issue persist karta hai, तो यह server-side misconfiguration ya Insomnia mein ek rare bug ka karan ho sakta hai. अगर aapko aur madad chahiye, तो मुझे bataye!