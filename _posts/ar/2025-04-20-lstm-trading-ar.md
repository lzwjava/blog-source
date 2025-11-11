---
audio: false
generated: true
lang: ar
layout: post
title: دمج البيانات التاريخية مع الشبكة العصبية طويلة المدى القصيرة
translated: true
type: note
---

دمج بيانات الأسهم التاريخية من TigerOpen API مع نموذج LSTM للتحليل أمر ممكن وهو نهج شائع في التنبؤ بالسلاسل الزمنية المالية. البرنامج النصي الثاني يسترجع بيانات الأسهم التاريخية (مثل أشرطة OHLCV)، والتي يمكن استخدامها لبناء مجموعة بيانات لتدريب نموذج LSTM مشابه للنموذج في البرنامج النصي الأول. أدناه، أشرح كيف يمكنك دمج هذين العنصرين، ومعالجة التحديات المحتملة، وتقديم نهج عالي المستوى لتحليل بيانات الأسهم باستخدام LSTM.

### النهج عالي المستوى لدمج العنصرين

1.  **استرجاع البيانات التاريخية**:
    - استخدم الدالة `get_history_data` من البرنامج النصي الثاني لجلب بيانات الأسهم التاريخية (مثل الرمز '00700' أو غيره).
    - تتضمن البيانات أسعار الفتح، الأعلى، الأدنى، والإغلاق، والحجم، والطوابع الزمنية، والتي يمكن استخدامها كسمات لنموذج LSTM.

2.  **المعالجة المسبقة للبيانات لـ LSTM**:
    - تحويل البيانات التاريخية إلى تنسيق مناسب لنموذج LSTM. يتضمن ذلك:
        - تسوية البيانات (مثل تحجيم الأسعار والحجم إلى [0, 1]).
        - إنشاء تسلسلات من البيانات التاريخية (مثل استخدام بيانات الـ 60 يومًا الماضية للتنبؤ بسعر الإغلاق في اليوم التالي).
        - ترميز السمات (مثل سعر الإغلاق، الحجم) إلى تنسيق tensor متوافق مع إدخال LSTM.

3.  **تعديل نموذج LSTM**:
    - تعديل فئة `Net` من البرنامج النصي الأول للتعامل مع بيانات السلاسل الزمنية المالية بدلاً من تسلسلات النص.
    - ضبط حجم الإدخال ليتطابق مع عدد السمات (مثل سعر الإغلاق، الحجم، إلخ) بدلاً من `vocab_size`.
    - تحديث طبقة الإخراج للتنبؤ بقيمة مستمرة (مثل سعر الإغلاق في اليوم التالي) أو تصنيف (مثل زيادة/انخفاض السعر).

4.  **تدريب النموذج**:
    - تقسيم البيانات التاريخية إلى مجموعات تدريب، وتحقق، واختبار.
    - تدريب LSTM باستخدام البيانات المعالجة مسبقًا، بشكل مشابه لحلقة التدريب في البرنامج النصي الأول.
    - استخدام دالة خسارة مثل Mean Squared Error (MSE) لمهام الانحدار أو Cross-Entropy Loss للتصنيف.

5.  **التحليل والتنبؤ**:
    - استخدام LSTM المدرب للتنبؤ بأسعار الأسهم المستقبلية أو الاتجاهات بناءً على البيانات التاريخية الحديثة.
    - تصور التنبؤات جنبًا إلى جنب مع البيانات الفعلية باستخدام `matplotlib`.

6.  **التكامل مع التداول**:
    - استخدام التنبؤات لإبلاغ قرارات التداول في الدالة `place_order`.
    - على سبيل المثال، تقديم أمر شراء إذا توقع LSTM زيادة في السعر تتجاوز عتبة معينة.

### مثال على الكود: دمج البيانات التاريخية مع LSTM

أدناه مقتطف كود نموذجي يدمج البرنامجين النصيين، مع التركيز على المعالجة المسبقة للبيانات التاريخية وتكييف LSTM للتنبؤ بأسعار الأسهم.

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tigeropen.common.consts import Language, Market, BarPeriod, QuoteRight
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.util.signature_utils import read_private_key
import os
from datetime import datetime

# --- إعداد TigerOpen API ---
def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config

def get_history_data(symbol='00700', period=BarPeriod.DAY, begin_time='2024-01-01', end_time=None, limit=100):
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    if not end_time:
        end_time = datetime.now().strftime('%Y-%m-%d')
    bars_dict = quote_client.get_bars(
        symbols=[symbol], period=period, begin_time=begin_time, end_time=end_time, limit=limit, right=QuoteRight.BR
    )
    bars = bars_dict.get(symbol, [])
    return pd.DataFrame([{
        'time': bar.time,
        'open': bar.open,
        'high': bar.high,
        'low': bar.low,
        'close': bar.close,
        'volume': bar.volume
    } for bar in bars])

