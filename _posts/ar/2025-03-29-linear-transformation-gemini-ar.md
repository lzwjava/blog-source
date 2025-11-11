---
audio: false
generated: true
lang: ar
layout: post
title: التحولات الخطية - جيميني
translated: true
type: note
---

حسنًا، دعنا نتعمق في برنامج تعليمي مفصل حول التحويلات الخطية، يغطي التعريف، الأمثلة، التمثيل المصفوفي، النواة، الصورة، والخصائص مثل الحقنية والانطباقية. هذا موضوع أساسي في الجبر الخطي.

## 6. التحويلات الخطية: برنامج تعليمي مفصل

**التحويل الخطي** هو دالة بين فضاءين متجهين تحافظ على عمليتي جمع المتجهات والضرب القياسي. ليكن \\(V\\) و \\(W\\) فضاءين متجهين فوق نفس الحقل \\(F\\) (والذي غالبًا ما يكون مجموعة الأعداد الحقيقية \\(\mathbb{R}\\) أو الأعداد المركبة \\(\mathbb{C}\\)).

**التعريف:** الدالة \\(T: V \rightarrow W\\) هي تحويل خطي إذا حققت الخاصيتين التاليتين لجميع المتجهات \\(\mathbf{u}, \mathbf{v} \in V\\) وجميع القياسات \\(c \in F\\):

1.  **الجمعية:** \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})\\)
2.  **التجانس (الضرب القياسي):** \\(T(c\mathbf{u}) = cT(\mathbf{u})\\)

يمكن دمج هاتين الخاصيتين في شرط واحد:
\\(T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})\\) لجميع \\(\mathbf{u}, \mathbf{v} \in V\\) وجميع القياسات \\(c, d \in F\\).

**النتائج الرئيسية للخطية:**

* \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)، حيث \\(\mathbf{0}_V\\) هو المتجه الصفري في \\(V\\) و \\(\mathbf{0}_W\\) هو المتجه الصفري في \\(W\\). (البرهان: \\(T(\mathbf{0}_V) = T(0\mathbf{u}) = 0T(\mathbf{u}) = \mathbf{0}_W\\) لأي \\(\mathbf{u} \in V\\)).
* \\(T(-\mathbf{u}) = -T(\mathbf{u})\\). (البرهان: \\(T(-\mathbf{u}) = T((-1)\mathbf{u}) = (-1)T(\mathbf{u}) = -T(\mathbf{u})\\)).

### أمثلة على التحويلات الخطية

لنلقِ نظرة على بعض الأمثلة لفهم المفهوم بشكل أفضل.

**المثال 1: تحويل في \\(\mathbb{R}^2\\) (الدوران)**

افترض تحويلاً \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) يقوم بتدوير كل متجه في \\(\mathbb{R}^2\\) عكس اتجاه عقارب الساعة بزاوية \\(\theta\\). إذا كان \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\)، فإن \\(T(\mathbf{v}) = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}\\).

لنتحقق مما إذا كان هذا تحويلاً خطياً. لنفرض أن \\(\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}\\) و \\(\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\\)، ولنفرض أن \\(c\\) عدد قياسي.

* **الجمعية:**
    \\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2)\cos\theta - (y_1 + y_2)\sin\theta \\ (x_1 + x_2)\sin\theta + (y_1 + y_2)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} (x_1\cos\theta - y_1\sin\theta) + (x_2\cos\theta - y_2\sin\theta) \\ (x_1\sin\theta + y_1\cos\theta) + (x_2\sin\theta + y_2\cos\theta) \end{pmatrix} = T(\mathbf{u}) + T(\mathbf{v})\\)

* **التجانس:**
    \\(T(c\mathbf{u}) = T\left(\begin{pmatrix} cx_1 \\ cy_1 \end{pmatrix}\right) = \begin{pmatrix} (cx_1)\cos\theta - (cy_1)\sin\theta \\ (cx_1)\sin\theta + (cy_1)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} c(x_1\cos\theta - y_1\sin\theta) \\ c(x_1\sin\theta + y_1\cos\theta) \end{pmatrix} = c \begin{pmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \end{pmatrix} = cT(\mathbf{u})\\)

وبالتالي، فإن الدوران هو تحويل خطي.

**المثال 2: تحويل في \\(\mathbb{R}^2\\) (الإسقاط على المحور السيني)**

