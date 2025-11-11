---
audio: false
generated: true
lang: es
layout: post
title: Docker contra Kubernetes
translated: true
type: note
---

Docker y Kubernetes son tecnologías complementarias en el ecosistema de contenedores, pero sirven para diferentes propósitos. Analicemos sus diferencias y cómo se relacionan.

---

### Docker: Plataforma de Contenedorización
**Qué hace**: Docker es una herramienta para crear, ejecutar y gestionar contenedores individuales—entornos ligeros y aislados que empaquetan una aplicación con sus dependencias.

#### Características Clave
1. **Runtime de Contenedores**:
   - Docker utiliza un runtime (por ejemplo, `containerd` o `runc`) para ejecutar contenedores basándose en características del kernel de Linux como namespaces y cgroups.
   - Es responsable del ciclo de vida de un contenedor individual: construir, iniciar, detener, etc.

2. **Gestión de Imágenes**:
   - Docker construye imágenes a partir de un `Dockerfile`, que define la aplicación, bibliotecas y configuraciones.
   - Las imágenes se almacenan en registros (por ejemplo, Docker Hub) y se ejecutan como contenedores.

3. **Enfoque en un Solo Host**:
   - Docker es excelente para gestionar contenedores en una sola máquina. Puedes ejecutar múltiples contenedores, pero la orquestación a través de múltiples hosts no está integrada.

4. **Basado en CLI**:
   - Comandos como `docker build`, `docker run` y `docker ps` te permiten interactuar directamente con los contenedores.

#### Caso de Uso
- Ejecutar una sola aplicación Spring Boot en tu portátil o en un servidor:
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```

#### Limitaciones
- Sin soporte nativo para múltiples hosts.
- Sin escalado automático, auto-reparación o balanceo de carga.
- Gestionar muchos contenedores manualmente se vuelve complicado.

---

### Kubernetes: Sistema de Orquestación de Contenedores
**Qué hace**: Kubernetes (a menudo abreviado como K8s) es una plataforma para gestionar y orquestar múltiples contenedores a través de un clúster de máquinas. Automatiza el despliegue, escalado y operación de aplicaciones containerizadas.

#### Características Clave
1. **Gestión de Clúster**:
   - Kubernetes se ejecuta en un clúster de nodos (máquinas físicas o virtuales). Un nodo es el "plano de control" (gestiona el clúster) y los otros son "nodos trabajadores" (ejecutan contenedores).

2. **Orquestación**:
   - **Programación**: Decide qué nodo ejecuta cada contenedor basándose en recursos y restricciones.
   - **Escalado**: Aumenta o disminuye automáticamente el número de instancias de contenedores (por ejemplo, basado en el uso de CPU).
   - **Auto-Reparación**: Reinicia contenedores fallidos, los reprograma si un nodo falla y asegura que se mantenga el estado deseado.
   - **Balanceo de Carga**: Distribuye el tráfico a través de múltiples instancias de contenedores.

3. **Capa de Abstracción**:
   - Utiliza "Pods" como la unidad más pequeña—un Pod puede contener uno o más contenedores (normalmente uno) que comparten recursos de almacenamiento y red.
   - Se gestiona mediante archivos YAML declarativos (por ejemplo, definiendo despliegues, servicios).

4. **Enfoque en Múltiples Hosts**:
   - Diseñado para sistemas distribuidos, coordinando contenedores a través de muchas máquinas.

5. **Ecosistema**:
   - Incluye características como descubrimiento de servicios, almacenamiento persistente, gestión de secretos y actualizaciones progresivas.

#### Caso de Uso
- Desplegar una aplicación de microservicios con 10 servicios, cada uno en su propio contenedor, a través de 5 servidores, con escalado automático y conmutación por error:
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: myapp
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: myapp
    template:
      metadata:
        labels:
          app: myapp
      spec:
        containers:
        - name: myapp
          image: myapp:latest
          ports:
          - containerPort: 8080
  ```

#### Limitaciones
- Curva de aprendizaje más pronunciada.
- Excesivo para aplicaciones simples de un solo contenedor en una máquina.

---

### Diferencias Clave

| Aspecto               | Docker                              | Kubernetes                          |
|-----------------------|-------------------------------------|-------------------------------------|
| **Propósito**         | Creación y runtime de contenedores  | Orquestación de contenedores        |
| **Alcance**           | Host único                          | Clúster de hosts                    |
| **Unidad**            | Contenedor                          | Pod (grupo de 1+ contenedores)      |
| **Escalado**          | Manual (ej., `docker run` múltiples veces) | Automático (vía réplicas)           |
| **Redes**             | Básico (bridge, host, overlay)      | Avanzado (servicios, ingress)       |
| **Auto-Reparación**   | Ninguno (reinicio manual)           | Integrado (reinicia, reprograma)    |
| **Gestión**           | CLI o Docker Compose para configuraciones pequeñas | Configs YAML, CLI `kubectl`         |
| **Dependencias**      | Independiente (necesita Docker Engine) | Necesita un runtime de contenedores (ej., Docker) |

---

### Cómo Trabajan Juntos
- **Docker como el Runtime**: Kubernetes no ejecuta contenedores directamente—depende de un runtime de contenedores como Docker (o alternativas como `containerd`) para iniciar y gestionar contenedores individuales dentro de los Pods.
- **Flujo de Trabajo**:
  1. Construyes una imagen de Docker (`docker build -t myapp:latest .`).
  2. La subes a un registro (`docker push myapp:latest`).
  3. Kubernetes descarga la imagen y la despliega a través del clúster basándose en tu configuración YAML (`kubectl apply -f deployment.yaml`).

- **Ejemplo**: Kubernetes podría usar Docker para ejecutar tres instancias de `myapp:latest` en diferentes nodos, exponiéndolas a través de un servicio con balanceo de carga.

---

### Analogía
- **Docker**: Un chef cocinando un solo plato en una cocina. Le dices al chef qué hacer (`Dockerfile`) y cómo servirlo (`docker run`).
- **Kubernetes**: Un gerente de restaurante supervisando múltiples chefs (instancias de Docker) a través de muchas cocinas (nodos). El gerente asegura que los platos se preparen a tiempo, escala el personal durante la hora pico y reemplaza a un chef que se enferma.

---

### ¿Cuándo Usar Cada Uno?
- **Solo Docker**: Para desarrollo, pruebas o aplicaciones simples en una máquina (por ejemplo, una sola aplicación Spring Boot).
- **Kubernetes**: Para aplicaciones distribuidas de grado productivo que necesitan alta disponibilidad, escalado y resiliencia (por ejemplo, una arquitectura de microservicios).

---

¿Queda clara la distinción? ¡Déjame saber si te gustaría explorar un aspecto específico—como configurar Kubernetes o compararlo con Docker Compose!