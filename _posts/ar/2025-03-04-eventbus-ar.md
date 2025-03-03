---
audio: false
generated: true
lang: ar
layout: post
title: استخدام EventBus في Android
translated: true
---

سأشرح كيفية استخدام EventBus في Android، وهي مكتبة شائعة للنقل عبر الحافلات التي تسهل التواصل بين المكونات مثل الأنشطة، الفragments، والخيوط الخلفية.

أولاً، أضف الاعتماد على EventBus إلى مشروعك. في ملف `build.gradle` (مودول التطبيق)، أضف:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

هنا دليل خطوة بخطوة:

1. **تعريف فئة الحدث**
إنشاء فئة POJO بسيطة لتمثيل حدثك:

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

2. **تسجيل المشترك**
في نشاطك/Fragment حيث تريد استلام الأحداث:

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // تسجيل في EventBus
        EventBus.getDefault().register(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // إلغاء التسجيل لمنع تسرب الذاكرة
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

3. **إرسال حدث**
من أي مكان في كودك (نشاط آخر، Fragment، خدمة، إلخ.):

```java
// إرسال حدث
EventBus.getDefault().post(new MessageEvent("مرحبًا من EventBus!"));
```

ميزات رئيسية وأختيارات:

- **خيارات ThreadMode**:
  - `ThreadMode.MAIN`: يعمل على الخيط الرئيسي لAndroid (الخيط المستخدم)
  - `ThreadMode.BACKGROUND`: يعمل على خيط خلفي
  - `ThreadMode.ASYNC`: يعمل في خيط منفصل
  - `ThreadMode.POSTING`: يعمل في نفس الخيط الذي أرسل منه

- **الأحداث اللاصقة**:
لأحداث تحتاج إلى البقاء للاشتراكات المتأخرة:

```java
// إرسال حدث لاصق
EventBus.getDefault().postSticky(new MessageEvent("رسالة لاصقة"));

// استلام الأحداث اللاصقة
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // معالجة الحدث اللاصق
}
```

- **الأولوية**:
تعيين الأولوية للمشتركين (عدد أكبر = أولوية أعلى):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // هذا المشترك لديه أولوية أعلى
}
```

أفضل الممارسات:
1. إلغاء التسجيل دائمًا في `onDestroy()` لمنع تسرب الذاكرة
2. استخدام فئات الأحداث المحددة بدلاً من الكائنات العامة
3. معالجة الاستثناءات في طرق المشتركين
4. التفكير في استخدام الأحداث اللاصقة لتغييرات التكوين
5. الحذر من إرسال الأحداث من الخيوط الخلفية إلى المشتركين في الواجهة

مثال بسيط مع مكونات متعددة:

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

// المستلم (مثل Activity)
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
        textView.setText("استلمت: " + event.getData());
    }
}
```

EventBus مفيد بشكل خاص ل:
- تفكيك المكونات
- التواصل بين الفragments
- تحديث الواجهة من العمليات الخلفية
- معالجة تغييرات التكوين

تذكر التعامل مع دورة الحياة بشكل صحيح واختبار تدفق الأحداث بشكل شامل!