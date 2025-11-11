---
audio: false
generated: true
lang: hant
layout: post
title: JavaCC 文法定義與編譯
translated: true
type: note
---

我將創建一個全面的示範文件，展示 JavaCC（Java 編譯器編譯器）的語法定義、變數宣告和編譯範例。

```java
/* 基礎 JavaCC 語法範例 */

// 選項與解析器類別宣告
options {
    STATIC = false;  // 允許多個解析器實例
    LOOKAHEAD = 2;   // 設定預看 2 個詞彙單元
}

PARSER_BEGIN(SimpleParser)
public class SimpleParser {
    public static void main(String[] args) throws ParseException {
        SimpleParser parser = new SimpleParser(System.in);
        parser.Start();
    }
}
PARSER_END(SimpleParser)

// 詞法規格（詞彙單元）
TOKEN : {
    // 關鍵字
    < VAR: "var" >
    < INT: "int" >
    < BOOLEAN: "boolean" >
    < STRING: "string" >

    // 字面值與識別符
    < NUMBER: (["0"-"9"])+ >
    < IDENTIFIER: ["a"-"z","A"-"Z","_"] (["a"-"z","A"-"Z","0"-"9","_"])* >

    // 運算子與標點符號
    < ASSIGN: "=" >
    < SEMICOLON: ";" >
    < PLUS: "+" >
    < MINUS: "-" >
    < MULTIPLY: "*" >
    < DIVIDE: "/" >
    < LPAREN: "(" >
    < RPAREN: ")" >
}

// 跳過空白與註解
SKIP : {
    " " | "\t" | "\n" | "\r"
    | <SINGLE_LINE_COMMENT: "//" (~["\n","\r"])* ("\n"|"\r"|"\r\n")>
    | <MULTI_LINE_COMMENT: "/*" (~["*"])* "*" ("*" | (~["*","/"] (~["*"])* "*"))* "/">
}

// 語法規則
void Start() : {} {
    (Statement())* <EOF>
}

void Statement() : {} {
    VariableDeclaration()
    | Expression()
    | AssignmentStatement()
}

void VariableDeclaration() : {} {
    // 語法：var [type] [identifier] (= [expression])?;
    <VAR> Type() <IDENTIFIER> 
    ( <ASSIGN> Expression() )? 
    <SEMICOLON>
}

void Type() : {} {
    <INT> | <BOOLEAN> | <STRING>
}

void Expression() : {} {
    AdditiveExpression()
}

void AdditiveExpression() : {} {
    MultiplicativeExpression() 
    (
        <PLUS> MultiplicativeExpression()
        | <MINUS> MultiplicativeExpression()
    )*
}

void MultiplicativeExpression() : {} {
    PrimaryExpression() 
    (
        <MULTIPLY> PrimaryExpression()
        | <DIVIDE> PrimaryExpression()
    )*
}

void PrimaryExpression() : {} {
    <NUMBER>
    | <IDENTIFIER>
    | <LPAREN> Expression() <RPAREN>
}

void AssignmentStatement() : {} {
    <IDENTIFIER> <ASSIGN> Expression() <SEMICOLON>
}

```

現在我將提供關於 JavaCC 以及如何處理此語法的全面說明：

### JavaCC 概述
JavaCC（Java Compiler Compiler）是一個解析器生成器，可協助您為自訂語言或領域特定語言建立解析器和詞法分析器。

### 範例中的關鍵組件：

1. **選項區塊**
   - `STATIC = false`：允許建立多個解析器實例
   - `LOOKAHEAD = 2`：設定解析器預看 2 個詞彙單元以消除歧義

2. **詞彙單元定義**
   - 定義關鍵字、識別符、數字和運算子等詞彙單元
   - 使用正規表示式來匹配詞彙單元模式
   - 範例詞彙單元：
     - `< NUMBER: (["0"-"9"])+ >` 匹配一個或多個數字
     - `< IDENTIFIER: ["a"-"z","A"-"Z","_"] (["a"-"z","A"-"Z","0"-"9","_"])* >` 匹配變數名稱

3. **跳過規格**
   - 定義在解析過程中要忽略的內容（空白、註解）
   - 包含單行和多行註解處理

4. **語法規則**
   - 定義語言的語法和結構
   - 使用遞迴下降解析
   - 像 `VariableDeclaration()`、`Expression()` 這樣的規則定義了語言結構

### 編譯與使用步驟

1. **生成解析器**
   ```bash
   javacc SimpleParser.jj
   ```
   此命令會生成：
   - `SimpleParserConstants.java`
   - `SimpleParserTokenManager.java`
   - `ParseException.java`
   - `SimpleParser.java`

2. **編譯生成的文件**
   ```bash
   javac *.java
   ```

3. **執行解析器**
   ```bash
   java SimpleParser
   ```

### 範例輸入
```
var int x = 10;
var int y = 20;
x = x + y;
```

### 展示的功能
- 帶有可選初始化的變數宣告
- 基礎算術表達式
- 型別系統（int、boolean、string）
- 指派陳述式
- 算術運算（+、-、*、/）

### 此範例的限制
- 基礎錯誤處理
- 有限的型別檢查
- 簡化的語法

### 進階使用提示
- 使用語義動作（`{}` 中的 Java 程式碼）進行更複雜的解析
- 實作自訂錯誤恢復
- 加入型別檢查和語義分析

您希望我詳細說明 JavaCC 或此語法範例的任何特定方面嗎？