---
audio: false
generated: true
lang: hi
layout: post
title: एंड्रॉइड में इवेंटबस का उपयोग
translated: true
type: note
---

मैं Android में EventBus के उपयोग के बारे में समझाऊंगा, जो एक लोकप्रिय publish/subscribe event bus लाइब्रेरी है जो Activities, Fragments, और background threads जैसे components के बीच communication को सरल बनाती है।

सबसे पहले, अपने प्रोजेक्ट में EventBus dependency जोड़ें। अपने `build.gradle` (app module) में, शामिल करें:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

यहां एक चरण-दर-चरण मार्गदर्शिका है:

1. **एक Event Class परिभाषित करें**
अपने event को represent करने के लिए एक साधारण POJO class बनाएं:

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

2. **Subscriber को पंजीकृत करें**
अपनी Activity/Fragment में जहां आप events प्राप्त करना चाहते हैं:

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // EventBus के लिए पंजीकरण करें
        EventBus.getDefault().register(this);
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Memory leaks से बचने के लिए अनपंजीकृत करें
        EventBus.getDefault().unregister(this);
    }
    
    // Subscriber method
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // Event को संभालें
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **एक Event पोस्ट करें**
अपने code में कहीं से भी (दूसरी Activity, Fragment, Service, आदि):

```java
// एक event पोस्ट करें
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

मुख्य विशेषताएं और विकल्प:

- **ThreadMode विकल्प**:
  - `ThreadMode.MAIN`: Android के main thread (UI thread) पर चलता है
  - `ThreadMode.BACKGROUND`: एक background thread पर चलता है
  - `ThreadMode.ASYNC`: एक अलग thread में कार्य करता है
  - `ThreadMode.POSTING`: poster के समान thread में चलता है

- **Sticky Events**:
ऐसे events के लिए जिन्हें late subscribers के लिए बनाए रखने की आवश्यकता है:

```java
// एक sticky event पोस्ट करना
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// Sticky events प्राप्त करना
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // Sticky event को संभालें
}
```

- **प्राथमिकता**:
Subscribers के लिए प्राथमिकता निर्धारित करें (उच्च संख्या = उच्च प्राथमिकता):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // इस subscriber की उच्च प्राथमिकता है
}
```

सर्वोत्तम अभ्यास:
1. Memory leaks से बचने के लिए हमेशा `onDestroy()` में अनपंजीकृत करें
2. सामान्य objects के बजाय विशिष्ट event classes का उपयोग करें
3. Subscriber methods में exceptions को संभालें
4. Configuration changes के लिए sticky events का उपयोग करने पर विचार करें
5. UI subscribers को background threads से event पोस्ट करने में सावधानी बरतें

कई Components के साथ सरल उदाहरण:

```java
// Event Class
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// Sender (उदाहरण के लिए, Fragment)
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// Receiver (उदाहरण के लिए, Activity)
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

EventBus विशेष रूप से उपयोगी है:
- Components को अलग करने के लिए
- Fragments के बीच communication के लिए
- Background operations से UI को अपडेट करने के लिए
- Configuration changes को संभालने के लिए

Lifecycle को ठीक से संभालना याद रखें और अपने event flows का पूरी तरह से परीक्षण करें!