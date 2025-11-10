---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: برنامج تعليمي للرسوم البيانية باستخدام NetworkX و Matplotlib
translated: true
type: note
---

### تثبيت المكتبات
لاستخدام NetworkX و Matplotlib لرسم المخططات، قم بتثبيتهما إذا لزم الأمر:
- NetworkX: تتعامل مع إنشاء المخططات ومعالجتها.
- Matplotlib: توفر إمكانيات الرسم.

التثبيت عبر pip:
```bash
pip install networkx matplotlib
```

للتقديم الأسرع، يوصي Matplotlib بتثبيت NumPy (`pip install numpy`).

### الإعداد الأساسي والمثال
1. **استيراد المكتبات**:  
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt
   ```

2. **إنشاء مخطط**:  
   استخدم NetworkX لبناء مخطط غير موجه بسيط (يمكنك التخصيص باستخدام المخططات الموجهة، الحواف الموزونة، إلخ):
   ```python
   G = nx.Graph()  # إنشاء مخطط فارغ
   G.add_nodes_from([1, 2, 3, 4, 5])  # إضافة عُقد (مثلاً، 5 عُقد)
   G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])  # إضافة حواف (اتصالات)
   ```

3. **رسم وعرض المخطط**:  
   استخدم الواجهة الخلفية لـ Matplotlib للتصور:
   ```python
   nx.draw(G, with_labels=True)  # رسم المخطط مع تسميات العُقد
   plt.show()  # عرض الرسم
   ```

هذا ينتج تخطيطاً دائرياً أساسياً للمخطط (دورة ذات 5 عُقد).

### التخصيصات المتقدمة
- **التخطيطات**: التحكم في مواقع العُقد (مثل التخطيط العشوائي، تخطيط الزنبرك):
  ```python
  pos = nx.spring_layout(G)  # تخطيط موجه بالقوى للشبكات الواقعية
  nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')
  plt.title("رسم بياني للشبكة")
  plt.show()
  ```
- **أنماط العُقد والحواف**: تخصيص المظهر:
  ```python
  nx.draw(G, pos=pos, node_size=500, node_color='red', edge_width=2, font_size=10)
  ```
- **المخططات الموجهة**: للعلاقات الهرمية، استخدم `nx.DiGraph`.
  ```python
  DG = nx.DiGraph()
  DG.add_edges_from([('A', 'B'), ('B', 'C')])
  nx.draw(DG, with_labels=True, arrows=True)
  plt.show()
  ```
- **حفظ المخطط**: التصدير إلى ملف بدلاً من العرض:
  ```python
  plt.savefig('diagram.png')
  ```

### نصائح وموارد
- وثائق NetworkX (networkx.org) لأنواع المخططات مثل الأشجار أو الشبكات.
- وثائق Matplotlib (matplotlib.org) للتضمين في واجهات المستخدم الرسومية أو الرسوم الفرعية.
- للمخططات الكبيرة (أكثر من 100 عقدة)، استخدم `nx.draw_networkx` أو أدوات خارجية مثل Graphviz لأداء أفضل.
- جرب في دفتر Jupyter notebook للرسم التفاعلي. إذا ظهرت مشاكل، فإن الأخطاء الشائعة تنبع من الواجهات الخلفية المفقودة (قم بتثبيتها عبر `pip install pyqt5` أو ما شابه للنوافذ التفاعلية).