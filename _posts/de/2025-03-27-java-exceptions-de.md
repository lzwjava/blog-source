---
audio: false
generated: true
lang: de
layout: post
title: Java-Ausnahmen
translated: true
type: note
---

Hier ist eine umfangreiche Liste von Java-Ausnahmen, kategorisiert in **Geprüfte Ausnahmen, Ungeprüfte Ausnahmen (Laufzeit) und Errors**.

---

## **1. Geprüfte Ausnahmen (Müssen behandelt oder mit `throws` deklariert werden)**
1.  **IOException** – Allgemeiner E/A-Fehler.
2.  **FileNotFoundException** – Datei fehlt oder ist nicht zugreifbar.
3.  **InterruptedException** – Thread-Unterbrechung ist aufgetreten.
4.  **SQLException** – Probleme im Zusammenhang mit Datenbankzugriff.
5.  **ParseException** – Fehler beim Parsen von Datenformaten.
6.  **MalformedURLException** – Ungültiges URL-Format.
7.  **ClassNotFoundException** – Klasse zur Laufzeit nicht gefunden.
8.  **InstantiationException** – Kann eine abstrakte Klasse oder ein Interface nicht instanziieren.
9.  **IllegalAccessException** – Zugriff auf eine Klasse, Methode oder ein Feld ist nicht erlaubt.
10. **NoSuchMethodException** – Methode existiert nicht.
11. **NoSuchFieldException** – Feld existiert nicht in der Klasse.
12. **TimeoutException** – Ein blockierender Vorgang hat das Zeitlimit überschritten.
13. **UnsupportedEncodingException** – Kodierung wird nicht unterstützt.
14. **URISyntaxException** – Ungültige URI-Syntax.
15. **NotBoundException** – Name nicht in einer RMI-Registry gefunden.
16. **AlreadyBoundException** – Name bereits in einer RMI-Registry gebunden.
17. **CloneNotSupportedException** – Objekt implementiert `Cloneable` nicht.
18. **DataFormatException** – Ungültiges Format in komprimierten Daten.
19. **EOFException** – Unerwartetes Dateiende erreicht.
20. **NotSerializableException** – Objekt ist nicht serialisierbar.
21. **LineUnavailableException** – Audiokanal ist nicht verfügbar.
22. **UnsupportedAudioFileException** – Nicht unterstütztes Audio-Dateiformat.
23. **PrinterException** – Fehler beim Druckvorgang.
24. **ReflectiveOperationException** – Allgemeiner Reflektionsfehler.
25. **ExecutionException** – Ausnahme während der Ausführung einer nebenläufigen Aufgabe.
26. **ScriptException** – Probleme bei der Skriptausführung.
27. **TransformerException** – Fehler bei der XML-Transformation.
28. **XPathExpressionException** – Ungültiger XPath-Ausdruck.
29. **SAXException** – Probleme beim XML-Parsing.
30. **JAXBException** – Probleme mit XML-Binding.
31. **MarshalException** – Fehler beim Marshalling von XML-Daten.
32. **UnmarshalException** – Fehler beim Unmarshalling von XML-Daten.
33. **DatatypeConfigurationException** – Ungültige XML-Datentyp-Konfiguration.
34. **GSSException** – Probleme mit GSS-Sicherheitsoperationen.
35. **KeyStoreException** – Probleme mit dem Java KeyStore.
36. **CertificateException** – Probleme bei der Zertifikatsverarbeitung.
37. **InvalidKeyException** – Ungültiger Schlüssel in kryptografischen Operationen.
38. **NoSuchAlgorithmException** – Angeforderter kryptografischer Algorithmus ist nicht verfügbar.
39. **NoSuchProviderException** – Angeforderter Sicherheits-Provider ist nicht verfügbar.
40. **UnrecoverableKeyException** – Kann einen Schlüssel nicht aus dem KeyStore wiederherstellen.
41. **IllegalBlockSizeException** – Ungültige Blockgröße für die Verschlüsselung.
42. **BadPaddingException** – Padding-Fehler in der Kryptografie.

---

