---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ओपनडब्ल्यूआरटी को वायरलेस ब्रिज के रूप में कॉन्फ़िगर करना
translated: true
type: note
---

Grok की मदद से, मैं अभी भी निम्नलिखित पर काम करने की कोशिश कर रहा हूँ।

---

आपके OpenWRT को wireless bridge के रूप में configure करने के steps के बारे में आपके query, "क्या यह सही है?" को संबोधित करने और इसे प्राप्त करने के सही तरीके प्रदान करने के लिए, मैं आपके द्वारा प्रदान किए गए steps का मूल्यांकन करूंगा और OpenWRT के लिए best practices के आधार पर उन्हें परिष्कृत करूंगा। आपका लक्ष्य अपने OpenWRT router (जैसे, OpenWRT 24.10.0 के साथ Xiaomi Mi Router 4C) को एक wireless bridge के रूप में सेट करना है—मौजूदा Wi-Fi network से wirelessly एक client के रूप में जुड़ना और उस connection को अपने स्वयं के Wi-Fi access point (AP) या Ethernet ports के माध्यम से साझा करना, सभी devices को main router के समान subnet पर रखते हुए।

आपके द्वारा प्रदान किए गए steps ज्यादातर सही हैं लेकिन उचित bridging सुनिश्चित करने और IP conflicts से बचने के लिए एक महत्वपूर्ण समायोजन छूट गया है। नीचे, मैं पहले आपके configuration का आकलन करूंगा और फिर OpenWRT में wireless bridge प्राप्त करने के लिए सही, पूर्ण steps प्रस्तुत करूंगा, simple bridge method (एक ही bridge पर client + AP) का उपयोग करते हुए, जो आपके इरादे के अनुरूप है। मैं विफल होने के मामलों में `relayd` का उपयोग करने वाले एक विकल्प का संक्षेप में उल्लेख भी करूंगा, हालांकि आपका setup संभवतः सरल तरीके का समर्थन करता है।

---

### **आपके प्रदान किए गए Steps का मूल्यांन**

आपके steps का लक्ष्य है:
1. OpenWRT router को मौजूदा Wi-Fi network से client के रूप में जोड़ना।
2. एक नया Wi-Fi network प्रसारित करने के लिए एक AP सेट करना।
3. Internet को साझा करने के लिए client और AP interfaces को bridge करना।

यहाँ एक त्वरित समीक्षा है:
- **Step 1: LuCI में लॉग इन करें** - सही, web interface तक पहुँचना शुरुआती बिंदु है।
- **Step 2: Wireless Client Configure करें** - Target Wi-Fi से जुड़ना और इसे `lan` network को असाइन करना एक अच्छी शुरुआत है, लेकिन OpenWRT में default `lan` configuration (static IP, आमतौर पर 192.168.1.1) main router के साथ conflict पैदा कर सकता है यदि वह same IP का उपयोग करता है। इसके लिए समायोजन की आवश्यकता है।
- **Step 3: Wireless AP Configure करें** - एक AP सेट करना और इसे `lan` को असाइन करना bridging के लिए सही है, लेकिन यह `lan` interface के ठीक से configured होने पर निर्भर करता है।
- **Step 4: Networks को Bridge करें** - दोनों interfaces को `lan` को असाइन करना सैद्धांतिक रूप से उन्हें bridge करता है, लेकिन DHCP server को disable किए बिना या IP settings को समायोजित किए बिना, यह निर्बाध रूप से काम नहीं कर सकता है।
- **Step 5: Setup का परीक्षण करें** - परीक्षण आवश्यक है, लेकिन सफलता पहले के steps के पूरी तरह से सही होने पर निर्भर करती है।

**क्या गायब है या गलत है?**
- Default रूप से, OpenWRT की `lan` interface का एक static IP (जैसे, 192.168.1.1) होता है और एक DHCP server चलता है। यदि main router भी 192.168.1.1 है, तो यह IP conflict का कारण बनता है। आपको `lan` interface को main router से IP प्राप्त करने के लिए DHCP client mode में सेट करने और सभी devices को IP असाइन करने के लिए main router को अनुमति देने के लिए local DHCP server को disable करने की आवश्यकता है।
- Firewall zone का `lan` को असाइनमेंट सरलता के लिए ठीक है, लेकिन IP configuration महत्वपूर्ण है।

इस बात को ध्यान में रखते हुए, आपके steps "ज्यादातर सही" हैं लेकिन `lan` interface settings को समायोजित किए बिना अधूरे हैं। नीचे सही किए गए steps दिए गए हैं।

---

### **OpenWRT को Wireless Bridge के रूप में Configure करने के सही Steps (Simple Bridge Method)**

