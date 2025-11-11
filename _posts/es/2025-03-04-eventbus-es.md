---
audio: false
generated: true
lang: es
layout: post
title: Uso de EventBus en Android
translated: true
type: note
---

Explicaré cómo usar EventBus en Android, una popular librería de bus de eventos de publicación/suscripción que simplifica la comunicación entre componentes como Activities, Fragments e hilos en segundo plano.

Primero, añade la dependencia de EventBus a tu proyecto. En tu `build.gradle` (módulo de la app), incluye:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

Aquí tienes una guía paso a paso:

1. **Define una Clase de Evento**
Crea una simple clase POJO para representar tu evento:

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

2. **Registra el Suscriptor**
En tu Activity/Fragment donde quieras recibir eventos:

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // Registrarse en EventBus
        EventBus.getDefault().register(this);
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Anular el registro para prevenir fugas de memoria
        EventBus.getDefault().unregister(this);
    }
    
    // Método suscriptor
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // Manejar el evento
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **Publica un Evento**
Desde cualquier parte de tu código (otra Activity, Fragment, Service, etc.):

```java
// Publicar un evento
EventBus.getDefault().post(new MessageEvent("¡Hola desde EventBus!"));
```

Características y Opciones Clave:

- **Opciones de ThreadMode**:
  - `ThreadMode.MAIN`: Se ejecuta en el hilo principal de Android (hilo de UI)
  - `ThreadMode.BACKGROUND`: Se ejecuta en un hilo en segundo plano
  - `ThreadMode.ASYNC`: Se ejecuta en un hilo separado
  - `ThreadMode.POSTING`: Se ejecuta en el mismo hilo que el publicador

- **Eventos Persistentes (Sticky)**:
Para eventos que necesitan persistir para suscriptores tardíos:

```java
// Publicando un evento sticky
EventBus.getDefault().postSticky(new MessageEvent("Mensaje sticky"));

// Recibiendo eventos sticky
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // Manejar evento sticky
}
```

- **Prioridad**:
Establece prioridad para suscriptores (número mayor = mayor prioridad):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // Este suscriptor tiene mayor prioridad
}
```

Mejores Prácticas:
1. Siempre anula el registro en `onDestroy()` para evitar fugas de memoria
2. Usa clases de evento específicas en lugar de objetos genéricos
3. Maneja excepciones en los métodos suscriptores
4. Considera usar eventos sticky para cambios de configuración
5. Ten precaución al publicar eventos desde hilos en segundo plano a suscriptores de UI

Ejemplo Simple con Múltiples Componentes:

```java
// Clase de Evento
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// Emisor (ej., Fragment)
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// Receptor (ej., Activity)
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
        textView.setText("Recibido: " + event.getData());
    }
}
```

EventBus es particularmente útil para:
- Desacoplar componentes
- Comunicación entre fragments
- Actualizar la UI desde operaciones en segundo plano
- Manejar cambios de configuración

¡Recuerda manejar el ciclo de vida correctamente y probar tus flujos de eventos exhaustivamente!