افترض \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) معرفًا بالعلاقة \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x \\ 0 \end{pmatrix}\\). يحول هذا التحويل كل متجه إلى الإسقاط على المحور السيني. يمكنك التحقق من أن هذا أيضًا تحويل خطي باستخدام التعريف.

**المثال 3: تحويل في \\(\mathbb{R}^2\\) (الانزياح)**

افترض \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) معرفًا بالعلاقة \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + a \\ y + b \end{pmatrix}\\)، حيث \\(a\\) و \\(b\\) ثابتان (ليسا صفرًا معًا).

لنتحقق من الخاصية الأولى:
\\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2) + a \\ (y_1 + y_2) + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)

يبدو هذا صحيحًا، دعنا نتحقق مرة أخرى.
\\(T(\mathbf{u} + \mathbf{v}) = \begin{pmatrix} x_1 + x_2 + a \\ y_1 + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + x_2 + 2a \\ y_1 + y_2 + 2b \end{pmatrix}\\)

إذا كان \\(a \neq 0\\) أو \\(b \neq 0\\)، فإن \\(T(\mathbf{u} + \mathbf{v}) \neq T(\mathbf{u}) + T(\mathbf{v})\\). أيضًا، \\(T(\mathbf{0}) = T\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} a \\ b \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}\\) إذا كان \\(a\\) أو \\(b\\) غير صفري. لذلك، فإن الانزياح بشكل عام **ليس** تحويلاً خطياً.

**المثال 4: تحويل من \\(\mathbb{R}^n\\) إلى \\(\mathbb{R}^m\\) معرف بمصفوفة**

لنفرض أن \\(A\\) مصفوفة من الرتبة \\(m \times n\\). التحويل \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) المعرف بالعلاقة \\(T(\mathbf{x}) = A\mathbf{x}\\) (حيث \\(\mathbf{x}\\) متجه عمودي من الرتبة \\(n \times 1\\)) هو تحويل خطي. هذا لأن ضرب المصفوفات يحقق خصائص الجمعية والتجانس:
\\(A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}\\)
\\(A(c\mathbf{u}) = c(A\mathbf{u})\\)

**المثال 5: اشتقاق متعددات الحدود**

لنفرض أن \\(P_n\\) هو فضاء المتجهات لمتعددات الحدود من الدرجة على الأكثر \\(n\\). التحويل \\(D: P_n \rightarrow P_{n-1}\\) المعرف بالعلاقة \\(D(p(x)) = p'(x)\\) (مشتق \\(p(x)\\)) هو تحويل خطي.
إذا كان \\(p(x)\\) و \\(q(x)\\) متعددي حدود و \\(c\\) عدد قياسي:
\\(D(p(x) + q(x)) = (p(x) + q(x))' = p'(x) + q'(x) = D(p(x)) + D(q(x))\\)
\\(D(cp(x)) = (cp(x))' = cp'(x) = cD(p(x))\\)

**المثال 6: تكامل الدوال**

لنفرض أن \\(C[a, b]\\) هو فضاء المتجهات للدوال المستمرة على الفترة \\([a, b]\\). التحويل \\(I: C[a, b] \rightarrow \mathbb{R}\\) المعرف بالعلاقة \\(I(f) = \int_a^b f(x) dx\\) هو تحويل خطي.
\\(I(f + g) = \int_a^b (f(x) + g(x)) dx = \int_a^b f(x) dx + \int_a^b g(x) dx = I(f) + I(g)\\)
\\(I(cf) = \int_a^b cf(x) dx = c \int_a^b f(x) dx = cI(f)\\)

### التمثيل المصفوفي للتحويل الخطي

نتيجة أساسية في الجبر الخطي هي أن أي تحويل خطي بين فضاءين متجهين ذوي أبعاد منتهية يمكن تمثيله بمصفوفة.

لنفرض أن \\(V\\) فضاء متجهي ذو بعد \\(n\\) مع الأساس \\(\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) و \\(W\\) فضاء متجهي ذو بعد \\(m\\) مع الأساس \\(\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, ..., \mathbf{c}_m\}\\). لنفرض أن \\(T: V \rightarrow W\\) تحويل خطي.

لإيجاد التمثيل المصفوفي لـ \\(T\\) بالنسبة للأساسين \\(\mathcal{B}\\) و \\(\mathcal{C}\\) (ويرمز له بـ \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) أو ببساطة \\([T]\\) عندما يكون الأساسان مفهومين)، نحتاج إلى تحديد صور متجهات الأساس لـ \\(V\\) تحت تأثير \\(T\\) والتعبير عن هذه الصور كتركيبات خطية من متجهات الأساس لـ \\(W\\).

