---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: FlashAttention löst den Speicher-Engpass von Transformern
translated: true
type: note
---

### Hintergrund: Die Herausforderungen von Standard-Attention in Transformern

Transformer, die Grundlage von Modellen wie GPT und BERT, verlassen sich stark auf den Self-Attention-Mechanismus zur Verarbeitung von Sequenzen. Bei der Self-Attention werden Eingabesequenzen als Query-Matrix \\(Q\\), Key-Matrix \\(K\\) und Value-Matrix \\(V\\) dargestellt (jeweils mit der Form \\(N \times d\\), wobei \\(N\\) die Sequenzlänge und \\(d\\) die Head-Dimension, typischerweise 64-128, ist). Die Attention-Ausgabe \\(O\\) wird wie folgt berechnet:

\\[
S = QK^T \in \mathbb{R}^{N \times N}, \quad P = \softmax(S) \in \mathbb{R}^{N \times N}, \quad O = PV \in \mathbb{R}^{N \times d},
\\]

wobei \\(\softmax\\) zeilenweise angewendet wird und \\(S\\) oft zur Stabilisierung um \\(\tau = 1 / \sqrt{d}\\) skaliert wird. Zusätzliche Operationen wie kausales Maskieren (für autoregressive Modelle) und Dropout sind üblich.

Diese Formulierung ist elegant, aber rechenintensiv. Die Zwischenmatrizen \\(S\\) und \\(P\\) sind \\(N \times N\\), was zu einer **quadratischen Zeit- und Speicherkomplexität** \\(O(N^2)\\) in der Sequenzlänge \\(N\\) führt. Bei langen Kontexten (z.B. \\(N = 4096\\) in GPT-2 oder bis zu 128k in modernen LLMs) wird dies zu einem ernsthaften Engpass:

- **Speicherhungrig**: Auf GPUs ist High-Bandwidth Memory (HBM) der primäre Speicher, aber die Materialisierung von \\(S\\) und \\(P\\) kann den verfügbaren HBM-Speicher überschreiten (z.B. 40-80 GB auf A100/H100). Bei \\(N=4096\\), \\(d=64\\) verbraucht dies allein für die Zwischenergebnisse ~1-2 GB, plus Eingaben/Ausgaben/Aktivierungen, was häufig zu Out-of-Memory (OOM) Fehlern führt.
- **Geschwindigkeitsbegrenzungen**: Attention ist speichergebunden, nicht rechengebunden. Moderne GPUs (z.B. NVIDIA A100) haben eine HBM-Bandbreite von ~1,5 TB/s, aber ~19 TFLOPS Rechenleistung – dennoch erfordern Operationen wie Softmax das mehrmalige Lesen/Schreiben der gesamten \\(N^2\\)-Matrix (z.B. 4-6 HBM-Zugriffe pro Element in Vorwärts-/Rückwärtspässen). Dies führt zu quadratisch skalierten Laufzeiten: z.B. Vorwärtspass ~36 ms bei \\(N=4096\\) in PyTorch, Rückwärtspass ~88 ms.
- **Trainings-/Generierungsbarrieren**: Während des Trainings erfordern Gradienten das Speichern von \\(P\\) für den Rückwärtspass, was den Speicherbedarf verdoppelt. Für das Inferenz-Szenario sind lange Kontexte (z.B. 64k Tokens) ohne Approximationen wie Sparse Attention oder Low-Rank-Methoden (z.B. Reformer, Linformer) nicht machbar, die Exaktheit gegen Effizienz eintauschen, aber aufgrund der Vernachlässigung von I/O-Kosten oft schlechter abschneiden.

FlashAttention (eingeführt 2022 von Tri Dao et al.) adressiert dies, indem es den Algorithmus überdenkt, um **I/O-bewusst** zu sein und die GPU-Speicherhierarchie (schneller SRAM ~20 MB vs. langsamer HBM) ohne Approximationen auszunutzen.

### Kernideen: Tiling, Kernel-Fusion und Online Softmax

FlashAttention berechnet **exakte** Attention (keine Approximationen) durch:

1.  **Tiling**: Anstatt die vollständigen \\(N \times N\\)-Matrizen zu materialisieren, unterteilt es \\(Q, K, V\\) in kleine Blöcke, die in den SRAM passen. \\(Q\\) wird in \\(T_r = \lceil N / B_r \rceil\\) Zeilenblöcke der Größe \\(B_r \times d\\) (z.B. \\(B_r \approx 64-256\\)) aufgeteilt und \\(K, V\\) in \\(T_c = \lceil N / B_c \rceil\\) Spaltenblöcke der Größe \\(B_c \times d\\) (z.B. \\(B_c \approx 128-1024\\)). Die Blockgrößen werden dynamisch basierend auf der SRAM-Kapazität \\(M\\) (z.B. \\(B_c \approx M / (4d)\\)) gewählt, um die Wiederverwendung zu maximieren.

