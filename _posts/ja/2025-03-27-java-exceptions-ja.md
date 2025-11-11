---
audio: false
generated: true
lang: ja
layout: post
title: Java例外処理
translated: true
type: note
---

Javaの例外を網羅的にまとめたリストです。**チェック例外、非チェック例外（ランタイム）、エラー**に分類されています。

---

## **1. チェック例外（処理または`throws`宣言が必須）**
1. **IOException** – 一般的なI/O障害  
2. **FileNotFoundException** – ファイルが存在しない、またはアクセス不可  
3. **InterruptedException** – スレッド割り込みが発生  
4. **SQLException** – データベースアクセス関連の問題  
5. **ParseException** – データ形式の解析エラー  
6. **MalformedURLException** – 無効なURL形式  
7. **ClassNotFoundException** – ランタイム時にクラスが見つからない  
8. **InstantiationException** – 抽象クラスやインターフェースをインスタンス化できない  
9. **IllegalAccessException** – クラス、メソッド、フィールドへのアクセスが許可されていない  
10. **NoSuchMethodException** – メソッドが存在しない  
11. **NoSuchFieldException** – クラス内にフィールドが存在しない  
12. **TimeoutException** – ブロッキング操作がタイムアウト  
13. **UnsupportedEncodingException** – エンコーディングがサポートされていない  
14. **URISyntaxException** – 無効なURI構文  
15. **NotBoundException** – RMIレジストリで名前が見つからない  
16. **AlreadyBoundException** – RMIレジストリで名前が既にバインドされている  
17. **CloneNotSupportedException** – オブジェクトが`Cloneable`を実装していない  
18. **DataFormatException** – 圧縮データの形式が無効  
19. **EOFException** – 予期しないファイルの終端に到達  
20. **NotSerializableException** – オブジェクトがシリアライズ可能ではない  
21. **LineUnavailableException** – オーディオラインが利用不可  
22. **UnsupportedAudioFileException** – サポートされていないオーディオファイル形式  
23. **PrinterException** – 印刷操作の失敗  
24. **ReflectiveOperationException** – 一般的なリフレクションエラー  
25. **ExecutionException** – 並行タスク実行中の例外  
26. **ScriptException** – スクリプト実行に関する問題  
27. **TransformerException** – XML変換の失敗  
28. **XPathExpressionException** – 無効なXPath式  
29. **SAXException** – XML解析に関する問題  
30. **JAXBException** – XMLバインディングに関する問題  
31. **MarshalException** – XMLデータのマーシャリング中のエラー  
32. **UnmarshalException** – XMLデータのアンマーシャリング中のエラー  
33. **DatatypeConfigurationException** – 無効なXMLデータ型設定  
34. **GSSException** – GSSセキュリティ操作に関する問題  
35. **KeyStoreException** – Java KeyStoreに関する問題  
36. **CertificateException** – 証明書処理に関する問題  
37. **InvalidKeyException** – 暗号操作で無効なキー  
38. **NoSuchAlgorithmException** – 要求された暗号アルゴリズムが利用不可  
39. **NoSuchProviderException** – 要求されたセキュリティプロバイダが利用不可  
40. **UnrecoverableKeyException** – KeyStoreからキーを回復できない  
41. **IllegalBlockSizeException** – 暗号化のブロックサイズが無効  
42. **BadPaddingException** – 暗号化のパディングエラー  

---

## **2. 非チェック例外（ランタイム例外）**
43. **NullPointerException** – `null`参照へのアクセス  
44. **ArrayIndexOutOfBoundsException** – 無効な配列インデックスへのアクセス  
45. **StringIndexOutOfBoundsException** – 無効な文字列インデックスへのアクセス  
46. **ArithmeticException** – ゼロ除算などの数学的エラー  
47. **NumberFormatException** – 無効な文字列の数値変換  
48. **ClassCastException** – 無効な型キャスト  
49. **IllegalArgumentException** – メソッドに無効な引数が渡された  
50. **IllegalStateException** – 無効な状態でメソッドが呼び出された  
51. **UnsupportedOperationException** – メソッドがサポートされていない  
52. **ConcurrentModificationException** – コレクションの同時変更  
53. **NoSuchElementException** – コレクション内の存在しない要素へのアクセス試行  
54. **IllegalMonitorStateException** – スレッド同期エラー  
55. **NegativeArraySizeException** – 負のサイズでの配列作成  
56. **StackOverflowError** – 無限再帰によるスタックオーバーフロー  
57. **OutOfMemoryError** – JVMのメモリ不足  
58. **SecurityException** – セキュリティ違反の検出  
59. **MissingResourceException** – リソースバンドルが見つからない  
60. **EmptyStackException** – 空のスタックからの要素アクセス試行  
61. **TypeNotPresentException** – ランタイム時に型が見つからない  
62. **EnumConstantNotPresentException** – 無効なenum定数  
63. **UncheckedIOException** – `IOException`の非チェック版  
64. **DateTimeException** – Javaの日時API関連のエラー  
65. **InvalidClassException** – クラスのデシリアライズに関する問題  
66. **IllegalCharsetNameException** – 無効な文字セット名  
67. **UnsupportedCharsetException** – 文字セットがサポートされていない  
68. **ProviderNotFoundException** – 必要なサービスプロバイダが存在しない  
69. **PatternSyntaxException** – 無効な正規表現構文  
70. **InvalidPathException** – 無効なファイルパス  
71. **ReadOnlyBufferException** – 読み取り専用バッファの変更試行  
72. **BufferUnderflowException** – バッファアンダーフロー発生  
73. **BufferOverflowException** – バッファオーバーフロー発生  
74. **FileSystemAlreadyExistsException** – ファイルシステムが既に存在  
75. **FileSystemNotFoundException** – ファイルシステムが見つからない  
76. **ClosedWatchServiceException** – ウォッチサービスが閉じられている  
77. **UncheckedExecutionException** – 並行タスク実行に関する問題  

---

## **3. エラー（キャッチすべきでない重大な問題）**
78. **StackOverflowError** – 過剰な再帰メソッド呼び出し  
79. **OutOfMemoryError** – JVMのメモリ不足  
80. **VirtualMachineError** – 重大なJVMエラー  
81. **InternalError** – 予期しないJVM内部エラー  
82. **UnknownError** – 未知の重大エラー  
83. **AssertionError** – `assert`によるアサーション失敗  
84. **NoClassDefFoundError** – ランタイム時にクラス定義が見つからない  
85. **IncompatibleClassChangeError** – クラスへの互換性のない変更  
86. **AbstractMethodError** – 抽象メソッドが実装されていない  
87. **InstantiationError** – インスタンス作成の失敗  
88. **IllegalAccessError** – クラスやメソッドへの不正アクセス  
89. **NoSuchMethodError** – メソッドが見つからない  
90. **NoSuchFieldError** – フィールドが見つからない  
91. **ClassFormatError** – 無効なクラス形式  
92. **UnsupportedClassVersionError** – サポートされていないバージョンでコンパイルされたJavaクラス  
93. **AnnotationFormatError** – Javaアノテーションに関する問題  
94. **ExceptionInInitializerError** – static初期化ブロックでの例外  
95. **ThreadDeath** – スレッドの強制終了  
96. **ServiceConfigurationError** – サービスプロバイダ設定の問題  
97. **BootstrapMethodError** – 動的言語サポートでのエラー  
98. **VerifierError** – バイトコード検証の失敗  
99. **FactoryConfigurationError** – XMLファクトリ設定のエラー  

---

### **まとめ**
これはJavaの例外とエラーの包括的なリストです。特定の例外について詳細が必要な場合は、お知らせください！🚀