لكل \\(\mathbf{b}_j \in \mathcal{B}\\)، فإن \\(T(\mathbf{b}_j)\\) هو متجه في \\(W\\)، لذا يمكن كتابته بشكل فريد كتركيب خطي من متجهات الأساس في \\(\mathcal{C}\\):
\\(T(\mathbf{b}_j) = a_{1j}\mathbf{c}_1 + a_{2j}\mathbf{c}_2 + ... + a_{mj}\mathbf{c}_m = \sum_{i=1}^{m} a_{ij}\mathbf{c}_i\\)

معاملات هذا التركيب الخطي تشكل العمود \\(j\\) من التمثيل المصفوفي \\([T]_{\mathcal{B}}^{\mathcal{C}}\\):
$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$

إذا كان للمتجه \\(\mathbf{v} \in V\\) متجه إحداثيات \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}\\) بالنسبة للأساس \\(\mathcal{B}\\)، فإن متجه إحداثيات \\(T(\mathbf{v})\\) بالنسبة للأساس \\(\mathcal{C}\\)، ويرمز له بـ \\([T(\mathbf{v})]_{\mathcal{C}}\\)، يعطى بمنتج المصفوفة:
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}}\\)

**مثال: التمثيل المصفوفي**

لنفرض أن \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) تحويل خطي معرف بالعلاقة \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\). لنفرض أن الأساسيات القياسية لـ \\(\mathbb{R}^2\\) و \\(\mathbb{R}^3\\) هي \\(\mathcal{B} = \{\mathbf{e}_1, \mathbf{e}_2\} = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}\\) و \\(\mathcal{C} = \{\mathbf{f}_1, \mathbf{f}_2, \mathbf{f}_3\} = \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\\).

نوجد صور متجهات الأساس لـ \\(\mathbb{R}^2\\) تحت تأثير \\(T\\):
\\(T(\mathbf{e}_1) = T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 + 0 \\ 2(1) - 0 \\ 3(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} = 1\mathbf{f}_1 + 2\mathbf{f}_2 + 0\mathbf{f}_3\\)
\\(T(\mathbf{e}_2) = T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0 + 1 \\ 2(0) - 1 \\ 3(1) \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = 1\mathbf{f}_1 - 1\mathbf{f}_2 + 3\mathbf{f}_3\\)

التمثيل المصفوفي لـ \\(T\\) بالنسبة للأساسيات القياسية هو:
\\([T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix}\\)

الآن، لنأخذ متجهًا عشوائيًا \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\) في \\(\mathbb{R}^2\\). متجه إحداثياته بالنسبة لـ \\(\mathcal{B}\\) هو \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x \\ y \end{pmatrix}\\).
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)
متجه الإحداثيات بالنسبة لـ \\(\mathcal{C}\\) هو بالفعل \\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)، والذي يتوافق مع المتجه \\(T(\mathbf{v})\\) الذي عرفناه سابقًا.

### النواة (الفضاء الفراغي) للتحويل الخطي

**النواة** (أو الفضاء الفراغي) للتحويل الخطي \\(T: V \rightarrow W\\)، ويرمز لها بـ \\(\text{ker}(T)\\) أو \\(N(T)\\)، هي مجموعة جميع المتجهات في \\(V\\) التي تتحول إلى المتجه الصفري في \\(W\\):
\\(\text{ker}(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}\\)

**خصائص النواة:**

* نواة التحويل الخطي هي دائمًا فضاء جزئي من المجال \\(V\\).
    * **تحتوي على المتجه الصفري:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)، لذا \\(\mathbf{0}_V \in \text{ker}(T)\\).
    * **مغلقة تحت الجمع:** إذا كان \\(\mathbf{u}, \mathbf{v} \in \text{ker}(T)\\)، فإن \\(T(\mathbf{u}) = \mathbf{0}_W\\) و \\(T(\mathbf{v}) = \mathbf{0}_W\\). وبالتالي، \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W\\)، لذا \\(\mathbf{u} + \mathbf{v} \in \text{ker}(T)\\).
    * **مغلقة تحت الضرب القياسي:** إذا كان \\(\mathbf{u} \in \text{ker}(T)\\) و \\(c\\) عدد قياسي، فإن \\(T(c\mathbf{u}) = cT(\mathbf{u}) = c\mathbf{0}_W = \mathbf{0}_W\\)، لذا \\(c\mathbf{u} \in \text{ker}(T)\\).

