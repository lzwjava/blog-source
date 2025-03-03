---
audio: false
generated: true
lang: hi
layout: post
title: EventBus का उपयोग Android में
translated: true
---

मैं EventBus का उपयोग Android में समझाने जा raha hoon, एक लोकप्रिय प्रकाशित/सब्सक्राइब इवेंट बस लाइब्रेरी जो एक्टिविटीज, फ्रैगमेंट्स और बैकग्राउंड थ्रेड्स जैसे घटकों के बीच संचार को सरल बनाती है।

पहले, अपने प्रोजेक्ट में EventBus निर्भरता जोड़ें। अपने `build.gradle` (app module) में शामिल करें:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

यह एक कदम-द्र-कदम मार्गदर्शिका है:

1. **इवेंट क्लास परिभाषित करें**
एक सरल POJO क्लास बनाएं जो आपकी इवेंट को प्रतिनिधित्व करे:

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

2. **सब्सक्राइबर पंजीकृत करें**
अपने एक्टिविटी/फ्रैगमेंट में जहां आप इवेंट प्राप्त करना चाहते हैं:

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // EventBus में पंजीकृत करें
        EventBus.getDefault().register(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // स्मृति लीक को रोकने के लिए अनपंजीकृत करें
        EventBus.getDefault().unregister(this);
    }

    // सब्सक्राइबर विधि
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // इवेंट को संभालें
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **एक इवेंट पोस्ट करें**
अपने कोड के किसी भी हिस्से से (अन्य एक्टिविटी, फ्रैगमेंट, सर्विस आदि):

```java
// एक इवेंट पोस्ट करें
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

मुख्य विशेषताएं और विकल्प:

- **ThreadMode विकल्प**:
  - `ThreadMode.MAIN`: एंड्रॉइड के मुख्य थ्रेड (UI थ्रेड) पर चलता है
  - `ThreadMode.BACKGROUND`: बैकग्राउंड थ्रेड पर चलता है
  - `ThreadMode.ASYNC`: अलग थ्रेड में किया जाता है
  - `ThreadMode.POSTING`: पोस्टर के साथ ही थ्रेड में चलता है

- **स्टिकी इवेंट्स**:
लेट सब्सक्राइबर्स के लिए इवेंटों को स्थायी बनाएं:

```java
// एक स्टिकी इवेंट पोस्ट करें
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// स्टिकी इवेंट प्राप्त करें
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // स्टिकी इवेंट को संभालें
}
```

- **प्राथमिकता**:
सब्सक्राइबर्स के लिए प्राथमिकता सेट करें (उच्च संख्या = उच्च प्राथमिकता):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // इस सब्सक्राइबर की उच्च प्राथमिकता है
}
```

सर्वोत्तम प्रथाएं:
1. हमेशा `onDestroy()` में अनपंजीकृत करें स्मृति लीक को रोकने के लिए
2. विशिष्ट इवेंट क्लासों का उपयोग करें, सामान्य वस्तुओं के बजाय
3. सब्सक्राइबर विधियों में अपवादों को संभालें
4. स्टिकी इवेंटों का विचार करें कनफिगरेशन बदलावों के लिए
5. बैकग्राउंड थ्रेड से UI सब्सक्राइबर्स को इवेंट पोस्ट करने में सावधान रहें

एक सरल उदाहरण कई घटकों के साथ:

```java
// इवेंट क्लास
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// सेंडर (उदाहरण के लिए, फ्रैगमेंट)
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// रिसीवर (उदाहरण के लिए, एक्टिविटी)
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
        textView.setText("प्राप्त: " + event.getData());
    }
}
```

EventBus विशेष रूप से उपयोगी है:
- घटकों को अलग करना
- फ्रैगमेंट्स के बीच संचार करना
- बैकग्राउंड ऑपरेशन से UI को अपडेट करना
- कनफिगरेशन बदलावों को संभालना

लाइफसाइकल को सही से संभालें और अपने इवेंट फ्लो को पूरी तरह से परीक्षण करें!