---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'Helm: Administrador de Paquetes de Kubernetes'
translated: true
type: note
---

Helm es el gestor de paquetes para Kubernetes, a menudo llamado "el yum o apt para Kubernetes". Simplifica el despliegue, la gestión y la actualización de aplicaciones complejas en clústeres de Kubernetes agrupando recursos relacionados (Deployments, Services, ConfigMaps, etc.) en **charts** reutilizables y versionados.

Piensa en un chart de Helm como una imagen de Docker para los manifiestos de Kubernetes: empaqueta archivos YAML, plantillas, valores por defecto y lógica en una sola unidad que se puede instalar con un solo comando.

En las pipelines de CI/CD como **Jenkins**, Helm se usa comúnmente para:
- Construir y probar charts.
- Subir charts a repositorios (por ejemplo, ChartMuseum, Harbor, Nexus).
- Desplegar aplicaciones en clústeres de staging/producción de forma segura.

---

## ¿Por qué usar Helm?

| Problema | Solución de Helm |
|--------|---------------|
| Gestionar manualmente 50+ archivos YAML | Agruparlos en un solo chart |
| Desplegar la misma app en dev/stage/prod | Usar anulaciones en `values.yaml` |
| Revertir despliegues fallidos | `helm rollback` |
| Compartir aplicaciones entre equipos | Publicar charts en un repositorio |
| Control de versiones de la infraestructura | Versionado semántico de los charts |

---

## Conceptos Básicos

### 1. **Chart**
- Estructura de directorios que contiene manifiestos de Kubernetes y metadatos.
- Ejemplo: `my-app-chart/`

```
my-app-chart/
├── Chart.yaml          # Metadatos (nombre, versión, etc.)
├── values.yaml         # Valores de configuración por defecto
├── templates/          # Plantillas YAML de Kubernetes
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # Fragmentos de plantilla reutilizables
└── charts/             # Sub-charts (dependencias)
```

### 2. **Release**
- Una instancia de un chart ejecutándose en un clúster.
- Un chart → múltiples releases (por ejemplo, `myapp-dev`, `myapp-prod`).

### 3. **Repository**
- Servidor HTTP que aloja charts indexados (como el registro de npm).
- Comunes: ChartMuseum, Harbor, Nexus, GitHub Pages, S3.

### 4. **Tiller** (Obsoleto)
- Helm v2 usaba un componente del lado del servidor llamado Tiller.
- **Helm v3+ elimina Tiller** → solo cliente, más seguro.

---

## Hoja de Referencia de Comandos de Helm

| Comando | Propósito |
|-------|--------|
| `helm create mychart` | Crear la estructura de un nuevo chart |
| `helm lint mychart/` | Validar el chart |
| `helm package mychart/` | Crear archivo `.tgz` |
| `helm repo add stable https://charts.helm.sh/stable` | Añadir repositorio |
| `helm repo update` | Actualizar caché local |
| `helm search repo nginx` | Buscar charts |
| `helm install myapp ./mychart` | Desplegar release |
| `helm upgrade myapp ./mychart -f prod-values.yaml` | Actualizar con nuevos valores |
| `helm rollback myapp 3` | Revertir a la revisión 3 |
| `helm uninstall myapp` | Eliminar release |
| `helm list` | Listar releases |
| `helm status myapp` | Mostrar estado del release |
| `helm template ./mychart -f values.yaml` | Renderizar plantillas localmente |

---

## Estructura del Chart en Profundidad

### `Chart.yaml` (Requerido)
```yaml
apiVersion: v2
kind: Chart
name: my-app
version: 1.2.3
appVersion: "2.5.0"
description: Una aplicación web de ejemplo
type: application
keywords:
  - web
  - http
home: https://example.com
sources:
  - https://github.com/user/my-app
maintainers:
  - name: Dev Team
    email: dev@example.com
icon: https://example.com/logo.png
```

### `values.yaml` (Valores por Defecto)
```yaml
replicaCount: 2
image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent
service:
  type: ClusterIP
  port: 80
resources:
  limits:
    cpu: 500m
    memory: 512Mi
```

