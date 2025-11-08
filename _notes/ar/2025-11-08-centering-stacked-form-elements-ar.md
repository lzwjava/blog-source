---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: محاذاة عناصر النماذج المتراصة باستخدام Flexbox
translated: true
type: note
---

```css
.sort-container {
    display: flex;
    flex-direction: column; /* إضافة هذه الخاصية لترتيب العناصر عمودياً */
    align-items: center; /* توسيط العناصر أفقياً في العمود */
    justify-content: center; /* توسيط العمود بشكل عمودي */
    gap: 10px;
    margin-bottom: 1rem;
}

.sort-container select {
    padding: 5px;
    font-size: 16px;
}

.sort-container .post-number {
    font-size: 16px;
}
```

### الشرح
- **flex-direction: column**: يغير المحور الرئيسي من أفقي (صف) إلى عمودي، مما يرتبب عناصر `select` و `.post-number` من الأعلى إلى الأسفل.
- **align-items: center**: يحافظ على التوسيط الأفقي للعناصر الفرعية.
- **justify-content: center**: يوسّط المكدس العمودي بأكمله داخل الحاوية.
- كما أنني أصلحت بناء جملة محددات المتداخلة (نقلت `select` و `.post-number` خارج الكتلة الرئيسية لممارسة أفضل، بافتراض أنها عناصر فرعية مباشرة - اضبطها حسب الحاجة). الخاصية `gap` تطبق الآن عمودياً بين العناصر.