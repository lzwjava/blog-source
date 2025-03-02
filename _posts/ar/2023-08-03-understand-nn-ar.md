---
audio: false
generated: false
lang: ar
layout: post
title: فهم الشبكات العصبية
translated: true
---

زيهوي:

بالطبع! إذا كنت تقصد كودًا معينًا، يرجى مشاركته هنا وسأكون سعيدًا بشرحه لك. إذا كنت تقصد كودًا عامًا أو مفهومًا برمجيًا معينًا، فيرجى توضيح ذلك حتى أتمكن من تقديم الشرح المناسب. 😊

```python
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

تمت ترجمة التعليقات البرمجية أعلاه إلى العربية كما يلي:

```python
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

في الكود أعلاه، يتم تحديث الأوزان (`weights`) والانحيازات (`biases`) باستخدام قاعدة التحديث المعتمدة على التدرج (gradient descent). يتم تعديل كل وزن وانحياز بناءً على التدرج المحسوب (`nabla_w` و `nabla_b`) ومعدل التعلم (`eta`)، مع الأخذ في الاعتبار حجم الدفعة الصغيرة (`mini_batch`).

ChatGPT:

بالطبع! الكود الذي قدمته يبدو جزءًا من خوارزمية تعلم الآلة، وتحديدًا تنفيذ لخوارزمية الانحدار التدرج العشوائي (Stochastic Gradient Descent - SGD) لتحديث الأوزان والتحيزات في شبكة عصبية أثناء عملية التدريب. دعنا نحلله خطوة بخطوة:

1. `self.weights` و `self.biases`:
من المحتمل أن تكون هذه المتغيرات جزءًا من فئة شبكة عصبية، حيث تمثل الأوزان والانحيازات الخاصة بالشبكة. في الشبكة العصبية، الأوزان هي معاملات تُعدل قوة الاتصالات بين الخلايا العصبية في الطبقات المختلفة، بينما الانحيازات هي معاملات تتحكم في عتبة تنشيط الخلية العصبية.

2. `nabla_w` و `nabla_b`:
من المحتمل أن تخزن هذه المتغيرات تدرجات دالة التكلفة بالنسبة للأوزان والتحيزات على التوالي. خلال عملية التدريب، يتم حساب التدرجات لتحديد كيفية تغير دالة التكلفة بالنسبة للأوزان والتحيزات، ويتم استخدام هذه المعلومات لتحديث المعلمات لتقليل التكلفة.

3. `eta`:
هذا هو معدل التعلم، والذي يتحكم في حجم الخطوة التي يتم اتخاذها في اتجاه التدرجات أثناء تحديث المعلمات. يمكن أن يؤدي معدل التعلم الأعلى إلى تقارب أسرع أثناء التدريب، ولكنه قد يتسبب أيضًا في عدم الاستقرار. قد يؤدي معدل التعلم الأصغر إلى تحسين الاستقرار ولكنه يزيد من وقت التدريب.

4. `mini_batch`:
هذا عبارة عن مجموعة فرعية من بيانات التدريب تُستخدم في كل تكرار من تنفيذ خوارزمية الانحدار التدرجي العشوائي (Stochastic Gradient Descent). خوارزمية الانحدار التدرجي باستخدام الدُفعات الصغيرة (Mini-batch Gradient Descent) هي نسخة معدلة من خوارزمية الانحدار التدرجي العشوائي، حيث يتم تقسيم مجموعة بيانات التدريب الكاملة إلى دفعات أصغر، ويتم تحديث المعلمات باستخدام كل دفعة صغيرة على حدة.

الآن، دعونا نلقي نظرة على الكود نفسه:

```python
self.weights = [w-(eta/len(mini_batch))*nw
                for w, nw in zip(self.weights, nabla_w)]
```

في الكود أعلاه، يتم تحديث الأوزان (`self.weights`) باستخدام قاعدة التحديث التالية:

