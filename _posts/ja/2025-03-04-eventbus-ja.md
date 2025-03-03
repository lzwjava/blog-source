---
audio: false
generated: true
lang: ja
layout: post
title: イベントバスをAndroidで使用する
translated: true
---

Androidで人気のあるパブリッシュ/サブスクライブイベントバスライブラリであるEventBusの使い方を説明します。このライブラリは、Activity、Fragment、バックグラウンドスレッドなどのコンポーネント間の通信を簡素化します。

まず、プロジェクトにEventBusの依存関係を追加します。`build.gradle`（アプリモジュール）に以下を含めます：

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

以下にステップバイステップのガイドを示します：

1. **イベントクラスの定義**
イベントを表す簡単なPOJOクラスを作成します：

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
        // メモリリークを防ぐために登録を解除
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
コードの任意の場所（他のActivity、Fragment、Serviceなど）から：

```java
// イベントを投稿
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

主要な機能とオプション：

- **ThreadModeのオプション**：
  - `ThreadMode.MAIN`：Androidのメインスレッド（UIスレッド）で実行
  - `ThreadMode.BACKGROUND`：バックグラウンドスレッドで実行
  - `ThreadMode.ASYNC`：別スレッドで実行
  - `ThreadMode.POSTING`：投稿者と同じスレッドで実行

- **スティッキーイベント**：
遅れてサブスクライブするためにイベントを保持する場合：

```java
// スティッキーイベントを投稿
EventBus.getDefault().postSticky(new MessageEvent("Sticky message"));

// スティッキーイベントを受信
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // スティッキーイベントを処理
}
```

- **優先度**：
サブスクライバーの優先度を設定（数値が大きいほど優先度が高い）：

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // このサブスクライバーは優先度が高い
}
```

ベストプラクティス：
1. `onDestroy()`で常に登録を解除してメモリリークを防ぐ
2. 一般的なオブジェクトではなく特定のイベントクラスを使用する
3. サブスクライバーメソッドで例外を処理する
4. 設定変更のためにスティッキーイベントを検討する
5. バックグラウンドスレッドからUIサブスクライバーにイベントを投稿する際は注意する

複数のコンポーネントを使用した簡単な例：

```java
// イベントクラス
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// 送信元（例：Fragment）
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// 受信元（例：Activity）
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

EventBusは特に以下に役立ちます：
- コンポーネントの分離
- フラグメント間の通信
- バックグラウンド操作からのUI更新
- 設定変更の処理

ライフサイクルを適切に処理し、イベントフローを徹底的にテストすることを忘れないでください！