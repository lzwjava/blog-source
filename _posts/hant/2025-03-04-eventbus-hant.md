---
audio: false
generated: true
lang: hant
layout: post
title: 在 Android 中使用 EventBus
translated: true
type: note
---

我將解釋如何在 Android 中使用 EventBus，這是一個流行的發布/訂閱事件匯流排函式庫，能簡化元件（如 Activity、Fragment 和背景執行緒）之間的通訊。

首先，將 EventBus 依賴項添加到你的專案中。在 `build.gradle`（app 模組）中加入：

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

以下是逐步指南：

1. **定義事件類別**
建立一個簡單的 POJO 類別來代表你的事件：

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
在你要接收事件的 Activity/Fragment 中：

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
        // 取消註冊以避免記憶體洩漏
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
從程式碼的任何地方（另一個 Activity、Fragment、Service 等）：

```java
// 發布事件
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

主要功能和選項：

- **ThreadMode 選項**：
  - `ThreadMode.MAIN`：在 Android 主執行緒（UI 執行緒）上運行
  - `ThreadMode.BACKGROUND`：在背景執行緒上運行
  - `ThreadMode.ASYNC`：在單獨的執行緒中執行
  - `ThreadMode.POSTING`：在與發布者相同的執行緒中運行

- **Sticky 事件**：
適用於需要持續存在以供後續訂閱者使用的事件：

```java
// 發布 sticky 事件
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// 接收 sticky 事件
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // 處理 sticky 事件
}
```

- **優先級**：
為訂閱者設定優先級（數字越大優先級越高）：

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // 此訂閱者擁有較高優先級
}
```

最佳實踐：
1. 始終在 `onDestroy()` 中取消註冊以避免記憶體洩漏
2. 使用特定事件類別而非通用物件
3. 在訂閱者方法中處理異常
4. 考慮使用 sticky 事件處理配置變更
5. 注意從背景執行緒向 UI 訂閱者發布事件的情況

多元件簡單範例：

```java
// 事件類別
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// 發送者（例如 Fragment）
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// 接收者（例如 Activity）
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

EventBus 特別適用於：
- 解耦元件
- Fragment 之間的通訊
- 從背景操作更新 UI
- 處理配置變更

請記住妥善處理生命週期並徹底測試你的事件流程！