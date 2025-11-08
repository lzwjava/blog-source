---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Jerome Friedman y el Potenciamiento de Gradientes
translated: true
type: note
---

### Introducción a Jerome H. Friedman

Jerome Harold Friedman, nacido el 29 de diciembre de 1939 en el pequeño pueblo de Yreka, California (cerca de la frontera con Oregón), es un estadístico estadounidense pionero y una de las figuras más influyentes en el desarrollo del machine learning moderno y la minería de datos. Con formación en física, tendió un puente entre los métodos computacionales de la física de partículas de alta energía y la estadística, creando algoritmos prácticos que manejan conjuntos de datos grandes y complejos. Su trabajo hace hincapié en modelos interpretables y robustos para la predicción y el descubrimiento de patrones, influyendo en campos que van desde los motores de búsqueda hasta la bioinformática. Friedman es autor de más de 70 publicaciones, ha coescrito libros fundamentales como *Classification and Regression Trees* (CART, 1984) y *The Elements of Statistical Learning* (2001), y ha recibido honores prestigiosos, incluyendo su elección a la National Academy of Sciences (2010), la American Academy of Arts and Sciences (2005) y múltiples premios por su innovación en minería de datos y métodos estadísticos.

### El Artículo Original sobre Gradient Boosting (Friedman, 2001)

El artículo histórico de Friedman, *"Greedy Function Approximation: A Gradient Boosting Machine"*, publicado en los *Annals of Statistics* en agosto de 2001, formalizó el gradient boosting como un método de ensemble versátil para regresión y clasificación. Partiendo de ideas previas sobre boosting de informáticos como Yoav Freund y Robert Schapire (que se centraban en el error de clasificación), Friedman lo extendió a funciones de pérdida arbitrarias utilizando un marco de "descenso de gradiente funcional". La idea central: añadir iterativamente weak learners (a menudo árboles de decisión simples) que se ajusten al gradiente negativo de la pérdida en los residuos actuales, minimizando efectivamente los errores paso a paso, como el descenso de gradiente estocástico en el espacio de funciones.

Las innovaciones clave incluyeron:
- **Shrinkage (tasa de aprendizaje)**: Un parámetro de regularización para prevenir el sobreajuste escalando cada nuevo árbol, reduciendo la varianza sin aumentar el sesgo.
- **Flexibilidad**: Aplicable a cualquier función de pérdida diferenciable (por ejemplo, error cuadrático para regresión, pérdida logarítmica para clasificación), lo que lo convierte en una herramienta de propósito general.
- **Interpretación estadística**: En colaboración con Trevor Hastie y Robert Tibshirani, demostró que el boosting reduce la correlación entre los weak learners, mejorando el rendimiento del ensemble.

Este artículo (presentado como su Rietz Lecture en 1999) provocó una adopción generalizada: implementaciones como XGBoost y LightGBM dominan hoy en día las competiciones de Kaggle y la industria. Tiene más de 20.000 citas y transformó el ensemble learning de una heurística a una potencia con bases estadísticas sólidas.

### Su Historia: De Manitas de Pueblo Pequeño a Pionero del Machine Learning

La trayectoria de Friedman parece un relato clásico de reinvención impulsada por la curiosidad. Creciendo en una familia de inmigrantes ucranianos—sus abuelos iniciaron una lavandería en la década de 1930, dirigida por su padre y su tío—se describía a sí mismo como un "fracasado dramático" en la escuela secundaria. No le interesaban los libros pero estaba obsesionado con la electrónica; construía radios de aficionados, receptores de galena y transmisores de alto voltaje, charlando con operadores de onda corta de todo el mundo. El padre de un amigo, también entusiasta de la radio, lo orientó, pero su director le advirtió que reprobaría en la universidad. Impávido, se matriculó en Humboldt State (ahora Cal Poly Humboldt) para dos años de fiestas y ciencias básicas, luego se transfirió a UC Berkeley en 1959 tras negociar con su padre. Allí, un profesor excepcional de física lo enganchó; se graduó con un A.B. en Física en 1962 (promedio B+/A-, hazaña no menor antes de la inflación de notas) mientras trabajaba en empleos diversos como bombero y en emisoras de radio.