**مثال: إيجاد النواة**

افترض التحويل الخطي \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) المعرف بالعلاقة \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\).
لإيجاد النواة، نحتاج إلى حل \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\):
\\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\)

هذا يعطي نظام المعادلات الخطية:
\\(x + y = 0\\)
\\(2x - y = 0\\)
\\(3y = 0\\)

من المعادلة الثالثة، \\(y = 0\\). بالتعويض في المعادلة الأولى، \\(x + 0 = 0\\)، لذا \\(x = 0\\). المعادلة الثانية محققة أيضًا: \\(2(0) - 0 = 0\\).
الحل الوحيد هو \\(x = 0\\) و \\(y = 0\\). لذلك، \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\\}\)، وهي الفضاء الجزئي الصفري لـ \\(\mathbb{R}^2\\).

### الصورة (المدى) للتحويل الخطي

**الصورة** (أو المدى) للتحويل الخطي \\(T: V \rightarrow W\\)، ويرمز لها بـ \\(\text{im}(T)\\) أو \\(R(T)\\)، هي مجموعة جميع المتجهات في \\(W\\) التي هي صورة لمتجه ما في \\(V\\):
\\(\text{im}(T) = \{\mathbf{w} \in W \mid \mathbf{w} = T(\mathbf{v}) \text{ لمتجه } \mathbf{v} \in V\}\\)

**خصائص الصورة:**

* صورة التحويل الخطي هي دائمًا فضاء جزئي من المجال المقابل \\(W\\).
    * **تحتوي على المتجه الصفري:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)، لذا \\(\mathbf{0}_W \in \text{im}(T)\\).
    * **مغلقة تحت الجمع:** إذا كان \\(\mathbf{w}_1, \mathbf{w}_2 \in \text{im}(T)\\)، فإن هناك متجهين \\(\mathbf{v}_1, \mathbf{v}_2 \in V\\) بحيث \\(T(\mathbf{v}_1) = \mathbf{w}_1\\) و \\(T(\mathbf{v}_2) = \mathbf{w}_2\\). إذن \\(\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{v}_1) + T(\mathbf{v}_2) = T(\mathbf{v}_1 + \mathbf{v}_2)\\). بما أن \\(\mathbf{v}_1 + \mathbf{v}_2 \in V\\)، فإن \\(\mathbf{w}_1 + \mathbf{w}_2 \in \text{im}(T)\\).
    * **مغلقة تحت الضرب القياسي:** إذا كان \\(\mathbf{w} \in \text{im}(T)\\) و \\(c\\) عدد قياسي، فإن هناك متجه \\(\mathbf{v} \in V\\) بحيث \\(T(\mathbf{v}) = \mathbf{w}\\). إذن \\(c\mathbf{w} = cT(\mathbf{v}) = T(c\mathbf{v})\\). بما أن \\(c\mathbf{v} \in V\\)، فإن \\(c\mathbf{w} \in \text{im}(T)\\).

* إذا كان \\(V\\) ذو أبعاد منتهية مع أساس \\(\{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\)، فإن صورة \\(T\\) هي المدى الممتد لصور متجهات الأساس:
    \\(\text{im}(T) = \text{span}\{T(\mathbf{b}_1), T(\mathbf{b}_2), ..., T(\mathbf{b}_n)\}\\)

**مثال: إيجاد الصورة**

افترض التحويل الخطي \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) المعرف بالعلاقة \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\).
باستخدام الأساس القياسي لـ \\(\mathbb{R}^2\\)، \\(\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\}\\)، لدينا:
\\(T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\)
\\(T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\)

صورة \\(T\\) هي المدى الممتد لهذين المتجهين:
\\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\\}\\
هذا فضاء جزئي من \\(\mathbb{R}^3\\). بما أن هذين المتجهين مستقلين خطيًا (أحدهما ليس مضاعفًا قياسيًا للآخر)، فإن الصورة هي مستوى يمر بنقطة الأصل في \\(\mathbb{R}^3\\).

**العلاقة بين التمثيل المصفوفي والصورة:**

إذا كان \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) معطى بالعلاقة \\(T(\mathbf{x}) = A\mathbf{x}\\)، حيث \\(A\\) مصفوفة من الرتبة \\(m \times n\\)، فإن صورة \\(T\\) هي فضاء أعمدة المصفوفة \\(A\\)، أي المدى الممتد لأعمدة \\(A\\).