2.  **Kernel-Fusion**: Alle Operationen (Matmul für \\(S\\), Maskieren, Softmax, Dropout, Matmul für \\(O\\)) werden in einen einzigen CUDA-Kernel fusioniert. Dies vermeidet das Schreiben von Zwischenergebnissen in den HBM und reduziert die I/O um ~50-70%. Der Kernel lädt Blöcke vom HBM in den SRAM, führt die Berechnung on-Chip durch und schreibt nur Teilsummen zurück – z.B. ein HBM-Lese-/Schreibzugriff pro Block statt pro Element.

3.  **Online Softmax mit Statistiken**: Softmax kann nicht teilweise ohne die vollständige Zeile berechnet werden, daher verwendet FlashAttention eine **assoziative Zerlegung** für die inkrementelle Berechnung. Für eine in Blöcke unterteilte Zeile \\(x = [x^{(1)}; x^{(2)}]\\) werden laufende Statistiken verfolgt:
    - Zeilenmaximum \\(m_i = \max_j S_{ij}\\),
    - Zeilensumme der Exponentialwerte \\(\ell_i = \sum_j \exp(S_{ij} - m_i)\\).

    Die Aktualisierung für einen neuen Block \\(x^{(t)}\\) mit lokalen Statistiken \\(\tilde{m}_t, \tilde{\ell}_t\\) erfolgt durch:
    \\[
    m_i^{\new} = \max(m_i, \tilde{m}_t), \quad \ell_i^{\new} = e^{m_i - m_i^{\new}} \ell_i + e^{\tilde{m}_t - m_i^{\new}} \tilde{\ell}_t.
    \\]
    Das partielle Softmax-Ergebnis ist dann \\(\tilde{P}_{ij} = \exp(S_{ij} - m_i^{\new})\\), und die Ausgabe akkumuliert sich als \\(O_i \leftarrow \frac{\ell_i}{\ell_i^{\new}} e^{m_i - m_i^{\new}} O_i + \frac{\tilde{\ell}_t}{\ell_i^{\new}} e^{\tilde{m}_t - m_i^{\new}} \tilde{P}_{ij} V_j\\).

    Dies ist numerisch stabil (entspricht fusioniertem Softmax) und exakt, wie induktiv bewiesen werden kann: Nach allen Blöcken gilt \\(O = \softmax(S) V\\).

Diese Ideen reduzieren den **Speicherbedarf auf \\(O(N)\\)** (Eingaben + Ausgabe + \\(O(N)\\) Statistiken wie \\(m, \ell\\)) und die **HBM-Zugriffe auf \\(O(N^2 d / M)\\)** – sub-quadratisch, da jedes \\(K/V\\)-Element einmal gelesen wird und \\(Q/O\\) \\(T_c \approx N d / M\\) Mal gelesen wird.

### Vorwärtspass: Blockweise Berechnung

Der Vorwärtspass (Pseudocode im Algorithmus 2 des Papers) iteriert über Spaltenblöcke von \\(K, V\\):

- Initialisiere \\(O = 0^{N \times d}\\), \\(m = -\infty^N\\), \\(\ell = 0^N\\) im HBM.
- Für jeden Spaltenblock \\(j = 1\\) bis \\(T_c\\):
  - Lade \\(K_j, V_j\\) in den SRAM (Wiederverwendung über Zeilen).
  - Für jeden Zeilenblock \\(i = 1\\) bis \\(T_r\\):
    - Lade \\(Q_i, O_i, m_i, \ell_i\\) in den SRAM.
    - Berechne lokales \\(S_{ij} = \tau Q_i K_j^T\\) (\\(B_r \times B_c\\)).
    - Maskiere: \\(S_{ij}^{\masked} = \mask(S_{ij})\\) (z.B. kausal: untere Dreiecksmatrix auf \\(-\infty\\)).
    - Lokale Softmax-Statistiken: \\(\tilde{m}_{ij} = \rowmax(S_{ij}^{\masked})\\), \\(\tilde{P}_{ij} = \exp(S_{ij}^{\masked} - \tilde{m}_{ij})\\), \\(\tilde{\ell}_{ij} = \rowsum(\tilde{P}_{ij})\\).
    - Aktualisiere globale Statistiken und Ausgabe mit den obigen Formeln, wende Dropout auf \\(\tilde{P}_{ij}\\) an.
    - Schreibe aktualisierte \\(O_i, m_i, \ell_i\\) in den HBM.

Dies fusioniert alles: Die gesamten FLOPs bleiben bei \\(O(N^2 d)\\), aber die I/O sinkt dramatisch (z.B. 9x weniger Zugriffe als Standard). Für kausale Attention ist das Maskieren günstig (vektorisiert). Dropout verwendet einen gemeinsamen RNG-Zustand \\(R\\), der für den Rückwärtspass gespeichert wird.

### Rückwärtspass: Gradientenberechnung via Rekomputation

Der Rückwärtspass (Algorithmus 4) ist kniffliger, da Gradienten von \\(P\\) abhängen:

\\[
dP = dO \cdot V^T, \quad dS = P \odot (dP - \rowsum(dO \odot O)), \quad dQ = dS \cdot K, \quad dK = Q^T \cdot dS, \quad dV = P^T \cdot dO.
\\]

