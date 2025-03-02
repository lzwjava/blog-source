---
audio: false
generated: false
lang: ar
layout: post
title: استكشاف WebSocket
translated: true
---

*تمت مساعدة هذه المدونة بواسطة ChatGPT-4o.*

---

### مقدمة
مرحبًا بالجميع، أنا Li Zhiwei. بصفتي المؤسس والمدير التقني لمنصة CodeReview، ومهندس سابق في LeanCloud، لدي خبرة واسعة في مجال WebSocket، خاصة أثناء تطوير SDK للرسائل الفورية (IM).

### أهمية WebSocket
WebSocket هو بروتوكول يوفر قناة اتصال ثنائية الاتجاه عبر اتصال TCP واحد. يتم استخدامه على نطاق واسع في التطبيقات الحديثة التي تتطلب تفاعلًا في الوقت الفعلي، مثل المراسلة الفورية، التعليقات الفورية، الألعاب متعددة اللاعبين، التحرير التعاوني، وأسعار الأسهم الفورية.

### التطبيقات الحديثة لـ WebSocket
يُستخدم WebSocket على نطاق واسع في المجالات التالية:
- **المراسلة الفورية (IM)**
- **التعليقات في الوقت الفعلي**
- **الألعاب متعددة اللاعبين**
- **التعديل التعاوني**
- **أسعار الأسهم في الوقت الفعلي**

### تطور WebSocket
**الاستطلاع (Polling):** يقوم العميل بطلب الخادم بشكل متكرر للحصول على التحديثات.
**الاستطلاع الطويل (Long Polling):** يحتفظ الخادم بالطلب مفتوحًا حتى تتوفر معلومات جديدة.
**اتصال HTTP ثنائي الاتجاه:** يتطلب اتصالات متعددة للإرسال والاستقبال، ويحتوي كل طلب على رؤوس HTTP.
**اتصال TCP واحد (WebSocket):** يتغلب على قيود اتصال HTTP ثنائي الاتجاه، ويوفر قدرات في الوقت الفعلي أعلى وزمن انتقال أقل.

### تنفيذ WebSocket على iOS

WebSocket هو بروتوكول اتصال يوفر قناة اتصال ثنائية الاتجاه بين العميل والخادم. في تطبيقات iOS، يمكن استخدام WebSocket لإنشاء اتصالات في الوقت الفعلي مع الخادم، مما يسمح بتبادل البيانات بسرعة وكفاءة. في هذا المقال، سنتعرف على كيفية تنفيذ WebSocket في تطبيق iOS باستخدام Swift.

#### الخطوة 1: إضافة مكتبة Starscream

