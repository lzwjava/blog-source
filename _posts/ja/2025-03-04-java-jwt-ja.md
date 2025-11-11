---
audio: false
generated: true
lang: ja
layout: post
title: Java JWTライブラリ
translated: true
type: note
---

Javaで`com.nimbusds.jwt`ライブラリを使用してJSON Web Token（JWT）から有効期限、発行日時、その他のクレーム情報を抽出するには、以下の手順に従ってください。このソリューションは、最も一般的なタイプである署名付きJWTを扱うことを想定しており、目的を達成するための明確で実践的なアプローチを提供します。

---

## 前提条件

まず、プロジェクトにNimbus JOSE + JWTライブラリが追加されていることを確認してください。Mavenを使用している場合は、`pom.xml`に以下の依存関係を追加します：

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- 最新バージョンに置き換えてください -->
</dependency>
```

最新バージョンは[Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt)で確認できます。

---

## 有効期限、発行日時、その他のクレームを抽出する手順

`com.nimbusds.jwt`ライブラリを使用してJWTを解析し、有効期限、発行日時、追加のクレームを取得する方法は以下の通りです：

1. **JWT文字列の解析**: `SignedJWT.parse()`メソッドを使用してJWT文字列を`SignedJWT`オブジェクトに変換します。
2. **クレームセットの取得**: `getJWTClaimsSet()`を使用してJWTからクレーム（キーと値のペア）にアクセスします。
3. **特定のクレームの抽出**:
   - 有効期限（`exp`クレーム）には`getExpirationTime()`を使用します。
   - 発行日時（`iat`クレーム）には`getIssueTime()`を使用します。
   - 追加のクレームには`getSubject()`、`getClaim()`、またはその他のメソッドを使用します。
4. **エラー処理**: 解析ロジックをtry-catchブロックで囲み、潜在的な解析の問題を管理します。

---

## コード例

以下は、JWTから有効期限、発行日時、および追加のクレーム（例：サブジェクト）を抽出する完全なJavaの例です：

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // これを実際のJWT文字列に置き換えてください
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // ステップ1: JWT文字列を解析
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // ステップ2: クレームセットを取得
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // ステップ3: 有効期限と発行日時を抽出
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // 他のクレームの例

            // ステップ4: 結果を表示
            if (expirationDate != null) {
                System.out.println("Expiration date: " + expirationDate);
            } else {
                System.out.println("No expiration date set.");
            }

            if (issuedDate != null) {
                System.out.println("Issued date: " + issuedDate);
            } else {
                System.out.println("No issued date set.");
            }

            if (subject != null) {
                System.out.println("Subject: " + subject);
            } else {
                System.out.println("No subject set.");
            }

        } catch (ParseException e) {
            System.out.println("Invalid JWT: " + e.getMessage());
        }
    }
}
```

---

## コードの説明

### 1. **インポート**
- `SignedJWT`: 署名付きJWTを表し、解析および処理するメソッドを提供します。
- `JWTClaimsSet`: JWTペイロードからのクレームを含みます。
- `ParseException`: JWT文字列が不正な形式である場合や解析できない場合にスローされます。
- `Date`: 有効期限と発行日時を表すために使用されます。

### 2. **JWTの解析**
- `SignedJWT.parse(jwtString)`メソッドはJWT文字列（例：`header.payload.signature`）を受け取り、`SignedJWT`オブジェクトを返します。JWTが無効な場合、`ParseException`をスローします。

### 3. **クレームへのアクセス**
- `signedJWT.getJWTClaimsSet()`は、JWTのペイロードからのすべてのクレームを保持するクレームセットを取得します。

### 4. **特定のクレームの抽出**
- **`getExpirationTime()`**: `exp`クレームを`Date`オブジェクトとして返します（存在しない場合は`null`）。これはトークンの有効期限が切れる時点を表します。
- **`getIssueTime()`**: `iat`クレームを`Date`オブジェクトとして返します（存在しない場合は`null`）。これはトークンが発行された時点を示します。
- **`getSubject()`**: `sub`クレームを`String`として返します（存在しない場合は`null`）。これは他の標準クレームの例です。カスタムクレームを取得するには、`getClaim("key")`を使用して`Object`として取得することもできます。

### 5. **エラー処理**
- try-catchブロックにより、JWTが不正な形式または無効な場合に、プログラムがエラーメッセージを表示して適切に処理します。

---

## 注意点

- **署名付きと署名なしJWT**: この例では署名付きトークンに`SignedJWT`を使用しています。署名なしJWTの場合は、代わりに`PlainJWT.parse(jwtString)`を使用してください。より汎用的なアプローチでは、`JWTParser.parse(jwtString)`を使用し、その後`instanceof`を使用してタイプ（`SignedJWT`、`PlainJWT`など）を確認できます。
- **署名検証**: このコードはJWTの署名を検証しません。本番環境では、適切なキーを使用して`signedJWT.verify(verifier)`で署名を検証し、トークンの信頼性を確保する必要があります。
- **nullチェック**: クレームはオプションであり、すべてのJWTに存在するとは限らないため、クレームを取得する際は常に`null`をチェックしてください。
- **カスタムクレーム**: 非標準のクレームにアクセスするには、`claimsSet.getClaim("claimName")`を使用します。これは`Object`を返すので、適切なタイプ（例：`String`、`Integer`）にキャストできます。

---

## 出力例

上記のJWT文字列の例の場合：
```
Expiration date: Wed Jan 17 19:52:02 UTC 2018
Issued date: Wed Jan 17 19:50:22 UTC 2018
Subject: 1234567890
```

---

このアプローチは、`com.nimbusds.jwt`ライブラリを使用してJWTから有効期限、発行日時、その他のクレームを抽出するためのシンプルで効果的な方法を提供します。`jwtString`を自身のトークンに置き換え、コードを特定のニーズに合わせて調整してください！