## **2. Ungeprüfte Ausnahmen (Laufzeit-Ausnahmen)**
43. **NullPointerException** – Zugriff auf einen Objektverweis, der `null` ist.
44. **ArrayIndexOutOfBoundsException** – Zugriff auf einen ungültigen Array-Index.
45. **StringIndexOutOfBoundsException** – Zugriff auf einen ungültigen String-Index.
46. **ArithmeticException** – Mathematische Fehler wie Division durch Null.
47. **NumberFormatException** – Konvertierung eines ungültigen Strings in eine Zahl.
48. **ClassCastException** – Ungültige Typumwandlung.
49. **IllegalArgumentException** – Ungültiges Argument an eine Methode übergeben.
50. **IllegalStateException** – Methode wurde in einem ungültigen Zustand aufgerufen.
51. **UnsupportedOperationException** – Methode wird nicht unterstützt.
52. **ConcurrentModificationException** – Gleichzeitige Modifikation einer Collection.
53. **NoSuchElementException** – Versuch, auf ein nicht vorhandenes Element in einer Collection zuzugreifen.
54. **IllegalMonitorStateException** – Thread-Synchronisierungsfehler.
55. **NegativeArraySizeException** – Erstellen eines Arrays mit negativer Größe.
56. **StackOverflowError** – Endlosrekursion führt zu Stacküberlauf.
57. **OutOfMemoryError** – Der JVM-Speicher ist erschöpft.
58. **SecurityException** – Sicherheitsverletzung erkannt.
59. **MissingResourceException** – Ressourcenpaket nicht gefunden.
60. **EmptyStackException** – Versuch, ein Element von einem leeren Stack zu holen.
61. **TypeNotPresentException** – Typ zur Laufzeit nicht gefunden.
62. **EnumConstantNotPresentException** – Ungültige Enum-Konstante.
63. **UncheckedIOException** – Ungeprüfte Version von `IOException`.
64. **DateTimeException** – Fehler im Zusammenhang mit der Java Date-Time-API.
65. **InvalidClassException** – Probleme beim Deserialisieren einer Klasse.
66. **IllegalCharsetNameException** – Ungültiger Zeichensatzname.
67. **UnsupportedCharsetException** – Zeichensatz wird nicht unterstützt.
68. **ProviderNotFoundException** – Benötigter Service-Provider fehlt.
69. **PatternSyntaxException** – Ungültige Regex-Syntax.
70. **InvalidPathException** – Ungültiger Dateipfad.
71. **ReadOnlyBufferException** – Versuch, einen schreibgeschützten Buffer zu modifizieren.
72. **BufferUnderflowException** – Buffer-Unterlauf ist aufgetreten.
73. **BufferOverflowException** – Buffer-Überlauf ist aufgetreten.
74. **FileSystemAlreadyExistsException** – Dateisystem existiert bereits.
75. **FileSystemNotFoundException** – Dateisystem wurde nicht gefunden.
76. **ClosedWatchServiceException** – Watch Service ist geschlossen.
77. **UncheckedExecutionException** – Probleme bei der Ausführung nebenläufiger Aufgaben.

---

## **3. Errors (Schwerwiegende Probleme, die nicht abgefangen werden sollten)**
78. **StackOverflowError** – Zu viele rekursive Methodenaufrufe.
79. **OutOfMemoryError** – Der JVM-Speicher ist erschöpft.
80. **VirtualMachineError** – Kritischer JVM-Fehler.
81. **InternalError** – Unerwarteter interner JVM-Fehler.
82. **UnknownError** – Unbekannter kritischer Fehler.
83. **AssertionError** – Assertion fehlgeschlagen (mit `assert`).
84. **NoClassDefFoundError** – Klassendefinition fehlt zur Laufzeit.
85. **IncompatibleClassChangeError** – Inkompatible Änderungen an einer Klasse.
86. **AbstractMethodError** – Abstrakte Methode ist nicht implementiert.
87. **InstantiationError** – Fehler bei der Instanzerstellung.
88. **IllegalAccessError** – Unerlaubter Zugriff auf eine Klasse oder Methode.
89. **NoSuchMethodError** – Methode wurde nicht gefunden.
90. **NoSuchFieldError** – Feld wurde nicht gefunden.
91. **ClassFormatError** – Ungültiges Klassenformat.
92. **UnsupportedClassVersionError** – Java-Klasse wurde mit einer nicht unterstützten Version kompiliert.
93. **AnnotationFormatError** – Probleme mit Java-Annotationen.
94. **ExceptionInInitializerError** – Ausnahme in einem statischen Initialisiererblock.
95. **ThreadDeath** – Thread wurde zwangsweise beendet.
96. **ServiceConfigurationError** – Problem mit der Service-Provider-Konfiguration.
97. **BootstrapMethodError** – Fehler in der Unterstützung dynamischer Sprachen.
98. **VerifierError** – Fehler bei der Bytecode-Verifizierung.
99. **FactoryConfigurationError** – Fehler in der XML-Factory-Konfiguration.

---

### **Fazit**
Dies ist eine umfassende Liste von Java-Ausnahmen und Errors. Wenn Sie weitere Details zu einer bestimmten Ausnahme benötigen, lassen Sie es mich wissen! 🚀