---
audio: false
generated: true
lang: hi
layout: post
title: लीनियर ट्रांसफॉर्मेशन - जेमिनी
translated: true
type: note
---

ठीक है, आइए रैखिक परिवर्तनों पर एक विस्तृत ट्यूटोरियल में गोता लगाएँ, जिसमें परिभाषा, उदाहरण, मैट्रिक्स निरूपण, कर्नेल, इमेज और इंजेक्टिविटी तथा सर्जेक्टिविटी जैसे गुण शामिल हैं। यह रैखिक बीजगणित का एक मौलिक विषय है।

## 6. रैखिक परिवर्तन: एक विस्तृत ट्यूटोरियल

एक **रैखिक परिवर्तन** दो सदिश समष्टियों के बीच एक फलन है जो सदिश योग और अदिश गुणन की संक्रियाओं को संरक्षित करता है। मान लीजिए \\(V\\) और \\(W\\) समान क्षेत्र \\(F\\) (जो अक्सर वास्तविक संख्याओं \\(\mathbb{R}\\) या सम्मिश्र संख्याओं \\(\mathbb{C}\\) का समुच्चय होता है) पर सदिश समष्टियाँ हैं।

**परिभाषा:** एक फलन \\(T: V \rightarrow W\\) एक रैखिक परिवर्तन है यदि यह सभी सदिशों \\(\mathbf{u}, \mathbf{v} \in V\\) और सभी अदिशों \\(c \in F\\) के लिए निम्नलिखित दो गुणों को संतुष्ट करता है:

1.  **योगात्मकता:** \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})\\)
2.  **समघातता (अदिश गुणन):** \\(T(c\mathbf{u}) = cT(\mathbf{u})\\)

इन दोनों गुणों को एक ही शर्त में संयोजित किया जा सकता है:
\\(T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})\\) सभी \\(\mathbf{u}, \mathbf{v} \in V\\) और सभी अदिशों \\(c, d \in F\\) के लिए।

**रैखिकता के मुख्य परिणाम:**

* \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), जहाँ \\(\mathbf{0}_V\\), \\(V\\) में शून्य सदिश है और \\(\mathbf{0}_W\\), \\(W\\) में शून्य सदिश है। (सिद्धांत: \\(T(\mathbf{0}_V) = T(0\mathbf{u}) = 0T(\mathbf{u}) = \mathbf{0}_W\\) किसी भी \\(\mathbf{u} \in V\\) के लिए)।
* \\(T(-\mathbf{u}) = -T(\mathbf{u})\\)। (सिद्धांत: \\(T(-\mathbf{u}) = T((-1)\mathbf{u}) = (-1)T(\mathbf{u}) = -T(\mathbf{u})\\))।

### रैखिक परिवर्तनों के उदाहरण

आइए अवधारणा को बेहतर ढंग से समझने के लिए कुछ उदाहरण देखें।

**उदाहरण 1: \\(\mathbb{R}^2\\) में परिवर्तन (घूर्णन)**

एक परिवर्तन \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) पर विचार करें जो \\(\mathbb{R}^2\\) में प्रत्येक सदिश को कोण \\(\theta\\) द्वारा वामावर्त घुमाता है। यदि \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\), तो \\(T(\mathbf{v}) = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}\\)।

आइए जाँचें कि क्या यह एक रैखिक परिवर्तन है। मान लीजिए \\(\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}\\) और \\(\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\\), और मान लीजिए \\(c\\) एक अदिश है।

* **योगात्मकता:**
    \\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2)\cos\theta - (y_1 + y_2)\sin\theta \\ (x_1 + x_2)\sin\theta + (y_1 + y_2)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} (x_1\cos\theta - y_1\sin\theta) + (x_2\cos\theta - y_2\sin\theta) \\ (x_1\sin\theta + y_1\cos\theta) + (x_2\sin\theta + y_2\cos\theta) \end{pmatrix} = T(\mathbf{u}) + T(\mathbf{v})\\)

