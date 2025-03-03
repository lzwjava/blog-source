---
audio: false
generated: true
lang: es
layout: post
title: Usando EventBus en Android
translated: true
---

Explicaré cómo usar EventBus en Android, una popular biblioteca de bus de eventos de publicación/suscripción que simplifica la comunicación entre componentes como Activities, Fragments y hilos en segundo plano.

Primero, agregue la dependencia de EventBus a su proyecto. En su `build.gradle` (módulo de la aplicación), incluya:

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

Aquí tiene una guía paso a paso:

1. **Definir una Clase de Evento**
Cree una clase POJO simple para representar su evento:

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

2. **Registrar Suscriptor**
En su Activity/Fragment donde desea recibir eventos:

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
        // Desregistrarse para evitar fugas de memoria
        EventBus.getDefault().unregister(this);
    }

    // Método del suscriptor
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // Manejar el evento
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **Publicar un Evento**
Desde cualquier parte de su código (otra Activity, Fragment, Service, etc.):

```java
// Publicar un evento
EventBus.getDefault().post(new MessageEvent("¡Hola desde EventBus!"));
```

Características Clave y Opciones:

- **Opciones de ThreadMode**:
  - `ThreadMode.MAIN`: Se ejecuta en el hilo principal de Android (hilo de la interfaz de usuario)
  - `ThreadMode.BACKGROUND`: Se ejecuta en un hilo en segundo plano
  - `ThreadMode.ASYNC`: Se realiza en un hilo separado
  - `ThreadMode.POSTING`: Se ejecuta en el mismo hilo que el publicador

- **Eventos Pegajosos**:
Para eventos que necesitan persistir para suscriptores tardíos:

```java
// Publicar un evento pegajoso
EventBus.getDefault().postSticky(new MessageEvent("Mensaje pegajoso"));

// Recibir eventos pegajosos
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // Manejar evento pegajoso
}
```

- **Prioridad**:
Establecer prioridad para suscriptores (número más alto = prioridad más alta):

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // Este suscriptor tiene una prioridad más alta
}
```

Mejores Prácticas:
1. Siempre desregistrarse en `onDestroy()` para evitar fugas de memoria
2. Usar clases de eventos específicas en lugar de objetos genéricos
3. Manejar excepciones en los métodos de suscripción
4. Considerar el uso de eventos pegajosos para cambios de configuración
5. Ser cauteloso con la publicación de eventos desde hilos en segundo plano a suscriptores de la interfaz de usuario

Ejemplo Simple con Múltiples Componentes:

```java
// Clase de Evento
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// Enviador (por ejemplo, Fragment)
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// Receptor (por ejemplo, Activity)
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
- Comunicarse entre fragmentos
- Actualizar la interfaz de usuario desde operaciones en segundo plano
- Manejar cambios de configuración

¡Recuerde manejar el ciclo de vida adecuadamente y probar sus flujos de eventos a fondo!