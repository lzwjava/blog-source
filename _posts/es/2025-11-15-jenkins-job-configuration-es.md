---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Configuración de Trabajos de Jenkins
translated: true
type: note
---

### Configurar un Job en Jenkins

Jenkins admite diferentes tipos de jobs (también llamados proyectos), siendo los más comunes los **proyectos Freestyle** (para builds simples) y los **proyectos Pipeline** (para flujos de trabajo más complejos y scripteados usando Jenkinsfile). A continuación, describiré los pasos para ambos. Esto asume que tienes Jenkins instalado y en ejecución (por ejemplo, mediante Docker o en un servidor). Accede al panel de control de Jenkins en `http://localhost:8080` (o la URL de tu servidor) e inicia sesión.

#### Pasos para Crear y Configurar un Proyecto Freestyle
Los proyectos Freestyle son sencillos y utilizan una GUI para configurar los pasos. Son ideales para principiantes o tareas simples como compilar y probar código.

1.  **Crear un Nuevo Job**:
    *   Desde el panel de control de Jenkins, haz clic en **New Item** en la barra lateral izquierda.
    *   Ingresa un nombre para tu job (por ejemplo, "MyFirstBuild").
    *   Selecciona **Freestyle project** y haz clic en **OK**.

2.  **Configuración General**:
    *   Añade una descripción para el job.
    *   Opcionalmente, habilita funciones como descartar builds antiguos (por ejemplo, mantener solo los últimos 10 builds) o añade parámetros (por ejemplo, parámetros de cadena o de elección para la entrada del usuario durante los builds).

3.  **Gestión del Código Fuente**:
    *   Elige tu herramienta SCM, como Git.
    *   Ingresa la URL del repositorio (por ejemplo, un repositorio de GitHub).
    *   Añade credenciales si es necesario (por ejemplo, usuario/contraseña o clave SSH).
    *   Especifica las ramas para construir (por ejemplo, `*/main`).

4.  **Disparadores de Build**:
    *   Selecciona cómo inicia el job, por ejemplo:
        *   **Build periodically** (por ejemplo, sintaxis cron como `H/5 * * * *` para cada 5 minutos).
        *   **Poll SCM** para verificar si hay cambios.
        *   **GitHub hook trigger** para webhooks desde GitHub.
        *   **Build after other projects** para encadenar jobs.

5.  **Entorno de Build**:
    *   Marca opciones como **Delete workspace before build starts** para comenzar desde cero.
    *   Añade marcas de tiempo a la salida de la consola o establece variables de entorno.

6.  **Pasos del Build**:
    *   Haz clic en **Add build step** y elige acciones como:
        *   **Execute shell** (para Linux/Mac: por ejemplo, `echo "Hello World"` o ejecutar scripts).
        *   **Invoke top-level Maven targets** para builds de Java.
        *   **Execute Windows batch command** para Windows.
    *   Puedes añadir múltiples pasos que se ejecuten secuencialmente.

7.  **Acciones Post-Build**:
    *   Añade acciones como:
        *   **Archive the artifacts** (por ejemplo, guardar archivos JAR).
        *   **Publish JUnit test result report**.
        *   **Send email notifications** en caso de éxito/fallo.
        *   **Trigger another project**.

8.  **Guardar y Ejecutar**:
    *   Haz clic en **Save**.
    *   De vuelta en la página del job, haz clic en **Build Now** para probarlo.
    *   Ve la salida de la consola para más detalles.

#### Pasos para Crear y Configurar un Proyecto Pipeline
Los Pipelines se definen como código (declarativo o scripted) y son más flexibles para flujos de trabajo de CI/CD.

1.  **Crear un Nuevo Job**:
    *   Desde el panel de control, haz clic en **New Item**.
    *   Ingresa un nombre y selecciona **Pipeline**, luego **OK**.

2.  **Configuración General**:
    *   Similar a Freestyle: añade descripción, parámetros, etc.

3.  **Disparadores de Build**:
    *   Las mismas opciones que en Freestyle (por ejemplo, webhooks, programaciones).

