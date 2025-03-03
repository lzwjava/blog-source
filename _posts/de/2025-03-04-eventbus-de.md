---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von EventBus in Android
translated: true
---

Ich erkläre, wie man EventBus in Android verwendet, eine beliebte Publish/Subscribe-Eventbus-Bibliothek, die die Kommunikation zwischen Komponenten wie Activities, Fragments und Hintergrundthreads vereinfacht.

Zuerst fügen Sie die EventBus-Abhängigkeit zu Ihrem Projekt hinzu. In Ihrer `build.gradle` (App-Modul) einschließen:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

Hier ist eine Schritt-für-Schritt-Anleitung:

1. **Definieren Sie eine Event-Klasse**
Erstellen Sie eine einfache POJO-Klasse, um Ihr Event darzustellen:

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

2. **Registrieren Sie einen Subscriber**
In Ihrer Activity/Fragment, wo Sie Events empfangen möchten:

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Registrieren Sie sich bei EventBus
        EventBus.getDefault().register(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Abmelden, um Speicherlecks zu verhindern
        EventBus.getDefault().unregister(this);
    }

    // Subscriber-Methode
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // Event verarbeiten
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **Senden Sie ein Event**
Von überall in Ihrem Code (eine andere Activity, Fragment, Service, etc.):

```java
// Senden Sie ein Event
EventBus.getDefault().post(new MessageEvent("Hallo von EventBus!"));
```

Wichtige Funktionen und Optionen:

- **ThreadMode-Optionen**:
  - `ThreadMode.MAIN`: Wird auf Androids Hauptthread (UI-Thread) ausgeführt
  - `ThreadMode.BACKGROUND`: Wird auf einem Hintergrundthread ausgeführt
  - `ThreadMode.ASYNC`: Wird in einem separaten Thread ausgeführt
  - `ThreadMode.POSTING`: Wird im gleichen Thread wie der Absender ausgeführt

- **Sticky Events**:
Für Events, die für verspätete Subscriber bestehen bleiben müssen:

```java
// Ein Sticky-Event senden
EventBus.getDefault().postSticky(new MessageEvent("Sticky Nachricht"));

// Empfangen von Sticky-Events
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // Sticky-Event verarbeiten
}
```

- **Priorität**:
Legen Sie die Priorität für Subscriber fest (höhere Zahl = höhere Priorität):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // Dieser Subscriber hat eine höhere Priorität
}
```

Best Practices:
1. Melden Sie sich immer in `onDestroy()` ab, um Speicherlecks zu vermeiden
2. Verwenden Sie spezifische Event-Klassen anstelle von generischen Objekten
3. Behandeln Sie Ausnahmen in Subscriber-Methoden
4. Überlegen Sie, Sticky-Events für Konfigurationsänderungen zu verwenden
5. Seien Sie vorsichtig beim Senden von Events von Hintergrundthreads an UI-Subscriber

Einfaches Beispiel mit mehreren Komponenten:

```java
// Event-Klasse
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// Sender (z.B. Fragment)
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// Empfänger (z.B. Activity)
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
        textView.setText("Empfangen: " + event.getData());
    }
}
```

EventBus ist besonders nützlich für:
- Entkoppeln von Komponenten
- Kommunikation zwischen Fragments
- Aktualisieren der UI von Hintergrundoperationen
- Verarbeiten von Konfigurationsänderungen

Denken Sie daran, den Lebenszyklus ordnungsgemäß zu verwalten und Ihre Event-Flüsse gründlich zu testen!