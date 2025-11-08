---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht des Vision Transformers
translated: true
type: note
---

### Einführung in Vision Transformer (ViT)

Der Vision Transformer (ViT) ist eine neuronale Netzarchitektur, die das Transformer-Modell – ursprünglich für die Verarbeitung natürlicher Sprache (NLP) entwickelt – für Aufgaben des Computer Vision, insbesondere Bildklassifizierung, adaptiert. Eingeführt im Jahr 2020 von Alexey Dosovitskiy und Kollegen bei Google in dem Papier *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*, behandelt ViT Bilder als Sequenzen von Patches, anstatt sie mit traditionellen Convolutional Neural Networks (CNNs) zu verarbeiten. Dies ermöglicht es ihm, die Stärken des Transformers im Umgang mit langreichweitigen Abhängigkeiten und paralleler Berechnung zu nutzen.

ViT hat auf großen Datensätzen wie ImageNet eine wettbewerbsfähige oder überlegene Leistung im Vergleich zu CNNs gezeigt, insbesondere wenn es mit riesigen Datenmengen (z.B. JFT-300M) vortrainiert wurde. Varianten wie DeiT (Data-efficient Image Transformers) machen es effizienter für kleinere Datensätze. Heute treiben von ViT inspirierte Modelle viele Vision-Aufgaben in Modellen wie DALL-E, Stable Diffusion und modernen Klassifikatoren an.

### Wie ViT funktioniert: Gesamtarchitektur und Workflow

Die Kernidee von ViT ist es, ein Bild in eine Sequenz von festen Patches zu "tokenisieren", ähnlich wie Text in Wörter oder Tokens unterteilt wird. Diese Sequenz wird dann von einem standard Transformer-Encoder verarbeitet (kein Decoder, anders als bei generativen Textmodellen). Hier ist eine schrittweise Aufschlüsselung der Funktionsweise:

1.  **Bildvorverarbeitung und Patch-Extraktion**:
    *   Starte mit einem Eingabebild der Größe \\(H \times W \times C\\) (Höhe × Breite × Kanäle, z.B. 224 × 224 × 3 für RGB).
    *   Teile das Bild in nicht überlappende Patches einer festen Größe \\(P \times P\\) (z.B. 16 × 16 Pixel). Dies ergibt \\(N = \frac{HW}{P^2}\\) Patches (z.B. 196 Patches für ein 224×224 Bild mit 16×16 Patches).
    *   Jeder Patch wird in einen 1D-Vektor der Länge \\(P^2 \cdot C\\) abgeflacht (z.B. 768 Dimensionen für 16×16×3).
    *   Warum Patches? Rohe Pixel würden eine unpraktisch lange Sequenz erzeugen (z.B. Millionen für ein hochauflösendes Bild), daher fungieren Patches als "visuelle Wörter", um die Dimensionalität zu reduzieren.

2.  **Patch Embedding**:
    *   Wende eine erlernbare lineare Projektion (eine einfache Fully-Connected-Layer) auf jeden abgeflachten Patch-Vektor an, um ihn auf eine feste Embedding-Dimension \\(D\\) abzubilden (z.B. 768, vergleichbar mit BERT-ähnlichen Transformern).
    *   Dies erzeugt \\(N\\) Embedding-Vektoren, jeweils der Größe \\(D\\).
    *   Optional: Füge ein spezielles [CLS]-Token-Embedding (ein erlernbarer Vektor der Größe \\(D\\)) am Anfang der Sequenz hinzu, ähnlich wie bei BERT für Klassifizierungsaufgaben.

3.  **Positionelle Embeddings**:
    *   Füge erlernbare 1D-positionelle Embeddings zu den Patch-Embeddings hinzu, um räumliche Informationen zu kodieren (Transformer sind ohne diese permutationsinvariant).
    *   Die vollständige Eingabesequenz ist nun: \\([ \text{[CLS]}, \text{patch}_1, \text{patch}_2, \dots, \text{patch}_N ] + \text{positions}\\), eine Matrix der Form \\((N+1) \times D\\).

4.  **Transformer-Encoder-Blöcke**:
    *   Speise die Sequenz in \\(L\\) gestapelte Transformer-Encoder-Layers (z.B. 12 Layers).
    *   Jede Layer besteht aus:
        *   **Multi-Head Self-Attention (MSA)**: Berechnet Aufmerksamkeits-Scores zwischen allen Paaren von Patches (einschließlich [CLS]). Dies ermöglicht es dem Modell, globale Beziehungen zu erfassen, wie z.B. "dieses Katzenohr bezieht sich auf die Schnurrhaare 100 Patches entfernt", anders als die lokalen rezeptiven Felder von CNNs.
            *   Formel: Attention(Q, K, V) = \\(\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V\\), wobei Q, K, V Projektionen der Eingabe sind.
        *   **Multi-Layer Perceptron (MLP)**: Ein Feed-Forward-Netzwerk (zwei lineare Layers mit GELU-Aktivierung), das positionsweise angewendet wird.
        *   Layer-Normalisierung und Residual Connections: Input + MSA → Norm → MLP → Norm + Input.
    *   Ausgabe: Eine Sequenz verfeinerter Embeddings, immer noch \\((N+1) \times D\\).

5.  **Klassifikations-Head**:
    *   Für die Bildklassifizierung wird die Ausgabe des [CLS]-Tokens extrahiert (oder der Durchschnitt aller Patch-Embeddings gebildet).
    *   Leite sie durch einen einfachen MLP-Head (z.B. eine oder zwei lineare Layers), um Klassen-Logits auszugeben.
    *   Während des Trainings wird der Cross-Entropy-Loss auf gelabelten Daten verwendet. Pre-training beinhaltet oft Masked-Patch-Prediction oder andere selbstüberwachte Aufgaben.

