---
audio: false
generated: false
lang: ar
layout: post
title: فهم الشبكات العصبية
translated: true
type: note
---

Zhiwei:

هل يمكنك شرح الكود؟

```python
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

ChatGPT:

بالتأكيد! الكود الذي قدمته يبدو جزءًا من خوارزمية تعلم الآلة، وتحديدًا تنفيذ لنزول التدرج العشوائي (SGD) لتحديث الأوزان والتحيزات في شبكة عصبية أثناء عملية التدريب. دعنا نشرحه خطوة بخطوة:

1. `self.weights` و `self.biases`:
هذه المتغيرات على الأرجح جزء من فئة الشبكة العصبية، تمثل الأوزان والتحيزات للشبكة. في الشبكة العصبية، الأوزان هي معلمات تضبط قوة الاتصالات بين الخلايا العصبية في الطبقات المختلفة، بينما التحيزات هي معلمات تتحكم في عتبة تفعيل الخلية العصبية.

2. `nabla_w` و `nabla_b`:
هذه المتغيرات على الأرجح تخزن تدرجات دالة التكلفة بالنسبة للأوزان والتحيزات على التوالي. أثناء عملية التدريب، يتم حساب التدرجات لتحديد كيف تتغير دالة التكلفة فيما يتعلق بالأوزان والتحيزات، وتستخدم هذه المعلومات لتحديث المعلمات لتقليل التكلفة.

3. `eta`:
هذا هو معدل التعلم، الذي يتحكم في حجم الخطوة المتخذة في اتجاه التدرجات أثناء تحديث المعلمات. معدل التعلم الأعلى يمكن أن يؤدي إلى تقارب أسرع أثناء التدريب، لكنه قد يسبب عدم استقرار. معدل التعلم الأصغر قد يحسن الاستقرار لكنه يزيد وقت التدريب.

4. `mini_batch`:
هذا مجموعة فرعية من بيانات التدريب المستخدمة في كل تكرار لنزول التدرج العشوائي. نزول التدرج بمجموعات مصغرة هو نوع من SGD حيث تقسم مجموعة بيانات التدريب الكاملة إلى دفعات أصغر، ويتم إجراء تحديثات المعلمات باستخدام كل مجموعة مصغرة.

الآن، دعنا ننظر إلى الكود نفسه:

```python
self.weights = [w-(eta/len(mini_batch))*nw
                for w, nw in zip(self.weights, nabla_w)]
```

هذا السطر يحدث أوزان الشبكة العصبية. يستخدم list comprehension للتكرار خلال كل وزن `w` والتدرج المقابل له `nw`. لكل وزن، يطرح جزءًا من التدرج (مقاسًا بمعدل التعلم `eta` وحجم المجموعة المصغرة) من الوزن الأصلي. هذه هي الطريقة التي يتم بها تحديث الأوزان لتقليل دالة التكلفة.

```python
self.biases = [b-(eta/len(mini_batch))*nb
               for b, nb in zip(self.biases, nabla_b)]