### خصائص التحويلات الخطية: الحقنية والانطباقية

**الحقنية (واحد لواحد)**

التحويل الخطي \\(T: V \rightarrow W\\) هو **حقني** (أو واحد لواحد) إذا كان لكل \\(\mathbf{w} \in W\\)، يوجد على الأكثر متجه واحد \\(\mathbf{v} \in V\\) بحيث \\(T(\mathbf{v}) = \mathbf{w}\\). وبالمكافئ، إذا كان \\(T(\mathbf{u}) = T(\mathbf{v})\\)، فإن \\(\mathbf{u} = \mathbf{v}\\).

**نظرية:** التحويل الخطي \\(T: V \rightarrow W\\) هو حقني إذا وفقط إذا كانت نواته هي الفضاء الجزئي الصفري، أي \\(\text{ker}(T) = \{\mathbf{0}_V\\}\\).

**البرهان:**
* **(\\(\Rightarrow\\)) افترض أن \\(T\\) حقني.** إذا كان \\(\mathbf{v} \in \text{ker}(T)\\)، فإن \\(T(\mathbf{v}) = \mathbf{0}_W\\). نعلم أيضًا أن \\(T(\mathbf{0}_V) = \mathbf{0}_W\\). بما أن \\(T\\) حقني و \\(T(\mathbf{v}) = T(\mathbf{0}_V)\\)، فلا بد أن \\(\mathbf{v} = \mathbf{0}_V\\). وبالتالي، \\(\text{ker}(T) = \{\mathbf{0}_V\\}\\).
* **(\\(\Leftarrow\\)) افترض أن \\(\text{ker}(T) = \{\mathbf{0}_V\\}\\).** افترض أن \\(T(\mathbf{u}) = T(\mathbf{v})\\) لمتجهين \\(\mathbf{u}, \mathbf{v} \in V\\). إذن \\(T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{0}_W\\). بسبب الخطية، \\(T(\mathbf{u} - \mathbf{v}) = \mathbf{0}_W\\). هذا يعني أن \\(\mathbf{u} - \mathbf{v} \in \text{ker}(T)\\). بما أن \\(\text{ker}(T) = \{\mathbf{0}_V\\}\\)، فإن \\(\mathbf{u} - \mathbf{v} = \mathbf{0}_V\\)، مما يعني أن \\(\mathbf{u} = \mathbf{v}\\). لذلك، \\(T\\) حقني.

**مثال: التحقق من الحقنية**

بالنسبة للتحويل \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) المعرف بالعلاقة \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)، وجدنا أن \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\\}\\). لذلك، هذا التحويل حقني.

**الانطباقية (شامل)**

التحويل الخطي \\(T: V \rightarrow W\\) هو **انطباقي** (أو شامل) إذا كان لكل \\(\mathbf{w} \in W\\)، يوجد على الأقل متجه واحد \\(\mathbf{v} \in V\\) بحيث \\(T(\mathbf{v}) = \mathbf{w}\\). بعبارة أخرى، صورة \\(T\\) تساوي المجال المقابل \\(W\\)، أي \\(\text{im}(T) = W\\).

**نظرية (رتبة-بطل):** للتحويل الخطي \\(T: V \rightarrow W\\)، حيث \\(V\\) فضاء متجهي ذو أبعاد منتهية،
\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\)
هنا، \\(\text{dim}(\text{ker}(T))\\) تسمى **البطل** لـ \\(T\\)، و \\(\text{dim}(\text{im}(T))\\) تسمى **الرتبة** لـ \\(T\\).

**العلاقة بين الانطباقية والأبعاد:**

