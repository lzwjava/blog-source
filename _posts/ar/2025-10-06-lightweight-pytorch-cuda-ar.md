---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: موارد تعلم PyTorch و CUDA خفيفة الوزن
translated: true
type: note
---

إذا كان tinygrad يبدو مربكًا بسبب حجمه الكودي الكبير، فهناك بدائل أخف وأكثر تركيزًا للتعمق في أطر عمل شبيهة بـ PyTorch أو المشاريع القائمة على CUDA. تركز هذه البدائل على البساطة التعليمية، حيث غالبًا ما تتكون من بضع مئات فقط من أسطر الكود، لمساعدتك على فهم الآليات الداخلية مثل autograd، أو الموترات (tensors)، أو نواة GPU (GPU kernels) دون التعقيد الكامل لإطار العمل. سأقوم بتقسيمها حسب مجال التركيز.

### تنفيذات بسيطة شبيهة بـ PyTorch (لتعلم أساسيات أطر عمل التعلم العميق)
هذه إعادة تنفيذ مصغرة تحاكي آليات PyTorch الأساسية (مثل الموترات، والانتشار العكسي backprop) ولكنها تتخلص من كل شيء آخر.

- **Micrograd**: محرك autograd فائق البساطة (أقل من 200 سطر) يشغل الشبكات العصبية من الصفر. إنه مثالي لفهم عملية الانتشار العكسي (backward pass) والتدرجات (gradients) في PyTorch. يرافقها فيديو تعليمي من أندريه كارباثي يشرحها خطوة بخطوة، حتى الوصول إلى شبكة MLP بسيطة. ابدأ من هنا إذا كنت تريد فهم جوهر الرسم البياني الحسابي الديناميكي (dynamic computation graph) في PyTorch.

- **minGPT**: إعادة تنفيذ نظيفة وسهلة الفهم لـ GPT في حوالي 300 سطر من كود PyTorch. يغطي عملية التحويل إلى الرموز (tokenization)، وطبقات المحولات (transformer layers)، وحلقات التدريب والاستدلال. رائع لرؤية كيف يتم ربط مكونات PyTorch معًا دون إضافات—مثالي إذا كنت مهتمًا بالنماذج التوليدية.

- **Mamba Minimal**: تنفيذ لـ Mamba state-space model في ملف واحد باستخدام PyTorch. إنه صغير جدًا (حوالي 100 سطر للنواة الأساسية) ويتطابق مع المخرجات الرسمية، مما يساعدك على تعلم عمليات المسح الانتقائي (selective scan ops) وآليات نمذجة التسلسل الداخلية.

### خيارات صغيرة شبيهة بـ TensorFlow
يوجد عدد أقل من النسخ المصغرة "الصرفة" لـ TensorFlow، ولكن هذه المشاريع تخدش السطح:

- **Mini TensorFlow from Scratch**: بناء من الصفر لمكتبة أساسية شبيهة بـ TensorFlow تركز على الرسوم البيانية القابلة للاشتقاق (differentiable graphs) والعمليات (ops). إنه مشروع تعليمي قصير (باستخدام Python فقط) يشرح عمليات الموترات والانتشار العكسي دون تعقيدات GPU—جيد للمقارنة مع الوضع الحثيث (eager mode) في PyTorch.

- **Tract**: محرك استدلال (inference engine) لـ TensorFlow/ONNX بسيط ومستقل في لغة Rust (ولكن مع روابط Python). إنه صغير ويركز على وقت التنفيذ، ومفيد لتعلم كيفية تشغيل نماذج TF تحت الغطاء دون عبء التدريب.

### مشاريع/دروس عامة حول CUDA (للتعلم المرتكز على GPU)
إذا كنت تريد التركيز على نواة CUDA إلى جانب جوهر PyTorch، فإن هذه المشاريع ترشدك خلال العمليات المخصصة (custom ops) أو أطر العمل الكاملة مع دعم GPU:

- **PyTorch from Scratch with CUDA**: مشروع عملي لإعادة إنشاء نواة PyTorch (الموترات، autograd، المُحسّنات optimizers) باستخدام C++/CUDA/Python. يتضمن تسريع GPU وينتهي بشبكة عصبية عاملة—ممتاز لربط PyTorch عالي المستوى بـ CUDA منخفض المستوى دون الغرق في الكود.

- **Writing CUDA Kernels for PyTorch**: دليل مناسب للمبتدئين لصنع ملحقات CUDA مخصصة في PyTorch. يبدأ بالأساسيات (ضرب المصفوفات على GPU) ويتدرج إلى العمليات الحقيقية، مع مقاطع كود يمكنك تعديلها. اقترنه بالوثائق الرسمية لملحقات PyTorch لتحقيق نتائج سريعة.

- **Implementing PyTorch CUDA Operators Tutorial**: شرح خطوة بخطوة لكيفية كتابة ودمج نواة CUDA في PyTorch (مثل الالتفافات المخصصة custom convolutions). يعتمد على الأسلوب التعليمي، كما لو كنت تشرح لصديق، ويفترض معرفة أساسية بـ C++—يركز على "كيفية" تحقيق تسريع GPU في أطر عمل التعلم العميق.

ابدأ بـ micrograd أو minGPT لتحقيق زخم سريع—فهما الأكثر سهولة في الفهم. إذا كان الهدف هو CUDA، فانتقل إلى مشروع PyTorch من الصفر. كل هذه المشاريع موجودة على GitHub، لذا يمكنك نسخها وتجربتها.

[Micrograd](https://github.com/karpathy/micrograd)
[minGPT](https://github.com/karpathy/minGPT)
[Mamba Minimal](https://github.com/johnma2006/mamba-minimal)
[Mini TensorFlow from Scratch](https://salviosage.medium.com/build-mini-tensorflow-like-library-from-scratch-fc28c9660037)
[Tract](https://github.com/sonos/tract)
[PyTorch from Scratch with CUDA](https://medium.com/data-science/recreating-pytorch-from-scratch-with-gpu-support-and-automatic-differentiation-8f565122a3cc)
[Writing CUDA Kernels for PyTorch](https://tinkerd.net/blog/machine-learning/cuda-basics/)
[Implementing PyTorch CUDA Operators](https://medium.com/@justygwen/teach-you-to-implement-pytorch-cuda-operators-like-teaching-a-loved-one-dbd572410558)