* **समघातता:**
    \\(T(c\mathbf{u}) = T\left(\begin{pmatrix} cx_1 \\ cy_1 \end{pmatrix}\right) = \begin{pmatrix} (cx_1)\cos\theta - (cy_1)\sin\theta \\ (cx_1)\sin\theta + (cy_1)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} c(x_1\cos\theta - y_1\sin\theta) \\ c(x_1\sin\theta + y_1\cos\theta) \end{pmatrix} = c \begin{pmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \end{pmatrix} = cT(\mathbf{u})\\)

अतः, घूर्णन एक रैखिक परिवर्तन है।

**उदाहरण 2: \\(\mathbb{R}^2\\) में परिवर्तन (x-अक्ष पर प्रक्षेपण)**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) पर विचार करें जिसे \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x \\ 0 \end{pmatrix}\\) द्वारा परिभाषित किया गया है। यह परिवर्तन प्रत्येक सदिश को x-अक्ष पर प्रक्षेपित करता है। आप परिभाषा का उपयोग करके सत्यापित कर सकते हैं कि यह भी एक रैखिक परिवर्तन है।

**उदाहरण 3: \\(\mathbb{R}^2\\) में परिवर्तन (स्थानांतरण)**

\\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) पर विचार करें जिसे \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + a \\ y + b \end{pmatrix}\\) द्वारा परिभाषित किया गया है, जहाँ \\(a\\) और \\(b\\) स्थिरांक हैं (दोनों शून्य नहीं)।

पहले गुण की जाँच करते हैं:
\\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2) + a \\ (y_1 + y_2) + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)

यह सही लगता है, आइए फिर से जाँच करें।
\\(T(\mathbf{u} + \mathbf{v}) = \begin{pmatrix} x_1 + x_2 + a \\ y_1 + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + x_2 + 2a \\ y_1 + y_2 + 2b \end{pmatrix}\\)

यदि \\(a \neq 0\\) या \\(b \neq 0\\), तो \\(T(\mathbf{u} + \mathbf{v}) \neq T(\mathbf{u}) + T(\mathbf{v})\\)। साथ ही, \\(T(\mathbf{0}) = T\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} a \\ b \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}\\) यदि \\(a\\) या \\(b\\) अशून्य है। इसलिए, स्थानांतरण आम तौर पर **नहीं** एक रैखिक परिवर्तन है।

**उदाहरण 4: एक मैट्रिक्स द्वारा परिभाषित \\(\mathbb{R}^n\\) से \\(\mathbb{R}^m\\) में परिवर्तन**

मान लीजिए \\(A\\) एक \\(m \times n\\) मैट्रिक्स है। परिवर्तन \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) जिसे \\(T(\mathbf{x}) = A\mathbf{x}\\) द्वारा परिभाषित किया गया है (जहाँ \\(\mathbf{x}\\) एक \\(n \times 1\\) कॉलम वेक्टर है) एक रैखिक परिवर्तन है। ऐसा इसलिए है क्योंकि मैट्रिक्स गुणन योगात्मकता और समघातता के गुणों को संतुष्ट करता है:
\\(A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}\\)
\\(A(c\mathbf{u}) = c(A\mathbf{u})\\)

**उदाहरण 5: बहुपदों का अवकलन**

