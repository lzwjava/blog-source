---
audio: false
generated: true
lang: de
layout: post
title: DeepSeek R1
translated: true
type: note
---

DeepSeek R1 verfolgt einen neuartigen Ansatz für Reinforcement Learning (RL), der **Reasoning-Fähigkeiten** in großen Sprachmodellen (LLMs) stark betont. Ihre Technik unterscheidet sich in mehreren wichtigen Aspekten vom traditionellen Reinforcement Learning from Human Feedback (RLHF).

Hier ist eine Aufschlüsselung der Techniken, die DeepSeek beim Reinforcement Learning von R1 eingesetzt hat:

**1. Reines Reinforcement Learning (RL) für initiales Reasoning (DeepSeek-R1-Zero):**

* **Kein anfängliches Supervised Fine-Tuning (SFT) auf Anweisungen:** Im Gegensatz zu vielen LLMs, die zunächst ein SFT auf von Menschen geschriebenen Anweisungen durchlaufen, wurde DeepSeek-R1-Zero mit **rein RL** direkt auf dem Basismodell (DeepSeek-V3-Base) trainiert.
* **Group Relative Policy Optimization (GRPO):** Sie setzten GRPO als ihren Kern-RL-Algorithmus ein. GRPO ist so konzipiert, dass es effizienter ist als Proximal Policy Optimization (PPO), da es kein separates Critic-Netzwerk benötigt. Es schätzt Baseline-Belohnungen, indem es eine Gruppe generierter Ausgaben vergleicht und ihnen basierend auf ihrer Qualität relative Scores zuweist. Dies ermutigt das Modell, bessere Antworten zu generieren als seine eigenen vorherigen Versuche.
* **Regelbasiertes Belohnungssystem:** Statt sich in der initialen RL-Phase ausschließlich auf menschliche Präferenzen zu verlassen, verwendete DeepSeek-R1-Zero ein **regelbasiertes Belohnungssystem**. Dieses System konzentrierte sich primär auf:
    * **Genauigkeitsbelohnungen (Accuracy Rewards):** Das Modell wurde dafür belohnt, korrekte Antworten zu liefern, insbesondere bei Aufgaben mit überprüfbaren Lösungen wie Mathematikproblemen (Überprüfung, ob die Endantwort korrekt ist).
    * **Formatbelohnungen (Format Rewards):** Das Modell wurde dafür belohnt, ein spezifisches Ausgabeformat einzuhalten, insbesondere die Verwendung von `` Tags, um seinen Denkprozess einzuschließen. Dies förderte die Entstehung von Chain-of-Thought Reasoning.
* **Entstehende Reasoning-Verhaltensweisen:** Dieser reine RL-Ansatz ermöglichte es DeepSeek-R1-Zero, auf natürliche Weise beeindruckende Reasoning-Fähigkeiten zu entwickeln, einschließlich Selbstverifikation, Reflexion und der Generierung langer Chain-of-Thought-Erklärungen, ohne explizite menschliche Demonstrationen für diese Verhaltensweisen.

**2. Mehrstufiges Training für verbesserte Lesbarkeit und allgemeine Fähigkeiten (DeepSeek-R1):**

Um die Einschränkungen von DeepSeek-R1-Zero (wie schlechte Lesbarkeit und Sprachvermischung) anzugehen, setzte DeepSeek-R1 eine umfassendere mehrstufige Trainingspipeline ein:

* **Cold-Start Data Fine-Tuning:** Vor der Haupt-RL-Phase wurde das Basismodell auf einem kleinen Datensatz mit hochwertigen, von Menschen geschriebenen (oder generierten und verfeinerten) langen Chain-of-Thought-Reasoning-Beispielen feinabgestimmt. Diese "Cold-Start"-Daten halfen dabei, das Modell in Richtung lesbarerer und kohärenterer Denkschritte zu lenken.
* **Reasoning-orientiertes Reinforcement Learning (Zweite RL-Stufe):** Das Modell durchlief dann eine zweite Phase von groß angelegtem RL (ähnlich wie DeepSeek-R1-Zero), jedoch mit einer zusätzlichen **Sprachkonsistenzbelohnung (Language Consistency Reward)**. Diese Belohnung bestrafte das Modell dafür, Sprachen innerhalb seines Denkprozesses zu vermischen.
* **Supervised Fine-Tuning (SFT):** Nach dem reasoning-orientierten RL wurde das Modell weiter auf einem diversen Datensatz feinabgestimmt, der sowohl Reasoning-Daten (synthetisiert mittels Rejection Sampling vom RL-Modell, bewertet durch DeepSeek-V3) als auch allgemeine Nicht-Reasoning-Daten (angereichert mit Chain-of-Thought) enthielt. Diese SFT-Stufe zielte darauf ab, die Hilfsbereitschaft und Harmlosigkeit des Modells zu verbessern und gleichzeitig seine starken Reasoning-Fähigkeiten zu bewahren.
* **RL für alle Szenarien (Dritte RL-Stufe):** Eine finale RL-Phase wurde mit Prompts aus einem breiteren Spektrum von Szenarien durchgeführt, um die allgemeinen Fähigkeiten des Modells und seine Ausrichtung auf das gewünschte Verhalten weiter zu verfeinern.

