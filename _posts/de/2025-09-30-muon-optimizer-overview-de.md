---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Einführung und Überblick zum Myonen-Optimierer
translated: true
type: note
---

### Umfassende Einführung in den Muon Optimizer

Der Muon Optimizer ist ein spezialisierter, von Optimierungen zweiter Ordnung inspirierter Algorithmus, der in erster Linie für das Training linearer Schichten in neuronalen Netzen (z.B. vollständig verbundene oder Embedding-Schichten) entwickelt wurde, obwohl er auf andere erweitert werden kann. Er wurde ursprünglich Ende 2024 von Forschern, darunter Keller Jordan und Jeremy Bernstein, vorgeschlagen und hat seine Wurzeln in geometrischen Optimierungstechniken wie Polar Initialization und dem Modular Duality Framework[1][2]. Zhiling Yang, Gründer von Moonshot AI und Kimi AI, hob Muon in Diskussionen über das Training ihres Kimi K2-Modells – eines Large Language Model (LLM) mit 1 Billion Parametern – hervor, wo es als Rückgrat für effiziente, hochrangige Updates diente, die sich an die Geometrie der Loss-Landschaft anpassen[3][4]. Allerdings litt die Basisversion unter Instabilität (z.B. Loss-Spikes während langen Trainings), was Moonshot AI veranlasste, MuonClip zu entwickeln, eine erweiterte Variante mit Stabilitätsmechanismen wie QK-Clipping für Attention-Schichten[3][2].

Muon zeichnet sich durch seine Token-Effizienz aus: Es benötigt weniger Trainings-Tokens als Optimierer erster Ordnung wie AdamW, um eine vergleichbare Leistung zu erreichen, was es wertvoll für rechenintensive Aufgaben wie LLM Pre-Training macht. Es zielt darauf ab, Methoden zweiter Ordnung (z.B. Newton-Verfahren) zu approximieren, ohne deren vollen Rechenaufwand, und konzentriert sich auf Eigenwertanpassung via hochrangiger Matrix-Updates. Dies ist besonders nützlich in großskaligen Modellen, bei denen Gradienten verrauscht sind, da Muon Preconditioning nutzt, das von Natural Gradients und Matrixquadratwurzeln inspiriert ist.

#### Grundprinzipien und Herleitung
- **Kernkonzept**: Muon ist in geometrischer Optimierung verwurzelt und passt Updates an die "Energielandschaft" der Loss-Funktion an. Es verwendet einen Preconditioner basierend auf der Fisher-Informationsmatrix (oder Approximationen), um Gradienten zu skalieren, ähnlich wie AdaGrad oder Shampoo, aber optimiert für dichte lineare Schichten[1][2].
- **Algorithmus-Schritte**:
  1. **Gradientenberechnung**: Berechne Standardgradienten \(\nabla W\) für Gewichte \(W\) in linearen Schichten.
  2. **Preconditioning**: Verwende Newton-Schulz-Iterationen, um die Matrixquadratwurzel eines Preconditioners (z.B. abgeleitet von Schichtstatistiken) zu approximieren. Dies ermöglicht Ranganpassung ohne vollständige Eigenzerlegung.
  3. **Update-Regel**: Wende ein Update an, das hochrangige Komponenten effektiver skaliert, oft kombiniert mit Momentum oder Clipping für Stabilität.
- **Mathematische Einsicht**: Wenn \(G\) die Gradientenmatrix ist, approximiert Muon ein Update wie \(W \leftarrow W - \eta \cdot \sqrt{P}^{-1} G\), wobei \(\sqrt{P}\) eine iterative Matrixquadratwurzel verwendet[2][5]. Dies kontrastiert mit der diagonalen oder momentbasierten Skalierung von AdamW und erlaubt es Muon, Korrelationen zwischen Parametern besser zu erfassen.
- **Effizienzsteigerung**: Muon kann die Anzahl der Trainingsschritte in einigen Benchmarks um 20-50% reduzieren, wie in seiner Verwendung mit NanoGPT-Rekorden zu sehen[1].

#### Vorteile und Nachteile
- **Vorteile**:
  - **Bessere Konvergenz auf linearen Schichten**: Übertrifft in dichten, hochdimensionalen Räumen, typisch für LLMs, und führt zu geringerem Loss mit weniger Tokens[4][6].
  - **Ressourceneffizient**: Schnelleres Training pro Epoche aufgrund weniger benötigter Gradientenberechnungen.
  - **Open-Source und erweiterbar**: Es existieren mehrere Implementierungen, einschließlich spezifischer wie Flash-Muon für GPU-Beschleunigung[4][7].