Su doctorado en física de partículas de alta energía llegó en 1967, centrándose en reacciones de mesones en cámaras de burbujas bajo el legendario grupo de Luis Alvarez en el Lawrence Berkeley Lab. Evitando el reclutamiento para Vietnam mediante aplazamientos por estudios, se sumergió en la computación—programando gráficos de dispersión en antiguas máquinas IBM en lenguaje máquina y Fortran. Esto desencadenó un cambio: el reconocimiento manual de patrones en película condujo a software como Kiowa (análisis exploratorio de datos) y Sage (simulaciones de Monte Carlo), fusionando física con estadística. Tras el doctorado, se quedó como investigador postdoctoral (1968–1972), pero una reestructuración del laboratorio forzó su salida.

En 1972, recaló como jefe del Computation Research Group en el Stanford Linear Accelerator Center (SLAC), desplazándose desde Berkeley con su esposa y su hija pequeña. Liderando a unos 10 programadores, abordó gráficos, algoritmos y herramientas para físicos en hardware de vanguardia. Sus períodos sabáticos—como en el CERN (1976–1977), donde construyó código adaptativo de Monte Carlo—lo ampliaron, pero la intensidad del SLAC se adaptaba a su estilo. Las conferencias sobre interfaces lo presentaron a gigantes de la estadística: John Tukey (proyección de proyección, 1974), Leo Breiman (colaboración en CART, desde 1977 en adelante) y Werner Stuetzle (extensiones de regresión).

Para 1982, se unió al Departamento de Estadística de Stanford a media jornada (Profesor Titular en 1984; Director 1988–1991; Emérito en 2007), equilibrando el liderazgo en SLAC hasta 2003. Su investigación de "paseo aleatorio"—resolviendo problemas espinosos mediante código y empirismo—produjo avances:
- **Década de 1970**: k-d trees para vecinos más cercanos rápidos (1977) y projection pursuit para detectar "grupos" en altas dimensiones.
- **Década de 1980**: CART (árboles para clasificación/regresión) y ACE (transformaciones no paramétricas, 1985).
- **Década de 1990**: MARS (regresión adaptativa basada en splines, 1991); críticas a PLS; caza de protuberancias (PRIM, 1999).
- **Década de 2000**: Gradient boosting (2001); RuleFit (reglas interpretables de ensembles); glmnet (LASSO/elastic net rápido).

Un consultor prolífico (por ejemplo, Google 2011–2014, Yahoo 2004–2005), comercializó herramientas como el software CART, influyendo en motores de búsqueda y más allá. Influenciado por el enfoque operacional de Tukey ("dime los pasos") y el pragmatismo de Breiman, Friedman rechazó la teoría pesada en favor de algoritmos elegantes y comprobables. Aprendió estadística sobre la marcha—sin cursos formales—viéndose a sí mismo como un "oportunista" que abordaba el caos de la minería de datos. Las colaboraciones con estudiantes y colegas "brillantes" lo impulsaron; se retiró del liderazgo en SLAC en 2006 pero mantuvo la consultoría y la escritura.

### ¿Dónde Está Ahora?

En 2025, a los 85 años, Friedman sigue vinculado al Departamento de Estadística de la Universidad de Stanford como Profesor Emérito, continuando influyendo en el campo a través de su legado y trabajo ocasional. Su perfil en Stanford lo enumera como un investigador activo en machine learning, y actualizaciones recientes (por ejemplo, American Academy of Arts and Sciences, septiembre de 2025) destacan su reconocimiento continuo. No hay indicios de una jubilación total—es probable que consulte o mentorice esporádicamente, dada su historia. Reside en el Área de la Bahía, fiel a sus raíces californianas.

**Referencias**
- [Jerome H. Friedman - Wikipedia](https://en.wikipedia.org/wiki/Jerome_H._Friedman)
- [Jerome H. Friedman | Department of Statistics, Stanford](https://statistics.stanford.edu/people/jerome-h-friedman)
- [A Conversation with Jerry Friedman (arXiv PDF)](https://arxiv.org/pdf/1507.08502)
- [Vita - Jerome H. Friedman (PDF)](https://jerryfriedman.su.domains/ftp/vita.pdf)
- [Jerome H. Friedman | American Academy of Arts and Sciences](https://www.amacad.org/person/jerome-h-friedman)