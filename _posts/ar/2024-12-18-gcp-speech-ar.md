---
audio: false
generated: false
image: false
lang: ar
layout: post
title: بدء العمل مع واجهة برمجة تطبيقات تحويل النص إلى كلام من Google
translated: true
---

أخطط لتحويل بعض مقالات Yin Wang إلى صوت باستخدام واجهة برمجة تطبيقات Google Text-to-Speech. أدناه دليل خطوة بخطوة، بالإضافة إلى بعض البرامج التعليمية المفيدة التي قدمها ChatGPT. بمجرد أن يصبح كل شيء جاهزًا، سأقوم بتحميل الصوت هنا لكي تتمكن من الاستماع إليه.

---

### الخطوة 1: إعداد حساب Google Cloud

أولاً، تحتاج إلى إنشاء حساب على Google Cloud إذا لم يكن لديك حساب بالفعل. اتبع الخطوات التالية:

1. **زيارة موقع Google Cloud**: انتقل إلى [Google Cloud Platform](https://cloud.google.com/).
2. **إنشاء حساب جديد**: انقر على "Get Started for Free" وقم بإنشاء حساب جديد باستخدام بريدك الإلكتروني.
3. **تفعيل الحساب**: قد يُطلب منك إدخال معلومات الدفع لتأكيد هويتك، ولكنك تحصل على رصيد مجاني لبدء الاستخدام.

بمجرد إنشاء حسابك، ستتمكن من الوصول إلى لوحة تحكم Google Cloud حيث يمكنك إدارة جميع خدماتك.

1. إنشاء حساب Google Cloud  
   إذا لم يكن لديك حساب، سجل في [Google Cloud Console](https://console.cloud.google.com/).

2. إنشاء مشروع جديد  
   - في وحدة التحكم السحابية (Cloud Console)، انقر على قائمة اختيار المشروع (في أعلى اليسار).  
   - اختر "New Project"، قم بإعطائه اسمًا، ثم أنشئ المشروع.

3. تفعيل واجهة برمجة التطبيقات (API) للتحويل من النص إلى كلام  
   - قم بزيارة [صفحة واجهة برمجة التطبيقات للتحويل من النص إلى كلام على Google Cloud](https://cloud.google.com/text-to-speech).  
   - انقر على "تفعيل" لتنشيط الواجهة لمشروعك.

4. إنشاء بيانات اعتماد API  
   - انتقل إلى APIs & Services > Credentials في Cloud Console.  
   - انقر على Create Credentials، ثم اختر Service Account.  
   - اتبع التعليمات لإنشاء حساب الخدمة وتنزيل ملف المفتاح الخاص بتنسيق JSON.  
   - احتفظ بهذا الملف JSON بأمان حيث يتم استخدامه للمصادقة على طلبات API الخاصة بك.

---

### الخطوة 2: تثبيت Google Cloud SDK ومكتبة العميل

في هذه الخطوة، سنقوم بتثبيت Google Cloud SDK ومكتبة العميل اللازمة للتفاعل مع خدمات Google Cloud.

1. تثبيت Google Cloud SDK  
   إذا لم تكن قد قمت بذلك بعد، اتبع التعليمات لتثبيت [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) لنظام التشغيل الخاص بك.

2. تثبيت مكتبة العميل لـ Python  
   إذا كنت تستخدم Python، قم بتثبيت مكتبة `google-cloud-texttospeech` باستخدام الأمر التالي:

```bash
   pip install google-cloud-texttospeech
   ```

---

### الخطوة 3: إعداد المصادقة

قبل استخدام API، تحتاج إلى المصادقة باستخدام بيانات الاعتماد الخاصة بك. قم بتعيين متغير البيئة إلى المسار الخاص بملف بيانات الاعتماد:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

استبدل المسار بالموقع الفعلي لملف JSON الذي قمت بتنزيله.

---

### الخطوة 4: تنفيذ تحويل النص إلى كلام

في هذه الخطوة، سنقوم بتنفيذ وظيفة تحويل النص إلى كلام باستخدام مكتبة `gTTS` (Google Text-to-Speech). هذه المكتبة تسمح لنا بتحويل النص إلى ملف صوتي بتنسيق MP3.

#### 1. تثبيت المكتبة المطلوبة

أولاً، نحتاج إلى تثبيت مكتبة `gTTS` إذا لم تكن مثبتة بالفعل. يمكنك تثبيتها باستخدام `pip`:

```bash
pip install gtts
```

#### 2. كتابة الكود لتحويل النص إلى كلام

بعد تثبيت المكتبة، يمكننا كتابة كود بسيط لتحويل النص إلى كلام وحفظه كملف صوتي.

```python
from gtts import gTTS

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    print("تم تحويل النص إلى كلام وحفظه في ملف output.mp3")

# مثال للاستخدام
text = "مرحبًا، هذا مثال على تحويل النص إلى كلام."
text_to_speech(text, lang='ar')
```

#### 3. تشغيل الملف الصوتي

بعد تحويل النص إلى كلام وحفظه كملف MP3، يمكنك تشغيل الملف باستخدام أي مشغل صوتي متوفر على نظامك. إذا كنت ترغب في تشغيل الملف مباشرة من الكود، يمكنك استخدام مكتبة `os` لتشغيل الملف.

```python
import os

def play_audio(file_path):
    os.system(f"start {file_path}")  # لنظام ويندوز
    # os.system(f"afplay {file_path}")  # لنظام macOS
    # os.system(f"mpg321 {file_path}")  # لنظام Linux

# تشغيل الملف الصوتي
play_audio("output.mp3")
```

#### 4. اختبار الكود

قم بتشغيل الكود وتأكد من أن النص يتم تحويله إلى كلام بشكل صحيح وأن الملف الصوتي يتم تشغيله كما هو متوقع.

```bash
python your_script_name.py
```

إذا سارت الأمور على ما يرام، يجب أن تسمع النص الذي أدخلته يتم تحويله إلى كلام ويتم تشغيله كملف صوتي.

هذه هي الخطوات الأساسية لتنفيذ تحويل النص إلى كلام باستخدام Python. يمكنك تعديل الكود ليتناسب مع احتياجاتك الخاصة، مثل تغيير لغة الكلام أو إضافة ميزات إضافية.

إليك مثالًا باستخدام لغة Python لتحويل النص إلى كلام باستخدام واجهة برمجة تطبيقات Google Cloud Text-to-Speech:

```python
from google.cloud import texttospeech
```

```python
def text_to_speech(text, output_filename):
    # تهيئة عميل تحويل النص إلى كلام
    client = texttospeech.TextToSpeechClient()
```

    # إعداد مدخل التوليف
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # تعيين معلمات الصوت (باستخدام 'en-US-Journey-D')
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # الإنجليزية (الولايات المتحدة)
        name="en-US-Journey-D"  # نموذج صوت محدد (Journey)
    )

    # تعيين إعدادات الصوت
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # تنسيق MP3
        effects_profile_id=["small-bluetooth-speaker-class-device"],  # مُحسّن لمكبرات الصوت البلوتوث
        pitch=0.0,  # بدون تعديل في النغمة
        speaking_rate=0.9,  # معدل الكلام المعدل (يمكن تعديله حسب الحاجة)
        volume_gain_db=5.0  # زيادة مستوى الصوت
    )

    # تنفيذ طلب تحويل النص إلى كلام
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # كتابة محتوى الصوت إلى ملف
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"تم كتابة محتوى الصوت في {output_filename}")