यह method आपके OpenWRT router को मौजूदा Wi-Fi network से client के रूप में जुड़ने और उस connection को अपने स्वयं के AP या Ethernet ports के माध्यम से साझा करने के लिए सेट करता है, सभी main router (जैसे, 192.168.1.x) के समान subnet पर। यहाँ बताया गया है कि इसे LuCI web interface के माध्यम से कैसे करें:

#### **पूर्वापेक्षाएँ**
- OpenWRT installed है (जैसे, Xiaomi Mi Router 4C पर version 24.10.0)।
- आपके पास main Wi-Fi network का SSID, password और encryption type (जैसे, WPA2-PSK) है।
- LuCI तक `http://192.168.1.1` (या current IP) पर पहुंच और आपके admin credentials।

#### **Step 1: LuCI में लॉग इन करें**
- एक browser खोलें और `http://192.168.1.1` पर नेविगेट करें।
- अपने OpenWRT username (default: `root`) और password (installation के दौरान सेट) के साथ लॉग इन करें।

#### **Step 2: Wireless Client Configure करें**
- **Wireless Settings पर नेविगेट करें:**
  - **Network > Wireless** पर जाएं।
- **Networks के लिए Scan करें:**
  - अपना radio (जैसे, Mi Router 4C पर 2.4 GHz के लिए `radio0`) locate करें।
  - उपलब्ध Wi-Fi networks की सूची देखने के लिए **Scan** पर क्लिक करें।
- **Main Wi-Fi Network से जुड़ें:**
  - अपने main router के Wi-Fi का SSID ढूंढें।
  - **Join Network** पर क्लिक करें।
- **Client Settings Configure करें:**
  - **Wi-Fi Key:** Main Wi-Fi का password दर्ज करें।
  - **Network:** `lan` का चयन करें या सेट करें (यह client interface को `br-lan` bridge में जोड़ता है)।
  - **Firewall Zone:** `lan` को असाइन करें (यह bridging के लिए traffic rules को सरल बनाता है)।
  - **Interface Name:** LuCI `wwan` सुझा सकता है; आप इसे छोड़ सकते हैं या स्पष्टता के लिए इसे `client` नाम दे सकते हैं, लेकिन सुनिश्चित करें कि यह `lan` से जुड़ा हुआ है।
- **Save & Apply:**
  - Main Wi-Fi से कनेक्ट होने के लिए **Save & Apply** पर क्लिक करें।

#### **Step 3: LAN Interface को DHCP Client में Adjust करें**
- **Interfaces पर जाएं:**
  - **Network > Interfaces** पर नेविगेट करें।
- **LAN Interface Edit करें:**
  - `lan` interface के आगे **Edit** पर क्लिक करें।
- **Protocol को DHCP Client में सेट करें:**
  - **Protocol** ड्रॉपडाउन में, **DHCP client** का चयन करें।
  - यह `br-lan` bridge (जिसमें अब wireless client शामिल है) को main router के DHCP server से IP address (जैसे, 192.168.1.x) प्राप्त करने की अनुमति देता है।
- **DHCP Server Disable करें:**
  - चूंकि `lan` अब एक DHCP client है, local DHCP server automatically disable हो जाता है। **Advanced Settings** या **DHCP and DNS** के तहत इसे सत्यापित करें—सुनिश्चित करें कि यदि विकल्प दिखाई दे तो "Ignore interface" चेक किया गया है।
- **Save & Apply:**
  - **Save & Apply** पर क्लिक करें। Router अब main router से IP का अनुरोध करेगा।

#### **Step 4: Wireless Access Point Configure करें**
- **नया Wireless Network जोड़ें:**
  - वापस **Network > Wireless** पर जाएं।
  - एक नया wireless interface बनाने के लिए same radio (जैसे, `radio0`) के तहत **Add** पर क्लिक करें।
- **AP सेट अप करें:**
  - **ESSID:** अपने Wi-Fi के लिए एक नाम चुनें (जैसे, `OpenWRT_AP`)।
  - **Mode:** **Access Point (AP)** पर सेट करें।
  - **Network:** `lan` को असाइन करें (यह इसे client interface और Ethernet ports के साथ bridge करता है)।
- **Security Configure करें:**
  - **Wireless Security** टैब पर जाएं।
  - **Encryption:** **WPA2-PSK** (recommended) का चयन करें।
  - **Key:** अपने AP के लिए एक मजबूत password सेट करें।
- **Save & Apply:**
  - **Save & Apply** पर क्लिक करें। आपका router अब अपना स्वयं का Wi-Fi प्रसारित करेगा।

