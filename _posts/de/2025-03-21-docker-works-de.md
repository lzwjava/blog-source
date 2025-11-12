---
audio: false
generated: true
lang: de
layout: post
title: Wie Docker Funktioniert
translated: true
type: note
---

Lassen Sie uns untersuchen, wie Docker funktioniert, mit einem Fokus auf die Nutzung des Linux-Dateisystems und wie es Anwendungen voneinander isoliert.

---

### Was ist Docker im Kern?
Docker ist eine Plattform, die es Ihnen ermöglicht, Anwendungen in leichtgewichtigen, isolierten Umgebungen, sogenannten **Containern**, zu verpacken, zu verteilen und auszuführen. Im Gegensatz zu virtuellen Maschinen (VMs), die ein vollständiges Betriebssystem enthalten, teilen sich Docker-Container den Host-OS-Kernel und nutzen dessen Funktionen, um Isolierung und Effizienz zu gewährleisten.

---

### Wie Docker funktioniert
Docker nutzt mehrere Linux-Kernel-Funktionen, um Container zu erstellen und zu verwalten:
1.  **Namespaces** - Zur Isolierung.
2.  **Control Groups (cgroups)** - Für das Ressourcen-Management.
3.  **Union Filesystems** - Für effiziente Speicherung und Layering.

So fügen sich diese Teile zusammen:

---

#### 1. Linux-Namespaces: Isolierungsmechanismus
Namespaces erstellen isolierte "Sichten" auf Systemressourcen und stellen sicher, dass Prozesse in einem Container nicht die in einem anderen beeinträchtigen. Wichtige Namespaces, die Docker verwendet, sind:

-   **PID-Namespace**: Jeder Container hat seinen eigenen Prozess-ID-Bereich. Die Prozess-ID 1 innerhalb eines Containers ist von der PID 1 des Hosts (normalerweise `init` oder `systemd`) isoliert.
-   **Network-Namespace**: Container erhalten ihren eigenen Netzwerk-Stack (IP-Adresse, Ports, Routing-Tabellen). Deshalb können zwei Container ohne Konflikt auf Port 8080 lauschen.
-   **Mount-Namespace**: Jeder Container hat seine eigene Sicht auf das Dateisystem, isoliert vom Host und anderen Containern.
-   **UTS-Namespace**: Container können ihren eigenen Hostnamen und Domänennamen haben.
-   **IPC-Namespace**: Isoliert die Interprozesskommunikation (z.B. Shared Memory, Message Queues).
-   **User-Namespace** (optional): Ordnet Container-Benutzer Host-Benutzern zu und erhöht so die Sicherheit.

**Beispiel**: Wenn Sie `ps` innerhalb eines Containers ausführen, sehen Sie nur Prozesse innerhalb des PID-Namespaces dieses Containers, nicht die Prozesse des Hosts.

---

#### 2. Control Groups (cgroups): Ressourcenbegrenzungen
Cgroups begrenzen und überwachen die Ressourcennutzung (CPU, Speicher, Disk I/O usw.) für jeden Container. Dies verhindert, dass ein Container alle Systemressourcen beansprucht und andere aushungert.

-   **Wie es funktioniert**: Docker weist jedem Container eine Cgroup zu. Sie können Limits setzen wie:
    ```bash
    docker run --memory="512m" --cpus="0.5" myapp
    ```
    Dies beschränkt den Container auf 512 MB RAM und einen halben CPU-Kern.

-   **Isolierung**: Während Namespaces die Sichtbarkeit isolieren, isolieren Cgroups den Ressourcenverbrauch.

---

#### 3. Union Filesystems: Geschichteter Speicher
Docker verwendet ein **Union Filesystem** (z.B. OverlayFS, AUFS), um Container-Images und deren Dateisysteme effizient zu verwalten. So bindet es sich in das Linux-Dateisystem ein:

-   **Image-Layer**: Ein Docker-Image besteht aus gestapelten, schreibgeschützten Layern. Jeder Layer repräsentiert eine Reihe von Änderungen (z.B. das Installieren eines Pakets, das Kopieren von Dateien), die in Ihrer `Dockerfile` definiert sind.
    -   Beispiel: `FROM openjdk:17` ist ein Layer, `COPY app.jar` fügt einen weiteren hinzu.
    -   Layer werden zwischengespeichert und wiederverwendet, was Speicherplatz spart und Builds beschleunigt.