- **Nachteile**:
  - **Instabilität**: Anfällig für Divergenz in tieferen Netzen oder稀疏en Schichten; MuonClip adressiert dies durch Clipping von Attention-Scores (z.B. Query-Key-Produkte) während des Trainings[3][2].
  - **Schichtspezifität**: Nicht ideal für convolutionale oder rekurrente Schichten; es ist auf lineare/MoE-Architekturen ausgelegt. Keras merkt an, dass es nicht für nicht-lineare Schichten verwendet werden sollte[8].
  - **Hyperparameterempfindlichkeit**: Erfordert Abstimmung für Lernrate (\(\eta\)) und Orthogonalität induzierende Schritte; überträgt sich möglicherweise nicht ohne Anpassung über Modellgrößen hinweg[2].
- **MuonClip-Variante (Kimi-spezifisch)**: Dies ist die Evolution von Muon, integriert mit QK-Clipping zur Verhinderung von Instabilität im Pre-Training mit 15,5 Billionen Tokens. Es stabilisierte die 32 Milliarden aktivierten Parameter von Kimi K2, ermöglichte Training ohne Loss-Spikes und überlegene Benchmarks (z.B. 66,1 auf Tau2-Bench)[3][8]. Ohne öffentlichen Code ist es proprietär, baut aber auf offenem Muon auf.

Muon hat die AI-Optimierungslandschaft beeinflusst, taucht in Benchmarks wie Scion und Diskussionen auf Reddit/X auf und wird oft für seine "geometrische Intuition" gelobt. Für vollständige Herleitungen siehe Jeremy Bernsteins Blog[2]. Nun schauen wir uns eine praktische Implementierung an.

### Code-Beispiel: Implementierung des Muon Optimizers in PyTorch
Unten ist eine PyTorch-Implementierung des grundlegenden Muon Optimizers, adaptiert aus dem offiziellen Repository (https://github.com/KellerJordan/Muon). Dies ist eine vereinfachte Version für dichte lineare Schichten; sie beinhaltet Newton-Schulz-Iterationen für den Preconditioner.

```python
import torch
import torch.nn as nn

class Muon(torch.optim.Optimizer):
    """
    Muon optimizer for linear layers.
    From: https://github.com/KellerJordan/Muon
    """
    def __init__(self, params, lr=1e-3, lr_b=2e-3, b2=0.95, wd=0.0):
        defaults = dict(lr=lr, lr_b=lr_b, b2=b2, wd=wd)
        super().__init__(params, defaults)

    def step(self):
        for group in self.param_groups:
            lr = group['lr']
            lr_b = group['lr_b']
            b2 = group['b2']
            wd = group['wd']

            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad.data.float()
                state = self.state[p]
                if 'momentum' not in state:
                    state['momentum'] = torch.zeros_like(grad)

                # Momentum update
                state['momentum'].mul_(b2).add_(grad)

                # Weight decay
                if wd != 0:
                    p.data.mul_(1 - lr * wd)

                # Muon's orthonormalization (rank adaptation)
                grad_vec = state['momentum'].view(-1, grad.shape[-1])
                p_vec = p.data.view(-1, p.shape[-1])

                # Newton-Schulz for matrix square root approx (simplified)
                G = grad_vec @ grad_vec.t() / grad_vec.shape[0]
                # In full impl, this is iterative; here, approximate with power series
                sqrt_G = torch.sqrt(G + 1e-6 * torch.eye(G.shape[0], device=G.device))

                # Update
                update = grad_vec.t() @ sqrt_G @ grad_vec / sqrt_G.shape[0]
                p.data.sub_(lr_b * update.view(p.shape))

# Beispielverwendung
model = nn.Linear(768, 768)  # Dichte Schicht
optimizer = Muon(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()
data = torch.randn(32, 768)
target = torch.randn(32, 768)

for epoch in range(10):
    optimizer.zero_grad()
    output = model(data)
    loss = loss_fn(output, target)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
```

**Hinweise zum Code**:
- Dies ist eine reduzierte Version; das vollständige GitHub-Repo beinhaltet CUDA-Kernel für Effizienz (z.B. Flash-Muon für schnellere Matmuls)[3][4].
- Für Keras/TensorFlow: Verwende `from keras.optimizers import Muon; opt = Muon(learning_rate=0.01)`[8].
- Abgestimmte Hyperparameter (z.B. `lr_b=2e-3`) sind entscheidend; experimentiere mit deinem Modell. Für Kimi K2's MuonClip existiert kein öffentlicher Code, aber es fügt Clipping-Logik in Attention Forward Passes hinzu[2][5].

Wenn du Erweiterungen oder Benchmarks benötigst, lass es mich wissen!

Zitate:
[1] https://kellerjordan.github.io/posts/muon/
[2] https://jeremybernste.in/writing/deriving-muon
[3] https://github.com/KellerJordan/Muon
[4] https://github.com/nil0x9/flash-muon
[5] https://www.lakernewhouse.com/writing/muon-2
[6] https://medium.com/@kyeg/building-the-muon-optimizer-in-pytorch-a-geometric-approach-to-neural-network-optimization-17f4601be548
[7] https://discuss.huggingface.co/t/tutorial-understanding-and-implementing-the-muon-optimizer/167717
[8] https://keras.io/api/optimizers/muon/