**Wichtige Hyperparameter** (vom originalen ViT-Base-Modell):
*   Patch-Größe \\(P\\): 16
*   Embedding-Dim \\(D\\): 768
*   Layers \\(L\\): 12
*   Heads: 12
*   Parameter: ~86M

ViT skaliert gut: Größere Modelle (z.B. ViT-Large mit \\(D=1024\\), \\(L=24\\)) performen besser, benötigen aber mehr Daten/Rechenleistung.

**Training und Inferenz**:
*   **Training**: End-to-End auf gelabelten Daten; profitiert enorm von Pre-training auf Milliarden von Bildern.
*   **Inferenz**: Forward Pass durch den Encoder (~O(N²) Zeit aufgrund von Attention, aber effizient mit Optimierungen wie FlashAttention).
*   Anders als CNNs hat ViT keine induktiven Verzerrungen wie Translationsinvarianz – alles wird erlernt.

### Vergleich mit Text-Transformern: Gemeinsamkeiten und Unterschiede

ViT ist grundsätzlich *die gleiche Architektur* wie der Encoder-Teil von Text-Transformern (z.B. BERT), aber angepasst für 2D-Bilddaten. Hier ist ein direkter Vergleich:

| Aspekt               | Text-Transformer (z.B. BERT)                   | Vision Transformer (ViT)                        |
|----------------------|------------------------------------------------|-------------------------------------------------|
| **Eingaberepräsentation** | Sequenz von Tokens (Wörter/Subwörter), eingebettet in Vektoren. | Sequenz von Bild-Patches, eingebettet in Vektoren. Patches sind wie "visuelle Tokens". |
| **Sequenzlänge**     | Variabel (z.B. 512 Tokens für einen Satz).    | Fest, basierend auf Bildgröße/Patch-Größe (z.B. 197 mit [CLS]). |
| **Positionelle Kodierung** | 1D (absolut oder relativ) für Wortreihenfolge. | 1D (erlernbar) für Patch-Reihenfolge (z.B. row-major Abflachung). Keine eingebaute 2D-Struktur. |
| **Kernmechanismus**  | Self-Attention über Tokens, um Abhängigkeiten zu modellieren. | Self-Attention über Patches – gleiche Mathematik, aber achtet auf räumliche "Beziehungen" statt syntaktische. |
| **Ausgabe/Aufgaben** | Encoder für Klassifikation/Masked LM; Decoder für Generierung. | Nur Encoder für Klassifikation; kann für Detektion/Segmentierung erweitert werden. |
| **Stärken**          | Verarbeitet langreichweitige Textabhängigkeiten. | Globaler Kontext in Bildern (z.B. Ganzszenen-Verständnis). |
| **Schwächen**        | Benötigt riesige Textkorpora.                 | Datenhungrig; kämpft auf kleinen Datensätzen ohne CNN-Pre-training. |
| **Vorhersagestil**   | Next-Token-Prediction in Decodern (autoregressiv). | Keine inhärente "Next"-Prediction – klassifiziert das gesamte Bild ganzheitlich. |

Im Wesentlichen ist ViT ein "Plug-and-Play"-Tausch: Ersetze Token-Embeddings durch Patch-Embeddings und du erhältst ein Vision-Modell. Beide verlassen sich auf Attention, um Beziehungen in einer Sequenz zu gewichten, aber Text ist inhärent sequentiell/linear, während Bilder räumlich sind (ViT lernt dies via Attention).

### Behandlung von "Next Token" vs. "Next Pixel" in ViT

Nein, ViT sagt *nicht* den "nächsten Pixel" vorher, so wie ein Text-Transformer das "nächste Token" in der autoregressiven Generierung (z.B. GPT) vorhersagt. Hier ist der Grund:

*   **Text-Transformer (Autoregressiv)**: In Modellen wie GPT generiert der Decoder sequentiell – ein Token nach dem anderen, konditioniert auf alle vorherigen. Für Bilder wäre dies Pixel-für-Pixel in einigen generativen Modellen (z.B. PixelRNN), aber ineffizient.

*   **Ansatz von ViT**: ViT ist *nicht-autoregressiv* und holistisch. Es verarbeitet das *gesamte* Bild (alle Patches) parallel durch den Encoder. Es gibt keine sequentielle "Next"-Prediction während der Inferenz – Attention berechnet Beziehungen über *alle* Patches gleichzeitig. Für Generierungsaufgaben (z.B. Inpainting) könnten ViT-Varianten einen Decoder verwenden, um maskierte Patches autoregressiv vorherzusagen, aber das Basis-ViT ist für Klassifikation, nicht für Generierung.

*   **Warum nicht Pixel?** Individuelle Pixel als Tokens zu behandeln, würde die Sequenzlänge explodieren lassen (z.B. 224×224×3 = ~150K Tokens), was quadratische Attention rechnerisch unpraktikabel macht (O(N²) = Billionen von Operationen). Patches gruppieren ~256 Pixel (16×16) zu einem "Token", was N handhabbar hält (~200).

Wenn du generative Vision (wie Next-Pixel oder Next-Patch) suchst, sieh dir Modelle wie VQ-VAE + Transformer oder Parti an, die auf ViT-Ideen aufbauen.

Weitere Details findest du im Original-Paper: [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929). Wenn du Code-Beispiele (z.B. in PyTorch) oder Vergleiche zu bestimmten Varianten möchtest, lass es mich wissen!