#### **Step 5: Bridge को Verify करें**
- **Interfaces की जांच करें:**
  - **Network > Interfaces** पर जाएं।
  - सुनिश्चित करें कि `lan` interface `br-lan` bridge के तहत wireless client (जैसे, `wlan0`) और AP (जैसे, `wlan0-1`) दोनों को सूचीबद्ध करती है।
- **IP Assignment की जांच करें:**
  - **Status > Overview** पर जाएं।
  - Main router द्वारा `lan` interface को असाइन किए गए IP address (जैसे, `192.168.1.100`) को नोट करें।

#### **Step 6: Setup का परीक्षण करें**
- **Wi-Fi का परीक्षण करें:**
  - किसी device को `OpenWRT_AP` Wi-Fi से कनेक्ट करें।
  - सत्यापित करें कि उसे main router से IP (जैसे, `192.168.1.x`) प्राप्त होता है और उसकी internet access है।
- **Ethernet का परीक्षण करें (यदि applicable):**
  - Router के किसी एक LAN port में एक device plug करें।
  - पुष्टि करें कि उसे main router से IP मिलता है और वह internet से जुड़ता है।
- **LuCI तक पहुंचें:**
  - OpenWRT interface तक पहुंचने के लिए नए IP address (जैसे, `http://192.168.1.100`) का उपयोग करें।

---

### **यह क्यों काम करता है**
- Client और AP दोनों interfaces को `lan` network को असाइन करने से वे `br-lan` bridge में जुड़ जाते हैं, जिससे layer 2 traffic उनके और main router के बीच प्रवाहित हो सकती है।
- `lan` को DHCP client पर सेट करना सुनिश्चित करता है कि OpenWRT router को main router से एक unique IP मिले, conflicts (जैसे, `192.168.1.1` के साथ) से बचे, और local DHCP server को disable कर दे ताकि main router सभी IP assignments प्रबंधित कर सके।
- AP या Ethernet ports से जुड़े devices main network के समान subnet (जैसे, `192.168.1.x`) पर दिखाई देते हैं, जिससे wireless bridge requirement पूरी होती है।

---

### **वैकल्पिक Method: relayd का उपयोग (Pseudo-Bridge)**
यदि simple bridge method विफल हो जाती है (जैसे, wireless driver limitations के कारण), तो आप एक pseudo-bridge के लिए `relayd` package का उपयोग कर सकते हैं। यह एक routed setup बनाता है जहां OpenWRT router के clients एक अलग subnet पर होते हैं, लेकिन यह कुछ hardware पर अधिक विश्वसनीय होता है। यहाँ एक संक्षिप्त विवरण दिया गया है:

1. **relayd इंस्टॉल करें:**
   - **System > Software** पर जाएं, `relayd` खोजें और इसे इंस्टॉल करें।
2. **Wireless Client Configure करें:**
   - Main Wi-Fi से जुड़ें, लेकिन इसे एक नई interface (जैसे, `wwan`) को असाइन करें जो DHCP client पर सेट हो।
3. **LAN Configure करें:**
   - `lan` को एक static IP (जैसे, `192.168.2.1`) पर सेट करें जिसका अपना DHCP server हो।
4. **relayd सेट अप करें:**
   - SSH या LuCI ( **Network > Hostnames** के तहत) के माध्यम से `relayd` को `wwan` और `lan` के बीच relay करने के लिए configure करें।
5. **AP Configure करें:**
   - AP को `lan` network पर सेट करें।
6. **परीक्षण करें:**
   - `OpenWRT_AP` पर devices `192.168.2.x` पर होंगे, जिनकी internet main router से relay की गई है।

**नोट:** यह एक true bridge नहीं है (अलग-अलग subnets), इसलिए इसका उपयोग केवल तभी करें जब simple method काम न करे। आपके Xiaomi Mi Router 4C के लिए OpenWRT 24.10.0 के साथ, simple bridge पर्याप्त होना चाहिए।

---

### **निष्कर्ष**
आपके original steps **ज्यादातर सही** हैं लेकिन IP conflicts से बचने और उचित bridging सुनिश्चित करने के लिए `lan` interface को DHCP client mode में सेट किए बिना अधूरे हैं। ऊपर दिए गए सही किए गए steps OpenWRT को wireless bridge के रूप में configure करने का एक विश्वसनीय तरीका प्रदान करते हैं। यदि आप उनका पालन करते हैं, तो आपका router main Wi-Fi से जुड़ जाएगा और उस connection को अपने AP या Ethernet ports के माध्यम से निर्बाध रूप से साझा करेगा, सभी समान subnet पर। Setup का परीक्षण करें, और यदि कोई समस्या उत्पन्न होती है (आधुनिक OpenWRT के साथ दुर्लभ), तो `relayd` विकल्प पर विचार करें।