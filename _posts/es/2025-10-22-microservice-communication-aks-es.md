---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de la Comunicación de Microservicios en AKS
translated: true
type: note
---

### Configuración de la Comunicación Entre Microservicios en Azure Kubernetes Service (AKS)

En Azure Kubernetes Service (AKS), los microservicios se implementan típicamente como **Pods** gestionados por **Deployments**. Para permitir que se comuniquen entre sí (por ejemplo, el Servicio A llamando al Servicio B), se utilizan **Kubernetes Services** para abstraer las IPs dinámicas de los Pods y proporcionar endpoints estables. Esto se hace a través de una red interna, aprovechando la resolución DNS integrada de Kubernetes. Aquí tienes una guía paso a paso para configurar e implementar esto.

#### 1. **Implementar los Microservicios como Deployments**
   Cada microservicio se ejecuta en un Pod (o conjunto de Pods para escalado). Usa un Deployment para gestionarlos.

   Ejemplo de YAML para un Deployment de microservicio simple (`service-a-deployment.yaml`):
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: service-a
     namespace: default  # O tu namespace personalizado
   spec:
     replicas: 3  # Escala según sea necesario
     selector:
       matchLabels:
         app: service-a
     template:
       metadata:
         labels:
           app: service-a
       spec:
         containers:
         - name: service-a
           image: your-registry/service-a:latest  # ej., imagen de ACR o Docker Hub
           ports:
           - containerPort: 8080  # Puerto en el que escucha tu aplicación
   ```

   Aplícalo:
   ```
   kubectl apply -f service-a-deployment.yaml
   ```

   Repite el proceso para otros servicios (ej., `service-b`).

#### 2. **Exponer los Microservicios con Services**
   Crea un **ClusterIP Service** para cada microservicio. Este tipo es solo para comunicación interna (no se expone fuera del cluster). Equilibra la carga del tráfico hacia los Pods y proporciona un nombre DNS.

   Ejemplo de YAML para el Servicio A (`service-a-service.yaml`):
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: service-a
     namespace: default
   spec:
     selector:
       app: service-a  # Coincide con las etiquetas del Deployment
     ports:
     - protocol: TCP
       port: 80  # Puerto del Servicio (el que usan los llamantes)
       targetPort: 8080  # Puerto del contenedor del Pod
     type: ClusterIP  # Solo interno
   ```

   Aplícalo:
   ```
   kubectl apply -f service-a-service.yaml
   ```

   Haz lo mismo para el Servicio B. Ahora, los Pods pueden alcanzarse entre sí a través del nombre DNS del Servicio.

#### 3. **Cómo se Llaman los Microservicios Entre Sí**
   - **Descubrimiento Basado en DNS**: El DNS de Kubernetes resuelve los nombres de los Services automáticamente. Desde un Pod en el Servicio A, llama al Servicio B usando:
     - `<nombre-del-servicio>.<namespace>.svc.cluster.local` (completamente calificado, ej., `service-b.default.svc.cluster.local`).
     - O simplemente `<nombre-del-servicio>` si están en el mismo namespace (ej., `service-b`).
   - **Llamadas HTTP/gRPC**: En el código de tu aplicación, realiza peticiones a `http://service-b:80/endpoint`. Kubernetes maneja el equilibrio de carga y la conmutación por error.
     - Ejemplo en Python (usando requests):
       ```python
       import requests
       response = requests.get("http://service-b:80/api/data")
       ```
     - Para gRPC, usa el mismo nombre de host con el puerto gRPC.
   - **Mapeo de Puertos**: El puerto del Servicio (ej., 80) se mapea al puerto objetivo del Pod (ej., 8080). No es necesario codificar las IPs de los Pods—cambian en los reinicios.

   Prueba la conectividad desde un Pod:
   ```
   kubectl exec -it <nombre-del-pod-en-service-a> -- curl http://service-b:80/health
   ```

#### 4. **Opciones de Configuración Avanzadas**
   - **Namespaces**: Implementa servicios en diferentes namespaces para aislamiento. Usa el DNS completo (ej., `service-b.other-ns.svc.cluster.local`).
   - **Network Policies**: Asegura la comunicación con políticas de Calico o Azure CNI para permitir/denegar tráfico entre servicios.
     Ejemplo de política que permite al Servicio A llamar al Servicio B:
     ```yaml
     apiVersion: networking.k8s.io/v1
     kind: NetworkPolicy
     metadata:
       name: allow-service-a-to-b
     spec:
       podSelector:
         matchLabels:
           app: service-b
       policyTypes:
       - Ingress
       ingress:
       - from:
         - podSelector:
             matchLabels:
               app: service-a
         ports:
         - protocol: TCP
           port: 80
     ```
   - **Service Mesh (ej., Istio o Linkerd)**: Para entornos de producción, añade una malla para observabilidad, mTLS y gestión de tráfico. Instálalo via Helm en AKS, luego inyecta sidecar proxies en los Pods.
   - **Acceso Externo (si es necesario)**: Usa Servicios **LoadBalancer** o **Ingress** para llamadas salientes, pero mantén ClusterIP para la comunicación interna.

#### 5. **Mejores Prácticas**
   - Usa **variables de entorno** o **ConfigMaps** para inyectar nombres DNS de los Services en las aplicaciones de forma dinámica.
   - Monitoriza con Azure Monitor for AKS para rastrear el tráfico entre servicios.
   - Escala horizontalmente con Horizontal Pod Autoscaler (HPA) basado en CPU/memoria.
   - Para integraciones específicas de Azure, usa Azure Container Registry (ACR) para las imágenes y Azure AD para autenticación.

Esta configuración asegura una comunicación confiable y escalable sin un acoplamiento estrecho. Comienza con Services básicos, luego añade seguridad/malla según sea necesario.

[Información General sobre Redes en AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-network)  
[Documentación de Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)  
[Tutorial de Microservicios en AKS](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)