- `w`: الوزن الحالي.
- `eta`: معدل التعلم (learning rate).
- `len(mini_batch)`: حجم الدفعة الصغيرة (mini-batch).
- `nabla_w`: التدرج (gradient) بالنسبة للوزن.

يتم تحديث كل وزن عن طريق طرح جزء من التدرج مضروبًا في معدل التعلم مقسومًا على حجم الدفعة الصغيرة. هذا التحديث يتم تطبيقه على جميع الأوزان باستخدام list comprehension.

هذا السطر يقوم بتحديث أوزان الشبكة العصبية. يستخدم قائمة استيعابية (list comprehension) للتنقل عبر كل وزن `w` والتدرج المتناظر `nw`. لكل وزن، يتم طرح جزء من التدرج (مضروبًا في معدل التعلم `eta` وحجم الدُفعة الصغيرة) من الوزن الأصلي. هذه هي الطريقة التي يتم بها تحديث الأوزان لتقليل دالة التكلفة.

```python
self.biases = [b-(eta/len(mini_batch))*nb
               for b, nb in zip(self.biases, nabla_b)]
```

في الكود أعلاه، يتم تحديث قيم الانحيازات (`biases`) باستخدام قاعدة التحديث التدرج التنازلي (gradient descent). يتم ذلك عن طريق طرح جزء من التدرج (`nabla_b`) مضروبًا في معدل التعلم (`eta`) مقسومًا على حجم الدفعة الصغيرة (`mini_batch`) من كل قيمة انحياز حالية (`b`). يتم تنفيذ هذه العملية لكل زوج من الانحيازات الحالية والتدرجات المقابلة لها باستخدام الدالة `zip`.

هذا السطر يقوم بتحديث التحيزات (biases) لشبكة العصبية بطريقة مشابهة. يستخدم قائمة استيعاب (list comprehension) للتنقل عبر كل تحيز `b` والتدرج (gradient) المقابل له `nb`. لكل تحيز، يتم طرح جزء من التدرج (مضروبًا في معدل التعلم `eta` وحجم الدُفعة الصغيرة) من التحيز الأصلي.

باختصار، تقوم هذه الأسطر من الكود بتحديث الأوزان والانحيازات للشبكة العصبية باستخدام خوارزمية الانحدار التدرجي العشوائي (Stochastic Gradient Descent). يتم تكرار هذه العملية لكل مجموعة صغيرة (mini-batch) خلال مرحلة التدريب لتحسين معلمات الشبكة وتعزيز أدائها في المهمة المحددة.

----

Zhiwei: ما هو نموذج اللغة SpaCy؟

ChatGPT: SpaCy هي مكتبة مفتوحة المصدر لمعالجة اللغة الطبيعية (NLP) تم تطويرها بواسطة Explosion AI. تم تصميمها لتكون فعالة وسريعة وجاهزة للإنتاج، مما يجعلها خيارًا شائعًا لمهام معالجة اللغة الطبيعية المختلفة. توفر SpaCy نماذج لغوية مُدربة مسبقًا يمكنها معالجة وفهم النصوص، مما يسمح للمطورين بتنفيذ مهام مختلفة في معالجة اللغة الطبيعية مثل وسم أجزاء الكلام، والتعرف على الكيانات المسماة، وتحليل الجمل، وغير ذلك.

الميزات الرئيسية لنموذج اللغة SpaCy تشمل:

1. **التجزئة (Tokenization):** يمكن لـ SpaCy تقسيم النص إلى كلمات أو وحدات فردية (tokens)، مع مراعاة القواعد اللغوية المختلفة والتعقيدات.

2. **تحديد نوع الكلمة (Part-of-speech Tagging):** يمكن للمكتبة تعيين علامات تحدد نوع الكلمة لكل وحدة لغوية (token)، مما يشير إلى ما إذا كانت الكلمة اسمًا، فعلًا، صفةً، إلخ.

