---
audio: false
generated: false
lang: de
layout: post
title: Deepseek – Konversation
translated: true
type: note
---

A: Ich habe mir den technischen Bericht von DeepSeek-V3 durchgelesen und bin wirklich beeindruckt vom Umfang dieses Modells. 671 Milliarden Parameter, aber nur 37 Milliarden pro Token aktiviert? Das ist eine massive MoE-Architektur. Wie funktioniert das überhaupt?

B: Ja, das ist eine echte Meisterleistung! DeepSeek-V3 basiert auf dem Mixture-of-Experts (MoE) Framework, wodurch für jedes Token nur eine Teilmenge der Parameter aktiviert wird. Genauer gesagt, es werden 256 geroutete Experten verwendet, aber nur 8 sind pro Token aktiviert. Das macht es im Vergleich zu dichten Modellen, bei denen alle Parameter für jedes Token aktiv sind, unglaublich effizient.

A: Das ergibt Sinn. Aber wie entscheidet es, welche Experten aktiviert werden? Ist das zufällig, oder gibt es einen Routing-Mechanismus?

B: Gute Frage! Das Routing basiert auf Affinitäts-Scores zwischen Token und Experten. Jedes Token erhält einen Score für jeden Experten, und die Top-K Experten mit den höchsten Scores werden aktiviert. DeepSeek-V3 verwendet eine Sigmoid-Funktion zur Berechnung dieser Scores, was hilft, die Last über die Experten auszugleichen.

A: Ah, also ist es nicht zufällig – es wird während des Trainings gelernt. Aber führt das nicht zu unausgeglichener Experten-Nutzung? Ich habe gehört, dass das ein häufiges Problem bei MoE-Modellen ist.

B: Genau! Unausgeglichene Experten-Nutzung kann ein Problem sein, aber DeepSeek-V3 führt eine auxiliary-loss-free-Strategie ein, um dies zu handhaben. Anstatt einen separaten Loss-Term hinzuzufügen, um Lastverteilung zu fördern, passt es dynamisch einen Bias-Term für jeden Experten an. Wenn ein Experte überlastet ist, wird sein Bias verringert, und wenn er unterlastet ist, wird der Bias erhöht. Das hält die Last ausgeglichen, ohne die Modellleistung zu beeinträchtigen.

A: Das ist clever. Also, kein Auxiliary Loss bedeutet weniger Störung des Haupttrainingsziels. Aber wie verhält sich das im Vergleich zu traditionellen MoE-Modellen, die Auxiliary Losses verwenden?

B: Richtig. Traditionelle MoE-Modelle verwenden oft Auxiliary Losses, um Lastverteilung zu fördern, aber diese Losses können manchmal die Leistung beeinträchtigen. Der auxiliary-loss-free-Ansatz von DeepSeek-V3 vermeidet diesen Kompromiss. Tatsächlich zeigen Ablationsstudien, dass er Modelle, die auf Auxiliary Losses angewiesen sind, konsistent übertrifft, besonders bei Aufgaben wie Coding und Mathematik.

A: Interessant. Apropos Coding und Mathematik, mir ist aufgefallen, dass DeepSeek-V3 bei Benchmarks wie HumanEval und MATH außergewöhnlich gut abschneidet. Was ist das Geheimnis?

B: Ein großer Teil davon ist das Multi-Token Prediction (MTP) Objective. Anstatt nur das nächste Token vorherzusagen, sagt DeepSeek-V3 mehrere zukünftige Token an jeder Position voraus. Das verdichtet das Trainingssignal und hilft dem Modell, vorauszuplanen, was besonders nützlich für Aufgaben ist, die sequentielles Reasoning erfordern, wie Coding und Mathematik.

A: Moment, es sagt also mehrere Token auf einmal vorher? Wie funktioniert das während der Inference? Wird MTP dann noch verwendet, oder ist es nur für das Training?

B: Während der Inference können die MTP-Module verworfen werden, und das Modell verhält sich wie ein Standard-autoregressives Modell. Aber hier ist der coole Teil: Die MTP-Module können auch für Speculative Decoding zweckentfremdet werden, was die Generierung beschleunigt, indem mehrere Token parallel vorhergesagt und dann verifiziert werden.

