---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Carnet de voyage bancaire à Hong Kong
translated: true
type: note
---

Je n'ai trouvé aucune source crédible confirmant que vous pouvez utiliser un **WeChat mini program** pour exporter directement vos *relevés de franchissement de frontière / d'entrée-sortie / de voyage* dans le but d'ouvrir un compte bancaire à Hong Kong.

Voici ce que j'ai découvert, ainsi que la meilleure approche probable :

---

## Ce que j'ai trouvé : les canaux officiels et leurs limites

* Le Département de l'immigration de Hong Kong a une procédure officielle : vous pouvez demander un **Statement of Travel Records** (c'est-à-dire le relevé de vos entrées/sorties via l'immigration hongkongaise) via leur site web. ([Immigration Department Hong Kong][1])

  * Vous soumettez vos documents d'identité, payez des frais (160 HK$), et cela prend environ 10 jours ouvrables. ([Hong Kong Government][2])
  * Il s'agit du relevé reconnu que les banques accepteraient comme preuve de votre historique de voyages à Hong Kong. ([Hong Kong Government][2])

* Je n'ai trouvé aucune preuve que WeChat ou un quelconque WeChat mini program soit intégré au système d'immigration de Hong Kong d'une manière qui permette d'exporter ou de vérifier vos données d'entrée/sortie à Hong Kong.

* Certaines banques (en Chine continentale ou proposant des services liés à Hong Kong / à la GBA) ont des WeChat mini programs pour la prise de rendez-vous, la soumission de documents ou les services transfrontaliers, mais pas pour l'extraction de relevés d'immigration. Par exemple, HSBC a un WeChat mini program GBA pour les services de comptes entreprise. ([business.hsbc.com.cn][3])

* De plus, HSBC Hong Kong a cessé de fournir certains services via son WeChat mini program / liaison depuis juillet 2022. ([hsbc.com.hk][4])

---

## Pourquoi c'est improbable via un WeChat mini program

* **Source des données** : Les relevés de franchissement de frontière / d'immigration sont contrôlés par le Département de l'immigration de Hong Kong, et ils ne semblent pas fournir d'API publique ou de service permettant à WeChat de récupérer ces données.

* **Confidentialité / sécurité** : Ces données personnelles sont sensibles et généralement non exposées via des plateformes tierces, sauf autorisation explicite par la loi ou un accord.

* **Absence de lien officiel** : Je n'ai trouvé aucune publication concernant une intégration entre la plateforme WeChat et le Département de l'immigration de Hong Kong à cette fin.

---

## Ce que vous *devriez* utiliser à la place (pour l'ouverture de compte bancaire)

Pour présenter des relevés de voyage fiables et acceptés par les banques de Hong Kong, voici la meilleure démarche :

1. **Demandez le Statement of Travel Records officiel** au Département de l'immigration de HK (formulaire ID 697 / en ligne). ([Hong Kong Government][2])
2. Utilisez ce document (imprimé / certifié) comme preuve de votre présence à Hong Kong lors de l'ouverture de votre compte bancaire. De nombreuses banques l'acceptent comme preuve de vos entrées/sorties passées à HK.
3. Si la banque demande une vérification supplémentaire (numérique ou autre), vous pouvez demander si elles acceptent d'autres documents, mais il est peu probable qu'elles acceptent une exportation WeChat, à moins qu'elles ne prennent explicitement en charge cette méthode.

---

Si vous le souhaitez, je peux vérifier si une banque à HK a *récemment* commencé à accepter les exports de WeChat mini program ou une autre méthode numérique alternative (en 2025). Voulez-vous que je vérifie cela pour vous ?

[1]: https://www.immd.gov.hk/eng/services/statement-of-travel-records.html?utm_source=chatgpt.com "Application for a Statement of Travel Records"
[2]: https://www.gov.hk/en/residents/immigration/records/str.htm?utm_source=chatgpt.com "Online Application for a Statement of Travel Records"
[3]: https://www.business.hsbc.com.cn/en-gb/campaigns/gba/wechat-mini-program?utm_source=chatgpt.com "HSBC GBA WeChat Mini Programme"
[4]: https://www.hsbc.com.hk/help/faq/banking/wechat/?utm_source=chatgpt.com "HSBC HK WeChat Official Account"