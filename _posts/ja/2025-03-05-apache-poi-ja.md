---
audio: false
generated: true
lang: ja
layout: post
title: Apache POI ライブラリ
translated: true
---

クエリ "how to use com.apache.poi." にタイポがあるようです。Javaでは、Apache POIのパッケージ名は `org.apache.poi` で始まりますが、`com.apache.poi` ではありません。Apacheプロジェクトは通常 `org` ドメインを使用します。`org.apache.poi` を指していると仮定します。これは、Excel、Word、PowerPointなどのMicrosoft Officeファイル形式を操作するための人気のあるJavaライブラリです。以下は、その使用方法についてのガイドです。特にExcelファイルの処理に焦点を当てています。

---

### **Apache POIとは？**
Apache POI（Poor Obfuscation Implementation）は、プログラム的にMicrosoft Officeドキュメントを読み取り、書き込み、操作するためのJavaライブラリです。Excelファイル（.xlsおよび.xlsx）で広く使用されますが、WordおよびPowerPoint形式もサポートしています。

---

### **ステップ1: Apache POIをプロジェクトに追加する**
Apache POIを使用するには、Javaプロジェクトに含める必要があります。**Maven**を使用している場合、`pom.xml` ファイルに以下の依存関係を追加します。

- 基本的なExcelサポート（.xlsおよび.xlsxの両方）:
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

**注意**: 最新バージョンについては、[Apache POIウェブサイト](https://poi.apache.org/)またはMaven Centralを参照してください。

Mavenを使用していない場合は、Apache POIウェブサイトからJARファイルをダウンロードし、プロジェクトのクラスパスに追加してください。

---

### **ステップ2: Excelファイルの基本的な使用方法**
Apache POIは、Excelのワークブック、シート、行、セルを操作するためのクラスを提供します。以下に、Excelファイルの読み取りと書き込みの基本的な方法を示します。

#### **Excelファイルの読み取り**
Excelファイルを読み取るには、`WorkbookFactory`を使用して`Workbook`インスタンスを作成し、シート、行、セルをナビゲートします。

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
            // すべてのシートをループ
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("Sheet: " + sheet.getSheetName());
                // 行とセルをループ
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
- `WorkbookFactory.create()`は、.xls（HSSF）および.xlsx（XSSF）の両方のファイルを処理します。
- `DataFormatter`は、異なるセルタイプ（文字列、数値、日付）を文字列としてフォーマットすることで、処理を簡素化します。
- `try-with-resources`を使用して、ファイルとワークブックを自動的に閉じます。

#### **異なるセルタイプの処理**
セルの値をそのタイプ（例：文字列、数値、日付）に基づいて処理する必要がある場合は、セルのタイプを明示的に確認します：

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
        System.out.println("不明なセルタイプ");
}
```

#### **Excelファイルへの書き込み**
Excelファイルを作成または変更するには、ワークブックを作成し、シート、行、セルを追加し、保存します。

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
- .xlsxファイル用に`XSSFWorkbook`を使用し、.xlsファイル用に`HSSFWorkbook`を使用します。
- `workbook.write()`を呼び出してファイルを保存します。

---

### **ステップ3: 主要なクラスと概念**
Excelで使用する主要なクラスは以下の通りです：
- **`Workbook`**: Excelファイル全体を表します（.xlsx用に`XSSFWorkbook`、.xls用に`HSSFWorkbook`）。
- **`Sheet`**: ワークブック内のシート。
- **`Row`**: シート内の行。
- **`Cell`**: 行内のセル。
- **`WorkbookFactory`**: ファイルまたはストリームからワークブックを作成し、両方のファイルタイプを処理します。
- **`DataFormatter`**: セル値を文字列としてフォーマットします。
- **`DateUtil`**: 日付形式の数値セルを識別および処理するのに役立ちます。

他の形式：
- **Word**: `.docx`用に`XWPFDocument`または`.doc`用に`HWPFDocument`を使用します。
- **PowerPoint**: `.pptx`用に`XMLSlideShow`または`.ppt`用に`HSLFSlideShow`を使用します。

---

### **ステップ4: ヒントとベストプラクティス**
- **リソース管理**: `try-with-resources`を使用してファイルとワークブックを閉じ、メモリリークを防ぎます。
- **エラーハンドリング**: ファイル操作には`IOException`をキャッチし、インデックスでアクセスする際に行またはセルがnullであることを確認します（例：`sheet.getRow(i)`はnullを返すことがあります）。
- **大規模なファイル**: 大規模なExcelファイルの場合、メモリ使用量を減らすためにストリーミングAPI（書き込み用に`SXSSFWorkbook`、読み取り用に`XSSFSheetXMLHandler`）を検討してください。
- **互換性**: POIは最新のOffice形式のすべての機能をサポートしていない場合があります。詳細については、[公式ドキュメント](https://poi.apache.org/)を参照してください。

---

### **まとめ**
`org.apache.poi`を使用するには：
1. ライブラリをプロジェクトに追加します（例：Maven経由）。
2. `WorkbookFactory`を使用して既存のファイルを読み取り、新しいワークブックを`XSSFWorkbook`/`HSSFWorkbook`で作成します。
3. `Sheet`、`Row`、`Cell`オブジェクトを使用してデータにアクセスおよび操作します。
4. ファイルに書き込んで変更を保存します。
5. 例外を適切に処理し、リソースを閉じます。

これは、Excelファイルに焦点を当てたApache POIの基本的な使用方法です。特定のタスク（例：WordまたはPowerPointの操作）があれば、お知らせください。さらに詳細な説明を提供できます！