मान लीजिए \\(P_n\\), अधिकतम घात \\(n\\) वाले बहुपदों की सदिश समष्टि है। परिवर्तन \\(D: P_n \rightarrow P_{n-1}\\) जिसे \\(D(p(x)) = p'(x)\\) (\\(p(x)\\) का अवकलज) द्वारा परिभाषित किया गया है, एक रैखिक परिवर्तन है।
यदि \\(p(x)\\) और \\(q(x)\\) बहुपद हैं और \\(c\\) एक अदिश है:
\\(D(p(x) + q(x)) = (p(x) + q(x))' = p'(x) + q'(x) = D(p(x)) + D(q(x))\\)
\\(D(cp(x)) = (cp(x))' = cp'(x) = cD(p(x))\\)

**उदाहरण 6: फलनों का समाकलन**

मान लीजिए \\(C[a, b]\\), अंतराल \\([a, b]\\) पर सतत फलनों की सदिश समष्टि है। परिवर्तन \\(I: C[a, b] \rightarrow \mathbb{R}\\) जिसे \\(I(f) = \int_a^b f(x) dx\\) द्वारा परिभाषित किया गया है, एक रैखिक परिवर्तन है।
\\(I(f + g) = \int_a^b (f(x) + g(x)) dx = \int_a^b f(x) dx + \int_a^b g(x) dx = I(f) + I(g)\\)
\\(I(cf) = \int_a^b cf(x) dx = c \int_a^b f(x) dx = cI(f)\\)

### एक रैखिक परिवर्तन का मैट्रिक्स निरूपण

रैखिक बीजगणित में एक मौलिक परिणाम यह है कि परिमित-विमीय सदिश समष्टियों के बीच किसी भी रैखिक परिवर्तन को एक मैट्रिक्स द्वारा दर्शाया जा सकता है।

मान लीजिए \\(V\\) एक \\(n\\)-विमीय सदिश समष्टि है जिसका आधार \\(\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) है और \\(W\\) एक \\(m\\)-विमीय सदिश समष्टि है जिसका आधार \\(\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, ..., \mathbf{c}_m\}\\) है। मान लीजिए \\(T: V \rightarrow W\\) एक रैखिक परिवर्तन है।

\\(T\\) के आधार \\(\mathcal{B}\\) और \\(\mathcal{C}\\) के संबंध में मैट्रिक्स निरूपण (जिसे \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) या केवल \\([T]\\) दर्शाया जाता है जब आधार समझ में आते हैं) ज्ञात करने के लिए, हमें \\(V\\) के आधार सदिशों के \\(T\\) के अंतर्गत प्रतिबिंबों को निर्धारित करने और इन प्रतिबिंबों को \\(W\\) के आधार सदिशों के रैखिक संयोजन के रूप में व्यक्त करने की आवश्यकता है।

प्रत्येक \\(\mathbf{b}_j \in \mathcal{B}\\) के लिए, \\(T(\mathbf{b}_j)\\), \\(W\\) में एक सदिश है, इसलिए इसे \\(\mathcal{C}\\) में आधार सदिशों के रैखिक संयोजन के रूप में विशिष्ट रूप से लिखा जा सकता है:
\\(T(\mathbf{b}_j) = a_{1j}\mathbf{c}_1 + a_{2j}\mathbf{c}_2 + ... + a_{mj}\mathbf{c}_m = \sum_{i=1}^{m} a_{ij}\mathbf{c}_i\\)

इस रैखिक संयोजन के गुणांक मैट्रिक्स निरूपण \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) के \\(j\\)-वें कॉलम का निर्माण करते हैं:
$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$

यदि \\(\mathbf{v} \in V\\) का आधार \\(\mathcal{B}\\) के संबंध में निर्देशांक सदिश \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}\\) है, तो आधार \\(\mathcal{C}\\) के संबंध में \\(T(\mathbf{v})\\) का निर्देशांक सदिश, जिसे \\([T(\mathbf{v})]_{\mathcal{C}}\\) दर्शाया जाता है, मैट्रिक्स गुणनफल द्वारा दिया जाता है:
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}}\\)

**उदाहरण: मैट्रिक्स निरूपण**

मान लीजिए \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) एक रैखिक परिवर्तन है जिसे \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) द्वारा परिभाषित किया गया है। मान लीजिए \\(\mathbb{R}^2\\) और \\(\mathbb{R}^3\\) के मानक आधार क्रमशः \\(\mathcal{B} = \{\mathbf{e}_1, \mathbf{e}_2\} = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}\\) और \\(\mathcal{C} = \{\mathbf{f}_1, \mathbf{f}_2, \mathbf{f}_3\} = \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}\\) हैं।