4.  **Definición del Pipeline**:
    *   Elige **Pipeline script** para código en línea o **Pipeline script from SCM** para extraerlo de un repositorio (por ejemplo, un `Jenkinsfile` en Git).
    *   Ejemplo de script de pipeline declarativo:
        ```
        pipeline {
            agent any
            stages {
                stage('Build') {
                    steps {
                        echo 'Building...'
                        sh 'mvn clean install'  // Ejemplo de build con Maven
                    }
                }
                stage('Test') {
                    steps {
                        echo 'Testing...'
                        sh 'mvn test'
                    }
                }
                stage('Deploy') {
                    steps {
                        echo 'Deploying...'
                    }
                }
            }
            post {
                always {
                    echo 'This runs always'
                }
            }
        }
        ```
    *   Esto define etapas (Build, Test, Deploy) con pasos.

5.  **Guardar y Ejecutar**:
    *   Guarda el job.
    *   Construye y monitorea la vista del pipeline para ver el progreso de las etapas.

Jenkins tiene muchas opciones en cada sección, así que explora según tus necesidades (por ejemplo, para seguridad, añade credenciales; para paralelismo, usa agentes/nodos). Si eres nuevo, comienza con Freestyle y pasa a Pipelines para escalabilidad.

### Integraciones de Software y Colaboraciones con Jenkins

Jenkins es altamente extensible a través de **plugins** (más de 2,000 disponibles), lo que le permite integrarse con prácticamente cualquier herramienta del ecosistema DevOps. Estas integraciones permiten disparar builds, despliegues, pruebas, notificaciones y más. Los plugins se pueden instalar a través de **Manage Jenkins > Manage Plugins**.

#### Integraciones Comunes por Categoría
*   **Control de Versiones**: Git, GitHub, GitLab, Bitbucket, SVN – Para extraer código y disparar builds en eventos de commits/push mediante webhooks.
*   **Contenerización y Orquestación**: Docker (construir/empujar imágenes), Kubernetes (desplegar en clusters), Helm – Para flujos de trabajo basados en contenedores.
*   **Proveedores de Nube**: AWS (EC2, S3, Lambda mediante plugins), Azure, Google Cloud – Para desplegar en infraestructura cloud.
*   **Pruebas y Calidad**: SonarQube (escaneos de calidad de código), Selenium (pruebas de UI), JUnit (pruebas unitarias), Cucumber (BDD) – Integrar en los pasos de build para pruebas automatizadas.
*   **Despliegue y Monitoreo**: Ansible, Terraform (infraestructura como código), Prometheus, Grafana – Para orquestación y monitoreo post-build.
*   **Notificaciones y Colaboración**: Slack, Microsoft Teams, Email, Jira, Trello – Enviar alertas o actualizar tickets sobre el estado del build.
*   **Herramientas de Build**: Maven, Gradle (Java), npm (Node.js), pip (Python) – Ejecutar builds para varios lenguajes.
*   **Seguridad**: OWASP Dependency-Check, Trivy (escaneo de vulnerabilidades) – Escanear en busca de problemas durante el CI.
*   **Otras**: Artifactory/Nexus (repositorios de artefactos), Zapier (integraciones sin código), Octopus Deploy (despliegues avanzados).

Por ejemplo, con GitHub, instala el plugin de GitHub para habilitar disparadores por webhook. Con Docker, usa el plugin Docker Pipeline para construir imágenes en los pipelines. Incluso se pueden crear plugins personalizados para herramientas específicas.

Para explorar más, consulta el índice oficial de plugins. Siempre actualiza los plugins regularmente por seguridad.

#### Referencias
*   [Working with projects - Jenkins](https://www.jenkins.io/doc/book/using/working-with-projects/)
*   [Jenkins - Setup Build Jobs - Tutorials Point](https://www.tutorialspoint.com/jenkins/jenkins_setup_build_jobs.htm)
*   [How to Create and Configure Build Jobs in Jenkins | BrowserStack](https://www.browserstack.com/guide/build-jobs-in-jenkins)
*   [Jenkins Build: Set Up Freestyle Project in Jenkins {Step-by-Step}](https://phoenixnap.com/kb/jenkins-build-freestyle-project)
*   [Managing Plugins - Jenkins](https://www.jenkins.io/doc/book/managing/plugins/)
*   [How to Integrate Jenkins with Different Tools and Technologies?](https://www.addwebsolution.com/blog/integrating-jenkins-with-other-tools-and-technologies)
*   [Jenkins Plugins](https://plugins.jenkins.io/)
*   [Jenkins](https://www.jenkins.io/)
*   [10 Of Our Favorite Jenkins Plugins | Octopus blog](https://octopus.com/blog/jenkins-ten-plugins)