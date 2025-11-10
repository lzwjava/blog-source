---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت إكسِيلاتيكْس
translated: true
type: note
---

لتركيب XeLaTeX على أوبونتو 24.04 أو 22.04، اتبع الخطوات التالية:

1.  **تحديث قائمة الحزم**:
    ```bash
    sudo apt update
    ```

2.  **تركيب TeX Live (والذي يتضمن XeLaTeX)**:
    *   للتركيب الكامل (موصى به لمعظم المستخدمين، يتضمن XeLaTeX والعديد من الحزم):
        ```bash
        sudo apt install texlive-xetex
        ```
    *   إذا كنت تريد تركيبًا أساسيًا، يمكنك تركيب `texlive` بدلاً من ذلك، لكن `texlive-xetex` هو الخيار المفضل للحصول على دعم XeLaTeX.

3.  **التحقق من التركيب**:
    قم بتشغيل الأمر التالي للتحقق مما إذا كان XeLaTeX مثبتًا:
    ```bash
    xelatex --version
    ```
    يجب أن ترى نتيجة مشابهة لـ `XeTeX 3.14159265-2.6-0.999991` (قد تختلف أرقام الإصدار).

4.  **اختياري: تركيب خطوط إضافية** (إذا كنت بحاجة إلى خطوط محددة لـ XeLaTeX):
    ```bash
    sudo apt install texlive-fonts-extra
    ```

5.  **اختبار XeLaTeX**:
    أنشئ ملف `.tex` بسيطًا، على سبيل المثال `test.tex`:
    ```latex
    \documentclass{article}
    \usepackage{fontspec}
    \setmainfont{Liberation Serif}
    \begin{document}
    Hello, XeLaTeX!
    \end{document}
    ```
    وقم بتحويله باستخدام:
    ```bash
    xelatex test.tex
    ```
    هذا من المفترض أن ينتج ملف `test.pdf`.

**ملاحظات**:
*   حزمة `texlive-xetex` متاحة في مستودعات أوبونتو 22.04 و 24.04.
*   إذا كنت بحاجة إلى أحدث إصدار من TeX Live، يمكنك تثبيته يدويًا من موقع TeX Live الإلكتروني، لكن حزمة أوبونتو عادةً ما تكون كافية.
*   تأكد من وجود مساحة تخزين كافية على القرص (~1-2 جيجابايت لـ `texlive-xetex`، وأكثر لـ `texlive-full`).
*   إذا واجهت مشاكل، تحقق من التبعيات المفقودة باستخدام `sudo apt install -f`.

أعلمني إذا كنت بحاجة إلى مزيد من المساعدة!