```

هذا السطر يحدث تحيزات الشبكة العصبية بطريقة مشابهة. يستخدم list comprehension للتكرار خلال كل تحيز `b` والتدرج المقابل له `nb`. لكل تحيز، يطرح جزءًا من التدرج (مقاسًا بمعدل التعلم `eta` وحجم المجموعة المصغرة) من التحيز الأصلي.

باختصار، هذه الأسطر من الكود تقوم بتحديث الأوزان والتحيزات للشبكة العصبية باستخدام نزول التدرج العشوائي. هذه العملية تكرر لكل مجموعة مصغرة أثناء مرحلة التدريب لتحسين معلمات الشبكة وتعزيز أدائها في المهمة المحددة.

----

Zhiwei: ما هو نموذج SpaCy اللغوي؟

ChatGPT: SpaCy هي مكتبة معالجة اللغة الطبيعية (NLP) مفتوحة المصدر طورتها Explosion AI. تم تصميمها لتكون فعالة وسريعة وجاهزة للإنتاج، مما يجعلها خيارًا شائعًا لمهام NLP متنوعة. توفر SpaCy نماذج لغوية مدربة مسبقًا يمكنها معالجة وفهم النص، مما يسمح للمطورين بأداء مهام NLP متنوعة مثل وسم جزء الكلام، والتعرف على الكيانات المسماة، وتحليل الجمل، والمزيد.

الميزات الرئيسية لنموذج SpaCy اللغوي تشمل:

1. Tokenization: تستطيع SpaCy تقسيم النص إلى كلمات فردية أو وحدات، مع الأخذ في الاعتبار قواعد وتعقيدات لغوية متنوعة.

2. Part-of-speech Tagging: يمكن للمكتبة تعيين وسم جزء الكلام لكل وحدة، مشيرًا إلى ما إذا كانت اسمًا، فعلًا، صفة، إلخ.

3. Named Entity Recognition (NER): تستطيع SpaCy تحديد وتصنيف كيانات مثل أسماء الأشخاص، المنظمات، المواقع، التواريخ، إلخ.

4. Dependency Parsing: يمكنها تحليل البنية النحوية للجملة وتحديد العلاقات بين الكلمات.

5. Lemmatization: تستطيع SpaCy تحويل الكلمات إلى شكلها الأساسي أو الجذر.

6. Word Vectors: توفر المكتبة متجهات الكلمات، المعروفة أيضًا باسم تضمينات الكلمات، وهي تمثيلات عددية كثيفة للكلمات تلتقط المعنى الدلالي.

تدعم SpaCy لغات متعددة وتأتي مع نماذج مدربة مسبقًا للغات مختلفة، مما يجعلها مستخدمة على نطاق واسع في تطبيقات NLP متنوعة، بما في ذلك استخراج المعلومات، تحليل المشاعر، روبوتات المحادثة، ترجمة اللغة، والمزيد. بالإضافة إلى ذلك، تسمح للمطورين بتدريب نماذج مخصصة على مجموعات البيانات الخاصة بهم إذا لزم الأمر.

---

Zhiwei: ما هو نموذج SpaCy اللغوي؟

ChatGPT: SpaCy هي مكتبة معالجة اللغة الطبيعية (NLP) مفتوحة المصدر طورتها Explosion AI. تم تصميمها لتكون فعالة وسريعة وسهلة الاستخدام، مما يجعلها خيارًا شائعًا لمهام NLP متنوعة. توفر SpaCy نماذج لغوية مدربة مسبقًا للعديد من اللغات، مما يسمح للمستخدمين بأداء مهام مثل tokenization، وسم جزء الكلام، التعرف على الكيانات المسماة، dependency parsing، والمزيد.

جوهر سرعة وكفاءة SpaCy يكمن في تطبيقات وهياكل بيانات Cython المحسنة، مما يجعلها مناسبة بشكل خاص لبيئات الإنتاج والتطبيقات الواقعية. المكتبة مكتوبة بلغة Python وتأتي مع نماذج مدربة مسبقًا للغات متنوعة، بما في ذلك الإنجليزية، الألمانية، الفرنسية، الإسبانية، والمزيد.

تستخدم نماذج SpaCy اللغوية تقنيات التعلم العميق لتعلم الأنماط الأساسية في بيانات اللغة الطبيعية. هذه النماذج يتم تدريبها على نصوص كبيرة، ويمكن بعد ذلك استخدام التمثيلات المتعلمة لمهام NLP متنوعة. النماذج المدربة مسبقًا يمكن ضبطها further على بيانات محددة لتحقيق أداء أفضل في المهام الخاصة بمجال معين.

جعلت البنية وسهولة الاستخدام SpaCy خيارًا شائعًا بين المطورين والباحثين في مجتمع NLP. غالبًا ما تستخدم في مهام مثل استخراج المعلومات، تصنيف النص، التعرف على الكيانات المسماة، وسم جزء الكلام، والتحليل النحوي. بالإضافة إلى ذلك، يسمح التصميم المعياري لـ SpaCy للمستخدمين بدمجها بسهولة في سير عمل ومجاري NLP الحالية.

---

Zhiwei: هل يمكنك الشرح؟

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

تشغيل الأمر ثم الحصول على سجل الخطأ.

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

تعلم تتبع الخطأ.

اسأل ChatGPT عن ماذا يعني Backend.NCCL في Pytorch؟

---

Zhiwei:

كود:

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

خطأ:

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

كيفية الإصلاح؟

ChatGPT:

رسالة الخطأ التي تواجهها تشير إلى وجود عدم تطابق في أنواع الأجهزة بين tensor الإدخال (`input_ids`) والنموذج (`LlamaForCausalLM`). tensor الإدخال على CPU (`cpu`)، بينما النموذج على GPU (`cuda`). للإصلاح، تحتاج إلى التأكد من أن tensor الإدخال على نفس جهاز النموذج قبل توليد النص باستخدام النموذج.

هذا هو الكود المعدل لإصلاح المشكلة:

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

# انقل tensor input_ids إلى نفس جهاز النموذج
input_ids = input_ids.to(model.device)

generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=32
)
print(tokenizer.decode(generation_output[0]))
```

