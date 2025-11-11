---
audio: false
generated: true
lang: es
layout: post
title: Excepciones de Java
translated: true
type: note
---

Aquí tienes una lista extensa de excepciones de Java, categorizadas en **Excepciones Verificadas, Excepciones No Verificadas (Runtime) y Errores**.

---

## **1. Excepciones Verificadas (Deben manejarse o declararse usando `throws`)**
1.  **IOException** – Falla general de E/S.
2.  **FileNotFoundException** – El archivo no se encuentra o es inaccesible.
3.  **InterruptedException** – Ocurre una interrupción de un hilo.
4.  **SQLException** – Problemas relacionados con el acceso a la base de datos.
5.  **ParseException** – Error al analizar formatos de datos.
6.  **MalformedURLException** – Formato de URL inválido.
7.  **ClassNotFoundException** – La clase no se encuentra en tiempo de ejecución.
8.  **InstantiationException** – No se puede crear una instancia de una clase abstracta o interfaz.
9.  **IllegalAccessException** – El acceso a una clase, método o campo no está permitido.
10. **NoSuchMethodException** – El método no existe.
11. **NoSuchFieldException** – El campo no existe en la clase.
12. **TimeoutException** – Una operación de bloqueo agotó el tiempo de espera.
13. **UnsupportedEncodingException** – La codificación no es compatible.
14. **URISyntaxException** – Sintaxis de URI inválida.
15. **NotBoundException** – Nombre no encontrado en un registro RMI.
16. **AlreadyBoundException** – El nombre ya está vinculado en un registro RMI.
17. **CloneNotSupportedException** – El objeto no implementa `Cloneable`.
18. **DataFormatException** – Formato inválido en datos comprimidos.
19. **EOFException** – Se alcanzó un final de archivo inesperado.
20. **NotSerializableException** – El objeto no es serializable.
21. **LineUnavailableException** – La línea de audio no está disponible.
22. **UnsupportedAudioFileException** – Formato de archivo de audio no compatible.
23. **PrinterException** – Falla en una operación de impresión.
24. **ReflectiveOperationException** – Error general de reflexión.
25. **ExecutionException** – Excepción durante la ejecución de una tarea concurrente.
26. **ScriptException** – Problemas al ejecutar scripts.
27. **TransformerException** – Falla en la transformación XML.
28. **XPathExpressionException** – Expresión XPath inválida.
29. **SAXException** – Problemas con el análisis de XML.
30. **JAXBException** – Problemas con el enlace XML.
31. **MarshalException** – Error al serializar (marshalling) datos XML.
32. **UnmarshalException** – Error al deserializar (unmarshalling) datos XML.
33. **DatatypeConfigurationException** – Configuración inválida de tipo de datos XML.
34. **GSSException** – Problemas con operaciones de seguridad GSS.
35. **KeyStoreException** – Problemas con Java KeyStore.
36. **CertificateException** – Problemas con el procesamiento de certificados.
37. **InvalidKeyException** – Clave inválida en operaciones criptográficas.
38. **NoSuchAlgorithmException** – El algoritmo criptográfico solicitado no está disponible.
39. **NoSuchProviderException** – El proveedor de seguridad solicitado no está disponible.
40. **UnrecoverableKeyException** – No se puede recuperar una clave del KeyStore.
41. **IllegalBlockSizeException** – Tamaño de bloque inválido para el cifrado.
42. **BadPaddingException** – Error de relleno (padding) en criptografía.

---