हम \\(T\\) के अंतर्गत \\(\mathbb{R}^2\\) के आधार सदिशों के प्रतिबिंब ज्ञात करते हैं:
\\(T(\mathbf{e}_1) = T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 + 0 \\ 2(1) - 0 \\ 3(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} = 1\mathbf{f}_1 + 2\mathbf{f}_2 + 0\mathbf{f}_3\\)
\\(T(\mathbf{e}_2) = T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0 + 1 \\ 2(0) - 1 \\ 3(1) \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = 1\mathbf{f}_1 - 1\mathbf{f}_2 + 3\mathbf{f}_3\\)

मानक आधारों के संबंध में \\(T\\) का मैट्रिक्स निरूपण है:
\\([T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix}\\)

अब, आइए \\(\mathbb{R}^2\\) में एक मनमाना सदिश \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\) लें। \\(\mathcal{B}\\) के संबंध में इसका निर्देशांक सदिश \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x \\ y \end{pmatrix}\\) है।
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)
\\(\mathcal{C}\\) के संबंध में निर्देशांक सदिश वास्तव में \\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) है, जो हमारे द्वारा पहले परिभाषित सदिश \\(T(\mathbf{v})\\) के अनुरूप है।

### एक रैखिक परिवर्तन का कर्नेल (नल समष्टि)

एक रैखिक परिवर्तन \\(T: V \rightarrow W\\) का **कर्नेल** (या नल समष्टि), जिसे \\(\text{ker}(T)\\) या \\(N(T)\\) द्वारा दर्शाया जाता है, प्रांत \\(V\\) में उन सभी सदिशों का समुच्चय है जिन्हें सह-प्रांत \\(W\\) में शून्य सदिश पर प्रतिबिंबित किया जाता है:
\\(\text{ker}(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}\\)

**कर्नेल के गुण:**

* एक रैखिक परिवर्तन का कर्नेल हमेशा प्रांत \\(V\\) का एक उप-समष्टि होता है।
    * **शून्य सदिश समाहित करता है:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), इसलिए \\(\mathbf{0}_V \in \text{ker}(T)\\)।
    * **योग के अंतर्गत संवृत:** यदि \\(\mathbf{u}, \mathbf{v} \in \text{ker}(T)\\), तो \\(T(\mathbf{u}) = \mathbf{0}_W\\) और \\(T(\mathbf{v}) = \mathbf{0}_W\\)। इस प्रकार, \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W\\), इसलिए \\(\mathbf{u} + \mathbf{v} \in \text{ker}(T)\\)।
    * **अदिश गुणन के अंतर्गत संवृत:** यदि \\(\mathbf{u} \in \text{ker}(T)\\) और \\(c\\) एक अदिश है, तो \\(T(c\mathbf{u}) = cT(\mathbf{u}) = c\mathbf{0}_W = \mathbf{0}_W\\), इसलिए \\(c\mathbf{u} \in \text{ker}(T)\\)।

**उदाहरण: कर्नेल ज्ञात करना**

रैखिक परिवर्तन \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) पर विचार करें जिसे \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) द्वारा परिभाषित किया गया है।
कर्नेल ज्ञात करने के लिए, हमें \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\) को हल करने की आवश्यकता है:
\\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\)

यह रैखिक समीकरणों की निम्नलिखित प्रणाली देता है:
\\(x + y = 0\\)
\\(2x - y = 0\\)
\\(3y = 0\\)

