---
audio: false
generated: true
lang: de
layout: post
title: Menschengestütztes bestärkendes Lernen (RLHF) erklärt
translated: true
type: note
---

**Reinforcement Learning from Human Feedback (RLHF)** ist eine Methode des maschinellen Lernens, die verwendet wird, um KI-Modelle, insbesondere große Sprachmodelle (LLMs), feinabzustimmen, damit sie besser mit menschlichen Präferenzen und Anweisungen übereinstimmen. Anstatt sich ausschließlich auf vordefinierte Belohnungsfunktionen zu verlassen, integriert RLHF direktes Feedback von Menschen, um den Lernprozess zu steuern.

**Warum ist RLHF wichtig?**

*   **Subjektive Aufgaben:** RLHF glänzt bei Aufgaben, bei denen das gewünschte Ergebnis schwer mit expliziten Regeln oder numerischen Belohnungen zu definieren ist, wie z.B. das Generieren von kreativen Texten, das Führen natürlicher Gespräche oder das Erstellen von hilfreichen und harmlosen Inhalten.
*   **Nuancen und Ausrichtung:** Es hilft KI-Modellen, subtile menschliche Präferenzen, ethische Überlegungen und gewünschte Interaktionsstile zu verstehen und einzuhalten.
*   **Verbesserte Leistung:** Mit RLHF trainierte Modelle zeigen oft eine deutlich verbesserte Leistung und höhere Benutzerzufriedenheit im Vergleich zu Modellen, die nur mit traditionellem Reinforcement Learning oder überwachtem Lernen trainiert wurden.

**Wie RLHF funktioniert (typischerweise in drei Stufen):**

1.  **Vorabtraining und überwachte Feinanpassung (SFT):**
    *   Ein Basissprachmodell wird zunächst auf einem riesigen Datensatz aus Text und Code vortrainiert, um ein allgemeines Sprachverständnis und -generierung zu erlernen.
    *   Dieses vortrainierte Modell wird dann oft mit überwachtem Lernen auf einem kleineren Datensatz mit hochwertigen Demonstrationen des gewünschten Verhaltens feinabgestimmt (z.B. Menschen, die ideale Antworten auf Prompts schreiben). Dieser Schritt hilft dem Modell, das Format und den Stil der erwarteten Ausgaben zu verstehen.

2.  **Belohnungsmodell-Training:**
    *   Dies ist ein entscheidender Schritt in RLHF. Ein separates **Belohnungsmodell** wird trainiert, um menschliche Präferenzen vorherzusagen.
    *   Menschliche Annotatoren erhalten verschiedene Ausgaben des SFT-Modells (oder einer späteren Version) für denselben Eingabe-Prompt. Sie bewerten oder rangieren diese Ausgaben basierend auf verschiedenen Kriterien (z.B. Hilfsbereitschaft, Kohärenz, Sicherheit).
    *   Diese Präferenzdaten (z.B. "Ausgabe A ist besser als Ausgabe B") werden verwendet, um das Belohnungsmodell zu trainieren. Das Belohnungsmodell lernt, einer beliebigen Modellausgabe einen skalaren Belohnungswert zuzuordnen, der widerspiegelt, wie sehr ein Mensch sie bevorzugen würde.

3.  **Reinforcement Learning Feinanpassung:**
    *   Das ursprüngliche Sprachmodell (initialisiert aus dem SFT-Modell) wird weiter mit Reinforcement Learning feinabgestimmt.
    *   Das Belohnungsmodell aus dem vorherigen Schritt dient als Belohnungsfunktion der Umgebung.
    *   Der RL-Agent (das Sprachmodell) generiert Antworten auf Prompts, und das Belohnungsmodell bewertet diese Antworten.
    *   Der RL-Algorithmus (oft Proximal Policy Optimization - PPO) aktualisiert die Policy des Sprachmodells (wie es Text generiert), um die vom Belohnungsmodell vorhergesagten Belohnungen zu maximieren. Dies ermutigt das Sprachmodell, Ausgaben zu generieren, die besser mit menschlichen Präferenzen übereinstimmen.
    *   Um zu verhindern, dass die RL-Feinabstimmung zu weit vom Verhalten des SFT-Modells abweicht (was zu unerwünschten Ergebnissen führen könnte), wird oft ein Regularisierungsterm (z.B. KL-Divergenz-Strafe) in das RL-Ziel aufgenommen.

**Wie man RLHF durchführt (Vereinfachte Schritte):**

1.  **Sammeln menschlicher Präferenzdaten:**
    *   Entwerfen Sie Prompts oder Aufgaben, die für Ihr gewünschtes KI-Verhalten relevant sind.
    *   Generieren Sie mehrere Antworten auf diese Prompts mit Ihrem aktuellen Modell.
    *   Rekrutieren Sie menschliche Annotatoren, um diese Antworten zu vergleichen und ihre Präferenzen anzugeben (z.B. sie zu rangieren, die beste auszuwählen oder zu bewerten).
    *   Speichern Sie diese Daten als Paare von (Prompt, bevorzugte Antwort, weniger bevorzugte Antwort) oder in ähnlichen Formaten.

