---
audio: false
generated: false
lang: fr
layout: post
title: Comprendre les réseaux de neurones
translated: true
type: note
---

Zhiwei : 

Pouvez-vous expliquer le code ?

```python
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

ChatGPT : 

Bien sûr ! Le code que vous avez fourni semble faire partie d'un algorithme d'apprentissage automatique, plus précisément une implémentation de la descente de gradient stochastique (SGD) pour mettre à jour les poids et les biais d'un réseau de neurones pendant le processus d'entraînement. Décomposons-le étape par étape :

1. `self.weights` et `self.biases` :
Ces variables font probablement partie d'une classe de réseau de neurones, représentant les poids et les biais du réseau. Dans un réseau de neurones, les poids sont des paramètres qui ajustent la force des connexions entre les neurones de différentes couches, tandis que les biais sont des paramètres qui contrôlent le seuil d'activation du neurone.

2. `nabla_w` et `nabla_b` :
Ces variables stockent vraisemblablement les gradients de la fonction de coût par rapport aux poids et aux biais, respectivement. Pendant le processus d'entraînement, les gradients sont calculés pour déterminer comment la fonction de coût change par rapport aux poids et aux biais, et cette information est utilisée pour mettre à jour les paramètres afin de minimiser le coût.

3. `eta` :
Il s'agit du taux d'apprentissage, qui contrôle la taille du pas effectué dans la direction des gradients pendant la mise à jour des paramètres. Un taux d'apprentissage plus élevé peut conduire à une convergence plus rapide pendant l'entraînement, mais il peut aussi causer une instabilité. Un taux d'apprentissage plus petit peut améliorer la stabilité mais augmenter le temps d'entraînement.

4. `mini_batch` :
Il s'agit d'un sous-ensemble des données d'entraînement utilisé pour chaque itération de la descente de gradient stochastique. La descente de gradient par mini-lots est une variante de SGD où l'ensemble complet des données d'entraînement est divisé en lots plus petits, et les mises à jour des paramètres sont effectuées en utilisant chaque mini-lot.

Maintenant, regardons le code lui-même :

```python
self.weights = [w-(eta/len(mini_batch))*nw
                for w, nw in zip(self.weights, nabla_w)]
```

Cette ligne met à jour les poids du réseau de neurones. Elle utilise une compréhension de liste pour parcourir chaque poids `w` et son gradient correspondant `nw`. Pour chaque poids, elle soustrait une partie du gradient (mis à l'échelle par le taux d'apprentissage `eta` et la taille du mini-lot) du poids original. C'est ainsi que les poids sont mis à jour pour minimiser la fonction de coût.

```python
self.biases = [b-(eta/len(mini_batch))*nb
               for b, nb in zip(self.biases, nabla_b)]
