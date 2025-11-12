---
audio: false
generated: true
lang: ja
layout: post
title: Apache POIライブラリ
translated: true
type: note
---

クエリ「how to use com.apache.poi.」にタイポがあるようです。Javaでは、Apache POIのパッケージ名は`com.apache.poi`ではなく`org.apache.poi`で始まります。Apacheプロジェクトは通常`org`ドメインを使用するためです。ここでは`org.apache.poi`を意味していると仮定して説明します。これはExcel、Word、PowerPointなどのMicrosoft Officeファイル形式を操作するための人気のあるJavaライブラリです。以下では、最も一般的な使用例であるExcelファイルの操作に焦点を当てたガイドを提供します。

---

### **Apache POIとは？**
Apache POI（Poor Obfuscation Implementation）は、Microsoft Officeドキュメントをプログラムで読み書きおよび操作できるようにするJavaライブラリです。Excelファイル（.xlsおよび.xlsx）で広く使用されていますが、WordおよびPowerPoint形式もサポートしています。

---

### **ステップ1: プロジェクトにApache POIを追加する**
Apache POIを使用するには、Javaプロジェクトに含める必要があります。**Maven**を使用している場合は、`pom.xml`ファイルに以下の依存関係を追加してください：

- 基本的なExcelサポート（.xlsと.xlsxの両方）の場合：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- .xlsxファイル専用（追加のOOXMLサポートが必要）：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**注意**: 最新バージョンについては[Apache POIウェブサイト](https://poi.apache.org/)またはMaven Centralを確認してください。

Mavenを使用していない場合は、Apache POIのウェブサイトからJARファイルをダウンロードし、プロジェクトのクラスパスに追加してください。

---

### **ステップ2: Excelファイルの基本的な使用方法**
Apache POIは、Excelワークブック、シート、行、セルを操作するためのクラスを提供します。以下は、Excelファイルの読み書きを始める方法です。

#### **Excelファイルの読み取り**
Excelファイルを読み取るには、`WorkbookFactory`を使用して`Workbook`インスタンスを作成し、シート、行、セルを順に処理します。

以下は、Excelファイルの内容を読み取って表示する簡単な例です：

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // Excelファイルへのパス
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // すべてのシートをループ処理
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("Sheet: " + sheet.getSheetName());
                // 行とセルをループ処理
                for (Row row : sheet) {
                    for (Cell cell : row) {
                        DataFormatter formatter = new DataFormatter();
                        String value = formatter.formatCellValue(cell);
                        System.out.print(value + "\t");
                    }
                    System.out.println(); // 各行の後に改行
                }
                System.out.println(); // 各シートの後に改行
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**重要なポイント**:
- `WorkbookFactory.create()`は.xls（HSSF）と.xlsx（XSSF）の両方のファイルで動作します。
- `DataFormatter`は、異なるセルタイプ（文字列、数値、日付）を文字列としてフォーマットすることで、処理を簡素化します。
- ファイルとワークブックを自動的に閉じるには`try-with-resources`を使用します。

#### **異なるセルタイプの処理**
セルのタイプ（例：文字列、数値、日付）に基づいてセルの値を処理する必要がある場合は、セルのタイプを明示的にチェックします：

```java
Cell cell = row.getCell(0); // 行の最初のセルを取得
switch (cell.getCellType()) {
    case STRING:
        System.out.println(cell.getStringCellValue());
        break;
    case NUMERIC:
        if (DateUtil.isCellDateFormatted(cell)) {
            System.out.println(cell.getDateCellValue());
        } else {
            System.out.println(cell.getNumericCellValue());
        }
        break;
    case BOOLEAN:
        System.out.println(cell.getBooleanCellValue());
        break;
    default:
        System.out.println("Unknown cell type");
}
```

#### **Excelファイルへの書き込み**
Excelファイルを作成または変更するには、ワークブックを作成し、シート、行、セルを追加してから保存します。

以下は、新しい.xlsxファイルを作成する例です：

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelWriter {
    public static void main(String[] args) {
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("MySheet");
            Row row = sheet.createRow(0); // 最初の行
            Cell cell = row.createCell(0); // 最初のセル
            cell.setCellValue("Hello, POI!");

            // ファイルに書き込み
            try (FileOutputStream fos = new FileOutputStream("output.xlsx")) {
                workbook.write(fos);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**重要なポイント**:
- .xlsxファイルには`XSSFWorkbook`を、.xlsファイルには`HSSFWorkbook`を使用します。
- ファイルを保存するには`workbook.write()`を呼び出します。

---

### **ステップ3: 主要なクラスと概念**
Excel用のApache POIで使用する主なクラスは以下のとおりです：
- **`Workbook`**: Excelファイル全体を表します（.xlsxには`XSSFWorkbook`、.xlsには`HSSFWorkbook`）。
- **`Sheet`**: ワークブック内の単一のシート。
- **`Row`**: シート内の行。
- **`Cell`**: 行内のセル。
- **`WorkbookFactory`**: ファイルまたはストリームからワークブックを作成し、両方のファイルタイプを処理します。
- **`DataFormatter`**: セル値を文字列としてフォーマットします。
- **`DateUtil`**: 日付フォーマットされた数値セルの識別と処理を支援します。

その他の形式の場合：
- **Word**: `.docx`には`XWPFDocument`、`.doc`には`HWPFDocument`を使用します。
- **PowerPoint**: `.pptx`には`XMLSlideShow`、`.ppt`には`HSLFSlideShow`を使用します。

---

### **ステップ4: ヒントとベストプラクティス**
- **リソース管理**: メモリリークを防ぐために、常に`try-with-resources`を使用してファイルとワークブックを閉じてください。
- **エラーハンドリング**: ファイル操作には`IOException`をキャッチし、インデックスでアクセスする際はnullの行/セルをチェックしてください（例：`sheet.getRow(i)`はnullを返す可能性があります）。
- **大きなファイル**: 大きなExcelファイルの場合は、メモリ使用量を減らすためにストリーミングAPI（書き込み用の`SXSSFWorkbook`、読み取り用の`XSSFSheetXMLHandler`）を検討してください。
- **互換性**: POIは最新のOffice形式のすべての機能をサポートしていない可能性があります。詳細については[公式ドキュメント](https://poi.apache.org/)を確認してください。

---

### **まとめ**
`org.apache.poi`を使用するには：
1. ライブラリをプロジェクトに追加します（例：Maven経由）。
2. 既存のファイルを読み取るには`WorkbookFactory`を、新しいワークブックを作成するには`XSSFWorkbook`/`HSSFWorkbook`を使用します。
3. `Sheet`、`Row`、`Cell`オブジェクトを介してデータにアクセスおよび操作します。
4. ファイルに書き込んで変更を保存します。
5. 例外を処理し、リソースを適切に閉じます。

これで、Excelファイルに焦点を当てたApache POIの基本的な使用方法をカバーしました。特定のタスク（例：WordやPowerPointの操作）をお考えの場合は、説明をさらに調整できますのでお知らせください！