3. التعرف على الكيانات المسماة (NER): يمكن لـ SpaCy تحديد وتصنيف الكيانات مثل أسماء الأشخاص، والمنظمات، والمواقع، والتواريخ، وغيرها.

4. تحليل التبعيات (Dependency Parsing): يمكنه تحليل البنية النحوية للجملة وتحديد العلاقات بين الكلمات.

5. التصريف: يمكن لـ SpaCy تحويل الكلمات إلى شكلها الأساسي أو الجذر (اللامات).

6. متجهات الكلمات: توفر المكتبة متجهات الكلمات، المعروفة أيضًا باسم تضمينات الكلمات، وهي تمثيلات عددية كثيفة للكلمات تعبر عن المعنى الدلالي.

SpaCy يدعم لغات متعددة ويأتي مع نماذج مدربة مسبقًا للغات مختلفة، مما يجعله مستخدمًا على نطاق واسع في تطبيقات معالجة اللغة الطبيعية (NLP) المتنوعة، بما في ذلك استخراج المعلومات، تحليل المشاعر، روبوتات الدردشة، الترجمة اللغوية، وغيرها. بالإضافة إلى ذلك، يسمح SpaCy للمطورين بتدريب نماذج مخصصة على مجموعات البيانات الخاصة بهم إذا لزم الأمر.

---

Zhiwei: ما هو نموذج اللغة SpaCy؟

ChatGPT: SpaCy هي مكتبة مفتوحة المصدر لمعالجة اللغة الطبيعية (NLP) تم تطويرها بواسطة Explosion AI. تم تصميمها لتكون فعالة وسريعة وسهلة الاستخدام، مما يجعلها خيارًا شائعًا لمهام معالجة اللغة الطبيعية المختلفة. توفر SpaCy نماذج لغوية مُدرَّبة مسبقًا للعديد من اللغات، مما يسمح للمستخدمين بتنفيذ مهام مثل التجزئة (tokenization)، ووضع علامات على أجزاء الكلام (part-of-speech tagging)، والتعرف على الكيانات المسماة (named entity recognition)، وتحليل التبعيات (dependency parsing)، والمزيد.

جوهر سرعة وكفاءة SpaCy يكمن في تطبيقاته وهياكل بياناته المُحسّنة باستخدام Cython، مما يجعله مناسبًا بشكل خاص للبيئات الإنتاجية والتطبيقات الواقعية. تمت كتابة المكتبة بلغة Python وتأتي مع نماذج مُدربة مسبقًا للعديد من اللغات، بما في ذلك الإنجليزية، الألمانية، الفرنسية، الإسبانية، وغيرها.

تستخدم نماذج اللغة في SpaCy تقنيات التعلم العميق لتعلم الأنماط الأساسية في بيانات اللغة الطبيعية. يتم تدريب هذه النماذج على مجموعات كبيرة من النصوص، ويمكن بعد ذلك استخدام التمثيلات التي تم تعلمها في مهام معالجة اللغة الطبيعية المختلفة. يمكن أيضًا ضبط النماذج المدربة مسبقًا على بيانات محددة لتحقيق أداء أفضل في المهام المتعلقة بمجال معين.

جعلت البنية وسهولة الاستخدام من SpaCy خيارًا شائعًا بين المطورين والباحثين في مجتمع معالجة اللغة الطبيعية (NLP). غالبًا ما يتم استخدامها في مهام مثل استخراج المعلومات، تصنيف النصوص، التعرف على الكيانات المسماة، وسم أجزاء الكلام، والتحليل النحوي. بالإضافة إلى ذلك، يسمح التصميم المعياري لـ SpaCy للمستخدمين بدمجها بسهولة في سير عملهم وخطوط أنابيب NLP الحالية.

---