```

Cette ligne met à jour les biais du réseau de neurones de manière similaire. Elle utilise une compréhension de liste pour parcourir chaque biais `b` et son gradient correspondant `nb`. Pour chaque biais, elle soustrait une partie du gradient (mis à l'échelle par le taux d'apprentissage `eta` et la taille du mini-lot) du biais original.

En résumé, ces lignes de code effectuent les mises à jour des poids et des biais pour le réseau de neurones en utilisant la descente de gradient stochastique. Ce processus est répété pour chaque mini-lot pendant la phase d'entraînement pour optimiser les paramètres du réseau et améliorer ses performances sur la tâche donnée.

----

Zhiwei : Qu'est-ce que le modèle linguistique SpaCy ?

ChatGPT : SpaCy est une bibliothèque de traitement du langage naturel (NLP) open-source développée par Explosion AI. Elle est conçue pour être efficace, rapide et prête pour la production, ce qui en fait un choix populaire pour diverses tâches de NLP. SpaCy fournit des modèles linguistiques pré-entraînés qui peuvent traiter et comprendre le texte, permettant aux développeurs d'effectuer diverses tâches de NLP telles que l'étiquetage morphosyntaxique, la reconnaissance d'entités nommées, l'analyse syntaxique des phrases, et plus encore.

Les caractéristiques clés du modèle linguistique SpaCy incluent :

1. Tokenisation : SpaCy peut diviser un texte en mots individuels ou tokens, en tenant compte de diverses règles et complexités linguistiques.

2. Étiquetage morphosyntaxique : La bibliothèque peut attribuer des étiquettes morphosyntaxiques à chaque token, indiquant s'il s'agit d'un nom, d'un verbe, d'un adjectif, etc.

3. Reconnaissance d'entités nommées (NER) : SpaCy peut identifier et catégoriser des entités telles que des noms de personnes, d'organisations, de lieux, de dates, etc.

4. Analyse syntaxique des dépendances : Elle peut analyser la structure grammaticale d'une phrase et déterminer les relations entre les mots.

5. Lemmatisation : SpaCy peut convertir les mots dans leur forme de base ou racine (lemmes).

6. Word Vectors : La bibliothèque fournit des vecteurs de mots, également connus sous le nom de plongements lexicaux, qui sont des représentations numériques denses des mots capturant la signification sémantique.

SpaCy prend en charge plusieurs langues et est livrée avec des modèles pré-entraînés pour différentes langues, ce qui la rend largement utilisée dans diverses applications de NLP, y compris l'extraction d'informations, l'analyse de sentiments, les chatbots, la traduction linguistique, et plus encore. De plus, elle permet aux développeurs d'entraîner des modèles personnalisés sur leurs ensembles de données spécifiques si nécessaire.

---

Zhiwei : Qu'est-ce que le modèle linguistique SpaCy ?

ChatGPT : SpaCy est une bibliothèque de traitement du langage naturel (NLP) open-source développée par Explosion AI. Elle est conçue pour être efficace, rapide et facile à utiliser, ce qui en fait un choix populaire pour diverses tâches de NLP. SpaCy fournit des modèles linguistiques pré-entraînés pour plusieurs langues, permettant aux utilisateurs d'effectuer des tâches telles que la tokenisation, l'étiquetage morphosyntaxique, la reconnaissance d'entités nommées, l'analyse syntaxique des dépendances, et plus encore.

Le cœur de la vitesse et de l'efficacité de SpaCy réside dans ses implémentations et structures de données optimisées en Cython, ce qui la rend particulièrement adaptée aux environnements de production et aux applications du monde réel. La bibliothèque est écrite en Python et est livrée avec des modèles pré-entraînés pour diverses langues, y compris l'anglais, l'allemand, le français, l'espagnol, et plus encore.

Les modèles linguistiques SpaCy utilisent des techniques d'apprentissage profond pour apprendre les motifs sous-jacents dans les données de langage naturel. Ces modèles sont entraînés sur de grands corpus de texte, et les représentations apprises peuvent ensuite être utilisées pour diverses tâches de NLP. Les modèles pré-entraînés peuvent être affinés sur des données spécifiques pour obtenir de meilleures performances sur des tâches spécifiques à un domaine.

L'architecture et la facilité d'utilisation ont fait de SpaCy un choix populaire parmi les développeurs et les chercheurs dans la communauté NLP. Elle est souvent utilisée pour des tâches comme l'extraction d'informations, la classification de texte, la reconnaissance d'entités nommées, l'étiquetage morphosyntaxique et l'analyse syntaxique. De plus, la conception modulaire de SpaCy permet aux utilisateurs de l'intégrer facilement dans leurs flux de travail et pipelines NLP existants.

---

Zhiwei : Pouvez-vous expliquer ?

```python
class Llama:
    @staticmethod
    def build(
        ckpt_dir: str,
        tokenizer_path: str,
        max_seq_len: int,
        max_batch_size: int,
        model_parallel_size: Optional[int] = None,
    ) -> "Llama":
        if not torch.distributed.is_initialized():
            torch.distributed.init_process_group("nccl")
        if not model_parallel_is_initialized():
            if model_parallel_size is None:
                model_parallel_size = int(os.environ.get("WORLD_SIZE", 1))
            initialize_model_parallel(model_parallel_size)

        local_rank = int(os.environ.get("LOCAL_RANK", 0))
        torch.cuda.set_device(local_rank)

        # seed must be the same in all processes
        torch.manual_seed(1)

        if local_rank > 0:
            sys.stdout = open(os.devnull, "w")

        start_time = time.time()
        checkpoints = sorted(Path(ckpt_dir).glob("*.pth"))
        assert len(checkpoints) > 0, f"no checkpoint files found in {ckpt_dir}"
        assert model_parallel_size == len(
            checkpoints
        ), f"Loading a checkpoint for MP={len(checkpoints)} but world size is {model_parallel_size}"
        ckpt_path = checkpoints[get_model_parallel_rank()]
        checkpoint = torch.load(ckpt_path, map_location="cpu")
        with open(Path(ckpt_dir) / "params.json", "r") as f:
            params = json.loads(f.read())
