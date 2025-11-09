---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: macOS डिफ़ॉल्ट डेमन प्रक्रियाएँ
translated: true
type: note
---

### macOS में डिफ़ॉल्ट डेमन प्रक्रियाएं

macOS में, डेमन प्रक्रियाएं पृष्ठभूमि सेवाएं हैं जो बिना यूजर इंटरफेस के चलती हैं, आमतौर पर बूट पर या डिमांड पर शुरू होती हैं। उन्हें **launchd** द्वारा प्रबंधित किया जाता है, जो सिस्टम का init और service management फ्रेमवर्क (PID 1) है। डेमन एजेंटों से अलग होते हैं: डेमन रूट/सिस्टम-वाइड (लॉगिन से पहले) चलते हैं, जबकि एजेंट प्रति-यूजर (लॉगिन के बाद) चलते हैं।

डिफ़ॉल्ट सिस्टम डेमन प्रॉपर्टी लिस्ट (.plist) फाइलों में परिभाषित होते हैं जो `/System/Library/LaunchDaemons/` में स्थित होती हैं। एक स्टैंडर्ड इंस्टॉल पर आमतौर पर लगभग 300–350 ऐसे डेमन होते हैं (उदाहरण के लिए, macOS 10.14 Mojave पर 339), जो नेटवर्किंग और सुरक्षा से लेकर हार्डवेयर प्रबंधन तक सब कुछ कवर करते हैं। यूजर-इंस्टॉल्ड या थर्ड-पार्टी डेमन `/Library/LaunchDaemons/` में जाते हैं।

#### डिफ़ॉल्ट डेमन कैसे देखें
टर्मिनल में सभी लोडेड डेमन (और एजेंट) की सूची देखने के लिए:
- `sudo launchctl list` (सिस्टम-वाइड डेमन और एजेंट दिखाता है)।
- `launchctl list` (केवल यूजर-स्पेसिफिक एजेंट दिखाता है)।

पूरी डायरेक्टरी लिस्टिंग के लिए: `ls /System/Library/LaunchDaemons/` (sudo की आवश्यकता नहीं है, लेकिन फाइलें रीड-ओनली हैं)।

ये कमांड PID, स्टेटस और लेबल (जैसे, `com.apple.timed`) जैसे कॉलम आउटपुट करते हैं।

#### "timed" डेमन
आपने विशेष रूप से "timed" का उल्लेख किया है, जो **com.apple.timed** (टाइम सिंक डेमन) को संदर्भित करता है। यह एक कोर सिस्टम डेमन है जिसे macOS High Sierra (10.13) में पुरानी `ntpd` प्रक्रिया को बदलने के लिए पेश किया गया था।

- **उद्देश्य**: यह मैक की सिस्टम घड़ी को सटीकता के लिए NTP (नेटवर्क टाइम प्रोटोकॉल) सर्वर के साथ स्वचालित रूप से सिंक्रनाइज़ करता है, उन्हें हर 15 मिनट में क्वेरी करता है। यह लॉग, सर्टिफिकेट और नेटवर्क ऑपरेशन के लिए सटीक टाइमकीपिंग सुनिश्चित करता है।
- **यह कैसे काम करता है**: इसे launchd द्वारा `/System/Library/LaunchDaemons/com.apple.timed.plist` से लॉन्च किया जाता है, यह `_timed` यूजर के रूप में (`_timed` और `_sntpd` ग्रुप में) चलता है। यह सर्वर प्रतिक्रियाओं के आधार पर घड़ी को एडजस्ट करने के लिए `settimeofday` सिसकॉल का उपयोग करता है। कॉन्फ़िगरेशन `/etc/ntpd.conf` (NTP सर्वर) में है और स्टेट `/var/db/timed/com.apple.timed.plist` में कैश की जाती है।
- **संबंधित**: सिस्टम सेटिंग्स > जनरल > दिनांक एवं समय > "दिनांक एवं समय स्वचालित रूप से निर्धारित करें" से जुड़ा हुआ है। यदि अक्षम है, तो timed सिंक नहीं करेगा। उन्नत सेटअप (जैसे, उच्च-परिशुद्धि आवश्यकताओं) के लिए, Chrony जैसे टूल इसे बदल सकते हैं लेकिन timed को अक्षम करना होगा।

