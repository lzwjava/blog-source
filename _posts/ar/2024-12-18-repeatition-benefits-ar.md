---
audio: false
generated: false
lang: ar
layout: post
title: فوائد التكرار في البرمجة
translated: true
---

```bash
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:"$HOME/Library/Python/3.9/bin":/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin
```

في هذه الحالة، تجنب استخدام المتغير:

`"$HOME/Library/Python/3.9/bin"`

```bash
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin
```

النسخة الثانية تبدو متكررة بعض الشيء مع ظهور دليل `/Users/lzwjava` عدة مرات، لكنها أكثر نظافة وأسهل في القراءة.

التكرار في البرمجة يمكن أن يكون مفيدًا في الواقع. لا نحتاج دائمًا إلى تجريد أو تبسيط كل شيء باستخدام المتغيرات أو الدوال. في هذه الحالة، من غير المرجح أن يتغير دليل المنزل `/Users/lzwjava` بشكل متكرر، لذا من المقبول تمامًا تكراره.

هذا مشابه لكيفية الإشارة إلى أسماء الأشخاص: إذا استخدمنا الضمائر مثل "هو"، "هي"، أو "هم" بشكل مفرط، يصبح من غير الواضح عمن نتحدث. الأسماء نفسها من غير المرجح أن تتغير، واستخدامها مباشرة يمكن أن يضيف وضوحًا.

التجريد والتبسيط مهمان، ولكن في بعض الحالات، قد يقدمان تعقيدًا غير ضروري. في بعض الأحيان، يكون التكرار أبسط وأكثر قابلية للفهم.