---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation d'EventBus dans Android
translated: true
---

Je vais expliquer comment utiliser EventBus dans Android, une bibliothèque de bus d'événements populaire de publication/abonnement qui simplifie la communication entre des composants comme les Activities, les Fragments et les threads en arrière-plan.

Tout d'abord, ajoutez la dépendance EventBus à votre projet. Dans votre `build.gradle` (module app), incluez :

```gradle
implementation 'org.greenrobot:eventbus:3.3.1'
```

Voici un guide étape par étape :

1. **Définir une classe d'événement**
Créez une simple classe POJO pour représenter votre événement :

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

2. **Enregistrer un abonné**
Dans votre Activity/Fragment où vous souhaitez recevoir des événements :

```java
import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // S'enregistrer à EventBus
        EventBus.getDefault().register(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Se désenregistrer pour éviter les fuites de mémoire
        EventBus.getDefault().unregister(this);
    }

    // Méthode d'abonné
    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onMessageEvent(MessageEvent event) {
        // Gérer l'événement
        Toast.makeText(this, event.getMessage(), Toast.LENGTH_SHORT).show();
    }
}
```

3. **Publier un événement**
Depuis n'importe où dans votre code (une autre Activity, Fragment, Service, etc.) :

```java
// Publier un événement
EventBus.getDefault().post(new MessageEvent("Hello from EventBus!"));
```

Caractéristiques clés et options :

- **Options ThreadMode** :
  - `ThreadMode.MAIN` : S'exécute sur le thread principal d'Android (thread UI)
  - `ThreadMode.BACKGROUND` : S'exécute sur un thread en arrière-plan
  - `ThreadMode.ASYNC` : S'exécute dans un thread séparé
  - `ThreadMode.POSTING` : S'exécute dans le même thread que l'expéditeur

- **Événements collants** :
Pour les événements qui doivent persister pour les abonnés tardifs :

```java
// Publier un événement collant
EventBus.getDefault().postSticky(new MessageEvent("Message collant"));

// Recevoir des événements collants
@Subscribe(sticky = true, threadMode = ThreadMode.MAIN)
public void onStickyEvent(MessageEvent event) {
    // Gérer l'événement collant
}
```

- **Priorité** :
Définir la priorité pour les abonnés (nombre plus élevé = priorité plus élevée) :

```java
@Subscribe(threadMode = ThreadMode.MAIN, priority = 1)
public void onMessageEvent(MessageEvent event) {
    // Cet abonné a une priorité plus élevée
}
```

Bonnes pratiques :
1. Toujours se désenregistrer dans `onDestroy()` pour éviter les fuites de mémoire
2. Utiliser des classes d'événements spécifiques plutôt que des objets génériques
3. Gérer les exceptions dans les méthodes d'abonné
4. Envisager d'utiliser des événements collants pour les changements de configuration
5. Faire attention à la publication d'événements depuis des threads en arrière-plan vers des abonnés UI

Exemple simple avec plusieurs composants :

```java
// Classe d'événement
public class DataEvent {
    private int data;
    public DataEvent(int data) { this.data = data; }
    public int getData() { return data; }
}

// Expéditeur (par exemple, Fragment)
public class SenderFragment extends Fragment {
    private void sendData() {
        EventBus.getDefault().post(new DataEvent(42));
    }
}

// Récepteur (par exemple, Activity)
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
        textView.setText("Reçu : " + event.getData());
    }
}
```

EventBus est particulièrement utile pour :
- Découpler les composants
- Communiquer entre fragments
- Mettre à jour l'UI depuis des opérations en arrière-plan
- Gérer les changements de configuration

N'oubliez pas de gérer le cycle de vie correctement et de tester vos flux d'événements de manière approfondie !