تشيوي: هل يمكنك أن تشرح؟

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
```

```python
local_rank = int(os.environ.get("LOCAL_RANK", 0))
torch.cuda.set_device(local_rank)
```

        # يجب أن يكون seed هو نفسه في جميع العمليات
        torch.manual_seed(1)

```python
if local_rank > 0:
    sys.stdout = open(os.devnull, "w")
```

```python
        start_time = time.time()
        checkpoints = sorted(Path(ckpt_dir).glob("*.pth"))
        assert len(checkpoints) > 0, f"لم يتم العثور على ملفات نقاط تفتيش في {ckpt_dir}"
        assert model_parallel_size == len(
            checkpoints
        ), f"جارٍ تحميل نقطة تفتيش لـ MP={len(checkpoints)} ولكن حجم العالم هو {model_parallel_size}"
        ckpt_path = checkpoints[get_model_parallel_rank()]
        checkpoint = torch.load(ckpt_path, map_location="cpu")
        with open(Path(ckpt_dir) / "params.json", "r") as f:
            params = json.loads(f.read())
```

قم بتشغيل الأمر ثم احصل على سجل الأخطاء.

```shell
% torchrun --nproc_per_node 1 example_text_completion.py \
    --ckpt_dir llama-2-7b/ \
    --tokenizer_path tokenizer.model \
    --max_seq_len 128 --max_batch_size 4
ملاحظة: إعادة التوجيه غير مدعومة حاليًا في Windows أو MacOs.
Traceback (آخر استدعاء أخير):
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
RuntimeError: الحزمة الموزعة لا تحتوي على NCCL مدمج
ERROR:torch.distributed.elastic.multiprocessing.api:فشل (رمز الخروج: 1) local_rank: 0 (pid: 23273) من الملف الثنائي: /Users/lzwjava/anaconda3/bin/python
```

```plaintext
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

تعلم تتبع مكدس الأخطاء.

اسأل ChatGPT عن معنى Backend.NCCL في Pytorch؟

---

تشيوي:

```code```

```python
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
```

```python
model_path = '.'
# model_path = 'openlm-research/open_llama_7b'
```

```python
tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map='auto',
)
```

```python
prompt = 'Q: ما هو أكبر حيوان؟\nA:'
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=32
)
print(tokenizer.decode(generation_output[0]))
```

خطأ:

```shell
/home/lzw/anaconda3/envs/llama/lib/python3.11/site-packages/transformers/generation/utils.py:1445: UserWarning: أنت تستدعي .generate() مع وجود `input_ids` على نوع جهاز مختلف عن جهاز النموذج الخاص بك. `input_ids` موجود على وحدة المعالجة المركزية (CPU)، بينما النموذج موجود على وحدة معالجة الرسومات (CUDA). قد تواجه سلوكيات غير متوقعة أو توليد أبطأ. يرجى التأكد من أنك قمت بوضع `input_ids` على الجهاز الصحيح عن طريق استدعاء input_ids = input_ids.to('cuda') قبل تشغيل `.generate()`.
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
RuntimeError: كان من المتوقع أن تكون جميع الموترات على نفس الجهاز، ولكن تم العثور على جهازين على الأقل، cuda:0 و cpu! (عند التحقق من الوسيط index في طريقة wrapper_CUDA__index_select)
```

كيفية الإصلاح؟

ChatGPT:

تشير رسالة الخطأ التي تواجهها إلى وجود عدم تطابق في أنواع الأجهزة بين موتر الإدخال (`input_ids`) ونموذجك (`LlamaForCausalLM`). موتر الإدخال موجود على وحدة المعالجة المركزية (`cpu`)، بينما النموذج موجود على وحدة معالجة الرسومات (`cuda`). لإصلاح هذا، تحتاج إلى التأكد من أن موتر الإدخال موجود على نفس الجهاز الذي يوجد عليه النموذج قبل توليد النص باستخدام النموذج.

إليك الكود المعدل لإصلاح المشكلة:

```python
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
```

