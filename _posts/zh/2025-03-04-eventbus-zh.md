---
audio: false
generated: true
lang: zh
layout: post
title: 使用 EventBus 在 Android 中
translated: true
---

我将解释如何在Android中使用EventBus，这是一个流行的发布/订阅事件总线库，简化了Activity、Fragment和后台线程等组件之间的通信。

首先，将EventBus依赖项添加到您的项目中。在您的`build.gradle`（应用模块）中包含：

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

以下是逐步指南：

1. **定义事件类**
创建一个简单的POJO类来表示您的事件：

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

2. **注册订阅者**
在您希望接收事件的Activity/Fragment中：

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 注册到EventBus
        EventBus.getDefault().register(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 取消注册以防止内存泄漏
        EventBus.getDefault().unregister(this);
    }

    // 订阅者方法
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // 处理事件
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **发布事件**
在代码的任何地方（另一个Activity、Fragment、Service等）：

```java
// 发布事件
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

关键功能和选项：

- **ThreadMode选项**：
  - `ThreadMode.MAIN`：在Android的主线程（UI线程）上运行
  - `ThreadMode.BACKGROUND`：在后台线程上运行
  - `ThreadMode.ASYNC`：在单独的线程中执行
  - `ThreadMode.POSTING`：在发布者的同一线程中运行

- **粘性事件**：
对于需要持久化以供晚订阅者使用的事件：

```java
// 发布粘性事件
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// 接收粘性事件
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // 处理粘性事件
}
```

- **优先级**：
为订阅者设置优先级（数字越大优先级越高）：

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // 此订阅者具有较高优先级
}
```

最佳实践：
1. 总是在`onDestroy()`中取消注册以避免内存泄漏
2. 使用特定的事件类而不是通用对象
3. 在订阅者方法中处理异常
4. 考虑使用粘性事件来处理配置更改
5. 从后台线程发布事件时要小心，以避免UI订阅者

使用多个组件的简单示例：

```java
// 事件类
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// 发送者（例如，Fragment）
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

EventBus特别适用于：
- 解耦组件
- 片段之间的通信
- 从后台操作更新UI
- 处理配置更改

记住正确处理生命周期并彻底测试您的事件流程！