# مثال على الاستخدام
article_text = "الأفلام، يا إلهي، أنا أعشقها تمامًا. إنها مثل آلات الزمن التي تأخذك إلى عوالم ومناظر طبيعية مختلفة، ولا أستطيع الحصول على ما يكفي منها."
output_file = "output_audio.mp3"  # الإخراج بصيغة MP3

# تحويل النص إلى كلام
text_to_speech(article_text, output_file)
```

---

### الخطوة 5: تشغيل البرنامج النصي

1. احفظ النص البرمجي كملف باسم `text_to_speech.py`.
2. قم بتشغيل النص البرمجي باستخدام:

   ```bash
   python text_to_speech.py
   ```

سيؤدي هذا إلى إنشاء ملف صوتي (`output_audio.mp3`) من النص المقدم.

---

### الخطوة 6: مفتاح حساب الخدمة

يجب أن يبدو مفتاح JSON لحساب الخدمة الخاص بك مشابهًا لهذا:

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "your-private-key",
  "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your-client-cert-url"
}
```

---

### لماذا تختار Journey؟

يقدم Google Cloud Text-to-Speech العديد من الأصوات، ولكن صوت Journey يتميز بكونه طبيعيًا ويشبه الصوت البشري. على عكس النماذج الأخرى التي غالبًا ما تبدو آلية، يتفوق Journey في التعبيرية والتوصيل الواقعي. وهو مناسب بشكل خاص للمحتوى الطويل مثل البودكاست أو الكتب الصوتية أو أي تطبيق يتطلب نبرة أكثر حوارية.

الميزات الرئيسية لـ Journey:
- الكلام الطبيعي: يبدو أقرب إلى صوت بشري.
- التعبيرية: يضبط النبرة والانعطاف بناءً على السياق.
- مثالي للمحتوى الطويل: مثالي للبودكاست والسرد.

لمزيد من التفاصيل حول فوائد خدمة Google Cloud Text-to-Speech، يمكنك الاطلاع على [نظرة عامة على Google Cloud](https://cloud.google.com/text-to-speech#benefits).

---

### الخطوة 7: إنشاء مفتاح حساب خدمة جديد (إذا لزم الأمر)

إذا كان مفتاح حساب الخدمة الخاص بك لا يتطابق مع المثال أعلاه، يمكنك إنشاء مفتاح جديد من خلال وحدة تحكم Google Cloud.

لإنشاء مفتاح جديد:
1. انتقل إلى [Google Cloud Console](https://console.cloud.google.com/).
2. انتقل إلى IAM & Admin > Service Accounts.
3. قم بإنشاء حساب خدمة جديد:
   - انقر على Create Service Account وقم بتعيين الأدوار المناسبة.
   - انقر على Create.
4. قم بإنشاء مفتاح:
   - بعد إنشاء حساب الخدمة، انقر عليه.
   - انتقل إلى علامة التبويب Keys، انقر على Add Key، واختر JSON. ثم قم بتنزيل المفتاح.

---

### مثال على إخراج الصوت

بمجرد أن يتم إعداد كل شيء، يمكنك إنشاء ملف صوتي، والذي سيكون متاحًا هنا:  
[تحميل الملف الصوتي](assets/audios/output-audio.mp3).

---

### الخلاصة

واجهة برمجة تطبيقات Google Cloud Text-to-Speech تجعل من السهل تحويل النص إلى كلام طبيعي. سواء كنت تبني تطبيقًا يحتاج إلى إخراج صوتي أو كنت تجرب تحويل النص إلى كلام، توفر هذه الواجهة ميزات قوية وخيارات تخصيص. استكشف الوثائق الكاملة للحصول على خيارات إضافية للأصوات واللغات والميزات المتقدمة.