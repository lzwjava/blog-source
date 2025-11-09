---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ar
layout: post
title: اختيار النموذج الأمثل للتكلفة والأداء
translated: true
type: note
---

بالنظر إلى إعدادات Claude Code الخاصة بك، أنت تريد التحسين من حيث التكلفة والأداء معًا. إليك بعض التوصيات لاختيار النماذج "الرخيصة والقوية" في إعداد جهاز التوجيه الخاص بك:

## أفضل النماذج من حيث التكلفة/الأداء من قائمتك:

**لمعظم المهام (الافتراضي):**
- `deepseek/deepseek-chat-v3.1` - أداء ممتاز بتكلفة منخفضة جدًا
- `deepseek/deepseek-r1` - قدرات استثنائية في التفكير، ولا تزال فعالة من حيث التكلفة

**للمهام الخلفية:**
- `deepseek/deepseek-chat-v3.1` - خيار جيد بالفعل
- `google/gemini-2.5-flash` - سريع وغير مكلف

**للتفكير/الاستدلال:**
- `deepseek/deepseek-r1` - مصمم خصيصًا لمهام التفكير
- `z-ai/glm-4.5` - خيارك الحالي جيد

**اقتراح جهاز التوجيه المحدث:**
```json
"Router": {
  "default": "openrouter,deepseek/deepseek-chat-v3.1",
  "background": "openrouter,google/gemini-2.5-flash", 
  "think": "openrouter,deepseek/deepseek-r1",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "webSearch": "openrouter,google/gemini-2.5-flash"
}
```

## الاعتبارات الرئيسية:
- **نماذج DeepSeek** تقدم أفضل نسبة سعر/أداء حاليًا
- **Gemini 2.5 Flash** سريع جدًا ورخيص للمهام الأبسط
- احتفظ بـ **Kimi** للسياق الطويل حيث يتعامل جيدًا مع 200 ألف+ رمز
- **Gemini 2.5 Pro** إذا كنت تحتاج إلى قدرات أكثر من Flash

يمكنك التحقق من الأسعار الحالية على موقع OpenRouter لمقارنة التكاليف الدقيقة، ولكن نماذج DeepSeek عادةً ما تكون أرخص بـ 10-20 مرة من نماذج مستوى GPT-4 مع تقديم أداء تنافسي.