في هذا الكود، أضفت السطر `input_ids = input_ids.to(model.device)` بعد الحصول على tensor `input_ids` من tokenizer. هذا السطر ينقل tensor `input_ids` إلى نفس جهاز النموذج (سواء CPU أو GPU) قبل توليد النص. هذا يجب أن يحل خطأ "Expected all tensors to be on the same device".

تذكر أنه إذا كنت تشغل هذا الكود على جهاز مدعوم بـ GPU ونموذجك على GPU، فمن الأكثر كفاءة عمومًا إبقاء كل من النموذج وبيانات الإدخال على GPU للاستفادة من إمكانيات المعالجة المتوازية.

---

Zhiwei: هل يمكنك شرح الأكواد أدناه؟

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

ChatGPT: بالتأكيد! الكود المقدم هو دالة تسمى `generate` تأخذ prompt (نص إدخال) وتولد نصًا باستخدام نموذج لغوي. هذه الدالة مصممة للعمل مع نموذج و tokenizer محددين وتقوم بتوليد النص باستخدام إما أخذ العينات الجشعة أو أخذ العينات top-p. إليك تفصيل لكيفية عمل الدالة:

1. **معاملات الدالة:**
   - `prompt_tokens`: قائمة بالـ prompts المعالجة إلى tokens، حيث يمثل كل prompt كقائمة من الأعداد الصحيحة (معرفات الـ tokens).
   - `max_gen_len`: الحد الأقصى لطول الناتج المُولد (بـ tokens).
   - `temperature`: معامل يتحكم في عشوائية التوليد. القيم الأعلى (مثل 1.0) تجعل الناتج أكثر عشوائية، بينما القيم الأقل (مثل 0.6) تجعله أكثر حتمية.
   - `top_p`: معامل يتحكم في تنوع النص المُولد. القيم الأعلى (مثل 0.9) تسمح بأخذ عينات أكثر تنوعًا.
   - `logprobs`: إذا كانت `True`، ترجع الدالة أيضًا log-probabilities للـ tokens المُولدة.
   - `echo`: إذا كانت `True`، سيتضمن الناتج المُولد الـ prompt نفسه.

2. **التهيئة:**
   الدالة تهيئ متغيرات مثل `params`، `bsz` (حجم الدفعة)، `min_prompt_len`، و `max_prompt_len`. كما تحسب `total_len` وهو الطول الإجمالي للناتج المُولد بما في ذلك الـ prompt.

3. **توليد الـ Tokens:**
   الدالة تولد tokens لنص الخرج. تستخدم حلقة للتكرار عبر المواضع في التسلسل المُولد، بدءًا من نهاية الـ prompt والتقدم للأمام.
   
   - يتم الحصول على الـ logits لكل موضع بتمرير التسلسل الجزئي إلى دالة forward للنموذج.
   - إذا كان `temperature` أكبر من 0، تتحول الـ logits إلى احتمالات باستخدام softmax مع قيمة temperature المعطاة. إذا كان `temperature` هو 0، يتم اختيار الـ token بأعلى logit باستخدام `torch.argmax`.
   - يتم تحديد الـ token التالي بناءً على الاحتمالات المُولدة أو argmax، ويوضع في الموضع المقابل لـ tensor الـ `tokens`.
   - يتم اكتشاف tokens EOS (نهاية التسلسل)، وإذا وصلت جميع التسلسلات إلى token EOS، تتوقف عملية التوليد.
   - يتم الاحتفاظ بالـ tokens المُولدة في tensor الـ `tokens`.

4. **معالجة الناتج المُولد:**
   - يتم معالجة الـ tokens المُولدة لقص الناتج إلى الطول الأقصى المطلوب (`max_gen_len`).
   - إذا كانت `echo` هي `True`، يتم تضمين الـ prompt في الناتج المُولد.
   - إذا تمت مصادفة token `eos`، يتم قطع النص المُولد عند تلك النقطة.

5. **الإرجاع:**
   ترجع الدالة tuple يحتوي على الـ tokens المُولدة، وإذا كانت `logprobs` هي `True`، فإن log-probabilities للـ tokens المُولدة.

هذه الدالة تولد النص من خلال التنبؤ بالـ tokens تكرارًا بناءً على السياق المقدم من الـ prompt والـ tokens المُولدة سابقًا. تستخدم معاملات التوليد المحددة للتحكم في العشوائية والتنوع للنص المُولد. الدالة مصممة لاستخدامها مع بنية نموذج و tokenizer محددين، حيث تعتمد على خصائصهم وطرقهم لتوليد النص.