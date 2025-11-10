---
audio: false
generated: true
lang: de
layout: post
title: Soziale Meta-Tags für SSI
translated: true
type: note
---

Der von Ihnen bereitgestgestellte Code besteht aus **Open Graph (OG)** und **Twitter Card** Meta-Tags, die verwendet werden, um zu steuern, wie Inhalte angezeigt werden, wenn sie auf Social-Media-Plattformen wie Facebook, Twitter (jetzt X) und anderen, die diese Protokolle unterstützen, geteilt werden. Diese Tags sind Teil des HTML-`<head>`-Abschnitts einer Website und liefern Metadaten über die Seite, um deren Darstellung in Social-Media-Feeds zu verbessern.

In diesem Fall sind die Meta-Tags für die Website von **Safe Superintelligence Inc.** (SSI) bestimmt, die unter `https://ssi.inc` erreichbar ist. Im Folgenden werde ich erklären, was diese Tags sind, wie sie funktionieren, und Kontext zu Safe Superintelligence Inc. auf der Grundlage der bereitgestellten Informationen geben.

---

### Was sind diese Meta-Tags?

**Open Graph (OG) Meta-Tags**:
- Entwickelt von Facebook, ermöglichen Open-Graph-Tags Websites zu definieren, wie ihre Inhalte aussehen, wenn sie auf Plattformen wie Facebook, LinkedIn und anderen, die das Open-Graph-Protokoll unterstützen, geteilt werden.
- Diese Tags legen wichtige Details wie den Titel der Seite, die Beschreibung, das Bild und die URL fest, um eine konsistente und ansprechende Vorschau zu gewährleisten, wenn der Link geteilt wird.

**Twitter Card Meta-Tags**:
- Twitter Cards sind ein ähnliches Konzept, das von Twitter (jetzt X) verwendet wird, um Linkvorschauen in Tweets oder Beiträgen anzureichern.
- Sie liefern Metadaten, um eine Zusammenfassung, ein Bild oder andere Medien anzuzeigen, wenn eine URL auf der Plattform geteilt wird.

Beide Tag-Sets optimieren die Benutzererfahrung, indem sie sicherstellen, dass geteilte Links professionell aussehen und relevante Informationen wie Titel, Beschreibung und Bild liefern.

---

### Aufschlüsselung der Meta-Tags

Hier ist die Funktion jedes Tags in Ihrem bereitgestellten Code:

#### Open-Graph-Tags
1. `<meta property="og:url" content="https://ssi.inc">`
   - Spezifiziert die kanonische URL der Seite, die geteilt werden soll. Dies stellt sicher, dass die korrekte URL angezeigt und verfolgt wird, um Duplikate zu vermeiden (z.B. `ssi.inc` vs. `www.ssi.inc`).
   - **Wert**: `https://ssi.inc`

2. `<meta property="og:type" content="website">`
   - Definiert den Inhaltstyp. In diesem Fall zeigt `website` eine allgemeine Webseite an (andere Typen sind `article`, `video` usw.).
   - **Wert**: `website`

3. `<meta property="og:title" content="Safe Superintelligence Inc.">`
   - Legt den Titel fest, der in der Social-Media-Vorschau angezeigt wird. Dies ist typischerweise der Name der Seite oder der Organisation.
   - **Wert**: `Safe Superintelligence Inc.`

4. `<meta property="og:description" content="The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.">`
   - Liefert eine kurze Beschreibung des Seiteninhalts, die in der Vorschau gezeigt wird. Dies fasst die Mission von Safe Superintelligence Inc. zusammen.
   - **Wert**: `The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.`

5. `<meta property="og:image" content="https://ssi.inc/public/og-preview.jpg">`
   - Spezifiziert das Bild, das in der Vorschau angezeigt werden soll. Dies ist typischerweise ein Logo, ein Banner oder eine relevante Grafik.
   - **Wert**: `https://ssi.inc/public/og-preview.jpg`

#### Twitter-Card-Tags
1. `<meta name="twitter:card" content="summary_large_image">`
   - Definiert den Typ der Twitter Card. `summary_large_image` erstellt eine Vorschau mit einem großen Bild, Titel und Beschreibung.
   - **Wert**: `summary_large_image`