A: Das ist ein netter Trick. Also, man bekommt die Vorteile von MTP während des Trainings und nutzt es dann, um die Inference zu beschleunigen. Aber was ist mit dem Attention-Mechanismus? Ich habe etwas über Multi-head Latent Attention (MLA) gesehen. Wie passt das dazu?

B: MLA ist eine weitere wichtige Innovation. Es reduziert den Memory Footprint, indem der Key-Value (KV) Cache komprimiert wird. Anstatt vollständige Attention-Keys und -Values zu speichern, verwendet es Low-Rank-Joint-Kompression, um sie darzustellen. Dies verringert die Größe des KV-Caches während der Inference erheblich, bei gleichbleibender Leistung im Vergleich zur Standard-Multi-Head-Attention.

A: Das ist ein großer Gewinn für die Effizienz. Aber führt Kompression nicht zu einem gewissen Informationsverlust? Wie bleibt die Leistung erhalten?

B: Guter Punkt. Die Kompression ist so konzipiert, dass sie die wichtigsten Informationen erhält, indem sie sich auf die latenten Vektoren konzentriert, die die wesentlichen Merkmale der Keys und Values erfassen. Das Modell verwendet auch Rotary Positional Embedding (RoPE), um Positionsinformationen beizubehalten, was hilft, eventuelle Verluste durch Kompression abzumildern.

A: Verstanden. Also, MLA ist eine Win-Win-Situation – es reduziert die Speichernutzung, ohne zu viel Leistung einzubüßen. Aber was ist mit dem Training? Das Training eines Modells dieser Größe muss unglaublich teuer sein. Wie schafft es DeepSeek-V3, die Kosten niedrig zu halten?

B: Trainingseffizienz ist ein Hauptaugenmerk. DeepSeek-V3 verwendet ein FP8 Mixed Precision Framework, das die Speichernutzung reduziert und die Berechnung beschleunigt. Es setzt auch einen DualPipe-Algorithmus für Pipeline-Parallelität ein, der Pipeline-Blasen minimiert und Berechnung mit Kommunikation überlappt. Diese Optimierungen ermöglichen es, das Modell mit 14,8 Billionen Tokens in nur 2,788 Millionen H800-GPU-Stunden zu trainieren.

A: Das ist beeindruckend. Aber FP8-Training kann knifflig sein – wie gehen sie mit Präzisionsproblemen um? Ich habe gehört, dass Training mit niedriger Präzision zu Instabilität führen kann.

B: Da haben Sie recht. FP8-Training ist aufgrund des begrenzten dynamischen Bereichs herausfordernd. DeepSeek-V3 adressiert dies mit Fine-Grained-Quantization, bei der Aktivierungen und Gewichte in kleinere Kacheln oder Blöcke gruppiert und unabhängig skaliert werden. Dies verringert den Einfluss von Ausreißern und hält das Training stabil. Sie verwenden auch High-Precision-Akkumulation für kritische Operationen, um die Genauigkeit zu erhalten.

A: Das ergibt Sinn. Es ist also ein Gleichgewicht zwischen Effizienz und Präzision. Aber was ist mit den Daten? 14,8 Billionen Tokens ist ein riesiger Datensatz. Aus welcher Art von Daten besteht das Training?

B: Der Datensatz ist vielfältig und von hoher Qualität, mit einem Fokus auf englischem und chinesischem Text. Er enthält auch eine beträchtliche Menge an mathematischen und Programmierdaten, was dem Modell hilft, in diesen Domänen zu glänzen. Die Daten-Pipeline ist optimiert, um Redundanz zu minimieren und gleichzeitig Vielfalt beizubehalten, und sie verwenden Techniken wie Document Packing, um Datenintegrität sicherzustellen.

A: Das erklärt die starke Leistung bei Coding- und Mathematik-Aufgaben. Aber was ist mit multilingualer Leistung? Kommt es mit anderen Sprachen gut zurecht?