أولاً، نحتاج إلى إضافة مكتبة [Starscream](https://github.com/daltoniam/Starscream) إلى مشروعنا. Starscream هي مكتبة شائعة لتنفيذ WebSocket في Swift.

1. افتح ملف `Podfile` وأضف السطر التالي:

   ```ruby
   pod 'Starscream', '~> 4.0.0'
   ```

2. قم بتشغيل الأمر التالي في Terminal لتثبيت المكتبة:

   ```bash
   pod install
   ```

#### الخطوة 2: إنشاء اتصال WebSocket

بعد تثبيت المكتبة، يمكننا البدء في إنشاء اتصال WebSocket.

```swift
import Starscream

class WebSocketManager: WebSocketDelegate {
    var socket: WebSocket!

    init() {
        var request = URLRequest(url: URL(string: "wss://yourserver.com")!)
        request.timeoutInterval = 5
        socket = WebSocket(request: request)
        socket.delegate = self
        socket.connect()
    }

    func didReceive(event: WebSocketEvent, client: WebSocket) {
        switch event {
        case .connected(let headers):
            print("WebSocket is connected: \(headers)")
        case .disconnected(let reason, let code):
            print("WebSocket is disconnected: \(reason) with code: \(code)")
        case .text(let string):
            print("Received text: \(string)")
        case .binary(let data):
            print("Received data: \(data.count)")
        case .ping(_):
            break
        case .pong(_):
            break
        case .viabilityChanged(_):
            break
        case .reconnectSuggested(_):
            break
        case .cancelled:
            print("WebSocket is cancelled")
        case .error(let error):
            print("WebSocket encountered an error: \(String(describing: error))")
        }
    }

    func sendMessage(_ message: String) {
        socket.write(string: message)
    }

    func disconnect() {
        socket.disconnect()
    }
}
```

#### الخطوة 3: استخدام WebSocketManager

الآن بعد أن أنشأنا `WebSocketManager`، يمكننا استخدامه في أي جزء من التطبيق لإرسال واستقبال الرسائل.

```swift
let webSocketManager = WebSocketManager()

// إرسال رسالة
webSocketManager.sendMessage("Hello, Server!")

// قطع الاتصال
webSocketManager.disconnect()
```

#### الخلاصة

في هذا المقال، تعلمنا كيفية تنفيذ WebSocket في تطبيق iOS باستخدام مكتبة Starscream. يمكن استخدام WebSocket لإنشاء اتصالات في الوقت الفعلي مع الخادم، مما يسمح بتبادل البيانات بسرعة وكفاءة. يمكن توسيع هذا المثال ليشمل المزيد من الميزات مثل إعادة الاتصال التلقائي وإدارة الأخطاء.

**مكتبات WebSocket الشهيرة لنظام iOS:**
- **SocketRocket (Objective-C، 4910 نجوم)**
- **Starscream (Swift، 1714 نجوم)**
- **SwiftWebSocket (Swift، 435 نجوم)**

### استخدام SRWebSocket

1. **التهيئة والاتصال:**
   ```objective-c
   SRWebSocket *webSocket = [[SRWebSocket alloc] initWithURLRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:@"ws://echo.websocket.org"]]];
   webSocket.delegate = self;
   [webSocket open];
   ```

2. **إرسال الرسالة:**
   ```objective-c
   [webSocket send:@"Hello, World!"];
   ```

3. **استقبال الرسائل:**
   قم بتنفيذ طرق `SRWebSocketDelegate` للتعامل مع الرسائل الواردة والأحداث.

4. **معالجة الأخطاء وإشعارات الأحداث:**
   قم بمعالجة الأخطاء بشكل مناسب وأخبر المستخدمين بأي مشاكل في الاتصال.

### شرح مفصل لبروتوكول WebSocket

WebSocket هو بروتوكول اتصالات يوفر قناة اتصال ثنائية الاتجاه (Full-Duplex) عبر اتصال TCP واحد. تم تصميمه ليتم تنفيذه في المتصفحات وخوادم الويب، ولكنه يمكن استخدامه أيضًا في أي تطبيق عميل/خادم. يتميز WebSocket بإمكانية إرسال البيانات بين العميل والخادم في الوقت الفعلي دون الحاجة إلى إجراء طلبات HTTP متكررة.

#### كيف يعمل WebSocket؟

1. **مصافحة اليد (Handshake):**
   - يبدأ الاتصال بمصافحة HTTP تُعرف بـ "Upgrade Request". يرسل العميل طلب HTTP إلى الخادم مع طلب ترقية الاتصال إلى WebSocket.
   - إذا وافق الخادم على الطلب، فإنه يرد برسالة تأكيد ترقية الاتصال إلى WebSocket.

   ```http
   GET /chat HTTP/1.1
   Host: server.example.com
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
   Sec-WebSocket-Version: 13
   ```

   ```http
   HTTP/1.1 101 Switching Protocols
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
   ```

2. **نقل البيانات:**
   - بعد إتمام المصافحة، يتم إنشاء قناة اتصال ثنائية الاتجاه يمكن من خلالها إرسال البيانات بين العميل والخادم.
   - يتم إرسال البيانات في شكل إطارات (Frames) صغيرة، والتي يمكن أن تحتوي على نصوص أو بيانات ثنائية.

3. **إغلاق الاتصال:**
   - يمكن لأي من الطرفين (العميل أو الخادم) إغلاق الاتصال بإرسال إطار إغلاق (Close Frame).

#### مميزات WebSocket:

- **الاتصال المستمر:** على عكس HTTP الذي يعتمد على طلبات فردية، فإن WebSocket يحافظ على اتصال مفتوح طوال فترة التفاعل.
- **الكفاءة:** يتم تقليل النفقات العامة (Overhead) مقارنة بطلبات HTTP المتكررة.
- **الدعم للبيانات الثنائية:** يمكن إرسال البيانات الثنائية (Binary Data) بالإضافة إلى النصوص.

#### استخدامات WebSocket:

- التطبيقات التي تتطلب تحديثات في الوقت الفعلي مثل تطبيقات الدردشة.
- الألعاب متعددة اللاعبين عبر الإنترنت.
- التطبيقات المالية التي تتطلب تحديثات سريعة للأسعار.

#### مثال بسيط باستخدام JavaScript:

```javascript
// إنشاء اتصال WebSocket
const socket = new WebSocket('ws://example.com/socket');

// فتح الاتصال
socket.onopen = function(event) {
    console.log('Connection established');
    socket.send('Hello Server!');
};

// استقبال الرسائل من الخادم
socket.onmessage = function(event) {
    console.log('Message from server:', event.data);
};

// إغلاق الاتصال
socket.onclose = function(event) {
    console.log('Connection closed');
};
```

```javascript
// على جانب الخادم (Node.js مع مكتبة ws)
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(message) {
        console.log('received: %s', message);
    });

    ws.send('Hello Client!');
});
```

WebSocket هو أداة قوية لبناء تطبيقات تفاعلية في الوقت الفعلي، ويوفر تحسينات كبيرة في الأداء مقارنة بالطرق التقليدية مثل HTTP Long Polling.

يعمل WebSocket فوق بروتوكول TCP ويقدم عدة تحسينات:
- **نموذج الأمان:** تمت إضافة نموذج أمان يعتمد على التحقق من المصدر في المتصفحات.
- **تسمية العناوين والبروتوكولات:** يدعم خدمات متعددة على منفذ واحد وأسماء نطاقات متعددة على عنوان IP واحد.
- **آلية الإطارات:** تم تعزيز TCP بآلية إطارات مشابهة لحزم IP، دون قيود على الطول.
- **مصافحة الإغلاق:** يضمن إغلاق الاتصال بشكل نظيف.

### أساسيات بروتوكول WebSocket

WebSocket هو بروتوكول اتصالات يوفر قناة اتصال ثنائية الاتجاه (Full-Duplex) عبر اتصال TCP واحد. تم تصميمه ليتم تنفيذه في المتصفحات وخوادم الويب، ولكنه يمكن استخدامه أيضًا في أي تطبيق عميل/خادم. تم تقديم WebSocket كجزء من HTML5، وهو يعمل على تحسين الاتصال بين العميل والخادم مقارنةً بالتقنيات القديمة مثل HTTP Long Polling.

#### الميزات الرئيسية لـ WebSocket:

1. **ثنائية الاتجاه (Full-Duplex)**: يمكن للعميل والخادم إرسال البيانات في نفس الوقت دون الحاجة إلى انتظار الطرف الآخر.
2. **اتصال مستمر**: بمجرد إنشاء الاتصال، يبقى مفتوحًا حتى يتم إغلاقه من قبل أحد الطرفين.
3. **نقل البيانات الخفيف**: يتم إرسال البيانات بتنسيق خفيف الوزن، مما يقلل من النفقات العامة (overhead) مقارنةً ببروتوكولات أخرى مثل HTTP.
4. **دعم للبيانات النصية والثنائية**: يمكن إرسال البيانات النصية والثنائية عبر WebSocket.

#### كيفية عمل WebSocket:

1. **مصافحة (Handshake)**: يبدأ الاتصال بمصافحة HTTP تُعرف باسم "Upgrade Request"، حيث يطلب العميل من الخادم ترقية الاتصال إلى بروتوكول WebSocket.
   
   ```http
   GET /chat HTTP/1.1
   Host: server.example.com
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
   Sec-WebSocket-Version: 13
   ```

   يقوم الخادم بالرد بالموافقة على الترقية:

   ```http
   HTTP/1.1 101 Switching Protocols
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
   ```

2. **نقل البيانات**: بعد إنشاء الاتصال، يمكن للعميل والخادم إرسال البيانات بشكل مستقل. يتم تقسيم البيانات إلى إطارات (frames) صغيرة يتم إرسالها عبر الاتصال.

3. **إغلاق الاتصال**: يمكن لأي من الطرفين إغلاق الاتصال بإرسال إطار إغلاق (Close Frame).

#### مثال بسيط باستخدام JavaScript:

```javascript
// إنشاء اتصال WebSocket
const socket = new WebSocket('ws://example.com/socket');

// عند فتح الاتصال
socket.onopen = function(event) {
    console.log('Connection opened');
    socket.send('Hello Server!');
};

// عند استقبال رسالة من الخادم
socket.onmessage = function(event) {
    console.log('Message from server:', event.data);
};

// عند إغلاق الاتصال
socket.onclose = function(event) {
    console.log('Connection closed');
};

// عند حدوث خطأ
socket.onerror = function(error) {
    console.error('WebSocket error:', error);
};
```

#### استخدامات WebSocket:

- **التطبيقات التفاعلية**: مثل الدردشة الحية، الألعاب متعددة اللاعبين.
- **التحديثات الفورية**: مثل تحديثات الأسهم، الإشعارات الفورية.
- **التحكم في الوقت الحقيقي**: مثل التحكم في الأجهزة عن بعد.

WebSocket يوفر طريقة فعالة ومرنة للتواصل في الوقت الحقيقي بين العميل والخادم، مما يجعله خيارًا مثاليًا للعديد من التطبيقات الحديثة.

**1. المصافحة:**
   تستخدم WebSocket آلية الترقية الخاصة بـ HTTP لإتمام المصافحة:
   - **طلب العميل:**
     ```http
     GET /chat HTTP/1.1
     Host: server.example.com
     Upgrade: websocket
     Connection: Upgrade
     Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
     Origin: http://example.com
     Sec-WebSocket-Protocol: chat, superchat
     Sec-WebSocket-Version: 13
     ```

   - **استجابة الخادم:**
     ```http
     HTTP/1.1 101 تبديل البروتوكولات
     الترقية: websocket
     الاتصال: الترقية
     Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
     Sec-WebSocket-Protocol: chat
     ```

**2. نقل البيانات:**
   يمكن أن تحتوي إطارات WebSocket على نصوص بتنسيق UTF-8، وبيانات ثنائية، وإطارات تحكم مثل الإغلاق، وping، وpong.

**3. الأمان:**
   يقوم المتصفح تلقائيًا بإضافة رأس `Origin`، والذي لا يمكن تزويره من قبل العملاء الآخرين.

### عنوان WebSocket

- **ws-URI:** `ws://host:port/path?query`
- **wss-URI:** `wss://host:port/path?query`

### بروتوكول إطارات WebSocket

WebSocket هو بروتوكول اتصال ثنائي الاتجاه يعمل فوق اتصال TCP واحد. يتم تقسيم البيانات المرسلة عبر WebSocket إلى إطارات (frames) صغيرة، حيث يتم إرسال كل إطار بشكل مستقل. يتكون بروتوكول إطارات WebSocket من عدة أجزاء رئيسية:

1. **البت الأول (FIN)**: يشير إلى ما إذا كانت هذه هي الإطار الأخير في الرسالة.
2. **بتات التحكم (Opcode)**: تحدد نوع الإطار (مثل نص، بيانات ثنائية، إغلاق، إلخ).
3. **بت الإخفاء (Mask)**: يشير إلى ما إذا كانت البيانات مخفية.
4. **طول الحمولة (Payload Length)**: يحدد طول البيانات المرسلة.
5. **مفتاح الإخفاء (Masking Key)**: يستخدم لإخفاء البيانات إذا كان بت الإخفاء مضبوطًا.
6. **البيانات (Payload Data)**: البيانات الفعلية المرسلة.

#### مثال على إطار WebSocket

```plaintext
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-------+-+-------------+-------------------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
| |1|2|3|       |K|             |                               |
+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
|     Extended payload length continued, if payload len == 127  |
+ - - - - - - - - - - - - - - - +-------------------------------+
|                               |Masking-key, if MASK set to 1  |
+-------------------------------+-------------------------------+
| Masking-key (continued)       |          Payload Data         |
+-------------------------------- - - - - - - - - - - - - - - - +
:                     Payload Data continued ...                :
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
|                     Payload Data continued ...                |
+---------------------------------------------------------------+
```

في هذا المثال، يتم تقسيم الإطار إلى أجزاء مختلفة تحدد خصائص الإطار والبيانات المرسلة. يتم استخدام هذا التنسيق لضمان نقل البيانات بشكل فعال وآمن عبر اتصال WebSocket.

**هيكل الإطار:**
- **FIN (1 بت):** يشير إلى أن هذا هو الجزء الأخير من الرسالة.
- **RSV1, RSV2, RSV3 (1 بت لكل منهما):** محجوزة للاستخدام المستقبلي.
- **Opcode (4 بتات):** يحدد كيفية تحليل بيانات الحمولة.
  - `0x0:` إطار متابعة
  - `0x1:` إطار نصي
  - `0x2:` إطار ثنائي
  - `0x8:` إغلاق الاتصال
  - `0x9:` ping
  - `0xA:` pong
- **Mask (1 بت):** يشير إلى ما إذا كانت بيانات الحمولة مقنعة أم لا.
- **طول الحمولة (7 بتات):** طول بيانات الحمولة.

**مفتاح القناع (Masking Key):** يُستخدم لمنع هجمات الرجل في المنتصف (Man-in-the-Middle) عن طريق إخفاء إطارات العميل.

### إغلاق المصافحة

**إطار الإغلاق (Close Frame):**
- يمكن أن يحتوي على نص يوضح سبب الإغلاق.
- يجب على كلا الطرفين إرسال واستقبال إطار الإغلاق.

### مثال

**المثال 1: رسالة نصية غير مقنعة بإطار واحد**
```hex
0x81 0x05 0x48 0x65 0x6c 0x6c 0x6f
```
تحتوي على "Hello"

**المثال الثاني: رسالة نصية بإطار واحد مع قناع**
```hex
0x81 0x85 0x37 0xfa 0x21 0x3d 0x7f 0x9f 0x4d 0x51 0x58
```
تحتوي على "Hello" مع مفتاح القناع.

**المثال الثالث: رسالة نصية مجزأة بدون قناع**
```hex
0x01 0x03 0x48 0x65 0x6c
0x80 0x02 0x6c 0x6f
```
الرسالة المجزأة تحتوي على إطارين: "Hel" و "lo".

### الموضوعات المتقدمة

**التعتيم وإزالة التعتيم:**
- يُستخدم التعتيم لمنع هجمات الرجل في المنتصف (Man-in-the-Middle).
- يجب تعتيم كل إطار (frame) يأتي من العميل.
- يتم اختيار مفتاح التعتيم لكل إطار بشكل عشوائي.

**التجزئة (Fragmentation):**
- تُستخدم لإرسال بيانات ذات طول غير معروف.
- تبدأ رسائل التجزئة بإطار ذو علامة FIN تساوي 0، وتنتهي بإطار ذو علامة FIN تساوي 1.

**إطارات التحكم:**
- تحتوي إطارات التحكم (مثل إغلاق الاتصال، ping، وpong) على أكواد تشغيل محددة.
- تُستخدم هذه الإطارات لإدارة حالة اتصال WebSocket.

### قابلية التوسع

**يمكن وضع البيانات الموسعة قبل بيانات التطبيق في جسم الرسالة:**
- يمكن التحكم في كل إطار باستخدام البتات المحجوزة.
- يتم حجز بعض رموز العمليات للتعريفات المستقبلية.
- إذا كانت هناك حاجة إلى المزيد من رموز العمليات، يمكن استخدام البتات المحجوزة.

**الإرسال:**
- يجب التأكد من أن الاتصال في حالة OPEN.
- يتم تغليف البيانات في إطارات، ويمكن اختيار إرسالها مجزأة إذا كانت البيانات كبيرة.
- يجب أن تكون قيمة الإطار الأول صحيحة، لإعلام الطرف المستقبل بنوع البيانات (نص أو ثنائي).
- يجب تعيين FIN للإطار الأخير إلى 1.

**إغلاق المصافحة:**
- يمكن لكلا الطرفين إرسال إطار الإغلاق.
- بعد إرسال إطار الإغلاق، لا يتم إرسال أي بيانات أخرى.
- عند استلام إطار الإغلاق، يتم تجاهل أي بيانات يتم تلقيها بعد ذلك.

**إغلاق الاتصال:**
- إغلاق اتصال WebSocket يعني إغلاق الاتصال TCP الأساسي.
- بعد إرسال أو استقبال إطار الإغلاق، تصبح حالة اتصال WebSocket في طور الإغلاق.
- عند إغلاق الاتصال TCP الأساسي، تصبح حالة اتصال WebSocket مغلقًا.

### المراجع

- WebSocket RFC: [RFC6455](https://tools.ietf.org/html/rfc6455)
- مقالة "ما هو مبدأ WebSocket؟" على Zhihu: [رابط Zhihu](https://www.zhihu.com/question/20215561)
- SocketRocket: [رابط GitHub](https://github.com/square/SocketRocket)

### الشكر والتقدير

شكرًا لكم جميعًا على اهتمامكم. إذا كانت لديكم المزيد من الأسئلة أو النقاشات، فلا تترددوا في التواصل معي على GitHub أو Weibo.