# --- نموذج LSTM ---
class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=50, num_layers=1):
        super(StockLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, bidirectional=False)
        self.l_out = nn.Linear(in_features=hidden_size, out_features=1)  # التنبؤ بسعر الإغلاق التالي

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x[:, -1, :]  # أخذ خطوة الوقت الأخيرة
        x = self.l_out(x)
        return x

# --- المعالجة المسبقة للبيانات ---
def prepare_data(df, sequence_length=60, target_col='close'):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[target_col]].values)
    
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])
    
    X = np.array(X)
    y = np.array(y)
    
    # التقسيم إلى تدريب واختبار
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return torch.Tensor(X_train), torch.Tensor(y_train), torch.Tensor(X_test), torch.Tensor(y_test), scaler

# --- حلقة التدريب ---
def train_model(model, X_train, y_train, X_test, y_test, num_epochs=50, lr=3e-4):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    training_loss, validation_loss = [], []
    
    for epoch in range(num_epochs):
        model.train()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        training_loss.append(loss.item())
        
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_test)
            val_loss = criterion(val_outputs, y_test)
            validation_loss.append(val_loss.item())
        
        if epoch % 5 == 0:
            print(f'Epoch {epoch}, Training Loss: {training_loss[-1]:.4f}, Validation Loss: {validation_loss[-1]:.4f}')
    
    return training_loss, validation_loss

# --- التنفيذ الرئيسي ---
if __name__ == '__main__':
    # جلب البيانات التاريخية
    df = get_history_data(symbol='00700', limit=1000)
    
    # تحضير البيانات
    sequence_length = 60
    X_train, y_train, X_test, y_test, scaler = prepare_data(df, sequence_length=sequence_length, target_col='close')
    
    # تهيئة وتدريب LSTM
    model = StockLSTM(input_size=1, hidden_size=50, num_layers=1)
    training_loss, validation_loss = train_model(model, X_train, y_train, X_test, y_test, num_epochs=50)
    
    # رسم خسائر التدريب والتحقق
    plt.figure()
    plt.plot(training_loss, 'r', label='Training Loss')
    plt.plot(validation_loss, 'b', label='Validation Loss')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.show()
    
    # عمل التنبؤات
    model.eval()
    with torch.no_grad():
        predicted = model(X_test).numpy()
    
    # التحويل العكسي للتنبؤات
    predicted = scaler.inverse_transform(predicted)
    y_test_actual = scaler.inverse_transform(y_test.numpy())
    
    # رسم التنبؤات مقابل الفعلية
    plt.figure()
    plt.plot(y_test_actual, 'b', label='Actual Close Price')
    plt.plot(predicted, 'r', label='Predicted Close Price')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.show()