B: Ja, DeepSeek-V3 wird auf einem multilingualen Korpus trainiert und schneidet gut bei Benchmarks wie MMMLU ab, die nicht-englische Aufgaben enthalten. Es ist besonders stark in Chinesisch und übertrifft Modelle wie Qwen2.5 bei chinesischen Benchmarks wie C-Eval und CMMLU.

A: Das ist beeindruckend. Aber was ist mit Long-Context-Aufgaben? Ich habe gesehen, dass es bis zu 128K Tokens unterstützt. Wie verarbeitet es so lange Eingaben?

B: DeepSeek-V3 erweitert seine Kontextlänge in zwei Stufen: zuerst auf 32K Tokens und dann auf 128K Tokens unter Verwendung der YaRN-Technik. Dies ermöglicht es, Long-Context-Aufgaben wie Dokumentenzusammenfassung und Retrieval effektiv zu handhaben. Es schneidet auch gut beim 'Needle In A Haystack'-Test ab, der das Long-Context-Verständnis evaluiert.

A: Das ist eine riesige Verbesserung gegenüber vorherigen Modellen. Aber was ist mit dem Deployment? Wie handhaben sie die Inference für ein so großes Modell?

B: Die Inference wird auf einem H800-Cluster durchgeführt, mit GPUs, die über NVLink und InfiniBand verbunden sind. Die Deployment-Strategie trennt die Pre-Filling- und Decoding-Phasen, um sowohl hohen Durchsatz als auch niedrige Latenz zu gewährleisten. Sie verwenden auch redundante Experten, um die Last während der Inference auszugleichen, was zur Aufrechterhaltung der Effizienz beiträgt.

A: Das sind eine Menge Optimierungen. Aber was sind die Einschränkungen? Ein Modell dieser Größe hat sicherlich einige Kompromisse.

B: Eine Einschränkung ist die Größe der Deployment-Einheit. DeepSeek-V3 erfordert einen relativ großen Cluster für effiziente Inference, was für kleinere Teams eine Herausforderung sein könnte. Es gibt auch Verbesserungspotenzial bei der Generierungsgeschwindigkeit, obwohl das Speculative Decoding mit MTP hilft.

A: Fair enough. Aber insgesamt scheint es ein großer Schritt nach vorn zu sein. Was kommt als Nächstes für DeepSeek-V3? Gibt es zukünftige Richtungen, die sie erforschen?

B: Sie schauen sich mehrere Bereiche an, wie die Verfeinerung der Architektur zur Unterstützung unendlicher Kontextlänge, die Erforschung zusätzlicher Trainingssignalquellen und die Verbesserung der Reasoning-Fähigkeiten des Modells. Sie arbeiten auch an umfassenderen Evaluierungsmethoden, um die Modellleistung besser beurteilen zu können.

A: Klingt, als würden sie so schnell nicht langsamer werden. Danke, dass du mich durch all das geführt hast – DeepSeek-V3 ist definitiv ein Game-Changer im Open-Source-LLM-Bereich.

B: Absolut! Es ist aufregend zu sehen, wie weit Open-Source-Modelle gekommen sind. DeepSeek-V3 verschiebt die Grenzen, und ich kann es kaum erwarten zu sehen, was sie als Nächstes tun.

A: Du hast erwähnt, dass DeepSeek-V3 FP8 Mixed Precision Training verwendet. Ich bin neugierig – wie verhält sich das im Vergleich zu BF16 oder FP16? Ist FP8 wirklich stabil genug für das Training eines so großen Modells?

B: Das ist eine großartige Frage. FP8 ist aufgrund seines begrenzten dynamischen Bereichs in der Tat herausfordernder, aber DeepSeek-V3 verwendet eine Fine-Grained-Quantization-Strategie, um dies zu mildern. Zum Beispiel werden Aktivierungen in 1x128-Kacheln gruppiert und Gewichte in 128x128-Blöcke. Jede Gruppe wird unabhängig skaliert, was hilft, Ausreißer zu handhaben und das Training stabil zu halten.