-   **Container-Dateisystem**: Wenn Sie einen Container starten, fügt Docker einen dünnen, beschreibbaren Layer oben auf die schreibgeschützten Image-Layer. Dies wird als **Copy-on-Write (CoW)**-Mechanismus bezeichnet:
    -   Lesevorgänge kommen aus den Image-Layern.
    -   Schreibvorgänge (z.B. Log-Dateien, temporäre Daten) gehen an den beschreibbaren Layer.
    -   Wenn eine Datei in einem unteren Layer modifiziert wird, wird sie zuerst in den beschreibbaren Layer kopiert (daher "Copy-on-Write").

-   **Isolierung**: Jeder Container erhält seinen eigenen beschreibbaren Layer, sodass Änderungen in einem Container andere nicht beeinflussen, selbst wenn sie dasselbe Basis-Image teilen.

-   **Auf der Festplatte**: Auf dem Host werden diese Layer in `/var/lib/docker` gespeichert (z.B. `/var/lib/docker/overlay2` für OverlayFS). Sie interagieren nicht direkt damit – Docker verwaltet dies.

---

### Wie Apps voneinander isoliert werden
So arbeiten die oben genannten Komponenten zusammen, um Anwendungen zu isolieren:

1.  **Prozessisolierung (PID-Namespace)**:
    -   Jeder Container führt seine App als einen unabhängigen Prozessbaum aus, der andere Container oder den Host nicht kennt.

2.  **Netzwerkisolierung (Network-Namespace)**:
    -   Container haben separate Netzwerkschnittstellen. Das standardmäßige "Bridge"-Netzwerk von Docker weist jedem Container eine eindeutige IP zu, und NAT übernimmt die externe Kommunikation.
    -   Beispiel: Zwei Spring Boot-Apps können beide an Port 8080 innerhalb ihrer Container binden, ohne dass es zu einem Konflikt kommt.

3.  **Dateisystemisolierung (Mount-Namespace + UnionFS)**:
    -   Jeder Container sieht nur sein eigenes Dateisystem, das aus den Image-Layern plus seinem beschreibbaren Layer aufgebaut ist.
    -   Wenn Container A in `/tmp` schreibt, sieht Container B es nicht.

4.  **Ressourcenisolierung (cgroups)**:
    -   Eine App kann nicht die CPU oder den Speicher des Hosts erschöpfen und eine andere zum Absturz bringen.

5.  **Gemeinsamer Kernel**:
    -   Container teilen sich den Linux-Kernel des Hosts, aber Namespaces stellen sicher, dass sie sich nicht gegenseitig stören. Systemaufrufe werden nach Bedarf gefiltert oder umgeleitet.

---

### Vereinfachter Workflow
1.  **Build**: Sie erstellen ein Image mit einem `Dockerfile`, das die App und ihre Abhängigkeiten definiert. Docker stapelt diese mithilfe eines Union Filesystems in Layer.
2.  **Run**: Docker erstellt einen Container, indem es:
    -   Namespaces für die Isolierung einrichtet.
    -   Cgroups für Ressourcenlimits zuweist.
    -   Die Image-Layers plus einen beschreibbaren Layer einhängt.
    -   Ihre App als Entrypoint startet (z.B. `java -jar app.jar`).
3.  **Cleanup**: Wenn der Container stoppt, wird der beschreibbare Layer verworfen (es sei denn, er wird mit `docker commit` als neues Image gespeichert).

---

### Warum Linux?
Docker ist auf Linux-Kernel-Funktionen (Namespaces, Cgroups, Union Filesystems) angewiesen, die tief in dessen Funktionsweise integriert sind. Unter macOS oder Windows führt Docker eine leichtgewichtige Linux-VM (über HyperKit oder WSL2) aus, um diese Fähigkeiten bereitzustellen, und bildet sie dann auf das Host-Betriebssystem ab.

---

### Visuelle Analogie
Stellen Sie sich Docker-Container als Wohnungen in einem Gebäude vor:
-   **Namespaces**: Wände und Türen halten die Bewohner getrennt.
-   **Cgroups**: Der Vermieter begrenzt Wasser oder Strom pro Einheit.
-   **UnionFS**: Alle Wohnungen teilen einen gemeinsamen Bauplan (Image-Layer), aber jeder Mieter kann seinen Raum dekorieren (beschreibbarer Layer).

---

Klärt dies, wie Docker funktioniert und Apps isoliert? Lassen Sie es mich wissen, wenn Sie einen tieferen Einblick in einen bestimmten Teil wünschen!