```

### التعديلات والملاحظات الرئيسية

1.  **استرجاع البيانات**:
    - يتم استخدام الدالة `get_history_data` لجلب بيانات الأسهم التاريخية لرمز معين (مثل '00700' لـ Tencent).
    - يتم تحويل البيانات إلى pandas DataFrame لتسهيل التلاعب.

2.  **المعالجة المسبقة**:
    - يتم تسوية البيانات باستخدام `MinMaxScaler` لتحجيم أسعار الإغلاق إلى [0, 1].
    - يتم إنشاء تسلسلات بطول `sequence_length` (مثل 60 يومًا) للتنبؤ بسعر الإغلاق في اليوم التالي.
    - يتم تقسيم البيانات إلى مجموعات تدريب (80%) واختبار (20%).

3.  **نموذج LSTM**:
    - تم تكييف فئة `StockLSTM` للتعامل مع سمة واحدة (سعر الإغلاق) أو سمات متعددة (مثل الإغلاق، الحجم) عن طريق ضبط `input_size`.
    - تتنبأ طبقة الإخراج بقيمة واحدة (سعر الإغلاق في اليوم التالي) باستخدام طبقة خطية.

4.  **التدريب**:
    - تستخدم حلقة التدريب خسارة MSE للانحدار، وهي مناسبة للتنبؤ بالقيم المستمرة مثل أسعار الأسهم.
    - يتم تقييم النموذج على مجموعة الاختبار لتتبع خسارة التحقق.

5.  **التصور**:
    - يتم رسم خسائر التدريب والتحقق لتقييم تقارب النموذج.
    - يتم رسم أسعار الإغلاق المتوقعة مقابل الفعلية لتقييم أداء النموذج.

### التحديات والاعتبارات المحتملة

1.  **جودة البيانات وكميتها**:
    - قد تكون كمية البيانات التاريخية (مثل `limit=1000` شريط) غير كافية لتدريب قوي لـ LSTM. فكر في جلب المزيد من البيانات أو استخدام `sequence_length` أصغر.
    - يمكن أن تكون بيانات الأسهم صاخبة، وقد تواجه نماذج LSTM صعوبة في التعامل مع التبعيات طويلة المدى أو التحولات المفاجئة في السوق.

2.  **هندسة السمات**:
    - يستخدم المثال سعر الإغلاق فقط. يمكن أن يؤدي تضمين سمات إضافية (مثل الحجم، المتوسطات المتحركة، المؤشرات الفنية مثل RSI) إلى تحسين أداء النموذج.
    - يعد اختيار السمات والمعالجة المسبقة (مثل معالجة البيانات المفقودة، القيم المتطرفة) أمرًا بالغ الأهمية.

3.  **تعقيد النموذج**:
    - بنية LSTM بسيطة (1 طبقة، 50 وحدة مخفية). للبيانات المالية المعقدة، فكر في نماذج أعمق، أو استخدام dropout للتنظيم، أو هياكل أخرى مثل GRU أو Transformer.

4.  **التجهيز الزائد (Overfitting)**:
    - راقب خسارة التدريب مقابل خسارة التحقق لاكتشاف التجهيز الزائد. أضف dropout أو decay للوزن إذا لزم الأمر.

5.  **التكامل في الوقت الفعلي**:
    - لاستخدام النموذج للتداول في الوقت الفعلي، قم بجلب البيانات الحديثة، ومعالجتها مسبقًا، وتغذيتها في LSTM المدرب لتوليد التنبؤات.
    - اجمع التنبؤات مع استراتيجية تداول (مثل الشراء إذا كان السعر المتوقع > السعر الحالي بنسبة X%).

6.  **قيود API**:
    - تأكد من تعيين بيانات اعتماد TigerOpen API بشكل صحيح في متغيرات البيئة (`TIGER_PEM`, `TIGER_TIGER_ID`, `TIGER_ACCOUNT`).
    - كن على علم بحدود معدل API وتوافر البيانات لرموز أو فترات زمنية معينة.

### مثال على الإخراج

بافتراض تشغيل الكود بنجاح، قد ترى:
- إخراج وحدة التحكم يظهر خسائر التدريب والتحقق لكل عصر (مثال: `Epoch 0, Training Loss: 0.1234, Validation Loss: 0.1345`).
- رسم بياني لخسائر التدريب والتحقق عبر العصور، يشير إلى التقارب.
- رسم بياني يقارن أسعار الإغلاق المتوقعة مقابل الفعلية لمجموعة الاختبار، يوضح مدى جودة捕捉 LSTM للاتجاهات.

### الخطوات التالية

-   **تحسين السمات**: دمج المؤشرات الفنية (مثل MACD، Bollinger Bands) أو بيانات المشاعر من منشورات X (إذا كانت متاحة عبر البحث).
-   **الاختبار الاسترجاعي (Backtesting)**: اختبار تنبؤات LSTM في بيئة تداول محاكاة باستخدام البيانات التاريخية لتقييم الربحية.
-   **تكامل التداول**: استخدام الدالة `place_order` لتنفيذ الصفقات بناءً على تنبؤات LSTM، مع إدارة مناسبة للمخاطر.
-   **ضبط المعاملات الفائقة**: تجربة `sequence_length`, `hidden_size`, `num_layers`, ومعدل التعلم لتحسين الأداء.

### هل سيعمل؟

نعم، يعد دمج بيانات الأسهم التاريخية مع LSTM للتحليل نهجًا قابلًا للتطبيق ومستخدمًا على نطاق واسع في التداول الخوارزمي. ومع ذلك، يعتمد النجاح على:
-   بيانات كافية ونظيفة.
-   المعالجة المسبقة الصحيحة وهندسة السمات.
-   نموذج LSTM مضبوط جيدًا.
-   استراتيجية تداول قوية للعمل على التنبؤات.

أسواق المال صاخبة بطبيعتها وتتأثر بعوامل خارجية (مثل الأخبار، الأحداث الاقتصادية الكلية)، لذا يجب استخدام تنبؤات LSTM بحذر، ويفضل أن تكون جزءًا من استراتيجية أوسع مع ضوابط للمخاطر.

إذا كنت ترغب في التعمق في أي جزء (مثل إضافة سمات، الاختبار الاسترجاعي، أو التداول في الوقت الفعلي)، دعني أعرف!