---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ओपनवेबटेक्स्ट और विकिपीडिया डेटासेट टोरेंट्स
translated: true
type: note
---

### OpenWebText डेटासेट टोरेंट्स

OpenWebText, OpenAI के WebText डेटासेट का एक ओपन-सोर्स रेप्लिकेशन है, जिसमें उच्च-कर्मा Reddit लिंक्स (मुख्य रूप से वेब पेज जिन्हें क्वालिटी के लिए स्क्रैप और फ़िल्टर किया गया है) से निकाले गए ~38GB साफ़ टेक्स्ट शामिल हैं। यह भाषा मॉडल प्रशिक्षण के लिए एक लोकप्रिय बड़े पैमाने का टेक्स्ट कॉर्पस है। हालांकि पूरा स्क्रैप किया गया टेक्स्ट हमेशा सीधे एक ही टोरेंट के रूप में उपलब्ध नहीं होता, यहां कुछ विश्वसनीय विकल्प दिए गए हैं:

- **URLs सूची (फ़िल्टर्ड, ~480MB)**: OpenWebText को स्क्रैप करने के लिए इस्तेमाल ~26 मिलियन URLs की एक पहले से फ़िल्टर की गई सूची। आप इसका इस्तेमाल टेक्स्ट को स्वयं डाउनलोड और प्रोसेस करने के लिए कर सकते हैं।
  - टोरेंट: [OpenWebText-urls-26M-filtered.xz](https://academictorrents.com/details/f5161721b322bca66ed74da32b963c1066e64312)
  - स्रोत: Academic Torrents (कम्युनिटी द्वारा सीडेड)।

- **URLs सूची (पूर्ण, ~1.75GB)**: Reddit सबमिशन्स से डीडुप्लिकेट किए गए पूरे URLs।
  - टोरेंट: [WebText dataset urls.txt.tar.gz](https://academictorrents.com/details/15f3494b2991e75194d3af72bf7afa5025a7abc3)
  - स्रोत: Academic Torrents (कम्युनिटी द्वारा सीडेड)।

- **टोकनाइज्ड वर्जन (~16GB)**: स्क्रैप किए गए कॉर्पस से GPT-2 टोकनाइज्ड टेक्स्ट फाइलें (395 फाइलें, मॉडल ट्रेनिंग के लिए तैयार)।
  - टोरेंट: [OpenWebText (Gokaslan's distribution, 2019), GPT-2 Tokenized](https://academictorrents.com/details/36c39b25657ce1639ccec0a91cf242b42e1f01db)
  - स्रोत: Academic Torrents (OSUOSL और कम्युनिटी द्वारा सीडेड)।

पूरे रॉ टेक्स्ट कॉर्पस के लिए, डायरेक्ट डाउनलोड (टोरेंट-आधारित नहीं) के लिए ऑफिशियल साइट चेक करें या ऊपर दिए गए URLs का इस्तेमाल [OpenWebText GitHub रेपो](https://github.com/eukaryote31/openwebtext) से स्क्रैपिंग स्क्रिप्ट्स के साथ करें। एक एन्हांस्ड वर्जन, OpenWebText2 (~मल्टी-टीबी स्केल), [EleutherAI's रेपो](https://github.com/EleutherAI/openwebtext2) के जरिए उपलब्ध है लेकिन यह टोरेंट्स के बजाय स्ट्रीमिंग का इस्तेमाल करता है।

### विकिपीडिया डंप टोरेंट्स

विकिपीडिया डंप पूरी डेटाबेस (लेख, रिवीजन्स, मेटाडेटा) के मासिक XML एक्सपोर्ट होते हैं। अंग्रेजी वर्जन बहुत बड़ा है (~20-25GB कम्प्रेस्ड एब्स्ट्रैक्ट्स के लिए, 100+GB पूरे इतिहास के लिए)। टोरेंट्स कम्युनिटी-मेंटेन्ड (अनऑफिशियल लेकिन ऑफिशियल चेकसम के मुताबिक वेरिफाइड) होते हैं और विश्वसनीयता के लिए विकिमीडिया सर्वर से वेब-सीडेड होते हैं। डाउनलोड को हमेशा [dumps.wikimedia.org](https://dumps.wikimedia.org/enwiki/latest/) के हैश के मुताबिक वेरिफाई करें।

टोरेंट्स का मुख्य हब [Meta-Wiki Data Dump Torrents पेज](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) है, जो नवीनतम अंग्रेजी विकिपीडिया डंप्स (जैसे, enwiki-20251101) को सूचीबद्ध करता है। यहां हाल के कुछ का सारांश दिया गया है:

| डंप तारीख | फाइल प्रकार | कम्प्रेस्ड साइज | टोरेंट लिंक | नोट्स |
|-----------|-----------|-----------------|--------------|-------|
| 2025-11-01 | Pages-Articles (XML, केवल सारांश) | ~22GB | [enwiki-20251101-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | मल्टीस्ट्रीम फॉर्मेट; टेक्स्ट एक्सट्रैक्शन के लिए सबसे आसान। |
| 2025-11-01 | Pages-Articles-History (XML, पूरे रिवीजन) | ~120GB | [enwiki-20251101-pages-meta-history*.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | सभी एडिट्स शामिल; आसान हैंडलिंग के लिए स्ट्रीम्स में बंटा हुआ। |
| 2025-10-01 | Pages-Articles (XML, केवल सारांश) | ~21GB | [enwiki-20251001-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | पिछला मासिक; ऐतिहासिक तुलना के लिए अच्छा। |

- **पूर्ण कलेक्शन**: [Academic Torrents Wikipedia Collection](https://academictorrents.com/collection/wikipedia) पर सभी ऐतिहासिक अंग्रेजी विकिपीडिया टोरेंट्स ब्राउज़ करें (इसमें ~2010 के पुराने डंप्स शामिल हैं)।
- **किविक्स ZIM फॉर्मेट**: अगर आप एक ब्राउज़ करने लायक ऑफलाइन विकिपीडिया (HTML, ~100GB) चाहते हैं, तो [wikipedia_en_all_maxi_2024-01.zim.torrent](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2024-01.zim.torrent) आज़माएं – कम्युनिटी-सीडेड, लेकिन 2025 के अपडेट्स के लिए [किविक्स डाउनलोड्स](https://download.kiwix.org/zim/wikipedia/) चेक करें।

इन्हें प्लेन टेक्स्ट में प्रोसेस करने के लिए, Python से `wikiextractor` जैसे टूल्स का इस्तेमाल करें। टोरेंट्स सर्वर लोड कम करते हैं और बीच में रुके हुए डाउनलोड को रिज्यूम करते हैं – qBittorrent जैसे क्लाइंट का इस्तेमाल करें। अगर आपको दूसरी भाषाओं या सबसेट्स के लिए डंप चाहिए, तो Meta-Wiki पेज में फिल्टर्स हैं।