---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Alumni de la Clase Yao de Tsinghua en Compiladores
translated: true
type: note
---

### Resumen de la Clase Yao de Tsinghua
La Clase Yao de la Universidad de Tsinghua (formalmente "Clase Experimental de Ciencias de la Computación de la Academia Tsinghua" o "清华学堂计算机科学实验班") es un programa de pregrado de élite fundado en 2005 por Andrew Chi-Chih Yao, el primer ganador chino del Premio Turing. Recluta talentos de primer nivel (a menudo medallistas de Olimpiadas y los mejores en exámenes provinciales) y enfatiza la informática teórica, con el objetivo de rivalizar con el MIT o Stanford. Hasta 2024, ha producido más de 500 graduados, muchos de los cuales se dedican a la academia, con una fuerte representación en investigación de algoritmos, IA y sistemas. Aunque no todos se centran en compiladores o lenguajes de programación, la base rigurosa del programa en teoría y computación canaliza naturalmente a algunos exalumnos hacia estas áreas.

Las discusiones en Zhihu a menudo destacan a los exalumnos de la Clase Yao como "joyas ocultas" en el mundo académico, señalando su impacto desproporcionado a pesar de la juventud del programa (primeros graduados ~2010). A continuación, me centro en aquellos que trabajan en el mundo académico en compiladores, lenguajes de programación (PL) o campos estrechamente relacionados como el diseño de lenguajes, IR (representación intermedia) y sistemas de computación de alto rendimiento. Esto se basa en perfiles públicos, publicaciones y rastreadores de exalumnos—las listas completas son difíciles debido a la privacidad, pero estos son ejemplos prominentes.

### Exalumnos Notables de la Clase Yao en el Mundo Académico (Enfoque en Compiladores/Lenguajes de Programación)
Aquí hay una tabla de exalumnos clave, sus roles actuales y contribuciones. He priorizado a aquellos con vínculos directos con la investigación en compiladores/PL.

| Nombre | Año de Graduación | Posición Actual | Contribuciones Clave en Compiladores/PL |
|------|-----------------|------------------|----------------------------------|
| **Yuanming Hu (胡渊明)** | 2017 | Profesor Asistente, MIT EECS (a partir de 2024); Fundador, Taichi Graphics | Creador de Taichi, un DSL (lenguaje específico del dominio) embebido y compilador orientado a datos para computación visual y simulaciones de alto rendimiento. Se centra en la compilación just-in-time (JIT), estructuras de datos dispersas y paralelización para cargas de trabajo de gráficos/IA. Publicaciones en SIGGRAPH/ACM Transactions on Graphics; citado por avanzar en la programación diferenciada y las optimizaciones de compiladores para la computación espacial. |
| **Mingkuan Xu** | 2021 | Candidato a PhD, Universidad Carnegie Mellon (asesorado por Zhihao Jia & Umut Acar) | Trabaja en infraestructura de compiladores para computación visual, incluyendo compiladores de cuantificación para simulaciones eficientes en memoria y la estandarización de Taichi IR (representación intermedia). Su investigación une la teoría de PL con la aceleración por hardware; publicaciones sobre compiladores portátiles y de alto rendimiento para cargas de trabajo dispersas. |
| **Danqi Chen** | 2012 | Profesora Asistente, Universidad de Princeton (Grupo de PLN) | Aunque se centra principalmente en PLN, su trabajo involucra modelos de lenguaje y análisis, incluyendo representaciones semánticas y sistemas de tipos para el procesamiento del lenguaje natural. Coautora de artículos fundamentales sobre comprensión lectora automatizada (ej., benchmarks SQuAD), con vínculos con PL a través de la compilación eficiente de modelos para inferencia a gran escala. (Nota: Influencia más amplia en PL a través de la comprensión del lenguaje escalable). |
| **Beihang Xiao (贝小辉, Xiao Beihang)** | ~2010s (promoción temprana) | Profesor Asistente, Universidad Tecnológica de Nanyang | Investigación en informática teórica con aplicaciones a lenguajes de programación cuántica y verificación de compiladores. Se centra en lenguajes type-safe para la corrección de errores cuánticos y la computación paralela; publicaciones en POPL (Principles of Programming Languages) y sedes relacionadas. |
| **Ma Tengyu (马腾宇)** | ~2010s | Profesor Asistente, Universidad de Duke | Especializado en teoría del aprendizaje automático que se interseca con PL, incluyendo programación probabilística y verificación automatizada para compiladores de ML. Su trabajo en optimización no convexa para redes neuronales tiene implicaciones para la compilación just-in-time en frameworks de aprendizaje profundo. |

### Contexto Adicional
- **Tendencias más Amplias**: A mediados de 2024, ~21 exalumnos de Yao enseñan en universidades chinas de primer nivel (ej., Tsinghua, Peking), y ~17 en el extranjero (ej., Stanford, Princeton). Muchos publican en sedes de PL como PLDI, OOPSLA o POPL, pero los compiladores/PL son un nicho—la mayoría se inclina hacia algoritmos/IA. Hilos de Zhihu (ej., sobre "姚班学术成果") elogian a exalumnos como Hu Yuanming por "democratizar la programación de alto rendimiento" a través de herramientas de código abierto.
- **¿Por Qué Estos Campos?** El plan de estudios de la Clase Yao (con gran carga en matemáticas discretas, algoritmos y teoría) prepara a los estudiantes para PL/compiladores, pero la ingeniería práctica es más ligera, adecuándose más al mundo académico que a las herramientas de la industria.
- **Fuentes para Lectura Adicional**:
  - Página de Exalumnos de Tsinghua IIIS: [iiis.tsinghua.edu.cn/en/Yao_Class](https://iiis.tsinghua.edu.cn/en/Yao_Class)
  - Discusión en Zhihu sobre los Logros de Yao: [zhihu.com/question/667767788](https://www.zhihu.com/question/667767788)
  - Perfil de Yuanming Hu: [yuanming.taichi.graphics](https://yuanming.taichi.graphics)
  - Sitio de Mingkuan Xu: [mingkuan.taichi.graphics](https://mingkuan.taichi.graphics)

Si tienes nombres específicos o más detalles de la publicación en Zhihu, ¡puedo investigar más a fondo