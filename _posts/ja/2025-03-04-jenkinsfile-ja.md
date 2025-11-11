---
audio: false
generated: true
lang: ja
layout: post
title: Jenkinsfileの書き方
translated: true
type: note
---

共有ライブラリ、文字列パラメータ、try-catchブロック、nodeブロック、if文を組み込んだJenkinsfileを作成するには、以下のアプローチを使用できます。JenkinsfileはGroovyで記述され、ビルド、テスト、デプロイのプロセスを自動化するパイプラインを定義します。以下は、これらの要件を満たすスクリプト形式のJenkinsfileの完全な例です。

まず、共有ライブラリを使用するには、`@Library`アノテーションでインポートする必要があります。Jenkinsの共有ライブラリには、複数のパイプラインから呼び出せる再利用可能なコードが含まれています。例えば、共有ライブラリの名前が`my-shared-library`の場合、以下のようにJenkinsfileの先頭に記述します：

```groovy
@Library('my-shared-library') _
```

アノテーションの後のアンダースコア（`_`）は、ライブラリを適切にインポートするために必要です。

次に、文字列パラメータを定義するには、`properties`ステップを使用します。これにより、ユーザーはパイプライン実行時に文字列値を渡すことができます。以下は`MY_STRING`という名前の文字列パラメータを追加する方法です：

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])
```

`node`ブロックは、パイプラインが実行される場所（例えば利用可能な任意のエージェント）を指定します。このブロック内にパイプラインロジックを含めることができます：

```groovy
node {
    // パイプラインのステップをここに記述
}
```

潜在的なエラーを処理するには、ステップを`try-catch`ブロックで囲みます。これにより、何かが失敗した場合に例外をキャッチして適切に処理できます。さらに、`if`文を使用して文字列パラメータ（`params.MY_STRING`）の値に基づいた判断を行うことができます。

以下は、これらすべての要素を組み合わせた完全なJenkinsfileです：

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])

node {
    try {
        // 共有ライブラリの関数を呼び出す（存在すると仮定）
        myLibraryFunction()
        
        // 文字列パラメータに基づいてif文を使用
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

- **`@Library('my-shared-library') _`**: `my-shared-library`という名前の共有ライブラリをインポートします。`my-shared-library`は実際のライブラリ名に置き換えてください。関数`myLibraryFunction()`はこのライブラリで定義されていると仮定されています。
- **`properties`**: デフォルト値が`'default'`で説明文付きの文字列パラメータ`MY_STRING`を定義します。このパラメータにはパイプライン内で`params.MY_STRING`を使用してアクセスできます。
- **`node`**: パイプラインを利用可能な任意のエージェントで実行します。必要に応じて特定のエージェント（例：`node('linux')`）を指定できます。
- **`try-catch`**: `try`ブロック内のステップを実行し、`catch`ブロックで例外をキャッチします。何か問題が発生した場合はエラーメッセージを出力します。
- **`if`**: `MY_STRING`が`'test'`と等しいかどうかをチェックし、それに応じてメッセージを出力します。条件とアクションは必要に応じて変更できます。

### 注意点
- この例は、Groovy構文により柔軟性を提供するスクリプト形式のパイプラインを想定しています。宣言型パイプラインが必要な場合は、構造が若干異なります（例：Groovyコード用の`pipeline`と`script`ブロックの使用）。
- `myLibraryFunction()`の呼び出しはプレースホルダーです。共有ライブラリでこの関数が定義されていることを確認するか、実際のライブラリ関数に置き換えてください。
- 要件に応じて、ステージ（例：`stage('Build')`）やより複雑なロジックを追加することで、このJenkinsfileを拡張できます。

このJenkinsfileは、共有ライブラリ、文字列パラメータ、try-catchブロック、nodeブロック、if文というすべての要求要素を含んだ堅実な基盤を提供します。詳細（ライブラリ名、関数呼び出し、条件など）はユースケースに合わせて調整してください！