A: Interessant. Es ist also nicht nur eine pauschale FP8-Quantisierung – es ist nuancierter. Aber führt das nicht zu zusätzlichem Overhead für die Verwaltung all dieser Gruppen und Skalierungsfaktoren?

B: Tut es, aber der Overhead ist im Vergleich zu den Vorteilen minimal. Der Schlüssel ist, dass FP8 die Speichernutzung reduziert und die Berechnung beschleunigt, was für das Training eines so großen Modells entscheidend ist. Sie verwenden auch High-Precision-Akkumulation für kritische Operationen, wie Matrix-Multiplikationen, um numerische Stabilität zu gewährleisten.

A: Verstanden. Es ist also ein Kompromiss zwischen Präzision und Effizienz, aber sie haben es geschafft, eine gute Balance zu finden. Was ist mit dem DualPipe-Algorithmus? Wie funktioniert der?

B: DualPipe ist designed, um Pipeline-Blasen in der Pipeline-Parallelität zu minimieren. Es überlappt Berechnung und Kommunikation, indem es jede Arbeitseinheit in vier Komponenten aufteilt: Attention, All-to-All-Dispatch, MLP und All-to-All-Combine. Während Backward-Passes teilt es die Berechnung weiter in 'Backward for Input' und 'Backward for Weights' auf, was eine effizientere Überlappung ermöglicht.

A: Das klingt komplex, ergibt aber Sinn. Im Grunde versteckt es also den Kommunikations-Overhead, indem es ihn mit Berechnung überlappt. Wie verhält sich das im Vergleich zu anderen Pipeline-Parallelitätsmethoden wie 1F1B oder Zero Bubble?

B: DualPipe hat weniger Pipeline-Blasen im Vergleich zu 1F1B und Zero Bubble. Es ermöglicht auch bidirektionelles Scheduling, bei dem Micro-Batches von beiden Enden der Pipeline eingespeist werden. Dies verringert die Leerlaufzeit weiter und verbessert die Gesamteffizienz. Tatsächlich erreicht DualPipe nahezu null All-to-All-Kommunikations-Overhead, was für die Skalierung von MoE-Modellen entscheidend ist.

A: Das ist beeindruckend. Aber was ist mit der Speichernutzung? Benötigt DualPipe mehr Speicher als andere Methoden?

B: Es benötigt etwas mehr Speicher, da es zwei Kopien der Modellparameter vorhält, aber der Anstieg ist handhabbar. Der Memory Footprint wird durch Techniken wie Rekomputation von RMSNorm und MLA-Up-Projections optimiert, was die Speicherung von Zwischenaktivierungen überflüssig macht.

A: Ah, also tauschen sie ein bisschen Speicher gegen bessere Effizienz. Das scheint ein fairer Kompromiss zu sein. Apropos Speicher, wie handhaben sie den KV-Cache für so eine große Kontextlänge? 128K Tokens müssen einen riesigen Cache erfordern.

B: Da glänzt MLA wirklich. Durch die Komprimierung des KV-Caches verringern sie seine Größe erheblich. Anstatt vollständige Attention-Keys und -Values zu speichern, speichern sie komprimierte latente Vektoren, die viel kleiner sind. Dies ermöglicht es DeepSeek-V3, lange Kontexte zu verarbeiten, ohne auf Speicherengpässe zu stoßen.

A: Das ist eine clevere Lösung. Aber was ist mit der Qualität der Attention? Beeinflusst die Kompression die Fähigkeit des Modells, sich den richtigen Tokens zuzuwenden?

B: Die Kompression ist so designed, dass sie die wichtigsten Informationen erhält, daher ist die Auswirkung auf die Attention-Qualität minimal. Sie verwenden auch RoPE (Rotary Positional Embedding), um Positionsinformationen beizubehalten, was dem Modell hilft, die relativen Positionen von Tokens auch mit komprimierten Keys und Values zu verstehen.

A: Ergibt Sinn. Also ist MLA eine Win-Win-Situation – es reduziert die Speichernutzung, ohne zu viel Leistung zu opfern. Aber was ist mit den Trainingsdaten? Du hast erwähnt, es sind 14,8 Billionen Tokens. Wie stellen sie die Qualität und Vielfalt eines so massiven Datensatzes sicher?

