---
audio: false
generated: true
lang: ja
layout: post
title: AndroidでのEventBusの使用
translated: true
type: note
---

Androidで人気のあるパブリッシュ/サブスクライブイベントバスライブラリであるEventBusの使用方法について説明します。このライブラリは、Activity、Fragment、バックグラウンドスレッドなどのコンポーネント間の通信を簡素化します。

まず、プロジェクトにEventBusの依存関係を追加します。`build.gradle`（appモジュール）に以下を記述します：

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

ステップバイステップガイド：

1. **イベントクラスの定義**
シンプルなPOJOクラスを作成してイベントを表現します：

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

2. **サブスクライバーの登録**
イベントを受信したいActivity/Fragmentで：

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // EventBusに登録
        EventBus.getDefault().register(this);
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        // メモリリークを防ぐために登録解除
        EventBus.getDefault().unregister(this);
    }
    
    // サブスクライバーメソッド
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // イベントを処理
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **イベントの投稿**
コード内のどこからでも（別のActivity、Fragment、Serviceなど）：

```java
// イベントを投稿
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

主な機能とオプション：

- **ThreadModeオプション**：
  - `ThreadMode.MAIN`：Androidのメインスレッド（UIスレッド）で実行
  - `ThreadMode.BACKGROUND`：バックグラウンドスレッドで実行
  - `ThreadMode.ASYNC`：別のスレッドで実行
  - `ThreadMode.POSTING`：投稿者と同じスレッドで実行

- **Stickyイベント**：
遅れて参加するサブスクライバーのために永続化する必要があるイベント：

```java
// Stickyイベントの投稿
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// Stickyイベントの受信
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // Stickyイベントを処理
}
```

- **優先度**：
サブスクライバーの優先度を設定（数値が大きいほど優先度が高い）：

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // このサブスクライバーはより高い優先度を持ちます
}
```

ベストプラクティス：
1. メモリリークを避けるために`onDestroy()`で必ず登録解除する
2. 汎用的なオブジェクトではなく、特定のイベントクラスを使用する
3. サブスクライバーメソッドで例外を処理する
4. 設定変更にはStickyイベントの使用を検討する
5. バックグラウンドスレッドからUIサブスクライバーへのイベント投稿には注意する

複数コンポーネントを使用したシンプルな例：

```java
// イベントクラス
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// 送信側（例：Fragment）
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// 受信側（例：Activity）
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
        textView.setText("受信: " + event.getData());
    }
}
```

EventBusは特に以下の場合に有用です：
- コンポーネントの分離
- Fragment間の通信
- バックグラウンド操作からのUI更新
- 設定変更の処理

ライフサイクルを適切に処理し、イベントフローを十分にテストすることを忘れないでください！