**Wichtige Unterschiede zum traditionellen RLHF:**

* **Geringere Abhängigkeit von umfangreichen menschlichen Präferenzdaten:** Während einige menschliche Bewertungen möglicherweise in die Beurteilung der Qualität der synthetisierten Daten involviert waren, stützte sich das Kern-RL-Training in DeepSeek-R1 stark auf regelbasierte Belohnungen, insbesondere in den Anfangsstadien. Dies verringert die Kosten und die Komplexität der Sammlung großer Mengen direkter menschlicher Präferenzvergleiche.
* **Fokus auf entstehendes Reasoning (Emergent Reasoning):** Der reine RL-Ansatz zielte darauf ab, das Modell dazu zu incentivieren, effektive Reasoning-Strategien *selbst zu entdecken*, anstatt nur aus von Menschen bereitgestellten Reasoning-Beispielen zu lernen.
* **Mehrstufiger Ansatz:** Die Pipeline von DeepSeek beinhaltet eine sorgfältig orchestrierte Abfolge von Pre-Training, gezieltem Fine-Tuning und mehreren RL-Stufen mit verschiedenen Belohnungssignalen, um sowohl starkes Reasoning als auch allgemeine Sprachfähigkeiten zu erreichen.

**Code zur Veranschaulichung von Reinforcement Learning (Konzeptionell und Vereinfacht):**

Es ist eine Herausforderung, ein direkt lauffähiges Codebeispiel bereitzustellen, das den gesamten RL-Trainingsprozess von DeepSeek aufgrund seiner Komplexität und seines Umfangs vollständig nachbildet. Das folgende konzeptionelle, PyTorch-ähnliche Codefragment veranschaulicht jedoch die Kernidee von GRPO und einer regelbasierten Belohnung:

```python
import torch
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# Angenommen, Sie haben ein vortrainiertes Sprachmodell und einen Tokenizer
model_name = "gpt2"  # Ersetzen durch ein geeigneteres Basismodell
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

def generate_responses(prompt, num_responses=4, max_length=128):
    input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = policy_model.generate(
        input_tokens.input_ids,
        max_length=max_length,
        num_return_sequences=num_responses,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return responses

def calculate_accuracy_reward(response):
    # Vereinfachtes Beispiel für ein Matheproblem: "Was ist 2 + 2?"
    if "2 + 2" in response and "4" in response:
        return 1.0
    else:
        return 0.0

def calculate_format_reward(response):
    if "" in response:
        return 0.5
    else:
        return 0.0

def calculate_combined_reward(response):
    accuracy_reward = calculate_accuracy_reward(response)
    format_reward = calculate_format_reward(response)
    return accuracy_reward + format_reward

def train_step(prompt, num_samples=4):
    optimizer.zero_grad()
    responses = generate_responses(prompt, num_samples=num_samples)
    rewards = torch.tensor([calculate_combined_reward(resp) for resp in responses]).float().to(device)

    # Vereinfachter GRPO-ähnlicher Update: Begünstige Antworten mit höherer Belohnung
    best_reward_index = torch.argmax(rewards)
    best_response = responses[best_reward_index]
    inputs = tokenizer(prompt + best_response, return_tensors="pt").to(device)
    outputs = policy_model(**inputs, labels=inputs.input_ids)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    return loss.item(), best_response, rewards.tolist()

# Trainingsschleife (stark vereinfacht)
num_episodes = 10
training_prompts = ["Solve: 2 + 2 = ?", "Explain the concept of gravity