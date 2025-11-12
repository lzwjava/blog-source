---
audio: false
generated: true
lang: de
layout: post
title: Virtuelle Threads
translated: true
type: note
---

Virtuelle Threads, eingeführt in Java 19 als Teil von Project Loom, bieten eine leichtgewichtige Alternative zu traditionellen Plattform-Threads. Sie sind darauf ausgelegt, die Skalierbarkeit und Effizienz von Anwendungen zu verbessern, indem der Overhead bei der Thread-Verwaltung reduziert wird.

Um Virtuelle Threads mit Spring zu verwenden, müssen Sie sicherstellen, dass Ihre Umgebung für die Unterstützung von Java 19 oder höher eingerichtet ist, da Virtuelle Threads ein Feature dieser Versionen sind. Hier ist eine allgemeine Anleitung zur Integration von Virtuellen Threads in eine Spring-Anwendung:

### 1. **Richten Sie Ihre Umgebung ein**

- **Java-Version**: Stellen Sie sicher, dass Sie Java 19 oder höher verwenden. Sie können Ihre Java-Version mit `java -version` überprüfen.
- **Spring Boot Version**: Stellen Sie sicher, dass Sie eine Version von Spring Boot verwenden, die Java 19 oder höher unterstützt.

### 2. **Aktivieren Sie Virtuelle Threads**

Virtuelle Threads können in Ihrer Spring-Anwendung verwendet werden, indem Sie Ihre Anwendung für deren Nutzung konfigurieren. So können Sie dies tun:

#### **a. Executor Service konfigurieren**

Sie können einen `ExecutorService` so konfigurieren, dass er Virtuelle Threads verwendet. Dies kann in Ihrer Spring-Konfigurationsklasse erfolgen:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class VirtualThreadConfig {

    @Bean
    public ExecutorService virtualThreadExecutor() {
        return Executors.newVirtualThreadPerTaskExecutor();
    }
}
```

#### **b. Verwenden Sie Virtuelle Threads in Ihrem Service**

Sie können diesen `ExecutorService` dann in Ihre Spring Services injecten und verwenden, um Tasks mit Virtuellen Threads auszuführen:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.concurrent.ExecutorService;

@Service
public class MyService {

    private final ExecutorService executorService;

    @Autowired
    public MyService(ExecutorService executorService) {
        this.executorService = executorService;
    }

    public void executeTask() {
        executorService.submit(() -> {
            // Ihre Task-Logik hier
            System.out.println("Task executed on a virtual thread: " + Thread.currentThread());
        });
    }
}
```

### 3. **Testen Sie Virtuelle Threads**

Um zu testen, ob Virtuelle Threads verwendet werden, können Sie die Thread-Informationen protokollieren. Virtuelle Threads haben Namen, die darauf hinweisen, dass sie virtuell sind, wie z.B. `VirtualThread[#<id>]`.

### 4. **Zu beachtende Punkte**

- **Kompatibilität**: Stellen Sie sicher, dass alle verwendeten Bibliotheken und Frameworks mit Java 19 oder höher kompatibel sind.
- **Performance**: Virtuelle Threads sind zur Verbesserung der Skalierbarkeit konzipiert, dennoch sollten Sie Ihre Anwendung profilieren, um sicherzustellen, dass sie die erwarteten Leistungsvorteile bieten.
- **Blockierende Operationen**: Virtuelle Threads sind besonders vorteilhaft für I/O-bound Tasks. Stellen Sie sicher, dass Ihre Anwendung darauf ausgelegt ist, dies auszunutzen.

Indem Sie diese Schritte befolgen, können Sie Virtuelle Threads in Ihre Spring-Anwendung integrieren und von deren Skalierbarkeitsvorteilen profitieren.