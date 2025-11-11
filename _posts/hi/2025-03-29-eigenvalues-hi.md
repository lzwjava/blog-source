---
audio: false
generated: true
lang: hi
layout: post
title: आइगेनमान और आइगेनसदिश
translated: true
type: note
---

निश्चित रूप से! आइए रैखिक बीजगणित में "Eigenvalues और Vectors" से संबंधित मुख्य अवधारणाओं और विषयों को समझते हैं, जो गणित, भौतिकी, इंजीनियरिंग और कंप्यूटर विज्ञान में कई अनुप्रयोगों को समझने के लिए मौलिक हैं।

### 1. Characteristic Polynomial
एक वर्ग मैट्रिक्स \\( A \\) का characteristic polynomial एक बहुपद है जो \\( (A - \lambda I) \\) के सारणिक से बनता है, जहां \\( \lambda \\) एक अदिश राशि है और \\( I \\) तत्समक मैट्रिक्स है। इसे इस प्रकार दिया जाता है:

\\[ p(\lambda) = \det(A - \lambda I) \\]

इस बहुपद के मूल मैट्रिक्स \\( A \\) के eigenvalues होते हैं।

### 2. Eigenvalues
Eigenvalues अदिश मान \\( \lambda \\) होते हैं जो समीकरण \\( Av = \lambda v \\) को संतुष्ट करते हैं, जहां \\( v \\) एक गैर-शून्य सदिश है जिसे eigenvector के रूप में जाना जाता है। Eigenvalues रैखिक परिवर्तनों के व्यवहार, जैसे स्केलिंग और रोटेशन, में अंतर्दृष्टि प्रदान करते हैं।

### 3. Eigenvectors
Eigenvectors गैर-शून्य सदिश \\( v \\) होते हैं जो एक eigenvalue \\( \lambda \\) के संगत होते हैं। वे दिशाएं हैं जो अपरिवर्तित रहती हैं (स्केलिंग को छोड़कर) जब एक रैखिक परिवर्तन लागू किया जाता है।

### 4. Diagonalization
एक वर्ग मैट्रिक्स \\( A \\) विकर्णीय (diagonalizable) होता है यदि इसे \\( A = PDP^{-1} \\) के रूप में लिखा जा सकता है, जहां \\( D \\) एक विकर्ण मैट्रिक्स है और \\( P \\) एक व्युत्क्रमणीय मैट्रिक्स है जिसके कॉलम \\( A \\) के eigenvectors हैं। विकर्णीकरण मैट्रिक्स घातों और अन्य संक्रियाओं की गणना को सरल बनाता है।

### 5. Applications
- **Stability Analysis**: eigenvalues का उपयोग सिस्टम की स्थिरता का विश्लेषण करने के लिए किया जाता है, जैसे कि नियंत्रण सिद्धांत और अवकल समीकरणों में।
- **Markov Processes**: eigenvectors और eigenvalues का उपयोग Markov chains के steady-state वितरण को खोजने के लिए किया जाता है, जो संभाव्यता संक्रमणों वाले सिस्टम को मॉडल करती हैं।

### Example
आइए इन अवधारणाओं को स्पष्ट करने के लिए एक सरल उदाहरण पर विचार करें।

मान लीजिए हमारे पास एक मैट्रिक्स \\( A \\) है:

\\[ A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \\]

हम इसके eigenvalues और eigenvectors ढूंढना चाहते हैं।

#### Step 1: Characteristic Polynomial ज्ञात करें
Characteristic polynomial इस प्रकार दिया गया है:

\\[ \det(A - \lambda I) = \det\begin{pmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{pmatrix} \\]

#### Step 2: सारणिक की गणना करें
\\[ \det\begin{pmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{pmatrix} = (4 - \lambda)(3 - \lambda) - (1)(2) \\]

\\[ = \lambda^2 - 7\lambda + 10 \\]

#### Step 3: Eigenvalues के लिए हल करें
द्विघात समीकरण को हल करें:

\\[ \lambda^2 - 7\lambda + 10 = 0 \\]

Eigenvalues हैं:

\\[ \lambda_1 = 5, \quad \lambda_2 = 2 \\]

#### Step 4: Eigenvectors ज्ञात करें
प्रत्येक eigenvalue के लिए, संगत eigenvectors ज्ञात करने के लिए \\( (A - \lambda I)v = 0 \\) को हल करें।

- \\( \lambda_1 = 5 \\) के लिए:

\\[ A - 5I = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \\]

\\( (A - 5I)v = 0 \\) को हल करने पर, हमें eigenvector \\( v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \\) प्राप्त होता है।

- \\( \lambda_2 = 2 \\) के लिए:

\\[ A - 2I = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \\]

\\( (A - 2I)v = 0 \\) को हल करने पर, हमें eigenvector \\( v_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix} \\) प्राप्त होता है।

### Conclusion
Eigenvalues और eigenvectors रैखिक बीजगणित में शक्तिशाली उपकरण हैं जो जटिल प्रणालियों को समझने और सरल बनाने में मदद करते हैं। इनके विभिन्न क्षेत्रों में व्यापक अनुप्रयोग हैं, जो उन्हें महारत हासिल करने के लिए आवश्यक अवधारणाएं बनाते हैं।