तीसरे समीकरण से, \\(y = 0\\)। इसे पहले समीकरण में प्रतिस्थापित करने पर, \\(x + 0 = 0\\), इसलिए \\(x = 0\\)। दूसरा समीकरण भी संतुष्ट होता है: \\(2(0) - 0 = 0\\)।
एकमात्र हल \\(x = 0\\) और \\(y = 0\\) है। इसलिए, \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\), जो \\(\mathbb{R}^2\\) का शून्य उप-समष्टि है।

### एक रैखिक परिवर्तन का इमेज (परिसर)

एक रैखिक परिवर्तन \\(T: V \rightarrow W\\) का **इमेज** (या परिसर), जिसे \\(\text{im}(T)\\) या \\(R(T)\\) द्वारा दर्शाया जाता है, सह-प्रांत \\(W\\) में उन सभी सदिशों का समुच्चय है जो प्रांत \\(V\\) में किसी सदिश के प्रतिबिंब हैं:
\\(\text{im}(T) = \{\mathbf{w} \in W \mid \mathbf{w} = T(\mathbf{v}) \text{ किसी } \mathbf{v} \in V \text{ के लिए }\}\\)

**इमेज के गुण:**

* एक रैखिक परिवर्तन का इमेज हमेशा सह-प्रांत \\(W\\) का एक उप-समष्टि होता है।
    * **शून्य सदिश समाहित करता है:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), इसलिए \\(\mathbf{0}_W \in \text{im}(T)\\)।
    * **योग के अंतर्गत संवृत:** यदि \\(\mathbf{w}_1, \mathbf{w}_2 \in \text{im}(T)\\), तो ऐसे \\(\mathbf{v}_1, \mathbf{v}_2 \in V\\) मौजूद हैं कि \\(T(\mathbf{v}_1) = \mathbf{w}_1\\) और \\(T(\mathbf{v}_2) = \mathbf{w}_2\\)। तब \\(\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{v}_1) + T(\mathbf{v}_2) = T(\mathbf{v}_1 + \mathbf{v}_2)\\)। चूँकि \\(\mathbf{v}_1 + \mathbf{v}_2 \in V\\), \\(\mathbf{w}_1 + \mathbf{w}_2 \in \text{im}(T)\\)।
    * **अदिश गुणन के अंतर्गत संवृत:** यदि \\(\mathbf{w} \in \text{im}(T)\\) और \\(c\\) एक अदिश है, तो ऐसा \\(\mathbf{v} \in V\\) मौजूद है कि \\(T(\mathbf{v}) = \mathbf{w}\\)। तब \\(c\mathbf{w} = cT(\mathbf{v}) = T(c\mathbf{v})\\)। चूँकि \\(c\mathbf{v} \in V\\), \\(c\mathbf{w} \in \text{im}(T)\\)।

* यदि \\(V\\) एक आधार \\(\{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) के साथ परिमित-विमीय है, तो \\(T\\) का इमेज आधार सदिशों के प्रतिबिंबों का अवधान है:
    \\(\text{im}(T) = \text{span}\{T(\mathbf{b}_1), T(\mathbf{b}_2), ..., T(\mathbf{b}_n)\}\\)

**उदाहरण: इमेज ज्ञात करना**

रैखिक परिवर्तन \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) पर विचार करें जिसे \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) द्वारा परिभाषित किया गया है।
\\(\mathbb{R}^2\\) के मानक आधार, \\(\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\}\\) का उपयोग करते हुए, हमारे पास है:
\\(T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\)
\\(T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\)

\\(T\\) का इमेज इन दोनों सदिशों का अवधान है:
\\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\)
यह \\(\mathbb{R}^3\\) का एक उप-समष्टि है। चूँकि ये दोनों सदिश रैखिक रूप से स्वतंत्र हैं (एक दूसरे का अदिश गुणज नहीं है), इमेज \\(\mathbb{R}^3\\) में मूल बिंदु से गुजरने वाला एक तल है।

**मैट्रिक्स निरूपण और इमेज के बीच संबंध:**