Das Speichern von \\(P\\) wäre \\(O(N^2\\), daher **rekomputiert** FlashAttention **Blöcke on-the-fly** (selektive Rekomputation, ähnlich wie Checkpointing, aber getiled):

- Iteriere ähnlich: Für jedes \\(j\\), lade \\(K_j, V_j\\); initialisiere lokales \\(dK_j, dV_j = 0\\).
- Für jedes \\(i\\): Rekomputiere \\(S_{ij}, P_{ij}\\) unter Verwendung der gespeicherten \\(m_i, \ell_i\\); regeneriere die Dropout-Maske aus \\(R\\).
- Berechne lokale Gradienten: \\(dV_j += P_{ij}^{dropped^T} dO_i\\), \\(dP_{ij} = dO_i V_j^T \odot Z_{ij}\\) (Dropout-Maske), \\(dS_{ij} = P_{ij} \odot (dP_{ij} - D_i)\\) wobei \\(D_i = \rowsum(dO_i \odot O_i)\\).
- Akkumuliere \\(dQ_i += \tau dS_{ij} K_j\\), \\(dK_j += \tau Q_i^T dS_{ij}\\).

Dies verwendet weitere \\(O(N^2 d)\\) FLOPs, aber nur \\(O(N)\\) zusätzlichen Speicher (keine \\(P\\)-Speicherung). Gesamt Vorwärts + Rückwärts: ~2-3x die FLOPs von Standard, aber 2-4x schneller aufgrund der I/O-Einsparungen.

### I/O-Bewusstsein und GPU-Optimierungen

GPUs haben eine Hierarchie: Register/SRAM (schnell, klein) >> HBM (langsam, groß). Standard-Attention überlastet den HBM mit \\(\Theta(N^2)\\) Zugriffen pro Durchlauf. Das Tiling von FlashAttention stellt sicher:
- \\(K, V\\) werden einmal geladen (\\(O(N d)\\)).
- \\(Q, O\\) werden \\(T_c \approx N / B_c \approx N d / M\\) Mal geladen (\\(O(N^2 d / M)\\)).
- Untere Schranke: Kein exakter Algorithmus schlägt \\(\Omega(N^2 d^2 / M)\\) für den mittleren Bereich von \\(M\\).

Empirisch: Auf A100 dominieren HBM-Stalls die Laufzeit; FlashAttention reduziert sie um 50-80% und erreicht das rechengebundene Regime. Es unterstützt Block-Sparsität (überspringe Null-Masken-Blöcke) für noch größere Gewinne (2-4x über dicht).

### Vorteile: Geschwindigkeit, Speicher und Downstream-Auswirkungen

- **Speicher**: Linear \\(O(N d)\\), ermöglicht 64k+ Sequenzen auf einzelnen GPUs (vs. 2k-4k Standard). Z.B. 13 GB bei \\(N=65k\\) vs. 200+ GB Standard.
- **Geschwindigkeit**: 2-4x End-to-End beim GPT/BERT-Training; bis zu 7x bei reiner Attention. Z.B. kombiniert fwd/bwd: 0,43 ms bei \\(N=128\\) bis 9s bei \\(N=65k\\) (vs. PyTorch OOM).
- **Qualität**: Exakt, daher kein Perplexity-Verlust. Ermöglicht längere Kontexte: 0,7 Punkte Perplexity-Gewinn auf GPT-2 bei 4x Länge; State-of-the-Art bei Langdokument-Aufgaben (z.B. 63% auf Path-256 bei 64k Sequenzen).
- **Erweiterungen**: FlashAttention-2 (2023) fügt bessere Parallelität hinzu (bis zu 2x schneller); FlashAttention-3 (2024) verwendet Asynchronie/Niedrige Präzision für H100 (50% schneller).

### PyTorch-Integration: Nahtlose Verwendung

PyTorch 2.0+ integriert FlashAttention nativ via `torch.nn.functional.scaled_dot_product_attention(q, k, v)`, das automatisch zum fusionierten Kernel dispatcht, wenn Bedingungen erfüllt sind (z.B. zusammenhängende Tensoren, unterstützte Datentypen). Kein benutzerdefiniertes CUDA nötig:

```python
import torch
from torch.nn.functional import scaled_dot_product_attention

q, k, v = torch.randn(1, 8, 1024, 64, device='cuda')  # Batch, Heads, Seq, Dim
with torch.backends.cuda.sdp_kernel(enable_flash=True, enable_math=False):
    out = scaled_dot_product_attention(q, k, v, attn_mask=mask, dropout_p=0.1)
```

Dies behandelt Maskieren/Dropout; fällt auf Math-Kernel zurück, falls nicht unterstützt. Für benutzerdefinierte Modelle ist es ein Drop-in-Ersatz für manuelle Attention-Schleifen und liefert out-of-the-box 2-3x Beschleunigungen.

FlashAttention revolutionierte das Training mit langen Kontexten und treibt Modelle wie Llama-2 (4k→70B) und darüber hinaus an.

[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)  
[PyTorch 2.2: FlashAttention-v2 Integration](https://pytorch.org/blog/pytorch2-2/)  
[GitHub: Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)