2. `<meta name="twitter:site" content="@ssi">`
   - Spezifiziert den mit der Website verknüpften Twitter (X)-Handle und verlinkt zum offiziellen Account der Organisation.
   - **Wert**: `@ssi`

3. `<meta property="twitter:domain" content="ssi.inc">`
   - Gibt die Domain der geteilten Website an.
   - **Wert**: `ssi.inc`

4. `<meta property="twitter:url" content="https://ssi.inc">`
   - Spezifiziert die URL der geteilten Seite, ähnlich wie `og:url`.
   - **Wert**: `https://ssi.inc`

5. `<meta name="twitter:title" content="Safe Superintelligence Inc.">`
   - Legt den Titel für die Twitter Card fest, der mit dem Open-Graph-Titel übereinstimmt.
   - **Wert**: `Safe Superintelligence Inc.`

6. `<meta name="twitter:description" content="The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.">`
   - Liefert die Beschreibung für die Twitter Card, die mit der Open-Graph-Beschreibung übereinstimmt.
   - **Wert**: `The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.`

7. `<meta name="twitter:image" content="https://ssi.inc/public/og-preview.jpg">`
   - Spezifiziert das Bild für die Twitter Card, das mit dem Open-Graph-Bild übereinstimmt.
   - **Wert**: `https://ssi.inc/public/og-preview.jpg`

---

### Wie funktionieren diese Meta-Tags?

1. **Zweck**:
   - Wenn jemand die URL `https://ssi.inc` auf einer Plattform wie Facebook oder Twitter (X) teilt, liest der Web-Crawler der Plattform (z.B. Facebooks Crawler oder Twitters Bot) diese Meta-Tags aus dem HTML der Seite.
   - Der Crawler extrahiert Titel, Beschreibung, Bild und andere Metadaten, um eine Rich-Preview-Card zu generieren. Zum Beispiel:
     - Auf **Facebook** wird der geteilte Link eine Card mit dem Titel "Safe Superintelligence Inc.", der Beschreibung "The world's first straight-shot SSI lab…" und dem Bild unter `https://ssi.inc/public/og-preview.jpg` anzeigen.
     - Auf **Twitter (X)** erscheint eine ähnliche Card mit einem großen Bild, demselben Titel und derselben Beschreibung sowie dem `@ssi`-Handle für die Zuschreibung.

2. **Mechanismus**:
   - **Crawling**: Wenn eine URL geteilt wird, sendet die Social-Media-Plattform eine Anfrage an den Server der Website, um das HTML abzurufen und die Meta-Tags zu parsen.
   - **Rendering**: Die Plattform verwendet die Tag-Werte, um eine Vorschau-Card zu erstellen. Zum Beispiel stellt `summary_large_image` auf Twitter sicher, dass ein prominentes Bild mit Text darunter angezeigt wird.
   - **Caching**: Plattformen können die Metadaten zwischenspeichern, um die Serverlast zu reduzieren. Wenn die Tags aktualisiert werden, bieten Plattformen wie Facebook Tools (z.B. den Sharing Debugger) an, um den Cache zu aktualisieren.
   - **Validierung**: Plattformen können das Bild validieren (z.B. sicherstellen, dass es zugänglich ist und Größenanforderungen erfüllt) und greifen auf Standardtexte oder -bilder zurück, wenn Tags fehlen oder ungültig sind.

3. **Auswirkung**:
   - Diese Tags verbessern die Nutzerbindung, indem sie geteilte Links visuell ansprechender und informativer machen.
   - Sie gewährleisten Markenkonsistenz, indem sie dem Website-Betreiber erlauben, Titel, Beschreibung und Bild zu steuern.
   - Sie können Traffic auf die Website lenken, indem sie eine ansprechende Vorschau bieten.

---

### Über Safe Superintelligence Inc. (SSI)

Basierend auf den Meta-Tags und zusätzlichem Kontext aus den bereitgestellten Suchergebnissen ist hier, was wir über Safe Superintelligence Inc. wissen:

