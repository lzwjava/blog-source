---
audio: false
generated: true
lang: hant
layout: post
title: Java 異常處理
translated: true
type: note
---

以下是一份詳盡的 Java 異常清單，分為**受檢異常（Checked Exceptions）、非受檢異常（Unchecked Exceptions / Runtime）及錯誤（Errors）**三大類。

---

## **1. 受檢異常（必須使用 `throws` 聲明或處理）**
1. **IOException** – 一般 I/O 故障  
2. **FileNotFoundException** – 檔案缺失或無法存取  
3. **InterruptedException** – 執行緒被中斷  
4. **SQLException** – 資料庫存取相關問題  
5. **ParseException** – 解析資料格式時出錯  
6. **MalformedURLException** – 無效的 URL 格式  
7. **ClassNotFoundException** – 執行時找不到類別  
8. **InstantiationException** – 無法實例化抽象類別或介面  
9. **IllegalAccessException** – 無權存取類別、方法或欄位  
10. **NoSuchMethodException** – 方法不存在  
11. **NoSuchFieldException** – 類別中不存在該欄位  
12. **TimeoutException** – 阻塞操作超時  
13. **UnsupportedEncodingException** – 不支援的編碼格式  
14. **URISyntaxException** – 無效的 URI 語法  
15. **NotBoundException** – RMI 註冊表中找不到名稱  
16. **AlreadyBoundException** – 名稱已綁定至 RMI 註冊表  
17. **CloneNotSupportedException** – 物件未實作 `Cloneable`  
18. **DataFormatException** – 壓縮資料格式錯誤  
19. **EOFException** – 意外到達檔案結尾  
20. **NotSerializableException** – 物件不可序列化  
21. **LineUnavailableException** – 音訊線路不可用  
22. **UnsupportedAudioFileException** – 不支援的音訊檔案格式  
23. **PrinterException** – 列印操作失敗  
24. **ReflectiveOperationException** – 反射操作通用錯誤  
25. **ExecutionException** – 並行任務執行期間發生異常  
26. **ScriptException** – 執行指令碼時發生問題  
27. **TransformerException** – XML 轉換失敗  
28. **XPathExpressionException** – 無效的 XPath 表達式  
29. **SAXException** – XML 解析問題  
30. **JAXBException** – XML 綁定問題  
31. **MarshalException** – 序列化 XML 資料時出錯  
32. **UnmarshalException** – 反序列化 XML 資料時出錯  
33. **DatatypeConfigurationException** – 無效的 XML 資料類型配置  
34. **GSSException** – GSS 安全操作問題  
35. **KeyStoreException** – Java KeyStore 相關問題  
36. **CertificateException** – 憑證處理問題  
37. **InvalidKeyException** – 加密操作中使用無效金鑰  
38. **NoSuchAlgorithmException** – 找不到要求的加密演算法  
39. **NoSuchProviderException** – 找不到要求的安全供應商  
40. **UnrecoverableKeyException** – 無法從 KeyStore 恢復金鑰  
41. **IllegalBlockSizeException** – 加密區塊大小無效  
42. **BadPaddingException** – 加密填充錯誤  

---

## **2. 非受檢異常（執行時異常）**
43. **NullPointerException** – 存取 `null` 物件參考  
44. **ArrayIndexOutOfBoundsException** – 存取無效的陣列索引  
45. **StringIndexOutOfBoundsException** – 存取無效的字串索引  
46. **ArithmeticException** – 數學錯誤（如除以零）  
47. **NumberFormatException** – 將無效字串轉換為數字  
48. **ClassCastException** – 無效的型別轉換  
49. **IllegalArgumentException** – 傳遞無效參數至方法  
50. **IllegalStateException** – 在無效狀態下呼叫方法  
51. **UnsupportedOperationException** – 不支援該方法  
52. **ConcurrentModificationException** – 並行修改集合內容  
53. **NoSuchElementException** – 嘗試存取集合中不存在的元素  
54. **IllegalMonitorStateException** – 執行緒同步錯誤  
55. **NegativeArraySizeException** – 建立負數大小的陣列  
56. **StackOverflowError** – 無限遞歸導致堆疊溢位  
57. **OutOfMemoryError** – JVM 記憶體耗盡  
58. **SecurityException** – 偵測到安全性違規  
59. **MissingResourceException** – 找不到資源包  
60. **EmptyStackException** – 嘗試從空堆疊存取元素  
61. **TypeNotPresentException** – 執行時找不到型別  
62. **EnumConstantNotPresentException** – 無效的枚舉常量  
63. **UncheckedIOException** – `IOException` 的非受檢版本  
64. **DateTimeException** – Java 日期時間 API 相關錯誤  
65. **InvalidClassException** – 反序列化類別時發生問題  
66. **IllegalCharsetNameException** – 無效的字元集名稱  
67. **UnsupportedCharsetException** – 不支援的字元集  
68. **ProviderNotFoundException** – 缺少所需的服務供應商  
69. **PatternSyntaxException** – 無效的正則表達式語法  
70. **InvalidPathException** – 無效的檔案路徑  
71. **ReadOnlyBufferException** – 嘗試修改唯讀緩衝區  
72. **BufferUnderflowException** – 緩衝區下溢  
73. **BufferOverflowException** – 緩衝區上溢  
74. **FileSystemAlreadyExistsException** – 檔案系統已存在  
75. **FileSystemNotFoundException** – 找不到檔案系統  
76. **ClosedWatchServiceException** – 監看服務已關閉  
77. **UncheckedExecutionException** – 並行任務執行問題  

---

## **3. 錯誤（不應捕獲的嚴重問題）**
78. **StackOverflowError** – 過多的遞歸方法呼叫  
79. **OutOfMemoryError** – JVM 記憶體耗盡  
80. **VirtualMachineError** – 嚴重的 JVM 錯誤  
81. **InternalError** – 未預期的 JVM 內部錯誤  
82. **UnknownError** – 未知的嚴重錯誤  
83. **AssertionError** – 使用 `assert` 的斷言失敗  
84. **NoClassDefFoundError** – 執行時缺少類別定義  
85. **IncompatibleClassChangeError** – 類別發生不相容的變更  
86. **AbstractMethodError** – 抽象方法未實作  
87. **InstantiationError** – 實例建立失敗  
88. **IllegalAccessError** – 無權存取類別或方法  
89. **NoSuchMethodError** – 找不到方法  
90. **NoSuchFieldError** – 找不到欄位  
91. **ClassFormatError** – 無效的類別格式  
92. **UnsupportedClassVersionError** – 使用不支援的 Java 版本編譯類別  
93. **AnnotationFormatError** – Java 註解相關問題  
94. **ExceptionInInitializerError** – 靜態初始化區塊中發生異常  
95. **ThreadDeath** – 執行緒被強制終止  
96. **ServiceConfigurationError** – 服務供應商配置問題  
97. **BootstrapMethodError** – 動態語言支援錯誤  
98. **VerifierError** – 位元組碼驗證失敗  
99. **FactoryConfigurationError** – XML 工廠配置錯誤  

---

### **總結**
這是一份完整的 Java 異常與錯誤清單。如需任何特定異常的詳細說明，歡迎隨時提問！🚀