```

Exécutez la commande et obtenez le journal d'erreur.

```shell
% torchrun --nproc_per_node 1 example_text_completion.py \
    --ckpt_dir llama-2-7b/ \
    --tokenizer_path tokenizer.model \
    --max_seq_len 128 --max_batch_size 4
NOTE: Redirects are currently not supported in Windows or MacOs.
Traceback (most recent call last):
  File "/Users/lzwjava/projects/llama/example_text_completion.py", line 55, in <module>
    fire.Fire(main)
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/fire/core.py", line 141, in Fire
    component_trace = _Fire(component, args, parsed_flag_args, context, name)
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/fire/core.py", line 475, in _Fire
    component, remaining_args = _CallAndUpdateTrace(
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/fire/core.py", line 691, in _CallAndUpdateTrace
    component = fn(*varargs, **kwargs)
  File "/Users/lzwjava/projects/llama/example_text_completion.py", line 18, in main
    generator = Llama.build(
  File "/Users/lzwjava/projects/llama/llama/generation.py", line 62, in build
    torch.distributed.init_process_group("nccl")
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 907, in init_process_group
    default_pg = _new_process_group_helper(
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 1013, in _new_process_group_helper
    raise RuntimeError("Distributed package doesn't have NCCL " "built in")
RuntimeError: Distributed package doesn't have NCCL built in
ERROR:torch.distributed.elastic.multiprocessing.api:failed (exitcode: 1) local_rank: 0 (pid: 23273) of binary: /Users/lzwjava/anaconda3/bin/python

Traceback (most recent call last):
  File "/Users/lzwjava/anaconda3/bin/torchrun", line 33, in <module>
    sys.exit(load_entry_point('torch==2.0.1', 'console_scripts', 'torchrun')())
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 346, in wrapper
    return f(*args, **kwargs)
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/torch/distributed/run.py", line 794, in main
    run(args)
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/torch/distributed/run.py", line 785, in run
    elastic_launch(
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 134, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/Users/lzwjava/anaconda3/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 250, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError:
============================================================
example_text_completion.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2023-08-03_15:35:37
  host      : 1.0.0.127.in-addr.arpa
  rank      : 0 (local_rank: 0)
  exitcode  : 1 (pid: 23273)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
```

Apprenez la trace de la pile d'erreurs.

Demandez à ChatGPT ce que signifie Backend.NCCL dans Pytorch ?

---

Zhiwei :

code :

```python
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

model_path = '.'
# model_path = 'openlm-research/open_llama_7b'

tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map='auto',
)

prompt = 'Q: What is the largest animal?\nA:'
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=32
)
print(tokenizer.decode(generation_output[0]))
```

erreur :

```shell
/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/transformers/generation/utils.py:1445: UserWarning: You are calling .generate() with the `input_ids` being on a device type different than your model's device. `input_ids` is on cpu, whereas the model is on cuda. You may experience unexpected behaviors or slower generation. Please make sure that you have put `input_ids` to the correct device by calling for example input_ids = input_ids.to('cuda') before running `.generate()`.
  warnings.warn(
Traceback (most recent call last):
  File "/home/lzw/Projects/open_llama_3b/run.py", line 17, in <module>
    generation_output = model.generate(
                        ^^^^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/transformers/generation/utils.py", line 1515, in generate
    return self.greedy_search(
           ^^^^^^^^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/transformers/generation/utils.py", line 2332, in greedy_search
    outputs = self(
              ^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 688, in forward
    outputs = self.model(
              ^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 531, in forward
    inputs_embeds = self.embed_tokens(input_ids)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/torch/nn/modules/sparse.py", line 162, in forward
    return F.embedding(
           ^^^^^^^^^^^^
  File "/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/torch/nn/functional.py", line 2210, in embedding
    return torch.embedding(weight, input, padding_idx, scale_grad_by_freq, sparse)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument index in method wrapper_CUDA__index_select)
```

comment résoudre ?

ChatGPT :

Le message d'erreur que vous rencontrez indique qu'il y a une incompatibilité entre les types de périphériques de votre tenseur d'entrée (`input_ids`) et de votre modèle (`LlamaForCausalLM`). Le tenseur d'entrée est sur le CPU (`cpu`), tandis que le modèle est sur le GPU (`cuda`). Pour résoudre ce problème, vous devez vous assurer que le tenseur d'entrée est sur le même périphérique que le modèle avant de générer du texte en utilisant le modèle.

Voici le code modifié pour résoudre le problème :

```python
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

model_path = '.'
# model_path = 'openlm-research/open_llama_7b'

tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map='auto',
)

prompt = 'Q: What is the largest animal?\nA:'
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

# Déplacez le tenseur input_ids vers le même périphérique que le modèle
input_ids = input_ids.to(model.device)

generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=32
)
print(tokenizer.decode(generation_output[0]))
```

Dans ce code, j'ai ajouté la ligne `input_ids = input_ids.to(model.device)` après avoir obtenu le tenseur `input_ids` du tokenizer. Cette ligne déplace le tenseur `input_ids` vers le même périphérique que le modèle (soit CPU, soit GPU) avant de générer du texte. Cela devrait résoudre l'erreur "Expected all tensors to be on the same device".

Rappelez-vous que si vous exécutez ce code sur une machine avec GPU activé et que votre modèle est sur un GPU, il est généralement plus efficace de garder à la fois le modèle et les données d'entrée sur le GPU pour profiter des capacités de traitement parallèle.

---

Zhiwei : Pouvez-vous expliquer les codes ci-dessous ?

```python
   def generate(
        self,
        prompt_tokens: List[List[int]],
        max_gen_len: int,
        temperature: float = 0.6,
        top_p: float = 0.9,
        logprobs: bool = False,
        echo: bool = False,
    ) -> Tuple[List[List[int]], Optional[List[List[float]]]]:
        params = self.model.params
        bsz = len(prompt_tokens)
        assert bsz <= params.max_batch_size, (bsz, params.max_batch_size)

        min_prompt_len = min(len(t) for t in prompt_tokens)
        max_prompt_len = max(len(t) for t in prompt_tokens)
        assert max_prompt_len <= params.max_seq_len
        total_len = min(params.max_seq_len, max_gen_len + max_prompt_len)

        pad_id = self.tokenizer.pad_id
        tokens = torch.full((bsz, total_len), pad_id, dtype=torch.long, device="cuda")
        for k, t in enumerate(prompt_tokens):
            tokens[k, : len(t)] = torch.tensor(t, dtype=torch.long, device="cuda")
        if logprobs:
            token_logprobs = torch.zeros_like(tokens, dtype=torch.float)

        prev_pos = 0
        eos_reached = torch.tensor([False] * bsz, device="cuda")
        input_text_mask = tokens != pad_id
        for cur_pos in range(min_prompt_len, total_len):
            logits = self.model.forward(tokens[:, prev_pos:cur_pos], prev_pos)
            if logprobs:
                token_logprobs[:, prev_pos + 1 : cur_pos + 1] = -F.cross_entropy(
                    input=logits.transpose(1, 2),
                    target=tokens[:, prev_pos + 1 : cur_pos + 1],
                    reduction="none",
                    ignore_index=pad_id,
                )
            if temperature > 0:
                probs = torch.softmax(logits[:, -1] / temperature, dim=-1)
                next_token = sample_top_p(probs, top_p)
            else:
                next_token = torch.argmax(logits[:, -1], dim=-1)

            next_token = next_token.reshape(-1)
            # only replace token if prompt has already been generated
            next_token = torch.where(
                input_text_mask[:, cur_pos], tokens[:, cur_pos], next_token
            )
            tokens[:, cur_pos] = next_token
            eos_reached |= (~input_text_mask[:, cur_pos]) & (
                next_token == self.tokenizer.eos_id
            )
            prev_pos = cur_pos
            if all(eos_reached):
                break

        if logprobs:
            token_logprobs = token_logprobs.tolist()
        out_tokens, out_logprobs = [], []
        for i, toks in enumerate(tokens.tolist()):
            # cut to max gen len
            start = 0 if echo else len(prompt_tokens[i])
            toks = toks[start : len(prompt_tokens[i]) + max_gen_len]
            probs = None
            if logprobs:
                probs = token_logprobs[i][start : len(prompt_tokens[i]) + max_gen_len]
            # cut to eos tok if any
            if self.tokenizer.eos_id in toks:
                eos_idx = toks.index(self.tokenizer.eos_id)
                toks = toks[:eos_idx]
                probs = probs[:eos_idx] if logprobs else None
            out_tokens.append(toks)
            out_logprobs.append(probs)
        return (out_tokens, out_logprobs if logprobs else None)
```

ChatGPT : Certainement ! Le code fourni est une méthode appelée `generate` qui prend un prompt (texte d'entrée) et génère du texte en utilisant un modèle de langage. Cette méthode est conçue pour fonctionner avec un modèle et un tokenizer spécifiques et effectue la génération de texte en utilisant soit un échantillonnage glouton, soit un échantillonnage top-p. Voici une explication détaillée du fonctionnement de la méthode :

1. **Paramètres de la méthode :**
   - `prompt_tokens` : Une liste de prompts tokenisés, où chaque prompt est représenté comme une liste d'entiers (IDs de tokens).
   - `max_gen_len` : La longueur maximale de la sortie générée (en tokens).
   - `temperature` : Un paramètre contrôlant le caractère aléatoire de la génération. Des valeurs plus élevées (par exemple, 1.0) rendent la sortie plus aléatoire, tandis que des valeurs plus basses (par exemple, 0.6) la rendent plus déterministe.
   - `top_p` : Un paramètre contrôlant la diversité du texte généré. Des valeurs plus élevées (par exemple, 0.9) permettent un échantillonnage plus diversifié.
   - `logprobs` : Si `True`, la méthode retourne également les log-probabilités des tokens générés.
   - `echo` : Si `True`, la sortie générée inclura le prompt lui-même.

2. **Initialisation :**
   La méthode initialise des variables telles que `params`, `bsz` (taille du lot), `min_prompt_len` et `max_prompt_len`. Elle calcule également `total_len` qui est la longueur totale de la sortie générée incluant le prompt.

3. **Génération de tokens :**
   La méthode génère des tokens pour le texte de sortie. Elle utilise une boucle pour itérer sur les positions dans la séquence générée, en commençant à la fin du prompt et en avançant.
   
   - Les logits pour chaque position sont obtenus en passant la séquence partielle à la fonction forward du modèle.
   - Si `temperature` est supérieure à 0, les logits sont transformés en probabilités en utilisant softmax avec la valeur de température donnée. Si `temperature` est 0, le token avec le logit le plus élevé est sélectionné en utilisant `torch.argmax`.
   - Le token suivant est déterminé en fonction des probabilités générées ou de l'argmax, et il est placé dans la position correspondante du tenseur `tokens`.
   - Les tokens EOS (fin de séquence) sont détectés, et si toutes les séquences ont atteint un token EOS, le processus de génération est arrêté.
   - Les tokens générés sont conservés dans le tenseur `tokens`.

4. **Traitement de la sortie générée :**
   - Les tokens générés sont traités pour tronquer la sortie à la longueur maximale souhaitée (`max_gen_len`).
   - Si `echo` est `True`, le prompt est inclus dans la sortie générée.
   - Si le token `eos` est rencontré, le texte généré est coupé à ce point.

5. **Retour :**
   La méthode retourne un tuple contenant les tokens générés et, si `logprobs` est `True`, les log-probabilités des tokens générés.

Cette méthode génère du texte en prédisant itérativement des tokens en fonction du contexte fourni par le prompt et des tokens précédemment générés. Elle utilise les paramètres de génération spécifiés pour contrôler le caractère aléatoire et la diversité du texte généré. La méthode est conçue pour être utilisée avec une architecture de modèle et un tokenizer spécifiques, car elle repose sur leurs propriétés et méthodes pour la génération de texte.