- **Überblick**:
  - Safe Superintelligence Inc. (SSI) ist ein amerikanisches Unternehmen für künstliche Intelligenz, das im Juni 2024 von Ilya Sutskever (ehemaliger OpenAI-Chefwissenschaftler), Daniel Gross (ehemaliger Leiter der Apple AI) und Daniel Levy (KI-Forscher und Investor) gegründet wurde.
  - Seine Mission ist die Entwicklung einer **sicheren Superintelligenz**, definiert als ein KI-System, das die menschliche Intelligenz übertrifft und dabei Sicherheit priorisiert, um Schaden zu verhindern.

- **Mission und Ansatz**:
  - SSIs einziger Fokus liegt auf der Schaffung eines sicheren superintelligenten Systems, was sowohl seine Mission als auch sein einziges Produkt ist. Im Gegensatz zu anderen KI-Unternehmen vermeidet SSI kommerzielle Produktzyklen, um sich auf langfristige Sicherheit und technische Durchbrüche zu konzentrieren.
  - Das Unternehmen betrachtet Sicherheit und KI-Fähigkeiten als miteinander verwobene technische Herausforderungen und zielt darauf ab, Fähigkeiten schnell voranzutreiben, während die Sicherheit oberste Priorität bleibt.
  - SSI betont ein Geschäftsmodell, das es vor kurzfristigen kommerziellen Zwängen abschirmt und einen Fokus auf Sicherheit, Security und Fortschritt erlaubt.

- **Betrieb**:
  - SSI unterhält Büros in **Palo Alto, Kalifornien**, und **Tel Aviv, Israel**, um Top-Technik-Talente anzuwerben.
  - Stand September 2024 hatte SSI etwa 20 Mitarbeiter, stellt aber aktiv Forscher und Ingenieure ein, mit einem Fokus auf "guten Charakter" und außergewöhnliche Fähigkeiten, nicht nur auf Qualifikationen.

- **Finanzierung und Bewertung**:
  - Im September 2024 sammelte SSI **1 Milliarde US-Dollar** zu einer Bewertung von **5 Milliarden US-Dollar** von Investoren wie Andreessen Horowitz, Sequoia Capital, DST Global und SV Angel ein.
  - Bis März 2025 erreichte SSI eine Bewertung von **30 Milliarden US-Dollar** in einer Finanzierungsrunde unter der Führung von Greenoaks Capital, mit zusätzlichen **2 Milliarden US-Dollar**, die im April 2025 eingesammelt wurden, was die Gesamtfinanzierung auf **3 Milliarden US-Dollar** zu einer Bewertung von **32 Milliarden US-Dollar** brachte.
  - Die Mittel werden verwendet, um Rechenleistung zu erwerben (z.B. durch eine Partnerschaft mit Google Cloud für TPUs) und Top-Talente einzustellen.

- **Kontext und Führung**:
  - Ilya Sutskever, ein Mitgründer von OpenAI und eine Schlüsselfigur hinter ChatGPT und AlexNet, verließ OpenAI im Mai 2024 nach einem Streit über Sicherheitsbedenken und der Entlassung von Sam Altman. SSI spiegelt seinen Glauben wider, dass OpenAI den Fokus auf Kommerzialisierung statt Sicherheit verlagerte.
  - SSIs Fokus auf **existentielle Sicherheit** (z.B. die Verhinderung katastrophaler Schäden durch KI) unterscheidet es von "Trust and Safety"-Bemühungen wie Inhaltsmoderation.
  - Das Unternehmen hat Aufmerksamkeit für sein hochkarätiges Team und seine Mission erregt, wobei Meta versuchte, SSI zu erwerben, und später 2025 seinen CEO, Daniel Gross, einstellte.

- **Aktueller Status**:
  - SSI befindet sich im **Stealth Mode**, ohne öffentliche Produkte oder Einnahmen Stand Juli 2025. Seine Website ist minimal und besteht aus einer einzigen Seite mit einer Missionserklärung und Kontaktinformationen.
  - Das Unternehmen konzentriert sich für mehrere Jahre auf F&E, bevor es sein erstes Produkt veröffentlicht, das eine sichere Superintelligenz sein wird.

---

### Wie arbeitet Safe Superintelligence Inc.?

Während SSIs technische Details aufgrund seines Stealth-Modus nicht öffentlich sind, kann sein Betriebsmodell aus den verfügbaren Informationen abgeleitet werden:

