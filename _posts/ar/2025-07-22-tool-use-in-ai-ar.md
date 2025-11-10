---
audio: false
generated: true
lang: ar
layout: post
title: استخدام أدوات الذكاء الاصطناعي في واجهات البرمجة موضَّح
translated: true
type: note
---

### ما هو استخدام الأدوات في واجهات برمجة تطبيقات الذكاء الاصطناعي؟

استخدام الأدوات، الذي يُشار إليه غالبًا باسم "استدعاء الأداة" أو "استدعاء الدالة"، هو ميزة في واجهات برمجة تطبيقات الذكاء الاصطناعي تسمح لنماذج اللغة الكبيرة بالتفاعل مع الأدوات أو الدوال أو واجهات برمجة التطبيقات الخارجية. بدلاً من إنشاء الردود بناءً على معرفتها الداخلية فقط، يمكن للنموذج أن يقرر استدعاء دوال محددة مسبقًا لجلب البيانات في الوقت الفعلي، أو إجراء العمليات الحسابية، أو تنفيذ الإجراءات. وهذا يجعل الذكاء الاصطناعي أكثر ديناميكية وفائدة لمهام مثل الاستعلام عن الطقس، أو البحث في قواعد البيانات، أو التكامل مع الخدمات الأخرى.

تعمل العملية عادة على النحو التالي:
- تقوم بتعريف الأدوات (الدوال) مع الأوصاف والمعلمات بتنسيق JSON.
- يحلل النموذج استعلام المستخدم، وإذا لزم الأمر، يُخرج "استدعاء أداة" مع اسم الدالة والوسائط.
- يقوم تطبيقك بتنفيذ الدالة وإعادة تغذية النتيجة إلى النموذج.
- بعد ذلك، يولد النموذج ردًا نهائيًا يتضمن ناتج الأداة.

هذا مستوحى بشكل شائع من واجهة برمجة تطبيقات استدعاء الدوال من OpenAI، وتدعم العديد من المزودين مثل Mistral و DeepSeek تطبيقات متوافقة.

### Mistral أم DeepSeek لاستخدام الأدوات؟

كلاً من Mistral AI و DeepSeek AI يدعمان استدعاء الأدوات في واجهات برمجة التطبيقات الخاصة بهما، مما يجعلهما مناسبين لبناء الوكلاء أو التطبيقات التي تتطلب تكاملات خارجية. إليك مقارنة سريعة بناءً على المعلومات المتاحة:

- **الدعم لاستخدام الأدوات**:
  - يتبع كلاهما هيكلاً مشابهًا لواجهة برمجة تطبيقات OpenAI، مما يسمح بالتكامل السهل مع الأدوات عبر مخططات JSON.
  - يدعم Mistral هذه الميزة عبر نماذج مثل Mistral Large و Medium، مع خيارات لسير عمل قائمة على الوكلاء.
  - يدعم DeepSeek هذه الميزة بشكل أساسي من خلال نموذجه "deepseek-chat" وهو متوافق بالكامل مع حزمة تطوير برامج OpenAI.

- **الإيجابيات والسلبيات**:
  - **Mistral**: أكثر تنوعًا للمهام العامة، استدلال أسرع في بعض المعايير، وأكثر ملاءمة لاحتياجات خصوصية البيانات الأوروبية. يتفوق في الردود السريعة وله قدرات قوية متعددة اللغات. ومع ذلك، يمكن أن يكون أكثر تكلفة (على سبيل المثال، تكاليف الإدخال/الإخراج أعلى مقارنة بـ DeepSeek).
  - **DeepSeek**: أرخص بشكل ملحوظ (أقل تكلفة بما يصل إلى 28 مرة في بعض المقارنات)، قوي في الرياضيات والبرمجة ومهام التفكير. إنه مثالي للمستخدمين المهتمين بالميزانية أو الاستخدام عالي الحجم. تشمل العيوب الأداء الأبطأ محتملاً في المهام غير التقنية وتركيز أقل على الميزات متعددة الوسائط.
  - **أيهما تختار؟** إذا كانت التكلفة هي الأولوية وحالة الاستخدام الخاصة بك تتضمن برمجة/رياضيات مع أدوات، فاختر DeepSeek. للتطبيقات الأوسع، أو الردود الأسرع، أو ميزات المؤسسات مثل الوكلاء، فإن Mistral أفضل. كلاهما صديق للبرمجيات مفتوحة المصدر ويتمتعان بأداء جيد، ولكن اختبر مع احتياجاتك المحددة.

في النهاية، لا يمكن القول بأن أحدهما "أفضل" بشكل صارم لاستخدام الأدوات — فكلاهما يعمل بشكل جيد. قد يتفوق DeepSeek في توفير التكاليف، بينما تقدم Mistral تكاملات أكثر تطورًا للوكلاء.

