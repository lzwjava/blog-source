---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von EventBus in Android
translated: true
type: note
---

Ich erkläre, wie man EventBus in Android verwendet, eine beliebte Publish/Subscribe-Event-Bus-Bibliothek, die die Kommunikation zwischen Komponenten wie Activities, Fragments und Hintergrund-Threads vereinfacht.

Fügen Sie zunächst die EventBus-Abhängigkeit zu Ihrem Projekt hinzu. In Ihrer `build.gradle` (App-Modul) fügen Sie hinzu:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

Hier ist eine Schritt-für-Schritt-Anleitung:

1. **Definieren Sie eine Event-Klasse**
Erstellen Sie eine einfache POJO-Klasse, die Ihr Event repräsentiert:

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
In Ihrer Activity/Fragment, in der Sie Events empfangen möchten:

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // Bei EventBus registrieren
        EventBus.getDefault().register(this);
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Abmelden, um Memory Leaks zu vermeiden
        EventBus.getDefault().unregister(this);
    }
    
    // Subscriber-Methode
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // Verarbeiten Sie das Event
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **Posten Sie ein Event**
Von überall in Ihrem Code (einer anderen Activity, Fragment, Service, etc.):

```java
// Ein Event posten
EventBus.getDefault().post(new MessageEvent("Hallo von EventBus!"));
```

Wichtige Funktionen und Optionen:

- **ThreadMode-Optionen**:
  - `ThreadMode.MAIN`: Läuft auf dem Android-Hauptthread (UI-Thread)
  - `ThreadMode.BACKGROUND`: Läuft in einem Hintergrund-Thread
  - `ThreadMode.ASYNC`: Führt in einem separaten Thread aus
  - `ThreadMode.POSTING`: Läuft im selben Thread wie der Poster

- **Sticky Events**:
Für Events, die für späte Subscriber bestehen bleiben müssen:

```java
// Ein Sticky-Event posten
EventBus.getDefault().postSticky(new MessageEvent("Sticky-Nachricht"));

// Sticky-Events empfangen
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // Sticky-Event verarbeiten
}
```

- **Priorität**:
Setzen Sie die Priorität für Subscriber (höhere Zahl = höhere Priorität):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // Dieser Subscriber hat eine höhere Priorität
}
```

Bewährte Methoden:
1. Immer in `onDestroy()` abmelden, um Memory Leaks zu vermeiden
2. Verwenden Sie spezifische Event-Klassen anstatt generischer Objekte
3. Behandeln Sie Ausnahmen in Subscriber-Methoden
4. Erwägen Sie die Verwendung von Sticky Events für Konfigurationsänderungen
5. Seien Sie vorsichtig beim Posten von Events aus Hintergrund-Threads zu UI-Subscribern

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
- Entkopplung von Komponenten
- Kommunikation zwischen Fragments
- Aktualisieren der UI aus Hintergrundoperationen
- Behandlung von Konfigurationsänderungen

Denken Sie daran, den Lebenszyklus korrekt zu handhaben und Ihre Event-Flüsse gründlich zu testen!