1. **Forschung und Entwicklung**:
   - SSI betreibt Grundlagenforschung in den Bereichen KI-Sicherheit, Ethik, Security und Governance, um Risiken zu identifizieren und überprüfbare Sicherheitsvorkehrungen zu entwickeln.
   - Das Unternehmen zielt darauf ab, ein superintelligentes KI-System zu schaffen, das sich mit menschlichen Werten in Einklang bringt und unter Kontrolle bleibt, verglichen mit der Gewährleistung der Sicherheit eines Kernreaktors unter extremen Bedingungen.

2. **Sicherheits-first-Ansatz**:
   - Im Gegensatz zu Unternehmen wie OpenAI, die kommerzielle Produkte wie ChatGPT entwickeln, konzentriert sich SSI ausschließlich auf den Aufbau eines einzigen sicheren superintelligenten Systems und vermeidet das "Wettrennen" von Produktzyklen.
   - Sicherheit ist in die Fähigkeitsentwicklung integriert, wobei beide als technische Probleme durch innovative Technik adressiert werden.

3. **Team und Talente**:
   - SSI baut ein schlankes, hochqualifiziertes Team von Ingenieuren und Forschern in Palo Alto und Tel Aviv auf, das solche priorisiert, die sich seiner Sicherheitsmission verpflichtet fühlen.
   - Das Unternehmen verbringt viel Zeit damit, Kandidaten auf Übereinstimmung mit seiner Kultur und Mission zu prüfen.

4. **Infrastruktur**:
   - SSI partners with cloud providers like Google Cloud for access to TPUs (Tensor Processing Units) to support its computational needs for AI training.
   - Das Unternehmen plant, mit Chip-Unternehmen für zusätzliche Rechenressourcen zusammenzuarbeiten.

5. **Bildung und Zusammenarbeit**:
   - Über die Entwicklung hinaus zielt SSI darauf ab, Forscher, Entwickler, politische Entscheidungsträger und die Öffentlichkeit über sichere KI-Praktiken zu informieren und fördert eine globale Denkweise, die Sicherheit über Kommerzialisierung stellt.
   - Es strebt danach, ein kollaboratives Ökosystem aufzubauen, um globale Normen und Best Practices für die sichere KI-Entwicklung zu etablieren.

---

### Warum diese Meta-Tags für SSI wichtig sind

Die Meta-Tags spiegeln SSIs Markenidentität und Mission wider:
- Der konsistente Titel und die Beschreibung ("Safe Superintelligence Inc." und "The world's first straight-shot SSI lab…") betonen seinen singulären Fokus auf sichere Superintelligenz, was mit seiner öffentlichen Kommunikation übereinstimmt.
- Der Twitter-Handle `@ssi` verbindet die Website mit seinem offiziellen X-Account, auf dem Updates wie die Gründungsankündigung des Unternehmens gepostet wurden.
- Das Bild (`og-preview.jpg`) ist wahrscheinlich eine Branding-Grafik oder ein Logo, obwohl sein Inhalt nicht öffentlich beschrieben ist. Es gewährleistet visuelle Konsistenz, wenn die Website geteilt wird.

Diese Tags sind kritisch für SSI, ein Stealth-Mode-Startup mit minimaler öffentlicher Präsenz, da sie helfen, seine Erzählung in den sozialen Medien zu steuern, insbesondere angesichts seiner hochkarätigen Gründer und des erheblichen Investor-Interesses.

---

### Einschränkungen und Hinweise
- **Fehlende öffentliche Details**: SSIs Website und öffentliche Informationen sind spärlich, was seinen Frühphasen- und Stealth-Status widerspiegelt. Die Meta-Tags bieten einen Einblick in sein Branding, aber nicht in seinen technischen Ansatz.
- **Spekulativer Charakter**: Behauptungen über SSIs Bewertung und Finanzierung basieren auf Berichten, aber genaue Details (z.B. Produkt-Roadmap) bleiben undurchsichtig.
- **X-Posts als Stimmungsbild**: Beiträge auf X deuten auf Aufregung über SSIs Potenzial hin, sind aber keine faktischen Beweise und können Spekulationen enthalten.