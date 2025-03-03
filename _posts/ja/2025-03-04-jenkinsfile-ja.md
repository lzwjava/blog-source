---
audio: true
generated: true
lang: ja
layout: post
title: Jenkinsfileを書く
translated: true
---

Jenkinsfileに共有ライブラリ、文字列パラメータ、try-catchブロック、nodeブロック、if文を含めるためのアプローチを使用することができます。JenkinsfileはGroovyで書かれ、ビルド、テスト、デプロイメントプロセスを自動化するパイプラインを定義できます。以下は、これらの要件を満たすスクリプト型のJenkinsfileの完全な例です。

まず、共有ライブラリを使用するには、`@Library`アノテーションでインポートする必要があります。Jenkinsの共有ライブラリには、複数のパイプラインから呼び出すことができる再利用可能なコードが含まれています。例えば、共有ライブラリの名前が`my-shared-library`の場合、Jenkinsfileの先頭に次のように含めます：

```groovy
@Library('my-shared-library') _
```

アノテーションの後にあるアンダースコア（`_`）は、ライブラリを正しくインポートするために必要です。

次に、文字列パラメータを定義するには、`properties`ステップを使用します。これにより、パイプラインが実行される際に文字列値をパイプラインに渡すことができます。以下に、`MY_STRING`という名前の文字列パラメータを追加する方法を示します：

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])
```

`node`ブロックは、パイプラインが実行される場所を指定します。例えば、任意の利用可能なエージェント上です。このブロック内にパイプラインのロジックを含めることができます：

```groovy
node {
    // パイプラインのステップをここに含めます
}
```

潜在的なエラーを処理するには、ステップを`try-catch`ブロックでラップします。これにより、何かが失敗した場合でも、例外をキャッチして優雅に処理できます。また、`if`文を使用して、文字列パラメータ（`params.MY_STRING`）の値に基づいて決定を下すことができます。

以下は、これらのすべての要素を含む完全なJenkinsfileです：

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])

node {
    try {
        // 共有ライブラリから関数を呼び出す（存在することを前提とする）
        myLibraryFunction()

        // 文字列パラメータに基づいてif文を使用する
        if (params.MY_STRING == 'test') {
            echo "Running test"
        } else {
            echo "Not running test"
        }
    } catch (Exception e) {
        echo "An error occurred: ${e.message}"
    }
}
```

### コンポーネントの説明

- **`@Library('my-shared-library') _`**: `my-shared-library`という名前の共有ライブラリをインポートします。`my-shared-library`を実際のライブラリの名前に置き換えてください。関数`myLibraryFunction()`は、このライブラリで定義されていると仮定されています。
- **`properties`**: デフォルト値が`'default'`で説明が付いた文字列パラメータ`MY_STRING`を定義します。このパラメータは、パイプライン内で`params.MY_STRING`を使用してアクセスできます。
- **`node`**: パイプラインを任意の利用可能なエージェント上で実行します。必要に応じて特定のエージェント（例：`node('linux')`）を指定できます。
- **`try-catch`**: `try`ブロック内のステップを実行し、`catch`ブロックで例外をキャッチし、何かが間違った場合にエラーメッセージを表示します。
- **`if`**: `MY_STRING`が`'test'`と等しいかどうかを確認し、それに応じてメッセージを表示します。条件やアクションを必要に応じて変更できます。

### 注意点

- この例は、Groovy構文でより多くの柔軟性を提供するスクリプト型のパイプラインを前提としています。宣言型のパイプラインが必要な場合、構造は少し異なります（例：Groovyコード用の`pipeline`と`script`ブロック）。
- `myLibraryFunction()`の呼び出しはプレースホルダーです。共有ライブラリでこの関数が定義されていることを確認するか、ライブラリからの実際の関数に置き換えてください。
- このJenkinsfileには、ステージ（例：`stage('Build')`）やより複雑なロジックを追加することで拡張できます。

このJenkinsfileは、共有ライブラリ、文字列パラメータ、try-catchブロック、nodeブロック、if文を含む堅牢な基盤を提供します。ライブラリ名、関数呼び出し、条件などの詳細を調整して、使用例に合わせてください！