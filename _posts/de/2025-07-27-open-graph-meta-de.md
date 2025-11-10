---
audio: false
generated: true
image: false
lang: de
layout: post
title: Open Graph Protocol erklärt
translated: true
type: note
---

Im Kontext von HTML-Meta-Tags wie `<meta property="og:type" content="website">` steht "og" für Open Graph. Dies bezieht sich auf das Open Graph Protocol, einen Standard, der ursprünglich von Facebook (jetzt Meta) entwickelt wurde, um Webseiten zu ermöglichen, strukturierte Metadaten über ihren Inhalt bereitzustellen. Diese Metadaten steuern, wie die Seite geteilt wird, wenn sie auf Social-Media-Plattformen oder in Messaging-Apps geteilt wird, z. B. durch die Anzeige eines Titels, einer Beschreibung, eines Bildes und anderer Details in einem Rich-Preview-Format (z. B. eine Karte mit Bild und Zusammenfassung).

Das Protokoll verwendet Eigenschaften mit dem Präfix "og:", um Elemente wie die folgenden zu definieren:
- `og:title`: Der Titel des Inhalts.
- `og:description`: Eine kurze Zusammenfassung.
- `og:image`: Eine URL für ein Vorschaubild.
- `og:type`: Die Art des Inhalts (z. B. website, article, video).

Obwohl es für Facebook erstellt wurde, unterstützen viele andere Plattformen und Apps Open Graph-Tags für Link-Vorschauen, einschließlich WeChat. Wenn Sie einen Link auf WeChat teilen, parsed die App oft diese Tags, um konsistent Miniaturbilder, Titel und Beschreibungen zu generieren. Wenn die Tags nicht vorhanden sind, können Plattformen auf andere Meta-Tags zurückgreifen oder den Seiteninhalt scrapen, was zu inkonsistenten Ergebnissen führen kann.

Ihre Vermutung von "open gx" scheint nah dran zu sein – es ist tatsächlich "Open Graph", nicht "open gx" (möglicherweise ein Tippfehler oder eine Autokorrektur für "graph"?).

### Referenzen
[The Open Graph protocol](https://ogp.me/)  
[Open Graph Meta Tags: Everything You Need to Know](https://ahrefs.com/blog/open-graph-meta-tags/)  
[What is Open Graph and how can I use it for my website?](https://www.freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website/)  
[How does wechat choose the link's thumbnail?](https://stackoverflow.com/questions/44564614/how-does-wechat-choose-the-links-thumbnail)  
[Meta tag - WeChat](https://github.com/freeCodeCamp/freeCodeCamp/issues/38707)