```python
model_path = '.'
# model_path = 'openlm-research/open_llama_7b'
```

```python
tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map='auto',
)
```

prompt = 'Q: ما هو أكبر حيوان؟\nA:'
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

# نقل tensor input_ids إلى نفس الجهاز الذي يعمل عليه النموذج
input_ids = input_ids.to(model.device)

```python
generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=32
)
print(tokenizer.decode(generation_output[0]))
```

في هذا الكود، أضفت السطر `input_ids = input_ids.to(model.device)` بعد الحصول على مصفوفة `input_ids` من الأداة المخصصة للتحويل (tokenizer). هذا السطر ينقل مصفوفة `input_ids` إلى نفس الجهاز الذي يعمل عليه النموذج (سواء كان CPU أو GPU) قبل توليد النص. هذا الإجراء يجب أن يحل مشكلة "Expected all tensors to be on the same device".

تذكر أنه إذا كنت تقوم بتشغيل هذا الكود على جهاز يدعم وحدة معالجة الرسوميات (GPU) وكان نموذجك يعمل على وحدة معالجة الرسوميات، فمن الأفضل عمومًا الاحتفاظ بكل من النموذج وبيانات الإدخال على وحدة معالجة الرسوميات للاستفادة من إمكانيات المعالجة المتوازية.

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
```

```python
min_prompt_len = min(len(t) for t in prompt_tokens)
max_prompt_len = max(len(t) for t in prompt_tokens)
assert max_prompt_len <= params.max_seq_len
total_len = min(params.max_seq_len, max_gen_len + max_prompt_len)
```

تم ترجمة الكود أعلاه إلى:

```python
min_prompt_len = min(len(t) for t in prompt_tokens)
max_prompt_len = max(len(t) for t in prompt_tokens)
assert max_prompt_len <= params.max_seq_len
total_len = min(params.max_seq_len, max_gen_len + max_prompt_len)
```

```python
pad_id = self.tokenizer.pad_id
tokens = torch.full((bsz, total_len), pad_id, dtype=torch.long, device="cuda")
for k, t in enumerate(prompt_tokens):
    tokens[k, : len(t)] = torch.tensor(t, dtype=torch.long, device="cuda")
if logprobs:
    token_logprobs = torch.zeros_like(tokens, dtype=torch.float)
```

```python
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
```

```python
            next_token = next_token.reshape(-1)
            # استبدال الرمز فقط إذا تم إنشاء النص المطلوب بالفعل
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
```

```python
        if logprobs:
            token_logprobs = token_logprobs.tolist()
        out_tokens, out_logprobs = [], []
        for i, toks in enumerate(tokens.tolist()):
            # قص إلى الحد الأقصى لطول التوليد
            start = 0 if echo else len(prompt_tokens[i])
            toks = toks[start : len(prompt_tokens[i]) + max_gen_len]
            probs = None
            if logprobs:
                probs = token_logprobs[i][start : len(prompt_tokens[i]) + max_gen_len]
            # قص إلى رمز نهاية الجملة إذا وجد
            if self.tokenizer.eos_id in toks:
                eos_idx = toks.index(self.tokenizer.eos_id)
                toks = toks[:eos_idx]
                probs = probs[:eos_idx] if logprobs else None
            out_tokens.append(toks)
            out_logprobs.append(probs)
        return (out_tokens, out_logprobs if logprobs else None)