### `templates/deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
  labels:
    {{- include "my-app.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "my-app.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "my-app.selectorLabels" . | nindent 8 }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: 80
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

### `_helpers.tpl` (Mejor Práctica)
```tpl
{{/* Generar etiquetas básicas */}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

---

## Helm en una Pipeline de CI/CD con Jenkins

Aquí hay una **Jenkins Pipeline** típica usando Helm:

```groovy
pipeline {
    agent any
    environment {
        CHART_DIR = "helm/my-app"
        IMAGE_NAME = "myregistry/my-app"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        HELM_REPO = "https://charts.mycompany.com"
    }
    stages {
        stage('Build & Push Docker') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Package Helm Chart') {
            steps {
                sh """
                cd ${CHART_DIR}
                yq eval '.image.tag = "${IMAGE_TAG}"' values.yaml -i
                helm dependency update
                helm package .
                """
            }
        }

        stage('Deploy to Staging') {
            when { branch 'main' }
            steps {
                withCredentials([kubeconfigFile(credentialsId: 'kubeconfig-staging')]) {
                    sh """
                    helm upgrade --install myapp-staging ./helm/my-app*.tgz \
                      --namespace staging \
                      --values values-staging.yaml \
                      --wait --timeout 5m
                    """
                }
            }
        }

        stage('Deploy to Production') {
            when { tag "v*" }
            input { message "Deploy to production?" }
            steps {
                withCredentials([kubeconfigFile(credentialsId: 'kubeconfig-prod')]) {
                    sh """
                    helm upgrade --install myapp-prod ./helm/my-app*.tgz \
                      --namespace production \
                      --values values-prod.yaml \
                      --atomic
                    """
                }
            }
        }
    }
}
```

### Plugins Clave de Jenkins
- **Kubernetes CLI** (`kubectl`)
- **Helm** (a través del binario `helm` en el agente)
- **Pipeline Utility Steps** (`readYaml`, `writeYaml`)
- **Credentials Binding** (para kubeconfig, registro)

---

## Mejores Prácticas

| Práctica | Por qué |
|--------|-----|
| Usar `helm lint` + `helm template` en CI | Detectar errores pronto |
| Versionar charts semánticamente | `1.0.0` → `1.0.1` para config, `1.1.0` para nuevas funciones |
| Usar `appVersion` para la app, `version` para el chart | Desacoplar aplicación y empaquetado |
| Separar entornos con `-f values-env.yaml` | Evitar duplicar charts |
| Usar `helm secrets` o SOPS para secretos | Nunca guardar en texto plano |
| Fijar versiones de dependencias | `helm dependency update --version X` |
| Usar helpers `{{ include "chart.labels" . }}` | Etiquetado consistente |
| Habilitar `--atomic` en actualizaciones de prod | Reversión automática en caso de fallo |

---

## Herramientas e Integraciones Comunes

| Herramienta | Uso con Helm |
|------|---------------|
| **ChartMuseum** | Repositorio de charts ligero |
| **Harbor / Nexus** | Registro empresarial + repositorio Helm |
| **ArgoCD** | GitOps + Helm |
| **Flux** | GitOps con Helm Operator |
| **helmfile** | Gestionar múltiples releases de forma declarativa |
| **k3s / kind** | Pruebas locales |

---

## Consejos para Resolver Problemas

| Problema | Solución |
|------|-----|
| `Error: UPGRADE FAILED: another operation is in progress` | Esperar o usar `--force` (peligroso) |
| Las plantillas no se renderizan | Usar `helm template .` localmente |
| ImagePullBackOff | Comprobar etiqueta, autenticación del registro |
| Release no encontrado | `helm ls --all --all-namespaces` |
| CRDs no aplicados | Añadir carpeta `crds/` y aplicarlos por separado |

---

## Ejemplo: Desplegar NGINX con Helm

```bash
# Añadir repositorio
helm repo add bitnami https://charts.bitnami.com/bitnami

# Instalar
helm install web-server bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=LoadBalancer

# Actualizar
helm upgrade web-server bitnami/nginx --set replicaCount=5

# Revertir
helm rollback web-server 1
```

---

## Recursos

- [Documentación Oficial de Helm](https://helm.sh/docs/)
- [Helm Hub (Repositorio de Charts)](https://hub.helm.sh/)
- [Artifact Hub (Búsqueda Moderna de Charts)](https://artifacthub.io/)
- [Mejores Prácticas para Charts de Helm](https://helm.sh/docs/topics/charts/#chart-best-practices)

[Sitio Oficial de Helm](https://helm.sh)  
[Charts de Bitnami](https://github.com/bitnami/charts)  
[Helm en Jenkins X](https://www.jenkins-x.io/docs/)