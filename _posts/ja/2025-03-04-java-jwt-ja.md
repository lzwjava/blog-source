---
audio: false
generated: true
lang: ja
layout: post
title: Java JWT ライブラリ
translated: true
---

`com.nimbusds.jwt` ライブラリを使用して、JSON Web Token (JWT) から有効期限、発行日、その他のクレームを抽出する方法について説明します。この解決策は、署名付きJWTを使用していることを前提としています。署名付きJWTは最も一般的なタイプであり、目標を達成するための明確で実践的なアプローチを提供します。

---

## 前提条件

まず、プロジェクトに Nimbus JOSE + JWT ライブラリを追加してください。Maven を使用している場合は、`pom.xml` に以下の依存関係を追加してください：

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- 最新バージョンに置き換えてください -->
</dependency>
```

最新バージョンは [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt) で確認できます。

---

## 有効期限、発行日、その他のクレームを抽出する手順

以下に、`com.nimbusds.jwt` ライブラリを使用して JWT を解析し、有効期限、発行日、その他のクレームを取得する方法を示します：

1. **JWT 文字列の解析**：`SignedJWT.parse()` メソッドを使用して JWT 文字列を `SignedJWT` オブジェクトに変換します。
2. **クレームセットの取得**：JWT からクレーム（キー値ペア）を `getJWTClaimsSet()` を使用して取得します。
3. **特定のクレームの抽出**：
   - 有効期限（`exp` クレーム）を取得するには `getExpirationTime()` を使用します。
   - 発行日（`iat` クレーム）を取得するには `getIssueTime()` を使用します。
   - 他のクレームを取得するには `getSubject()`、`getClaim()`、または他のメソッドを使用します。
4. **エラーの処理**：解析ロジックを try-catch ブロックで囲んで、潜在的な解析問題を管理します。

---

## 例コード

以下は、JWT から有効期限、発行日、その他のクレーム（例：サブジェクト）を抽出する完全な Java 例です：

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // 実際の JWT 文字列に置き換えてください
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // ステップ 1: JWT 文字列の解析
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // ステップ 2: クレームセットの取得
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // ステップ 3: 有効期限と発行日の抽出
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // 他のクレームの例

            // ステップ 4: 結果の表示
            if (expirationDate != null) {
                System.out.println("有効期限: " + expirationDate);
            } else {
                System.out.println("有効期限が設定されていません。");
            }

            if (issuedDate != null) {
                System.out.println("発行日: " + issuedDate);
            } else {
                System.out.println("発行日が設定されていません。");
            }

            if (subject != null) {
                System.out.println("サブジェクト: " + subject);
            } else {
                System.out.println("サブジェクトが設定されていません。");
            }

        } catch (ParseException e) {
            System.out.println("無効な JWT: " + e.getMessage());
        }
    }
}
```

---

## コードの説明

### 1. **インポート**
- `SignedJWT`：署名付き JWT を表し、解析および処理するためのメソッドを提供します。
- `JWTClaimsSet`：JWT ペイロードからのクレームを含みます。
- `ParseException`：JWT 文字列が不正または解析できない場合にスローされます。
- `Date`：有効期限と発行時刻を表すために使用されます。

### 2. **JWT の解析**
- `SignedJWT.parse(jwtString)` メソッドは、JWT 文字列（例：`header.payload.signature`）を受け取り、`SignedJWT` オブジェクトを返します。JWT が無効の場合は `ParseException` をスローします。

### 3. **クレームへのアクセス**
- `signedJWT.getJWTClaimsSet()` は、JWT ペイロードからすべてのクレームを含むクレームセットを取得します。

### 4. **特定のクレームの抽出**
- **`getExpirationTime()`**：`exp` クレームを `Date` オブジェクトとして返します（存在しない場合は `null`）。これはトークンの有効期限を示します。
- **`getIssueTime()`**：`iat` クレームを `Date` オブジェクトとして返します（存在しない場合は `null`）。これはトークンの発行時刻を示します。
- **`getSubject()`**：`sub` クレームを `String` として返します（存在しない場合は `null`）。これは他の標準クレームの例です。カスタムクレームを取得するには `getClaim("key")` を使用して `Object` として取得し、適切な型（例：`String`、`Integer`）にキャストします。

### 5. **エラー処理**
- try-catch ブロックは、JWT が不正または無効の場合に、プログラムがエラーを優雅に処理するようにします。

---

## 注意点

- **署名付き vs. 署名なし JWT**：この例では署名付きトークン用の `SignedJWT` を使用しています。署名なしの JWT を持っている場合は、`PlainJWT.parse(jwtString)` を使用してください。より一般的なアプローチとして、`JWTParser.parse(jwtString)` を使用し、型（`SignedJWT`、`PlainJWT` など）を `instanceof` を使用して確認することもできます。
- **署名の検証**：このコードは JWT の署名を検証しません。本番環境では、`signedJWT.verify(verifier)` を使用して適切なキーで署名を検証し、トークンの真正性を確認する必要があります。
- **null チェック**：クレームを取得する際には常に `null` を確認してください。クレームはオプションであり、すべての JWT に存在するわけではありません。
- **カスタムクレーム**：非標準クレームにアクセスするには、`claimsSet.getClaim("claimName")` を使用して `Object` を取得し、適切な型（例：`String`、`Integer`）にキャストします。

---

## 例出力

上記の例の JWT 文字列に対して：
```
有効期限: 2018年1月17日 19:52:02 UTC
発行日: 2018年1月17日 19:50:22 UTC
サブジェクト: 1234567890
```

---

このアプローチは、`com.nimbusds.jwt` ライブラリを使用して JWT から有効期限、発行日、その他のクレームを抽出するための簡単で効果的な方法を提供します。`jwtString` を自分のトークンに置き換え、コードを特定のニーズに合わせて適応させてください！