إذا كان \\(T: V \rightarrow W\\) تحويل خطي بين فضاءين متجهين ذوي أبعاد منتهية، فإن:
* إذا كان \\(\text{dim}(V) < \text{dim}(W)\\)، فإن \\(T\\) لا يمكن أن يكون انطباقيًا. (بواسطة نظرية الرتبة-البطل، \\(\text{dim}(\text{im}(T)) \leq \text{dim}(V) < \text{dim}(W)\\)).
* إذا كان \\(\text{dim}(V) > \text{dim}(W)\\)، فإن \\(T\\) لا يمكن أن يكون حقنيًا (لأن \\(\text{dim}(\text{ker}(T)) = \text{dim}(V) - \text{dim}(\text{im}(T)) \geq \text{dim}(V) - \text{dim}(W) > 0\\)، لذا النواة ليست فقط المتجه الصفري).
* إذا كان \\(\text{dim}(V) = \text{dim}(W)\\)، فإن \\(T\\) حقني إذا وفقط إذا كان انطباقيًا. (إذا كان \\(T\\) حقنيًا، \\(\text{dim}(\text{ker}(T)) = 0\\)، لذا \\(\text{dim}(\text{im}(T)) = \text{dim}(V) = \text{dim}(W)\\)، مما يعني أن \\(\text{im}(T) = W\\)، لذا \\(T\\) انطباقي. وبالعكس، إذا كان \\(T\\) انطباقيًا، \\(\text{dim}(\text{im}(T)) = \text{dim}(W) = \text{dim}(V)\\)، لذا \\(\text{dim}(\text{ker}(T)) = 0\\)، مما يعني أن \\(T\\) حقني).

**مثال: التحقق من الانطباقية**

بالنسبة للتحويل \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) المعرف بالعلاقة \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)، وجدنا أن \\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\\}\\). بعد الصورة (رتبة \\(T\\)) هو 2، لأن المتجهين الممتدين مستقلين خطيًا. بعد المجال هو \\(\text{dim}(\mathbb{R}^2) = 2\\). بواسطة نظرية الرتبة-البطل، \\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = 2\\)، لذا \\(\text{dim}(\text{ker}(T)) + 2 = 2\\)، مما يعطي \\(\text{dim}(\text{ker}(T)) = 0\\)، متسق مع ما وجدناه سابقًا.

بما أن بعد الصورة (2) أقل من بعد المجال المقابل (3)، فإن الصورة هي فضاء جزئي حقيقي من المجال المقابل، وبالتالي التحويل ليس انطباقيًا. هناك متجهات في \\(\mathbb{R}^3\\) ليست في صورة \\(T\\). على سبيل المثال، \\(\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\\) لا يمكن التعبير عنه كتركيب خطي لـ \\(\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\) و \\(\begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\).

**التشاكل الخطي**

التحويل الخطي \\(T: V \rightarrow W\\) يسمى **تشاكل خطي** إذا كان حقنيًا وانطباقيًا معًا. إذا وجد تشاكل خطي بين فضاءين متجهين \\(V\\) و \\(W\\)، فإن \\(V\\) و \\(W\\) يقال إنهما **متماثلان تركيبياً**، ويرمز له بـ \\(V \cong W\\). الفضاءات المتجهة المتماثلة تركيبياً لها نفس البنية الجبرية بشكل أساسي.

للأفضية المتجهة ذات الأبعاد المنتهية، يكون فضائان متجهان متماثلان تركيبياً إذا وفقط إذا كان لهما نفس البعد. إذا كان \\(\text{dim}(V) = \text{dim}(W) = n\\)، فإن التحويل الخطي \\(T: V \rightarrow W\\) هو تشاكل خطي إذا وفقط إذا كان إما حقنيًا أو انطباقيًا.

**ملخص للمفاهيم الرئيسية:**

* **التحويل الخطي:** دالة بين فضاءين متجهين تحافظ على جمع المتجهات والضرب القياسي.
* **التمثيل المصفوفي:** طريقة لتمثيل تحويل خطي بين فضاءين متجهين ذوي أبعاد منتهية كمصفوفة.
* **النواة (الفضاء الفراغي):** مجموعة المتجهات في المجال التي تتحول إلى المتجه الصفري في المجال المقابل. وهي فضاء جزئي من المجال.
* **الصورة (المدى):** مجموعة المتجهات في المجال المقابل التي هي صورة لمتجه ما في المجال. وهي فضاء جزئي من المجال المقابل.
* **الحقنية (واحد لواحد):** التحويل الخطي حقني إذا وفقط إذا كانت نواته هي الفضاء الجزئي الصفري.
* **الانطباقية (شامل):** التحويل الخطي انطباقي إذا وفقط إذا كانت صورته تساوي المجال المقابل.
* **نظرية الرتبة-البطل:** للتحويل الخطي \\(T: V \rightarrow W\\) مع \\(V\\) ذي أبعاد منتهية، \\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\).
* **التشاكل الخطي:** تحويل خطي يكون حقنيًا وانطباقيًا معًا.

يجب أن يوفر هذا البرنامج التعليمي المفصل أساسًا متينًا لفهم التحويلات الخطية