---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Autoren und Beiträge des Vision Transformers
translated: true
type: note
---

### Einführung zu den Autoren von "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"

Das bahnbrechende Paper "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale", das 2020 von Alexey Dosovitskiy und Kollegen bei Google eingeführt wurde, markierte einen Wendepunkt in der Computer Vision. Es schlug das Vision Transformer (ViT)-Modell vor, ein Modell, das Transformer-Architekturen – ursprünglich für die Verarbeitung natürlicher Sprache entwickelt – direkt auf Bildpatches anwendet und damit state-of-the-art Leistung auf großen Datensätzen wie ImageNet erzielt, wenn es mit massiven Daten (z.B. JFT-300M) vortrainiert wird. Diese Arbeit zeigte, dass reine Transformer bei ausreichender Rechenleistung und Datenmenge Convolutional Neural Networks (CNNs) in Effizienz und Genauigkeit übertreffen können, und beeinflusste nachfolgende Fortschritte in multimodaler KI und skalierbaren Vision-Modellen.

Das Paper war eine gemeinsame Arbeit von 12 Forschern, hauptsächlich vom Google Brain-Team in Zürich, die Expertise in Deep Learning, Sequenzmodellierung und Training in großem Maßstab vereinten. Im Folgenden finden Sie einen Überblick über die wichtigsten Autoren, der ihre Hintergründe und Beiträge zum Fachgebiet hervorhebt. (Der Kürze halber habe ich mich auf die prominentesten Mitwirkenden konzentriert; die vollständige Liste umfasst Dirk Weissenborn, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly und Jakob Uszkoreit – alles Google-Alumni mit tiefen Wurzeln in Transformern, Optimierung und Vision-Sprache-Integration.)

#### Wichtige Autoren und ihre Hintergründe

-   **Alexey Dosovitskiy (Hauptautor):** Als treibende Kraft hinter ViT konzipierte Dosovitskiy die Kernidee, Bilder als Sequenzen von Patches zu behandeln. Er hat einen MSc und PhD in Mathematik von der Lomonosov Moscow State University, gefolgt von einer Postdoc-Tätigkeit an der Universität Freiburg zum Thema unüberwachtes Feature-Learning. Nach seinem Wechsel zu Google Brain im Jahr 2019 leitete er die Entwicklung von ViT, bevor er 2021 zu Inceptive (einem Berliner KI-Unternehmen) wechselte. Seine Arbeit umfasst Computer Vision, generative Modelle und biologieinspiriertes ML, mit über 136.000 Zitaten.

-   **Lucas Beyer:** Beyer spielte eine entscheidende Rolle bei der praktischen Implementierung von ViT, der Evaluation auf Benchmarks und Effizienzoptimierungen. Der gebürtige Belgier studierte Maschinenbau an der RWTH Aachen und erwarb 2018 einen PhD in Robotik und KI mit Schwerpunkt auf Game AI und Reinforcement Learning. Nach seinem PhD wechselte er zu Google Brain in Zürich und stieg zum Staff Research Scientist bei Google DeepMind auf. 2025 wurde er einer der Top-KI-Einstellungen bei Meta und setzt seine Arbeit an Vision Transformern und datenzentriertem ML fort.

-   **Alexander Kolesnikov:** Kolesnikov trug zu den Skalierungsexperimenten von ViT und den Erkenntnissen zum Transfer Learning bei, wobei er die Leistung auf mittelgroßen Datensätzen betonte. Er erwarb einen Master in Mathematik von der Moscow State University und einen PhD in Maschinellem Lernen/Computer Vision vom Institute of Science and Technology Austria (ISTA) im Jahr 2018. Nach seinem Start bei Google Brain im Jahr 2018 stieg er bei DeepMind in Stabsrollen auf, bevor er zu OpenAI und 2025 zu Meta wechselte – wo er aufgrund seiner Expertise in effizienten Vision-Modellen abgeworben wurde.

-   **Xiaohua Zhai:** Zhai konzentrierte sich auf die Vortrainierungsstrategien von ViT und multimodale Erweiterungen, basierend auf seiner Arbeit im Representation Learning. Er hat einen PhD in Elektroniktechnik von der Peking University und wechselte 2015 als Software Engineer zu Google, bevor er 2017 zur Forschung bei Google Brain und 2023 zu DeepMind wechselte. Jetzt ist er Forscher bei Meta (über OpenAI Zürich im Jahr 2025), und seine Beiträge verbinden Vision, Sprache und selbstüberwachtes Lernen, mit über 100.000 Zitaten.

-   **Neil Houlsby (Senior Author):** Als Teamleiter überwachte Houlsby das architektonische Design von ViT und die weiteren Implikationen für Skalierungsgesetze in der Vision. Er erhielt um 2010 ein Google European Doctoral Fellowship und promovierte in Maschinellem Lernen. Als langjähriger Google-Forscher seit seinen Praktikumstagen leitete er Teams bei Google Brain und DeepMind zu neuronalen Architekturen und Vision-Sprache-Modellen. 2025 wechselte er zu Anthropic, um deren neues Zürcher Büro zu leiten und sich auf sichere KI-Skalierung zu konzentrieren.

Diese Google Brain-Kollaboration (hauptsächlich mit Sitz in Zürich) nutzte die Nähe des Teams zu TPUs für massive Experimente – über 25.000 TPU-Tage – und bewies damit die Tauglichkeit von Transformern jenseits von Text. Viele Autoren sind seitdem zu führenden KI-Laboren wie Meta, OpenAI und Anthropic gewechselt, was den bleibenden Einfluss von ViT auf das Fachgebiet widerspiegelt.

#### Referenzen

-   [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (arXiv)](https://arxiv.org/abs/2010.11929)
-   [Alexey Dosovitskiy Google Scholar Profile](https://scholar.google.com/citations?user=FXNJRDoAAAAJ)
-   [Lucas Beyer Google Scholar Profile](https://scholar.google.com/citations?user=p2gwhK4AAAAJ)
-   [Alexander Kolesnikov Google Scholar Profile](https://scholar.google.com/citations?user=H9I0CVwAAAAJ)
-   [Xiaohua Zhai Google Scholar Profile](https://scholar.google.com/citations?user=8gruapYAAAAJ)
-   [Neil Houlsby Google Scholar Profile](https://scholar.google.com/citations?user=sm1-TZMAAAAJ)
-   [From Ph.D. Detour to Meta's Top AI Hire: Lucas Beyer (Times of India)](https://timesofindia.indiatimes.com/education/news/lucas-beyer-educational-qualification-from-ph-d-detour-and-google-rejection-to-becoming-metas-top-ai-hire/articleshow/122158414.cms)
-   [Zuckerberg Poaches Alexander Kolesnikov from OpenAI (Times of India)](https://timesofindia.indiatimes.com/education/news/zuckerberg-poached-alexander-kolesnikov-from-sam-altmans-openai-where-did-this-ai-genius-study/articleshow/122158654.cms)
-   [Anthropic Poaches Neil Houlsby from Google DeepMind (Euronews)](https://www.euronews.com/next/2025/02/13/anthropic-poaches-google-deepmind-talent-to-lead-new-european-office)