यदि \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) को \\(T(\mathbf{x}) = A\mathbf{x}\\) द्वारा दिया जाता है, जहाँ \\(A\\) एक \\(m \times n\\) मैट्रिक्स है, तो \\(T\\) का इमेज मैट्रिक्स \\(A\\) का कॉलम समष्टि है, अर्थात, \\(A\\) के कॉलमों का अवधान।

### रैखिक परिवर्तनों के गुण: इंजेक्टिविटी और सर्जेक्टिविटी

**इंजेक्टिविटी (एकैकी)**

एक रैखिक परिवर्तन \\(T: V \rightarrow W\\) **इंजेक्टिव** (या एकैकी) है यदि प्रत्येक \\(\mathbf{w} \in W\\) के लिए, अधिकतम एक \\(\mathbf{v} \in V\\) मौजूद है जैसे कि \\(T(\mathbf{v}) = \mathbf{w}\\)। समतुल्य रूप से, यदि \\(T(\mathbf{u}) = T(\mathbf{v})\\), तो \\(\mathbf{u} = \mathbf{v}\\)।

**प्रमेय:** एक रैखिक परिवर्तन \\(T: V \rightarrow W\\) इंजेक्टिव है यदि और केवल यदि इसका कर्नेल शून्य उप-समष्टि है, अर्थात, \\(\text{ker}(T) = \{\mathbf{0}_V\}\\)।

**सिद्धांत:**
* **(\\(\Rightarrow\\)) मान लीजिए \\(T\\) इंजेक्टिव है।** यदि \\(\mathbf{v} \in \text{ker}(T)\\), तो \\(T(\mathbf{v}) = \mathbf{0}_W\\)। हम यह भी जानते हैं कि \\(T(\mathbf{0}_V) = \mathbf{0}_W\\)। चूँकि \\(T\\) इंजेक्टिव है और \\(T(\mathbf{v}) = T(\mathbf{0}_V)\\), यह अवश्य होना चाहिए कि \\(\mathbf{v} = \mathbf{0}_V\\)। इस प्रकार, \\(\text{ker}(T) = \{\mathbf{0}_V\}\\)।
* **(\\(\Leftarrow\\)) मान लीजिए \\(\text{ker}(T) = \{\mathbf{0}_V\}\\)।** मान लीजिए कुछ \\(\mathbf{u}, \mathbf{v} \in V\\) के लिए \\(T(\mathbf{u}) = T(\mathbf{v})\\) है। तब \\(T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{0}_W\\)। रैखिकता द्वारा, \\(T(\mathbf{u} - \mathbf{v}) = \mathbf{0}_W\\)। इसका अर्थ है कि \\(\mathbf{u} - \mathbf{v} \in \text{ker}(T)\\)। चूँकि \\(\text{ker}(T) = \{\mathbf{0}_V\}\\), हमारे पास \\(\mathbf{u} - \mathbf{v} = \mathbf{0}_V\\) है, जिसका अर्थ है \\(\mathbf{u} = \mathbf{v}\\)। इसलिए, \\(T\\) इंजेक्टिव है।

**उदाहरण: इंजेक्टिविटी की जाँच करना**

परिवर्तन \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) के लिए जिसे \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) द्वारा परिभाषित किया गया है, हमने पाया कि \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\)। इसलिए, यह परिवर्तन इंजेक्टिव है।

**सर्जेक्टिविटी (आच्छादक)**

एक रैखिक परिवर्तन \\(T: V \rightarrow W\\) **सर्जेक्टिव** (या आच्छादक) है यदि प्रत्येक \\(\mathbf{w} \in W\\) के लिए, कम से कम एक \\(\mathbf{v} \in V\\) मौजूद है जैसे कि \\(T(\mathbf{v}) = \mathbf{w}\\)। दूसरे शब्दों में, \\(T\\) का इमेज सह-प्रांत \\(W\\) के बराबर है, अर्थात, \\(\text{im}(T) = W\\)।

**प्रमेय (रैंक-शून्य