यदि आपकी घड़ी ड्रिफ्ट हो रही है, तो NTP (UDP पोर्ट 123) पर नेटवर्क समस्याओं या फ़ायरवॉल ब्लॉक की जांच करें।

#### अन्य सामान्य डिफ़ॉल्ट डेमन ("आदि")
यहां कुछ बार-बार चलने वाले डिफ़ॉल्ट सिस्टम डेमन की एक तालिका दी गई है, जो फ़ंक्शन के अनुसार समूहीकृत है। यह संपूर्ण नहीं है (सैकड़ों हैं), लेकिन आवश्यकताओं को कवर करती है। लेबल .plist फ़ाइलनामों से हैं।

| श्रेणी           | डेमन लेबल                      | विवरण |
|------------------|---------------------------------|-------------|
| **कोर सिस्टम**  | `com.apple.launchd`             | launchd प्रक्रिया स्वयं; अन्य सभी को शुरू करती है। |
| **समय और सिंक** | `com.apple.timed`               | NTP समय सिंक्रनाइज़ेशन (जैसा ऊपर बताया गया है)। |
| **यूजर प्रबंधन** | `com.apple.opendirectoryd`     | यूजर/ग्रुप अकाउंट और डायरेक्टरी सेवाएं संभालता है। |
| **यूजर प्रबंधन** | `com.apple.accounts`           | यूजर अकाउंट और प्रमाणीकरण प्रबंधित करता है। |
| **नेटवर्किंग**  | `com.apple.mDNSResponder`       | स्थानीय नेटवर्क डिस्कवरी (जैसे, AirDrop) के लिए Bonjour/mDNS। |
| **नेटवर्किंग**  | `com.apple.nesessionmanager`    | नेटवर्क एक्सटेंशन और VPN प्रबंधन। |
| **ब्लूटूथ/वायरलेस** | `com.apple.bluetoothd`       | ब्लूटूथ डिवाइस हैंडलिंग। |
| **iCloud/सिंक** | `com.apple.cloudd`              | iCloud डेटा सिंकिंग और सेवाएं। |
| **सुरक्षा**     | `com.apple.securityd`           | कीचेन और क्रेडेंशियल प्रबंधन (अक्सर एक एजेंट के रूप में भी)। |
| **अपडेट**       | `com.apple.softwareupdated`     | सॉफ़्टवेयर अपडेट और कैटलॉग डाउनलोड संभालता है। |
| **हार्डवेयर**   | `com.apple.kextd`               | कर्नल एक्सटेंशन लोडिंग और प्रबंधन। |
| **लॉगिंग**      | `com.apple.systemnotificationd` | सिस्टम नोटिफिकेशन और लॉगिंग। |
| **MDM (यदि सक्षम)** | `com.apple.mdmclient`        | एंटरप्राइज़ सेटअप के लिए मोबाइल डिवाइस मैनेजमेंट क्लाइंट। |

ये macOS को स्थिर रखने के लिए लगातार या ट्रिगर पर चलते हैं। यदि कोई गलत व्यवहार करता है (जैसे, उच्च CPU), आप इसे अस्थायी रूप से `sudo launchctl unload /System/Library/LaunchDaemons/com.apple.example.plist` से अनलोड कर सकते हैं, लेकिन सिस्टम फाइलों को संशोधित करने से बचें।

अपने मैक पर एक पूरी, वर्तमान सूची के लिए (अक्टूबर 2025 तक, संभवतः macOS 15 Sequoia या बाद में), ऊपर दिए गए कमांड चलाएं—संस्करण अपडेट के साथ थोड़ा विकसित होते हैं।

#### संदर्भ
- [The macOS Process Journey — “timed” (Time Sync Daemon)](https://medium.com/@boutnaru/the-macos-process-journey-timed-time-sync-daemon-4898c8185b4b)
- [Daemons and Agents could be slowing down your Mac](https://appleinsider.com/inside/macos/tips/daemons-and-agents-could-be-slowing-down-your-mac)
- [What files are included in the /System/Library/LaunchAgents and /System/Library/LaunchDaemons](https://apple.stackexchange.com/questions/361029/what-files-are-included-in-the-system-library-launchagents-and-system-library)
- [Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- [How to show all running launchctl daemons/agents?](https://apple.stackexchange.com/questions/134817/how-to-show-all-running-launchctl-daemons-agents)