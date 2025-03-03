---
audio: false
generated: true
lang: hant
layout: post
title: 使用 EventBus 在 Android
translated: true
---

我將解釋如何在 Android 中使用 EventBus，這是一個流行的發布/訂閱事件總線庫，簡化了活動、片段和後台線程之間的通信。

首先，將 EventBus 依賴項添加到您的項目中。在您的 `build.gradle`（應用模組）中包含：

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

以下是逐步指南：

1. **定義事件類**
創建一個簡單的 POJO 類來表示您的事件：

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

2. **註冊訂閱者**
在您想要接收事件的 Activity/Fragment 中：

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 註冊到 EventBus
        EventBus.getDefault().register(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 取消註冊以防止記憶體洩漏
        EventBus.getDefault().unregister(this);
    }

    // 訂閱者方法
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // 處理事件
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **發布事件**
從代碼的任何地方（另一個 Activity、Fragment、Service 等）：

```java
// 發布事件
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

主要功能和選項：

- **ThreadMode 選項**：
  - `ThreadMode.MAIN`：在 Android 的主線程（UI 線程）上運行
  - `ThreadMode.BACKGROUND`：在後台線程上運行
  - `ThreadMode.ASYNC`：在單獨的線程中執行
  - `ThreadMode.POSTING`：在發布者的同一線程中運行

- **粘性事件**：
對於需要持久化的事件：

```java
// 發布粘性事件
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// 接收粘性事件
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // 處理粘性事件
}
```

- **優先級**：
設置訂閱者的優先級（數字越高優先級越高）：

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // 這個訂閱者優先級較高
}
```

最佳實踐：
1. 總是在 `onDestroy()` 中取消註冊以避免記憶體洩漏
2. 使用特定的事件類而不是通用對象
3. 在訂閱者方法中處理例外
4. 考慮使用粘性事件來處理配置變更
5. 小心從後台線程發布事件到 UI 訂閱者

簡單示例與多個組件：

```java
// 事件類
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// 發送者（例如，Fragment）
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// 接收者（例如，Activity）
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

EventBus 特別適合：
- 解耦組件
- 片段之間的通信
- 從後台操作更新 UI
- 處理配置變更

記住要正確處理生命週期並彻底測試您的事件流程！