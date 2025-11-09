---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: जीपीजी एएससीआईआई आर्मर की व्याख्या
translated: true
type: note
---

GPG (GNU Privacy Guard) में, "आर्मर" ASCII आर्मर को संदर्भित करता है, यह एक ऐसा फॉर्मेट है जो बाइनरी OpenPGP डेटा (जैसे एन्क्रिप्टेड फाइलें, सिग्नेचर या कुंजियाँ) को एक मानव-पठनीय, टेक्स्ट-आधारित प्रतिनिधित्व में एनकोड करता है। यह डेटा को केवल-टेक्स्ट चैनलों, जैसे ईमेल, के माध्यम से बिना क्षति के प्रसारित करने के लिए उपयोगी है - यह काम uuencode या base64 की तरह ही करता है, लेकिन इसमें अखंडता के लिए हेडर (जैसे, "-----BEGIN PGP MESSAGE-----") और चेकसम जुड़े होते हैं।

आप इसे कमांड्स जैसे एन्क्रिप्शन (`gpg -a -e file.txt`) या कुंजी एक्सपोर्ट (`gpg --armor --export keyid`) के दौरान `--armor` (या `-a`) विकल्प के साथ सक्षम कर सकते हैं, जो परिणाम को कच्चे बाइनरी के बजाय इस आर्मर्ड टेक्स्ट फॉर्मेट में आउटपुट करता है।

## संदर्भ
- [What is the armored option for in GnuPG?](https://unix.stackexchange.com/questions/623375/what-is-the-armored-option-for-in-gnupg)
- [Exchanging keys - GnuPG](https://www.gnupg.org/gph/en/manual/x56.html)
- [13. ASCII armor - Notes on OpenPGP](https://openpgp.dev/book/armor.html)
- [GPG Input and Output (Using the GNU Privacy Guard)](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Input-and-Output.html)