### كيفية استخدام خاصية استخدام الأدوات

لاستخدام استدعاء الأدوات، ستحتاج إلى مفتاح واجهة برمجة تطبيقات من المزود المعني (سجل في mistral.ai لـ Mistral أو platform.deepseek.com لـ DeepSeek). يستخدم كلاهما حزم تطوير برامج Python مشابهة لتلك الخاصة بـ OpenAI. فيما يلي أمثلة خطوة بخطوة لأداة استعلام بسيطة عن الطقس.

#### استخدام خاصية استخدام الأدوات مع Mistral AI
تدعم واجهة برمجة تطبيقات Mistral استدعاء الأدوات عبر `MistralClient` في اكمال المحادثة. قم بتثبيت حزمة تطوير البرامج باستخدام `pip install mistralai`.

**كود Python مثال** (معدل من مصادر رسمية ومجتمعية):
```python
from mistralai import Mistral

# تهيئة العميل بمفتاح واجهة برمجة التطبيقات الخاص بك
api_key = "YOUR_MISTRAL_API_KEY"
model = "mistral-large-latest"  # يدعم استدعاء الأدوات
client = Mistral(api_key=api_key)

# تعريف الأدوات (الدوال)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city, e.g., San Francisco"}
                },
                "required": ["location"]
            }
        }
    }
]

# رسالة المستخدم
messages = [{"role": "user", "content": "What's the weather in Hangzhou?"}]

# أول استدعاء لواجهة برمجة التطبيقات: النموذج يقرر ما إذا كانت الأداة مطلوبة
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"  # يقرر تلقائيًا استخدام الأداة
)

# التحقق من وجود استدعاءات أدوات
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    # إضافة رد النموذج إلى الرسائل
    messages.append(response.choices[0].message)
    
    # محاكاة تنفيذ الأداة (في الكود الحقيقي، استدع واجهة برمجة تطبيقات فعلية)
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C and sunny"  # استبدال باستدعاء دالة حقيقي
        
        # إضافة نتيجة الأداة
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": weather_result
        })
    
    # ثاني استدعاء لواجهة برمجة التطبيقات: النموذج يولد الرد النهائي
    final_response = client.chat.complete(model=model, messages=messages)
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)
```

يرسل هذا الكود استعلامًا، يتحقق من استدعاء أداة، ينفذه (محاكى هنا)، ويحصل على الإجابة النهائية. للإعدادات القائمة على الوكلاء، استخدم واجهة برمجة تطبيقات وكلاء Mistral التجريبية لسير العمل الأكثر تعقيدًا.

#### استخدام خاصية استخدام الأدوات مع DeepSeek AI
واجهة برمجة تطبيقات DeepSeek متوافقة مع OpenAI، لذا يمكنك استخدام حزمة تطوير برامج OpenAI لـ Python. قم بالتثبيت باستخدام `pip install openai`.

**كود Python مثال** (من الوثائق الرسمية):
```python
from openai import OpenAI

# تهيئة العميل مع عنوان URL الأساسي لـ DeepSeek ومفتاح واجهة برمجة التطبيقات
client = OpenAI(
    api_key="YOUR_DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com"
)

# تعريف الأدوات
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

# دالة لإرسال الرسائل
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # يدعم استدعاء الأدوات
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

# رسالة المستخدم
messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

# معالجة استدعاء الأداة
tool = message.tool_calls[0]
messages.append(message)

# محاكاة تنفيذ الأداة (استبدال بدالة حقيقية)
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})

# الحصول على الرد النهائي
message = send_messages(messages)
print(f"Model>\t {message.content}")
```

يتبع هذا نفس التدفق: استعلام → استدعاء أداة → تنفيذ → رد نهائي. يحدد DeepSeek طول السياق، لذا حافظ على إيجاز الرسائل.

للحالات المتقدمة، تحقق من حدود المعدل، والتكاليف، والوثائق الخاصة بالنموذج. اختبر في بيئة اختبار للتعامل مع الأخطاء مثل المعلمات غير الصالحة.

### المراجع
- [Mistral AI Function Calling Documentation](https://docs.mistral.ai/agents/function_calling/)
- [DeepSeek API Function Calling Guide](https://api-docs.deepseek.com/guides/function_calling)
- [Mistral AI Function Calling Example with Code](https://medium.com/@jcrsch/mistral-ai-function-calling-a-simple-example-with-code-72f3a762550f)
- [DeepSeek vs. Mistral: A Comprehensive AI Models Comparison](https://medium.com/ai-tools-tips-and-news/deepseek-vs-mistral-a-comprehensive-ai-models-comparison-f7d7b86f4b28)
- [Mistral Large vs DeepSeek-V3 Comparison](https://docsbot.ai/models/compare/mistral-large-2/deepseek-v3)