```

بالطبع! الكود المقدم هو طريقة تُسمى `generate` تأخذ نصًا مُدخلًا (prompt) وتُنشئ نصًا باستخدام نموذج لغوي. تم تصميم هذه الطريقة للعمل مع نموذج ومُرمز معينين وتقوم بإنشاء النص باستخدام إما أخذ العينات الجشعة (greedy sampling) أو أخذ العينات من أعلى الاحتمالات (top-p sampling). إليك تفصيل لكيفية عمل هذه الطريقة:

1. **معلمات الطريقة:**
   - `prompt_tokens`: قائمة بالرموز المميزة (tokens) للطلبات، حيث يتم تمثيل كل طلب كقائمة من الأعداد الصحيحة (معرفات الرموز).
   - `max_gen_len`: الطول الأقصى للناتج المُولد (بالرموز).
   - `temperature`: معلمة تتحكم في عشوائية الناتج. القيم الأعلى (مثل 1.0) تجعل الناتج أكثر عشوائية، بينما القيم الأقل (مثل 0.6) تجعله أكثر حتمية.
   - `top_p`: معلمة تتحكم في تنوع النص المُولد. القيم الأعلى (مثل 0.9) تسمح بعينات أكثر تنوعًا.
   - `logprobs`: إذا كانت `True`، فإن الطريقة تُرجع أيضًا اللوغاريتمات الاحتمالية للرموز المولدة.
   - `echo`: إذا كانت `True`، فإن الناتج المُولد سيتضمن الطلب نفسه.

2. **التهيئة:**
   تقوم الطريقة بتهيئة المتغيرات مثل `params`، و`bsz` (حجم الدُفعة)، و`min_prompt_len`، و`max_prompt_len`. كما تقوم بحساب `total_len` وهو الطول الكلي للمخرجات المولدة بما في ذلك النص المبدئي.

3. **إنشاء الرموز (Token Generation):**
   تقوم الطريقة بإنشاء رموز للنص الناتج. تستخدم حلقة للتكرار عبر المواضع في التسلسل المُنشأ، بدءًا من نهاية المطالبة (prompt) والتحرك للأمام.
   
   - يتم الحصول على القيم اللوغاريتمية (logits) لكل موضع عن طريق تمرير التسلسل الجزئي إلى دالة التقدم (forward function) للنموذج.
   - إذا كانت قيمة `temperature` أكبر من 0، يتم تحويل القيم اللوغاريتمية إلى احتمالات باستخدام دالة softmax مع قيمة درجة الحرارة المحددة. إذا كانت `temperature` تساوي 0، يتم اختيار الرمز ذو القيمة اللوغاريتمية الأعلى باستخدام `torch.argmax`.
   - يتم تحديد الرمز التالي بناءً على الاحتمالات المُنشأة أو القيمة المحددة بواسطة `argmax`، ويتم وضعه في الموضع المناسب في مصفوفة `tokens`.
   - يتم اكتشاف رموز نهاية التسلسل (EOS)، وإذا وصلت جميع التسلسلات إلى رمز EOS، يتم إيقاف عملية الإنشاء.
   - يتم الاحتفاظ بالرموز المُنشأة في مصفوفة `tokens`.

4. **معالجة الناتج المُنشأ:**
   - يتم معالجة الرموز المُنشأة لتقليم الناتج إلى الطول الأقصى المطلوب (`max_gen_len`).
   - إذا كانت قيمة `echo` هي `True`، يتم تضمين النص المطلوب في الناتج المُنشأ.
   - إذا تم مواجهة رمز `eos`، يتم قطع النص المُنشأ عند تلك النقطة.

5. **الإرجاع:**
   تُرجع الدالة مجموعة (tuple) تحتوي على الرموز المولدة، وإذا كانت `logprobs` تساوي `True`، فإنها تُرجع أيضًا اللوغاريتمات الاحتمالية (log-probabilities) للرموز المولدة.

هذه الطريقة تولد النص من خلال التنبؤ التكراري للرموز بناءً على السياق المقدم من خلال المطالبة والرموز التي تم إنشاؤها مسبقًا. تستخدم معلمات التوليد المحددة للتحكم في العشوائية والتنوع للنص المولد. تم تصميم هذه الطريقة لاستخدامها مع بنية نموذجية محددة ومُعَدِّل، حيث تعتمد على خصائصها وطرقها لتوليد النص.

---