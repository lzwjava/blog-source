---
audio: false
generated: true
lang: ar
layout: post
title: استخدام إيفنت باس في أندرويد
translated: true
type: note
---

سأشرح كيفية استخدام EventBus في Android، وهي مكتبة شائعة لنظام نشر/اشتراك الأحداث تبسط التواصل بين المكونات مثل الأنشطة (Activities) والشظايا (Fragments) والخيوط الخلفية (background threads).

أولاً، أضف تبعية EventBus إلى مشروعك. في ملف `build.gradle` (وحدة التطبيق)، أدرج:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

إليك دليلًا خطوة بخطوة:

1. **تحديد فئة الحدث (Event Class)**
أنشئ فئة POJO بسيطة لتمثيل الحدث الخاص بك:

```java
public class MessageEvent {
    private String message;
    
    public MessageEvent(String message) {
        this.message = message;
    }
    
    public String getMessage() {
        return message;
    }
}
```

2. **تسجيل المشترك (Subscriber)**
في Activity/Fragment حيث تريد استقبال الأحداث:

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // التسجيل في EventBus
        EventBus.getDefault().register(this);
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        // إلغاء التسجيل لمنع تسريبات الذاكرة
        EventBus.getDefault().unregister(this);
    }
    
    // طريقة المشترك
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // معالجة الحدث
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **نشر حدث (Post an Event)**
من أي مكان في الكود الخاص بك (نشاط آخر، شظية، خدمة، إلخ):

```java
// نشر حدث
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

الميزات والخيارات الرئيسية:

- **خيارات ThreadMode**:
  - `ThreadMode.MAIN`: يعمل على الخيط الرئيسي في Android (خيط واجهة المستخدم)
  - `ThreadMode.BACKGROUND`: يعمل على خيط خلفي
  - `ThreadMode.ASYNC`: ينفذ في خيط منفصل
  - `ThreadMode.POSTING`: يعمل في نفس الخيط الذي نشره

- **الأحداث اللاصقة (Sticky Events)**:
للأحداث التي تحتاج إلى الاستمرار للمشتركين المتأخرين:

```java
// نشر حدث لاصق
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// استقبال الأحداث اللاصقة
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // معالجة الحدث اللاصق
}
```

- **الأولوية (Priority)**:
حدد أولوية للمشتركين (رقم أعلى = أولوية أعلى):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // هذا المشترك لديه أولوية أعلى
}
```

أفضل الممارسات:
1. قم دائمًا بإلغاء التسجيل في `onDestroy()` لتجنب تسريبات الذاكرة
2. استخدم فئات أحداث محددة بدلاً من الكائنات العامة
3. تعامل مع الاستثناءات في طرق المشتركين
4. فكر في استخدام الأحداث اللاصقة لتغييرات التكوين
5. كن حذرًا عند نشر الأحداث من الخيوط الخلفية إلى مشتركي واجهة المستخدم

مثال بسيط بمكونات متعددة:

```java
// فئة الحدث
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// المرسل (مثل Fragment)
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// المستقبل (مثل Activity)
public class ReceiverActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EventBus.getDefault().register(this);
    }
    
    @Override
    protected void onDestroy() {
        EventBus.getDefault().unregister(this);
        super.onDestroy();
    }
    
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onDataEvent(DataEvent event) {
        textView.setText("Received: " + event.getData());
    }
}
```

EventBus مفيد بشكل خاص لـ:
- فصل المكونات
- التواصل بين الشظايا (Fragments)
- تحديث واجهة المستخدم من العمليات الخلفية
- التعامل مع تغييرات التكوين

تذكر أن تتعامل مع دورة الحياة بشكل صحيح وأن تختبر تدفقات الأحداث الخاصة بك بدقة!