2.  **Trainieren eines Belohnungsmodells:**
    *   Wählen Sie eine geeignete Modellarchitektur für Ihr Belohnungsmodell (oft ein transformerbasiertes Modell, ähnlich dem Sprachmodell).
    *   Trainieren Sie das Belohnungsmodell auf den gesammelten menschlichen Präferenzdaten. Das Ziel ist, dass das Belohnungsmodell den Antworten, die Menschen bevorzugt haben, höhere Werte zuweist. Eine häufig verwendete Verlustfunktion basiert auf der Maximierung der Marge zwischen den Werten der bevorzugten und der weniger bevorzugten Antworten.

3.  **Feinabstimmung des Sprachmodells mit Reinforcement Learning:**
    *   Initialisieren Sie Ihr Sprachmodell mit den Gewichten aus dem SFT-Schritt (falls durchgeführt).
    *   Verwenden Sie einen Reinforcement-Learning-Algorithmus (wie PPO).
    *   Für jeden Trainingsschritt:
        *   Ziehen Sie einen Prompt.
        *   Lassen Sie das Sprachmodell eine Antwort generieren.
        *   Verwenden Sie das trainierte Belohnungsmodell, um einen Belohnungswert für die generierte Antwort zu erhalten.
        *   Aktualisieren Sie die Parameter des Sprachmodells basierend auf dem Belohnungssignal, um Aktionen (Token-Generierung) zu fördern, die zu höheren Belohnungen führen.
        *   Fügen Sie einen Regularisierungsterm (z.B. KL-Divergenz) hinzu, um die aktualisierte Policy nahe an der SFT-Policy zu halten.

**Code-Beispiel (Konzeptionell und vereinfacht mit PyTorch):**

Dies ist ein stark vereinfachtes konzeptionelles Beispiel, um die Kernideen zu veranschaulichen. Eine vollständige RLHF-Implementierung ist erheblich komplexer und beinhaltet Bibliotheken wie Hugging Face Transformers, Accelerate und RL-Bibliotheken.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# Angenommen, Sie haben menschliche Präferenzdaten gesammelt:
# Liste von Tupeln: (prompt, preferred_response, less_preferred_response)
preference_data = [
    ("Write a short story about a cat.", "Whiskers the cat lived in a cozy cottage...", "A cat story. The end."),
    ("Summarize this article:", "The article discusses...", "Article summary."),
    # ... mehr Daten
]

# 1. Lade vortrainiertes Sprachmodell und Tokenizer
model_name = "gpt2"  # Oder ein anderes geeignetes vortrainiertes Modell
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

# 2. Definiere ein einfaches Belohnungsmodell
class RewardModel(nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base_model = base_model.transformer  # Verwende die Transformer-Layers
        self.v_head = nn.Linear(base_model.config.n_embd, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden_states = outputs.last_hidden_state
        reward = self.v_head(last_hidden_states[:, -1])  # Belohnung vom letzten Token
        return reward

reward_model = RewardModel(policy_model)
reward_model.to(device)
reward_optimizer = optim.AdamW(reward_model.parameters(), lr=1e-5)
reward_criterion = nn.MarginRankingLoss(margin=1.0) # Höhere Belohnung für bevorzugte Antwort

# Trainiere das Belohnungsmodell
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens)
        less_preferred_reward = reward_model(**less_preferred_tokens)

        labels = torch.ones(preferred_reward.size(0)).to(device) # Wir wollen preferred > less preferred
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")

# 3. Reinforcement Learning Feinanpassung (Konzeptionell - PPO ist komplex)
policy_optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)

num_rl_episodes = 5
for episode in range(num_rl_episodes):
    for prompt in [data[0] for data in preference_data]: # Ziehe Prompts
        input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
        output_sequences = policy_model.generate(
            input_tokens.input_ids,
            max_length=60,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        generated_response = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

        response_tokens = tokenizer(prompt + generated_response, return_tensors="pt", truncation=True, max_length=128).to(device)
        reward = reward_model(**response_tokens)

        # (Vereinfachte) Policy-Aktualisierung - In der Realität verwendet PPO anspruchsvollere Methoden
        loss = -reward.mean() # Versuche, die Belohnung zu maximieren
        policy_optimizer.zero_grad()
        loss.backward()
        policy_optimizer.step()

    print(f"RL Episode {episode+1}, Reward: {reward.item()}, Response: {generated_response}")

print("RLHF Training Done!")
```

**Wichtige Herausforderungen bei RLHF:**

*   **Datensammlung:** Das Beschaffen hochwertiger und diverser menschlicher Präferenzdaten kann teuer und zeitaufwändig sein.
*   **Subjektivität und Verzerrung:** Menschliche Präferenzen können subjektiv sein und Verzerrungen enthalten, die vom Belohnungsmodell gelernt werden können.
*   **Reward Hacking:** Der RL-Agent könnte Wege finden, das Belohnungsmodell auszunutzen, die nicht mit den tatsächlichen menschlichen Präferenzen übereinstimmen.
*   **Skalierbarkeit:** Die Skalierung von RLHF auf sehr große Modelle und Datensätze erfordert erhebliche Rechenressourcen und sorgfältiges Engineering.
*   **Instabilität:** Das Training von RLHF-Modellen kann instabil sein und erfordert eine sorgfältige Hyperparameter-Optimierung.

Trotz dieser Herausforderungen hat sich RLHF als eine leistungsstarke Technik erwiesen, um KI-Modelle mit menschlichen Werten in Einklang zu bringen, und ist eine Schlüsselkomponente in der Entwicklung modernster Sprachmodelle wie ChatGPT und anderen.