---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPU SM-Grenze für maximales Autotune
translated: true
type: note
---

Die Warnung "Not enough SMs to use max_autotune_gemm" stammt von PyTorchs TorchInductor-Backend (verwendet in `torch.compile` mit `mode="max-autotune"` oder ähnlichen aggressiven Autotuning-Modi). Sie zeigt an, dass Ihre GPU weniger Streaming Multiprocessors (SMs) hat als der Schwellenwert, der für die umfassendsten GEMM (Matrix-Multiplikation) Autotuning-Optionen erforderlich ist. Diese Optionen durchsuchen einen riesigen Raum von Triton/CUTLASS-Kernel-Konfigurationen, um die Spitzenleistung zu erreichen.

PyTorch betrachtet eine GPU erst als "groß genug", wenn sie eine beträchtliche Anzahl von SMs hat (typischerweise ≥68–80, abhängig von der genauen PyTorch-Version; z.B. RTX 3080/3090 grenzwertig, A100/H100/RTX 4090 komfortabel darüber). Bei kleineren GPUs (z.B. RTX 3060, 3070, 2080 Ti, T4, etc.) deaktiviert es den vollständigen `max_autotune_gemm`-Pfad, um übermäßige Kompilierzeiten oder suboptimale Auswahl zu vermeiden.

### Warum es passiert und die Auswirkung
- Autotuning benchmarkt viele Kernel-Varianten zur Kompilierzeit. Vollständiges GEMM-Autotuning benötigt genügend Parallelität (SMs), um die aggressivsten Templates sinnvoll zu machen.
- Die Warnung ist **harmlos** – die Kompilierung ist weiterhin erfolgreich und Sie erhalten eine gute (aber nicht die absolute maximale) Leistung. Anderes Autotuning (nicht-GEMM Teile, weniger aggressive GEMM-Suche) läuft weiterhin.
- Es bedeutet **nicht** Padding/Ineffizienz aufgrund von Batch-Größe oder Modellarchitektur, wie man vielleicht denken könnte. Die vom Benutzer vorgeschlagene Interpretation ist nahe dran, aber hier nicht ganz zutreffend – diese spezifische Warnung handelt rein von der GPU-Größe, nicht von Input-/Shape-Padding.

### Wie man es verbessern oder umgehen kann
1. **Verwenden Sie eine GPU mit mehr SMs** (beste Lösung für echte Maximalleistung):
   - Empfohlenes Minimum für zuverlässiges vollständiges `max_autotune_gemm`: RTX 4090 (128 SMs), A100 (108 SMs), H100 (132+ SMs) oder neuere Data-Center-Karten.
   - Consumer-Karten unter ~80 SMs (z.B. RTX 3070 = 46 SMs, RTX 3080 = 68 SMs) lösen dies aus.

   | GPU Beispiel     | SM-Anzahl | Volles max_autotune_gemm? |
   |------------------|-----------|----------------------------|
   | RTX 3060/3070    | 46–58     | Nein                       |
   | RTX 3080/3090    | 68–82     | Grenzwertig (manchmal Ja)  |
   | RTX 4090         | 128       | Ja                         |
   | A100             | 108       | Ja                         |
   | H100             | 132+      | Ja                         |

2. **Ändern des torch.compile-Modus** (keine Hardware-Änderung nötig):
   - Verwenden Sie `mode="max-autotune-no-cudagraphs"` – behält die meisten Autotuning-Vorteile, überspringt aber CUDA Graphs und den SM-gesteuerten GEMM-Pfad. Oft fast genauso schnell mit viel kürzeren Kompilierzeiten auf kleineren GPUs.
   - Oder `mode="reduce-overhead"` – leichter, verwendet CUDA Graphs für niedrige Latenz, gut für Inference.
   - Beispiel:
     ```python
     compiled_model = torch.compile(model, mode="max-autotune-no-cudagraphs", fullgraph=True)
     ```

3. **Aktivieren von hochpräzisen Matmuls** (hilft in jedem Modus/jeder GPU):
   ```python
   torch.set_float32_matmul_precision("high")  # oder "highest"
   ```
   Dies erlaubt TensorFloat-32 / bessere cuBLAS-Kernel.

4. **Erzwingen von aggressiverem Tuning trotzdem** (hacky, nicht offiziell unterstützt):
   - Monkey-patching der Prüfung im PyTorch-Quellcode (bearbeite `torch/_inductor/utils.py` oder Runtime-Patch), um den SM-Schwellenwert zu senken. Riskant und kann die Leistung beeinträchtigen oder die Kompilierzeit explodieren lassen.

5. **Andere allgemeine Tipps für bessere Ausrichtung/Effizienz** (nicht verwandt mit dieser exakten Warnung, aber adressiert Ihr Padding-Anliegen):
   - Padden Sie Batch-/Sequenz-Dimensionen auf Vielfache von 8/16/32, wenn möglich (üblich für Tensor Cores).
   - Erhöhen Sie die Batch-Größe, wenn Ihre Workload es erlaubt – größere GEMMs nutzen die GPU besser aus.
   - Für Inference-fokussierte Workloads, ziehen Sie Alternativen wie vLLM, TensorRT-LLM oder Hugging Face Optimum in Betracht, wenn `torch.compile`-Einschränkungen bestehen bleiben.

In den meisten realen Fällen ist der Leistungsunterschied durch das Fehlen von vollständigem `max_autotune_gemm` klein (ein paar Prozent), und `max-autotune-no-cudagraphs` bringt Sie auf Consumer-GPUs zu 95 %+ dorthin.

[PyTorch Inductor utils.py Quelle](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/utils.py)
[Torch.compile Warnungsdiskussion](https://discuss.pytorch.org/t/torch-compile-warning-not-enough-sms-to-use-max-autotune-gemm-mode/184405)
[Dissecting torch.compile](https://themlsurgeon.substack.com/p/dissecting-torchcompile-surgical)