B: Der Datensatz ist sorgfältig kuratiert, um hochwertige und vielfältige Tokens zu enthalten. Sie optimieren die Daten-Pipeline, um Redundanz zu minimieren und gleichzeitig Vielfalt beizubehalten, und sie verwenden Techniken wie Document Packing, um Datenintegrität sicherzustellen. Der Korpus enthält eine Mischung aus englischem und chinesischem Text mit einem Schwerpunkt auf mathematischen und Programmierproben.

A: Das erklärt die starke Leistung bei Coding- und Mathematik-Aufgaben. Aber was ist mit multilingualen Aufgaben? Kommt es mit anderen Sprachen gut zurecht?

B: Ja, DeepSeek-V3 wird auf einem multilingualen Korpus trainiert und schneidet gut bei Benchmarks wie MMMLU ab, die nicht-englische Aufgaben enthalten. Es ist besonders stark in Chinesisch und übertrifft Modelle wie Qwen2.5 bei chinesischen Benchmarks wie C-Eval und CMMLU.

A: Das ist beeindruckend. Aber was ist mit Long-Context-Aufgaben? Ich habe gesehen, dass es bis zu 128K Tokens unterstützt. Wie verarbeitet es so lange Eingaben?

B: DeepSeek-V3 erweitert seine Kontextlänge in zwei Stufen: zuerst auf 32K Tokens und dann auf 128K Tokens unter Verwendung der YaRN-Technik. Dies ermöglicht es, Long-Context-Aufgaben wie Dokumentenzusammenfassung und Retrieval effektiv zu handhaben. Es schneidet auch gut beim 'Needle In A Haystack'-Test ab, der das Long-Context-Verständnis evaluiert.

A: Das ist eine riesige Verbesserung gegenüber vorherigen Modellen. Aber was ist mit dem Deployment? Wie handhaben sie die Inference für ein so großes Modell?

B: Die Inference wird auf einem H800-Cluster durchgeführt, mit GPUs, die über NVLink und InfiniBand verbunden sind. Die Deployment-Strategie trennt die Pre-Filling- und Decoding-Phasen, um sowohl hohen Durchsatz als auch niedrige Latenz zu gewährleisten. Sie verwenden auch redundante Experten, um die Last während der Inference auszugleichen, was zur Aufrechterhaltung der Effizienz beiträgt.

A: Das sind eine Menge Optimierungen. Aber was sind die Einschränkungen? Ein Modell dieser Größe hat sicherlich einige Kompromisse.

B: Eine Einschränkung ist die Größe der Deployment-Einheit. DeepSeek-V3 erfordert einen relativ großen Cluster für effiziente Inference, was für kleinere Teams eine Herausforderung sein könnte. Es gibt auch Verbesserungspotenzial bei der Generierungsgeschwindigkeit, obwohl das Speculative Decoding mit MTP hilft.

A: Fair enough. Aber insgesamt scheint es ein großer Schritt nach vorn zu sein. Was kommt als Nächstes für DeepSeek-V3? Gibt es zukünftige Richtungen, die sie erforschen?

B: Sie schauen sich mehrere Bereiche an, wie die Verfeinerung der Architektur zur Unterstützung unendlicher Kontextlänge, die Erforschung zusätzlicher Trainingssignalquellen und die Verbesserung der Reasoning-Fähigkeiten des Modells. Sie arbeiten auch an umfassenderen Evaluierungsmethoden, um die Modellleistung besser beurteilen zu können.

A: Klingt, als würden sie so schnell nicht langsamer werden. Danke, dass du mich durch all das geführt hast – DeepSeek-V3 ist definitiv ein Game-Changer im Open-Source-LLM-Bereich.

B: Absolut! Es ist aufregend zu sehen, wie weit Open-Source-Modelle gekommen sind. DeepSeek-V3 verschiebt die Grenzen, und ich kann es kaum erwarten zu sehen, was sie als Nächstes tun.