## **2. Excepciones No Verificadas (Excepciones en Tiempo de Ejecución)**
43. **NullPointerException** – Se accede a una referencia de objeto que es `null`.
44. **ArrayIndexOutOfBoundsException** – Se accede a un índice de array inválido.
45. **StringIndexOutOfBoundsException** – Se accede a un índice de cadena inválido.
46. **ArithmeticException** – Errores matemáticos como la división por cero.
47. **NumberFormatException** – Conversión de una cadena inválida a un número.
48. **ClassCastException** – Conversión de tipo (casting) inválida.
49. **IllegalArgumentException** – Argumento inválido pasado a un método.
50. **IllegalStateException** – Método llamado en un estado inválido.
51. **UnsupportedOperationException** – El método no es compatible.
52. **ConcurrentModificationException** – Modificación concurrente de una colección.
53. **NoSuchElementException** – Intento de acceder a un elemento inexistente en una colección.
54. **IllegalMonitorStateException** – Error de sincronización de hilos.
55. **NegativeArraySizeException** – Creación de un array con un tamaño negativo.
56. **StackOverflowError** – Recursión infinita que provoca desbordamiento de pila.
57. **OutOfMemoryError** – La JVM se queda sin memoria.
58. **SecurityException** – Se detectó una violación de seguridad.
59. **MissingResourceException** – No se encuentra el paquete de recursos.
60. **EmptyStackException** – Intentar acceder a un elemento de una pila vacía.
61. **TypeNotPresentException** – Tipo no encontrado en tiempo de ejecución.
62. **EnumConstantNotPresentException** – Constante de enumeración inválida.
63. **UncheckedIOException** – Versión no verificada de `IOException`.
64. **DateTimeException** – Errores relacionados con la API de fecha y hora de Java.
65. **InvalidClassException** – Problemas al deserializar una clase.
66. **IllegalCharsetNameException** – Nombre de juego de caracteres inválido.
67. **UnsupportedCharsetException** – El juego de caracteres no es compatible.
68. **ProviderNotFoundException** – Falta el proveedor de servicio requerido.
69. **PatternSyntaxException** – Sintaxis de expresión regular inválida.
70. **InvalidPathException** – Ruta de archivo inválida.
71. **ReadOnlyBufferException** – Intento de modificar un buffer de solo lectura.
72. **BufferUnderflowException** – Ocurre un subdesbordamiento (underflow) del búfer.
73. **BufferOverflowException** – Ocurre un desbordamiento (overflow) del búfer.
74. **FileSystemAlreadyExistsException** – El sistema de archivos ya existe.
75. **FileSystemNotFoundException** – No se encuentra el sistema de archivos.
76. **ClosedWatchServiceException** – El servicio de vigilancia (watch service) está cerrado.
77. **UncheckedExecutionException** – Problemas en la ejecución de tareas concurrentes.

---

## **3. Errores (Problemas graves que no deberían capturarse)**
78. **StackOverflowError** – Demasiadas llamadas recursivas a métodos.
79. **OutOfMemoryError** – La JVM se queda sin memoria.
80. **VirtualMachineError** – Error crítico de la JVM.
81. **InternalError** – Error interno inesperado de la JVM.
82. **UnknownError** – Error crítico desconocido.
83. **AssertionError** – La aserción falló al usar `assert`.
84. **NoClassDefFoundError** – Falta la definición de la clase en tiempo de ejecución.
85. **IncompatibleClassChangeError** – Cambios incompatibles en una clase.
86. **AbstractMethodError** – El método abstracto no está implementado.
87. **InstantiationError** – Falla en la creación de instancia.
88. **IllegalAccessError** – Acceso ilegal a una clase o método.
89. **NoSuchMethodError** – No se encuentra el método.
90. **NoSuchFieldError** – No se encuentra el campo.
91. **ClassFormatError** – Formato de clase inválido.
92. **UnsupportedClassVersionError** – Clase de Java compilada con una versión no compatible.
93. **AnnotationFormatError** – Problemas con las anotaciones de Java.
94. **ExceptionInInitializerError** – Excepción en un bloque inicializador estático.
95. **ThreadDeath** – Hilo terminado forzosamente.
96. **ServiceConfigurationError** – Problema de configuración del proveedor de servicios.
97. **BootstrapMethodError** – Error en el soporte de lenguaje dinámico.
98. **VerifierError** – Falla en la verificación del bytecode.
99. **FactoryConfigurationError** – Error en la configuración de la fábrica XML.

---

### **Conclusión**
Esta es una lista exhaustiva de excepciones y errores de Java. ¡Si necesitas más detalles sobre alguna excepción en particular, házmelo saber! 🚀